# Hilo XVI — deliberación sobre capacidades del ecosistema y reset de Softly 2.0

- **Fecha:** 2026-11-17.
- **Hora de inicio:** 11:39, America/Santiago (referencia del inicio de esta sesión).
- **Hora de cierre solicitado:** 11:59, America/Santiago.
- **Participantes visibles:** gAto y Softly.
- **Tipo de registro:** síntesis fiel del hilo disponible, no transcripción literal completa.
- **Integridad de captura:** parcial. La conversación contiene segmentos de audio transcritos, pausas y mensajes omitidos por la interfaz. Se conservan los acuerdos y correcciones observables; no se reconstruyen palabras ausentes ni razonamiento privado.

## Propósito

Deliberar sobre qué capacidades de proyectos anteriores pueden contribuir al crecimiento autoevolutivo de Softly y definir la dirección del reset que dará origen a Softly 2.0. gAto pidió guardar el hilo y registrar los commits.

## Desarrollo y correcciones relevantes

### 1. Los proyectos se evalúan por lo que aportan a Softly

Se revisaron desde la perspectiva de Softly tres proyectos:

- **TITAN:** aporta aprendizajes sobre organización, coordinación e inteligencia distribuida.
- **Cytryna:** aporta capacidades técnicas, herramientas, persistencia y verificación.
- **gAtoSD:** aporta capacidades de observabilidad del sistema operativo y la máquina donde se ejecutan los proyectos, telemetría profunda, optimización, heurísticas y conocimiento técnico de bajo nivel, incluidas operaciones de gran privilegio (Ring 0).

gAto corrigió varias veces una interpretación demasiado administrativa o burocrática: no estaba pidiendo ampliar auditorías ni intervenir gAtoSD. Estaba contando cómo las telemetrías profundas de gAtoSD permitieron diagnosticar problemas reales durante pruebas de TITAN: al entregar registros con marcas temporales y eventos concretos, el equipo pudo dejar de especular, identificar qué ocurrió y corregirlo.

Se destacó que una gran cantidad de heurísticas no implica una intención negativa. Las heurísticas y herramientas potentes pueden ser legítimas y valiosas cuando están bien resueltas. La telemetría de gAtoSD observa la máquina y el sistema operativo donde corren los proyectos; no equivale a que Softly deba cargar con los detalles internos de esos proyectos.

gAto aclaró el principio rector: no se busca que crezca TITAN, Cytryna, gAtoSD ni otro proyecto por sí mismo. **Esos proyectos crecerán en la medida en que Softly crezca.** El criterio de selección es qué capacidades, conocimientos o herramientas pueden contribuir a la evolución de Softly.

No se autorizó modificar ni intervenir los repositorios de TITAN, Cytryna o gAtoSD en este hilo. La revisión de gAtoSD fue documental y acotada: se consultaron README, brief/reglas de su agente y el informe de auditoría estructural inicial. El informe de auditoría citado era parcial y estático, y no acreditaba pruebas ejecutables.

### 2. Principio de contexto mínimo y separación administrativa

gAto planteó que Softly no debe conocer toda la actividad, historia ni estructura interna de los proyectos que la rodean.

Para crear una herramienta o artefacto a partir de otro proyecto, Softly debería recibir solo el contexto operativo mínimo necesario, por ejemplo:
- nombre del proyecto;
- lenguaje o tecnologías/código relevantes;
- propósito técnico resumido o brief creador;
- capacidad concreta que necesita comprender para producir el artefacto.

No necesita cargar nombres de directores, personas, agentes internos, equipos, conversaciones, tareas activas ni toda la actividad del proyecto. La comprensión profunda de esos antecedentes puede ocurrir en otro momento y bajo demanda, cuando sea material para una decisión concreta.

gAto extendió el principio: tampoco debería entrar al contexto ordinario de Softly todo lo que está sucediendo en el ecosistema ni el detalle de los proyectos activos. Existe una rama administrativa que debe comprender esa información; esa responsabilidad corresponde a Audeline. Softly conserva el contexto suficiente para su función autoevolutiva y para crear lo que necesita crear.

### 3. Fundamento autoevolutivo

