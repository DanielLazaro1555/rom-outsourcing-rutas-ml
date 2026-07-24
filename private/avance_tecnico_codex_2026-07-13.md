# Avance Tecnico Del Proyecto

Fecha: `2026-07-13`

## Objetivo De Este Documento

Este archivo resume lo que se implemento en el proyecto durante la revision tecnica, por que se hizo, en que parte del `Informe.md` se apoya y que puntos aun quedan pendientes para seguir alineando el MVP con el alcance funcional del proyecto.

## Base De Referencia

Las decisiones tomadas se guiaron por el documento [Informe.md](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/private/Informe.md:147), especialmente por estas ideas:

- “prioridad comercial de los PDV”
- “disponibilidad y capacidad operativa de los promotores”
- “carga masiva de datos”
- “ausencias del personal”
- “sin repetir PDVs en días consecutivos”

Tambien fue clave esta validacion funcional del informe en [Informe.md](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/private/Informe.md:1248):

> “sin repetir PDVs en días consecutivos de la misma semana”

Y esta historia de usuario en [Informe.md](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/private/Informe.md:1208):

> “redistribuye automáticamente los PDVs del promotor ausente”

## Lo Que Se Implemento

### 1. Saneamiento Del Padron De PDV

Se implemento una importacion centralizada para PDV en [pdv_importer.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/pdv_importer.py:1).

Que hace ahora:

- valida columnas minimas
- normaliza texto
- detecta duplicados en archivo y BD
- conserva `codigo_pdv`, `empresa`, `canal`, `zona`, `distrito`
- marca `FUERA_DE_RUTA` como `activo=False`

Por que se hizo:

- el informe condiciona la efectividad del sistema a la calidad del dato
- el CSV original tenia duplicados, codificacion defectuosa y mezcla de plazas
- el sistema estaba perdiendo informacion importante del padron al importar

### 2. Ampliacion Del Modelo De PDV

Se amplio el modelo [PDV](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/models.py:26) para guardar:

- `codigo_pdv`
- `empresa`
- `canal`
- `zona`
- `distrito`

Por que se hizo:

- el informe describe gestion maestra de PDV con mas contexto de negocio
- sin estos campos no era posible planificar y auditar correctamente por plaza o cuenta

### 3. Filtrado De Planificacion Por Plaza

Se ajusto la planificacion para trabajar por plaza activa en [app.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/app.py:376) y [planificador.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/planificador.py:10).

Que cambia:

- el dashboard permite elegir `zona`
- la generacion de rutas ya no mezcla ciudades
- el selector manual y la exportacion respetan la plaza activa

Por que se hizo:

- el padron mezcla `LIMA`, `CUSCO`, `CHICLAYO`, `TRUJILLO`, `HUANCAYO`, `AREQUIPA`, `PIURA`
- optimizar todo junto era incorrecto operativamente

### 4. Sincronizacion Y Limpieza De La Base Local

Se agregaron scripts de mantenimiento:

- [refresh_pdvs.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/refresh_pdvs.py:1)
- [deactivate_legacy_pdvs.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/deactivate_legacy_pdvs.py:1)

Que se hizo en la base local:

- sincronizacion del padron actual
- desactivacion de `FUERA_DE_RUTA`
- desactivacion de PDV legado duplicados sin codigo maestro

Por que se hizo:

- el sistema necesitaba una base coherente antes de mejorar reglas de negocio

### 5. Carga Real De Promotores

Se implemento importacion de promotores en:

- [promotor_importer.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/promotor_importer.py:1)
- [refresh_promotores.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/refresh_promotores.py:1)
- [Csv/promotores_ejemplo.csv](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/Csv/promotores_ejemplo.csv:1)

Que hace ahora:

- crea o vincula usuario `promotor`
- registra nombre, zona, cuenta, activo
- permite carga desde UI o CLI

Por que se hizo:

- el MVP dependia de `Promotor 0..4`
- el informe pide registro de promotores con zona, cuenta y disponibilidad

### 6. Desactivacion De Promotores Semilla

Se agrego [deactivate_seed_promotores.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/deactivate_seed_promotores.py:1) para desactivar `Promotor 0..4`.

Por que se hizo:

