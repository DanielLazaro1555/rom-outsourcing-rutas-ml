import os
import sys


def load_local_env(path=".env"):
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def main():
    source_path = sys.argv[1] if len(sys.argv) > 1 else "Csv/pdv.csv"
    load_local_env()

    from app import app
    from models import db
    from pdv_importer import load_pdv_dataframe, sync_pdv_dataframe

    with app.app_context():
        df = load_pdv_dataframe(source_path, filename=source_path)
        stats = sync_pdv_dataframe(df)
        db.session.commit()

    print(
        "Sincronizacion de PDV completada. "
        f"Leidos: {stats['rows_read']}. "
        f"Insertados: {stats['inserted']}. "
        f"Actualizados: {stats['updated']}. "
        f"Sin cambios: {stats['unchanged']}. "
        f"Duplicados en archivo: {stats['duplicates_in_file']}. "
        f"Invalidos: {stats['invalid_rows']}. "
        f"Fuera de ruta inactivos detectados: {stats['inactive_fuera_de_ruta']}. "
        f"Alertas de codificacion: {stats['encoding_warnings']}."
    )


if __name__ == "__main__":
    main()
