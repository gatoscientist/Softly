# Reconstrucción arquitectónica integrada — Fase IV
**Deliberación:** La arquitectura minimalista de Softly  
**Coordinación:** Katarina 2.0.0 — `katarina` (Agent Softly)  
**Participante:** Softly  
**Dirección humana:** gAto  
**Versión:** 0.1 — integración de trabajo para revisión bilateral  
**Fecha:** 2026-11-16  
**Estado:** Integración de Katarina completada; pendiente de revisión explícita de Softly y decisión de gAto

## 1. Alcance y base documental

Este documento integra:
1. *La arquitectura minimalista de Softly.pdf* (9 páginas).
2. Informe inicial independiente de Katarina.
3. Informe inicial independiente de Softly.
4. Revisión cruzada de Softly sobre Katarina.
5. Revisión cruzada de Katarina sobre Softly.
6. Respuesta de Softly al HANDOFF KAT-002, Fase IV.

No sustituye las fuentes. Distingue:
- **[FUENTE]** contenido explícito del PDF;
- **[ACUERDO]** posiciones coincidentes;
- **[COMPLEMENTARIEDAD]** perspectivas compatibles;
- **[INFERENCIA]** reconstrucción derivada;
- **[PROPUESTA]** diseño sugerido, no aprobado;
- **[HIPÓTESIS]** afirmación que requiere evaluación;
- **[PENDIENTE]** cuestión no resuelta;
- **[DECISIÓN gAto]** reservado a aprobación humana explícita.

Esta versión es una integración de Katarina. No se presenta todavía como consenso bilateral: Softly debe revisarla expresamente.

## 2. Definición arquitectónica provisional

**[FUENTE]** El PDF describe una arquitectura multiagente apoyada en Prompting + Contratos + GitHub, con identidad documental, coordinación asincrónica, gobernanza y mecanismos de síntesis.

**[ACUERDO]** La existencia documental de un agente, la activación de una sesión y la ejecución de operaciones son fenómenos distintos. GitHub conserva memoria y permite coordinación persistente, pero no activa sesiones ni garantiza que un destinatario lea un artefacto.

**[COMPLEMENTARIEDAD]** “Sistema de conocimiento y coordinación cognitiva” describe la función que organiza Softly; “arquitectura de información operacional” describe cómo la información, los contratos y los eventos orientan operaciones cuando una sesión activa los interpreta y dispone de herramientas. No es necesario tratarlas como definiciones excluyentes.

**[INFERENCIA — definición de trabajo]**

> Softly es una matriz generativa y gobernada que organiza agentes, capacidades y trabajo cognitivo mediante definiciones, contratos y memoria documental persistente. Sus operaciones ocurren cuando sesiones activas interpretan esa arquitectura y actúan a través de herramientas y permisos disponibles en su entorno.

Esta formulación es una síntesis analítica provisional, no un cambio de identidad ni una decisión normativa.

**[PENDIENTE]** Softly y Katarina deben confirmar si “matriz generativa” es la identidad fundamental y si “arquitectura de información operacional” caracteriza el sustrato, el mecanismo o ambos.

## 3. Núcleo mínimo: responsabilidades antes que artefactos

**[FUENTE]** El PDF propone cinco elementos para el MVP: SOFTLY.md, CHECKPOINT.md, molde universal, shared/ y conector a archivos.

**[ACUERDO]** Los cinco elementos son una hipótesis de implementación mínima, no prueba de suficiencia universal ni definición rígida del núcleo.

**[INFERENCIA]** El núcleo debe definirse por responsabilidades irreducibles:

1. **Identidad y autoridad:** quién es cada agente, misión, competencias, fronteras y dirección humana.
2. **Estado y memoria:** estado vigente recuperable, historial preservado y referencias a fuentes.
3. **Contratos y límites:** alcance, permisos declarados, prohibiciones y criterios.
4. **Coordinación:** eventos identificables, asignaciones, handoffs, recepción y transferencia.
5. **Aceptación e integración:** evidencia de entrega, criterios de aceptación y resolución de incompatibilidades.
6. **Frontera de ejecución:** modelo/sesión activa, herramientas y permisos efectivos claramente diferenciados de la definición documental.

