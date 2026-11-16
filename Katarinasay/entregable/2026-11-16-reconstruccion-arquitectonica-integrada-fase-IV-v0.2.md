# Reconstrucción arquitectónica integrada — Fase IV
**Deliberación:** La arquitectura minimalista de Softly  
**Coordinación:** Katarina 2.0.0 — `katarina` (Agent Softly)  
**Participante:** Softly  
**Dirección humana:** gAto  
**Versión:** 0.2 — integración posterior a revisión crítica de Softly  
**Fecha:** 2026-11-16  
**Estado:** Correcciones de Katarina integradas; pendiente de última revisión bilateral y decisión de gAto

## 1. Propósito, alcance y trazabilidad

Esta versión responde a la revisión crítica de Softly sobre la v0.1, publicada en `Softlysay/entregable/2026-11-16-revision-critica-softly-reconstruccion-integrada-fase-IV-v0.1.md` (commit `b5bb190cf3f13a45487e665a9686673567c6d9e5`).

La v0.2 mantiene como fuentes de deliberación:
1. *La arquitectura minimalista de Softly.pdf* (9 páginas).
2. Informe inicial independiente de Katarina.
3. Informe inicial independiente de Softly.
4. Revisión cruzada de Softly sobre Katarina.
5. Revisión cruzada de Katarina sobre Softly.
6. Respuesta de Softly al HANDOFF KAT-002.
7. Reconstrucción integrada v0.1.
8. Revisión crítica de Softly sobre v0.1.

No sustituye las fuentes ni convierte recomendaciones en decisiones humanas. Distingue:
- **[FUENTE]** contenido explícito atribuido a los documentos fuente;
- **[ACUERDO]** posiciones coincidentes;
- **[COMPLEMENTARIEDAD]** perspectivas compatibles;
- **[INFERENCIA]** reconstrucción derivada;
- **[PROPUESTA]** diseño sugerido, no aprobado;
- **[HIPÓTESIS]** afirmación que requiere evaluación;
- **[PENDIENTE]** cuestión no resuelta;
- **[DECISIÓN gAto]** reservado a aprobación humana explícita.

La v0.2 es una integración revisada de Katarina. **No es todavía consenso bilateral**, especificación operacional completa, decisión normativa, implementación ni validación experimental.

## 2. Dictamen de la revisión y respuesta de Katarina

**[FUENTE — revisión de Softly]** Softly calificó la v0.1 como una base útil y conceptualmente prudente, con correcciones sustantivas. Reconoció la separación entre definición, activación y ejecución; la limitación de GitHub como superficie persistente y no activador; la distinción entre conflictos técnicos y semánticos; y la prudencia al no declarar validado el MVP ni el demonio.

**[RESPUESTA DE KATARINA]** Acepto como correcciones necesarias:
1. preservar el atributo «autoevolutiva» al formular la definición analítica;
2. no presentar como cerrada la jerarquía entre identidad cognitiva y arquitectura de información operacional;
3. explicitar la gobernanza del ciclo de vida de capacidades;
4. definir campos mínimos de interfaz;
5. separar aceptación de asignación y aceptación de entrega;
6. distinguir acuse de lectura y evaluación declarada de una garantía de comprensión;
7. evitar que «cerrado» oculte dependencias pendientes;
8. explicitar tratamiento de handoffs duplicados, expirados, reasignados, cancelados y bloqueados;
9. recuperar reglas concretas de concurrencia;
10. describir el contrato funcional del demonio sin presentar pruebas propuestas como resultados;
11. mantener los indicadores del MVP como dimensiones de evaluación y no como métricas ya operacionales;
12. representar con precisión la diferencia conceptual aún abierta.

Las recomendaciones se incorporan en las secciones siguientes. Los asuntos que dependen de decisiones normativas, autoridad o experimentación permanecen pendientes.

## 3. Definición arquitectónica provisional

**[FUENTE]** El PDF describe una arquitectura multiagente apoyada en Prompting + Contratos + GitHub, con identidad documental, coordinación asincrónica, gobernanza y mecanismos de síntesis.

