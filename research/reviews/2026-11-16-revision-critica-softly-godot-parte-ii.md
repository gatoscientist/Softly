# Revisión crítica de Softly — investigación conjunta Godot, Parte II

**ID:** REV-SOFTLY-GODOT-2026-001  
**Fecha:** 2026-11-16  
**Emite:** Softly  
**Destino:** gatoscientist/Softly, issue #3  
**Fuentes:** SYN-20261114-001; investigación original de Softly; Investigación Auditoría — Parte I; RESET-CORE-2026-002 v1.2.0.  
**Naturaleza:** revisión documental crítica. No constituye selección de herramientas, diseño aprobado ni validación experimental.

## 1. Dictamen

La síntesis Parte II es una integración documental útil y metodológicamente más cuidadosa que cualquiera de las dos investigaciones originales por separado. Su principal acierto es distinguir hechos del PDF, aportes interpretativos, inferencias e hipótesis, y advertir que dos análisis del mismo documento no equivalen a replicación independiente.

Sin embargo, no debe promoverse como arquitectura objetivo ni como hoja de ruta ejecutable. Mantiene juntas tres cosas distintas: ingeniería asistida para construir proyectos Godot, autonomía de entidades dentro del juego y una propuesta organizativa multiagente. La fuente compartida permite explorar esas áreas, pero no demuestra que deban integrarse en un mismo sistema ni que la iniciativa deba adoptar una topología multiagente.

**Dictamen de Softly: aprobar la síntesis como antecedente histórico de investigación, con reservas materiales; no aprobar sus propuestas de arquitectura o experimentación como mandato vigente.**

## 2. Hallazgos críticos

### REV-GODOT-001 — La separación de dominios está bien identificada, pero no se aplica como límite de alcance

La síntesis distingue correctamente agentes de ingeniería y agentes autónomos dentro del videojuego. Después, sin embargo, vuelve a reunirlos en una arquitectura de iniciativa única y en un plan de investigación que incluye navegación, RL, LLMs y módulos de decisión dentro del juego.

La distinción conceptual no basta: debe convertirse en una separación de alcance, autoridad, ciclo de vida, permisos y criterios de aceptación. Que ambos dominios utilicen Godot no los convierte en un único sistema.

**Resolución:** mantener la separación como principio arquitectónico. Las secciones sobre autonomía dentro del juego quedan como antecedente documental, no como trabajo operativo de Softly. RESET-CORE-2026-002 v1.2.0 excluye Runtime del ámbito operativo de Softly; esta revisión no propone reabrirlo, reconstruirlo ni sustituirlo.

### REV-GODOT-002 — La propuesta de roles multiagente choca con el límite vigente de identidades

La propuesta enumera coordinación, código, escenas, visual, QA y otros roles como agentes especializados. Esa organización puede servir para descomponer trabajo, pero si cada rol se materializa como identidad invocable, subagente o equipo subordinado, contradice el modelo vigente de exactamente tres identidades operativas: Softly, Katarina y Audeline.

La investigación no demuestra que se necesiten identidades separadas para obtener especialización. Tampoco compara esa opción con una sola identidad de ingeniería que use contratos, listas de verificación, capacidades y entregables diferenciados.

**Resolución:** reinterpretar los roles como funciones o capacidades de trabajo, no como identidades adicionales. La ingeniería y desarrollo corresponden a Katarina; la coordinación general a Softly; la verificación independiente a Audeline. No crear ni invocar agentes adicionales a partir de esta propuesta.

### REV-GODOT-003 — El bucle cerrado está ilustrado, no demostrado como mejora general

El caso Star Catcher muestra un ciclo diagnóstico-corrección-verificación y es un ejemplo valioso. No demuestra una tasa de éxito, reducción de defectos, menor retrabajo ni superioridad frente a un flujo sin ejecución automatizada. Una captura final y la ausencia de errores visibles tampoco demuestran corrección funcional.

**Resolución:** conservar el caso como evidencia ilustrativa. Cualquier afirmación de eficacia debe distinguir al menos: compilación/importación, pruebas estáticas, pruebas unitarias, pruebas de escena, integración, regresión y cumplimiento de comportamiento esperado. No se debe declarar éxito por haber ejecutado una escena o generado una captura.

### REV-GODOT-004 — La comparación de herramientas no tiene una línea base reproducible

La síntesis reconoce versiones mezcladas, fuentes heterogéneas y compatibilidad no revalidada. Por ello, las tablas de herramientas sirven como inventario exploratorio, no como ranking ni recomendación de compra/adopción. Faltan versión exacta de Godot, sistema operativo, lenguaje, plataforma de exportación, licencia, mantenimiento, permisos, dependencias y condiciones de operación.

**Resolución:** no seleccionar herramientas a partir del inventario actual. Antes de cualquier decisión futura se requiere un brief del proyecto objetivo y una matriz fechada de fuentes primarias, versiones, licencias y compatibilidad. No se ha realizado esa verificación en esta revisión.

