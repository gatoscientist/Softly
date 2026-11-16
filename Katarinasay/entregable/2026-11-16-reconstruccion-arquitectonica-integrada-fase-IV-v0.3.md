# Reconstrucción arquitectónica integrada — Fase IV
**Deliberación:** La arquitectura minimalista de Softly  
**Coordinación:** Katarina 2.0.0 — `katarina` (Agent Softly)  
**Participante:** Softly  
**Dirección humana:** gAto  
**Versión:** 0.3 — integración final tras revisión bilateral  
**Fecha:** 2026-11-16  
**Estado:** Integración documental corregida; Fase IV completada en el plano deliberativo; decisiones normativas y experimentales reservadas a gAto

## 1. Propósito, alcance y fuentes

Esta versión consolida la reconstrucción v0.2 y responde a la revisión final de Softly sobre KAT-004, publicada en:

`Softlysay/entregable/2026-11-16-revision-final-softly-reconstruccion-integrada-fase-IV-v0.2.md`

Commit de la revisión: `d9b53a366fde5a6e65434240600f57bfdc7cca33`.

La revisión final de Softly concluye que la v0.2 es **conforme en lo sustantivo**, con tres correcciones de precisión. También identifica dos asuntos menores que deben permanecer como pendientes de diseño: separar estado del proceso y resultado de tarea, y definir el ciclo de retrabajo.

Fuentes de la deliberación:
1. *La arquitectura minimalista de Softly.pdf* (9 páginas).
2. Informe inicial independiente de Katarina.
3. Informe inicial independiente de Softly.
4. Revisión cruzada de Softly sobre Katarina.
5. Revisión cruzada de Katarina sobre Softly.
6. Respuesta de Softly al HANDOFF KAT-002.
7. Reconstrucción integrada v0.1.
8. Revisión crítica de Softly KAT-003.
9. Reconstrucción integrada v0.2.
10. Revisión final de Softly KAT-004.
11. SOFTLY.md vigente y `schemas/handoff.schema.json` vigente.

Este documento es una síntesis conceptual de la deliberación. No modifica SOFTLY.md ni schemas, no implementa runtime, no valida experimentalmente el MVP ni el demonio y no resuelve decisiones reservadas a gAto.

Se mantienen las etiquetas:
- **[FUENTE]** contenido explícito atribuido a documentos.
- **[ACUERDO]** posiciones coincidentes.
- **[COMPLEMENTARIEDAD]** perspectivas compatibles sin jerarquía resuelta.
- **[INFERENCIA]** reconstrucción derivada.
- **[PROPUESTA]** diseño sugerido, no aprobado.
- **[HIPÓTESIS]** afirmación que requiere evaluación.
- **[PENDIENTE]** cuestión no resuelta.
- **[DECISIÓN gAto]** reservado a aprobación humana explícita.

## 2. Definición arquitectónica provisional y precisión de identidad

**[FUENTE — SOFTLY.md, sección 1]** La formulación normativa vigente dice literalmente que Softly es **«una matriz generativa y un sistema autoevolutivo»**. Esta formulación se conserva sin alteración.

**[FUENTE]** El PDF describe una arquitectura multiagente apoyada en Prompting + Contratos + GitHub, con identidad documental, coordinación asincrónica, gobernanza y mecanismos de síntesis.

**[ACUERDO]** La existencia documental de un agente, la activación de una sesión y la ejecución de operaciones son fenómenos distintos. GitHub conserva memoria y permite coordinación persistente, pero no activa sesiones ni garantiza que un destinatario lea un artefacto.

**[COMPLEMENTARIEDAD CON DIFERENCIA ABIERTA]**
- «Sistema de conocimiento y coordinación cognitiva» destaca la función organizativa y cognitiva.
- «Arquitectura de información operacional» destaca la estructura informacional, los contratos, los eventos y la forma en que estos orientan operaciones cuando una sesión activa los interpreta y dispone de herramientas.
- Ambas perspectivas pueden coexistir para esta reconstrucción, pero no se ha decidido cuál constituye la identidad fundamental y cuál describe el mecanismo, sustrato o dimensión funcional.

**[INFERENCIA — definición analítica de trabajo]**

> Softly puede describirse, respetando su identidad normativa, como una matriz generativa y un sistema autoevolutivo que organiza agentes, capacidades y trabajo cognitivo mediante gobernanza, definiciones, contratos y memoria documental persistente. Sus operaciones ocurren cuando sesiones activas interpretan esa arquitectura y actúan mediante las herramientas y permisos disponibles en su entorno.

Esta formulación es analítica y provisional. No reemplaza SOFTLY.md ni constituye un cambio de identidad normativa.