**[ACUERDO]** La existencia documental de un agente, la activación de una sesión y la ejecución de operaciones son fenómenos distintos. GitHub conserva memoria y permite coordinación persistente, pero no activa sesiones ni garantiza que un destinatario lea un artefacto.

**[COMPLEMENTARIEDAD CON DIFERENCIA ABIERTA]**
- «Sistema de conocimiento y coordinación cognitiva» destaca la función organizativa y cognitiva.
- «Arquitectura de información operacional» destaca la estructura informacional, los contratos, los eventos y la forma en que estos orientan operaciones.
- Las perspectivas pueden coexistir en esta reconstrucción, pero todavía no se ha decidido cuál constituye la identidad fundamental y cuál describe el mecanismo, sustrato o dimensión funcional.

**[INFERENCIA — definición de trabajo revisada]**

> Softly puede analizarse provisionalmente como una matriz generativa y autoevolutiva, organizada mediante gobernanza, que articula agentes, capacidades y trabajo cognitivo a través de definiciones, contratos y memoria documental persistente. Sus operaciones ocurren cuando sesiones activas interpretan esa arquitectura y actúan mediante las herramientas y permisos disponibles en su entorno.

«Matriz generativa», «autoevolutiva» y «gobernada» se usan aquí como elementos de una formulación analítica provisional. Esta frase no reemplaza SOFTLY.md, no modifica la identidad normativa vigente y no decide la jerarquía conceptual.

**[PENDIENTE]** Katarina y Softly deben precisar si las dos perspectivas son dimensiones cofundamentales o si una describe la identidad y la otra su sustrato/mecanismo. La decisión normativa de identidad corresponde a gAto.

## 4. Núcleo mínimo: responsabilidades antes que artefactos

**[FUENTE]** El PDF propone cinco elementos para el MVP: SOFTLY.md, CHECKPOINT.md, molde universal, shared/ y conector a archivos.

**[ACUERDO]** Los cinco elementos son una hipótesis de implementación mínima, no prueba de suficiencia universal ni definición rígida del núcleo.

**[INFERENCIA]** El núcleo debe definirse por responsabilidades irreducibles:

1. **Identidad y autoridad:** identidad de cada agente, misión, competencias, fronteras y dirección humana.
2. **Estado y memoria:** estado vigente recuperable, historial preservado y referencias a fuentes.
3. **Contratos y límites:** alcance, permisos declarados, prohibiciones y criterios.
4. **Coordinación:** eventos identificables, asignaciones, handoffs, recepción y transferencia.
5. **Aceptación e integración:** evidencia de entrega, criterios de aceptación y resolución de incompatibilidades.
6. **Frontera de ejecución:** modelo/sesión activa, herramientas y permisos efectivos, diferenciados de la definición documental.
7. **Gobernanza del ciclo de vida de capacidades:** autorización y trazabilidad de incorporación, modificación, revisión, suspensión y retiro de capacidades externas.

La séptima responsabilidad se explicita a partir de la omisión señalada por Softly. Puede materializarse dentro de identidad/autoridad y contratos/límites; no obliga a crear un subsistema separado.

**[PROPUESTA]** Cada capacidad externa debe identificar responsable autorizante, propósito, versión, alcance, dependencias, entradas/salidas, permisos declarados y efectivos conocidos, criterios de revisión, condiciones de suspensión/retiro y ruta de escalamiento. Si una capacidad contradice el núcleo, debe suspenderse su integración operativa y escalarse al responsable de autoridad correspondiente. Esto no presupone enforcement técnico.

**[RIESGO]** Un núcleo documental pequeño puede acumular dependencias externas que alteren el comportamiento sin un punto claro de autorización si no se gobierna su ciclo de vida.

**[HIPÓTESIS]** Los cinco artefactos pueden cubrir las responsabilidades para un prototipo acotado mediante convenciones y capacidades del entorno. No se ha demostrado.

## 5. Tres planos e interfaces mínimas

