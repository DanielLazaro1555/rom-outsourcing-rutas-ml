import os


SEED_PROMOTOR_NAMES = [f"Promotor {i}" for i in range(5)]


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
    from models import Promotor, db

    with app.app_context():
        promotores = Promotor.query.filter(Promotor.nombre.in_(SEED_PROMOTOR_NAMES)).order_by(Promotor.id).all()
        updated = 0

        for promotor in promotores:
            if promotor.activo:
                promotor.activo = False
                updated += 1

        db.session.commit()

    print(
        "Desactivacion de promotores semilla completada. "
        f"Objetivos: {len(SEED_PROMOTOR_NAMES)}. "
        f"Encontrados: {len(promotores)}. "
        f"Desactivados ahora: {updated}."
    )


if __name__ == "__main__":
    main()