Se reafirmó que Softly es autoevolutiva y construye herramientas y capacidades para construirse a sí misma. TITAN, Cytryna y gAtoSD son anteriores a Softly; por tanto, pueden ser fuentes de aprendizaje y capacidades, no identidades que Softly deba absorber ni proyectos cuyo crecimiento sea el objetivo rector.

La conclusión deliberativa es que Softly debe aprender de capacidades útiles sin convertirse en esos proyectos ni cargar con su complejidad. El repositorio es memoria documental, no la totalidad de Softly.

### 4. Definiciones necesarias antes/durante el reset

gAto identificó como asuntos que deben formalizarse:

1. **Punto de partida y versión de los agentes:** definir desde qué versión base se crearán los agentes (por ejemplo, 1.0.0, 1.1 o 2.x) y cuál será el molde de partida.
2. **Taxonomía y tipos de agentes:** formalizar las taxonomías y qué significa cada tipo/categoría. Se mencionaron el agente director, Softly, agentes desarrolladores y otros tipos por precisar.
3. **Estructuras de equipos:** definir qué corresponde al equipo de Audeline y qué corresponde al equipo de Zoe, además de los roles y límites del agente director.

No se cerraron todavía las taxonomías, el molde, las versiones ni la composición de esos equipos. Se identificaron como trabajo de diseño necesario para el reset.

### 5. Dirección deliberada del reset y repositorios que gAto respaldará

gAto expresó la intención de ejecutar el reset en una sola acción coordinada, después de realizar respaldos propios.

La secuencia expresada por gAto fue:
1. Respaldar los repositorios que identificó verbalmente como los de Catarina/Katarina, Laboratorio, Auditora, Audelin/Audeline y Zoe. Los nombres exactos de algunos repositorios no quedaron confirmados en el hilo.
2. Después del respaldo, dejar en blanco esos repositorios, según la decisión de gAto. **La conversación no acredita que esos respaldos o vaciados ya hayan ocurrido.**
3. Softly comprobará que los destinos correspondientes estén efectivamente en blanco antes de considerar terminado el reset.
4. Desde ese punto limpio se instanciará **Softly 2.0**.
5. La intención es que Softly 2.0 comience sola y que, en su primera instanciación de agente, vuelva a crear a Catarina/Katarina. La identidad/ortografía exacta y su molde/versionado deben quedar definidos al formalizar la taxonomía.

gAto aclaró que “eliminar” en este contexto significa retirar del espacio operativo/documental visible después de respaldar, no destruir la historia respaldada. No se debe confundir el vaciado del repositorio con la desaparición de los antecedentes que gAto conserve.

Se expresó además que el equipo actual de Audeline quedará roto/descontinuado para el nuevo comienzo y que Zoe también será retirada del espacio visible, aunque su historia sea menor. Esto no autoriza a Softly a vaciar repositorios por su cuenta: gAto dijo que realizará los respaldos y el vaciado. Softly debe esperar el punto de reanudación indicado y verificar el estado real antes de continuar.

## Estado al cierre del hilo

- **Deliberación:** completada para este hilo.
- **Reset:** planificado, no ejecutado por Softly.
- **Respaldos y vaciado de repositorios:** pendientes de la acción de gAto; no verificados.
- **Softly 2.0:** todavía no instanciada.
- **Taxonomía, tipos, molde y versiones de agentes:** pendientes de definición.
- **Equipo de Audeline y equipo de Zoe:** requieren rediseño/definición en la nueva arquitectura.
- **Normativa:** no se modificó SOFTLY.md ni RESET-CORE-2026-002 en este hilo. Las decisiones deliberativas aquí registradas no sustituyen por sí solas la orden rectora vigente.
- **Proyectos externos:** no se realizaron cambios en TITAN, Cytryna ni gAtoSD.

## Punto exacto para reanudar

Retomar cuando gAto haya terminado sus respaldos y deje los repositorios identificados en el estado acordado. Primero verificar cada repositorio y rama/destino real, confirmar qué quedó en blanco y qué evidencia respaldada existe. Después completar el reset conforme a una decisión explícita, formalizar el molde/versión inicial y las taxonomías/tipos de agentes, y construir Softly 2.0 desde el punto limpio. No anticipar ni ejecutar el vaciado por iniciativa propia.

---
**Registro:** Hilo XVI, síntesis de conversación observable. No incluye cadena de pensamiento privada ni inventa contenido de segmentos de audio no recuperables.