**[PENDIENTE]** Katarina y Softly aceptan mantener ambas perspectivas en el análisis, pero la jerarquía identitaria entre ellas permanece abierta. Su resolución normativa corresponde a gAto.

## 3. Núcleo mínimo: responsabilidades antes que artefactos

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

La séptima responsabilidad puede materializarse dentro de identidad/autoridad y contratos/límites; no obliga a crear un subsistema separado.

**[PROPUESTA]** Cada capacidad externa debe identificar responsable autorizante, propósito, versión, alcance, dependencias, entradas/salidas, permisos declarados y efectivos conocidos, criterios de revisión, condiciones de suspensión/retiro y ruta de escalamiento. Si contradice el núcleo, su integración operativa debe detenerse y escalarse al responsable de autoridad correspondiente. Esto no presupone enforcement técnico.

**[HIPÓTESIS]** Los cinco artefactos pueden cubrir estas responsabilidades para un prototipo acotado mediante convenciones y capacidades del entorno. No se ha demostrado.

## 4. Tres planos e interfaces mínimas

Los tres planos son una separación conceptual de responsabilidades; no implican necesariamente tres directorios, servicios o procesos.

### 4.1 Definición
Incluye identidad, misión, competencias, fronteras, autoridad, permisos declarados y contratos.

### 4.2 Coordinación
Incluye buzones, shared/, eventos, asignaciones, handoffs, estados, reclamos y reglas de integración.

### 4.3 Ejecución
Incluye modelo activo, sesión, herramientas, permisos efectivos, operaciones y verificación.

**[PROPUESTA]** Toda interfaz de transición debe permitir recuperar, como mínimo:

| Campo | Condición | Propósito |
|---|---|---|
| ID de tarea/handoff | Obligatorio | Identidad estable del encargo |
| Versión del handoff | Obligatorio | Fijar el contenido exacto evaluado |
| Emisor y destinatario | Obligatorio | Atribuir origen y responsabilidad |
| Mandato y autoridad de origen | Obligatorio | Establecer por qué se asigna y quién autoriza |
| Alcance y límites | Obligatorio | Delimitar el trabajo |
| Fuentes y versiones | Obligatorio | Reconstruir el contexto |
| Permisos declarados y restricciones | Obligatorio | Hacer visibles las condiciones |
| Resultado esperado y criterios de aceptación | Obligatorio | Definir la entrega válida |
| Evidencia exigida | Obligatorio | Hacer verificable el resultado |
| Prioridad y plazo | Condicional | Cuando el encargo los establezca |
| Dependencias y reclamos/lease | Condicional | Cuando exista concurrencia o bloqueo |
| Entorno/herramientas disponibles | Condicional | Cuando restrinjan la ejecución |

### 4.4 Relación con el schema existente

**[HECHO VERIFICADO — `schemas/handoff.schema.json`]** El repositorio ya contiene un schema declarativo de handoff. Define como obligatorios `handoff_id`, `event_id`, `status`, `from`, `to`, `assignment_id`, `task`, `result`, `evidence`, `next`, `acceptance` y `created_at`. Su enum actual de `status` es `ready`, `accepted`, `rejected`, `blocked` y `closed`. También permite `lease.claim_id` y `lease.expires_at`.

**[PROPUESTA]** La tabla de campos y el ciclo ampliado de esta reconstrucción amplían conceptualmente el contrato descrito en el schema declarativo existente; **no constituyen una actualización del schema ni una implementación de enforcement**.

**[LÍMITE DE EVIDENCIA]** La existencia del schema y de campos de lease no demuestra que un runtime lo valide, gestione exclusión mutua, renueve/libere leases o aplique transiciones automáticamente. El enum actual del schema tampoco debe confundirse con los estados conceptuales ampliados de esta síntesis.

## 5. Ciclo de handoff: contrato formal de transición observable

El handoff se trata como contrato formal de transición observable, no como mera convención documental. Cada transición debe atribuirse a un actor y vincularse a una versión del encargo, condición y evidencia. GitHub puede acreditar persistencia, pero no lectura, aceptación ni ejecución.

### 5.1 Dos dimensiones relacionadas

**[CORRECCIÓN]** Se distinguen formalmente:

1. **Estado del proceso/handoff:** situación del flujo de asignación, ejecución, entrega, bloqueo, expiración, cancelación, sustitución o cierre administrativo.
2. **Resultado de la tarea/entrega:** resultado de la evaluación del trabajo, por ejemplo aceptado/completado, observado, rechazado o incompleto.

No deben mezclarse como si fueran valores intercambiables de una sola máquina de estados.