**[HIPÓTESIS]** Es posible que los cinco artefactos cubran estas responsabilidades para un prototipo acotado mediante convenciones y capacidades del entorno. No se ha demostrado. La suficiencia debe probarse con interrupciones, concurrencia, errores, handoffs no recibidos y resultados incompatibles.

## 4. Modelo de tres planos e interfaces

Los tres planos son una separación conceptual de responsabilidades; no implican necesariamente tres directorios, servicios o procesos.

### 4.1 Definición
Incluye identidad, misión, competencias, fronteras, autoridad, permisos declarados y contratos.

**Interfaz hacia coordinación:** identificador de agente, destinatario, mandato, alcance autorizado, prioridad, fuentes, resultado esperado y criterios de aceptación.

**No garantiza:** activación, recepción, interpretación correcta ni enforcement efectivo de los permisos.

### 4.2 Coordinación
Incluye buzones, shared/, eventos, asignaciones, handoffs, estados, reclamos y reglas de integración.

**Interfaz hacia ejecución:** tarea, contexto mínimo, fuentes, prioridad, restricciones, entregable esperado y criterio de aceptación.

**No garantiza:** que el destinatario haya leído el encargo, acepte la tarea o haya iniciado ejecución.

### 4.3 Ejecución
Incluye modelo activo, sesión, herramientas, permisos efectivos, operaciones y verificación.

**Retorno hacia coordinación:** acuse de recepción, evaluación, aceptación/rechazo, estado, resultado, evidencia, bloqueos y solicitud de integración.

**No garantiza:** corrección semántica ni satisfacción del mandato hasta que se aplique una evaluación de aceptación.

**[INFERENCIA]** Las fronteras entre planos deben definirse mediante contratos de transición y evidencia observable, no solo mediante carpetas o nombres de archivos.

## 5. Ciclo de handoff: contrato formal de transición observable

**Pregunta planteada por Softly:** ¿el ciclo de estados es una interfaz formal entre coordinación y ejecución o una convención documental?

**Resolución de Katarina:** debe tratarse como **contrato formal de transición observable**. No es una mera convención, porque cada estado tiene significado operacional y habilita expectativas distintas. Pero tampoco debe confundirse con enforcement automático: GitHub no impone por sí mismo la recepción, aceptación ni ejecución.

### Estados propuestos

1. **Publicado:** el artefacto existe en la ruta acordada. Evidencia: ruta y commit.
2. **Recibido:** el destinatario confirma que lo leyó. Evidencia: acuse explícito atribuible.
3. **Evaluado:** el destinatario confirma que entiende alcance, fuentes, límites y resultado esperado. Evidencia: evaluación explícita.
4. **Aceptado / rechazado / requiere aclaración:** decisión explícita de asumir, declinar o solicitar precisión.
5. **En ejecución:** existe evidencia de inicio del trabajo; no se infiere de la aceptación.
6. **Entregado:** resultado y evidencia fueron publicados.
7. **Aceptado / observado / rechazado:** el responsable de aceptación contrasta el resultado con los criterios acordados.
8. **Cerrado:** estado final registrado y dependencias resueltas o declaradas.

Reglas:
- Ningún estado posterior se infiere automáticamente del anterior.
- Publicado no equivale a recibido; recibido no equivale a aceptado; aceptado no equivale a ejecución; entregado no equivale a aceptado.
- Cada transición debe registrar actor, fecha, estado anterior, estado nuevo y evidencia suficiente.
- Un rechazo o bloqueo no borra el historial: produce un evento nuevo y trazable.
- La plataforma puede aportar evidencia de persistencia; la confirmación de lectura, aceptación y ejecución requiere evidencia de la sesión o actor correspondiente.

**[PROPUESTA]** Este contrato debe ser la interfaz común entre coordinación y ejecución. Su implementación concreta puede variar según el entorno.

