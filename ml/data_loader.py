# ml/data_loader.py
import pandas as pd
def cargar_pdv(path="data/pdv.csv"):
    df = pd.read_csv(path, sep=";", encoding="latin1")
    print("Columnas encontradas:", df.columns.tolist())

    df = df.dropna(subset=["Latitud", "Longitud"])
    print(df.head())

    return df