### 5.2 Transiciones y declaraciones observables

1. **Publicado:** el artefacto existe en la ruta acordada. Evidencia: ruta, versión y commit.
2. **Acuse de lectura:** el destinatario declara haber leído una versión concreta. No prueba comprensión interna.
3. **Evaluación declarada:** el destinatario declara haber evaluado alcance, fuentes, límites y resultado esperado. No prueba por sí sola comprensión correcta.
4. **Aceptación de asignación / rechazo de asignación / solicitud de aclaración:** decisión del destinatario de asumir, declinar o pedir precisión.
5. **En ejecución:** existe evidencia de inicio; no se infiere de aceptar la asignación.
6. **Entregado:** resultado y evidencia publicados para una versión concreta del encargo.
7. **Aceptación de entrega / entrega observada / entrega rechazada:** el responsable contrasta el resultado con los criterios acordados. Es distinta de aceptar la asignación.
8. **Cierre administrativo:** registro de que el ciclo fue terminado, cancelado o sustituido. No implica necesariamente que el objetivo se haya cumplido.

### 5.3 Datos de cada transición

**[PROPUESTA]** Cada evento registra ID estable y versión del handoff, actor, timestamp con zona horaria, estado anterior/nuevo, evidencia y referencias a artefactos/versiones. Debe incluir motivo ante rechazo, observación, bloqueo, cancelación o sustitución.

La aceptación apunta a la versión exacta evaluada. Una nueva versión sustantiva no hereda automáticamente la aceptación de contenido que cambió.

### 5.4 Estados y resultados no exitosos

- **Completado:** resultado de tarea cuyos criterios de aceptación se han satisfecho.
- **Cerrado administrativamente incompleto:** el registro se cierra sin cumplir el objetivo; conserva el resultado incompleto, bloqueado, cancelado o rechazado.
- **Bloqueado:** impedimento no resuelto, con responsable/condición de desbloqueo cuando sea posible.
- **Cancelado:** autoridad competente detiene el encargo.
- **Expirado:** venció la vigencia o plazo definido sin transición válida.
- **Sustituido:** otro handoff/versionado reemplaza al anterior, conservando el vínculo histórico.

### 5.5 Duplicación, reasignación y retrabajo

**[PROPUESTA]**
- ID estable y clave de idempotencia permiten detectar reintentos/duplicados; no se borran eventos previos.
- La reasignación emite evento nuevo, identifica quién la autorizó y registra qué ocurre con la responsabilidad anterior.
- No se asume una tarea ya reclamada por otro actor sin resolver el reclamo.
- Si no hay leases, se declara una regla alternativa de exclusión, por ejemplo partición de rutas y escritor único por recurso.
- Responsable de aceptación identificado en el handoff o derivado de una regla de autoridad explícita.
- Conflictos de alcance o autoridad se escalan; no se resuelven por orden cronológico de commits.

**[PENDIENTE — ciclo de retrabajo]** Antes de implementar el contrato se debe definir quién corrige una entrega observada/rechazada, si se reabre la misma asignación o se emite una nueva versión/handoff, cómo se conservan las aceptaciones de versiones anteriores y qué evidencia cierra el retrabajo.

**[PENDIENTE]** La máquina definitiva, transiciones permitidas, expiraciones y semántica de lease requieren diseño posterior. No se afirma que estén implementadas.

## 6. Concurrencia, consistencia e integración semántica

**[ACUERDO]** Se separan:
- **Conflicto técnico:** escrituras concurrentes, versiones obsoletas, colisiones o pérdida de cambios.
- **Conflicto semántico:** resultados persistidos correctamente con decisiones, interpretaciones o recomendaciones incompatibles.

**[FUENTE — PDF, según contraste bilateral]** El material contempla topología diferenciada de canales say/ y shared/, aislamiento de escrituras, partición por agente, namespacing, relectura del remoto, reintento limpio, no forzar escrituras, separación entre depósito de resultados del líder y espacio compartido del equipo, además de reclamos/leases para trabajo concurrente.

**[PROPUESTA — reglas a preservar]**
1. Cada agente escribe en rutas/canales aislados o namespaced cuando la tarea lo permita.
2. Los canales direccionales say/ no se confunden con shared/.
3. Eventos con identificador único y tratamiento idempotente ante reintentos.
4. Antes de actualizar una referencia remota, releer el estado vigente y reconciliar el cambio.
5. Ante conflicto técnico, relectura y reintento limpio; no forzar una escritura para ocultar divergencia.
6. Separar espacio de trabajo compartido del depósito o resultado consolidado bajo responsabilidad del líder/integrador.
7. Si dos actores pueden reclamar la misma tarea/recurso, lease/reclamo con vigencia, liberación y reasignación, o alternativa explícita de escritor único/partición.
8. Vistas consolidadas derivadas, versionadas y reconstruibles desde eventos originales.
9. Integrador designado resuelve incompatibilidades semánticas conforme a matriz de autoridad; no se atribuye autoridad al último escritor ni al propietario técnico del repositorio por ese solo hecho.

