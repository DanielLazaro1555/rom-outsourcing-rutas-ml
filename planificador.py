# planificador.py

import pandas as pd
import folium
import random
from sklearn.cluster import KMeans
from models import Ausencia, db, PDV, Promotor, RutaPlanificada
from ml.tsp_solver import resolver_tsp
from planning_window import get_day_name, get_operational_week

PRIORITY_ORDER = {"alta": 0, "media": 1, "baja": 2}
DAY_ORDER = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

def clusterizar_y_planificar_db(n_promotores=5, visitas_diarias=5, semana_planificar=1, zona=None):
    """
    Realiza la planificación leyendo de la base de datos PostgreSQL,
    aplica K-Means para segmentar y TSP para ordenar, y guarda el resultado.
    """
    # 1. Obtener PDVs y Promotores activos desde la Base de Datos
    pdv_query = PDV.query.filter_by(activo=True)
    if zona:
        pdv_query = pdv_query.filter_by(zona=zona)

    pdvs_db = pdv_query.all()
    promotor_query = Promotor.query.filter_by(activo=True)
    if zona:
        promotor_query = promotor_query.filter_by(zona=zona)

    promotores_db = promotor_query.order_by(Promotor.nombre).limit(n_promotores).all()
    
    if not pdvs_db or not promotores_db:
        return pd.DataFrame(), [], {"unassigned_visits": 0, "ausencias_aplicadas": 0}
        
    n_promotores_efectivo = min(len(promotores_db), len(pdvs_db))
    promotores_db = promotores_db[:n_promotores_efectivo]
    
    # Convertir PDVs a DataFrame para el clustering
    pdv_data = []
    for p in pdvs_db:
        pdv_data.append({
            "id": p.id,
            "Punto de Venta": p.nombre,
            "Zona": p.zona,
            "Prioridad": p.prioridad or "media",
            "Latitud": p.latitud,
            "Longitud": p.longitud,
            "Dirección": p.direccion
        })
    df = pd.DataFrame(pdv_data)
    
    # 2. Clustering con K-Means
    coords = df[["Latitud", "Longitud"]]
    kmeans = KMeans(n_clusters=n_promotores_efectivo, random_state=42)
    df["Promotor_Cluster"] = kmeans.fit_predict(coords)
    centroides = kmeans.cluster_centers_
    
    # Mapear los índices de cluster de K-Means a los IDs de los promotores reales
    mapa_promotores = {i: prom.id for i, prom in enumerate(promotores_db)}
    df["Promotor_Id"] = df["Promotor_Cluster"].map(mapa_promotores)
    
    week_start, week_end = get_operational_week()
    ausencias_por_promotor = {}
    ausencias_db = Ausencia.query.filter(
        Ausencia.promotor_id.in_([prom.id for prom in promotores_db]),
        Ausencia.fecha >= week_start,
        Ausencia.fecha <= week_end,
    ).all()
    for ausencia in ausencias_db:
        ausencia_dia = ausencia.dia or get_day_name(ausencia.fecha)
        if ausencia_dia in DAY_ORDER:
            ausencias_por_promotor.setdefault(ausencia.promotor_id, set()).add(ausencia_dia)

    # 3. Planificar rutas aplicando el solucionador TSP
    df_planificado, stats = planificar_rutas_tsp(
        df,
        promotores_db,
        visitas_diarias,
        semana_planificar,
        ausencias_por_promotor=ausencias_por_promotor
    )
    
    # 4. Guardar los resultados en la base de datos (RutaPlanificada)
    guardar_planificacion_db(df_planificado, promotores_db, semana_planificar, zona=zona)
    
    return df_planificado, centroides, stats


