import os
import sys
import hashlib
from datetime import datetime
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy.exc import OperationalError
from sqlalchemy import inspect, text

# Hash SHA-256 de la contraseña requerida para iniciar el servidor
ACCESS_KEY_HASH = "88a082fe69ad460145094456f9c42d8b9491156a7c49615905064daa2626384d"

# Validación de seguridad en el arranque
access_key = os.environ.get("ACCESS_KEY", "")
user_hash = hashlib.sha256(access_key.encode("utf-8")).hexdigest()

if user_hash != ACCESS_KEY_HASH:
    print("\n" + "="*80)
    print("[-] ERROR CRÍTICO: La clave ACCESS_KEY es incorrecta o no fue proporcionada.")
    print("[-] Para iniciar la aplicación, debe proveer la clave correcta.")
    print("="*80 + "\n")
    sys.exit(1)

app = Flask(__name__)

# Configuración de Logs (Consola y Archivo)
import logging
logging.basicConfig(level=logging.INFO)
os.makedirs("logs", exist_ok=True)
file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
app.logger.addHandler(file_handler)

# Configuración de Base de Datos y Sesiones (SQLAlchemy & Flask-Login)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "algo_secreto_super_seguro_2026")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///rutas.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar Base de Datos
from models import db, Usuario, PDV, Promotor, Ausencia, RutaPlanificada
from password_reset import assign_temporary_password
from pdv_importer import import_pdv_dataframe, load_pdv_dataframe
from planning_window import LABOR_DAY_NAMES, get_day_name, get_operational_week, is_within_operational_week
from promotor_importer import load_promotor_dataframe, sync_promotor_dataframe
db.init_app(app)

# Inicializar Administrador de Sesiones (Login)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Crear tablas automáticamente al arrancar si no existen
with app.app_context():
    db.create_all()

    def safe_execute_ddl(statement):
        try:
            db.session.execute(text(statement))
        except OperationalError as exc:
            if "duplicate column name" not in str(exc).lower():
                raise

    inspector = inspect(db.engine)
    pdv_columns = {column["name"] for column in inspector.get_columns("pdvs")}
    missing_columns = {
        "codigo_pdv": "ALTER TABLE pdvs ADD COLUMN codigo_pdv VARCHAR(100)",
        "empresa": "ALTER TABLE pdvs ADD COLUMN empresa VARCHAR(200)",
        "canal": "ALTER TABLE pdvs ADD COLUMN canal VARCHAR(100)",
        "zona": "ALTER TABLE pdvs ADD COLUMN zona VARCHAR(100)",
        "distrito": "ALTER TABLE pdvs ADD COLUMN distrito VARCHAR(150)",
    }
    promotor_columns = {column["name"] for column in inspector.get_columns("promotores")}
    ausencia_columns = {column["name"] for column in inspector.get_columns("ausencias")}

    for column_name, ddl in missing_columns.items():
        if column_name not in pdv_columns:
            safe_execute_ddl(ddl)

    if "capacidad_diaria" not in promotor_columns:
        safe_execute_ddl("ALTER TABLE promotores ADD COLUMN capacidad_diaria INTEGER DEFAULT 5")
        db.session.execute(text("UPDATE promotores SET capacidad_diaria = 5 WHERE capacidad_diaria IS NULL"))

    if "semana" not in ausencia_columns:
        safe_execute_ddl("ALTER TABLE ausencias ADD COLUMN semana INTEGER")
    if "dia" not in ausencia_columns:
        safe_execute_ddl("ALTER TABLE ausencias ADD COLUMN dia VARCHAR(20)")

    db.session.commit()