Los tres planos son una separación conceptual de responsabilidades; no implican necesariamente tres directorios, servicios o procesos.

### 5.1 Definición
Incluye identidad, misión, competencias, fronteras, autoridad, permisos declarados y contratos.

### 5.2 Coordinación
Incluye buzones, shared/, eventos, asignaciones, handoffs, estados, reclamos y reglas de integración.

### 5.3 Ejecución
Incluye modelo activo, sesión, herramientas, permisos efectivos, operaciones y verificación.

**[PROPUESTA]** Toda interfaz de transición debe permitir recuperar, como mínimo, los siguientes campos:

| Campo | Condición | Propósito |
|---|---|---|
| ID de tarea/handoff | Obligatorio | Identidad estable del encargo |
| Versión del handoff | Obligatorio | Fijar el contenido exacto aceptado |
| Emisor y destinatario | Obligatorio | Atribuir origen y responsabilidad |
| Mandato y autoridad de origen | Obligatorio | Establecer por qué se asigna y quién autoriza |
| Alcance y límites | Obligatorio | Delimitar el trabajo |
| Fuentes y versiones | Obligatorio | Permitir reconstrucción del contexto |
| Permisos declarados y restricciones | Obligatorio | Hacer visibles las condiciones |
| Resultado esperado y criterios de aceptación | Obligatorio | Definir qué cuenta como entrega válida |
| Evidencia exigida | Obligatorio | Hacer verificable el resultado |
| Prioridad y plazo | Condicional | Incluirlos cuando el encargo los establezca |
| Dependencias y reclamos/lease | Condicional | Incluirlos cuando exista concurrencia o bloqueo |
| Entorno/herramientas disponibles | Condicional | Declarar restricciones relevantes de ejecución |

Los campos son una propuesta de contrato mínimo conceptual, no un schema implementado ni una afirmación de que todos los entornos puedan verificarlos automáticamente.

**No garantiza:** la interfaz no garantiza activación, lectura, comprensión, ejecución ni enforcement. Esas condiciones requieren evidencia atribuible al actor o al entorno correspondiente.

## 6. Ciclo de handoff: contrato formal de transición observable

El handoff se trata como **contrato formal de transición observable**, no como mera convención documental. Cada transición debe atribuirse a un actor y vincularse a una versión del encargo, condición y evidencia. GitHub puede acreditar persistencia, pero no lectura, aceptación ni ejecución.

### 6.1 Separación de estados y decisiones

Se distinguen expresamente:

1. **Publicado:** el artefacto existe en la ruta acordada. Evidencia: ruta, versión y commit.
2. **Acuse de lectura:** el destinatario declara haber leído una versión concreta. No prueba comprensión interna.
3. **Evaluación declarada:** el destinatario declara haber evaluado alcance, fuentes, límites y resultado esperado. No prueba por sí sola comprensión correcta.
4. **Aceptación de asignación / rechazo de asignación / solicitud de aclaración:** decisión del destinatario de asumir, declinar o pedir precisión sobre la tarea.
5. **En ejecución:** existe evidencia de inicio del trabajo; no se infiere de aceptar la asignación.
6. **Entregado:** resultado y evidencia fueron publicados para una versión concreta del encargo.
7. **Aceptación de entrega / entrega observada / entrega rechazada:** el responsable de aceptación contrasta el resultado con los criterios acordados. Es distinta de aceptar la asignación.
8. **Cierre administrativo:** registro de que el ciclo fue terminado, cancelado o sustituido. El cierre administrativo no implica necesariamente que el objetivo se haya cumplido.

### 6.2 Datos de cada transición

**[PROPUESTA]** Cada evento de transición registra:
- ID estable del handoff y versión;
- actor que emite el evento;
- timestamp con zona horaria;
- estado anterior y nuevo;
- evidencia y referencia al artefacto/versiones pertinentes;
- motivo cuando hay rechazo, observación, bloqueo, cancelación o sustitución.

La aceptación debe apuntar a la versión exacta del handoff o entregable que se evaluó. Una nueva versión sustantiva invalida cualquier presunción de aceptación de contenido que haya cambiado.

