# ml/cluster.py
from sklearn.cluster import KMeans
import pandas as pd

def agrupar_pdv(df, n_promotores=3):
    coords = df[["Latitud", "Longitud"]]
    kmeans = KMeans(n_clusters=n_promotores, random_state=42).fit(coords)
    df["Grupo"] = kmeans.labels_
    return df
