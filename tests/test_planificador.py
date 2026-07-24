import os
import tempfile
import unittest
from datetime import date
from unittest.mock import patch

import pandas as pd
from flask import Flask

from models import Ausencia, PDV, Promotor, RutaPlanificada, db
from planificador import clusterizar_y_planificar, clusterizar_y_planificar_db, guardar_planificacion_db


class PlanificadorTests(unittest.TestCase):
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

    def test_clusterizar_y_planificar_db_applies_absence_by_operational_week_dates(self):
        promotor = Promotor(nombre="Promotor Centro", zona="LIMA", capacidad_diaria=1, activo=True)
        db.session.add(promotor)
        db.session.flush()

        pdvs = [
            PDV(nombre="PDV A", latitud=-12.01, longitud=-77.01, direccion="Dir A", prioridad="media", activo=True, zona="LIMA"),
            PDV(nombre="PDV B", latitud=-12.02, longitud=-77.02, direccion="Dir B", prioridad="media", activo=True, zona="LIMA"),
        ]
        db.session.add_all(pdvs)

        db.session.add(
            Ausencia(
                promotor_id=promotor.id,
                fecha=date(2026, 7, 13),
                semana=999,
                dia=None,
                motivo="Descanso",
            )
        )
        db.session.commit()

        with patch("planificador.get_operational_week", return_value=(date(2026, 7, 13), date(2026, 7, 18))):
            df_planificado, centroides, stats = clusterizar_y_planificar_db(
                n_promotores=1,
                visitas_diarias=1,
                semana_planificar=1,
                zona="LIMA",
            )

        self.assertEqual(len(centroides), 1)
        self.assertEqual(stats["ausencias_aplicadas"], 1)
        self.assertFalse((df_planificado["Dia"] == "Lunes").any())
        self.assertEqual(RutaPlanificada.query.count(), 2)

    def test_guardar_planificacion_db_raises_when_commit_fails(self):
        promotor = Promotor(nombre="Promotor Sur", zona="LIMA", capacidad_diaria=1, activo=True)
        pdv = PDV(nombre="PDV X", latitud=-12.03, longitud=-77.03, direccion="Dir X", prioridad="media", activo=True, zona="LIMA")
        db.session.add_all([promotor, pdv])
        db.session.commit()

        df_planificado = pd.DataFrame(
            [
                {
                    "Promotor_Id": promotor.id,
                    "id": pdv.id,
                    "Dia": "Martes",
                    "Orden": 1,
                }
            ]
        )

        with patch("planificador.db.session.commit", side_effect=Exception("db down")):
            with self.assertRaises(RuntimeError):
                guardar_planificacion_db(df_planificado, [promotor], semana_planificar=1, zona="LIMA")

    def test_clusterizar_y_planificar_legacy_returns_dataframe(self):
        csv_content = "\n".join(
            [
                "Punto de Venta;Latitud;Longitud",
                "PDV 1;-12,01;-77,01",
                "PDV 2;-12,02;-77,02",
                "PDV 3;-12,03;-77,03",
            ]
        )

        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="latin1") as temp_file:
            temp_file.write(csv_content)
            csv_path = temp_file.name

        try:
            df_planificado, centroides = clusterizar_y_planificar(csv_path, n_promotores=1, visitas_diarias=2)
        finally:
            os.unlink(csv_path)

        self.assertIsInstance(df_planificado, pd.DataFrame)
        self.assertEqual(len(centroides), 1)


if __name__ == "__main__":
    unittest.main()