- limpiar la operacion real
- evitar que el planificador siga usando datos ficticios cuando ya existen promotores reales

### 7. Capacidad Diaria Por Promotor

Se agrego `capacidad_diaria` en [models.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/models.py:46) y se conecto a:

- importacion de promotores
- generacion de rutas
- asignacion manual
- tabla principal

Por que se hizo:

- el informe habla de carga equilibrada entre `4` y `6` visitas por dia
- antes el limite era global y fijo
- ahora cada promotor puede tener un techo propio

### 8. Prioridad De PDV

Se integro el campo `Prioridad` en:

- importacion de PDV
- motor de planificacion
- tabla y exportacion

Referencias tecnicas:

- [pdv_importer.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/pdv_importer.py:1)
- [planificador.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/planificador.py:65)

Por que se hizo:

- el informe menciona cobertura sobre PDV de alta prioridad
- si no hay capacidad suficiente, ahora entran primero `alta`, luego `media`, luego `baja`

### 9. Ausencias Con Redistribucion Basica

Se implemento registro y uso de ausencias en:

- [models.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/models.py:58)
- [app.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/app.py:219)
- [planificador.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/planificador.py:10)
- [templates/index.html](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/templates/index.html:500)

Que hace ahora:

- registra ausencia con fecha, dia, semana y motivo
- excluye al promotor ausente en ese dia
- intenta redistribuir visitas a otros promotores con cupo disponible
- informa si quedaron visitas sin asignar
- permite eliminar ausencias registradas

Por que se hizo:

- el informe lo pide de forma explicita en la historia de usuario de ausencias
- era una de las brechas mas visibles entre documento y MVP

### 10. No Repeticion Basica De PDV En La Semana

Se reforzo la regla en:

- [planificador.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/planificador.py:65)
- [app.py](/home/daniel/Documentos/Github/sistema-rutas-promotores-Integrador2/app.py:287)

Que hace ahora:

- la planificacion automatica evita repetir el mismo `pdv_id` para un promotor en la semana
- la asignacion manual bloquea agregar un PDV si ese promotor ya lo tiene en la semana 1
- si el choque es en dia consecutivo, el mensaje lo indica explicitamente

Por que se hizo:

- el informe pide “sin repetir PDVs en días consecutivos de la misma semana”
- antes el sistema podia duplicar visitas del mismo PDV para el mismo promotor

## Cambios Que Mejoran El Proyecto Pero Aun Son Parciales

Estos puntos ya avanzaron, pero todavia no estan completos al nivel del informe:

- la redistribucion por ausencias ya existe, pero aun no optimiza por cercania ni por tiempo estimado
- la prioridad de PDV ya influye en la seleccion, pero no aun en una estrategia de cobertura semanal mas rica
- la carga diaria por promotor ya se respeta, pero aun no hay control por horas de jornada
- la regla de no repeticion ya evita duplicados semanales basicos, pero aun no modela ventanas mas complejas de rotacion

## Lo Que Aun Falta

Para seguir alineando el sistema con el `Informe.md`, faltaria priorizar estos bloques:

### Pendiente Alto

- mejorar la redistribucion por ausencias usando cercania o costo de insercion
- agregar metricas visibles de negocio:
  - visitas no asignadas
  - cobertura de PDV priorizados
  - carga por promotor
  - ausencias aplicadas
- reporte de cobertura de PDV visitados y no visitados

### Pendiente Medio

- control por horas estimadas de jornada
- cierre temporal de PDV con fechas de inicio y reapertura
- exportacion mas rica alineada al informe
- filtros y vistas mas ejecutivas para seguimiento semanal

### Pendiente Futuro

- trafico o tiempos estimados mas realistas
- consulta de ruta diaria desde vista movil para promotor
- registro de visita realizada por promotor
- dashboard ejecutivo con comparativos semanales

## Conclusiones

El proyecto ya dejo de ser solo un MVP tecnico de `K-Means + TSP` y ahora cubre varias reglas operativas reales del informe:

- carga masiva de PDV y promotores
- planificacion por plaza
- capacidad diaria por promotor
- prioridad comercial de PDV
- ausencias con redistribucion basica
- no repeticion semanal basica

Lo siguiente ya no es limpiar estructura, sino profundizar calidad operativa y visibilidad del negocio.
