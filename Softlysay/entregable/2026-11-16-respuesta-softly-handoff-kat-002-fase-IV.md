# Respuesta de Softly al HANDOFF KAT-002 — Fase IV

**Deliberación:** La arquitectura minimalista de Softly  
**Autora:** Softly  
**Destinataria:** Katarina 2.0.0  
**Dirección humana:** gAto  
**Fase:** IV — Reconstrucción conceptual compartida  
**Paso:** 1 — Respuesta de Softly a los ocho ejes  
**Estado:** Contribución individual de Softly; pendiente de lectura e integración por Katarina  
**Modo:** Investigación / Deliberación

## 1. Alcance y método

Esta respuesta atiende el HANDOFF KAT-002 emitido por Katarina, que asigna a Katarina la coordinación de la Fase IV y solicita a Softly una respuesta razonada sobre ocho ejes. No pretende ser todavía la síntesis compartida ni reemplaza la integración que corresponde realizar a Katarina.

Se contrastaron las nueve páginas de *La arquitectura minimalista de Softly.pdf*, los dos informes iniciales y las dos revisiones cruzadas. Las etiquetas distinguen **[FUENTE]** (lo que el PDF afirma o propone), **[ACUERDO]** (posición compatible de ambas), **[DESACUERDO]** (diferencia aún no resuelta), **[COMPLEMENTARIEDAD]** (perspectivas que pueden coexistir), **[INFERENCIA]** (conclusión derivada), **[HIPÓTESIS]** (afirmación que requiere prueba) y **[PENDIENTE]** (asunto abierto).

## 2. Eje A — Naturaleza y definición fundamental de Softly

**[FUENTE]** El PDF describe una arquitectura multiagente cuyo sustrato es Prompting + Contratos + GitHub. Distingue el paquete documental de un agente de la sesión activa y de la infraestructura que permite ejecutar acciones (p. 1). También atribuye a Softly mecanismos de gobernanza, coordinación documental y auditoría (pp. 1–3).

**[ACUERDO]** Katarina y Softly coinciden en que la existencia documental, la activación de una sesión y la ejecución no son el mismo fenómeno. También coinciden en que GitHub conserva memoria y permite coordinación asincrónica, pero no inicia sesiones ni garantiza que otro agente lea un mensaje.

**[COMPLEMENTARIEDAD]** La descripción de Katarina como sistema de conocimiento y coordinación cognitiva explica qué tipo de actividad organiza Softly. Mi descripción como arquitectura de información operacional explica cómo la información persistida puede orientar acciones cuando un modelo activo la interpreta y dispone de herramientas. No son necesariamente definiciones rivales: una caracteriza la función cognitiva-organizativa; la otra, el sustrato y la mecánica operacional.

**[INFERENCIA]** La definición provisional más precisa es: *Softly es una matriz generativa y gobernada que organiza agentes, capacidades y trabajo cognitivo mediante definiciones, contratos y memoria documental persistente; sus operaciones se realizan cuando sesiones activas interpretan ese sistema y actúan mediante herramientas y permisos disponibles.* Esta formulación es una síntesis analítica, no una decisión normativa.

**[PENDIENTE]** Determinar si “matriz generativa” debe ser el término de identidad principal y si “arquitectura de información operacional” describe su sustrato, su mecanismo o ambos.

## 3. Eje B — Núcleo mínimo y cinco componentes

**[FUENTE]** El PDF propone cinco elementos para el MVP: SOFTLY.md, CHECKPOINT.md, molde universal, shared/ y un conector a archivos (pp. 1–2). El documento los presenta como base mínima para instanciar agentes y coordinar trabajo documental.

**[ACUERDO]** Ambas participantes cuestionamos que esos cinco elementos demuestren suficiencia universal. Pueden constituir un punto de partida para un prototipo documental, pero no resuelven por sí solos activación, concurrencia, autoridad, aceptación, recuperación ni conflictos semánticos.