def planificar_rutas_tsp(df, promotores, visitas_diarias, semana_planificar, ausencias_por_promotor=None):
    dias_laborables = DAY_ORDER
    asignacion = []
    ausencias_por_promotor = ausencias_por_promotor or {}
    backlog = []
    slots_disponibles = {}

    promotores_ordenados = []
    for promotor in promotores:
        # Filtrar puntos de venta asignados a este promotor
        tiendas = df[df["Promotor_Id"] == promotor.id].copy().reset_index(drop=True)
        if tiendas.empty:
            continue

        capacidad_promotor = max(1, min(visitas_diarias, getattr(promotor, "capacidad_diaria", visitas_diarias) or visitas_diarias))
        dias_ausentes = ausencias_por_promotor.get(promotor.id, set())
        dias_disponibles = [dia for dia in dias_laborables if dia not in dias_ausentes]
        capacidad_total_objetivo = capacidad_promotor * len(dias_disponibles)

        # Priorizar PDV de alta prioridad antes de recortar por capacidad semanal.
        tiendas["Prioridad_Orden"] = tiendas["Prioridad"].map(PRIORITY_ORDER).fillna(PRIORITY_ORDER["media"])
        tiendas = tiendas.sort_values(
            by=["Prioridad_Orden", "Punto de Venta"],
            ascending=[True, True]
        ).head(capacidad_total_objetivo).copy().reset_index(drop=True)
            
        # Obtener coordenadas para el TSP
        locations = list(zip(tiendas["Latitud"], tiendas["Longitud"]))
        
        # Si hay más de 2 puntos, aplicar TSP real para ordenarlos óptimamente
        if len(locations) > 2:
            try:
                tsp_route = resolver_tsp(locations)
                unique_route = []
                for idx in tsp_route:
                    if idx not in unique_route and idx < len(tiendas):
                        unique_route.append(idx)
                # Reordenar según el itinerario óptimo
                tiendas = tiendas.iloc[unique_route].copy().reset_index(drop=True)
            except Exception as e:
                print(f"[-] Error al calcular TSP para promotor {promotor.nombre}: {e}")
                # Fallback al orden aleatorio en caso de error
                tiendas = tiendas.sample(frac=1, random_state=42).reset_index(drop=True)
        else:
            tiendas = tiendas.sample(frac=1, random_state=42).reset_index(drop=True)

        promotores_ordenados.append((promotor, tiendas, capacidad_promotor, dias_disponibles))

    for promotor, tiendas, capacidad_promotor, dias_disponibles in promotores_ordenados:
        i = 0
        pdvs_asignados_semana = set()
        for dia in dias_disponibles:
            slots_disponibles[(promotor.id, dia)] = capacidad_promotor
            for orden_visita in range(capacidad_promotor):
                while i < len(tiendas) and int(tiendas.iloc[i]["id"]) in pdvs_asignados_semana:
                    i += 1
                if i < len(tiendas):
                    row = tiendas.iloc[i].copy()
                    pdv_id = int(row["id"])
                    row["Semana"] = semana_planificar
                    row["Dia"] = dia
                    row["Orden"] = orden_visita + 1
                    row["Promotor_Nombre"] = promotor.nombre
                    row["Capacidad_Diaria"] = capacidad_promotor
                    asignacion.append(row)
                    pdvs_asignados_semana.add(pdv_id)
                    slots_disponibles[(promotor.id, dia)] -= 1
                    i += 1

        while i < len(tiendas):
            row = tiendas.iloc[i].copy()
            if int(row["id"]) not in pdvs_asignados_semana:
                backlog.append(row)
            i += 1

    if backlog:
        promotores_por_id = {prom.id: prom for prom in promotores}
        asignados_por_promotor = {}
        for item in asignacion:
            asignados_por_promotor.setdefault(item["Promotor_Id"], set()).add(int(item["id"]))
        for row in backlog:
            assigned = False
            for (promotor_id, dia), slots_restantes in list(slots_disponibles.items()):
                if slots_restantes <= 0:
                    continue
                pdv_id = int(row["id"])
                if pdv_id in asignados_por_promotor.get(promotor_id, set()):
                    continue
                promotor = promotores_por_id[promotor_id]
                orden_actual = sum(
                    1 for item in asignacion
                    if item["Promotor_Id"] == promotor_id and item["Dia"] == dia
                )
                nueva_row = row.copy()
                nueva_row["Semana"] = semana_planificar
                nueva_row["Dia"] = dia
                nueva_row["Orden"] = orden_actual + 1
                nueva_row["Promotor_Nombre"] = promotor.nombre
                nueva_row["Capacidad_Diaria"] = getattr(promotor, "capacidad_diaria", visitas_diarias) or visitas_diarias
                nueva_row["Promotor_Id"] = promotor_id
                asignacion.append(nueva_row)
                asignados_por_promotor.setdefault(promotor_id, set()).add(pdv_id)
                slots_disponibles[(promotor_id, dia)] -= 1
                assigned = True
                break
            if not assigned:
                row["No_Asignado"] = True

    stats = {
        "unassigned_visits": sum(1 for row in backlog if row.get("No_Asignado")),
        "ausencias_aplicadas": sum(len(dias) for dias in ausencias_por_promotor.values()),
    }

    return pd.DataFrame(asignacion), stats