## 6. Concurrencia, consistencia e integración semántica

**[ACUERDO]** Se deben separar dos clases de conflicto:

- **Conflicto técnico:** escrituras concurrentes, versiones obsoletas, colisiones o pérdida de cambios.
- **Conflicto semántico:** resultados persistidos correctamente que contienen decisiones, interpretaciones o recomendaciones incompatibles.

**[PROPUESTA]**
- Preferir eventos individuales identificados por autor y operación, evitando un archivo común mutable como registro primario.
- Mantener el historial original; cualquier vista consolidada será derivada, versionada y reconstruible.
- La integración semántica debe registrar conflicto detectado, fuentes, alternativas, regla aplicada, autoridad que decide y resultado.
- No atribuir autoridad al último escritor ni al actor que controla el repositorio por el solo hecho de persistir el cambio.

**Autoridad:** depende del dominio y del mandato. Las decisiones sobre identidad, autoridad, permisos normativos y cambios del núcleo quedan reservadas a gAto cuando corresponda. Las integraciones dentro de una tarea delegada pueden asignarse a un responsable explícito, sujeto a los contratos vigentes.

**[PENDIENTE]** Definir una matriz de autoridad por tipo de decisión y qué conflictos deben escalarse obligatoriamente a gAto.

## 7. Contratos, permisos y gobernanza de capacidades

Se distinguen cinco conceptos:

- **Mandato:** instrucción y autoridad de origen.
- **Permiso declarado:** autorización descrita en el contrato.
- **Permiso efectivo:** acción realmente permitida por herramientas y plataforma.
- **Enforcement:** control técnico que bloquea o rechaza una acción.
- **Auditoría:** mecanismo para detectar, explicar y corregir desviaciones.

**[ACUERDO]** Un contrato declarativo no equivale a enforcement técnico.

**[PROPUESTA]** Cada capacidad externa debe declarar:
- identidad y versión;
- propósito y alcance;
- entradas y salidas;
- dependencias y fuentes;
- permisos mínimos;
- criterios de aceptación;
- límites y prohibiciones;
- procedimiento de incorporación, modificación, suspensión y retiro;
- responsable de integración.

Una capacidad externa no puede modificar unilateralmente identidad, autoridad ni reglas normativas del núcleo. La modularidad sin gobernanza no basta.

**[PENDIENTE]** Para cada entorno de ejecución se debe documentar qué permisos son técnicamente impuestos y cuáles son compromisos declarativos sujetos a auditoría.

## 8. Demonio de síntesis como transformador de representaciones

**[FUENTE]** El PDF propone preservar evidencia original (Capa A), producir representaciones condensadas (Capa B) y permitir recuperación escalonada a las fuentes (Capa C). Incluye pruebas de reconstrucción, equivalencia de acción y detección de vacíos; la deliberación incorporó una cuarta prueba de transferencia.

**[ACUERDO]** El demonio es un transformador de representaciones, no solo un compresor. Las fuentes originales permanecen intactas. La trazabilidad es necesaria, pero no demuestra fidelidad.

### Cuatro pruebas propuestas

1. **Reconstrucción fiel:** recuperar hechos, relaciones, límites, atribuciones y grados de certeza.
2. **Equivalencia de acción:** producir decisiones operativas compatibles con las fuentes bajo tareas equivalentes.
3. **Detección de vacíos:** reconocer información ausente, contradictoria o insuficiente y volver a la fuente correcta sin inventar.
4. **Transferencia:** resolver un caso nuevo no expresado literalmente en la síntesis, preservando relaciones relevantes.

**[HIPÓTESIS]** La aprobación de una prueba solo acredita desempeño en el corpus, versión, dominio y condiciones evaluadas; no demuestra fidelidad universal ni equivalencia entre modelos.

**[PROPUESTA]** El conjunto de evaluación debe incluir casos positivos, contradicciones, omisiones, referencias rotas, cambios de versión y preguntas imposibles de responder desde la síntesis. Registrar errores y permitir reconstruir el resultado desde fuentes.

