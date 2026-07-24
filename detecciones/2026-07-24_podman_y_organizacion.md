# Bitácora de detecciones

Fecha de registro: 2026-07-24

## Resumen

Se validó el proyecto en Podman y se confirmó que la aplicación responde correctamente cuando el stack está levantado. También se registraron los problemas de entorno que aparecieron durante la verificación para que queden documentados a futuro.

## Estado funcional

* El contenedor de PostgreSQL arranca correctamente.
* El contenedor web ejecuta el sembrado inicial.
* Flask responde con `200` en `/` y `/login` desde dentro del contenedor.
* El semillado cargó 963 PDVs y creó 5 promotores de prueba.

## Detecciones de entorno

1. `pytest` no está instalado en el entorno local de validación.
2. La ejecución con `unittest` falló inicialmente porque faltaban dependencias del proyecto en el host: `flask`, `pandas` y `flask_sqlalchemy`.
3. `podman` rootless requirió ajustar `XDG_RUNTIME_DIR` a un directorio escribible para que el runtime arrancara en este entorno.
4. `podman-compose` con red puente falló por `netavark/aardvark-dns` al crear la carpeta auxiliar de red.
5. El stack sí pudo arrancar en Podman usando `--network host` para los contenedores, sin cambiar el código de la aplicación.
6. La prueba `curl` desde el host no alcanzó `127.0.0.1:5000`, pero la verificación interna al contenedor devolvió `200`.

## Organización del repositorio

### Mantener en la raíz

Estos archivos son parte activa de la aplicación y no conviene eliminarlos:

* `app.py`
* `models.py`
* `planificador.py`
* `planning_window.py`
* `pdv_importer.py`
* `promotor_importer.py`
* `password_reset.py`
* `ml/`

### Utilidades operativas

Estos scripts son importantes, pero su función es administrativa o de mantenimiento:

* `scripts/maintenance/seed.py`
* `scripts/maintenance/refresh_pdvs.py`
* `scripts/maintenance/refresh_promotores.py`
* `scripts/maintenance/deactivate_legacy_pdvs.py`
* `scripts/maintenance/deactivate_seed_promotores.py`

### Artefactos generados

Estos directorios aparecen por la ejecución local y deben seguir ignorados:

* `logs/`
* `instance/`
* `__pycache__/`
* `venv/`

### Datos y notas locales

Estos directorios sirven de apoyo al proyecto, pero no forman parte del flujo central de ejecución:

* `Csv/` contiene archivos de ejemplo para carga manual.
* `data/` contiene el CSV de semilla usado por `scripts/maintenance/seed.py`.
* `private/` reúne notas técnicas y registros de análisis locales; conviene mantenerlo fuera del artefacto de despliegue.

## Conclusión

El proyecto cumple con la intención descrita en el `README`: planificación de rutas con Flask, PostgreSQL, clustering y exportación de reportes. Los problemas encontrados fueron de entorno y no de funcionalidad principal.