def guardar_planificacion_db(df_planificado, promotores, semana_planificar, zona=None):
    """
    Elimina la planificación previa de la semana seleccionada para los promotores indicados
    e inserta los nuevos registros.
    """
    try:
        promotor_ids = [p.id for p in promotores]
        
        # Reemplazar solo la planificación del universo seleccionado
        rutas_query = RutaPlanificada.query.filter(
            RutaPlanificada.semana == semana_planificar,
            RutaPlanificada.promotor_id.in_(promotor_ids)
        )

        if zona:
            pdv_ids_zona = [
                pdv_id for (pdv_id,) in db.session.query(PDV.id).filter(
                    PDV.zona == zona
                ).all()
            ]
            if pdv_ids_zona:
                rutas_query = rutas_query.filter(RutaPlanificada.pdv_id.in_(pdv_ids_zona))

        rutas_query.delete(synchronize_session=False)
        
        # Insertar nuevas asignaciones
        for _, row in df_planificado.iterrows():
            nueva_ruta = RutaPlanificada(
                promotor_id=int(row["Promotor_Id"]),
                pdv_id=int(row["id"]),
                semana=semana_planificar,
                dia=row["Dia"],
                orden=int(row["Orden"])
            )
            db.session.add(nueva_ruta)
            
        db.session.commit()
        print(f"[+] Éxito: Planificación para la semana {semana_planificar} guardada en BD.")
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Error guardando planificación en BD: {e}") from e


def generar_mapa(df, centroides, output_path="static/mapa.html"):
    colores = ['red', 'blue', 'green', 'orange', 'purple', 'darkred', 'cadetblue', 'lightgreen']
    
    if df.empty:
        # Mapa por defecto centrado en Lima si no hay datos
        m = folium.Map(location=[-12.046374, -77.042793], zoom_start=12)
        m.save(output_path)
        return
        
    m = folium.Map(location=[df["Latitud"].mean(), df["Longitud"].mean()], zoom_start=12)
    
    # Dibujar marcadores de PDVs
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["Latitud"], row["Longitud"]],
            popup=f"<b>{row['Punto de Venta']}</b><br>Promotor: {row['Promotor_Nombre']}<br>{row['Dia']} - Orden: {row['Orden']}",
            icon=folium.Icon(color=colores[int(row.get('Promotor_Cluster', 0)) % len(colores)])
        ).add_to(m)
        
    # Dibujar los centroides de K-Means
    for i, (lat, lon) in enumerate(centroides):
        folium.Marker(
            location=[lat, lon],
            popup=f'Centroide Zona Promotor {i}',
            icon=folium.Icon(color='black', icon='star')
        ).add_to(m)
        
    m.save(output_path)


# Mantener compatibilidad con el código anterior por si acaso
def clusterizar_y_planificar(path_csv, n_promotores=5, visitas_diarias=5):
    """
    Función de compatibilidad que lee directamente del CSV si la base de datos no se usa.
    """
    df = pd.read_csv(path_csv, sep=";", encoding="latin1").dropna(subset=["Latitud", "Longitud"]).copy()
    
    # Adaptar coordenadas lat/lon con coma decimal
    df["Latitud"] = df["Latitud"].astype(str).str.replace(",", ".").astype(float)
    df["Longitud"] = df["Longitud"].astype(str).str.replace(",", ".").astype(float)
    if "id" not in df.columns:
        df["id"] = range(1, len(df) + 1)
    if "Prioridad" not in df.columns:
        df["Prioridad"] = "media"
    
    kmeans = KMeans(n_clusters=n_promotores, random_state=42)
    df["Promotor_Cluster"] = kmeans.fit_predict(df[["Latitud", "Longitud"]])
    centroides = kmeans.cluster_centers_
    
    # Crear perfil de promotores ficticios
    class FakePromotor:
        def __init__(self, id, nombre):
            self.id = id
            self.nombre = nombre
            
    fake_promotores = [FakePromotor(i, f"Promotor {i}") for i in range(n_promotores)]
    df["Promotor_Id"] = df["Promotor_Cluster"]
    
    df_planificado, _stats = planificar_rutas_tsp(df, fake_promotores, visitas_diarias, 1)
    return df_planificado, centroides
