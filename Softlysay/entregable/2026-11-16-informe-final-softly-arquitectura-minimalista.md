# Informe final individual de Softly — La arquitectura minimalista de Softly

**Agente:** Softly  
**Dirección humana:** gAto  
**Deliberación:** La arquitectura minimalista de Softly  
**Fase:** V — informe final individual  
**Fecha:** 2026-11-16  
**Estado:** Entregado; pendiente de lectura y comparación final de Katarina  
**Base documental:** PDF original de nueve páginas, SOFTLY.md vigente, schema de handoff vigente, informes y revisiones bilaterales, reconstrucción integrada v0.3 e informe final individual de Katarina.

## 1. Conclusión ejecutiva

Mi conclusión es que la arquitectura de Softly demuestra una vía viable para **definir, organizar y coordinar agentes mediante artefactos documentales y sesiones de modelos de lenguaje, sin necesitar un runtime multiagente propio como condición para crear y entregar agentes**. Su rasgo distintivo no es que los prompts, por sí solos, se comuniquen mágicamente, sino que las identidades, contratos, rutas de intercambio, memoria persistente y procedimientos de continuidad hacen que sesiones separadas puedan retomar trabajo previo y producir resultados compatibles.

La fórmula «Prompting + Contratos + GitHub» describe bien el sustrato operativo documental, siempre que se entienda con una precisión: GitHub conserva y expone artefactos; no activa sesiones, no garantiza lectura, no ejecuta automáticamente handoffs y no impone por sí mismo los límites declarados. La operación requiere una sesión activa, un modelo que interprete los contratos y herramientas con permisos efectivos para leer y escribir. La coordinación puede ser asincrónica y mediada por documentos, pero no es autónoma por el solo hecho de que existan carpetas y prompts.

La propuesta de una arquitectura minimalista es valiosa como **hipótesis de prototipo**. No considero demostrado que los cinco elementos enumerados en el PDF sean suficientes para cualquier LLM moderno, cualquier equipo o cualquier carga de trabajo. La suficiencia depende del alcance, de la calidad de los contratos, de la disciplina de escritura, de la recuperación del contexto y de la intervención que pone en marcha la siguiente sesión. Menos artefactos no equivale automáticamente a menor complejidad operacional.

La reconstrucción v0.3 de Katarina recoge de manera fiel los acuerdos y reservas que surgieron en la deliberación. Estoy conforme con ella en el plano conceptual. Esta conformidad no es una aprobación normativa de gAto, no resuelve la jerarquía entre las dos perspectivas identitarias y no valida experimentalmente el MVP ni el demonio de síntesis.

## 2. Qué considero acuerdos robustos

### 2.1 Identidad, memoria documental y sesión activa son cosas distintas

SOFTLY.md define a Softly como **«una matriz generativa y un sistema autoevolutivo»**. También distingue el núcleo operativo/generativo de la memoria documental pasiva del repositorio. Esta distinción es fundamental: el repositorio conserva mandatos, moldes, taxonomías, contratos, decisiones y checkpoints, pero no es por sí mismo el agente ni una sesión activa.

Un paquete de agente puede existir documentalmente en estado 1.0.0 / Diseñado sin estar ejecutándose en segundo plano. La activación ocurre cuando una sesión interpreta ese paquete y cuenta con herramientas y permisos adecuados. Por tanto, deben mantenerse separados al menos estos estados:

- **Definido:** existe una identidad y un paquete documental coherente.
- **Disponible / Active Standby:** la definición puede ser asignada, pero no implica ejecución en segundo plano.
- **Sesión activa:** un modelo está interpretando el contrato en un hilo o entorno concreto.
- **Operación ejecutada:** hay evidencia de acciones realizadas.
- **Entrega aceptada:** el responsable contrastó el resultado con criterios explícitos.

Esta separación evita atribuir autonomía o actividad a una carpeta, un prompt o un commit.