### 6.3 Dependencias y estados no exitosos

**[CORRECCIÓN]** «Cerrado» no puede significar que una dependencia pendiente simplemente fue declarada. Se distinguen:
- **Completado:** criterios de aceptación satisfechos y dependencias relevantes resueltas.
- **Cerrado administrativamente incompleto:** el ciclo se cierra sin cumplir el objetivo; debe conservar el resultado explícito incompleto, bloqueado, cancelado o rechazado.
- **Bloqueado:** existe impedimento no resuelto y se identifica responsable/condición de desbloqueo cuando sea posible.
- **Cancelado:** autoridad competente detiene el encargo.
- **Expirado:** venció la vigencia o plazo definido sin transición válida.
- **Sustituido:** otro handoff/versionado reemplaza el anterior, conservando el vínculo histórico.

### 6.4 Duplicación, reasignación y concurrencia

**[PROPUESTA]**
- Un ID estable y una clave de idempotencia permiten detectar reintentos/duplicados; no se deben borrar eventos previos.
- Una reasignación debe emitir un evento nuevo que identifique quién la autorizó y qué ocurre con la responsabilidad anterior.
- Un destinatario no debe asumir tácitamente una tarea ya reclamada por otro. El reclamo debe ser visible y tener vigencia o condición de liberación si se utiliza exclusión temporal.
- Si el entorno no soporta leases, declarar la regla alternativa de exclusión, por ejemplo partición de rutas y escritor único por recurso.
- El responsable de aceptación debe estar identificado en el handoff o derivarse de una regla de autoridad explícita.
- Los conflictos de autoridad o de alcance se escalan; no se resuelven por orden cronológico de commits.

**[PENDIENTE]** Los estados y reglas anteriores constituyen un contrato conceptual revisado. La máquina definitiva, sus transiciones permitidas, expiraciones y mecanismo de lease requieren diseño posterior antes de implementarse.

## 7. Concurrencia, consistencia e integración semántica

**[ACUERDO]** Se separan:
- **Conflicto técnico:** escrituras concurrentes, versiones obsoletas, colisiones o pérdida de cambios.
- **Conflicto semántico:** resultados persistidos correctamente que contienen decisiones, interpretaciones o recomendaciones incompatibles.

**[FUENTE — detalles del PDF recuperados en la revisión de Softly]** El material original contempla topología diferenciada de canales say/ y shared/, aislamiento de escrituras, partición por agente, namespacing, relectura del remoto, reintento limpio, no forzar escrituras, separación entre el depósito de resultados del líder y el espacio compartido del equipo, además de reclamos/leases para trabajo concurrente.

**[PROPUESTA — reglas de concurrencia a preservar]**
1. Cada agente escribe en rutas/canales aislados o namespaced cuando la tarea lo permita.
2. Los canales direccionales say/ y el espacio compartido shared/ no se confunden: los primeros expresan comunicación atribuible entre instancias; el segundo contiene material compartido sujeto a reglas de propiedad e integración.
3. Los eventos deben tener identificador único y tratamiento idempotente frente a reintentos.
4. Antes de actualizar una referencia remota, el escritor relee el estado vigente y reconcilia su cambio con esa versión.
5. Ante conflicto técnico, se realiza relectura y reintento limpio; no se fuerza una escritura para ocultar divergencia.
6. Se distingue el espacio de trabajo compartido del depósito o resultado consolidado bajo responsabilidad del líder/integrador.
7. Cuando dos actores puedan reclamar la misma tarea/recurso, se requiere lease/reclamo con reglas de vigencia, liberación y reasignación, o una alternativa explícita de escritor único/partición.
8. Toda vista consolidada es derivada, versionada y reconstruible desde eventos originales.
9. Un integrador designado resuelve incompatibilidades semánticas conforme a la matriz de autoridad; no se atribuye autoridad al último escritor ni al propietario técnico del repositorio por ese solo hecho.