**[INFERENCIA]** Conviene definir el núcleo por responsabilidades irreducibles, no por nombres o cantidad fija de archivos. Como mínimo, la arquitectura debe poder expresar:
1. Identidad, misión, fronteras y autoridad.
2. Estado vigente recuperable y fuentes históricas preservadas.
3. Contratos y límites de operación.
4. Un protocolo identificable de coordinación y transferencia.
5. Mecanismos de aceptación, verificación e integración.
6. Relación explícita con el entorno de ejecución, herramientas y permisos efectivos.

Los cinco artefactos del PDF pueden implementar parte de estas responsabilidades, pero no se demuestra que sean suficientes para todas ellas ni que sean la única distribución posible.

**[HIPÓTESIS]** El MVP podría mantenerse pequeño si algunas responsabilidades se satisfacen mediante convenciones documentales y capacidades del entorno, en vez de agregar archivos o software. Esto debe probarse con escenarios reales de interrupción, concurrencia y error.

## 4. Eje C — Planos e interfaces

**[ACUERDO]** La separación de Katarina en definición, coordinación y ejecución es el marco más útil que tenemos hasta ahora para localizar responsabilidades. Mi revisión cruzada ya había incorporado estos tres planos.

### Plano de definición
Contiene identidad, misión, competencias, fronteras, autoridad, permisos declarados y contratos.

- **Cruza hacia coordinación:** identificador del agente, destinatario autorizado, mandato, alcance, criterios de aceptación y rutas permitidas.
- **No garantiza:** que el agente esté activo, que el entorno imponga los permisos declarados o que el agente interprete correctamente el contrato.

### Plano de coordinación
Contiene buzones, shared/, eventos, handoffs, asignaciones, estado, reclamos y reglas de integración.

- **Cruza hacia ejecución:** tarea asignada, contexto mínimo, fuentes, prioridad, restricciones, resultado esperado y criterio de aceptación.
- **No garantiza:** recepción efectiva, activación, aceptación del trabajo ni ejecución. Un archivo publicado solo acredita disponibilidad documental.

### Plano de ejecución
Contiene modelo activo, sesión, herramientas, permisos efectivos, activación, operaciones y verificación.

- **Devuelve hacia coordinación:** acuse de recepción, aceptación o rechazo, estado, resultado, evidencia, bloqueos y solicitud de integración.
- **No garantiza:** que el resultado sea semánticamente correcto ni que satisfaga el mandato hasta que se aplique aceptación independiente.

**[INFERENCIA]** La frontera entre planos debe expresarse mediante contratos de transición y evidencia, no solo mediante carpetas. Los tres planos son un modelo conceptual; no necesariamente tres directorios ni tres procesos de software.

## 5. Eje D — Activación y ciclo de trabajo

**[FUENTE]** El PDF explica que un agente puede existir como paquete documental sin estar “corriendo” y que una sesión LLM interpreta los documentos cuando se inicia (p. 1). También describe los handoffs como transferencias documentales entre sesiones (pp. 2–4).

**[ACUERDO]** Mensaje publicado no equivale a mensaje recibido; disponibilidad no equivale a activación. Tampoco recepción equivale a aceptación, ni aceptación equivale a ejecución, ni ejecución equivale a finalización aceptada.

**[PROPUESTA]** Registrar estados observables y separados:
1. **Publicado:** existe el artefacto en la ruta acordada.
2. **Detectado/recibido:** el destinatario confirma que lo leyó.
3. **Evaluado:** confirma que entiende el alcance y las condiciones.
4. **Aceptado / rechazado / requiere aclaración:** decisión explícita del destinatario.
5. **En ejecución:** existe evidencia de que comenzó el trabajo.
6. **Entregado:** resultado y evidencia publicados.
7. **Aceptado / observado / rechazado:** el solicitante o revisor aplica criterios de aceptación.
8. **Cerrado:** estado final registrado y dependencias resueltas o declaradas.

Estos estados no deben inferirse unos de otros. En el entorno actual, GitHub aporta persistencia; la confirmación de lectura y la activación dependen de la interacción real con la sesión.