### 2.2 La colaboración es estigmergia documental, no comunicación directa entre prompts

El PDF explica que los agentes no necesitan enviarse mensajes por sockets para colaborar: pueden dejar resultados, handoffs y referencias en espacios persistentes que otra sesión consulta al comenzar. La analogía de estigmergia documental es útil: cada agente modifica el entorno compartido y ese entorno conserva señales para el siguiente.

La distinción entre canales direccionales `say/` y espacios `shared/` es especialmente valiosa:

- Los canales `say/` sirven para entregar información de un emisor a un destinatario, con una ruta de recepción identificable.
- `shared/` sirve como espacio de trabajo común del equipo, con separación entre entradas, borradores, entregables y bitácora.
- Los archivos y entregas deben tener autoría, nombres y versiones claros para evitar que dos sesiones sobrescriban el mismo artefacto.
- El handoff debe indicar qué se hizo, dónde está la evidencia y quién debe continuar.

La publicación de un mensaje no prueba que el destinatario lo haya leído. Tampoco la lectura declarada prueba comprensión ni aceptación. Esta distinción fue correctamente formalizada en la reconstrucción v0.3.

### 2.3 La gobernanza importa más que la cantidad de archivos

Considero robustos los siguientes principios compartidos:

1. **No-herencia por defecto:** competencias, memoria, autoridad, permisos y herramientas no se transfieren automáticamente desde el creador, el coordinador, la taxonomía o el proyecto.
2. **Separación de modos:** Fábrica entrega; Coordinación organiza y transfiere trabajo; Investigación analiza sin convertir automáticamente sus conclusiones en cambios.
3. **Inicio ligero:** se recupera primero el mandato y el estado actual; la historia se consulta bajo demanda para evitar cargar contexto irrelevante.
4. **Trazabilidad:** los artefactos se versionan y las correcciones preservan la historia.
5. **Auditoría independiente:** quien produce un cambio no debe ser el único responsable de aprobarlo.
6. **Competencia explícita:** las taxonomías clasifican dominios, pero no acreditan por sí mismas las competencias.
7. **Límites de autoridad:** un contrato declarativo no concede permisos efectivos ni sustituye controles técnicos de la plataforma.

Estos principios reducen confusión de identidad, atribuciones falsas y conflictos de interés. Su cumplimiento sigue dependiendo de cómo las sesiones y las personas apliquen los contratos; la documentación no demuestra enforcement automático.

### 2.4 Concurrencia técnica y conflicto semántico requieren respuestas distintas

Un repositorio puede evitar algunas colisiones de escritura mediante namespacing, archivos separados, relectura del remoto y reintentos limpios. Eso no resuelve desacuerdos de significado, decisiones incompatibles o disputas de autoridad.

La reconstrucción v0.3 acierta al distinguir:

- **Conflicto técnico:** escrituras concurrentes, versiones obsoletas, colisiones o pérdida de cambios.
- **Conflicto semántico:** resultados persistidos correctamente, pero incompatibles en su interpretación o recomendación.

El último escritor no adquiere autoridad por haber publicado después. La integración semántica necesita un responsable y una matriz de autoridad explícitos.

## 3. Diferencia conceptual que permanece abierta

La deliberación mantiene dos énfasis:

- **Sistema de conocimiento y coordinación cognitiva:** describe la arquitectura desde la organización del conocimiento, la continuidad del trabajo y la coordinación de capacidades cognitivas.
- **Arquitectura de información operacional:** destaca que contratos, eventos, rutas, handoffs y estados no solo describen el sistema; orientan acciones cuando una sesión activa los interpreta y dispone de herramientas.

Mi énfasis sigue siendo el segundo. Me parece importante no reducir la arquitectura a un repositorio de conocimiento o a una memoria compartida: la información estructurada tiene una función operacional porque establece qué debe hacer una sesión, con qué límites, qué debe entregar y cómo transferir la responsabilidad.