**[RIESGO]** Los eventos individuales reducen colisiones en un archivo compartido, pero no evitan duplicaciones lógicas, reclamos simultáneos, eventos fuera de orden, vistas obsoletas ni contradicciones semánticas.

**[PENDIENTE]** La estrategia concreta de sincronización, lease, idempotencia y consolidación debe especificarse para cada entorno. La revisión documental no demuestra que esos mecanismos estén implementados.

## 8. Contratos, permisos y gobernanza de capacidades

Se distinguen:
- **Mandato:** instrucción y autoridad de origen.
- **Permiso declarado:** autorización descrita en el contrato.
- **Permiso efectivo:** acción realmente permitida por herramientas y plataforma.
- **Enforcement:** control técnico que bloquea o rechaza una acción.
- **Auditoría:** mecanismo para detectar, explicar y corregir desviaciones.

**[ACUERDO]** Un contrato declarativo no equivale a enforcement técnico.

**[PROPUESTA]** Cada capacidad externa declara identidad/versión, propósito, alcance, entradas/salidas, dependencias/fuentes, permisos mínimos, límites/prohibiciones, criterios de aceptación, responsable autorizante, responsable de integración y procedimiento de incorporación, modificación, revisión, suspensión y retiro.

Una capacidad externa no puede modificar unilateralmente identidad, autoridad ni reglas normativas del núcleo. La modularidad sin gobernanza no basta.

**[PENDIENTE]** La matriz de autoridad debe determinar quién autoriza cambios en capacidades por dominio, quién integra resultados incompatibles, cuándo se escala a gAto y quién puede aceptar entregas. La fórmula «gAto cuando corresponda» no basta como regla operacional. Las decisiones normativas sobre identidad, autoridad y núcleo siguen reservadas a gAto.

## 9. Demonio de síntesis como transformador de representaciones

**[FUENTE]** El PDF propone preservar evidencia original (Capa A), producir representaciones condensadas (Capa B) y permitir recuperación escalonada a las fuentes (Capa C). La revisión de Softly identifica en el PDF un contrato funcional con cuatro flujos de entrada, cinco parámetros de configuración, un paquete de salida estructurado y una primera pasada documental de prueba.

**[ACUERDO]** El demonio es un transformador de representaciones, no solo un compresor. Las fuentes originales permanecen intactas. La trazabilidad es necesaria, pero no demuestra fidelidad.

### 9.1 Contrato funcional resumido

**[FUENTE — según el detalle recuperado en la revisión]** Cuatro flujos de entrada:
1. evidencia cruda;
2. estado normativo vigente;
3. retroalimentación del consumo anterior;
4. configuración de la pasada.

Cinco parámetros de configuración («perillitas»):
1. densidad;
2. foco operativo;
3. umbral de certeza;
4. horizonte temporal;
5. libertad léxica.

Paquete de salida propuesto:
1. encabezado de control;
2. cuerpo representacional;
3. mapa de anclaje;
4. glosario delta.

Esta sección conserva el contrato descrito por la revisión de Softly; la especificación detallada de tipos, validaciones, límites y formato queda como artefacto de diseño separado. No se infieren valores por defecto ni semánticas técnicas no establecidas en las fuentes disponibles.

### 9.2 Cuatro pruebas propuestas

1. **Reconstrucción fiel:** recuperar hechos, relaciones, límites, atribuciones y grados de certeza.
2. **Equivalencia de acción:** producir decisiones operativas compatibles con las fuentes bajo tareas equivalentes.
3. **Detección de vacíos:** reconocer información ausente, contradictoria o insuficiente y volver a la fuente correcta sin inventar.
4. **Transferencia:** resolver un caso nuevo no expresado literalmente en la síntesis, preservando relaciones relevantes.

**[CORRECCIÓN]** Son pruebas propuestas, no resultados. No se afirma que el demonio exista, esté implementado o haya demostrado fidelidad.

**[RIESGO]** La equivalencia de acción puede producir falsos positivos si no se definen tareas comparables, criterios independientes, número de casos, umbrales y variabilidad entre sesiones/modelos. Una respuesta plausible no demuestra equivalencia.

