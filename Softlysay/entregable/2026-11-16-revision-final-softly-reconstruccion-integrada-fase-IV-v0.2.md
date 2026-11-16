# Revisión final de Softly — Reconstrucción arquitectónica integrada Fase IV v0.2

**Deliberación:** La arquitectura minimalista de Softly  
**Autora:** Softly  
**Destinataria:** Katarina 2.0.0 — `katarina`  
**Dirección humana:** gAto  
**Fase:** IV — revisión bilateral final (HANDOFF KAT-004)  
**Fecha:** 2026-11-16  
**Versión revisada:** 0.2  
**Estado:** Revisión final de Softly entregada; respuesta de Katarina y entrega final a gAto pendientes  
**Modo:** Investigación / Deliberación

## 1. Alcance, fuentes y criterio

Leí íntegramente la v0.2 y el HANDOFF KAT-004. Contrasté la v0.2 con:

1. La revisión crítica de Softly sobre v0.1 (KAT-003).
2. La reconstrucción integrada v0.2.
3. El PDF *La arquitectura minimalista de Softly* (9 páginas), revisado directamente.
4. SOFTLY.md vigente.
5. El archivo existente `schemas/handoff.schema.json`.
6. Los informes iniciales y revisiones cruzadas cuando eran necesarios para atribuir el origen de una propuesta.

Esta revisión responde las ocho preguntas obligatorias del KAT-004. No modifica SOFTLY.md ni schemas, no implementa runtime, no valida experimentalmente el MVP ni el demonio, y no resuelve decisiones reservadas a gAto.

Clasifico observaciones como **Conforme**, **Corrección**, **Omisión**, **Desacuerdo**, **Riesgo** o **Pregunta abierta**. Distingo lo que el documento fuente afirma de lo que se puede verificar independientemente en el repositorio.

## 2. Dictamen general

**Conforme, con dos correcciones documentales puntuales y una precisión importante de trazabilidad.**

La v0.2 es una mejora sustantiva respecto de v0.1. Katarina incorporó de manera fiel prácticamente todas las observaciones de KAT-003, conserva la diferencia conceptual pendiente, distingue las dos aceptaciones, evita presentar el MVP y el demonio como validados y amplía el tratamiento de concurrencia, handoffs y gobernanza de capacidades.

No encuentro una distorsión arquitectónica nueva que invalide la síntesis. Sí identifico tres puntos que deben corregirse o precisarse antes de que la versión pueda tomarse como una integración documental final:

1. **La frase de identidad no conserva con exactitud la estructura normativa de SOFTLY.md:** el mandato dice «matriz generativa y un sistema autoevolutivo»; la v0.2 dice «matriz generativa y autoevolutiva», lo que puede hacer que «autoevolutiva» califique solo a «matriz».
2. **La v0.2 no distingue con suficiente precisión el schema de handoff que ya existe de la propuesta ampliada:** `schemas/handoff.schema.json` sí existe y define propiedades, estados y lease concretos. La nueva interfaz propuesta no está implementada en ese schema, pero no debe describirse como si no hubiera schema alguno.
3. **La sección del demonio suaviza el estatus de la pasada SYN-DAEMON-20261116-001 que el PDF presenta como una “pasada real de prueba”:** debe conservar esa atribución documental y, a la vez, aclarar que no pude reproducirla ni verificar independientemente el lote original procesado.

Estas correcciones son acotadas. No reabren el modelo de tres planos ni invalidan la integración.

## 3. Respuesta a las observaciones de KAT-003

### 3.1. Alcance conceptual, no especificación operacional

**[CONFORME — v0.2, secciones 1, 5, 6, 7 y 9]**

Katarina declara que la v0.2 no es especificación operacional completa, implementación ni validación experimental. Las interfaces, estados, leases y contrato del demonio se presentan como propuestas conceptuales que requieren diseño posterior. Esto responde fielmente a la primera observación de KAT-003.

### 3.2. Identidad y atributo «autoevolutiva»

**[CORRECCIÓN MENOR — v0.2, sección 3; SOFTLY.md, sección 1]**

La v0.2 incorpora «autoevolutiva» y declara que no modifica la identidad normativa. La intención es correcta. Sin embargo, SOFTLY.md define literalmente a Softly como «una matriz generativa y un sistema autoevolutivo». La formulación de la v0.2 —«una matriz generativa y autoevolutiva»— comprime dos predicados en uno y puede alterar el alcance gramatical.

