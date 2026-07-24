![Imagen que contiene dibujo, señal, relojDescripción generada automáticamente][image1]

Facultad Ingeniería

Carrera Profesional de Ingeniería de Sistemas e Informática

Sistema Web Inteligente Basado en Machine Learning para la Optimización de Rutas de Promotores en el Trade Marketing para la empresa ROM Outsourcing

González Vilchez Howard Paul 

Huaman Ramos Piero Andersson

Huaman Lazaro Daniel Esteban

Minaya Lopez Jorge Luis

Miranda Fuentes Alessandro Djorkaeff

Curso Integrador II: Sistemas \- Sección 55174

Docente: Huaman Lazaro, Daniel Esteban

Lima – Perú

2026 \- 1

**Contenido**  
**[1\.](#resumen-ejecutivo)**	[**Resumen Ejecutivo**	3](#resumen-ejecutivo)

[**2\.**	**Antecedentes**	4](#antecedentes)

[**3\.**	**Descripción del Problema del Negocio**	5](#descripción-del-problema-del-negocio)

[**4\.**	**Descripción Detallada de la Empresa**	6](#descripción-detallada-de-la-empresa)

[**5\.**	**Análisis del Problema o Mejora del Proceso**	7](#análisis-del-problema-o-mejora-del-proceso)

[**6\.**	**Objetivo del Proyecto**	9](#objetivo-del-proyecto)

[**7\.**	**Alcance del Proyecto**	9](#alcance-del-proyecto)

[**8\.**	**Requerimientos del Proyecto**	11](#requerimientos-del-proyecto)

[**9\.**	**Estrategia del Desarrollo**	15](#estrategia-del-desarrollo)

[**10\.**	**Cronograma de Desarrollo**	16](#cronograma-de-desarrollo)

[**11\.**	**Referencias**	17](#referencias)

**ESTRUCTURA DEL AVANCE 1 DEL PROYECTO DE SOFTWARE**

1. # **Resumen Ejecutivo** {#resumen-ejecutivo}

* Breve descripción del proyecto  
  El presente proyecto comprende el diseño e implementación de un sistema web inteligente orientado a la automatización y optimización de la planificación de rutas para promotores de trade marketing en la empresa ROM Outsourcing SAC. La solución integra algoritmos de Machine Learning específicamente clustering geográfico mediante K-Means y optimización de recorridos basada en heurísticas del Problema del Agente Viajero (TSP) con el propósito de generar asignaciones diarias equilibradas y contextualmente adaptadas a variables operativas reales, tales como condiciones de tráfico, ausencias del personal y restricciones normativas del negocio.  
* Objetivo principal  
  Desarrollar una herramienta web que permita reducir significativamente los tiempos de desplazamiento y los costos logísticos asociados a la operación de campo, al mismo tiempo que optimice la cobertura de puntos de venta (PDV) y garantice una distribución equitativa de la carga laboral entre los promotores, sustituyendo el modelo de planificación manual actualmente vigente por un sistema basado en datos y algoritmos de inteligencia artificial.  
* Justificación del desarrollo  
  La asignación de rutas en ROM Outsourcing SAC se ejecuta en la actualidad de forma completamente manual, sustentada en la experiencia del personal operativo y en herramientas ofimáticas de propósito general (Microsoft Excel). Este paradigma genera ineficiencias operativas cuantificables: sobrecostos logísticos en el orden del 15 al 20%, índices de fatiga laboral elevados y tasas de rotación de personal superiores al 20%. Adicionalmente, expone a la empresa a riesgos de incumplimiento contractual con cuentas estratégicas de alta exigencia, como Pernod Ricard. La organización dispone de un repositorio de datos históricos y geográficos de considerable valor que permanece subutilizado; la incorporación de técnicas de Machine Learning constituye una oportunidad concreta para cerrar esta brecha de madurez digital mediante una solución de bajo costo y alto impacto operacional.  
* Beneficios esperados  
  La implementación del sistema proyecta los siguientes beneficios cuantificables y estratégicos:  
  * Reducción del 15 al 20% en tiempos de movilización y costos logísticos directos.  
  * Incremento del 10 al 15% en la cobertura efectiva de puntos de venta por jornada.  
  * Equilibrio de la carga laboral entre promotores, con una asignación óptima de entre 4 y 6 visitas diarias por persona.  
  * Disminución de la tasa de rotación de personal derivada de la sobrecarga y la fatiga operativa.  
  * Cumplimiento más estable y predecible de los Acuerdos de Nivel de Servicio (SLA) con clientes estratégicos.  
  * Arquitectura tecnológica escalable y basada en componentes open-source, replicable a otras regiones geográficas y cuentas comerciales de la cartera empresarial.

2. # **Antecedentes** {#antecedentes}

* Contexto del problema.  
  En el sector de trade marketing peruano, particularmente en categorías de alta rotación y dinamismo comercial como la distribución de bebidas alcohólicas cuyo crecimiento proyectado en exportaciones asciende al 8.5% para el período 2025, la eficiencia logística y la presencia sostenida en el punto de venta constituyen factores críticos de competitividad. ROM Outsourcing SAC enfrenta el desafío estructural de coordinar decenas de promotores en Lima Metropolitana y provincias, en un entorno donde la dispersión geográfica de los PDV, la congestión del tráfico urbano y la variabilidad operativa inherente al trabajo de campo demandan un sistema de planificación ágil y adaptativo, del cual la empresa carece en la actualidad.  
* Situación actual del proceso o sistema.  
  El proceso de asignación de rutas es ejecutado en su totalidad de forma manual por analistas de Business Intelligence y ejecutivos de cuenta, quienes recurren a hojas de cálculo y a criterios empíricos para determinar los recorridos diarios. Este procedimiento demanda entre 60 y 90 minutos de dedicación por planificador cada semana, sin considerar variables dinámicas como condiciones de tráfico en tiempo real o ausencias imprevistas del personal. Como consecuencia, se generan rutas subóptimas caracterizadas por trayectorias cruzadas, repetición innecesaria de visitas y jornadas laborales desequilibradas. Estas ineficiencias se traducen en desgaste físico del personal, riesgo de síndrome de agotamiento profesional (burnout) y pérdidas económicas derivadas de penalidades contractuales, estimadas entre el 10 y el 15% de la facturación por cuenta cliente.  
* Intentos previos de solución (si los hubiera).  
  Al interior de ROM Outsourcing SAC no se han implementado previamente herramientas de automatización específicas para la gestión de rutas. No obstante, la literatura académica especializada y los casos de estudio documentados en logística y retail evidencian reducciones del 15 al 30% en costos y tiempos operativos al migrar de la planificación heurística manual a modelos basados en datos. Estos referentes validan la viabilidad técnica del enfoque propuesto y sustentan su pertinencia en el contexto organizacional específico.  
* Motivación para el desarrollo del software  
  La motivación central del proyecto radica en transformar un proceso operativo crítico, pero tecnológicamente obsoleto, en una ventaja competitiva sostenible a través de la digitalización accesible. El proyecto aprovecha la infraestructura de datos existente en la organización, aplica metodologías ágiles de desarrollo (Scrum) y tecnologías de código abierto (Flask/Django, Scikit-learn) para entregar un Producto Mínimo Viable (MVP) funcional sin requerir inversión inicial significativa. Asimismo, sienta las bases para una futura implementación piloto, la medición de retorno sobre la inversión (ROI) real y la escalabilidad hacia otras operaciones de la empresa.

3. # **Descripción del Problema del Negocio** {#descripción-del-problema-del-negocio}

* Problema general del negocio  
  En ROM Outsourcing SAC, la planificación y asignación de rutas de promotores y puntos de venta se ejecuta de manera predominantemente manual, sustentada en la experiencia acumulada del equipo de operaciones y en criterios simplificados de proximidad geográfica entre establecimientos. Este enfoque se torna estructuralmente frágil ante el incremento del volumen de PDV, la mayor dispersión territorial y la variabilidad operativa inherente al trabajo de campo. El resultado es la generación sistemática de rutas subóptimas y la necesidad recurrente de replanificación manual, lo que implica un consumo ineficiente de recursos humanos y operativos.  
* Impacto en la operación, productividad o servicio  
  Desde la perspectiva operacional, la asignación manual produce itinerarios no optimizados que incrementan los tiempos y costos de desplazamiento, al mismo tiempo que generan brechas de cobertura en PDV de alta prioridad. La gestión basada en hojas de cálculo expone el proceso a inconsistencias derivadas de la dependencia del conocimiento individual y de ajustes ad hoc fuera de cualquier marco sistemático.  
  En materia de productividad, la ausencia de una asignación algorítmica por zonas y capacidad resulta en recorridos ineficientes, mayor fatiga laboral y una reducción en el número efectivo de PDV visitados por jornada. El diagnóstico interno reporta baja eficiencia del proceso manual y una incidencia significativa de errores humanos asociados a la dependencia exclusiva de herramientas ofimáticas.  
  En cuanto al nivel de servicio, la ineficiencia en las rutas se traduce en variabilidad en el cumplimiento de frecuencias de visita, dificultades para mantener patrones de atención consistentes y una capacidad de respuesta reducida ante cambios operativos urgentes, comprometiendo la calidad del servicio ofrecida a los clientes estratégicos de la cartera.  
* **Formulación del problema general**  
  ¿De qué manera el desarrollo e implementación de un sistema de software basado en algoritmos de Machine Learning puede mejorar la planificación y asignación de rutas de promotores y puntos de venta en ROM Outsourcing SAC, con el fin de reducir las ineficiencias operativas, incrementar la productividad de las visitas y optimizar la cobertura del servicio en campo?

4. # **Descripción Detallada de la Empresa** {#descripción-detallada-de-la-empresa}

* Misión  
  Brindar soluciones integrales de comercialización que potencien el crecimiento de nuestros clientes, mediante la gestión eficiente de fuerzas de venta, el uso de tecnología e innovación, y el desarrollo del mejor talento, asegurando resultados medibles, calidad en el servicio y optimización de costos  
* Visión  
  Ser el socio estratégico líder en servicios de comercialización en el Perú y la región, reconocido por nuestra capacidad de innovación, excelencia operativa y generación de valor sostenible para nuestros clientes  
* Rubro del negocio  
  ROM Outsourcing SAC es una empresa peruana que opera en el rubro de outsourcing en trade marketing, gestionando promotores y actividades en el punto de venta (PDV) para clientes como Pernod Ricard.  
* Recursos disponibles:  
  * Recursos humanos.  
    * Equipo de Ejecutivos de Cuenta: Encargados de organizar y delegar los requerimientos de los clientes, son la cara visible de la empresa en las reuniones con cliente. Aproximadamente 10 personas.  
    * Equipo de BI: Analistas responsables de mejorar la reportería en base a datos para facilitar la toma de decisiones. Aproximadamente 10 personas  
    * Operaciones (Supervisores y/o coordinadores): Encargados de validar ajustes operativos de campo. Suelen armar las rutas de visita. Aproximadamente: 20 personas  
    * Campo (Promotores y/o mercaderista): Encargados de las ventas y visitas a PDV. Aproximadamente 500 personas  
  * Equipos tecnológicos (hardware y software).  
    * Plataforma ALL IN (versión web y móvil): La versión web permite la asignación de PDV y la generación de reportes operativos; la versión móvil facilita el registro de ingreso a los PDV y la cumplimentación de reportes en tiempo real por el personal de campo.  
    * Nube híbrida: La organización mantiene una base de datos local complementada con almacenamiento en servidores de Amazon Web Services (AWS).  
    * BIWEB: Plataforma web que da visibilidad en tiempo real al cliente de los reportes creados. La reportería se automatiza a través de Jobs usando SQL y Power BI.

5. # **Análisis del Problema o Mejora del Proceso** {#análisis-del-problema-o-mejora-del-proceso}

* Evaluación de los siguientes aspectos:  
  * Funcional: ¿Qué funciones no se cumplen o pueden mejorar?  
    La organización carece de un sistema automatizado para la planificación de rutas, lo que impide el cumplimiento eficiente de funciones operativas clave. Entre las funcionalidades críticas ausentes se identifican:  
* Optimización algorítmica y automática de rutas de visita.  
* Reajuste dinámico de itinerarios ante eventos imprevistos (ausencias, tráfico, campañas especiales).  
* Explotación analítica del historial de visitas para la mejora continua del proceso de planificación.  
* De proceso: ¿Qué pasos del proceso son ineficientes?  
  * La planificación de rutas se fundamenta exclusivamente en la experiencia empírica del personal y en criterios geográficos rudimentarios.  
  * Ausencia de agrupación geográfica sistemática de los PDV, lo que impide la construcción de zonas de atención coherentes y equilibradas.  
  * Generación de recorridos redundantes e innecesarios que incrementan los tiempos y costos de movilización.  
  * Inexistencia de una planificación estructurada de frecuencias de visita semanales, lo que origina tanto duplicidades como brechas de cobertura en determinados PDV.  
  * Organizacional: ¿Cómo afecta a la estructura o roles?  
    * Sobrecarga laboral en el personal de campo, que frecuentemente excede el número recomendado de visitas por jornada.  
    * Incremento de los índices de fatiga laboral y riesgo de rotación de personal, con el consecuente impacto en la continuidad operativa.  
    * Dependencia estructural de analistas y ejecutivos para la toma de decisiones operativas de rutina, lo que genera cuellos de botella.  
    * Dificultad para honrar los compromisos contractuales establecidos con los clientes estratégicos de la cartera.  
  * Tecnológico: ¿Qué limitaciones tecnológicas existen?  
    * Ausencia de sistemas inteligentes específicamente diseñados para la optimización de rutas logísticas.  
    * Subutilización sistemática de los datos disponibles, incluyendo coordenadas GPS, historial de visitas y métricas de desempeño comercial.  
    * Inexistencia de integración con herramientas de análisis avanzado basadas en Machine Learning o inteligencia artificial.  
    * Carencia de una plataforma web centralizada que unifique la gestión operativa bajo un único ecosistema de información.

6. # **Objetivo del Proyecto** {#objetivo-del-proyecto}

* Objetivo General  
  Desarrollar un sistema web inteligente fundamentado en técnicas de Machine Learning que permita optimizar la planificación y asignación de rutas de promotores de trade marketing en ROM Outsourcing SAC, contribuyendo a la mejora sustancial de la eficiencia operativa, la reducción de los costos logísticos y el incremento de la cobertura de puntos de venta.  
* Objetivos Específicos  
* Analizar los datos geográficos y operativos históricos de los puntos de venta y promotores, con el propósito de identificar patrones de ineficiencia estructural en los itinerarios actualmente generados.  
* Diseñar e implementar modelos de Machine Learning específicamente algoritmos de clustering (K-Means) y heurísticas de optimización de recorridos (TSP) orientados a la mejora sistemática de la planificación de rutas diarias.  
* Desarrollar una aplicación web con interfaz gráfica intuitiva que permita a los planificadores visualizar, gestionar y ajustar las rutas generadas de forma dinámica e interactiva.  
* Evaluar el impacto operativo del sistema propuesto mediante métricas cuantificables, incluyendo reducción de tiempos de desplazamiento, disminución de costos logísticos y mejora en la tasa de cobertura efectiva de puntos de venta.

7. # **Alcance del Proyecto** {#alcance-del-proyecto}

* Descripción del proyecto de desarrollo  
  El proyecto tiene por objetivo la construcción de un sistema web inteligente que automatice y optimice la planificación de rutas del equipo de trade marketing. El sistema recopilará y procesará información relativa a la ubicación geográfica, historial de visitas y prioridad comercial de los PDV, así como la disponibilidad y capacidad operativa de los promotores. A partir de dicha información, se aplicarán técnicas de clustering geográfico (K-Means) y algoritmos de optimización de recorridos basados en TSP para generar, de forma automatizada, planes diarios equilibrados y rutas eficientes, presentados a través de una plataforma web interactiva con capacidad de exportación.  
* Descripción de los procesos de negocio involucrados  
  * Planificación y asignación de rutas: Proceso central en el que analistas u operaciones organizan y distribuyen la carga de trabajo diaria o semanal, asignando entre 4 y 6 visitas por promotor según su zona operativa.  
  * Gestión de puntos de venta (PDV): Proceso de mantenimiento y actualización de la información maestra de los clientes, incluyendo coordenadas GPS, ventanas horarias y nivel de prioridad comercial.  
  * Supervisión operativa: Proceso de validación y control previo al despliegue de rutas en campo, verificando el cumplimiento de los SLA y la coherencia operativa de los itinerarios generados.  
* Aspectos dentro del alcance  
  * Carga masiva de datos: Se desarrollará un módulo que permita subir fácilmente archivos, para registrar tanto los puntos de venta (PDVs) como la lista de promotores disponibles.  
  * Sectorización inteligente de clientes: Se implementarán modelos de Machine Learning, como K-Means, que ayudarán a agrupar a los clientes de forma más eficiente según su ubicación y características.  
  * Optimización de rutas: Se integrará un motor basado en el problema del Agente Viajero (TSP) para definir el mejor orden de visitas, buscando reducir al máximo las distancias recorridas.  
  * Interfaz web (dashboard): El sistema contará con una plataforma administrativa donde se podrán visualizar las rutas directamente en mapas interactivos, utilizando herramientas como Leaflet o Google Maps.  
  * Visualización de indicadores clave: Se incluirá un módulo que muestre métricas importantes de cada ruta, como la distancia total estimada, el tiempo de traslado y la carga de trabajo por promotor.  
  * Exportación de rutas:  
  * Las rutas generadas podrán descargarse en formatos como PDF o Excel, facilitando su distribución al equipo en campo.  
* Aspectos fuera del alcance  
  * Desarrollo de una aplicación móvil nativa para el personal de campo.  
  * Seguimiento en tiempo real mediante GPS de los promotores durante la ejecución de sus rutas.  
* Restricciones (tiempo, presupuesto, tecnología, etc.)  
  * Temporal: El proyecto deberá completarse dentro del plazo definido por el ciclo académico vigente.  
  * Presupuestaria: Desarrollo bajo enfoque de costo nulo o mínimo, utilizando exclusivamente capas gratuitas de servicios en la nube para el despliegue inicial.  
  * Tecnológica: Uso exclusivo de herramientas y frameworks de código abierto (Python, PostgreSQL y el ecosistema científico de Python).  
  * De datos: La efectividad del sistema está condicionada a la calidad y precisión de las coordenadas geográficas de los PDV registrados en el sistema.

8. # **Requerimientos del Proyecto** {#requerimientos-del-proyecto}

1) Requerimientos para el desarrollo  
* Recursos humanos (roles y perfiles)  
  * Scrum Master: Jorge Luis Minaya Lopez  
  * Product Owner: Alessandro Miranda Fuentes  
  * Stakeholders: Huaman Lazaro, Daniel Esteban  
  * Scrum Team Members: Daniel Huaman Lazaro  
* Equipos y dispositivos necesarios  
  * Equipos de trabajo: Cada desarrollador deberá contar con una laptop o computadora de escritorio que tenga las características mínimas necesarias para ejecutar modelos de Machine Learning y trabajar con servidores en local.  
  * Software de desarrollo: Se utilizarán distintos programas y herramientas que faciliten el desarrollo, las pruebas y la implementación del sistema.  
  * Conexión a internet estable y de banda ancha para investigación, uso de repositorios en la nube y consumo de APIs de mapas.  
* Programas y herramientas de desarrollo  
  * Entornos de desarrollo (IDE): Los desarrolladores podrán trabajar con herramientas como Visual Studio Code.  
  * Control de versiones: El proyecto se gestionará con Git, utilizando plataformas como GitHub o GitLab para facilitar el trabajo en equipo y el seguimiento de cambios.  
  * Gestión del proyecto: Para organizar las tareas y hacer seguimiento al avance, se usarán herramientas como Notion, aplicando metodologías ágiles como Scrum.  
* Lenguajes y frameworks:  
  * Se trabajará principalmente con Python para todo lo relacionado a datos y Machine Learning, y con Flask o Django para el backend. En el frontend se usarán HTML, CSS y JavaScript, apoyándose en librerías como Bootstrap y Leaflet para mejorar el diseño y la visualización de mapas.  
  * Base de datos: Se utilizarán motores relacionales open source como PostgreSQL o MySQL para almacenar la información del sistema.  
  * Diseño y prototipado: Se empleará Figma para crear los diseños y prototipos de la interfaz web antes de su desarrollo.  
* Mobiliario y espacio físico (si aplica)  
  Dado el contexto actual, el proyecto puede desarrollarse de forma remota o en una modalidad híbrida. Lo ideal es que cada integrante cuente con un espacio de estudio o trabajo cómodo y adecuado (con escritorio y una buena silla) que le permita trabajar sin generar fatiga durante las horas de programación.  
2) Requerimientos para el desarrollo  
* Requerimientos funcionales y no funcionales.

| Código | Nombre | Descripción |
| ----- | ----- | ----- |
| **RF1** | Carga de Datos | El sistema debe permitir al administrador la carga masiva del padrón de PDV y la nómina de promotores mediante archivos CSV o Excel. |
| **RF2** | Segmentación territorial inteligente | Aplicar K-Means para sectorizar geograficamente los clientes de forma automática y equitativa. |
| **RF2** | Optimización de Rutas | Optimizacion de secuencia de visitas con heuristicas TSP para reducir distancia total recorrida. |
| **RF3** | Visualización Cartográfica | Visualizacion de rutas y clusters en mapa web interactivo con colores por zona y lineas de recorrido. |
| **RF4** | Exportación de Rutas | Exportar rutas aprobadas en PDF y Excel para su distribucion al equipo de promotores en campo. |

| Código | Atributo | Descripción |
| ----- | ----- | ----- |
| **RNF1** | Usabilidad | La interfaz gráfica debe ser intuitiva y accesible para usuarios sin formación técnica en programación, con un diseño limpio y flujos de navegación simplificados. |
| **RNF2** | Disponibilidad | El sistema web debe garantizar un tiempo de disponibilidad (uptime) del 99% durante el horario laboral, desplegado en infraestructura cloud. |
| **RNF3** | Seguridad | El acceso a la plataforma debe estar restringido mediante autenticación con credenciales individuales y contraseñas cifradas, limitado al personal autorizado. |
| **RNF4** | Compatibilidad | La plataforma debe ser plenamente funcional en los navegadores Google Chrome, Mozilla Firefox y Microsoft Edge. |


* Backlog


| Product Backlog |  |  |  |  |  |  |
| :---: | ----- | ----- | ----- | ----- | ----- | ----- |
| ID | **Como** | **Quiero** | **Para poder** | **Prioridad** | **Sprint** | **Status** |
| SP-01 |   |  |   |  |  |  |
| SP-02 |   |  |   |  |  |  |
| SP-03 |   |  |   |  |  |  |
| HU-01 | Administrador | Registrar nuevos usuarios asignándoles un rol | Que cada persona acceda solo a las funciones de su cargo | Alta | 1 | Pendiente |
| HU-02 | Cualquier usuario registrado | Iniciar sesión con mi correo y contraseña | Acceder a las funciones habilitadas según mi rol | Alta | 1 | Pendiente |
| HU-03 | Cualquier usuario registrado | Recuperar mi contraseña mediante mi correo registrado | No perder acceso al sistema si la olvido | Media | 1 | Pendiente |
| HU-04 | Administrador / Analista | Registrar puntos de venta con nombre, dirección y coordenadas GPS | Contar con una base de datos actualizada para generar rutas | Alta | 1 | Pendiente |
| HU-05 | Administrador | Registrar promotores con zona, cuenta y disponibilidad | Que el sistema los considere al generar rutas equilibradas | Alta | 1 | Pendiente |
| HU-06 | Supervisor | Registrar la ausencia de un promotor con fecha y motivo | Que el sistema redistribuya sus PDV automáticamente | Alta | 2 | Pendiente |
| HU-07 | Supervisor / Analista | Marcar un PDV como cerrado temporalmente con fechas | Que el sistema no lo incluya en rutas durante ese período | Media | 2 | Pendiente |
| HU-08 | Analista | Cargar un archivo Excel con PDV de una cuenta cliente | Integrar los datos a la base sin digitación manual | Alta | 2 | Pendiente |
| HU-09 | Analista | Generar rutas optimizadas con K-Means y TSP genético | Reducir el tiempo de desplazamiento de los promotores | Alta | 2 | Pendiente |
| HU-10 | Analista | Modificar manualmente una ruta generada por el sistema | Adaptarla a condiciones especiales no capturadas por el algoritmo | Media | 3 | Pendiente |
| HU-11 | Administrador | Configurar reglas de negocio (visitas diarias, horas, no repetición) | Adaptar el comportamiento del algoritmo a las políticas de ROM | Alta | 1 | Pendiente |
| HU-12 | Analista / Ejecutivo | Ver las rutas en un mapa interactivo con PDV marcados por promotor | Revisar gráficamente la distribución antes de aprobarla | Alta | 3 | Pendiente |
| HU-13 | Promotor | Consultar mi ruta del día desde el sistema web en mi celular | Saber qué PDV visitar y en qué orden sin esperar que me lo envíen | Alta | 3 | Pendiente |
| HU-14 | Promotor | Registrar cada visita completada con hora y observaciones | Que el sistema tenga trazabilidad real del cumplimiento de rutas | Alta | 3 | Pendiente |
| HU-15 | Analista | Exportar las rutas generadas en formato Excel y PDF | Compartirlas con el equipo de campo y clientes | Media | 3 | Pendiente |
| HU-16 | Ejecutivo de Cuenta | Ver reporte semanal de cobertura de PDV visitados y no visitados | Identificar brechas y tomar acciones correctivas con el cliente | Alta | 4 | Pendiente |
| HU-17 | Gerente | Ver cuánto tiempo toma generar rutas vs. el proceso manual | Demostrar el ahorro operativo a la dirección | Media | 4 | Pendiente |
| HU-18 | Gerente | Ver estimación de km recorridos y reducción de emisiones CO2 | Evaluar el impacto en costos de movilidad y sostenibilidad | Media | 4 | Pendiente |
| HU-19 | Supervisor | Ver reporte de visitas asignadas vs. realizadas por promotor | Identificar desequilibrios de carga y ajustar asignaciones futuras | Media | 4 | Pendiente |
| HU-20 | Gerente | Contar con un dashboard con indicadores clave del sistema | Monitorear el rendimiento operativo de un vistazo | Alta | 4 | Pendiente |


* Historias de usuario

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 1 | **Usuario:** Administrador |
| **Nombre de la Historia:** | Registro de nuevo usuario |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 3 horas | **Iteración Asignada:** 1 |
| **Programador responsable:** |  |
| **Descripción:** Como administrador, quiero registrar nuevos usuarios en el sistema asignándoles un rol (Analista, Supervisor, Ejecutivo, Promotor, Gerente), para que cada persona acceda solo a las funciones correspondientes a su cargo. |  |
| **Validación: Escenario N°1: Registro exitoso** Dado que el administrador completa el formulario con nombre, correo, contraseña y rol válidos, cuando presiona Registrar, entonces el sistema crea el usuario y envía confirmación al correo.   **Escenario N°2: Correo duplicado** Dado que el correo ingresado ya existe en la base de datos, cuando el administrador intenta registrar, entonces el sistema muestra el mensaje "El correo ya está registrado".   |  |

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 2 | **Usuario:** Cualquier usuario registrado |
| **Nombre de la Historia:** | Inicio de sesión |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 2 horas | **Iteración Asignada:** 1 |
| **Programador responsable:** |  |
| **Descripción:** Como usuario registrado, quiero iniciar sesión con mi correo y contraseña, para acceder a las funciones habilitadas según mi rol. |  |
| **Validación: Escenario N°1: Ingreso exitoso** Dado que el usuario escribe credenciales correctas y registradas, cuando presiona Iniciar sesión, entonces el sistema muestra el dashboard correspondiente a su rol.   **Escenario N°2: Credenciales incorrectas** Dado que el usuario escribe una contraseña incorrecta, cuando presiona Iniciar sesión, entonces el sistema muestra "Usuario y contraseña incorrecto" sin revelar cuál campo falló.   |  |

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 3 | **Usuario:** Cualquier usuario registrado |
| **Nombre de la Historia:** | Recuperación de contraseña |
| **Prioridad de negocio:** Media | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 2 horas | **Iteración Asignada:** 1 |
| **Programador responsable:** |  |
| **Descripción:** Como usuario registrado, quiero recuperar mi contraseña mediante mi correo registrado, para no perder acceso al sistema si la olvido. |  |
| **Validación: Escenario N°1: Enlace enviado** Dado que el usuario ingresa un correo registrado en el sistema, cuando presiona Recuperar contraseña, entonces el sistema envía un enlace de restablecimiento válido por 30 minutos.   **Escenario N°2: Correo no registrado** Dado que el correo ingresado no existe en la base de datos, cuando el usuario presiona Recuperar, entonces el sistema muestra "Correo no encontrado".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 4 | **Usuario:** Administrador / Analista |
| **Nombre de la Historia:** | Registro de punto de venta (PDV) |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 4 horas | **Iteración Asignada:** 1 |
| **Programador responsable:** |  |
| **Descripción:** Como administrador o analista, quiero registrar puntos de venta con nombre, dirección, coordenadas GPS, cuenta cliente y horario de apertura, para contar con una base de datos actualizada que el sistema use para generar rutas. |  |
| **Validación: Escenario N°1: Registro exitoso** Dado que se completan todos los campos obligatorios con coordenadas válidas, cuando se presiona Guardar PDV, entonces el sistema almacena el registro y lo muestra en el listado.   **Escenario N°2: PDV duplicado** Dado que ya existe un PDV con el mismo nombre y coordenadas, cuando el usuario intenta registrar, entonces el sistema muestra "PDV ya registrado".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 5 | **Usuario:** Administrador |
| **Nombre de la Historia:** | Registro de promotor |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 3 horas | **Iteración Asignada:** 1 |
| **Programador responsable:** |  |
| **Descripción:** Como administrador, quiero registrar promotores con su nombre, zona asignada, cuenta que atiende y disponibilidad semanal, para que el sistema los considere al generar rutas equilibradas. |  |
| **Validación: Escenario N°1: Registro exitoso** Dado que el administrador completa todos los datos del promotor, cuando presiona Guardar, entonces el sistema crea el promotor vinculado a su usuario con rol Promotor.   **Escenario N°2: Datos incompletos** Dado que el administrador deja campos obligatorios vacíos, cuando presiona Guardar, entonces el sistema resalta los campos faltantes y no permite continuar.   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 6 | **Usuario:** Supervisor |
| **Nombre de la Historia:** | Registro de ausencia de promotor |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 4 horas | **Iteración Asignada:** 2 |
| **Programador responsable:** |  |
| **Descripción:** Como supervisor, quiero registrar la ausencia de un promotor indicando fecha y motivo, para que el sistema redistribuya automáticamente sus PDV del día entre los promotores disponibles. |  |
| **Validación: Escenario N°1: Redistribución exitosa** Dado que el supervisor registra la ausencia de un promotor con fecha y motivo, cuando confirma, entonces el sistema redistribuye los PDV respetando el límite de 4 a 6 visitas diarias por promotor disponible.   **Escenario N°2: Sin promotores disponibles** Dado que no hay promotores disponibles para reasignación, cuando el supervisor registra la ausencia, entonces el sistema muestra "No hay promotores disponibles para redistribuir las rutas".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 7 | **Usuario:** Supervisor / Analista |
| **Nombre de la Historia:** | Registro de cierre temporal de PDV |
| **Prioridad de negocio:** Media | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 2 horas | **Iteración Asignada:** 2 |
| **Programador responsable:** |  |
| **Descripción:** Como supervisor o analista, quiero marcar un PDV como cerrado temporalmente con fecha de inicio y fin, para que el sistema no lo incluya en rutas durante ese período. |  |
| **Validación: Escenario N°1: Cierre registrado** Dado que se ingresa el PDV, fecha de inicio y fecha de reapertura, cuando se confirma el cierre, entonces el sistema excluye ese PDV de las rutas generadas durante ese período.   **Escenario N°2: Reapertura automática** Dado que se cumple la fecha de reapertura definida, cuando el sistema genera nuevas rutas, entonces el PDV vuelve a estar disponible automáticamente.   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 8 | **Usuario:** Analista |
| **Nombre de la Historia:** | Carga masiva de PDV desde Excel |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 5 horas | **Iteración Asignada:** 2 |
| **Programador responsable:** |  |
| **Descripción:** Como analista, quiero cargar un archivo Excel con los PDV de una cuenta cliente, para que el sistema los procese e integre a la base de datos sin digitación manual. |  |
| **Validación: Escenario N°1: Carga exitosa** Dado que el archivo .xlsx tiene columnas correctas (nombre, dirección, latitud, longitud, cuenta), cuando se carga, entonces el sistema muestra el resumen de registros importados y errores encontrados.   **Escenario N°2: Formato incorrecto** Dado que el archivo no tiene las columnas requeridas, cuando se intenta cargar, entonces el sistema muestra "Formato de archivo incorrecto" y no realiza ninguna importación.   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 9 | **Usuario:** Analista |
| **Nombre de la Historia:** | Generación automática de rutas con ML |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Alta |
| **Puntos estimados:** 13 horas | **Iteración Asignada:** 2 |
| **Programador responsable:** |  |
| **Descripción:** Como analista, quiero que el sistema genere rutas optimizadas agrupando PDV por zonas geográficas con K-Means y aplicando TSP con algoritmos genéticos, para reducir el tiempo de desplazamiento de los promotores. |  |
| **Validación: Escenario N°1: Generación exitosa** Dado que existen PDV y promotores registrados, cuando el analista ejecuta la optimización, entonces el sistema genera rutas con entre 4 y 6 visitas diarias por promotor sin repetir PDV en días consecutivos de la misma semana.   **Escenario N°2: Sin datos suficientes** Dado que no hay PDV cargados para la cuenta seleccionada, cuando se intenta generar rutas, entonces el sistema muestra "No hay datos suficientes para generar rutas".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 10 | **Usuario:** Analista |
| **Nombre de la Historia:** | Ajuste manual de ruta generada |
| **Prioridad de negocio:** Media | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 5 horas | **Iteración Asignada:** 3 |
| **Programador responsable:** |  |
| **Descripción:** Como analista, quiero modificar manualmente una ruta generada por el sistema (agregar, quitar o reordenar PDV), para adaptarla a condiciones especiales no capturadas por el algoritmo. |  |
| **Validación: Escenario N°1: Ajuste aplicado** Dado que el analista modifica el orden o la composición de una ruta, cuando guarda los cambios, entonces el sistema recalcula el tiempo estimado y registra quién realizó el ajuste y en qué fecha.   **Escenario N°2: Ajuste supera límite de visitas** Dado que el analista agrega un PDV que supera las 6 visitas diarias, cuando intenta guardar, entonces el sistema muestra una advertencia "Se superó el límite de visitas diarias permitidas".   |  |

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 11 | **Usuario:** Administrador |
| **Nombre de la Historia:** | Configuración de reglas de negocio |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 4 horas | **Iteración Asignada:** 1 |
| **Programador responsable:** |  |
| **Descripción:** Como administrador, quiero configurar las reglas del sistema (mínimo y máximo de visitas diarias, horas máximas de jornada, días de no repetición), para adaptar el comportamiento del algoritmo a las políticas de ROM Outsourcing SAC. |  |
| **Validación: Escenario N°1: Configuración guardada** Dado que el administrador actualiza los parámetros en el panel de configuración, cuando presiona Guardar, entonces los nuevos valores se aplican desde la siguiente generación de rutas.   **Escenario N°2: Valor inválido** Dado que el administrador ingresa un valor fuera del rango permitido (ej. máximo de visitas mayor a 10), cuando intenta guardar, entonces el sistema muestra un mensaje de validación indicando el rango aceptado.   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 12 | **Usuario:** Analista / Ejecutivo |
| **Nombre de la Historia:** | Visualización de rutas en mapa interactivo |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 8 horas | **Iteración Asignada:** 3 |
| **Programador responsable:** |  |
| **Descripción:** Como analista o ejecutivo, quiero ver las rutas generadas sobre un mapa interactivo con los PDV marcados por promotor y día, para revisar gráficamente la distribución antes de aprobarla. |  |
| **Validación: Escenario N°1: Mapa cargado correctamente** Dado que existen rutas generadas para la semana seleccionada, cuando el usuario accede al módulo de mapa, entonces el sistema muestra los PDV con colores diferenciados por promotor y permite filtrar por día.   **Escenario N°2: Sin rutas generadas** Dado que no existen rutas para el período seleccionado, cuando el usuario accede al mapa, entonces el sistema muestra el mensaje "No hay rutas generadas para el período seleccionado".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 13 | **Usuario:** Promotor |
| **Nombre de la Historia:** | Consulta de ruta diaria desde dispositivo móvil |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 5 horas | **Iteración Asignada:** 3 |
| **Programador responsable:** |  |
| **Descripción:** Como promotor, quiero consultar mi ruta del día desde el sistema web en mi celular, para saber qué PDV visitar y en qué orden sin esperar que me lo envíen por WhatsApp o correo. |  |
| **Validación: Escenario N°1: Ruta disponible** Dado que el promotor inicia sesión en el sistema desde su celular, cuando accede a Mi ruta del día, entonces el sistema muestra los PDV en orden de visita con nombre, dirección y hora estimada.   **Escenario N°2: Sin ruta asignada** Dado que el promotor no tiene rutas asignadas para el día, cuando accede al módulo de ruta, entonces el sistema muestra "No tienes PDV asignados para hoy".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 14 | **Usuario:** Promotor |
| **Nombre de la Historia:** | Registro de visita realizada |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 4 horas | **Iteración Asignada:** 3 |
| **Programador responsable:** |  |
| **Descripción:** Como promotor, quiero registrar cada visita completada indicando hora de llegada y observaciones, para que el sistema tenga trazabilidad real del cumplimiento de rutas. |  |
| **Validación: Escenario N°1: Visita registrada** Dado que el promotor accede a un PDV de su ruta y presiona Registrar visita, cuando completa la hora de entrada, salida y observaciones, entonces el sistema guarda el registro y marca el PDV como visitado.   **Escenario N°2: PDV no disponible** Dado que el PDV aparece cerrado al momento de la visita, cuando el promotor selecciona No visitado e ingresa el motivo, entonces el sistema registra el PDV como pendiente con la razón indicada.   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 15 | **Usuario:** Analista |
| **Nombre de la Historia:** | Exportación de rutas en Excel y PDF |
| **Prioridad de negocio:** Media | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 3 horas | **Iteración Asignada:** 3 |
| **Programador responsable:** |  |
| **Descripción:** Como analista, quiero exportar las rutas generadas en formato Excel y PDF, para compartirlas con el equipo de campo y con los clientes sin necesidad de acceder al sistema. |  |
| **Validación: Escenario N°1: Exportación exitosa** Dado que existen rutas generadas para la semana y cuenta seleccionada, cuando el analista presiona Exportar, entonces el sistema descarga el archivo con promotor, PDV, dirección, día y hora estimada.   **Escenario N°2: Sin datos para exportar** Dado que no existen rutas en el período seleccionado, cuando el analista presiona Exportar, entonces el sistema muestra "No hay rutas disponibles para exportar en el período indicado".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 16 | **Usuario:** Ejecutivo de Cuenta |
| **Nombre de la Historia:** | Reporte de cobertura de PDV |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 5 horas | **Iteración Asignada:** 4 |
| **Programador responsable:** |  |
| **Descripcion:** Como ejecutivo de cuenta, quiero ver un reporte semanal de cobertura que muestre qué PDV fueron visitados y cuáles no, para identificar brechas y tomar acciones correctivas con el cliente. |  |
| **Validación: Escenario N°1: Reporte generado** Dado que el ejecutivo selecciona una semana y cuenta cliente, cuando accede al módulo de reporte, entonces el sistema muestra el porcentaje de cobertura por zona, promotor y cuenta con PDV visitados y no visitados.   **Escenario N°2: Sin registros de visita** Dado que no hay visitas registradas para el período seleccionado, cuando el ejecutivo genera el reporte, entonces el sistema muestra "No existen registros de visita para el período indicado".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 17 | **Usuario:** Gerente |
| **Nombre de la Historia:** | Reporte de tiempo de planificación |
| **Prioridad de negocio:** Media | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 4 horas | **Iteración Asignada:** 4 |
| **Programador responsable:** |  |
| **Descripción:** Como gerente, quiero ver cuánto tiempo toma generar rutas con el sistema comparado con el proceso manual anterior, para demostrar el ahorro operativo a la dirección. |  |
| **Validación: Escenario N°1: Comparativo disponible** Dado que existen registros de generación de rutas con el sistema, cuando el gerente accede al reporte, entonces el sistema muestra el tiempo promedio actual vs. la línea base manual de 60 a 90 minutos.   **Escenario N°2: Sin datos comparativos** Dado que aún no existe suficiente historial de uso del sistema, cuando el gerente accede al reporte, entonces el sistema muestra "Se requieren más registros para generar el comparativo".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Número:** 18 | **Usuario:** Gerente |
| **Nombre de la Historia:** | Reporte de kilómetros recorridos y emisiones |
| **Prioridad de negocio:** Media | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 4 horas | **Iteración Asignada:** 4 |
| **Programador responsable:** |  |
| **Descripcion:** Como gerente, quiero ver la estimación de kilómetros totales recorridos por semana y la reducción comparativa con rutas manuales, para evaluar el impacto en costos de movilidad y emisiones de CO2. |  |
| **Validación: Escenario N°1: Reporte generado** Dado que existen rutas ejecutadas en el período seleccionado, cuando el gerente accede al módulo, entonces el sistema calcula km totales por promotor y muestra la reducción porcentual vs. línea base con estimación de CO2 ahorrado.   **Escenario N°2: Datos insuficientes** Dado que no hay suficientes rutas completadas en el período, cuando el gerente accede al reporte, entonces el sistema muestra "Datos insuficientes para calcular la reducción de emisiones".   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 19 | **Usuario:** Supervisor |
| **Nombre de la Historia:** | Reporte de carga de trabajo por promotor |
| **Prioridad de negocio:** Media | **Riesgo de desarrollo:** Baja |
| **Puntos estimados:** 3 horas | **Iteración Asignada:** 4 |
| **Programador responsable:** |  |
| **Descripción:** Como supervisor, quiero ver un reporte de visitas asignadas vs. realizadas por cada promotor en la semana, para identificar desequilibrios de carga y ajustar asignaciones futuras. |  |
| **Validación: Escenario N°1: Reporte con alerta de desequilibrio** Dado que un promotor supera el 20% de diferencia respecto al promedio del equipo, cuando el supervisor accede al reporte semanal, entonces el sistema resalta visualmente al promotor con sobrecarga o subcarga.   **Escenario N°2: Carga equilibrada** Dado que todos los promotores tienen una distribución dentro del rango aceptable, cuando el supervisor accede al reporte, entonces el sistema muestra el listado sin alertas de desequilibrio.   |  |

 

| Historia de Usuario |  |
| ----- | ----- |
| **Numero:** 20 | **Usuario:** Gerente |
| **Nombre de la Historia:** | Dashboard ejecutivo de métricas clave |
| **Prioridad de negocio:** Alta | **Riesgo de desarrollo:** Media |
| **Puntos estimados:** 8 horas | **Iteración Asignada:** 4 |
| **Programador responsable:** |  |
| **Descripcion:** Como gerente, quiero un dashboard con los indicadores principales del sistema (cobertura de PDV, km recorridos, tiempo de planificación, ausencias registradas), para monitorear el rendimiento operativo de un vistazo. |  |
| **Validación: Escenario N°1: Dashboard cargado** Dado que el gerente inicia sesión y accede al dashboard, cuando selecciona un rango de fechas y cuenta cliente, entonces el sistema muestra los indicadores actualizados con comparativos semana a semana y flechas de tendencia.   **Escenario N°2: Sin datos en el período** Dado que no existen datos operativos en el período seleccionado, cuando el gerente accede al dashboard, entonces el sistema muestra "Sin datos disponibles para el período indicado" en cada indicador.   |  |

* Identificación de procesos del negocio.  
  * Recopilación de Insumos: El equipo operativo define la "cuota" de visitas semanales y la disponibilidad de la planilla de promotores.  
  * Ingesta y Parametrización (Input): El usuario ingresa a la plataforma web, carga la base de datos actualizada y define los parámetros del día.  
  * Ajuste y Control de Calidad: El analista visualiza el output en el mapa. Revisa las cargas de trabajo (ej. verifica que cada promotor tenga entre 4 y 6 visitas) y realiza ajustes manuales menores si el conocimiento empírico lo demanda.  
  * Aprobación y Despliegue (Output): El analista bloquea la ruta, la exporta y la distribuye mediante los canales de comunicación de la empresa para la ejecución en campo.  
* Identificación de los sprints (si se usa metodología ágil).  
  * Sprint 1: Configuración de la Arquitectura e Interfaz Base.  
    Definición de repositorios y stack tecnológico (Python/Flask, DB, Frontend).  
    Diseño y modelado de la base de datos.  
    Desarrollo de la pantalla de inicio de sesión (Login/Auth) y el cascarón del Dashboard principal (UI/UX).  
* Sprint 2: Gestión de Datos y Visualización Geográfica.

  Desarrollo del módulo de importación masiva de datos (Lectura de CSV/Excel).

  Integración de la librería de mapas (ej. Leaflet.js o Google Maps API).

  Ploteo (marcadores) de los PDVs en bruto sobre el mapa interactivo.

* Sprint 3: Integración del Motor de Inteligencia (Machine Learning).

  Codificación e integración del algoritmo K-Means para agrupar los puntos de venta.

  Codificación e integración de las heurísticas de optimización (TSP) para definir la secuencia de los puntos.

  Representación visual de los clústeres y trazado de las líneas de ruta en el mapa.

* Sprint 4: Refinamiento, Ajustes Manuales y Entrega del MVP.

  Desarrollo de la funcionalidad para reasignación manual de rutas (Edición "Drag & Drop" o mediante formulario).

  Creación del módulo de reportes y exportación (generación de PDFs).

  Pruebas de calidad (QA), corrección de errores (bugs) y despliegue del software en un servidor en la nube para su uso en etapa de piloto.

9. # **Estrategia del Desarrollo** {#estrategia-del-desarrollo}

* Metodología seleccionada (Scrum, XP, RUP, etc.).  
  Para el desarrollo del presente proyecto se adopta el marco de trabajo Scrum. Conforme a la definición de Schwaber y Sutherland (2020), Scrum constituye un marco de trabajo liviano que habilita a los equipos y organizaciones para generar valor a través de soluciones adaptativas aplicadas a problemas complejos. A diferencia de las metodologías tradicionales, Scrum establece un conjunto mínimo de reglas que estructuran la forma en que el equipo planifica, ejecuta, inspecciona y adapta su trabajo de forma iterativa e incremental.  
  El plan de desarrollo contempla cuatro sprints de tres semanas de duración cada uno, precedidos por una fase de levantamiento de información y una fase de diseño de arquitectura y prototipos, abarcando en su totalidad las 18 semanas del ciclo académico.  
* Justificación de la elección.  
  La decisión de adoptar Scrum responde a razones concretas relacionadas con la naturaleza exploratoria del proyecto. Si bien el alcance general del sistema está delimitado optimizar rutas de promotores mediante Machine Learning, los requisitos funcionales detallados evolucionarán a medida que avance el desarrollo. Al trabajar con algoritmos de clustering geográfico como K-Means, los resultados intermedios pueden exigir la reconfiguración de la interfaz o de la lógica de asignación. Un enfoque en cascada no tolera este tipo de ajustes iterativos, lo que lo hace inadecuado para proyectos con alto componente de exploración algorítmica.  
* Herramientas de gestión y desarrollo  
  * Gestión del proyecto (Scrum): Se utilizará Jira para la planificación y seguimiento de los sprints, gestión del backlog, historias de usuario y control del avance del equipo. Alternativamente, se puede emplear Trello para una gestión más visual mediante tableros Kanban.  
  * Control de versiones: Se utilizará Git junto con GitHub para el versionamiento del código, trabajo colaborativo y gestión de ramas (branches).

10. # **Cronograma de Desarrollo** {#cronograma-de-desarrollo}

* Etapas o fases del proyecto:  
* El proyecto se distribuye en ocho fases a lo largo de las 18 semanas del ciclo académico. Las dos primeras fases corresponden a la preparación del proyecto; los cuatro sprints centrales constituyen el núcleo del desarrollo incremental del sistema; y las dos semanas finales se destinan a las pruebas de calidad y a la exposición y entrega formal.  
* Duración estimada de cada fase

| Fase / Actividad | Semanas | Inicio | Fin |
| :---- | :---: | :---: | :---: |
| Levantamiento de informacion | S1-S2 | Sem. 1 | Sem. 2 |
| Diseno (prototipos, BD, arquitectura) | S3-S4 | Sem. 3 | Sem. 4 |
| Sprint 1: Arquitectura e Interfaz Base | S5-S7 | Sem. 5 | Sem. 7 |
| Sprint 2: Datos y Visualizacion Geografica | S8-S10 | Sem. 8 | Sem. 10 |
| Sprint 3: Motor de ML (K-Means \+ TSP) | S11-S13 | Sem. 11 | Sem. 13 |
| Sprint 4: Refinamiento, Ajustes y MVP | S14-S16 | Sem. 14 | Sem. 16 |
| Pruebas finales y QA | S17 | Sem. 17 | Sem. 17 |
| Exposicion y entrega final | S18 | Sem. 18 | Sem. 18 |


* Calendario gráfico (Gantt u otro formato visual)

| Fase / Actividad |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Levantamiento de informacion |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Diseno (prototipos, BD, arq.) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sprint 1: Arquitectura e Interfaz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sprint 2: Datos y Mapas  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sprint 3: Motor ML (K-Means+TSP) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sprint 4: Refinamiento y MVP |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Pruebas finales y QA  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Exposicion y entrega final  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Entregables academicos  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


  


  


  


  


  


  


  


  


  


  


  

11. # **Diseño de la Base de datos**

12. **Análisis de los requerimientos del negocio**

**A. Requerimientos e Historias de Usuario Priorizadas y Estimadas**

Para el desarrollo del sistema web inteligente orientado a la optimización de rutas de promotores en ROM Outsourcing SAC, se aplicó un enfoque basado en la metodología ágil Scrum. Esto permitió identificar, priorizar y estimar las historias de usuario según el valor de negocio, complejidad técnica e impacto operativo.

La priorización consideró las necesidades críticas del negocio, enfocándose en la automatización de la planificación de rutas, reducción de tiempos operativos y mejora de la cobertura de puntos de venta (PDV). La estimación del esfuerzo se realizó mediante la técnica de Story Points con la secuencia de Fibonacci (1, 2, 3, 5, 8, 13).

 

## **A.1 Criterios de Priorización y Estimación**

•       Alta prioridad: Funcionalidades esenciales para el funcionamiento principal del sistema (MVP).

•       Media prioridad: Funcionalidades importantes, pero no críticas para el MVP.

•       Baja prioridad: Funcionalidades complementarias o de mejora futura.

 

Las estimaciones consideraron los siguientes factores:

–      Complejidad técnica del módulo.

–      Tiempo estimado de desarrollo.

–      Dependencias entre módulos del sistema.

–      Riesgo de implementación.

 

## **A.2 Product Backlog Priorizado**

La siguiente tabla presenta las nueve historias de usuario identificadas, ordenadas según su prioridad y asignadas al sprint correspondiente:

 

| ID | Historia de Usuario | Actor | Prioridad | SP | Sprint | Criterio de Aceptación |
| :---: | :---- | :---- | :---: | :---: | :---: | :---- |
| **HU01** | **Como Administrador, quiero iniciar sesión mediante autenticación segura para proteger el acceso a la plataforma** | **Administrador** | **Alta** | **3** | **Sprint 1** | **El usuario accede correctamente con credenciales válidas** |
| **HU02** | **Como Analista, quiero cargar archivos Excel/CSV con los PDV para evitar el registro manual de datos** | **Analista de Planificación** | **Muy Alta** | **5** | **Sprint 2** | **El sistema importa archivos sin errores** |
| **HU03** | **Como Analista, quiero visualizar los PDV en un mapa interactivo para identificar su distribución geográfica** | **Analista de Planificación** | **Alta** | **5** | **Sprint 2** | **Los PDV se muestran correctamente en el mapa** |
| **HU04** | **Como Analista, quiero que el sistema agrupe automáticamente los clientes por zonas (K-Means) para distribuir equitativamente el trabajo** | **Analista de Planificación** | **Muy Alta** | **8** | **Sprint 3** | **El sistema genera agrupaciones automáticas con K-Means** |
| **HU05** | **Como Analista, quiero optimizar automáticamente las rutas de visita para minimizar tiempos de desplazamiento** | **Analista de Planificación** | **Muy Alta** | **8** | **Sprint 3** | **El sistema genera rutas optimizadas con heurísticas TSP** |
| **HU06** | **Como Supervisor, quiero validar las rutas generadas antes de su aprobación para asegurar el cumplimiento de SLA** | **Supervisor Operativo** | **Alta** | **5** | **Sprint 4** | **El supervisor visualiza y aprueba rutas correctamente** |
| **HU07** | **Como Ejecutivo de Cuenta, quiero reasignar clientes entre promotores para responder ante ausencias o cambios operativos** | **Ejecutivo de Cuenta** | **Media** | **5** | **Sprint 4** | **El sistema reasigna clientes entre promotores** |
| **HU08** | **Como Analista, quiero visualizar rutas optimizadas en el mapa para validar la lógica geográfica del recorrido** | **Analista de Planificación** | **Alta** | **5** | **Sprint 4** | **Las rutas generadas se muestran sobre el mapa** |
| **HU09** | **Como Analista, quiero exportar las rutas aprobadas en PDF o Excel para compartirlas con el equipo de campo** | **Analista de Planificación** | **Alta** | **3** | **Sprint 4** | **El sistema exporta correctamente los reportes** |

 

## **A.3 Resumen de Estimación por Sprint**

| Sprint | Enfoque Principal | HU incluidas | Story Points |
| :---: | :---- | :---: | :---: |
| **Sprint 1** | **Arquitectura base y autenticación** | **HU01** | **3** |
| **Sprint 2** | **Carga de datos y visualización geográfica** | **HU02, HU03** | **10** |
| **Sprint 3** | **Motor de Machine Learning y optimización** | **HU04, HU05** | **16** |
| **Sprint 4** | **Refinamiento, ajustes manuales y MVP** | **HU06, HU07, HU08, HU09** | **18** |
| **TOTAL** |   | **9 HU** | **47 SP** |

 

La distribución de Story Points refleja la complejidad técnica de cada módulo. Los componentes de Machine Learning (Sprint 3\) y las funcionalidades finales del MVP (Sprint 4\) concentran el mayor esfuerzo, debido al procesamiento de datos geográficos, entrenamiento de modelos y validación de resultados. Las funcionalidades administrativas (autenticación, exportación) fueron estimadas con menor complejidad al contar con bibliotecas disponibles.

 **B. Planificación del Sprint y Procesos del Negocio**  
 

Se adoptó la metodología ágil Scrum para el desarrollo del sistema, con una duración de dos semanas por sprint. La planificación se estructuró considerando las necesidades operativas del negocio, las dependencias técnicas y la prioridad de las historias de usuario definidas en la sección anterior.

 

## **B.1 Planificación General de Sprints**

| Sprint | Objetivo del Sprint | Duración | Story Points |
| :---: | :---- | :---: | :---: |
| **Sprint 1** | **Implementar la arquitectura base del sistema, módulo de autenticación e interfaz inicial del dashboard** | **2 semanas** | **3 SP** |
| **Sprint 2** | **Desarrollar el módulo de carga masiva de datos (CSV/Excel) e integrar visualización geográfica de PDV** | **2 semanas** | **10 SP** |
| **Sprint 3** | **Implementar el motor de Machine Learning: clustering K-Means y optimización de rutas con heurísticas TSP** | **2 semanas** | **16 SP** |
| **Sprint 4** | **Implementar validación de rutas, ajustes manuales, exportación de reportes y despliegue del MVP** | **2 semanas** | **18 SP** |

 

## **B.2 Procesos del Negocio Involucrados**

El sistema impactará directamente en los siguientes procesos críticos de ROM Outsourcing SAC:

 

**Proceso 1 – Recopilación de Insumos:**

El equipo operativo recopila información sobre la disponibilidad de promotores, ubicación de PDV, prioridades comerciales y restricciones operativas. Entradas: lista de promotores, base de PDV, restricciones de negocio, horarios. Salida: datos preparados para carga al sistema.

**Proceso 2 – Ingesta y Parametrización:**

El analista carga información al sistema mediante archivos Excel/CSV y configura los parámetros de optimización (número de clusters, capacidad máxima por promotor). Entradas: archivos Excel/CSV, parámetros de clustering. Salida: datos procesados y almacenados en base de datos.

**Proceso 3 – Optimización Inteligente:**

El motor de ML aplica K-Means para segmentar los PDV por zonas y TSP para calcular la secuencia óptima de visitas por promotor. Entradas: PDV con coordenadas GPS, disponibilidad de promotores. Salida: rutas optimizadas con carga balanceada.

**Proceso 4 – Ajuste y Control de Calidad:**

El analista revisa las rutas en el mapa interactivo, verifica la carga por promotor (4-6 visitas/día) y realiza ajustes manuales si el conocimiento empírico lo requiere. Salida: rutas validadas.

**Proceso 5 – Aprobación y Despliegue:**

El analista bloquea las rutas aprobadas, las exporta en PDF/Excel y las distribuye al equipo de campo a través de los canales de comunicación de la empresa. Salida: plan de rutas distribuido.

   
**Diagrama General de Clases del Sistema**  
 El siguiente diagrama representa la estructura general del sistema propuesto para ROM Outsourcing SAC, mostrando las entidades principales, relaciones y funcionalidades involucradas en el proceso de autenticación, gestión de puntos de venta, optimización inteligente de rutas, visualización geográfica y generación de reportes.  
   
 **![][image2]**  
   
   
   
   
   
   
   
   
   
 **C. Historias de Usuario por Sprint y Diagramas**  
 

A continuación, se presentan las historias de usuario asignadas a cada sprint, junto con el Sprint Backlog, Burndown Chart y los diagramas UML correspondientes (Casos de Uso, Clases, Secuencia y Actividades).

 

## **C.1 Sprint 1 – Configuración Base del Sistema**

| Objetivo: | Implementar la estructura principal del sistema: autenticación, configuración del entorno y estructura inicial de la interfaz web. |
| :---- | :---- |
| **Duración:** | **2 semanas (10 días hábiles)** |
| **Story Points:** | **3 SP** |
| **Responsable:** | **Scrum Team – Backend \+ Frontend** |

   
**Historias de Usuario – Sprint 1**

| ID | Historia de Usuario | Actor | Prioridad | SP |
| :---: | :---- | :---- | :---: | :---: |
| **HU01** | **Como Administrador del Sistema, quiero iniciar sesión mediante autenticación segura para proteger el acceso a la plataforma** | **Administrador** | **Alta** | **3** |

   
**Sprint Backlog – Sprint 1**

| Tarea | Responsable | Estado |
| :---- | :---: | :---: |
| **Configuración del repositorio GitHub y branching strategy** | **Backend Team** |  **Planificado** |
| **Configuración del entorno de desarrollo (Python, Flask/Django)** | **Backend Team** |  **Planificado** |
| **Diseño y modelado inicial de la base de datos** | **Backend Team** | **Planificado** |
| **Implementación del sistema de autenticación (usuario/contraseña encriptada)** | **Backend Team** |  **Planificado** |
| **Configuración del control de accesos por roles** | **Backend Team** |  **Planificado** |
| **Diseño del cascarón del Dashboard administrativo** | **Frontend Team** | **Planificado** |
| **Pruebas de acceso y validación del módulo de login** | **Scrum Team** | **Planificado** |

   
**Burndown Chart – Sprint 1**

La siguiente tabla muestra la evolución del trabajo restante durante los 8 días del Sprint 1 (3 SP iniciales):

 

| Día | Trabajo Restante (SP) | Línea Ideal | Progreso |
| :---: | :---: | :---: | :---: |
| **Día 1** | **3 SP** | **3 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 2** | **3 SP** | **3 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 3** | **2 SP** | **2 SP** | **███████░░░░░░░░░░░░░** |
| **Día 4** | **2 SP** | **2 SP** | **███████░░░░░░░░░░░░░** |
| **Día 5** | **1 SP** | **1 SP** | **█████████████░░░░░░░** |
| **Día 6** | **1 SP** | **1 SP** | **█████████████░░░░░░░** |
| **Día 7** | **0 SP** | **0 SP** | **████████████████████** |
| **Día 8** | **0 SP** | **0 SP** | **████████████████████** |

 

### **Diagrama de Casos de Uso – Sprint 1**

Actor principal: Administrador del Sistema. El siguiente diagrama describe las interacciones del Administrador con el módulo de autenticación:

 

###  

###  

###  

###  

###  

###  

###  

###  

###  

###  

###  **Diagrama de Clases – Sprint 1**

###  **![][image3]**

###   **Diagrama de Secuencia – Sprint 1**

Flujo de autenticación: desde el ingreso de credenciales hasta el acceso al dashboard. 

###  **![][image4]**

###  **Diagrama de Actividades – Sprint 1** 

###  **![][image5]**

###  

###  

###  

###  

###  

###  

###  

###  

###  

###  

##  

##  

##  **C.2 Sprint 2 – Gestión de Datos y Visualización Geográfica**

| Objetivo: | Implementar el módulo de carga masiva de datos y la visualización geográfica de PDV en mapa interactivo. |
| :---- | :---- |
| **Duración:** | **2 semanas (10 días hábiles)** |
| **Story Points:** | **10 SP** |
| **Responsable:** | **Backend Team (importación) \+ Frontend Team (mapas)** |

 

### **Historias de Usuario – Sprint 2**

| ID | Historia de Usuario | Actor | Prioridad | SP |
| :---: | :---- | :---- | :---: | :---: |
| **HU02** | **Como Analista de Planificación, quiero cargar archivos Excel o CSV con los PDV para evitar el registro manual de datos** | **Analista de Planificación** | **Muy Alta** | **5** |
| **HU03** | **Como Analista de Planificación, quiero visualizar los PDV en un mapa interactivo para identificar su distribución geográfica** | **Analista de Planificación** | **Alta** | **5** |

 

### **Sprint Backlog – Sprint 2**

| Tarea | Responsable | Estado |
| :---- | :---: | :---: |
| **Diseñar módulo de carga de archivos (UI)** | **Frontend Team** | **Planificado** |
| **Programar importación y parseo de CSV/Excel** | **Backend Team** | **Planificado** |
| **Validar estructura y datos del archivo importado** | **Backend Team** | **Planificado** |
| **Registrar automáticamente PDV en la base de datos** | **Backend Team** | **Planificado** |
| **Integrar librería Leaflet.js en el frontend** | **Frontend Team** | **Planificado** |
| **Mostrar marcadores de PDV sobre el mapa interactivo** | **Frontend Team** | **Planificado** |
| **Crear marcadores dinámicos con información del PDV** | **Scrum Team** | **Planificado** |

 

### **Burndown Chart – Sprint 2**

| Día | Trabajo Restante (SP) | Línea Ideal | Progreso |
| :---: | :---: | :---: | :---: |
| **Día 1** | **10 SP** | **10 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 2** | **10 SP** | **9 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 3** | **8 SP** | **7 SP** | **████░░░░░░░░░░░░░░░░** |
| **Día 4** | **7 SP** | **6 SP** | **██████░░░░░░░░░░░░░░** |
| **Día 5** | **5 SP** | **4 SP** | **██████████░░░░░░░░░░** |
| **Día 6** | **3 SP** | **3 SP** | **██████████████░░░░░░** |
| **Día 7** | **1 SP** | **1 SP** | **██████████████████░░** |
| **Día 8** | **0 SP** | **0 SP** | **████████████████████** |

 

### **Diagrama de Casos de Uso – Sprint 2**

![][image6] 

###  

###  

###  

###  **Diagrama de Clases – Sprint 2**

### **![][image7]** 

###   **Diagrama de Secuencia – Sprint 2**

### **![][image8]** 

###  

###  

###  **Diagrama de Actividades – Sprint 2**

### **![][image9]** 

###  

###  

###  

###  

###  

###  

###  

###  

###  

###  

###  

###  

###  **C.3 Sprint 3 – Integración del Motor de Machine Learning**

| Objetivo: | Implementar los algoritmos de ML para agrupar PDV por zonas (K-Means) y calcular secuencias de visita óptimas (TSP). |
| :---- | :---- |
| **Duración:** | **2 semanas (10 días hábiles)** |
| **Story Points:** | **16 SP** |
| **Responsable:** | **Backend Team (ML) \+ Frontend Team (visualización de clusters)** |

 

### **Historias de Usuario – Sprint 3**

| ID | Historia de Usuario | Actor | Prioridad | SP |
| :---: | :---- | :---- | :---: | :---: |
| **HU04** | **Como Analista de Planificación, quiero que el sistema agrupe automáticamente los clientes por zonas usando K-Means para distribuir equitativamente la carga laboral** | **Analista de Planificación** | **Muy Alta** | **8** |
| **HU05** | **Como Analista de Planificación, quiero optimizar automáticamente las rutas de visita para minimizar tiempos de desplazamiento** | **Analista de Planificación** | **Muy Alta** | **8** |

 

### **Sprint Backlog – Sprint 3**

| Tarea | Responsable | Estado |
| :---- | :---: | :---: |
| **Configurar entorno de Machine Learning (Scikit-learn, NumPy)** | **Backend Team** | **Planificado** |
| **Implementar algoritmo K-Means para clustering de PDV** | **Backend Team** | **Planificado** |
| **Definir zonas geográficas óptimas según número de promotores** | **Backend Team** | **Planificado** |
| **Implementar heurística del Problema del Agente Viajero (TSP)** | **Backend Team** | **Planificado** |
| **Calcular secuencia óptima de visitas por cluster/promotor** | **Backend Team** | **Planificado** |
| **Balancear carga laboral (4-6 visitas/día por promotor)** | **Scrum Team** | **Planificado** |
| **Integrar rutas optimizadas con el mapa interactivo (colores por cluster)** | **Frontend Team** | **Planificado** |

 **Burndown Chart – Sprint 3**

| Día | Trabajo Restante (SP) | Línea Ideal | Progreso |
| :---: | :---: | :---: | :---: |
| **Día 1** | **16 SP** | **16 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 2** | **16 SP** | **14 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 3** | **14 SP** | **11 SP** | **██░░░░░░░░░░░░░░░░░░** |
| **Día 4** | **12 SP** | **9 SP** | **█████░░░░░░░░░░░░░░░** |
| **Día 5** | **9 SP** | **7 SP** | **█████████░░░░░░░░░░░** |
| **Día 6** | **6 SP** | **5 SP** | **████████████░░░░░░░░** |
| **Día 7** | **2 SP** | **2 SP** | **█████████████████░░░** |
| **Día 8** | **0 SP** | **0 SP** | **████████████████████** |

 

### **Diagrama de Casos de Uso – Sprint 3**

###  **![][image10]**

###  

###  

###  

###  **Diagrama de Clases – Sprint 3**

### **![][image11]** 

###  

###  

###  

###  

###  

###  

###  

###  **Diagrama de Secuencia – Sprint 3**

### **![][image12]** 

###  **Diagrama de Actividades – Sprint 3**

### **![][image13]** 

###  

###  **C.4 Sprint 4 – Refinamiento del Sistema y Entrega del MVP**

| Objetivo: | Implementar validación de rutas, ajustes manuales, exportación de reportes y despliegue del producto mínimo viable (MVP). |
| :---- | :---- |
| **Duración:** | **2 semanas (10 días hábiles)** |
| **Story Points:** | **18 SP** |
| **Responsable:** | **Scrum Team completo (Backend \+ Frontend \+ QA)** |

 

### **Historias de Usuario – Sprint 4**

| ID | Historia de Usuario | Actor | Prioridad | SP |
| :---: | :---- | :---- | :---: | :---: |
| **HU06** | **Como Supervisor Operativo, quiero validar las rutas generadas antes de su aprobación para asegurar el cumplimiento de los SLA** | **Supervisor Operativo** | **Alta** | **5** |
| **HU07** | **Como Ejecutivo de Cuenta, quiero reasignar clientes entre promotores para responder rápidamente ante ausencias o cambios operativos** | **Ejecutivo de Cuenta** | **Media** | **5** |
| **HU08** | **Como Analista de Planificación, quiero visualizar las rutas optimizadas en el mapa para validar su lógica geográfica** | **Analista de Planificación** | **Alta** | **5** |
| **HU09** | **Como Analista de Planificación, quiero exportar las rutas aprobadas en PDF o Excel para compartirlas con el equipo de campo** | **Analista de Planificación** | **Alta** | **3** |

 

### **Sprint Backlog – Sprint 4**

| Tarea | Responsable | Estado |
| :---- | :---: | :---: |
| **Implementar módulo de validación y aprobación de rutas** | **Supervisor / Backend Team** | **Planificado** |
| **Programar reasignación manual de clientes entre promotores** | **Backend Team** | **Planificado** |
| **Crear interfaz de edición de rutas (drag & drop o formulario)** | **Frontend Team** | **Planificado** |
| **Mostrar rutas finales optimizadas con detalle en el mapa** | **Frontend Team** | **Planificado** |
| **Programar generación de reportes en formato PDF** | **Backend Team** | **Planificado** |
| **Programar exportación de rutas en formato Excel** | **Backend Team** | **Planificado** |
| **Ejecutar pruebas de calidad (QA) y corrección de bugs** | **Scrum Team** | **Planificado** |
| **Despliegue del MVP en servidor cloud (AWS/Heroku free tier)** | **Scrum Team** | **Planificado** |

   
 **Burndown Chart – Sprint 4**

| Día | Trabajo Restante (SP) | Línea Ideal | Progreso |
| :---: | :---: | :---: | :---: |
| **Día 1** | **18 SP** | **18 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 2** | **18 SP** | **15 SP** | **░░░░░░░░░░░░░░░░░░░░** |
| **Día 3** | **15 SP** | **13 SP** | **███░░░░░░░░░░░░░░░░░** |
| **Día 4** | **12 SP** | **10 SP** | **███████░░░░░░░░░░░░░** |
| **Día 5** | **9 SP** | **8 SP** | **██████████░░░░░░░░░░** |
| **Día 6** | **6 SP** | **5 SP** | **█████████████░░░░░░░** |
| **Día 7** | **2 SP** | **3 SP** | **██████████████████░░** |
| **Día 8** | **0 SP** | **0 SP** | **████████████████████** |

 

### **Diagrama de Casos de Uso – Sprint 4**

### **![][image14]** 

###  **Diagrama de Clases – Sprint 4**

### **![][image15]** 

### **Diagrama de Secuencia – Sprint 4**

Representa el proceso desde la validación de una ruta hasta su exportación final. 

###  **![][image16]**

### **Diagrama de Actividades – Sprint 4**

Representa el flujo final de validación, edición y exportación de rutas 

###  **![][image17]**

El análisis de los requerimientos del negocio permitió identificar, priorizar y estructurar las nueve funcionalidades esenciales del sistema mediante metodología Scrum, garantizando un desarrollo incremental alineado con las necesidades operativas de ROM Outsourcing SAC.

 La distribución en cuatro sprints asegura entregas progresivas y verificables: desde la infraestructura base hasta el MVP funcional con capacidad de optimización inteligente de rutas. Los 47 Story Points estimados reflejan un balance adecuado entre complejidad técnica y tiempo disponible.

###  

###  

###  

###  

###  

###  

###  

13. **Elaboración de la matriz de trazabilidad**

14. **Elaboración de los casos de usos**

A continuación se identifican los actores que interactúan con el sistema y su rol dentro del proceso operativo.

| ID Actor | Actor | Descripción |
| ----- | ----- | ----- |
| **AC-01** | **Administrador** | Gestiona usuarios, promotores, reglas de negocio y configuración general del sistema. |
| **AC-02** | **Analista** | Carga datos, genera rutas con ML, ajusta rutas manualmente y exporta informes. |
| **AC-03** | **Supervisor** | Registra ausencias de promotores y cierre temporal de PDVs; supervisa carga de trabajo. |
| **AC-04** | **Promotor** | Consulta su ruta diaria y registra visitas realizadas desde dispositivo móvil. |
| **AC-05** | **Ejecutivo de Cuenta** | Visualiza reportes de cobertura de PDV para gestión con clientes estratégicos. |
| **AC-06** | **Gerente** | Monitorea KPIs operativos, ahorro logístico e impacto ambiental en el dashboard. |

Requerimientos Funcionales

| Código | Nombre | Descripción |
| ----- | ----- | ----- |
| RF1 | Carga de Datos | El sistema permite la carga masiva del padrón de PDVs y nómina de promotores mediante archivos CSV o Excel. |
| RF2 | Segmentación Territorial (K-Means) | Aplica K-Means para sectorizar geográficamente los PDVs de forma automática y equitativa por zonas. |
| RF3 | Optimización de Rutas (TSP) | Optimiza la secuencia de visitas con heurísticas TSP y algoritmos genéticos para minimizar la distancia total recorrida. |
| RF4 | Visualización Cartográfica | Muestra rutas y clústeres en mapa web interactivo con colores por zona y líneas de recorrido (Leaflet/Google Maps). |
| RF5 | Exportación de Rutas | Exporta las rutas aprobadas en formatos PDF y Excel para su distribución al equipo de campo. |
| RF6 | Gestión de Usuarios y Roles | Permite registrar usuarios con roles (Analista, Supervisor, Ejecutivo, Promotor, Gerente) con acceso diferenciado. |
| RF7 | Inicio de Sesión y Recuperación | Autenticación con correo y contraseña; recuperación de contraseña por enlace temporal al correo registrado. |
| RF8 | Gestión de PDVs | Registro, edición y cierre temporal de puntos de venta con coordenadas GPS, cuenta cliente y horario. |
| RF9 | Gestión de Promotores | Registro de promotores con zona, cuenta y disponibilidad semanal; registro de ausencias con redistribución automática. |
| RF10 | Ajuste Manual de Rutas | Permite agregar, quitar o reordenar PDVs en rutas generadas, con recálculo de tiempos y registro de auditoría. |
| RF11 | Configuración de Reglas de Negocio | El Administrador configura parámetros como mínimo/máximo de visitas diarias, horas de jornada y días de no repetición. |
| RF12 | Consulta de Ruta Diaria (Promotor) | El promotor visualiza su ruta del día con PDVs en orden de visita, dirección y hora estimada desde dispositivo móvil. |
| RF13 | Registro de Visitas Realizadas | El promotor registra hora de llegada, salida y observaciones por cada PDV; el sistema marca el PDV como visitado. |
| RF14 | Reportes Operativos | Genera reportes de cobertura de PDV, carga de trabajo por promotor, tiempo de planificación y km recorridos vs. línea base. |
| **RF15** | **Dashboard Ejecutivo** | Dashboard con KPIs clave: cobertura, km, tiempo de planificación y ausencias, con comparativos semana a semana. |

Requerimientos No Funcionales

| Código | Atributo | Descripción |
| ----- | ----- | ----- |
| RNF1 | Usabilidad | La interfaz debe ser intuitiva para usuarios sin formación técnica, con flujos de navegación simplificados y diseño limpio. |
| RNF2 | Disponibilidad | El sistema garantiza un uptime del 99% durante el horario laboral, desplegado en infraestructura cloud (AWS). |
| RNF3 | Seguridad | Acceso restringido mediante autenticación con credenciales individuales y contraseñas cifradas; solo personal autorizado. |
| RNF4 | Compatibilidad | Plataforma totalmente funcional en Google Chrome, Mozilla Firefox y Microsoft Edge; responsive para móviles. |
| RNF5 | Rendimiento | La generación de rutas optimizadas debe completarse en tiempo razonable para conjuntos típicos de PDVs operativos. |
| RNF6 | Escalabilidad | Arquitectura basada en componentes open-source (Python/Flask, PostgreSQL) replicable a otras regiones y cuentas. |
| RNF7 | Mantenibilidad | El código se gestiona con Git/GitHub, documentado y estructurado para facilitar cambios y evolución futura. |

Especificación de Casos de Uso

A continuación se presenta la especificación detallada de cada caso de uso, relacionando actores, requerimientos funcionales y no funcionales involucrados.

## CU-01 – Gestión de Usuarios y Autenticación

| CU-01 – Gestión de Usuarios y Autenticación |  |
| ----- | :---- |
| Actores | AC-01 Administrador, Todos los usuarios registrados |
| Req. Funcionales | RF6, RF7 |
| Req. No Funcionales | RNF3 Seguridad, RNF1 Usabilidad |
| Descripción | Permite al Administrador registrar nuevos usuarios asignándoles un rol. Cualquier usuario registrado puede iniciar sesión con correo y contraseña y recuperar su contraseña mediante enlace temporal enviado al correo. |
| Precondiciones | El sistema está desplegado y operativo. El Administrador tiene credenciales válidas. |
| Flujo Principal | El Administrador accede al módulo de gestión de usuarios. |
|   | Ingresa nombre, correo, contraseña y rol del nuevo usuario. |
|   | El sistema valida que el correo no esté registrado previamente. |
|   | El sistema crea el usuario y envía confirmación al correo. |
|   | El usuario ingresa sus credenciales en la pantalla de Login. |
|   | El sistema valida las credenciales y redirige al dashboard correspondiente al rol. |
| Flujo Alternativo | Correo duplicado: el sistema muestra 'El correo ya está registrado' y no crea el usuario. |
|   | Credenciales incorrectas: el sistema muestra 'Usuario y contraseña incorrectos' sin revelar qué campo falló. |
|   | Recuperación de contraseña: el sistema envía enlace válido por 30 minutos; si el correo no existe, muestra 'Correo no encontrado'. |
| Postcondiciones | El usuario queda registrado en el sistema con su rol y puede autenticarse. El historial de accesos queda registrado. |

 

## CU-02 – Gestión de Puntos de Venta (PDV)

| CU-02 – Gestión de Puntos de Venta (PDV) |  |
| ----- | :---- |
| Actores | AC-01 Administrador, AC-02 Analista, AC-03 Supervisor |
| Req. Funcionales | RF8 |
| Req. No Funcionales | RNF1 Usabilidad, RNF6 Escalabilidad |
| Descripción | Permite registrar, editar y gestionar el ciclo de vida de los PDVs, incluyendo el cierre temporal con fechas de inicio y reapertura y la carga masiva desde archivos Excel. |
| Precondiciones | El usuario tiene sesión activa con rol Administrador, Analista o Supervisor. |
| Flujo Principal | El usuario accede al módulo de Puntos de Venta. |
|   | Selecciona 'Registrar nuevo PDV' e ingresa nombre, dirección, coordenadas GPS, cuenta cliente y horario. |
|   | El sistema valida que no exista un PDV duplicado con mismo nombre y coordenadas. |
|   | El sistema almacena el registro y lo muestra en el listado. |
|   | Opcionalmente, el Supervisor marca un PDV como cerrado indicando fecha de inicio y reapertura. |
|   | El sistema excluye ese PDV de las rutas durante el período definido y lo reactiva automáticamente al vencer el plazo. |
| Flujo Alternativo | PDV duplicado: el sistema muestra 'PDV ya registrado' y no guarda el registro. |
|   | Coordenadas inválidas: el sistema resalta el campo e impide guardar hasta corregirlo. |
|   | Carga masiva: si el archivo .xlsx no tiene las columnas requeridas, el sistema muestra 'Formato incorrecto' sin importar datos. |
| Postcondiciones | El PDV queda disponible (o excluido temporalmente) en la base de datos para la generación de rutas. |

 

## CU-03 – Gestión de Promotores y Ausencias

| CU-03 – Gestión de Promotores y Ausencias |  |
| ----- | :---- |
| Actores | AC-01 Administrador, AC-03 Supervisor |
| Req. Funcionales | RF9 |
| Req. No Funcionales | RNF1 Usabilidad, RNF3 Seguridad |
| Descripción | Permite registrar promotores con su información operativa y gestionar ausencias diarias, disparando una redistribución automática de PDVs entre los promotores disponibles. |
| Precondiciones | El Administrador o Supervisor tiene sesión activa. Existen promotores y PDVs registrados. |
| Flujo Principal | El Administrador accede al módulo de Promotores. |
|   | Ingresa nombre, zona asignada, cuenta que atiende y disponibilidad semanal. |
|   | El sistema crea el promotor vinculado a su usuario con rol Promotor. |
|   | El Supervisor registra una ausencia indicando fecha y motivo. |
|   | El sistema redistribuye automáticamente los PDVs del promotor ausente entre los disponibles, respetando el límite de 4 a 6 visitas diarias. |
| Flujo Alternativo | Datos incompletos: el sistema resalta campos faltantes e impide guardar. |
|   | Sin promotores disponibles para distribución: el sistema muestra 'No hay promotores disponibles para redistribuir las rutas'. |
| Postcondiciones | El promotor queda registrado o la ausencia queda registrada con los PDVs redistribuidos. El historial de ausencias queda en el sistema. |

 

## CU-04 – Carga Masiva de PDVs desde Excel

| CU-04 – Carga Masiva de PDVs desde Excel |  |
| ----- | :---- |
| Actores | AC-02 Analista |
| Req. Funcionales | RF1 |
| Req. No Funcionales | RNF1 Usabilidad, RNF5 Rendimiento |
| Descripción | Permite al Analista cargar un archivo Excel con el listado de PDVs de una cuenta cliente para integrarlos masivamente a la base de datos sin digitación manual. |
| Precondiciones | El Analista tiene sesión activa. Dispone de un archivo .xlsx con columnas: nombre, dirección, latitud, longitud, cuenta. |
| Flujo Principal | El Analista accede al módulo de Importación de Datos. |
|   | Selecciona el archivo .xlsx correspondiente a la cuenta cliente. |
|   | El sistema valida el formato y la presencia de las columnas requeridas. |
|   | El sistema procesa los registros e integra los PDVs válidos a la base de datos. |
|   | El sistema muestra un resumen con el número de registros importados y los errores encontrados. |
| Flujo Alternativo | Formato incorrecto: si el archivo no tiene las columnas requeridas, el sistema muestra 'Formato de archivo incorrecto' y no realiza ninguna importación. |
|   | Filas con datos inválidos: el sistema importa las filas válidas y lista las filas con error indicando la causa. |
| Postcondiciones | Los PDVs válidos quedan disponibles en la base de datos para ser usados en la generación de rutas. |

 

## CU-05 – Generación Automática de Rutas con ML

| CU-05 – Generación Automática de Rutas con ML |  |
| ----- | :---- |
| Actores | AC-02 Analista |
| Req. Funcionales | RF2, RF3 |
| Req. No Funcionales | RNF5 Rendimiento, RNF6 Escalabilidad |
| Descripción | El sistema aplica K-Means para agrupar PDVs en zonas geográficas y TSP con algoritmos genéticos para optimizar la secuencia de visitas, generando rutas diarias equilibradas por promotor. |
| Precondiciones | Existen PDVs y promotores registrados en el sistema. El Analista tiene sesión activa. |
| Flujo Principal | El Analista accede al módulo de Generación de Rutas. |
|   | Selecciona la cuenta cliente, la semana y los parámetros de optimización. |
|   | El sistema ejecuta K-Means para agrupar PDVs geográficamente por zonas. |
|   | El sistema aplica heurísticas TSP para definir el orden óptimo de visitas dentro de cada zona. |
|   | El sistema asigna entre 4 y 6 visitas diarias por promotor sin repetir PDVs en días consecutivos de la misma semana. |
|   | Las rutas generadas quedan disponibles para revisión en el mapa interactivo. |
| Flujo Alternativo | Sin datos suficientes: si no hay PDVs cargados para la cuenta seleccionada, el sistema muestra 'No hay datos suficientes para generar rutas'. |
|   | Parámetros fuera de rango: el sistema valida las reglas de negocio configuradas y alerta al usuario si no se pueden cumplir. |
| Postcondiciones | Las rutas quedan registradas en el sistema asociadas a promotores y PDVs para el período seleccionado. |

 

## CU-06 – Visualización de Rutas en Mapa Interactivo

| CU-06 – Visualización de Rutas en Mapa Interactivo |  |
| ----- | :---- |
| Actores | AC-02 Analista, AC-05 Ejecutivo de Cuenta |
| Req. Funcionales | RF4 |
| Req. No Funcionales | RNF1 Usabilidad, RNF4 Compatibilidad |
| Descripción | El usuario visualiza las rutas generadas sobre un mapa web interactivo con PDVs diferenciados por promotor y día, pudiendo filtrar por período y zona. |
| Precondiciones | Existen rutas generadas en el sistema para el período seleccionado. El usuario tiene sesión activa. |
| Flujo Principal | El usuario accede al módulo de Mapa Interactivo. |
|   | Selecciona la semana y la cuenta cliente. |
|   | El sistema renderiza el mapa mostrando PDVs con colores diferenciados por promotor y líneas de recorrido. |
|   | El usuario filtra por día para revisar la distribución diaria. |
|   | El usuario revisa la distribución geográfica antes de aprobar las rutas. |
| Flujo Alternativo | Sin rutas generadas: el sistema muestra 'No hay rutas generadas para el período seleccionado'. |
|   | Error de carga del mapa: el sistema muestra un mensaje de error de conexión e invita a reintentar. |
| Postcondiciones | El usuario tiene visibilidad completa de las rutas para tomar decisiones de aprobación o ajuste. |

 

## CU-07 – Ajuste Manual de Rutas Generadas

| CU-07 – Ajuste Manual de Rutas Generadas |  |
| ----- | :---- |
| Actores | AC-02 Analista |
| Req. Funcionales | RF10 |
| Req. No Funcionales | RNF1 Usabilidad, RNF5 Rendimiento |
| Descripción | Permite al Analista modificar manualmente rutas generadas por el sistema (agregar, quitar o reordenar PDVs) para adaptarlas a condiciones especiales no capturadas por el algoritmo. |
| Precondiciones | Existen rutas generadas. El Analista tiene sesión activa. |
| Flujo Principal | El Analista accede a la ruta que desea modificar. |
|   | Selecciona la acción: agregar PDV, quitar PDV o reordenar visitas. |
|   | Realiza el ajuste en la interfaz. |
|   | El sistema valida que no se supere el límite de visitas diarias. |
|   | El sistema recalcula el tiempo estimado de recorrido y registra el ajuste con el usuario y fecha. |
| Flujo Alternativo | Se supera el límite de 6 visitas: el sistema muestra 'Se superó el límite de visitas diarias permitidas' y no guarda el cambio. |
| Postcondiciones | La ruta ajustada queda registrada con trazabilidad del cambio (quién, cuándo y qué se modificó). |

 

## CU-08 – Configuración de Reglas de Negocio

| CU-08 – Configuración de Reglas de Negocio |  |
| ----- | :---- |
| Actores | AC-01 Administrador |
| Req. Funcionales | RF11 |
| Req. No Funcionales | RNF3 Seguridad, RNF1 Usabilidad |
| Descripción | El Administrador configura los parámetros que gobiernan el comportamiento del algoritmo: mínimo y máximo de visitas diarias, horas máximas de jornada y días de no repetición de PDV. |
| Precondiciones | El Administrador tiene sesión activa y permisos de configuración del sistema. |
| Flujo Principal | El Administrador accede al panel de Configuración de Reglas. |
|   | Modifica los parámetros operativos según las políticas de ROM Outsourcing SAC. |
|   | Presiona Guardar. |
|   | El sistema valida que los valores estén dentro del rango permitido. |
|   | Los nuevos parámetros se aplican desde la siguiente generación de rutas. |
| Flujo Alternativo | Valor fuera de rango (ej. máximo de visitas mayor a 10): el sistema muestra mensaje de validación indicando el rango aceptado y no guarda. |
| Postcondiciones | Las reglas de negocio quedan actualizadas y son aplicadas por el motor de ML en la siguiente ejecución. |

 

## CU-09 – Consulta y Registro de Visitas (Promotor)

| CU-09 – Consulta y Registro de Visitas (Promotor) |  |
| ----- | :---- |
| Actores | AC-04 Promotor |
| Req. Funcionales | RF12, RF13 |
| Req. No Funcionales | RNF1 Usabilidad, RNF4 Compatibilidad |
| Descripción | El Promotor consulta su ruta diaria desde el dispositivo móvil y registra cada visita completada con hora de llegada, salida y observaciones, o marca el PDV como no disponible con el motivo. |
| Precondiciones | El Promotor tiene sesión activa. Existen rutas asignadas para el día. |
| Flujo Principal | El Promotor inicia sesión desde su celular y accede a 'Mi ruta del día'. |
|   | El sistema muestra los PDVs en orden de visita con nombre, dirección y hora estimada. |
|   | Al llegar a cada PDV, el Promotor presiona 'Registrar visita'. |
|   | Ingresa hora de entrada, salida y observaciones. |
|   | El sistema guarda el registro y marca el PDV como visitado. |
| Flujo Alternativo | Sin ruta asignada: el sistema muestra 'No tienes PDV asignados para hoy'. |
|   | PDV cerrado: el Promotor selecciona 'No visitado' con el motivo; el sistema registra el PDV como pendiente. |
| Postcondiciones | Las visitas quedan registradas con trazabilidad completa (hora, promotor, observaciones) para reportes de cobertura. |

 

## CU-10 – Exportación de Rutas

| CU-10 – Exportación de Rutas |  |
| ----- | :---- |
| Actores | AC-02 Analista |
| Req. Funcionales | RF5 |
| Req. No Funcionales | RNF1 Usabilidad, RNF4 Compatibilidad |
| Descripción | El Analista exporta las rutas aprobadas en formato Excel o PDF para su distribución al equipo de campo y a los clientes estratégicos. |
| Precondiciones | Existen rutas generadas y aprobadas para el período seleccionado. |
| Flujo Principal | El Analista accede al módulo de Exportación. |
|   | Selecciona la semana, cuenta cliente y formato de exportación (Excel o PDF). |
|   | El sistema genera el archivo con promotor, PDV, dirección, día y hora estimada. |
|   | El archivo se descarga al dispositivo del Analista. |
| Flujo Alternativo | Sin rutas disponibles: el sistema muestra 'No hay rutas disponibles para exportar en el período indicado'. |
| Postcondiciones | El archivo queda descargado y listo para distribución al equipo de campo y clientes. |

 

## CU-11 – Reportes Operativos y Dashboard Ejecutivo

| CU-11 – Reportes Operativos y Dashboard Ejecutivo |  |
| ----- | :---- |
| Actores | AC-05 Ejecutivo de Cuenta, AC-03 Supervisor, AC-06 Gerente |
| Req. Funcionales | RF14, RF15 |
| Req. No Funcionales | RNF1 Usabilidad, RNF2 Disponibilidad, RNF4 Compatibilidad |
| Descripción | Permite a los distintos perfiles generar y visualizar reportes operativos: cobertura de PDVs, carga de trabajo por promotor, tiempo de planificación y proceso manual, km recorridos y estimación de CO2 ahorrado. El Gerente accede además al dashboard ejecutivo con KPIs globales. |
| Precondiciones | Existen datos de visitas registradas en el período seleccionado. El usuario tiene sesión activa con el rol correspondiente. |
| Flujo Principal | El usuario accede al módulo de Reportes o Dashboard. |
|   | Selecciona el rango de fechas y la cuenta cliente. |
|   | El sistema calcula y presenta los indicadores: cobertura, km, tiempo de planificación, carga por promotor, ausencias. |
|   | El Gerente visualiza el dashboard con flechas de tendencia y comparativos semana a semana. |
|   | El Supervisor identifica promotores con desequilibrio de carga (\>20% sobre/bajo el promedio) resaltados visualmente. |
| Flujo Alternativo | Sin datos en el período: el sistema muestra 'Sin datos disponibles para el período indicado' en cada indicador. |
|   | Historial insuficiente para comparativo: el sistema muestra 'Se requieren más registros para generar el comparativo'. |
| Postcondiciones | Los reportes quedan disponibles para la toma de decisiones operativas y la gestión con clientes estratégicos. |

 

15. **Aplicación de un plan de Versiones**

# **16\. Elaboración de la Arquitectura de Software según Requerimientos del Negocio**

## **16.1. Introducción y Enfoque Arquitectónico**

La arquitectura del **Sistema Web Inteligente para la Optimización de Rutas de Promotores** se diseña bajo un enfoque **modular y de capas**, priorizando la escalabilidad, el bajo costo operativo y la capacidad de integrar modelos de Machine Learning (ML) en tiempo casi real. Se adopta un **patrón arquitectónico de tres capas \+ motor de optimización**, con comunicación vía API RESTful, lo que permite desacoplar la presentación, la lógica de negocio y los algoritmos de ML, facilitando futuras expansiones (ej. app móvil, integración con APIs de tráfico).

Esta arquitectura responde directamente a los requerimientos de negocio de ROM Outsourcing SAC: manejo de \~1,540 PDV, reglas de 4-6 visitas diarias por promotor, límite de 8 horas por jornada, rotación semanal sin repeticiones, y adaptación a variables dinámicas (ausencias, tráfico, campañas).

## **16.2. Arquitectura Lógica (Componentes del Sistema)**

El sistema se estructura en cuatro componentes principales:

| Capa/Componente | Responsabilidad | Tecnologías |
| ----- | ----- | ----- |
| **Presentación (Frontend)** | Interfaz web para analistas y administradores. Visualización de mapas interactivos, carga de archivos Excel/CSV, exportación de rutas y dashboard de KPIs. | HTML5, CSS3, JavaScript, Flask/Jinja2, Leaflet/Folium, Chart.js |
| **Servicios de Negocio (Backend API)** | Validación de reglas de negocio, gestión de usuarios, control de accesos, orquestación de llamadas al motor ML, manejo de sesiones y auditoría. | Python, Flask/FastAPI, SQLAlchemy, Celery (tareas asíncronas) |
| **Motor de Optimización (ML Layer)** | Ejecución de algoritmos de clustering (K-Means), cálculo de distancias (Haversine), resolución del TSP con heurísticas (algoritmos genéticos/gradiente), aplicación de restricciones (4-6 visitas, 8h, sin repeticiones semanales). | Scikit-learn, NumPy, Pandas, OR-Tools (opcional), scripts Python |
| **Persistencia y Datos** | Almacenamiento estructurado de PDV, promotores, historial de visitas, métricas y rutas generadas. Soporte para consultas geográficas y backups. | PostgreSQL \+ PostGIS (recomendado) o MySQL, Redis (cache opcional) |

## **16.3. Arquitectura Física y Dispositivos**

| Entorno | Dispositivo/Infraestructura | Sistema Operativo | Justificación |
| ----- | ----- | ----- | ----- |
| **Servidor de Producción/Piloto** | Máquina virtual en cloud (Render, Railway, AWS Free Tier) o servidor local en ROM | Ubuntu Server 22.04 LTS o Debian 12 | Estabilidad, compatibilidad nativa con Python/PostgreSQL, bajo costo |
| **Estación de Analistas/Gerencia** | Laptops/PC corporativos (Windows 10/11, macOS, Linux) | Navegadores modernos (Chrome, Edge, Firefox) | Acceso vía navegador, sin instalación local |
| **Dispositivos de Campo (Fase 2\)** | Smartphones Android/iOS | PWA o App nativa (Flutter/React Native) | Consultas de rutas, registro de visitas, notificaciones |
| **Entorno de Desarrollo** | Laptop propia del equipo | Windows 11 / WSL2 o macOS | Git, VS Code, Docker Desktop (opcional), Python 3.10+ |

## **16.4. Arquitectura de Datos y Conexión a Base de Datos**

* **Motor de BD:** PostgreSQL con extensión PostGIS (para consultas geoespaciales eficientes) o MySQL si se prioriza simplicidad.  
* **Gestión de Conexiones:** SQLAlchemy con connection pooling (5-10 conexiones máximas), variables de entorno para credenciales (DATABASE\_URL), y migraciones versionadas con Flask-Migrate (Alembic).  
* **Flujo de Datos:**  
  1. Carga de archivo Excel/CSV → Validación de coordenadas y duplicados.  
  2. Inserción en tabla pdv y promotores.  
  3. Ejecución de pipeline ML → Generación de rutas optimizadas.  
  4. Almacenamiento en tabla rutas\_asignadas y historial\_visitas.  
  5. Visualización en frontend y exportación a PDF/Excel.  
* **Backups:** Dumps automáticos diarios (cron job o GitHub Actions), retención de 30 días, almacenados en bucket S3/compatible o disco externo cifrado.

## **16.5. Arquitectura de Seguridad**

Diseñada bajo principios de **Confidencialidad, Integridad y Disponibilidad**, alineada con controles del Anexo A de la ISO 27001:2022 y la Ley N.º 29733 de Protección de Datos Personales del Perú:

| Control | Implementación |
| :---: | :---: |
| **Autenticación y Autorización** | JWT/Session-based, roles: admin, analista, promotor. Validación de contraseñas con bcrypt (hash SHA-256/Argon2). |
| **Control de Acceso (A.5.15)** | RBAC (Role-Based Access Control). Analistas solo ven/editan sus rutas; promotores solo consultan las asignadas. |
| **Protección de Datos** | Encriptación TLS 1.2+ en tránsito, datos sensibles anonimizados en logs, cumpliendo normativa peruana. |
| **Prevención de Vulnerabilidades** | Sanitización de inputs, protección contra SQLi/XSS, rate limiting en APIs, validación de archivos Excel (pandas/openpyxl). |
| **Auditoría y Logs** | Registro de accesos, cambios en rutas y ejecución de modelos. Logs centralizados en archivo estructurado o servicio ligero. |
| **Disponibilidad** | Health checks automáticos, reinicio de servicio con systemd/PM2, monitoreo básico (UptimeRobot o GitHub Actions cron). |

## **16.6. Plan de Versiones y Despliegue (Release Strategy)**

Se adopta **Semantic Versioning** y control de versiones con Git/GitHub, siguiendo ramificación GitFlow simplificada:

| Versión | Alcance | Fecha Estimada |
| :---: | :---: | :---: |
| v0.1.0 | MVP: carga de PDV, K-Means \+ TSP básico, reglas estáticas (4-6 visitas, 8h), exportación Excel | Sprint 1-2 |
| v0.2.0 | Interfaz web completa, mapas interactivos, control de accesos, logs, backups automáticos | Sprint 3 |
| v1.0.0 | Producción piloto (ROM): manejo de ausencias, rotación semanal, validación de tráfico estático, dashboard KPIs | Sprint 4 |
| v1.1.0 | Integración OSRM/Google Maps API, cálculo de distancias viales reales, notificaciones por email | Sprint 5 |
| v2.0.0 | PWA móvil para promotores, aprendizaje supervisado (predicción de tiempos), escalado multi-sucursal | Fase 2 |

* **CI/CD:** GitHub Actions para pruebas unitarias (pytest), linting (flake8/black) y despliegue automático al servidor.  
* **Rollback:** Migraciones reversibles, feature flags para activar/desactivar funcionalidades, snapshots de BD antes de despliegues.

## **16.7. Alineación Directa con Requerimientos del Negocio**

| Requerimiento de Negocio | Respuesta Arquitectónica |
| :---: | :---: |
| Optimización de rutas con ML | Motor dedicado (scikit-learn \+ TSP heurístico) desacoplado del frontend |
| Reglas: 4-6 visitas/día, máx. 8h, sin repeticiones semanales | Validación en capa de negocio \+ constraints en modelo TSP |
| Manejo de ausencias y eventos estacionales | Endpoint de override manual \+ rebalanceo automático en pipeline |
| Bajo presupuesto / Open Source | Stack 100% gratuito (Flask, Postgres, Leaflet, GitHub Actions) |
| Cumplimiento normativo y seguridad | RBAC, cifrado, logs, anonimización, backups versionados |
| Escalabilidad a otras cuentas/región | Arquitectura modular, BD normalizada (3FN), API RESTful preparada para microservicios futuros |

16. # **Referencias** {#referencias}

Google OR-Tools. (2024). Traveling Salesperson Problem. Google Developers. https://developers.google.com/optimization/routing/tsp

Leaflet. (s.f.). An open-source JavaScript library for mobile-friendly interactive maps. https://leafletjs.com/ Pallets Projects. (2024). Flask: Web development, one drop at a time. https://flask.palletsprojects.com/

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M. y Duchesnay, E. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830. https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html

PostGIS Project. (s.f.). Spatial and Geographic objects for PostgreSQL. https://postgis.net/

Satpathy, T. (2017). A Guide to the Scrum Body of Knowledge (SBOK Guide) (3ra ed.). SCRUMstudy. https://www.scrumstudy.com/SBOK/SCRUMstudy-SBOK-Guide-3rd-edition.pdf

Schwaber, K. y Sutherland, J. (2020). La Guia de Scrum. La Guia Definitiva de Scrum: Las Reglas del Juego. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-Latin-South- American.pdf

Scikit-learn developers. (2024). 2.3. Clustering: K-Means. Scikit-learn 1.8.0 documentation. https://scikit- learn.org/stable/modules/clustering.html\#k-means