def calcular_distancia_total_rutas(zona=None):
    """
    Calcula la distancia geodésica acumulada de las rutas planificadas 
    en la semana 1 utilizando las coordenadas de los PDVs ordenados por ruta.
    """
    rutas_query = db.session.query(
        RutaPlanificada, Promotor, PDV
    ).join(Promotor, RutaPlanificada.promotor_id == Promotor.id)\
     .join(PDV, RutaPlanificada.pdv_id == PDV.id)\
     .filter(RutaPlanificada.semana == 1)

    if zona:
        rutas_query = rutas_query.filter(PDV.zona == zona)

    rutas_planificadas = rutas_query.all()
     
    # Agrupar coordenadas por (promotor, día) para calcular trayectos individuales
    por_grupo = {}
    for r, prom, pdv in rutas_planificadas:
        key = (prom.id, r.dia)
        if key not in por_grupo:
            por_grupo[key] = []
        por_grupo[key].append((r.orden, pdv.latitud, pdv.longitud))
        
    distancia_total = 0.0
    from geopy.distance import geodesic
    for key, puntos in por_grupo.items():
        puntos_ordenados = sorted(puntos, key=lambda x: x[0])
        for i in range(len(puntos_ordenados) - 1):
            p1 = (puntos_ordenados[i][1], puntos_ordenados[i][2])
            p2 = (puntos_ordenados[i+1][1], puntos_ordenados[i+1][2])
            try:
                distancia_total += geodesic(p1, p2).kilometers
            except Exception:
                pass
                
    return round(distancia_total, 2)


def son_dias_consecutivos(dia_a, dia_b):
    orden = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5}
    if dia_a not in orden or dia_b not in orden:
        return False
    return abs(orden[dia_a] - orden[dia_b]) == 1


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.check_password(password):
            login_user(usuario)
            return redirect(url_for('index'))
        else:
            flash("Credenciales incorrectas. Verifique su correo institucional y contraseña.")
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/upload_pdv', methods=['POST'])
@login_required
def upload_pdv():
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para importar archivos.")
        return redirect(url_for('index'))
        
    file = request.files.get('file')
    if not file or file.filename == '':
        flash("No se seleccionó ningún archivo.")
        return redirect(url_for('index'))
        
    try:
        df = load_pdv_dataframe(file, filename=file.filename)
        stats = import_pdv_dataframe(df)
        db.session.commit()
        flash(
            "Carga masiva completada. "
            f"Importados: {stats['imported']}. "
            f"Duplicados en archivo: {stats['duplicates_in_file']}. "
            f"Duplicados en BD: {stats['duplicates_in_db']}. "
            f"Filas inválidas: {stats['invalid_rows']}. "
            f"Fuera de ruta inactivos: {stats['inactive_fuera_de_ruta']}. "
            f"Alertas de codificación: {stats['encoding_warnings']}."
        )
    except Exception as e:
        db.session.rollback()
        flash(f"Error al procesar el archivo: {str(e)}")
        
    return redirect(url_for('index'))

@app.route('/upload_promotores', methods=['POST'])
@login_required
def upload_promotores():
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para importar promotores.")
        return redirect(url_for('index'))

    file = request.files.get('file')
    if not file or file.filename == '':
        flash("No se seleccionó ningún archivo.")
        return redirect(url_for('index'))

    try:
        df = load_promotor_dataframe(file, filename=file.filename)
        stats = sync_promotor_dataframe(df)
        db.session.commit()
        flash(
            "Carga de promotores completada. "
            f"Insertados: {stats['inserted']}. "
            f"Actualizados: {stats['updated']}. "
            f"Sin cambios: {stats['unchanged']}. "
            f"Duplicados en archivo: {stats['duplicates_in_file']}. "
            f"Filas inválidas: {stats['invalid_rows']}. "
            f"Usuarios creados: {stats['users_created']}."
        )
    except Exception as e:
        db.session.rollback()
        flash(f"Error al procesar el archivo de promotores: {str(e)}")

    return redirect(url_for('index'))