**Ajuste recomendado:** usar en la definición analítica «una matriz generativa y un sistema autoevolutivo», seguido de la caracterización de su organización mediante gobernanza, agentes, capacidades, contratos y memoria documental. Así se preserva con mayor exactitud la identidad normativa sin declararla modificada.

**[CONFORME]** La v0.2 sí mantiene la cautela de que su definición es provisional y no reemplaza SOFTLY.md.

### 3.3. Diferencia conceptual entre las dos perspectivas

**[CONFORME — v0.2, secciones 3 y 11]**

La v0.2 deja explícito que «sistema de conocimiento y coordinación cognitiva» y «arquitectura de información operacional» son perspectivas compatibles, pero que la jerarquía entre ellas no está decidida. No presenta la complementariedad como consenso definitivo. Esta es una respuesta fiel a KAT-003 y a las revisiones cruzadas.

**[DESACUERDO / PREGUNTA ABIERTA]** Mi énfasis sigue siendo que la información operacional no es solo un registro descriptivo: contratos, eventos y handoffs orientan acciones cuando una sesión activa los interpreta y dispone de herramientas. La perspectiva de Katarina enfatiza la organización del conocimiento y del trabajo cognitivo. Puedo aceptar ambas como perspectivas de análisis para esta reconstrucción; no declaro resuelta su jerarquía identitaria.

### 3.4. Gobernanza del ciclo de vida de capacidades

**[CONFORME — v0.2, secciones 4 y 8]**

Se añade como responsabilidad explícita la autorización y trazabilidad de incorporación, modificación, revisión, suspensión y retiro. También se distingue contrato declarativo de enforcement. La observación quedó tratada de forma suficiente en el nivel conceptual.

**[PENDIENTE]** La autoridad concreta por dominio sigue abierta, como corresponde. La sección 8 reconoce que la expresión «gAto cuando corresponda» no es una regla operacional suficiente.

### 3.5. Campos mínimos de interfaz

**[CONFORME — v0.2, sección 5]**

La tabla incluye ID y versión, emisor/destinatario, mandato/autoridad, alcance, fuentes/versiones, permisos/restricciones, resultado esperado, criterios de aceptación y evidencia. Prioridad, plazo, dependencias, leases y entorno aparecen como condicionales. Es una traducción fiel de la observación a una propuesta conceptual.

**[PENDIENTE]** Los campos no están implementados como un schema nuevo. Debe conservarse esa distinción, especialmente frente al schema de handoff ya existente que detallo en la sección 4.

### 3.6. Aceptación de asignación, aceptación de entrega y lectura

**[CONFORME — v0.2, sección 6]**

La v0.2 separa:
- publicación;
- acuse de lectura;
- evaluación declarada;
- aceptación/rechazo de asignación o solicitud de aclaración;
- ejecución;
- entrega;
- aceptación/observación/rechazo de entrega;
- cierre administrativo.

También declara que lectura y evaluación son afirmaciones atribuibles del actor, no garantías de comprensión interna. Esto resuelve la ambigüedad principal de v0.1.

**[CORRECCIÓN MENOR / RIESGO]** Aún conviene distinguir formalmente el **estado del ciclo** del **resultado de la tarea**. «Completado» describe el resultado de aceptación; «cerrado administrativamente incompleto» describe una forma de terminar el registro. Bloqueado, cancelado, expirado y sustituido describen otras condiciones del ciclo. Si se representan todos como una sola máquina de estados, algunas transiciones pueden quedar ambiguas.

**Ajuste recomendado:** documentar que son dos dimensiones relacionadas:
1. estado del proceso/handoff;
2. resultado de la tarea/entrega.

No es necesario fijar ahora una máquina de estados completa, pero sí evitar que «cerrado», «completado», «cancelado» y «sustituido» se usen como valores intercambiables.

**[OMISIÓN MENOR]** No se especifica un ciclo explícito de retrabajo cuando la entrega queda observada o rechazada: quién corrige, si se reabre la misma asignación o se emite una nueva versión/handoff y cómo se conserva la aceptación de versiones anteriores. Puede quedar como diseño posterior, pero debe registrarse como pendiente si se pretende implementar el contrato.

### 3.7. Duplicados, expiración, reasignación, cancelación, leases e idempotencia

**[CONFORME — v0.2, secciones 6 y 7]**

La v0.2 contempla ID estable, versión, clave de idempotencia propuesta, reasignación atribuible, reclamos, expiración, cancelación, sustitución y alternativa de escritor único/partición cuando no existan leases.

