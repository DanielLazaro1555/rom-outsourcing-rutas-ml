import pandas as pd

from models import PDV, db


REQUIRED_COLUMNS = {"Punto de Venta", "Latitud", "Longitud"}
OPTIONAL_COLUMNS = {
    "Codigo Punto de Venta",
    "Empresas",
    "Canal",
    "Zona",
    "Distrito",
    "Prioridad",
}


def _normalize_text(value):
    if pd.isna(value):
        return ""
    text = str(value).strip()
    return " ".join(text.split())


def _parse_coordinate(value):
    if pd.isna(value):
        return None
    text = str(value).strip().replace(",", ".")
    if not text:
        return None
    return float(text)


def _parse_priority(value):
    if pd.isna(value) or value == "":
        return "media"

    normalized = _normalize_text(value).lower()
    valid = {"alta", "media", "baja"}
    return normalized if normalized in valid else "media"


def _build_pdv_payload(row, stats=None):
    nombre = _normalize_text(row.get("Punto de Venta"))
    codigo = _normalize_text(row.get("Codigo Punto de Venta"))
    empresa = _normalize_text(row.get("Empresas"))
    canal = _normalize_text(row.get("Canal"))
    zona = _normalize_text(row.get("Zona")).upper()
    distrito = _normalize_text(row.get("Distrito")).upper()
    prioridad = _parse_priority(row.get("Prioridad"))

    lat = _parse_coordinate(row.get("Latitud"))
    lon = _parse_coordinate(row.get("Longitud"))

    if any(marker in field for marker in ("�", "?") for field in (nombre, empresa, distrito)):
        if stats is not None:
            stats["encoding_warnings"] += 1

    activo = zona != "FUERA_DE_RUTA"
    if not activo and stats is not None:
        stats["inactive_fuera_de_ruta"] += 1

    direccion_parts = [nombre]
    location_parts = [part for part in (distrito, zona) if part]
    if location_parts:
        direccion_parts.append(", ".join(location_parts))
    direccion = " - ".join(direccion_parts)

    return {
        "codigo_pdv": codigo or None,
        "nombre": nombre,
        "empresa": empresa or None,
        "canal": canal or None,
        "zona": zona or None,
        "distrito": distrito or None,
        "latitud": lat,
        "longitud": lon,
        "direccion": direccion,
        "prioridad": prioridad,
        "activo": activo,
    }


def load_pdv_dataframe(file_or_path, filename=""):
    source_name = (filename or getattr(file_or_path, "name", "") or "").lower()

    if source_name.endswith(".csv"):
        df = pd.read_csv(file_or_path, sep=";", encoding="latin1")
    elif source_name.endswith((".xls", ".xlsx")):
        df = pd.read_excel(file_or_path)
    else:
        raise ValueError("Formato no soportado. Suba un archivo CSV o Excel.")

    missing_columns = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing_columns:
        missing = ", ".join(missing_columns)
        raise ValueError(f"Faltan columnas obligatorias en el archivo: {missing}")

    for column in OPTIONAL_COLUMNS:
        if column not in df.columns:
            df[column] = ""

    return df


def import_pdv_dataframe(df):
    stats = {
        "rows_read": len(df),
        "imported": 0,
        "duplicates_in_file": 0,
        "duplicates_in_db": 0,
        "invalid_rows": 0,
        "inactive_fuera_de_ruta": 0,
        "encoding_warnings": 0,
    }

    seen_codes = set()
    seen_keys = set()

    for _, row in df.iterrows():
        try:
            payload = _build_pdv_payload(row, stats=stats)
        except ValueError:
            stats["invalid_rows"] += 1
            continue

        nombre = payload["nombre"]
        codigo = payload["codigo_pdv"] or ""
        lat = payload["latitud"]
        lon = payload["longitud"]

        if not nombre or lat is None or lon is None:
            stats["invalid_rows"] += 1
            continue

        duplicate_key = (
            nombre.casefold(),
            round(lat, 6),
            round(lon, 6),
        )

        if codigo:
            if codigo in seen_codes:
                stats["duplicates_in_file"] += 1
                continue
            seen_codes.add(codigo)
        elif duplicate_key in seen_keys:
            stats["duplicates_in_file"] += 1
            continue

        seen_keys.add(duplicate_key)

        existing = None
        if codigo:
            existing = PDV.query.filter_by(codigo_pdv=codigo).first()
        if existing is None:
            existing = PDV.query.filter_by(nombre=nombre, latitud=lat, longitud=lon).first()
        if existing is not None:
            stats["duplicates_in_db"] += 1
            continue

        pdv = PDV(**payload)
        db.session.add(pdv)
        stats["imported"] += 1

    return stats


def sync_pdv_dataframe(df):
    stats = {
        "rows_read": len(df),
        "inserted": 0,
        "updated": 0,
        "unchanged": 0,
        "duplicates_in_file": 0,
        "invalid_rows": 0,
        "inactive_fuera_de_ruta": 0,
        "encoding_warnings": 0,
    }

    seen_codes = set()
    seen_keys = set()

    for _, row in df.iterrows():
        try:
            payload = _build_pdv_payload(row, stats=stats)
        except ValueError:
            stats["invalid_rows"] += 1
            continue

        nombre = payload["nombre"]
        codigo = payload["codigo_pdv"] or ""
        lat = payload["latitud"]
        lon = payload["longitud"]

        if not nombre or lat is None or lon is None:
            stats["invalid_rows"] += 1
            continue

        duplicate_key = (
            nombre.casefold(),
            round(lat, 6),
            round(lon, 6),
        )

        if codigo:
            if codigo in seen_codes:
                stats["duplicates_in_file"] += 1
                continue
            seen_codes.add(codigo)
        elif duplicate_key in seen_keys:
            stats["duplicates_in_file"] += 1
            continue

        seen_keys.add(duplicate_key)

        existing = None
        if codigo:
            existing = PDV.query.filter_by(codigo_pdv=codigo).first()
        if existing is None:
            existing = PDV.query.filter_by(nombre=nombre, latitud=lat, longitud=lon).first()

        if existing is None:
            db.session.add(PDV(**payload))
            stats["inserted"] += 1
            continue

        changed = False
        for field, value in payload.items():
            if getattr(existing, field) != value:
                setattr(existing, field, value)
                changed = True

        if changed:
            stats["updated"] += 1
        else:
            stats["unchanged"] += 1

    return stats