@app.route('/delete_route/<int:ruta_id>')
@login_required
def delete_route(ruta_id):
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para modificar rutas.")
        return redirect(url_for('index'))
        
    ruta = RutaPlanificada.query.get_or_404(ruta_id)
    promotor_id = ruta.promotor_id
    dia = ruta.dia
    semana = ruta.semana
    
    db.session.delete(ruta)
    
    # Reordenar las visitas restantes de ese promotor ese día
    restantes = RutaPlanificada.query.filter_by(
        promotor_id=promotor_id, dia=dia, semana=semana
    ).order_by(RutaPlanificada.orden).all()
    
    for idx, r in enumerate(restantes):
        r.orden = idx + 1
        
    db.session.commit()
    flash("Visita eliminada de la planificación y orden reajustado.")
    return redirect(url_for('index'))


@app.route('/add_absence', methods=['POST'])
@login_required
def add_absence():
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para registrar ausencias.")
        return redirect(url_for('index'))

    try:
        promotor_id = int(request.form.get("promotor_id"))
        fecha_texto = request.form.get("fecha")
        motivo = request.form.get("motivo", "").strip()

        promotor = Promotor.query.filter_by(id=promotor_id, activo=True).first()
        if not promotor:
            flash("Error: Promotor no encontrado para registrar ausencia.")
            return redirect(url_for('index'))

        fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
        if not is_within_operational_week(fecha):
            week_start, week_end = get_operational_week()
            flash(
                "Error: la ausencia debe registrarse dentro de la semana operativa actual "
                f"({week_start} a {week_end})."
            )
            return redirect(url_for('index'))

        dia = get_day_name(fecha)
        if dia not in LABOR_DAY_NAMES:
            flash("Error: solo se permiten ausencias de lunes a sábado.")
            return redirect(url_for('index'))

        ausencia_existente = Ausencia.query.filter_by(promotor_id=promotor_id, fecha=fecha).first()
        if ausencia_existente:
            ausencia_existente.motivo = motivo
            ausencia_existente.semana = fecha.isocalendar().week
            ausencia_existente.dia = dia
            flash(f"Ausencia actualizada para {promotor.nombre} el {dia}.")
        else:
            ausencia = Ausencia(
                promotor_id=promotor_id,
                fecha=fecha,
                semana=fecha.isocalendar().week,
                dia=dia,
                motivo=motivo
            )
            db.session.add(ausencia)
            flash(f"Ausencia registrada para {promotor.nombre} el {dia}.")

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f"Error al registrar ausencia: {str(e)}")

    return redirect(url_for('index'))


@app.route('/delete_absence/<int:ausencia_id>')
@login_required
def delete_absence(ausencia_id):
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para eliminar ausencias.")
        return redirect(url_for('index'))

    try:
        ausencia = Ausencia.query.get_or_404(ausencia_id)
        db.session.delete(ausencia)
        db.session.commit()
        flash("Ausencia eliminada correctamente.")
    except Exception as e:
        db.session.rollback()
        flash(f"Error al eliminar ausencia: {str(e)}")

    return redirect(url_for('index'))


@app.route('/reset_promotor_password/<int:promotor_id>', methods=['POST'])
@login_required
def reset_promotor_password(promotor_id):
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para resetear contraseñas.")
        return redirect(url_for('index'))

    try:
        promotor = Promotor.query.get_or_404(promotor_id)
        if not promotor.usuario:
            flash(f"El promotor {promotor.nombre} no tiene un usuario vinculado.")
            return redirect(url_for('index'))

        temporary_password = assign_temporary_password(promotor.usuario)
        db.session.commit()
        flash(
            f"Contraseña temporal generada para {promotor.nombre} "
            f"({promotor.usuario.email}): {temporary_password}"
        )
    except Exception as e:
        db.session.rollback()
        flash(f"Error al resetear la contraseña del promotor: {str(e)}")

    return redirect(url_for('index'))

