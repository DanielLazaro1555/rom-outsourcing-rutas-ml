import os


LEGACY_PDV_IDS = [70, 81, 84, 159, 491, 617]


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
    load_local_env()

    from app import app
    from models import PDV, db

    with app.app_context():
        pdvs = PDV.query.filter(PDV.id.in_(LEGACY_PDV_IDS)).order_by(PDV.id).all()
        updated = 0

        for pdv in pdvs:
            if pdv.activo:
                pdv.activo = False
                updated += 1

        db.session.commit()

    print(
        "Desactivacion de PDV legado completada. "
        f"Objetivos: {len(LEGACY_PDV_IDS)}. "
        f"Encontrados: {len(pdvs)}. "
        f"Desactivados ahora: {updated}."
    )


if __name__ == "__main__":
    main()