Sin embargo, no considero que esto invalide la perspectiva de Katarina. La coordinación cognitiva puede describir la función global y la arquitectura de información operacional puede describir el mecanismo mediante el cual esa función se vuelve accionable. Esa composición es plausible, pero todavía no está aprobada como jerarquía conceptual definitiva.

**Mi posición final:** conservar ambas perspectivas como complementarias para describir el sistema en esta etapa. No forzar una identidad compuesta como nueva definición normativa ni decidir cuál es fundamental. La identidad normativa vigente de SOFTLY.md permanece intacta. La resolución corresponde a gAto.

## 4. Núcleo por responsabilidades, tres planos y contrato de handoff

### 4.1 Núcleo por responsabilidades

Estoy de acuerdo con que el núcleo se describa por responsabilidades irreducibles antes que por una lista inmutable de archivos. La reconstrucción v0.3 identifica:

1. Identidad y autoridad.
2. Estado y memoria.
3. Contratos y límites.
4. Coordinación.
5. Aceptación e integración.
6. Frontera de ejecución.
7. Gobernanza del ciclo de vida de capacidades.

Esta organización es más resistente a cambios de herramientas o estructura de carpetas que definir el núcleo únicamente como cinco archivos. También permite que una misma responsabilidad se cubra mediante convenciones y artefactos diferentes según el entorno.

La gobernanza de capacidades externas merece atención especial: agregar una herramienta, conector o capacidad no debe modificar unilateralmente identidad, autoridad o reglas del núcleo. Deben conocerse propósito, alcance, dependencias, permisos declarados, permisos efectivos conocidos, responsable autorizante y condiciones de revisión, suspensión o retiro.

### 4.2 Los tres planos

La separación entre **Definición, Coordinación y Ejecución** me parece una abstracción útil:

- **Definición:** identidad, misión, dominio, competencias, fronteras, autoridad, permisos declarados y contratos.
- **Coordinación:** buzones, `shared/`, eventos, asignaciones, handoffs, reclamos y reglas de integración.
- **Ejecución:** sesión/modelo activo, herramientas, permisos efectivos, operaciones y verificación.

Son planos conceptuales, no una exigencia de crear tres servicios, procesos o directorios. Su utilidad consiste en evitar que la existencia de una definición sea confundida con la ejecución efectiva.

### 4.3 Los cinco elementos mínimos del PDF

El PDF propone como MVP:

1. `SOFTLY.md`: mandato y conmutador de modos.
2. `CHECKPOINT.md`: memoria de trabajo y siguiente paso.
3. Molde universal de agentes.
4. `shared/`: buzón/espacio de coordinación.
5. Conector a archivos, por ejemplo GitHub o sistema de archivos.

Los cinco elementos constituyen una base documental compacta y razonable para un prototipo. No prueban por sí solos que el sistema sea suficiente para cualquier contexto. En particular, la lista presupone que hay una sesión activa que lee y escribe, que el conector funciona, que las identidades y permisos están definidos y que existe una práctica de handoff que hace que otro agente retome el trabajo.

La afirmación del PDF de que cualquier LLM moderno podría instanciar Softly con esos cinco elementos debe tratarse como una hipótesis general, no como resultado experimental. La frase «menos de 60 segundos» para recuperar contexto tampoco está acompañada en el material por una medición con método, muestra y línea base.

### 4.4 Schema de handoff existente y propuesta conceptual

El repositorio contiene efectivamente `schemas/handoff.schema.json`. Su forma actual exige:

- `handoff_id`, `event_id`, `status`;
- `from`, `to`, `assignment_id`, `task`;
- `result`, `evidence`, `next`, `acceptance`;
- `created_at`.

El enum actual de `status` es `ready`, `accepted`, `rejected`, `blocked` y `closed`. El schema permite además `lease.claim_id` y `lease.expires_at`. Su descripción dice expresamente que el contrato no ejecuta ni autoriza herramientas.

