import unittest

from flask import Flask

from models import Promotor, Usuario, db
from promotor_importer import sync_promotor_dataframe


class SimpleFrame:
    def __init__(self, rows):
        self._rows = rows

    def __len__(self):
        return len(self._rows)

    def iterrows(self):
        for index, row in enumerate(self._rows):
            yield index, row


class PromotorImporterTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.config["TESTING"] = True
        db.init_app(self.app)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_new_imported_user_does_not_accept_default_password(self):
        df = SimpleFrame([
            {
                "Nombre": "Promotor Norte",
                "Email": "norte@example.com",
                "Zona": "LIMA",
                "Cuenta": "Pernod Ricard",
                "Activo": "1",
                "Capacidad Diaria": "4",
            }
        ])

        stats = sync_promotor_dataframe(df)
        db.session.commit()

        usuario = Usuario.query.filter_by(email="norte@example.com").first()
        promotor = Promotor.query.filter_by(nombre="Promotor Norte").first()

        self.assertEqual(stats["users_created"], 1)
        self.assertIsNotNone(usuario)
        self.assertIsNotNone(promotor)
        self.assertFalse(usuario.check_password("password"))
        self.assertEqual(promotor.usuario_id, usuario.id)


if __name__ == "__main__":
    unittest.main()
