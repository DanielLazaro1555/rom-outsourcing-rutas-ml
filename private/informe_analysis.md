# Análisis Detallado del Informe Técnico

Este análisis evalúa el documento **[Informe.md](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/Informe.md)** en contraste con el código fuente actual del proyecto. El objetivo es identificar brechas (gaps) entre lo especificado en la teoría académica y lo implementado en la práctica, proporcionándote recomendaciones clave para tu entrega universitaria.

---

## 📌 1. Resumen y Estructura del Informe

El informe es de naturaleza académica-técnica para el curso **Integrador II: Sistemas (UTP, 2026-1)**. Presenta una propuesta formal para automatizar y optimizar la planificación de rutas para la empresa **ROM Outsourcing SAC** (específicamente la cuenta del cliente *Pernod Ricard*).

El documento está estructurado de manera excelente y cumple con los estándares de ingeniería de software:
* **Metodología Ágil**: Define un Product Backlog con 20 Historias de Usuario (HUs) distribuidas en 4 Sprints, con sus respectivos Burndown Charts y estimaciones en Story Points.
* **Casos de Uso e UML**: Define diagramas y flujos detallados para 11 Casos de Uso (CUs).
* **Arquitectura de Software**: Detalla una arquitectura en capas, persistencia geoespacial (PostgreSQL/PostGIS) y seguridad alineada a la norma **ISO 27001:2022**.

---

## 🔍 2. Brechas Identificadas (Documento vs. Código)

Al analizar el código actual del proyecto, se identifican diferencias significativas entre lo que el documento dice que hace el sistema y lo que realmente está implementado. Estas discrepancias son normales en avances de Sprints, pero debes cuidarlas en las entregas finales:

### A. ⚠️ Motor de Optimización: ¿K-Means + TSP?
* **El Informe dice**: Que el sistema agrupa los PDV usando **K-Means** y calcula la secuencia óptima mediante el algoritmo del **Agente Viajero (TSP)** con algoritmos genéticos o heurísticas para minimizar los kilómetros.
* **El Código real**: 
  * En **[planificador.py](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/planificador.py)**, efectivamente se aplica K-Means para segmentar los promotores.
  * Sin embargo, para ordenar la ruta, el código hace un simple desorden aleatorio:
    ```python
    random.shuffle(tiendas.values.tolist())
    ```
  * Aunque existe un script **[ml/tsp_solver.py](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/ml/tsp_solver.py)** con lógica para resolver el TSP usando `networkx` y `geopy`, **esta función nunca es importada ni ejecutada** en el flujo principal de planificación.

### B. ⚠️ Capa de Persistencia y Base de Datos
* **El Informe dice**: Que la arquitectura utiliza una Base de Datos relacional (**PostgreSQL con PostGIS** o MySQL) con SQLAlchemy y migraciones automáticas.
* **El Código real**: No existe conexión a ninguna base de datos ni modelos ORM. La aplicación lee directamente del archivo estático **[data/pdv.csv](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/data/pdv.csv)** y genera un mapa en HTML estático (**[static/mapa.html](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/static/mapa.html)**) en cada petición.

### C. ⚠️ Gestión de Usuarios, Sesiones y Roles (RBAC)
* **El Informe dice**: Que el sistema tiene 6 roles de usuario diferenciados (Admin, Analista, Supervisor, Promotor, Ejecutivo, Gerente) con login, recuperación de contraseña (CUs 01, 03 y 09) y un Control de Acceso Basado en Roles (RBAC).
* **El Código real**: No hay inicio de sesión, sesiones HTTP, ni roles implementados en la web. La única seguridad activa es el bloqueo por la variable de entorno `ACCESS_KEY` que agregamos recientemente para proteger la ejecución del contenedor.

### D. ⚠️ Módulos de Exportación y Dashboard Ejecutivo
* **El Informe dice**: Que se permite la exportación de rutas a PDF y Excel (HU-15 / CU-10) y cuenta con un Dashboard Ejecutivo para gerentes con KPIs sobre ahorro logístico, km y estimación de emisiones de CO2 (HU-18, HU-20 / CU-11).
* **El Código real**: Estos módulos no se encuentran desarrollados aún en la interfaz gráfica ni en el backend.

---

## 💡 3. Recomendaciones de Mejora para tu Proyecto

Para asegurar la máxima nota en tu curso y tener un proyecto consistente con tu informe, te sugiero las siguientes acciones priorizadas:

### 🚀 Acción 1: Conectar el solucionador TSP en la ruta
Deberíamos modificar **[planificador.py](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/planificador.py)** para importar `resolver_tsp` de **[ml/tsp_solver.py](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/ml/tsp_solver.py)**. Esto justificará el uso de Machine Learning e Inteligencia Artificial que se expone en la introducción del informe.

### 🗄️ Acción 2: Implementar persistencia ligera (SQLite)
Si la entrega del Sprint requiere una base de datos activa pero no quieres lidiar con configuraciones complejas de PostgreSQL en la nube, podemos usar **SQLite** (un motor de base de datos en un solo archivo). SQLite es ideal para prototipos, se configura en 5 minutos en Flask con SQLAlchemy y es completamente soportado por Podman/Docker.

### 🔑 Acción 3: Login e Interfaz Básica de Roles
Can agregar un login simple en Flask usando `flask_login` o cookies de sesión para simular los roles (por ejemplo, permitir ver botones de "Configuración de Reglas" solo si el rol es Administrador, o "Reporte de KPIs" si el rol es Gerente).