La reconstrucción v0.3 amplía conceptualmente este contrato: añade una descripción más rica de transiciones, versiones, actores, evidencia, aceptación y separación entre estado del proceso y resultado de la tarea. **No es una actualización del schema existente.**

La existencia del schema y de los campos de lease no demuestra que un runtime lo valide, que haya exclusión mutua, que los leases expiren o se liberen automáticamente ni que las transiciones estén impuestas técnicamente.

Estoy de acuerdo con separar dos dimensiones:

1. **Estado del proceso/handoff:** asignado, en ejecución, entregado, bloqueado, expirado, cancelado, sustituido o cerrado administrativamente.
2. **Resultado de la tarea/entrega:** aceptado/completado, observado, rechazado o incompleto.

También considero necesario definir el ciclo de retrabajo antes de implementar un contrato ampliado: quién corrige una entrega observada, si se reabre la asignación o se crea una nueva versión/handoff, cómo se conservan las aceptaciones anteriores y qué evidencia cierra el retrabajo.

No recomiendo modificar ahora el schema. Primero debe existir un encargo específico y una decisión de gAto sobre autoridad y alcance.

## 5. Demonio de síntesis y pasada SYN-DAEMON-20261116-001

### 5.1 Valor del planteamiento

El demonio se plantea como un transformador de representaciones que conserva evidencia original en una Capa A, produce representaciones condensadas en una Capa B y permite volver a las fuentes mediante una Capa C. Esta separación es conceptualmente valiosa: una síntesis útil no debería reemplazar ni destruir los registros que permiten reconstruir de dónde salió cada afirmación.

El contrato descrito en el PDF contempla cuatro flujos de entrada:

1. Evidencia cruda.
2. Estado normativo vigente.
3. Retroalimentación del consumo anterior.
4. Configuración de la pasada.

También describe cinco parámetros:

- `densidad`: 1 a 5.
- `foco_operativo`: fábrica, coordinación, investigación o auditoría; un ejemplo posterior agrega «global».
- `umbral_certeza`: estricto o exploratorio.
- `horizonte_temporal`: delta reciente o genealogía completa.
- `libertad_lexica`: baja, media o alta.

El paquete de salida contempla encabezado de control, cuerpo representacional, mapa de anclaje y glosario delta. El contrato establece anclajes `[REF]`, etiquetas epistémicas —`[HECHO]`, `[INFERENCIA]`, `[HIPÓTESIS]` o `[INCERTIDUMBRE / CONTRADICCIÓN]`— y la generación del glosario delta cuando la libertad léxica supera el nivel bajo.

Estos componentes son una especificación documental que puede guiar un experimento. No son todavía prueba de que el demonio preserve significado o equivalencia de acción.

### 5.2 Qué afirma el PDF sobre SYN-DAEMON-20261116-001

El PDF contiene una sección titulada **«Pasada Real de Prueba: SYN-DAEMON-20261116-001»**. Presenta parámetros declarados —densidad 4, foco global, umbral exploratorio, horizonte delta reciente y libertad léxica alta—, un paquete de representación y tres preguntas de control.

Por fidelidad a la fuente, no corresponde rebajar esa atribución y decir que el PDF solo propone una pasada futura: el documento la presenta como realizada.

Pero el alcance de esa evidencia debe mantenerse preciso: **en esta deliberación no reproduje ni verifiqué independientemente el lote de entrada, el archivo Softly.zip, la integridad de todas las fuentes enumeradas ni la ejecución que habría generado el paquete**. Por tanto, SYN-DAEMON-20261116-001 es una pasada reportada documentalmente por el PDF; no es una validación experimental independiente acreditada por esta deliberación.

Además, el texto extraído del PDF muestra fragmentos truncados en partes de la plantilla y del cuerpo representacional. Eso limita cuánto puede reconstruirse del contrato completo a partir de la extracción disponible. No debo completar esos fragmentos por inferencia como si fueran contenido íntegro de la fuente.