## 9. Trade-offs y evaluación del MVP

**[ACUERDO]** No existe prioridad universal entre simplicidad, autonomía, confiabilidad, evolución, portabilidad y costo de contexto. Menos archivos no implica automáticamente menos complejidad operacional.

**[PROPUESTA]** Mantener los cinco componentes como hipótesis inicial y agregar mecanismos solo cuando una prueba muestre una responsabilidad no cubierta.

Métricas/escenarios de evaluación:
- tiempo y pasos para recuperar contexto;
- tasa de handoffs recibidos, aceptados y completados;
- pérdida, duplicación o bloqueo de trabajo bajo concurrencia;
- detección y resolución de contradicciones semánticas;
- cumplimiento de fronteras y permisos;
- recuperabilidad de fuentes y decisiones;
- fidelidad y utilidad de las síntesis;
- costo de contexto, mantenimiento y recuperación.

No se ha ejecutado este plan. No hay evidencia experimental que permita declarar el MVP suficiente ni el demonio validado.

## 10. Matriz de acuerdos, complementariedades y asuntos abiertos

### Acuerdos robustos
1. Definición, coordinación y ejecución son planos distinguibles.
2. GitHub es memoria y superficie persistente de coordinación; no agente ni activador automático.
3. Los cinco componentes no demuestran suficiencia universal.
4. El núcleo se define por responsabilidades, no por una lista rígida de archivos.
5. Eventos individuales reducen colisiones técnicas, pero no contradicciones semánticas.
6. Contratos declarativos no equivalen a enforcement.
7. Las fuentes originales deben preservarse.
8. Las entregas requieren criterios y evidencia de aceptación.
9. Portabilidad documental no prueba equivalencia conductual.
10. Las propuestas no son decisiones aprobadas por gAto.

### Complementariedades
- Sistema de conocimiento/coordinación cognitiva describe la función organizativa.
- Arquitectura de información operacional describe el sustrato y la mecánica por la que información y contratos orientan operaciones.
- Ambas perspectivas pueden coexistir en una definición por capas.

### Desacuerdos sustantivos
No queda identificado un desacuerdo binario irresuelto entre los informes disponibles. Sí persisten elecciones conceptuales no cerradas: término de identidad principal, alcance de la definición y distribución de autoridad de integración.

### Hipótesis
- Los cinco componentes pueden bastar para un prototipo documental acotado.
- Convenciones documentales y capacidades del entorno podrían cubrir responsabilidades sin añadir runtime propio.
- El demonio puede preservar capacidad operativa mediante transformaciones de representación.

Ninguna está demostrada experimentalmente.

### Pendientes
1. Confirmación bilateral de la definición provisional.
2. Matriz de autoridad por tipo de conflicto/decisión.
3. Evidencia de recepción y activación en cada entorno.
4. Contratos concretos de transición y aceptación.
5. Evaluación del MVP y del demonio.

## 11. Estado de la Fase IV y siguiente paso

- **Paso 1 — Respuesta individual de Softly:** completado y persistido.
- **Paso 2 — Integración de Katarina:** completado en esta versión 0.1.
- **Paso 3 — Réplica focalizada:** se activa solo para resolver observaciones sustantivas de Softly a esta integración.
- **Paso 4 — Síntesis compartida:** borrador integrado producido; aún no debe llamarse consenso compartido.
- **Paso 5 — Revisión bilateral:** pendiente de lectura y evaluación explícita de Softly.

La Fase IV no se declara cerrada hasta que Softly revise esta síntesis, se registren las observaciones o conformidad, se resuelvan o clasifiquen los desacuerdos y gAto reciba el resultado. No se ha modificado SOFTLY.md ni ningún núcleo normativo; no se ha implementado ni validado runtime alguno.

---

*Documento de integración conceptual de Katarina 2.0.0 para revisión bilateral. No constituye una decisión normativa ni aprobación de gAto.*