**[RIESGO]** Eventos individuales reducen colisiones sobre un archivo común, pero no evitan duplicaciones lógicas, reclamos simultáneos, eventos fuera de orden, vistas obsoletas ni contradicciones semánticas.

**[PENDIENTE]** La estrategia concreta de sincronización, lease, idempotencia y consolidación debe especificarse por entorno. La revisión documental no demuestra que esos mecanismos estén implementados.

## 7. Contratos, permisos y gobernanza de capacidades

Se distinguen:
- **Mandato:** instrucción y autoridad de origen.
- **Permiso declarado:** autorización descrita en el contrato.
- **Permiso efectivo:** acción realmente permitida por herramientas y plataforma.
- **Enforcement:** control técnico que bloquea o rechaza una acción.
- **Auditoría:** mecanismo para detectar, explicar y corregir desviaciones.

**[ACUERDO]** Un contrato declarativo no equivale a enforcement técnico.

**[PROPUESTA]** Cada capacidad externa declara identidad/versión, propósito, alcance, entradas/salidas, dependencias/fuentes, permisos mínimos, límites/prohibiciones, criterios de aceptación, responsable autorizante, responsable de integración y procedimiento de incorporación, modificación, revisión, suspensión y retiro.

Una capacidad externa no puede modificar unilateralmente identidad, autoridad ni reglas normativas del núcleo. La modularidad sin gobernanza no basta.

**[PENDIENTE]** La matriz de autoridad debe determinar quién autoriza cambios en capacidades por dominio, quién integra resultados incompatibles, cuándo se escala a gAto y quién puede aceptar entregas. Las decisiones normativas sobre identidad, autoridad y núcleo siguen reservadas a gAto.

## 8. Demonio de síntesis como transformador de representaciones

**[FUENTE]** El PDF propone preservar evidencia original (Capa A), producir representaciones condensadas (Capa B) y permitir recuperación escalonada a las fuentes (Capa C). El contrato funcional descrito incluye cuatro flujos de entrada, cinco parámetros, paquete de salida estructurado y reglas de anclaje/estatus epistémico.

### 8.1 Entradas

1. Evidencia cruda.
2. Estado normativo vigente.
3. Retroalimentación del consumo anterior.
4. Configuración de la pasada.

### 8.2 Parámetros y dominios documentados

Los valores siguientes se conservan según la revisión directa del contrato descrita por Softly. El propio material contiene una variación: el desarrollo enumera cuatro focos operativos, mientras un ejemplo posterior agrega «global». No se decide aquí el enum definitivo.

| Parámetro | Valores documentados |
|---|---|
| `densidad` | 1 a 5 |
| `foco_operativo` | fábrica, coordinación, investigación o auditoría; un ejemplo posterior añade «global» |
| `umbral_certeza` | estricto o exploratorio |
| `horizonte_temporal` | delta reciente o genealogía completa |
| `libertad_lexica` | baja, media o alta |

### 8.3 Paquete de salida y reglas de representación

El paquete de salida descrito contiene:
1. encabezado de control;
2. cuerpo representacional;
3. mapa de anclaje;
4. glosario delta.

Reglas que deben preservarse:
- cada afirmación o símbolo del cuerpo se ancla mediante `[REF]` a una fuente concreta;
- cada bloque marca su estado epistémico: `[HECHO]`, `[INFERENCIA]`, `[HIPÓTESIS]` o `[INCERTIDUMBRE / CONTRADICCIÓN]`;
- el glosario delta se genera cuando `libertad_lexica` es superior a baja.

La especificación detallada de tipos, validaciones, límites y formato queda como artefacto de diseño separado. No se infieren valores por defecto adicionales.

### 8.4 Pasada SYN-DAEMON-20261116-001

**[FUENTE — atribución documental]** El PDF presenta una sección titulada «Pasada Real de Prueba: SYN-DAEMON-20261116-001», con parámetros declarados, paquete de representación y tres preguntas de control. Se conserva el hecho de que el documento fuente presenta esa pasada como realizada.

**[LÍMITE DE EVIDENCIA]** En esta deliberación no se reprodujo ni verificó independientemente el lote de entrada, el archivo Softly.zip ni la ejecución de esa pasada. Por tanto, se registra como evidencia documental reportada por el PDF, no como validación experimental independiente.