@app.route('/move_route/<int:ruta_id>/<direction>')
@login_required
def move_route(ruta_id, direction):
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para modificar rutas.")
        return redirect(url_for('index'))
        
    ruta = RutaPlanificada.query.get_or_404(ruta_id)
    promotor_id = ruta.promotor_id
    dia = ruta.dia
    semana = ruta.semana
    orden = ruta.orden
    
    if direction == "up":
        # Intercambiar con el anterior (orden - 1)
        otro = RutaPlanificada.query.filter_by(
            promotor_id=promotor_id, dia=dia, semana=semana, orden=orden - 1
        ).first()
        if otro:
            ruta.orden = orden - 1
            otro.orden = orden
    elif direction == "down":
        # Intercambiar con el siguiente (orden + 1)
        otro = RutaPlanificada.query.filter_by(
            promotor_id=promotor_id, dia=dia, semana=semana, orden=orden + 1
        ).first()
        if otro:
            ruta.orden = orden + 1
            otro.orden = orden
            
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_route', methods=['POST'])
@login_required
def add_route():
    if current_user.rol not in ['admin', 'analista']:
        flash("Acceso denegado: No tiene permisos para modificar rutas.")
        return redirect(url_for('index'))
        
    try:
        promotor_id = int(request.form.get("promotor_id"))
        pdv_id = int(request.form.get("pdv_id"))
        dia = request.form.get("dia")

        promotor = Promotor.query.filter_by(id=promotor_id, activo=True).first()
        if not promotor:
            flash("Error: Promotor no encontrado.")
            return redirect(url_for('index'))

        ausencia_semana_actual = Ausencia.query.filter_by(
            promotor_id=promotor.id,
            dia=dia
        ).filter(
            Ausencia.fecha >= get_operational_week()[0],
            Ausencia.fecha <= get_operational_week()[1],
        ).first()
        if ausencia_semana_actual:
            flash(
                "Error de regla de negocio: "
                f"{promotor.nombre} tiene una ausencia registrada para {dia} "
                f"({ausencia_semana_actual.fecha})."
            )
            return redirect(url_for('index'))
        
        capacidad_promotor = promotor.capacidad_diaria or 5

        # Validación de regla de negocio: respetar capacidad diaria del promotor
        visitas_hoy = RutaPlanificada.query.filter_by(
            promotor_id=promotor.id, dia=dia, semana=1
        ).count()
        
        if visitas_hoy >= capacidad_promotor:
            flash(
                "Error de regla de negocio: "
                f"Se superó el límite diario permitido para {promotor.nombre} "
                f"(máximo {capacidad_promotor} visitas)."
            )
            return redirect(url_for('index'))

        ruta_existente_semana = RutaPlanificada.query.filter_by(
            promotor_id=promotor.id, pdv_id=pdv_id, semana=1
        ).first()
        if ruta_existente_semana:
            if son_dias_consecutivos(ruta_existente_semana.dia, dia):
                flash(
                    "Error de regla de negocio: "
                    f"El PDV ya está asignado a {promotor.nombre} en un día consecutivo "
                    f"({ruta_existente_semana.dia})."
                )
            else:
                flash(
                    "Error de regla de negocio: "
                    f"El PDV ya está asignado a {promotor.nombre} en la semana 1 "
                    f"({ruta_existente_semana.dia})."
                )
            return redirect(url_for('index'))
            
        # Insertar nueva visita al final
        nueva_visita = RutaPlanificada(
            promotor_id=promotor.id,
            pdv_id=pdv_id,
            semana=1,
            dia=dia,
            orden=visitas_hoy + 1
        )
        db.session.add(nueva_visita)
        db.session.commit()
        flash(f"PDV agregado correctamente a la ruta de {promotor.nombre} el {dia}.")
    except Exception as e:
        db.session.rollback()
        flash(f"Error al agregar visita: {str(e)}")
        
    return redirect(url_for('index'))