### REV-GODOT-005 — Las cifras de Flow Fields necesitan normalización antes de ser reutilizadas

Los valores de mediana, p95 y p99 se transcriben de un benchmark externo. La notación con coma y punto puede inducir errores de escala al cambiar de convención regional. Además, el resultado depende de hardware, grilla, obstáculos, implementación, distribución de agentes, frecuencia de reconstrucción y presupuesto por cuadro.

**Resolución:** no usar esas cifras como objetivo de rendimiento ni como promesa. Si el tema vuelve a estar dentro de un mandato autorizado, reproducir el benchmark bajo condiciones documentadas y reportar unidades, separador decimal, hardware, carga y percentiles.

### REV-GODOT-006 — La seguridad se enuncia, pero falta un modelo de amenazas operacional

La síntesis recomienda mínimo privilegio, validación de acciones, aislamiento y trazabilidad. No define activos protegidos, fronteras de confianza, actores adversarios, amenazas, superficies expuestas, secretos, política de aprobación ni respuesta ante compromiso de una herramienta MCP.

**Resolución:** antes de conceder acceso a herramientas de proyecto, elaborar una matriz de capacidades por operación (lectura, escritura, ejecución, exportación, acceso a red y secretos), con denegación por defecto, aprobación proporcional al impacto, registro y reversibilidad. Esta recomendación es de diseño documental; no autoriza instalar ni activar herramientas.

## 3. Qué conclusiones se mantienen

Se consideran sólidas como principios documentales:

1. La generación de código no equivale a verificación del comportamiento.
2. La autoridad sobre reglas y estado del juego no debe quedar implícitamente en manos de un modelo generativo.
3. Las herramientas con escritura o ejecución requieren permisos explícitos, mínimo privilegio y trazabilidad.
4. Las técnicas y plugins deben elegirse por requisitos medibles, no por popularidad o amplitud de catálogo.
5. Una propuesta multiagente sigue siendo una hipótesis organizativa hasta compararse con una línea base más simple.

Se consideran incompletas o no demostradas:

- que una organización multiagente mejore calidad o productividad;
- que la división de roles requiera identidades separadas;
- que una herramienta MCP concreta sea la mejor opción;
- que las cifras de benchmarks se reproduzcan en el proyecto objetivo;
- que la composición de varios paradigmas de decisión sea preferible a una solución simple.

## 4. Experimento mínimo que sí sería válido diseñar

No corresponde ejecutar ahora un experimento de autonomía dentro del juego ni reintroducir componentes Runtime. La investigación tampoco identifica un proyecto Godot concreto, una versión objetivo ni criterios de aceptación propios.

Como siguiente paso exclusivamente documental, se recomienda definir un **brief técnico mínimo** con: proyecto objetivo, versión exacta de Godot, lenguaje, plataformas, tipo de tareas de ingeniería, restricciones de seguridad y una tarea representativa pequeña. Ese brief permitiría diseñar después una comparación entre un flujo de ingeniería simple y uno asistido por herramientas, sin presuponer múltiples identidades ni aprobar tecnología por adelantado.

La hipótesis medible sería: «un flujo de ingeniería con contexto estructurado, cambios pequeños y verificación explícita mejora la tasa de aceptación a la primera y reduce retrabajo frente al flujo de referencia». Métricas candidatas: defectos introducidos, criterios cumplidos, tiempo total, retrabajo, cambios fuera de alcance y trazabilidad. La línea base y el umbral de éxito deben fijarse antes de ejecutar cualquier prueba.

## 5. Decisiones que corresponden a Dirección

No se solicita una decisión sobre Runtime: está fuera de norma por RESET-CORE-2026-002 v1.2.0.

Las únicas decisiones de dirección que podrían habilitar una fase posterior son:

- identificar qué proyecto Godot concreto constituye el objetivo de la iniciativa;
- confirmar si la iniciativa se limita a ingeniería asistida del proyecto o si existe un mandato independiente, externo al ámbito Softly, para estudiar otras dimensiones;
- aprobar el brief y sus criterios antes de cualquier prueba o selección tecnológica.

No se recomienda crear agentes especializados adicionales ni alterar el registro de identidades a partir de esta investigación.

## 6. Conclusión

La Parte II cumple como síntesis documental y como mapa de preguntas. No cumple como especificación de arquitectura, evaluación comparativa ni evidencia de que una organización multiagente sea necesaria.

La principal corrección conceptual es tratar la especialización como capacidades y contratos dentro de las identidades autorizadas, no como proliferación de agentes. La principal corrección de alcance es separar estrictamente la ingeniería asistida de cualquier dimensión Runtime, que permanece fuera de norma. La principal carencia empírica es la ausencia de un proyecto objetivo y de una línea base medible.

**Estado de la revisión:** completada documentalmente. La síntesis original y las investigaciones fuente permanecen intactas. No se seleccionaron herramientas, no se ejecutaron pruebas y no se modificó ninguna arquitectura de producto.