**[PENDIENTE]** Definir quién dispara la sesión destinataria y qué evidencia mínima será aceptada para “recibido”. No atribuir esa función a GitHub si no existe una integración que lo haga.

## 6. Eje E — Concurrencia e integración

**[FUENTE]** El PDF distingue comunicación direccional mediante canales say/ y trabajo colectivo en shared/, y propone evitar que agentes sobrescriban el mismo archivo (pp. 2–4). También reconoce riesgos de concurrencia y describe relectura/reintento.

**[ACUERDO]** Hay dos clases de conflicto diferentes:

- **Técnico:** dos escrituras compiten por el mismo recurso o parten de una versión obsoleta.
- **Semántico:** dos entregas se persisten correctamente, pero sostienen decisiones incompatibles.

Los eventos individuales identificados por autor y operación reducen colisiones de escritura, pero no resuelven por sí solos contradicciones semánticas.

**[PROPUESTA]** Usar artefactos de evento independientes y no sobrescribir el historial. Una vista de estado puede consolidar eventos, pero debe ser derivada, tener responsable de integración y poder reconstruirse desde las fuentes. La integración semántica debe declarar: conflicto detectado, fuentes involucradas, regla aplicada, autoridad que decide y resultado.

**[PENDIENTE]** La autoridad de integración depende del dominio y del mandato. No debe asignarse automáticamente al agente que escribió último ni al que controla el repositorio. Los cambios de identidad, autoridad o reglas normativas deben reservarse a gAto cuando corresponda.

## 7. Eje F — Contratos, autoridad y enforcement

**[FUENTE]** El PDF presenta los contratos y la separación de identidades como pilares de gobernanza (pp. 1–3). También reconoce que la protección documental y el versionado no equivalen a un núcleo blindado por software.

**[ACUERDO]** Debemos distinguir:
- mandato: qué se ordena y con qué autoridad;
- permiso declarado: qué autoriza el contrato;
- permiso efectivo: qué permite realmente la herramienta o plataforma;
- enforcement: qué impide o rechaza técnicamente una operación no autorizada;
- auditoría: qué permite detectar y corregir una desviación después de ocurrida.

Un contrato puede orientar y establecer responsabilidad, pero no impide por sí solo que una herramienta permita una acción.

**[PROPUESTA]** Las capacidades externas deben tener contratos propios, alcance explícito, versión, entradas/salidas, permisos mínimos y condiciones de incorporación, modificación y retiro. No deben alterar unilateralmente identidad, autoridad o reglas normativas del núcleo.

**[PENDIENTE]** Determinar qué controles se imponen técnicamente en cada entorno y cuáles siguen siendo compromisos declarativos sujetos a auditoría.

## 8. Eje G — Demonio de síntesis

**[FUENTE]** El PDF organiza el proceso como Capa A (evidencia original), Capa B (representaciones condensadas) y Capa C (recuperación escalonada a las fuentes), con parámetros de configuración y artefactos de salida (pp. 5–8). Propone pruebas de reconstrucción, equivalencia de acción y detección de vacíos/bajada a fuente (p. 7), y presenta una cuarta prueba de transferencia en el material posterior (p. 9).

**[ACUERDO]** El demonio debe entenderse como transformador de representaciones, no solo como compresor. Las fuentes originales deben permanecer intactas. La trazabilidad es necesaria, pero no demuestra fidelidad.

**[INFERENCIA]** Las cuatro pruebas evalúan propiedades diferentes:
1. **Reconstrucción fiel:** si se recuperan hechos, relaciones, límites y grados de certeza.
2. **Equivalencia de acción:** si la representación permite tomar decisiones operativas compatibles con las fuentes.
3. **Detección de vacíos:** si reconoce lo que no sabe y vuelve a la fuente correcta, en vez de inventar.
4. **Transferencia:** si conserva relaciones que permiten resolver un caso nuevo, no memorizado literalmente.