@app.route('/export_routes/excel')
@login_required
def export_routes_excel():
    zona_seleccionada = request.args.get("zona")

    # Consultar las rutas de la BD
    rutas_query = db.session.query(
        RutaPlanificada, Promotor, PDV
    ).join(Promotor, RutaPlanificada.promotor_id == Promotor.id)\
     .join(PDV, RutaPlanificada.pdv_id == PDV.id)\
     .filter(RutaPlanificada.semana == 1)

    if zona_seleccionada:
        rutas_query = rutas_query.filter(PDV.zona == zona_seleccionada)

    rutas_planificadas = rutas_query\
     .order_by(Promotor.nombre, RutaPlanificada.dia, RutaPlanificada.orden)\
     .all()
     
    data = []
    for r, prom, pdv in rutas_planificadas:
        data.append({
            'Promotor': prom.nombre,
            'Semana Planificada': r.semana,
            'Día de Visita': r.dia,
            'N° Visita Diaria': r.orden,
            'Punto de Venta (PDV)': pdv.nombre,
            'Prioridad': pdv.prioridad,
            'Zona': pdv.zona,
            'Distrito': pdv.distrito,
            'Dirección Completa': pdv.direccion
        })
        
    df = pd.DataFrame(data)
    
    # Crear buffer y exportar
    import io
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Rutas Planificadas')
    output.seek(0)
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=(
            f"Rutas_Planificadas_Semana1_{zona_seleccionada}.xlsx"
            if zona_seleccionada else
            'Rutas_Planificadas_Semana1.xlsx'
        )
    )


