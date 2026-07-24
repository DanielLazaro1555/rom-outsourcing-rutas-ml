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
    source_path = sys.argv[1] if len(sys.argv) > 1 else "Csv/promotores_ejemplo.csv"
    load_local_env()

    from app import app
    from models import db
    from promotor_importer import load_promotor_dataframe, sync_promotor_dataframe

    with app.app_context():
        df = load_promotor_dataframe(source_path, filename=source_path)
        stats = sync_promotor_dataframe(df)
        db.session.commit()

    print(
        "Sincronizacion de promotores completada. "
        f"Leidos: {stats['rows_read']}. "
        f"Insertados: {stats['inserted']}. "
        f"Actualizados: {stats['updated']}. "
        f"Sin cambios: {stats['unchanged']}. "
        f"Duplicados en archivo: {stats['duplicates_in_file']}. "
        f"Invalidos: {stats['invalid_rows']}. "
        f"Usuarios creados: {stats['users_created']}. "
        f"Vinculados: {stats['users_linked']}."
    )


if __name__ == "__main__":
    main()
