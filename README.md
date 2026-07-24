# Sistema de Rutas para Promotores - Integrador 2

Este es un sistema inteligente de Trade Marketing enfocado en la **planificación, secuenciación y optimización geodésica de rutas de promotores**. El sistema agrupa puntos de venta (PDVs) utilizando aprendizaje no supervisado (**K-Means**) y los ordena de forma óptima mediante algoritmos de resolución del problema del agente viajero (**TSP**).

## 🚀 Arquitectura y Componentes
* **Servicio Web:** Desarrollado en Python con Flask y persistencia con SQLAlchemy.
* **Base de Datos:** PostgreSQL 15 ejecutándose dentro del contenedor.
* **Motor de ML/Optimización:** 
  * Clustering con **K-Means** (Scikit-Learn) para asignar zonas de forma equitativa.
  * Solucionador de **TSP** (Traveling Salesman Problem) usando optimización heurística de distancias geodésicas directas.
* **Interfaz Gráfica:** Dashboard moderno con tema oscuro, KPIs automatizados (ahorro de CO2, kilometraje total de rutas), mapa interactivo con Leaflet y herramientas de exportación (Excel, PDF).

---

## 🔒 Control de Acceso Basado en Roles (RBAC)

El sistema cuenta con un esquema de permisos estricto para diferenciar a los usuarios con permisos de edición (Administración) de aquellos que solo necesitan auditar la información (Lectura).

### Cuentas y Credenciales de Acceso
Las cuentas base del sistema se crean/actualizan automáticamente en la base de datos al arrancar el contenedor con la contraseña predeterminada: **`password`**.

| Correo Institucional | Rol / Perfil | Permisos en el Sistema |
| :--- | :--- | :--- |
| **`admin@rom.com`** | **Admin** | **Acceso Total:** Puede generar rutas por ML, realizar carga masiva de PDVs, agregar/eliminar visitas manualmente e intercambiar el orden de paradas en tiempo real. |
| **`analista@rom.com`** | **Analista** | **Acceso Total:** Mismos permisos que el Administrador para ajustar planificaciones y procesar datasets. |
| **`supervisor@rom.com`** | **Supervisor** | **Solo Lectura:** Puede ver el mapa, filtrar rutas y exportar PDFs/Excel, pero tiene bloqueadas las herramientas de carga masiva y reordenamiento de visitas. |
| **`gerente@rom.com`** | **Gerente** | **Solo Lectura:** Puede monitorear KPIs de eficiencia de rutas y ahorro de CO2 en formato de auditoría. |
| **`ejecutivo@rom.com`** | **Ejecutivo** | **Solo Lectura:** Monitoreo general de la cobertura semanal de visitas. |
| **`promotor@rom.com`** | **Promotor** | **Solo Lectura:** Visualización de sus hojas de ruta y paradas asignadas para la semana. |

> [!NOTE]
> Para alternar entre usuarios durante la prueba del sistema, haga clic en **"Cerrar Sesión"** en la barra superior derecha de la interfaz antes de ingresar con otra cuenta para limpiar de manera segura la sesión de Flask-Login.

> [!IMPORTANT]
> Los usuarios creados por la **importación masiva de promotores** ya no reciben una contraseña pública fija. Un administrador o analista debe generar una **contraseña temporal** desde el panel en la sección **"Acceso de Promotores"**.

---

## 🛠️ Instrucciones de Configuración y Ejecución

La aplicación está completamente containerizada y diseñada para correr de manera aislada con **Podman Compose**.

### 1. Variables de Entorno (`.env`)
Cree un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido (este archivo está excluido del control de versiones por seguridad):

```env
ACCESS_KEY=tu_clave_de_acceso_privada
SECRET_KEY=tu_clave_secreta_flask
```

> [!WARNING]
> La clave configurada en `ACCESS_KEY` dentro de `.env` se utiliza únicamente en el arranque del backend para validar y proteger la inicialización segura del servidor. **No debe confundirse ni utilizarse como contraseña de login en la interfaz web** (para el inicio de sesión use `password`).

### 2. Levantar el Entorno con Podman Compose (Recomendado)
Para iniciar la base de datos y la aplicación en un entorno seguro y aislado:

```bash
# Apagar contenedores previos y limpiar volúmenes huérfanos
podman-compose down

# Construir e iniciar el entorno
podman-compose up --build
```

El servidor web estará disponible en [http://localhost:5000](http://localhost:5000).

---

## 📈 Características Destacadas
* **Carga Masiva de Datos:** Los usuarios administradores pueden subir un archivo Excel o CSV con nuevos puntos de venta conteniendo las columnas `Punto de Venta`, `Latitud`, `Longitud`, `Distrito` y `Zona`.
* **Cálculo de KPIs Geodésicos:** Distancia acumulada basada en coordenadas terrestres reales (fórmula geodésica) para estimar el ahorro logístico y la huella ecológica (CO2).
* **Exportación de Reportes:** Permite descargar la planeación de visitas en formatos de hoja de cálculo estructurada (`xlsx`) o formato de impresión limpio y optimizado (`PDF`).

---

## 📁 Estructura del Proyecto

La raíz del repositorio contiene solo los componentes que se usan para ejecutar o mantener la aplicación:

* **Núcleo de la app:** `app.py`, `models.py`, `planificador.py`, `planning_window.py`, `pdv_importer.py`, `promotor_importer.py`, `password_reset.py` y `ml/`.
* **Utilidades operativas:** `seed.py`, `refresh_pdvs.py`, `refresh_promotores.py`, `deactivate_legacy_pdvs.py` y `deactivate_seed_promotores.py`.
* **Ejecución en contenedor:** `Containerfile`, `compose.yaml`, `entrypoint.sh` y `.containerignore`.
* **Datos de ejemplo:** `Csv/` y `data/`.
* **Pruebas:** `tests/`.

Los archivos generados en tiempo de ejecución, como `logs/`, `instance/`, `__pycache__/` y `venv/`, se mantienen fuera del control de versiones mediante `.gitignore`.