### 8.5 Cuatro pruebas propuestas

1. **Reconstrucción fiel:** recuperar hechos, relaciones, límites, atribuciones y grados de certeza.
2. **Equivalencia de acción:** producir decisiones operativas compatibles con las fuentes bajo tareas equivalentes.
3. **Detección de vacíos:** reconocer información ausente, contradictoria o insuficiente y volver a la fuente correcta sin inventar.
4. **Transferencia:** resolver un caso nuevo no expresado literalmente en la síntesis, preservando relaciones relevantes.

Las tres primeras se atribuyen al contrato original del PDF; la cuarta fue incorporada durante la deliberación.

**[RIESGO]** La equivalencia de acción puede producir falsos positivos si no se definen tareas comparables, criterios independientes, número de casos, umbrales y variabilidad entre sesiones/modelos.

**[PROPUESTA]** El diseño experimental separado fija corpus/versiones, casos positivos/negativos, contradicciones, omisiones deliberadas, referencias rotas, rúbrica, umbrales, regresiones y criterios de consulta a Capa A. La prueba ciega especifica qué fuentes no pueden consultarse durante la medición y cuándo se permite recuperación.

**[PENDIENTE]** El protocolo, corpus, umbrales y reproducibilidad de la pasada reportada no han sido verificados experimentalmente en esta deliberación.

## 9. MVP y criterios de evaluación

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

Estas son dimensiones, no métricas listas para comparar. Antes de medir se requieren fórmula, unidad, denominador, escenario, línea base, método de detección y umbral de aceptación. No se ha ejecutado un plan experimental en esta deliberación. No hay evidencia que permita declarar el MVP suficiente ni el demonio validado.

## 10. Acuerdos, complementariedades y asuntos abiertos

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

### Complementariedad provisional y diferencia conceptual abierta
Katarina enfatiza el sistema de conocimiento y coordinación cognitiva como centro de la arquitectura; Softly enfatiza la arquitectura de información operacional y la capacidad de contratos, eventos y handoffs para orientar acciones. Ambas aceptan mantener las dos perspectivas para esta reconstrucción, pero no declaran resuelta su jerarquía identitaria. No se identifica una contradicción binaria que obligue a descartar una tesis; sí persiste una diferencia conceptual sustantiva.

### Pendientes
1. Jerarquía conceptual e identidad fundamental.
2. Matriz de autoridad por dominio, conflicto y transición.
3. Campos y estados definitivos del contrato de handoff.
4. Separación técnica de estado del proceso y resultado de la tarea.
5. Ciclo de retrabajo tras entregas observadas o rechazadas.
6. Mecanismo de leases/reclamos, idempotencia y consolidación por entorno.
7. Contrato detallado y evaluación reproducible del demonio.
8. Validación del MVP.

## 11. Registro de las tres correcciones de KAT-004

| Observación de Softly | Tratamiento en v0.3 |
|---|---|
| Preservar la estructura normativa «matriz generativa y un sistema autoevolutivo» | Sección 2; formulación literal separada de la descripción analítica |
| Reconocer el schema de handoff existente y diferenciarlo de la propuesta ampliada | Sección 4.4; se identifican campos, enum y lease declarativos, sin atribuir enforcement |
| Describir SYN-DAEMON-20261116-001 como pasada presentada como realizada en el PDF, sin afirmar reproducción independiente | Sección 8.4 |
| Separar estado del proceso y resultado de la tarea | Sección 5.1 |
| Registrar ciclo de retrabajo como pendiente | Sección 5.5 |
| Preservar dominios de parámetros, anclaje [REF], etiquetas epistémicas y condición del glosario delta | Secciones 8.2 y 8.3 |

## 12. Estado de la deliberación y límites

**Fase I — análisis independiente:** completada.  
**Fase II — informes iniciales individuales:** completada.  
**Fase III — intercambio y revisión cruzada:** completada.  
**Fase IV — reconstrucción conceptual y revisión bilateral:** completada en el plano deliberativo con esta integración final v0.3 y la conformidad sustantiva de Softly, manteniendo expresamente las diferencias y pendientes enumerados.  
**Fase V — informes finales individuales:** en curso; cada agente debe entregar su informe final a gAto.

La conformidad de Softly no equivale a aprobar identidad normativa, cerrar la matriz de autoridad, validar el MVP, validar el demonio ni certificar una implementación. No se ha modificado SOFTLY.md ni schemas; no se ha implementado runtime.

---

*Integración final de la deliberación por Katarina 2.0.0. No constituye decisión normativa ni aprobación de gAto.*
