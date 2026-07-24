# Hoja de Ruta (Roadmap) de Desarrollo

Esta lista de actividades está basada estrictamente en los **Requerimientos Funcionales (RF)**, **Historias de Usuario (HU)** y la **Arquitectura** descritos en **[Informe.md](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/Informe.md)**. 

El plan está estructurado de manera incremental para alinear el software con lo que el docente va a evaluar.

---

## 📅 Plan de Actividades por Fases

### Fase 1: Base de Datos y Persistencia (SQLAlchemy + SQLite/PostgreSQL)
*Objetivo: Migrar del CSV estático a un modelo de persistencia relacional.*
* [x] **Actividad 1.1**: Instalar dependencias necesarias (`flask-sqlalchemy`, `flask-migrate`).
* [x] **Actividad 1.2**: Diseñar los modelos ORM en un archivo nuevo `models.py`:
  * `Usuario`: Para gestionar credenciales (correo, contraseña encriptada) y roles (Admin, Analista, Supervisor, Promotor, Ejecutivo, Gerente).
  * `PDV`: Para almacenar puntos de venta (nombre, latitud, longitud, dirección, prioridad, estado activo/inactivo).
  * `Promotor`: Para almacenar datos operativos del promotor (nombre, zona, cuenta asignada, estado).
  * `Ausencia`: Registrar ausencias de promotores.
  * `RutaPlanificada`: Almacenar las asignaciones semanales de PDV por promotor (semana, día, orden de visita).
* [x] **Actividad 1.3**: Crear script de semilla (`seed.py`) que lea el archivo **[data/pdv.csv](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/data/pdv.csv)** e inserte los datos iniciales en la base de datos local SQLite para pruebas.

### Fase 2: Motor Inteligente (K-Means + TSP Real)
*Objetivo: Integrar el algoritmo de optimización geográfica y secuenciación en las rutas.*
* [x] **Actividad 2.1**: Actualizar **[planificador.py](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/planificador.py)** para importar `resolver_tsp` y `calcular_distancia` de **[ml/tsp_solver.py](file:///home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/ml/tsp_solver.py)**.
* [x] **Actividad 2.2**: Modificar la lógica de planificación para que:
  * Agrupe por K-Means según el número de promotores.
  * Resuelva el problema del Agente Viajero (TSP) para encontrar el orden de visita que minimice la distancia real (o geodésica).
  * Distribuya las visitas respetando la regla del negocio: entre 4 y 6 visitas diarias.
* [x] **Actividad 2.3**: Almacenar el resultado de la planificación directamente en la base de datos en lugar de solo generar el archivo HTML estático.

### Fase 3: Autenticación de Usuarios y Roles (RBAC)
*Objetivo: Implementar inicio de sesión y menús según el rol.*
* [x] **Actividad 3.1**: Agregar sistema de sesiones de Flask (`flask_login` o sesiones básicas).
* [x] **Actividad 3.2**: Crear vistas y pantallas para:
  * Pantalla de Login (`/login`).
  * Pantalla de Registro (`/register`) accesible solo para el rol **Administrador**.
* [x] **Actividad 3.3**: Diseñar el Dashboard Administrativo con menús condicionales:
  * **Analista**: Carga de archivos, generación de rutas y ajuste manual.
  * **Supervisor**: Registro de ausencias y cierres de PDVs.
  * **Promotor**: Vista simplificada de su ruta del día.
  * **Gerente**: Reportes y KPIs.

### Fase 4: Carga Masiva y Ajuste Manual
*Objetivo: Desarrollar interfaces para importar datos y realizar overrides.*
* [x] **Actividad 4.1**: Programar la carga de archivos CSV/Excel en el backend para parsear y almacenar automáticamente nuevos PDVs en la base de datos (HU-08 / CU-04).
* [x] **Actividad 4.2**: Implementar la funcionalidad de ajuste manual en el frontend (permitir cambiar el orden de las visitas de un promotor o mover un PDV a otro promotor) y recalcular la ruta (HU-10 / CU-07).

### Fase 5: Reportes y Exportación
*Objetivo: Generar salidas en PDF/Excel y visualización gerencial.*
* [x] **Actividad 5.1**: Desarrollar la exportación de rutas generadas a archivos Excel y PDF (HU-15 / CU-10).
* [x] **Actividad 5.2**: Crear el **Dashboard Ejecutivo** (HU-20 / CU-11) en el frontend mostrando:
  * Porcentaje de cobertura de visitas.
  * Estimación de kilómetros totales ahorrados vs. proceso manual.
  * Estimación de reducción de huella de carbono (CO2) en base a los kilómetros ahorrados.