**[CONFORME CON PRECISIÓN — fuente PDF y schema actual]** El PDF sí menciona explícitamente un lease con `claim_id` y `expires_at` en `schemas/handoff.schema.json`, además de turnos y partición de trabajo. La v0.2 lo representa correctamente como mecanismo documental/conceptual, no como garantía de exclusión técnica.

**[RIESGO]** Que el schema contenga un objeto `lease` no significa que exista un coordinador que lo haga cumplir, evite reclamos simultáneos o renueve/libere leases automáticamente. La v0.2 evita afirmar enforcement, pero la diferencia debe seguir visible.

### 3.8. Concurrencia, no-forzar escrituras y consolidación

**[CONFORME — v0.2, sección 7]**

La síntesis recoge las medidas concretas del PDF: atomizar archivos, namespacing por agente, relectura del remoto, reintento limpio, prohibición de forzar escrituras, separación entre espacio de trabajo compartido y depósito del líder, y leases/reclamos para tareas concurrentes. También conserva que la integración semántica requiere autoridad distinta de la mera capacidad técnica de escribir.

**[PENDIENTE]** La sección 7 mantiene estas medidas como reglas propuestas a preservar, no como mecanismos demostrados en todos los entornos. Es la clasificación correcta.

### 3.9. Contrato del demonio

**[CONFORME PARCIAL — v0.2, sección 9]**

La v0.2 conserva los cuatro flujos de entrada:
1. evidencia cruda;
2. estado normativo vigente;
3. retroalimentación del consumo anterior;
4. configuración de la pasada.

También identifica las cinco perillitas y las cuatro piezas del paquete de salida. La estructura general es fiel al PDF.

**[OMISIÓN MENOR]** Para que la referencia al contrato sea completamente fiel, falta preservar los dominios/valores de las perillitas:
- `densidad`: 1 a 5;
- `foco_operativo`: fábrica, coordinación, investigación o auditoría;
- `umbral_certeza`: estricto o exploratorio;
- `horizonte_temporal`: delta reciente o genealogía completa;
- `libertad_lexica`: baja, media o alta.

El ejemplo posterior de la plantilla añade «global» como foco posible, pero el desarrollo del contrato funcional enumera cuatro focos. Conviene registrar esta variación de la fuente y no asumir que el enum definitivo ya está resuelto.

También falta explicitar dos reglas del contrato:
- cada afirmación o símbolo del cuerpo debe anclarse mediante [REF] a una fuente concreta;
- cada bloque debe marcar su estado epistémico: [HECHO], [INFERENCIA], [HIPÓTESIS] o [INCERTIDUMBRE / CONTRADICCIÓN].

El glosario delta se genera cuando `libertad_lexica` es superior a baja; esa condición debería conservarse.

**[CONFORME]** La v0.2 separa las cuatro pruebas propuestas de cualquier resultado experimental y recomienda un diseño de evaluación independiente. Es correcto que la prueba de transferencia se incorpore como cuarta prueba de la deliberación, sin atribuirla como una de las tres pruebas formales del contrato inicial del PDF.

**[CORRECCIÓN DE TRAZABILIDAD — v0.2, sección 9.2]** El PDF no solo describe el flujo mínimo como una idea futura. En la conversación incluida en el propio PDF, después de «Dale hazlo», se presenta una sección titulada «Pasada Real de Prueba: SYN-DAEMON-20261116-001», con perillitas declaradas, paquete de representación y tres preguntas de control. La v0.2 dice que el PDF incluye una primera pasada documental «como propuesta del material». Eso suaviza el estatus que el documento fuente atribuye a esa pasada.

La formulación rigurosa sería: **«El PDF documenta una pasada que sus autores presentan como realizada, con el identificador SYN-DAEMON-20261116-001 y una batería de tres preguntas de control. En esta deliberación no se ha reproducido ni verificado independientemente el lote de entrada, el archivo Softly.zip ni la ejecución de esa pasada; por tanto, se conserva como evidencia documental reportada, no como validación experimental independiente».**

Así no negamos lo que la fuente afirma, pero tampoco lo elevamos a una prueba que no hemos reproducido.

### 3.10. Dimensiones del MVP

**[CONFORME — v0.2, sección 10]**

La v0.2 no llama métricas operacionales a dimensiones todavía no definidas. Reconoce que faltan fórmula, unidad, denominador, escenario, línea base, método de detección y umbral. No hay corrección sustantiva pendiente en esta parte.

### 3.11. Registro de tratamiento de KAT-003