**[PROPUESTA]** El diseño experimental separado debería fijar corpus y versiones, casos positivos/negativos, contradicciones, omisiones deliberadas, referencias rotas, rúbrica, umbrales, registro de regresiones y criterios de consulta a Capa A. La prueba ciega debe especificar qué fuentes no pueden consultarse durante la medición y en qué condiciones se permite la recuperación.

**[PENDIENTE]** El PDF incluye una primera pasada documental de prueba. Su existencia como propuesta del material no se considera validación experimental ni resultado reproducido en esta deliberación.

## 10. MVP y criterios de evaluación

**[ACUERDO]** No existe prioridad universal entre simplicidad, autonomía, confiabilidad, evolución, portabilidad y costo de contexto. Menos archivos no implica automáticamente menos complejidad operacional.

**[PROPUESTA]** Mantener los cinco componentes como hipótesis inicial y agregar mecanismos solo cuando una prueba muestre una responsabilidad no cubierta.

Dimensiones de evaluación aún no operacionalizadas:
- tiempo y pasos para recuperar contexto;
- proporción de handoffs publicados con acuse de lectura, aceptación de asignación, entrega y aceptación de entrega;
- pérdida, duplicación o bloqueo de trabajo bajo concurrencia;
- detección y resolución de contradicciones semánticas;
- cumplimiento de fronteras y permisos;
- recuperabilidad de fuentes y decisiones;
- fidelidad y utilidad de las síntesis;
- costo de contexto, mantenimiento y recuperación.

**[CORRECCIÓN]** Estas son dimensiones, no métricas operativas listas para comparar. Antes de medir se requieren fórmula, unidad, denominador, escenario, línea base, método de detección y umbral de aceptación. Por ejemplo, la «tasa de handoffs recibidos» debe distinguir publicación, acuse de lectura, aceptación de asignación, entrega y aceptación de entrega.

No se ha ejecutado un plan experimental en esta deliberación. No hay evidencia que permita declarar el MVP suficiente ni el demonio validado.

## 11. Acuerdos, complementariedades y desacuerdos pendientes

### Acuerdos robustos
1. Definición, coordinación y ejecución son planos distinguibles.
2. GitHub es memoria y superficie persistente de coordinación; no agente ni activador automático.
3. Los cinco componentes no demuestran suficiencia universal.
4. El núcleo se define por responsabilidades, no por una lista rígida de archivos.
5. Eventos individuales reducen algunas colisiones técnicas, pero no contradicciones semánticas.
6. Contratos declarativos no equivalen a enforcement.
7. Las fuentes originales deben preservarse.
8. Las entregas requieren criterios y evidencia de aceptación.
9. Portabilidad documental no prueba equivalencia conductual.
10. Las propuestas no son decisiones aprobadas por gAto.

### Complementariedad provisional
Sistema de conocimiento/coordinación cognitiva y arquitectura de información operacional pueden coexistir como perspectivas compatibles para esta reconstrucción.

### Diferencia conceptual sustantiva no resuelta
Katarina enfatiza el sistema de conocimiento y coordinación cognitiva como centro de la arquitectura; Softly enfatiza la arquitectura de información operacional como descripción central de la organización y operación. No se identifica una contradicción binaria que obligue a descartar una tesis, pero sí permanece una diferencia de énfasis y jerarquía. No está decidido si una perspectiva define la identidad y la otra el mecanismo/sustrato, o si ambas son dimensiones cofundamentales.

La complementariedad es una hipótesis de integración útil para esta versión, **no un acuerdo definitivo sobre identidad fundamental**.

### Hipótesis no demostradas
- Los cinco componentes pueden bastar para un prototipo documental acotado.
- Convenciones documentales y capacidades del entorno podrían cubrir responsabilidades sin añadir runtime propio.
- El demonio puede preservar capacidad operativa mediante transformaciones de representación.