@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    # Asegurar que existan promotores y PDVs sembrados en la BD
    if Promotor.query.count() == 0 or PDV.query.count() == 0:
        from scripts.maintenance.seed import seed_database
        seed_database()
        
    promotores = int(request.values.get("promotores", 5))
    visitas = int(request.values.get("visitas", 5))
    zonas_disponibles = [
        zona for (zona,) in db.session.query(PDV.zona)
        .filter(PDV.activo.is_(True), PDV.zona.isnot(None), PDV.zona != "")
        .distinct()
        .order_by(PDV.zona)
        .all()
    ]
    zona_seleccionada = request.values.get("zona")
    if zonas_disponibles:
        if zona_seleccionada not in zonas_disponibles:
            zona_seleccionada = zonas_disponibles[0]
    else:
        zona_seleccionada = None

    promotores_query = Promotor.query.filter(Promotor.activo.is_(True))
    if zona_seleccionada:
        promotores_query = promotores_query.filter(Promotor.zona == zona_seleccionada)
    promotores_disponibles = promotores_query.order_by(Promotor.nombre).all()

    from planificador import clusterizar_y_planificar_db, generar_mapa

    def ejecutar_planificacion():
        df_planificado, centroides_planificados, stats_planificacion = clusterizar_y_planificar_db(
            promotores,
            visitas,
            semana_planificar=1,
            zona=zona_seleccionada
        )
        generar_mapa(df_planificado, centroides_planificados)
        return df_planificado, centroides_planificados, stats_planificacion

    if request.method == "POST":
        if not promotores_disponibles:
            flash(f"No hay promotores activos cargados para la plaza {zona_seleccionada}. Importe promotores antes de planificar.")
            df, centroides = pd.DataFrame(), []
            generar_mapa(df, centroides)
        else:
            try:
                df, centroides, stats = ejecutar_planificacion()
                if stats.get("ausencias_aplicadas"):
                    flash(f"Planificación generada aplicando {stats['ausencias_aplicadas']} ausencia(s).")
                if stats.get("unassigned_visits"):
                    flash(f"Quedaron {stats['unassigned_visits']} visita(s) sin asignar por falta de capacidad disponible.")
            except Exception as exc:
                app.logger.exception("Error generando planificación")
                flash(f"Error al generar la planificación: {exc}")
                generar_mapa(pd.DataFrame(), [])
    else:
        # Si es GET, ver si hay rutas previas en la base de datos
        rutas_query = db.session.query(RutaPlanificada).join(PDV, RutaPlanificada.pdv_id == PDV.id).filter(
            RutaPlanificada.semana == 1
        )
        if zona_seleccionada:
            rutas_query = rutas_query.filter(PDV.zona == zona_seleccionada)

        rutas_db = rutas_query.count()
        if rutas_db == 0 and promotores_disponibles:
            try:
                ejecutar_planificacion()
            except Exception:
                app.logger.exception("Error generando planificación inicial")
        elif promotores_disponibles:
            try:
                ejecutar_planificacion()
            except Exception:
                app.logger.exception("Error recalculando planificación existente")
        else:
            generar_mapa(pd.DataFrame(), [])

    # Recuperar de la base de datos para mostrar en la tabla web
    rutas_planificadas = db.session.query(
        RutaPlanificada, Promotor, PDV
    ).join(Promotor, RutaPlanificada.promotor_id == Promotor.id)\
     .join(PDV, RutaPlanificada.pdv_id == PDV.id)\
     .filter(RutaPlanificada.semana == 1)
    
    if zona_seleccionada:
        rutas_planificadas = rutas_planificadas.filter(PDV.zona == zona_seleccionada)

    rutas_planificadas = rutas_planificadas\
     .order_by(Promotor.nombre, RutaPlanificada.dia, RutaPlanificada.orden)\
     .all()

    tabla = []
    # Días para ordenar correctamente en la visualización
    orden_dias = {"Lunes": 1, "Martes": 2, "Miércoles": 3, "Jueves": 4, "Viernes": 5, "Sábado": 6}
    
    for ruta, promotor, pdv in rutas_planificadas:
        tabla.append({
            'Ruta_Id': ruta.id,
            'Promotor': promotor.nombre,
            'Capacidad': promotor.capacidad_diaria or 5,
            'Semana': ruta.semana,
            'Dia': ruta.dia,
            'Punto de Venta': pdv.nombre,
            'Prioridad': pdv.prioridad,
            'Zona': pdv.zona,
            'Orden': ruta.orden,
            'Dia_Num': orden_dias.get(ruta.dia, 7)
        })
        
    # Ordenar la tabla por Promotor, Semana, Día de la semana y Orden
    tabla = sorted(tabla, key=lambda x: (x['Promotor'], x['Semana'], x['Dia_Num'], x['Orden']))

    # Recuperar todos los PDVs para el desplegable de asignación manual
    todos_pdvs_query = PDV.query.filter(PDV.activo.is_(True))
    if zona_seleccionada:
        todos_pdvs_query = todos_pdvs_query.filter(PDV.zona == zona_seleccionada)
    todos_pdvs = todos_pdvs_query.order_by(PDV.nombre).all()

    week_start, week_end = get_operational_week()
    ausencias_query = db.session.query(Ausencia, Promotor).join(
        Promotor, Ausencia.promotor_id == Promotor.id
    ).filter(
        Ausencia.fecha >= week_start,
        Ausencia.fecha <= week_end,
        Promotor.activo.is_(True)
    )
    if zona_seleccionada:
        ausencias_query = ausencias_query.filter(Promotor.zona == zona_seleccionada)
    ausencias_registradas = ausencias_query.order_by(Ausencia.fecha.desc(), Promotor.nombre).all()

    promotores_con_usuario = [
        promotor for promotor in promotores_disponibles
        if promotor.usuario is not None
    ]

    # Calcular KPIs de distancia (TSP) y CO2 ahorrado
    total_km = calcular_distancia_total_rutas(zona=zona_seleccionada)
    km_manual = total_km * 1.25 # Suposición de ineficiencia de ruta manual (25% más larga)
    co2_saved = round((km_manual - total_km) * 0.12, 2) # 0.12 kg de CO2 por km ahorrado

    return render_template(
        "index.html",
        tabla=tabla,
        promotores=promotores,
        promotores_disponibles=promotores_disponibles,
        visitas=visitas,
        zonas_disponibles=zonas_disponibles,
        zona_seleccionada=zona_seleccionada,
        semana_operativa_inicio=week_start,
        semana_operativa_fin=week_end,
        promotores_con_usuario=promotores_con_usuario,
        todos_pdvs=todos_pdvs,
        ausencias_registradas=ausencias_registradas,
        total_km=total_km,
        co2_saved=co2_saved
    )

if __name__ == '__main__':
    import os
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))
    app.run(host=host, port=port, debug=True)
