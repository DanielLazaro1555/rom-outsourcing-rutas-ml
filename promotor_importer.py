import secrets

import pandas as pd

from models import Promotor, Usuario, db


REQUIRED_COLUMNS = {"Nombre"}
OPTIONAL_COLUMNS = {"Email", "Zona", "Cuenta", "Activo", "Capacidad Diaria"}


def _normalize_text(value):
    if pd.isna(value):
        return ""
    text = str(value).strip()
    return " ".join(text.split())


def _parse_bool(value):
    if pd.isna(value) or value == "":
        return True
    text = str(value).strip().lower()
    return text not in {"0", "false", "no", "inactivo"}


def _parse_capacity(value):
    if pd.isna(value) or value == "":
        return 5
    capacity = int(float(value))
    if capacity < 1:
        return 1
    return capacity


def load_promotor_dataframe(file_or_path, filename=""):
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


def sync_promotor_dataframe(df):
    stats = {
        "rows_read": len(df),
        "inserted": 0,
        "updated": 0,
        "unchanged": 0,
        "duplicates_in_file": 0,
        "invalid_rows": 0,
        "users_created": 0,
        "users_linked": 0,
    }

    seen_keys = set()

    for _, row in df.iterrows():
        nombre = _normalize_text(row.get("Nombre"))
        email = _normalize_text(row.get("Email")).lower()
        zona = _normalize_text(row.get("Zona")).upper()
        cuenta = _normalize_text(row.get("Cuenta")) or "Pernod Ricard"
        activo = _parse_bool(row.get("Activo"))
        capacidad_diaria = _parse_capacity(row.get("Capacidad Diaria"))

        if not nombre:
            stats["invalid_rows"] += 1
            continue

        duplicate_key = (nombre.casefold(), zona, email)
        if duplicate_key in seen_keys:
            stats["duplicates_in_file"] += 1
            continue
        seen_keys.add(duplicate_key)

        usuario = None
        if email:
            usuario = Usuario.query.filter_by(email=email).first()
            if usuario is None:
                usuario = Usuario(email=email, rol="promotor")
                # Evita dejar cuentas importadas con una contraseña pública conocida.
                usuario.set_password(secrets.token_urlsafe(24))
                db.session.add(usuario)
                db.session.flush()
                stats["users_created"] += 1
            elif usuario.rol != "promotor":
                usuario.rol = "promotor"

        promotor = None
        if usuario is not None:
            promotor = Promotor.query.filter_by(usuario_id=usuario.id).first()
        if promotor is None:
            promotor = Promotor.query.filter_by(nombre=nombre, zona=zona or None).first()

        if promotor is None:
            promotor = Promotor(
                nombre=nombre,
                usuario_id=usuario.id if usuario else None,
                zona=zona or None,
                cuenta=cuenta,
                capacidad_diaria=capacidad_diaria,
                activo=activo,
            )
            db.session.add(promotor)
            stats["inserted"] += 1
            if usuario is not None:
                stats["users_linked"] += 1
            continue

        changed = False
        updates = {
            "nombre": nombre,
            "zona": zona or None,
            "cuenta": cuenta,
            "capacidad_diaria": capacidad_diaria,
            "activo": activo,
        }
        if usuario is not None:
            updates["usuario_id"] = usuario.id

        for field, value in updates.items():
            if getattr(promotor, field) != value:
                setattr(promotor, field, value)
                changed = True

        if changed:
            stats["updated"] += 1
        else:
            stats["unchanged"] += 1

        if usuario is not None and promotor.usuario_id == usuario.id:
            stats["users_linked"] += 1

    return stats