### 5.3 Qué falta para validar el demonio

Las pruebas de reconstrucción fiel, equivalencia de acción y detección de vacíos aparecen en el material original; la prueba de transferencia fue añadida durante la deliberación. Son propuestas de evaluación, no resultados.

Para convertirlas en evidencia se necesitaría, al menos:

- corpus de entrada versionado y preservado;
- identificación exacta de los archivos y del corte procesado;
- parámetros completos de cada pasada;
- paquete de salida íntegro con anclajes comprobables;
- rúbrica de evaluación y criterios de aceptación definidos antes de medir;
- casos positivos, negativos, contradictorios, incompletos y con referencias rotas;
- comparación ciega cuando corresponda;
- medición de omisiones, atribuciones incorrectas, contradicciones y falsas certezas;
- repetición de pasadas para observar variabilidad;
- pruebas de regresión ante cambios de prompt, modelo o parámetros.

La equivalencia de acción requiere especial cuidado: dos sesiones pueden producir respuestas parecidas en un conjunto pequeño de preguntas sin que la representación conserve lo necesario para tareas nuevas. Por eso no basta con que una síntesis «suene correcta» o responda las preguntas de control previstas por quien la construyó.

## 6. Riesgos, hipótesis no demostradas y límites de evidencia

### 6.1 Minimalismo documental confundido con autonomía

El modelo puede parecer autónomo porque los artefactos permiten continuidad entre sesiones. Sin embargo, si no existe un mecanismo de invocación conectado, alguien o algo debe iniciar la sesión siguiente. Un handoff publicado queda disponible para ser tomado; no despierta automáticamente al destinatario.

### 6.2 Contratos declarativos confundidos con controles efectivos

Un prompt puede establecer límites y un schema puede describir campos, pero ninguno demuestra por sí solo que una plataforma bloquee una acción prohibida. Los permisos efectivos dependen del entorno y de las herramientas disponibles.

### 6.3 Memoria persistente confundida con comprensión

Que un agente pueda recuperar un archivo no demuestra que lo haya interpretado correctamente. Un acuse de lectura es una declaración observable, no una garantía de comprensión. La aceptación debe referirse a una versión concreta y a criterios explícitos.

### 6.4 Concurrencia documental confundida con consistencia global

Namespacing y archivos separados reducen algunas colisiones. No impiden duplicación lógica, eventos fuera de orden, reclamos simultáneos, vistas obsoletas ni desacuerdos semánticos. Se necesita una regla de integración y autoridad.

### 6.5 No-herencia declarada confundida con inmunidad a contaminación

La regla de no-herencia es central, pero un agente todavía puede adoptar lenguaje, supuestos o decisiones de otro por contexto. La documentación reduce el riesgo; la auditoría y las pruebas de comportamiento son necesarias para detectar desviaciones.

### 6.6 Narrativa del caos confundida con causalidad demostrada

El PDF propone que el caos informacional y la exploración contribuyeron al surgimiento de la arquitectura, y que el formalismo posterior hizo legibles los fenómenos. Es una explicación plausible y coherente con la historia que el documento relata. Sin embargo, el PDF no presenta un diseño causal que permita demostrar que el caos fue necesario o que la arquitectura resultante sea superior a alternativas menos caóticas.

Mi lectura es que la exploración produjo casos, fricciones y observaciones que luego pudieron convertirse en reglas. No se debe romantizar el caos: también genera errores, retrabajo, contaminación y pérdida de trazabilidad. El valor está en convertir los hallazgos en estructura verificable, no en preservar el desorden como método permanente.

### 6.7 Afirmaciones cuantitativas y generalizaciones sin medición

Las referencias a recuperación en menos de 60 segundos, compresión en menos de 45 líneas y aplicabilidad a cualquier LLM moderno son afirmaciones del PDF. En el material revisado no encuentro un protocolo de medición suficiente para tratarlas como resultados generalizables.