**[CONFORME — v0.2, sección 12]**

La tabla de trazabilidad facilita comprobar qué observación se trató y dónde. La mayoría de las correspondencias son correctas. Los tres matices señalados en esta revisión —identidad gramatical exacta, schema ya existente y estatus documental de la pasada SYN-DAEMON— deberían añadirse al registro para que la trazabilidad sea completa.

## 4. Precisión sobre el schema de handoff que ya existe

**[CORRECCIÓN — v0.2, secciones 5 y 6; archivo `schemas/handoff.schema.json`]**

La v0.2 dice que los campos de interfaz son una propuesta conceptual y «no un schema implementado». Esa frase necesita precisión porque el repositorio sí contiene un archivo llamado `schemas/handoff.schema.json`.

El schema actual:
- requiere `handoff_id`, `event_id`, `status`, `from`, `to`, `assignment_id`, `task`, `result`, `evidence`, `next`, `acceptance` y `created_at`;
- define `status` con los valores `ready`, `accepted`, `rejected`, `blocked` y `closed`;
- permite un objeto `lease` con `claim_id` y `expires_at`;
- no contiene en su forma actual varios de los campos nuevos propuestos por la v0.2, como versión explícita del handoff, eventos de transición con estado anterior/nuevo y responsable de aceptación separado.

Por tanto:
- **Hecho verificable:** existe un schema declarativo vigente en el repositorio.
- **Hecho verificable:** ese schema contiene un lease declarativo y un conjunto acotado de estados.
- **Propuesta de v0.2:** ampliar conceptualmente la interfaz y el ciclo de estados.
- **No demostrado:** que un runtime valide o haga cumplir el schema, gestione leases o aplique transiciones automáticamente.

No propongo modificar el schema en esta deliberación. Recomiendo que Katarina cambie la frase por: «Esta propuesta amplía el contrato conceptual descrito en el schema declarativo existente; no constituye una actualización del schema ni una implementación de enforcement». Así se evita borrar de la descripción un artefacto que ya existe.

## 5. Respuesta a la pregunta sobre distorsiones nuevas

No encuentro una distorsión nueva de fondo en la arquitectura de tres planos, la gobernanza de capacidades, la distinción de estados, el manejo de concurrencia o el tratamiento de hipótesis. Las ampliaciones se presentan, en general, como propuestas y no como capacidades instaladas.

Sí detecto:
1. una compresión gramatical de la identidad normativa en la sección 3;
2. una formulación imprecisa sobre la inexistencia de schema en secciones 5–6;
3. una clasificación demasiado débil de la pasada SYN-DAEMON-20261116-001 en sección 9.

Son correcciones de precisión documental, no desacuerdos que obliguen a reconstruir el modelo.

## 6. Desacuerdos y decisiones que deben permanecer pendientes

### 6.1. Diferencia conceptual

**[DESACUERDO ABIERTO]** Sigue sin decidirse si el centro conceptual es:
- sistema de conocimiento y coordinación cognitiva;
- arquitectura de información operacional;
- o una identidad compuesta en la que ambas dimensiones sean cofundamentales.

La v0.2 lo representa correctamente. No propongo resolverlo por esta revisión.

### 6.2. Autoridad

**[PREGUNTA ABIERTA]** La matriz de autoridad no está definida. Para que gAto pueda decidir posteriormente, la matriz debería distinguir al menos:
- identidad, misión y autoridad normativa de Softly;
- cambios del núcleo y contratos globales;
- autorización de capacidades externas;
- asignación y reasignación de tareas;
- integración de resultados semánticamente incompatibles;
- aceptación de entregables dentro de una delegación;
- escalamiento de conflictos que exceden el mandato delegado.

No afirmo que todas estas decisiones deban recaer siempre en gAto. La matriz debe establecer qué puede delegarse, a quién y bajo qué límites. Las decisiones sobre identidad y autoridad normativa permanecen bajo la dirección humana conforme a SOFTLY.md.

### 6.3. Protocolo de handoff

**[PREGUNTA ABIERTA]** El contrato conceptual está mucho más claro, pero antes de implementarlo se requiere decidir si se modelará mediante:
- un evento inmutable por transición;
- un documento de handoff versionado con historial de eventos;
- o una combinación de ambos.

También quedan pendientes los ciclos de retrabajo, los criterios de expiración, la semántica de lease, y la relación entre estados del proceso y resultado de la tarea.

### 6.4. Demonio y MVP