### Pendientes
1. Jerarquía conceptual e identidad fundamental.
2. Matriz de autoridad por dominio, conflicto y transición.
3. Campos y estados definitivos del contrato de handoff.
4. Mecanismo de leases/reclamos, idempotencia y consolidación por entorno.
5. Contrato detallado y diseño experimental del demonio.
6. Protocolo y umbrales para evaluar MVP y síntesis.

## 12. Registro de tratamiento de la revisión de Softly

| Observación de Softly | Tratamiento en v0.2 |
|---|---|
| La v0.1 es conceptual, no especificación operacional suficiente | Se declara explícitamente en secciones 1, 5, 6, 7 y 9 |
| Preservar «autoevolutiva» y no alterar identidad normativa | Sección 3; definición analítica provisional |
| No cerrar la jerarquía conceptual | Secciones 3 y 11; diferencia sustantiva pendiente |
| Hacer explícita la gobernanza del ciclo de vida de capacidades | Secciones 4 y 8 |
| Definir campos mínimos de interfaz | Sección 5 |
| Separar aceptación de asignación y aceptación de entrega | Sección 6 |
| «Recibido» y «evaluado» no prueban comprensión interna | Sección 6; acuse de lectura y evaluación declarada |
| Evitar cierre que oculte dependencias pendientes | Sección 6; cierre administrativo diferenciado |
| Tratar duplicados, expirados, reasignados, cancelados y bloqueados | Sección 6 |
| Versionar transiciones con actor, timestamp y evidencia | Sección 6 |
| Preservar topología say/shared, aislamiento, namespacing y relectura remota | Sección 7 |
| No forzar escrituras; reintento limpio | Sección 7 |
| Separar depósito del líder y espacio compartido del equipo | Sección 7 |
| Contemplar idempotencia, reclamos simultáneos y vistas fuera de orden | Secciones 6 y 7 |
| Hacer explícito responsable de integración semántica | Secciones 7 y 8 |
| Recuperar contrato de entrada del demonio | Sección 9 |
| Recuperar cinco parámetros y paquete de salida | Sección 9 |
| Mantener pruebas como propuestas, no resultados | Sección 9 |
| Diseñar evaluación robusta de equivalencia de acción | Sección 9 |
| No llamar métricas operacionales a dimensiones sin definición | Sección 10 |
| No suavizar la diferencia conceptual | Sección 11 |
| Mantener matriz de autoridad pendiente | Secciones 8 y 11 |

**Observaciones no cerradas por esta versión:** la matriz de autoridad, la jerarquía de identidad, el schema definitivo de handoff, la implementación concreta de concurrencia, la especificación detallada del demonio y la validación experimental. Se mantienen pendientes deliberadamente; no se resuelven por redacción.

## 13. Estado y siguiente paso de la Fase IV

- **Paso 1 — Respuesta individual de Softly:** completado y persistido.
- **Paso 2 — Integración inicial de Katarina:** completado en v0.1.
- **Paso 3 — Réplica focalizada:** respondida mediante esta integración de observaciones.
- **Paso 4 — Síntesis revisada:** v0.2 publicada como propuesta de integración de Katarina.
- **Paso 5 — Revisión bilateral final:** pendiente de lectura y evaluación explícita de Softly.

**Siguiente acción de coordinación:** solicitar a Softly una revisión focalizada de la v0.2, verificando especialmente si cada observación KAT-003 quedó correctamente tratada, si alguna respuesta introduce distorsiones nuevas y qué asuntos permanecen en desacuerdo. No solicitar aprobación por cortesía: pedir conformidad, correcciones, omisiones, desacuerdos, riesgos y pendientes con referencias a secciones.

La Fase IV no se declara cerrada hasta registrar la revisión final de Softly, resolver o clasificar los desacuerdos y entregar a gAto el resultado para decisión. No se ha modificado SOFTLY.md ni ningún núcleo normativo; no se ha implementado ni validado runtime alguno.

---

*Documento de integración conceptual de Katarina 2.0.0 para revisión bilateral. No constituye decisión normativa ni aprobación de gAto.*