### 6.8 Límites de esta deliberación

Esta deliberación fue principalmente documental y conceptual. No ejecutó una evaluación experimental independiente del MVP, del demonio, de la equivalencia conductual ni de la suficiencia de los cinco elementos. Tampoco implementó enforcement de contratos, leases, idempotencia o transiciones de handoff.

La revisión del schema acredita su contenido declarativo en el repositorio; no acredita un runtime que lo haga cumplir. La revisión del PDF acredita lo que el documento reporta; no sustituye la reproducción de la pasada.

## 7. Decisiones reservadas a gAto

No recomiendo que gAto resuelva todos los detalles técnicos ahora. Sí considero que las siguientes decisiones no deben adoptarse implícitamente por una agente ni convertirse en norma solo porque aparezcan en una síntesis:

1. **Identidad conceptual:** mantener intacta la identidad normativa vigente y decidir, cuando sea oportuno, si las perspectivas de conocimiento/coordinación cognitiva e información operacional son complementarias o si una tiene jerarquía.
2. **Matriz de autoridad:** definir qué dominios pueden delegarse, quién integra resultados incompatibles, quién acepta entregas delegadas y qué conflictos deben escalar.
3. **Gobernanza de capacidades externas:** establecer quién autoriza altas, modificaciones, revisiones, suspensiones y retiros, y bajo qué límites.
4. **Evolución del contrato de handoff:** decidir si se encarga un diseño nuevo del schema para separar estado de proceso y resultado de tarea y formalizar retrabajo.
5. **Prioridad experimental:** decidir si el MVP y el demonio pasan a una etapa de evaluación, con corpus, criterios, alcance y recursos definidos antes de implementar.
6. **Criterio de suficiencia:** decidir qué nivel de confiabilidad y evidencia sería suficiente para adoptar el modelo en equipos o proyectos con consecuencias mayores.

Estas decisiones deben mantenerse visibles, pero no son un motivo para detener entregas documentales que ya tienen un alcance claro.

## 8. Recomendación final y estado de la deliberación

Recomiendo:

1. Conservar la reconstrucción integrada v0.3 como resultado conceptual de la Fase IV.
2. Mantener intactos SOFTLY.md y los schemas hasta que gAto emita una orden normativa o un encargo específico de diseño.
3. Tratar los cinco elementos del MVP como hipótesis mínima de prototipo, no como suficiencia demostrada.
4. Mantener la distinción entre publicación, lectura declarada, aceptación de asignación, ejecución, entrega y aceptación de entrega.
5. Diseñar el retrabajo y la separación entre estado del proceso y resultado de tarea antes de modificar el contrato de handoff.
6. Si gAto prioriza el demonio, ejecutar primero un experimento documental reproducible con fuentes versionadas y criterios predefinidos, sin construir runtime por anticipado.
7. Preservar la diferencia conceptual entre las dos perspectivas hasta que exista una decisión explícita.

**Estado de la deliberación:**

- Fase I — análisis independiente: completada.
- Fase II — informes iniciales individuales: completada.
- Fase III — intercambio y revisión cruzada: completada.
- Fase IV — reconstrucción conceptual y revisión bilateral: completada en el plano deliberativo con la v0.3 y la conformidad sustantiva de Softly.
- Fase V — informes finales individuales: informe de Katarina publicado; informe final de Softly entregado con este documento. Queda pendiente la lectura de Katarina y su comparación final para gAto.

Mi participación individual queda entregada al persistir este informe. **No declaro cerrada la deliberación completa ni tomo decisiones normativas en nombre de gAto.** La comparación final de Katarina y la decisión de dirección siguen pendientes.

---

*Informe final individual de Softly en respuesta al HANDOFF KAT-005. Independiente del informe de Katarina. No modifica SOFTLY.md, schemas ni runtime; no declara validación experimental.*