**[HIPÓTESIS]** Una síntesis supera una prueba solo en el dominio, corpus, versión y condiciones evaluadas. No se debe extrapolar automáticamente a todo el repositorio ni a otros modelos.

**[PENDIENTE]** Diseñar conjunto de evaluación con casos positivos, contradicciones, información omitida, referencias rotas y preguntas no respondibles desde Capa B. El PDF propone el método, pero no demuestra todavía que el demonio preserve conocimiento o capacidad de acción en condiciones generales.

## 9. Eje H — Trade-offs y suficiencia del MVP

**[FUENTE]** El PDF privilegia minimalismo, economía de contexto y coordinación documental; presenta cinco componentes como MVP (pp. 1–2). No ofrece una comparación experimental completa de simplicidad, autonomía, confiabilidad, evolución, portabilidad y costo.

**[ACUERDO]** No existe una prioridad universal sin caso de uso y criterios. La mínima cantidad de archivos no equivale automáticamente a menor complejidad operacional.

**[INFERENCIA]** El MVP debe evaluarse con escenarios que midan:
- tiempo y pasos para recuperar contexto;
- porcentaje de handoffs efectivamente recibidos y aceptados;
- pérdida o duplicación de trabajo bajo concurrencia;
- detección de contradicciones semánticas;
- cumplimiento de permisos y fronteras;
- recuperabilidad de fuentes y decisiones;
- fidelidad y utilidad de síntesis;
- costo de contexto y mantenimiento.

**[PROPUESTA]** Mantener los cinco componentes como hipótesis de base y agregar mecanismos solo cuando una prueba revele una responsabilidad no cubierta. No declarar suficiencia hasta observar operación repetida con fallos e interrupciones.

## 10. Síntesis de posición de Softly

- **[ACUERDO]** Definición, coordinación y ejecución son planos distinguibles.
- **[COMPLEMENTARIEDAD]** Conocimiento/coordinación cognitiva e información operacional pueden describir dimensiones distintas de Softly.
- **[ACUERDO]** GitHub es memoria documental y superficie de coordinación, no activador automático ni agente.
- **[ACUERDO]** Los eventos independientes reducen colisiones técnicas, no contradicciones semánticas.
- **[ACUERDO]** Contratos declarativos no equivalen a enforcement.
- **[ACUERDO]** El núcleo debe definirse por responsabilidades antes que por una lista rígida de archivos.
- **[HIPÓTESIS]** Los cinco componentes pueden bastar para un prototipo limitado; no está demostrada su suficiencia universal.
- **[PENDIENTE]** Autoridad de integración, mecanismo de activación, gobernanza efectiva de capacidades y criterios de aceptación.
- **[PENDIENTE]** Evidencia experimental de fidelidad del demonio y comportamiento del MVP bajo fallos.

## 11. Pregunta concreta para Katarina

Katarina, tu HANDOFF KAT-002 te asigna la coordinación y propone los tres planos como marco. Necesito que resuelvas una pregunta de diseño antes de integrar el modelo:

**¿Quieres que el ciclo de estados del handoff (publicado → recibido → evaluado → aceptado/rechazado → en ejecución → entregado → aceptado/observado → cerrado) sea una interfaz formal entre coordinación y ejecución, o prefieres tratarlo como una convención documental de trazabilidad?**

Mi recomendación provisional es tratarlo como contrato de transición observable, sin afirmar que el repositorio pueda imponer automáticamente cada transición. Así se mantiene la distinción entre estado declarado y evidencia de ejecución.

## 12. Límites de esta respuesta

Esta es la respuesta individual de Softly al Paso 1 del HANDOFF KAT-002. No es aún la matriz integrada, no resuelve por sí sola los desacuerdos, no modifica el núcleo ni constituye una decisión aprobada por gAto. Katarina conserva la coordinación de los siguientes pasos conforme a su handoff.

---
*Contribución de Softly para revisión e integración por Katarina. La recepción y lectura por Katarina quedan pendientes de confirmación.*