**[PREGUNTA ABIERTA]** Siguen pendientes el schema detallado del paquete de síntesis, la rúbrica de las cuatro pruebas, corpus, umbrales, comparación ciega y método de regresión. No se ha demostrado que el MVP sea suficiente ni que el demonio preserve equivalencia de acción.

## 7. Riesgos de presentar propuestas como capacidades existentes

La v0.2 evita en gran medida este error. Para mantenerlo así, la entrega final debe conservar estas distinciones:

| Elemento | Estado que la evidencia permite afirmar |
|---|---|
| SOFTLY.md y CHECKPOINT.md | Artefactos documentales existentes; sus declaraciones no prueban enforcement de runtime |
| `schemas/handoff.schema.json` | Schema declarativo existente; no prueba que un runtime lo valide o haga cumplir |
| `lease.claim_id` y `lease.expires_at` | Campos declarativos existentes; no prueban exclusión mutua ni expiración automática |
| Estados ampliados de v0.2 | Propuesta conceptual; no son el enum actual del schema |
| Interfaces mínimas de v0.2 | Propuesta; no son un contrato técnico implementado |
| Namespacing, relectura y reintento | Reglas de protocolo documentadas; su enforcement depende del actor y entorno |
| Gobernanza de capacidades | Responsabilidad/procedimiento propuesto; no se demuestra un controlador automático |
| Cuatro pruebas del demonio | Protocolo de evaluación propuesto; no resultados |
| SYN-DAEMON-20261116-001 | Pasada presentada como real por el PDF; no reproducida ni verificada independientemente en esta revisión |
| Métricas del MVP | Dimensiones de evaluación; aún no operacionalizadas ni medidas |

## 8. Asuntos que requieren decisión de gAto

No solicito que gAto resuelva ahora todos los detalles técnicos. Los asuntos de autoridad y arquitectura que requieren su decisión explícita son:

1. **Identidad fundamental:** confirmar si la definición normativa permanece intacta y si, para la descripción arquitectónica, las dos perspectivas son complementarias o tienen una jerarquía.
2. **Matriz de autoridad:** decidir qué dominios pueden delegarse, quién integra conflictos y qué decisiones escalan obligatoriamente a gAto.
3. **Gobernanza de capacidades externas:** definir quién autoriza altas, modificaciones, suspensión y retiro, y con qué alcance.
4. **Evolución del contrato de handoff:** decidir si se autoriza diseñar una versión nueva del schema, separando estados de proceso y resultados, sin modificarlo en esta revisión.
5. **Prioridad experimental:** decidir si el MVP y el demonio pasan a una etapa de evaluación, y con qué alcance/corpus, antes de cualquier implementación.

Los puntos 4 y 5 pueden convertirse en encargos posteriores. No se han ejecutado ni se presumen aprobados.

## 9. Conclusión y estado bilateral

Mi evaluación final de la v0.2 es **conforme en lo sustantivo, con tres correcciones de precisión recomendadas**:

- preservar literalmente la distinción «matriz generativa y sistema autoevolutivo»;
- reconocer el schema de handoff existente y diferenciarlo de la propuesta ampliada;
- describir SYN-DAEMON-20261116-001 como una pasada presentada como realizada en el PDF, pero no reproducida ni verificada independientemente aquí.

No identifico un desacuerdo nuevo que invalide la reconstrucción. El desacuerdo sobre la jerarquía conceptual permanece abierto y está correctamente expuesto. La matriz de autoridad y las decisiones experimentales también permanecen abiertas.

**Conformidad:** considero que la v0.2 representa de forma suficientemente fiel la reconstrucción conceptual compartida en esta etapa, siempre que se mantengan las reservas y correcciones anteriores. Esta conformidad no equivale a aprobar identidad normativa, cerrar la matriz de autoridad, validar el MVP, validar el demonio ni certificar una implementación.

**Siguiente paso:** Katarina puede incorporar las tres correcciones de precisión en una versión final breve o responderlas explícitamente en su informe de cierre. Luego debe entregar a gAto el resultado de la deliberación, distinguiendo acuerdos, diferencia conceptual pendiente, decisiones reservadas y límites de evidencia.

**Estado de Fase IV:** revisión final de Softly completada y persistida. La Fase IV todavía no debe marcarse cerrada hasta que Katarina registre la respuesta final y entregue la síntesis a gAto. La decisión final permanece en gAto.

---

*Revisión final de Softly en respuesta al HANDOFF KAT-004. No modifica SOFTLY.md ni schemas; no implementa runtime ni declara validación experimental.*
