# Investigación independiente — Coordinación universal y rediseño de la arquitectura de colaboración

**Investigadora:** Softly  
**Dirección humana:** gAto  
**Fecha:** 2026-11-16  
**Versión:** 1.0  
**Estado:** Informe de investigación y recomendación; no implementado ni aprobado  
**Modalidad:** Investigación / Deliberación  
**Alcance:** seis repositorios autorizados y fuentes públicas académicas/técnicas  
**Restricción:** no se modificaron contratos, prompts normativos, schemas, taxonomías ni directorios productivos.

---

## 1. Resumen ejecutivo

### 1.1 Dictamen

No recomiendo reconstruir literalmente la combinación de directorios say/, shared/, inbox/ y outbox/ como arquitectura universal del ecosistema.

Tampoco concluyo que esos conceptos sean inútiles. El problema no es que existan canales, espacios compartidos o bandejas de entrada. El problema observado es que **las mismas etiquetas físicas representan responsabilidades diferentes según el repositorio, y varias responsabilidades distintas se expresan mediante archivos sin un ciclo de vida común**.

La arquitectura actual no es una sola arquitectura coherente: es una familia de convenciones locales que han evolucionado en paralelo. Algunas son razonables y otras presentan ambigüedades o duplicaciones. No hay evidencia suficiente para afirmar que todas fallen en operación; sí hay evidencia documental suficiente para afirmar que la interoperabilidad semántica entre ellas no está resuelta.

**Recomendación principal: Alternativa B, simplificación orientada a tareas**, manteniendo GitHub como memoria documental y plano de coordinación mientras no exista un runtime de agentes conectado. La unidad principal debe ser la tarea con responsable, alcance, dependencias, estado y aceptación. Los mensajes deben quedar vinculados a esa tarea cuando corresponda; los eventos deben registrar cambios; los documentos/artifacts deben ser resultados referenciados, no mensajes duplicados. Las vistas de inbox y outbox pueden derivarse de asignaciones y autoría, en vez de mantenerse como copias físicas independientes.

### 1.2 Respuestas a las dos preguntas finales

**¿Volvería a construir say/, shared/, inbox/ y outbox/?**

No como cuatro capas obligatorias ni como cuatro directorios universales por agente.

- Mantendría la capacidad de comunicación directa, pero no exigiría un directorio say/ por emisor.
- Mantendría un espacio compartido solo cuando exista trabajo o conocimiento que realmente deba ser común y editable por varios integrantes.
- Mantendría la función de recepción de tareas, pero como una vista por responsable sobre tareas persistentes.
- No mantendría un outbox/ duplicado por defecto: el envío debe registrarse una vez y la recepción/aceptación debe referenciar ese mismo identificador.
- Mantendría entregables y bitácoras como conceptos distintos: el artefacto prueba qué se produjo; el evento registra qué ocurrió.

**¿Qué cambios mínimos haría para que cualquier agente se coordine mejor desde su instanciación?**

Incorporaría una competencia universal breve de coordinación propia: comprender autoridad y alcance, identificar responsable y dependencias, declarar estado, comunicar bloqueos mediante confirmación explícita, entregar evidencia y dejar una siguiente acción verificable. La capacidad de dirigir o asignar trabajo a otros sería una competencia adicional según rol y autoridad, no una atribución automática a todos.

### 1.3 Hallazgos de mayor impacto

1. **No existe una semántica universal de directorios.** shared/ puede ser espacio de recepción, memoria propia, workspace de equipo o contenedor de inbox/deliveries/decisions/bitácoras.
2. **Los canales son documentales, no transporte activo.** Los propios contratos de TITAN y Softly advierten que publicar un handoff no activa una sesión ni demuestra lectura, recepción o aceptación.
3. **Hay una contradicción concreta en la documentación de canales.** Auditoria/Softlysay/README.md define Softly → Auditoría y señala que el retorno es audsay/res/ en Softly; en cambio Softly/audsay/README.md titula ese directorio como Softly → Auditoría, aunque dentro describe respuestas de Auditoría hacia Softly.
4. **El handoff actual no equivale a un ciclo completo de tarea.** El schema registra ready, accepted, rejected, blocked y closed, pero no define por sí solo estados de ejecución como working, submitted o completed. El contrato es de transferencia, no un gestor completo de tareas.
5. **La instrumentación de coordinación es insuficiente.** Hay logs y eventos, pero el propio repositorio declara congelada y no normativa la propuesta de schema de eventos JSONL; no hay evidencia de un validador operativo.
6. **Existe un caso real de confusión de destino.** Durante la creación de Katarina para TITAN, Softly escribió inicialmente 42 archivos en el repositorio Softly, actualizó su taxonomía y después debió migrar y limpiar. La ubicación final fue corregida; la causa raíz sigue sin demostrarse.
7. **La evidencia externa no respalda “más agentes = mejor resultado”.** Los resultados dependen del tipo de tarea, de la capacidad del agente individual, del costo de coordinación y de la existencia de dependencias reales.
8. **La coordinación universal es razonable si se define por niveles.** Todos deben saber coordinar su propio trabajo y colaborar entre pares; no todos necesitan autoridad ni competencia profesional para dirigir equipos.

---

## 2. Metodología y límites

### 2.1 Inspección interna

Se consultó la rama main y se recuperó el árbol recursivo de los seis repositorios autorizados. El inventario observado fue:

| Repositorio | Archivos en el árbol inspeccionado | Foco de lectura |
|---|---:|---|
| gatoscientist/Softly | 194 | Mandato, checkpoint, moldes, schemas, canales, logs, handoffs, incidencia y coordinación |
| gatoscientist/Katarina | 31 | Casa canónica, contrato, procedimiento, Softlysay, shared y equipo |
| gatoscientist/Cytryna | 129 | Contrato general, coordinador de herramientas, inbox, políticas, logs, workspace y Camila |
| gatoscientist/TITAN | 231 | Direcciones, constitución, channels, shared/inbox, deliveries, bitácoras y coordinación |
| gatoscientist/Auditoria | 107 | TEAM/COORDINATION, TASK_BOARD, contratos y canal Softlysay |
| gatoscientist/Laboratorio-de-agentes | 404 | README, estructuras históricas de Katarina, inbox/outbox, shared y documentación del arenero |

El inventario de árbol fue recursivo; la lectura de contenido fue selectiva y guiada por las responsabilidades de coordinación y por los casos reales. **No se afirma que se haya leído íntegramente el contenido de los 1.096 archivos.** Se leyeron documentos centrales y ejemplos distribuidos por los seis repositorios, y se contrastaron reglas declaradas con estructuras y registros observables.

No se consultaron repositorios fuera de la lista autorizada. No se solicitó ni se utilizaron conclusiones de la investigación independiente de Katarina. La inspección de su repositorio se limitó a sus contratos, estructura y evidencia operativa disponible.

### 2.2 Investigación externa

Se consultaron literatura académica sobre teoría de coordinación, blackboard systems, teamwork y memoria transaccional; benchmarks recientes de colaboración entre agentes; especificaciones A2A y MCP; y documentación de patrones de orquestación, persistencia y workflows.

Se distingue entre:
- **Hecho interno:** contenido observado en un archivo, estructura o registro del repositorio.
- **Hallazgo:** patrón que emerge al comparar varias evidencias.
- **Evidencia externa:** resultado publicado o documentación técnica.
- **Inferencia:** explicación plausible que conecta hechos.
- **Hipótesis:** explicación que requiere prueba.
- **Propuesta:** diseño recomendado, todavía no aprobado.

### 2.3 Límites

- No se ejecutaron sesiones independientes de agentes ni pruebas runtime.
- No se midieron tokens, latencia, duplicación, tiempos de recepción ni tasa de aceptación en el ecosistema real.
- Los repositorios describen varios flujos, pero su documentación no prueba que todos se hayan ejecutado de forma consistente.
- Algunos estudios recientes son preprints y sus resultados deben tratarse como evidencia emergente, no como leyes universales.
- No se implementó ninguna de las propuestas de este informe.

---

## 3. Marco conceptual: qué es coordinar

Malone y Crowston (1994) definen la coordinación como la gestión de dependencias entre actividades. Esta formulación es útil porque evita reducir la coordinación a “hablar”, “tener un canal” o “asignar personas”. Se coordina cuando existe una dependencia que debe ser gestionada: un recurso compartido, una relación productor-consumidor, una restricción temporal, una tarea que depende de otra o una interfaz entre entregables.

Por tanto, no toda interacción requiere coordinación explícita. Si dos agentes trabajan en tareas independientes y no comparten recursos ni resultados intermedios, añadir mensajes puede no aportar valor.

### 3.1 Coordinar y coordinarse

Propongo conservar la distinción de gAto y precisar sus niveles:

| Dimensión | Qué hace | Quién la necesita |
|---|---|---|
| Coordinación propia | Organiza el propio trabajo, entiende límites, declara estado, detecta dependencias y comunica bloqueos | Universal |
| Coordinación entre pares | Acuerda interfaces, intercambia información necesaria, sincroniza entregas y resuelve dependencias locales | Universal cuando existe colaboración |
| Orquestación | Descompone objetivos, asigna responsables, ordena dependencias, integra resultados y administra el trabajo de otros | Roles de dirección/coordinación, o delegación explícita y acotada |

La hipótesis universal es sólida si significa que ningún agente debe ser incapaz de gestionar su propio trabajo dentro de un sistema colectivo. Sería excesiva si significa que todos deben asumir autoridad para dirigir a otros.

**Coordinarse es una competencia de pertenencia al equipo. Orquestar es una responsabilidad de rol y autoridad.**

La ausencia de un coordinador central para cada interacción no significa ausencia de estructura. Significa que las dependencias simples se resuelven localmente y las dependencias complejas se elevan a una instancia responsable.

### 3.2 Competencia universal mínima

La competencia transversal debería incluir seis comportamientos observables:

1. **Orientación:** identificar objetivo, autoridad, alcance, restricciones, responsable y criterio de aceptación.
2. **Planificación propia:** dividir el trabajo propio en pasos, estimar qué necesita y reconocer qué puede resolver sin depender de otros.
3. **Gestión de dependencias:** identificar qué necesita de otros, quién lo posee y qué parte del resultado queda bloqueado.
4. **Comunicación de ciclo cerrado:** enviar una solicitud concreta, confirmar recepción/entendimiento, responder o rechazar con motivo y avisar cambios relevantes.
5. **Monitoreo y adaptación:** detectar retrasos, errores, contradicciones y cambios de prioridad; pedir ayuda o redistribución cuando corresponda.
6. **Entrega e integración:** dejar artefacto, evidencia, estado, limitaciones y siguiente acción verificable.

La capacidad de asignar tareas, administrar equipos y arbitrar prioridades pertenece al nivel de orquestación. Un agente especializado puede coordinar sus interfaces sin convertirse en director.

---

## 4. Qué dice la evidencia externa

### 4.1 La coordinación gestiona dependencias, no directorios

El marco de Malone y Crowston permite formular la pregunta correcta: ¿qué dependencia resuelve cada estructura? Un directorio no es útil por existir; es útil si hace visible, resoluble y verificable una dependencia.

Los tipos de dependencia que más importan en este ecosistema son:
- **Precedencia:** B no puede comenzar hasta que A produzca un resultado.
- **Interfaz:** dos agentes producen componentes que deben encajar.
- **Recurso compartido:** varios agentes pueden modificar el mismo archivo, registro o proyecto.
- **Información:** un agente necesita un dato que otro conoce.
- **Autoridad:** una decisión requiere aprobación de gAto o de un responsable autorizado.
- **Integración/aceptación:** un resultado debe ser contrastado contra un criterio antes de considerarse terminado.

La estructura de coordinación debe representar estas dependencias directamente. Un inbox vacío o una carpeta shared sin reglas no las resuelve.

### 4.2 Blackboard y memoria compartida

La arquitectura blackboard clásica utiliza un espacio común donde varias fuentes de conocimiento leen y escriben resultados parciales. La idea sirve para colaboración indirecta y para evitar que cada agente tenga que enviar el mismo contenido a todos los demás.

Pero el blackboard clásico también incorpora una estrategia de control que selecciona qué fuente de conocimiento actúa. El espacio compartido no elimina automáticamente la necesidad de decidir quién actúa, cuándo y con qué criterio. En muchas formulaciones el control es secuencial y centralizado.

Conclusión: shared/ puede reducir mensajes repetidos, pero no reemplaza:
- propiedad de tareas;
- reglas de escritura;
- control de concurrencia;
- criterios de aceptación;
- autoridad;
- estados de trabajo.

Un espacio compartido sin propiedad ni interfaces claras puede convertirse en un lugar donde todos leen, pocos escriben y nadie responde por la integración.

### 4.3 Costos de comunicación y tamaño de equipos

El estudio *When Agents Coordinate* (Destefanis y Aste, 2026; preprint) instrumentó 1.902 ejecuciones de equipos de agentes de programación. Representó agentes y archivos como nodos, y mensajes, lecturas y escrituras como aristas temporales.

Sus resultados relevantes:
- La mensajería directa puede crecer cerca de forma cuadrática en determinadas tareas y tamaños.
- El tipo de tarea cambia la topología: tareas de especificación compartida generan redes densas; pipelines con interfaces locales generan redes más dispersas.
- En tareas intensivas en mensajes, los archivos compartidos redujeron cerca de 42% los tokens de salida a ocho agentes; en la otra condición agregaron costo.
- Nombrar un coordinador en el prompt no produjo por sí solo un hub de comunicación ni una mejora fiable de éxito.
- En una cadena de ocho pasos hubo fallos repetidos porque la convención de redondeo en una interfaz entre dos responsables no tuvo dueño.

Es una evidencia muy pertinente, pero acotada: tareas sintéticas de programación, modelo y entorno específicos. No permite extrapolar porcentajes al ecosistema del gAto. Sí respalda tres principios: medir la coordinación, usar archivos cuando sustituyen comunicación repetida y asignar dueño explícito a cada interfaz.

### 4.4 Más agentes no significa mejor resultado

La evaluación del MIT Media Lab de 260 configuraciones y seis benchmarks encontró que la colaboración puede ayudar o perjudicar según la tarea y la capacidad del agente individual. La coordinación centralizada mejoró el resultado en un benchmark financiero, mientras que todas las variantes multiagente evaluadas perjudicaron un benchmark de planificación. En sus pruebas, la línea base de un solo agente fue un predictor importante de si sumar agentes aportaría valor.

Esto coincide con las recomendaciones de Microsoft y Akka: usar el nivel más bajo de complejidad que cumpla confiablemente el objetivo; incorporar agentes especializados cuando la separación de contexto, capacidades, datos o seguridad lo justifique.

**Regla de diseño:** antes de crear un equipo, demostrar qué parte del trabajo no puede resolver de forma fiable un agente único o un workflow sencillo.

### 4.5 Roles y límites no se garantizan solo con prompts

TeamBench (2026; preprint) separa Planner, Executor y Verifier mediante permisos de sistema operativo. Reporta que los equipos con roles definidos solo por prompt intentaron que el verificador modificara el código 3,6 veces más que los equipos con aislamiento; también observa verificaciones que aprobaron entregas que fallaban el evaluador determinista.

El resultado no significa que todo rol deba ejecutarse en un contenedor. Sí advierte que **un contrato documental no es enforcement técnico**. En los repositorios actuales abundan declaraciones de permisos, pero varias instancias están en estado Diseñado y no conectadas a runtime. No se debe presentar una separación declarada como una barrera técnica real.

### 4.6 Privacidad y memoria transaccional

PAC-Bench (2026; preprint) encuentra que las restricciones de privacidad pueden degradar la colaboración por filtraciones tempranas, abstracciones excesivamente conservadoras y alucinaciones inducidas por información incompleta. Esto refuerza que un shared/ no debe significar “todo visible para todos”.

La investigación sobre transactive memory systems estudia cómo los equipos saben quién conoce qué. Esta memoria no es simplemente una carpeta común: es conocimiento sobre la distribución de expertise y la forma de encontrar al especialista correcto. La evidencia meta-analítica reporta una asociación positiva moderada entre sistemas de memoria transaccional y resultados de equipo, con variación según cómo se mida el resultado.

La implicancia para Softly es mantener un registro claro de dominios, competencias demostradas y responsables, sin copiar indiscriminadamente toda la memoria de cada agente a un espacio común.

### 4.7 Formación de equipos

El modelo “Big Five” de teamwork identifica liderazgo, monitoreo mutuo del desempeño, conducta de respaldo, adaptabilidad y orientación al equipo, apoyados por modelos mentales compartidos, comunicación de ciclo cerrado y confianza.

Un estudio experimental de cross-training encontró mejoras en modelos mentales de interacción del equipo y una relación mediada entre esos modelos, coordinación y desempeño. La profundidad de entrenamiento necesaria no quedó resuelta de forma uniforme.

Transferencia prudente a agentes:
- Es razonable enseñar vocabulario, roles, dependencias, confirmación y entrega.
- Es razonable evaluar con ejercicios de colaboración y no solo con preguntas teóricas.
- No está demostrado que añadir un documento largo de formación a cada prompt mejore automáticamente el comportamiento de un LLM.
- Debe compararse formación formal con instrucciones mínimas y protocolos explícitos.

### 4.8 Protocolos y workflows

FIPA ACL aporta una lección histórica: un mensaje de agente no es solo texto. Incluye el acto comunicativo (performative), emisor, destinatario, contenido, protocolo, identificador de conversación y campos de respuesta/tiempo.

A2A lleva la separación a un modelo moderno:
- Message representa comunicación.
- Task representa una unidad de trabajo con ID, estado e historial.
- Artifact representa el resultado producido.
- El ciclo de tarea distingue recepción, ejecución, espera de input y estados terminales.
- La especificación define operaciones de consulta, cancelación, streaming y notificación; también contempla idempotencia mediante identificadores de mensaje.

MCP cumple otra función: conecta un host/cliente con servidores de herramientas, recursos y prompts. No sustituye un protocolo de coordinación entre agentes. A2A y MCP son capas complementarias: agente↔agente y agente↔herramienta.

Temporal y LangGraph ilustran lo que se gana con runtime: persistencia de estado, checkpoints, reanudación, eventos, retries e intervención humana. También introducen infraestructura, reglas de determinismo, operación y seguridad. Son referencias para una futura etapa, no una razón para abandonar hoy el modelo documental.

### 4.9 Event sourcing: útil, pero no gratuito

Un registro append-only mejora trazabilidad y reconstrucción histórica. Sin embargo, event sourcing completo agrega complejidad en concurrencia, versionado de schemas, consistencia eventual, consultas, snapshots y replay.

Para el estado actual de Softly no recomiendo implantar event sourcing completo. Recomiendo un **registro de eventos liviano** asociado a una tarea y un estado actual verificable. El historial Git y los eventos append-only ya ofrecen una base suficiente si se normalizan y validan. No se necesita construir un motor de eventos antes de demostrar que el volumen o la concurrencia lo exigen.

---

## 5. Auditoría del sistema actual

### 5.1 Softly

El mandato ejecutivo define a Softly como matriz generativa y sistema autoevolutivo; el repositorio es memoria documental pasiva. El inicio se apoya en SOFTLY.md y CHECKPOINT.md. Se declara que GitHub conserva asignaciones, entregables, decisiones y handoffs, pero que un handoff publicado no despierta otra sesión.

El molde de handoff contiene destinatario, assignment ID, resultado, evidencia, decisiones, bloqueos, siguiente acción, aceptación y referencias de contexto. El schema añade handoff_id, event_id, status, emisor, receptor, tarea, resultado, evidencia, fecha y lease opcional.

Fortalezas:
- Distingue identidad, competencia, permisos y herramientas.
- El handoff obliga a declarar resultado y aceptación.
- La documentación no confunde publicación con activación.
- Hay actividad, decisiones, incidencias y conservación de hilos.
- El incidente de destino equivocado se registró con hechos, consecuencias e hipótesis separadas.

Deficiencias observadas:
- El schema de handoff representa transferencia, no ciclo de vida completo de una tarea.
- La regla de no duplicar por event_id no equivale a deduplicación técnica si no existe consumidor que la aplique.
- El schema existe, pero el repositorio advierte que su presencia no demuestra un validador automático.
- La propuesta de schema de eventos JSONL está congelada y no normativa; el propio documento declara que no existe validador de eventos.
- El árbol raíz no contiene un directorio shared/ ni outbox/, aunque esos conceptos aparecen en modelos y antecedentes.
- La documentación de audsay/ tiene una contradicción de dirección: su README lo titula Softly → Auditoría, pero describe allí la recepción de respuestas de Auditoría hacia Softly. El README de Auditoria/Softlysay/ define el sentido opuesto de manera explícita.
- Softlysay/ en la raíz de Softly contiene entregables propios, pero no un README de canal que aclare su función en el árbol actual.
- docs/architecture/operational-modes-and-autocoordination.md conserva la frase “Modelo: Softly agente”, que contradice la identidad más reciente de SOFTLY.md: matriz generativa, no agente individual. Es deriva documental que debe corregirse cuando gAto autorice una actualización normativa.

Un informe anterior de Softly defendió la separación say/shared como una forma de reducir ambigüedad. Esa afirmación fue una evaluación conceptual, no una medición. La auditoría actual no la da por demostrada y encuentra convenciones que la contradicen.

### 5.2 Katarina

La casa canónica de Katarina es gatoscientist/Katarina. Su canal de entrada Softly → Katarina se llama Softlysay/; el canal de retorno Katarina → Softly vive en Katarinasay/ del repositorio Softly.

Su procedimiento diferencia:
- asignación de gAto;
- mensaje informativo;
- encargo ejecutable dentro del mandato;
- propuesta fuera del alcance o con duda razonable.

También separa shared/ como depósito de materiales y antecedentes —no activa trabajo por sí solo— de mancos/shared/, usado para delegaciones, borradores y entregables del equipo.

Fortalezas:
- La recepción no equivale a activación.
- La activación no autoriza a exceder el mandato.
- La delegación exige objetivo, contexto, entregable, aceptación, restricciones y ubicación.
- El especialista conserva identidad y memoria privada.

Riesgos:
- El procedimiento depende de que el agente interprete correctamente el tipo de mensaje y el mandato.
- La distinción informativo/encargo/propuesta no está unificada con el ciclo de estados de tareas del resto del ecosistema.
- El modelo histórico del Laboratorio contiene un outbox local que es copia de lo enviado por Katarinasay; es útil como archivo, pero duplica el objeto comunicativo si no se trata explícitamente como copia de auditoría.

### 5.3 Cytryna

Cytryna organiza sus raíces de trabajo por agente. AGENTDEV y AGENTGUI tienen inbox de solo lectura, logs, reportes, workspace, notas, scratch y archive. La política indica que las respuestas se hacen mediante reports o canal compartido; los logs son append-only y distinguen observado, inferido y propuesto.

Camila declara un equipo de tres especialistas y un procedimiento de dirección con objetivo, alcance, entregables, responsables, dependencias, integración y escalamiento.

El archivo Cytryna/coordinator.py es importante para evitar una confusión conceptual: su AgentCoordinator coordina proveedores de modelos, contexto y herramientas dentro de Cytryna. No es, por sí solo, un coordinador multiagente del ecosistema.

Fortalezas:
- Políticas de escritura explícitas.
- Separación entre identidad del agente y proyecto activo.
- Logs con campos de evidencia y estado.
- No se permite escribir en la raíz de otro agente.
- Camila explicita que no puede afirmar activación por haber publicado una asignación.

Riesgos:
- Inbox de solo lectura y reports son convenciones locales que no equivalen a un protocolo de aceptación común.
- No hay una capa compartida de tareas que conecte automáticamente Cytryna con Softly, Katarina o TITAN.
- El sistema real de Cytryna posee coordinación interna de herramientas, pero esa función no debe confundirse con coordinación entre agentes.

### 5.4 TITAN

TITAN contiene el ejemplo documental más explícito de separación entre asignación, resultado y decisión. La Dirección de Recuperación de Cytryna define:
- canales externos hacia Softly y Katarina;
- shared/inbox/ para tareas;
- shared/deliveries/ para resultados;
- shared/decisions/ para decisiones;
- shared/bitacoras/ para cronología.

La constitución exige ID, responsable, competencia, objetivo, alcance/rutas, evidencia, dependencias, permisos, entregable y aceptación.

Fortalezas:
- La tarea está mejor definida que un mensaje libre.
- Se distingue inbox de deliveries.
- Se separan decisiones y cronología.
- Se explicita que los canales son documentales y no implican conectividad.
- El informe 06 conserva el estado real: handoff publicado, especialistas no activados, revisión independiente pendiente.

Riesgos:
- shared/ se convierte en un contenedor de cuatro responsabilidades distintas. Es comprensible localmente, pero no necesariamente portable como convención universal.
- Los canales externos y el inbox interno coexisten; sin un identificador común y una única fuente de estado, una misma misión puede aparecer como mensaje, handoff y tarea.
- La dirección documental no garantiza que el agente haya recibido o ejecutado la asignación.

### 5.5 Auditoría

Auditoría usa un modelo distinto: TEAM/COORDINATION.md y TEAM/TASK_BOARD.md. La coordinación aplica regla 1-1-1: encargo, ejecución single-pass y triage de salida. Aurora y Autumn emiten un informe por encargo; Audeline consolida, filtra por alcance y mantiene GO, GO con deuda o NO-GO acotado. El retest está limitado a un parche P0.

Fortalezas:
- La tarea y su responsable aparecen en un tablero.
- Se reduce deliberación ceremonial y duplicación.
- La salida tiene criterios de aceptación y severidad.
- El cierre distingue riesgos eliminados de deuda aceptada.
- La ausencia de evidencia se declara como limitación.

Riesgos:
- El tablero es un documento Markdown; no hay evidencia de actualización automática ni bloqueo por estado.
- La coordinación single-pass es apropiada para auditoría delimitada, pero no debe convertirse en una regla universal para investigación o trabajo iterativo.
- La consolidación depende de que Audeline reciba y contraste informes, no de que el tablero por sí solo garantice recepción.

### 5.6 Laboratorio de agentes

El Laboratorio conserva material histórico, paquetes, prototipos y estructuras de agentes. Su README declara que el repositorio no equivale a runtime ni demuestra despliegue.

Las estructuras históricas de Katarina muestran:
- Softlysay/inbox/ para mensajes de Softly;
- Softlysay/outbox/ como copia local de lo despachado por Katarinasay;
- shared/ para materiales;
- mancos/shared/inbox/ con carpetas por agente;
- entregables/, borradores/ y bitácoras.

Es evidencia de evolución y experimentación, no una descripción automática de la estructura canónica actual de Katarina. Mantenerla como antecedente es correcto; usarla como norma vigente sin comprobar versión y destino sería incorrecto.

---

## 6. Reconstrucción de flujos observables

Los siguientes flujos describen lo que establecen los documentos, no una afirmación de que cada transferencia haya sido ejecutada en runtime.

### 6.1 Softly ↔ Katarina

~~~text
Softly
  └─ deposita mensaje/entregable en Softlysay (casa de Katarina)
       └─ Katarina clasifica: informativo / encargo / propuesta
            ├─ informativo: recibe y conserva
            ├─ encargo: valida mandato y ejecuta
            └─ propuesta: registra y eleva a gAto
                 └─ entrega / respuesta hacia Katarinasay (casa de Softly)
~~~

La clasificación de intención está bien concebida. Falta una convención única para estado de recepción, aceptación y finalización que se aplique de la misma forma a todos los repositorios.

### 6.2 Katarina → especialistas

~~~text
Katarina
  └─ asignación delimitada en mancos/shared/inbox
       └─ especialista trabaja en su espacio propio
            └─ entrega resultado terminado
                 └─ Katarina integra, verifica interfaces y consolida
~~~

Este flujo tiene un dueño de integración y límites de especialidad. El principal riesgo está en la falta de un estado compartido normalizado para saber si la asignación fue aceptada, iniciada, bloqueada o terminada.

### 6.3 Elara y equipo de TITAN

~~~text
gAto / misión aprobada
  └─ Elara descompone y asigna
       └─ shared/inbox
            └─ especialista produce
                 └─ shared/deliveries
                      └─ Elara integra y registra decisiones
                           └─ channels/softly o channels/katarina si corresponde
~~~

El propio informe de TITAN distingue publicación de handoff y activación real. Esta honestidad debe conservarse.

### 6.4 Cytryna

~~~text
Coordinación
  └─ inbox de la raíz de trabajo (solo lectura)
       └─ agente inspecciona y planifica
            └─ workspace / notes / scratch
                 └─ reports + logs
                      └─ coordinación integra o decide
~~~

El runtime de Cytryna también gestiona llamadas a herramientas y proveedores. Esa coordinación interna no constituye mensajería multiagente.

### 6.5 Auditoría

~~~text
gAto asigna misión
  └─ TEAM/TASK_BOARD
       ├─ Aurora: observación conductual
       ├─ Autumn: revisión técnica
       └─ Audeline: scope gatekeeper e integración
            └─ dictamen: GO / GO con deuda / NO-GO acotado
~~~

Este flujo prioriza control de alcance y economía de revisión. Es un patrón específico de auditoría, no un molde obligatorio para todos los proyectos.

---

## 7. Problemas y causas

### 7.1 Problemas confirmados documentalmente

| ID | Hallazgo | Severidad provisional | Evidencia |
|---|---|---|---|
| H-01 | Semántica no uniforme de shared/ entre repositorios | Alta | Katarina, TITAN y estructuras históricas del Laboratorio |
| H-02 | Contradicción de dirección en README de audsay/ | Media | Softly/audsay frente a Auditoria/Softlysay |
| H-03 | Handoff no define por sí solo el ciclo de vida completo de tarea | Alta | handoff.schema.json y handoff.md |
| H-04 | No hay validación automática demostrada para eventos JSONL | Media | schemas/README y propuesta congelada |
| H-05 | Publicación documental no demuestra recepción, activación ni ejecución | Alta | SOFTLY.md, TITAN y reportes de continuidad |
| H-06 | Deriva documental sobre identidad/modelo de Softly | Media | SOFTLY.md frente a operational-modes-and-autocoordination.md |
| H-07 | El ecosistema tiene patrones locales útiles, pero no un contrato común de interoperabilidad | Alta | comparación de seis repositorios |

Las severidades son estimaciones de impacto arquitectónico, no una auditoría formal P0/P1/P2.

### 7.2 Incidente de destino equivocado

El registro INC-20261116-003 y la observación OBS-20261116-004 documentan que Softly interpretó /TITAN como carpeta dentro de gatoscientist/Softly, creó 42 archivos allí y actualizó el registro taxonómico antes de confirmar el repositorio correcto. Después migró los paquetes al repositorio TITAN, eliminó la copia incorrecta y verificó el estado final.

**Causa inmediata confirmada:** resolución incorrecta de la ubicación destino.

**Factores contribuyentes plausibles, no demostrados:**
- ambigüedad entre casa del agente, repositorio de proyecto y carpeta interna;
- falta de un preflight que fijara owner/repo + branch + path;
- sesgo hacia el repositorio activo de la sesión;
- actualización prematura del registro taxonómico;
- ausencia de un manifiesto de origen-destino antes de migrar.

**Causa raíz:** no demostrada. El registro interno también lo declara así.

La prevención debe ser más simple que la reparación: antes de escribir, resolver repositorio, rama, ruta y operación; comprobar el destino; después escribir. Un canal o un directorio no resuelve esta clase de error.

### 7.3 ¿El sistema ayuda o se mantiene a sí mismo?

No hay mediciones internas que permitan calcular el costo neto. Por lo tanto, no afirmo que el ecosistema esté trabajando más para mantener sus directorios que para producir resultados.

Sí hay indicadores de costo potencial:
- el mismo encargo puede aparecer como mensaje, handoff, tarea y bitácora;
- los estados no están normalizados;
- hay copias locales de mensajes en estructuras históricas;
- las convenciones cambian entre repositorios;
- no hay confirmación técnica de lectura/aceptación;
- los reportes a veces deben aclarar que la activación no ocurrió.

La hipótesis que debe probarse es: **la carga principal no proviene del número de directorios, sino de tener que reconstruir qué significa cada archivo y cuál es el estado verdadero de la tarea.**

---

## 8. Arquitecturas alternativas

### Alternativa A — Evolución conservadora

Mantener say/, shared/, inbox/, outbox/, deliveries/ y logs/, pero normalizar sus significados.

Componentes:
- say/: mensajes informativos y solicitudes.
- inbox/: tareas recibidas.
- outbox/: registro de envíos, no copia del resultado.
- shared/: workspace común y únicamente común.
- deliveries/: resultados finales.
- logs/: eventos append-only.

Flujo:
~~~text
Mensaje → clasificación → tarea en inbox → aceptación → ejecución
        → entrega → aceptación/rechazo → evento de cierre
~~~

Ventajas:
- Baja migración.
- Conserva rutas conocidas.
- Permite corregir los problemas más evidentes.
- Es compatible con los paquetes existentes.

Riesgos:
- Sigue habiendo muchas superficies físicas.
- El concepto de mensaje puede seguir duplicando una tarea.
- La interoperabilidad depende de mantener muchas convenciones.
- Puede normalizar una complejidad que quizá no se necesita.

**Evaluación:** opción de transición segura si gAto no quiere rediseñar todavía, pero no es mi arquitectura objetivo.

### Alternativa B — Simplificación centrada en tareas (recomendada)

La unidad primaria es una tarea persistente. La comunicación, los cambios de estado y los resultados se vinculan a esa tarea.

Componentes lógicos:
1. **Task record:** ID, creador, responsable, objetivo, alcance, permisos, dependencias, entregable, aceptación, estado y referencias.
2. **Event log:** eventos append-only que registran creación, asignación, aceptación, inicio, bloqueo, cambio, entrega, aceptación final o rechazo.
3. **Messages:** comunicación breve asociada a una tarea; puede ser solicitud, aclaración, información, respuesta o escalamiento. No contiene el artefacto final por duplicado.
4. **Artifacts:** archivos de resultado, con autor, versión, commit, evidencia y limitaciones.
5. **Workspace:** espacio compartido solo cuando dos o más agentes deben trabajar sobre el mismo recurso.
6. **Agent capability registry:** identidad, dominio, competencias demostradas, disponibilidad declarada y límites.

Diagrama:
~~~text
                 ┌─────────────────────┐
                 │   Task record       │
                 │ objetivo/owner      │
                 │ alcance/dependencias│
                 │ estado/aceptación   │
                 └──────────┬──────────┘
                            │
               ┌────────────┼────────────┐
               │            │            │
          Messages      Event log     Artifacts
        (comunicación)  (trazabilidad) (resultados)
               │            │            │
               └────────────┼────────────┘
                            │
                    Workspace opcional
                    solo si es compartido
~~~

Reglas:
- Una tarea tiene un único responsable de resultado, aunque varios agentes contribuyan.
- Cada dependencia tiene dueño y condición de desbloqueo.
- El agente que recibe una asignación confirma accepted, rejected o blocked; la aceptación no significa que el trabajo esté terminado.
- El responsable actualiza el estado y no crea una segunda tarea para comunicar el mismo cambio.
- El resultado se entrega como artifact con referencia al commit y criterio de aceptación.
- La aceptación final la realiza el solicitante o integrador autorizado.
- Los mensajes informativos pueden existir sin tarea, pero no activan trabajo por sí solos.
- Las vistas de “mis tareas”, “pendientes por agente” o “enviadas por agente” se derivan de los campos de tarea; no requieren duplicar el objeto en inbox y outbox.

Estados mínimos sugeridos:
proposed → ready → accepted → working → blocked / submitted → accepted_final / rejected / canceled.

No todos los flujos necesitan todos los estados. La transición debe tener actor, timestamp y motivo cuando corresponda. No se debe permitir cerrar una tarea solo porque se escribió un archivo.

Gestión de conflictos:
- conflicto de edición: propietario del archivo o bloqueo/versionado explícito;
- conflicto de alcance: escalar a quien tiene autoridad;
- conflicto de interfaz: asignar dueño de interfaz y criterio verificable;
- conflicto de evidencia: conservar ambas fuentes y pedir contraste;
- duplicación: detectar mismo objetivo/artefacto/alcance antes de crear otra tarea.

Ventajas:
- Una fuente de verdad por tarea.
- Menos duplicación de mensajes y archivos.
- Estado visible sin inferirlo desde el nombre de carpeta.
- Permite coordinación descentralizada dentro de límites.
- Compatible con GitHub y con el modelo Prompting + Contratos + GitHub.
- Puede migrar gradualmente sin requerir runtime.

Riesgos:
- Requiere acordar un schema pequeño.
- Puede transformarse en burocracia si cada conversación se convierte en tarea.
- Un event log mal diseñado puede convertirse en otro sistema que mantener.
- Sin permisos de filesystem/branch o validador, los estados siguen siendo declarativos.

**Evaluación:** mejor equilibrio entre claridad, costo, trazabilidad y compatibilidad con el ecosistema actual.

### Alternativa C — Arquitectura nueva con runtime y protocolos

Construir un plano de coordinación ejecutable:
- A2A para comunicación y delegación entre agentes independientes.
- MCP para acceso a herramientas y recursos.
- Agent Cards para descubrir capacidades e interfaces.
- Workflow engine para tareas duraderas, reintentos, espera de input y recuperación.
- Event store/estado de tareas con permisos y deduplicación.
- Auditoría de eventos, trazas y artefactos.
- Aprobación humana en operaciones sensibles.

Diagrama:
~~~text
                    gAto / autoridad
                           │
                    Human approval
                           │
                 Workflow / task engine
                  ┌────────┴────────┐
                  │                 │
              A2A router       Task state
                  │                 │
          ┌───────┼───────┐         │
        Agent A Agent B Agent C     │
          │       │       │         │
          └───────┴───────┘         │
                  │                 │
             MCP clients ───── Tools / APIs
                  │
          Artifacts + event history
~~~

Ventajas:
- Recepción, estados, reintentos y notificaciones pueden ser reales.
- Reduce la dependencia de revisar manualmente carpetas.
- Permite interoperabilidad con agentes heterogéneos.
- Puede aplicar permisos técnicos y límites de ejecución.

Riesgos:
- Costos de desarrollo, operación, seguridad y mantenimiento.
- Necesidad de autenticar agentes y proteger sus datos.
- Fallos de entrega, retries duplicados, consistencia y observabilidad.
- La automatización puede propagar errores más rápido.
- Exige runtime, conectores y operación que el mandato actual no requiere.
- No resuelve por sí sola la calidad de las tareas ni la ambigüedad de los contratos.

**Evaluación:** no recomendada como siguiente paso. Solo debe considerarse cuando el experimento demuestre que la coordinación documental/manual es un cuello de botella que justifica infraestructura.

---

## 9. Recomendación arquitectónica

Recomiendo **Alternativa B**, implementada gradualmente y sin cambiar todavía los mandatos normativos.

La arquitectura futura debería tener cinco entidades conceptuales:

| Entidad | Pregunta que responde | Debe contener |
|---|---|---|
| Mensaje | ¿Qué necesita comunicar alguien? | emisor, destinatario, tipo, referencia a tarea, respuesta a, fecha |
| Tarea | ¿Quién debe producir qué y bajo qué condiciones? | owner, alcance, dependencia, estado, entregable y aceptación |
| Evento | ¿Qué cambió y cuándo? | actor, acción, timestamp, entidad afectada, evidencia |
| Artifact | ¿Qué resultado persistente se produjo? | ruta, autor, versión, commit, evidencia, límites |
| Workspace | ¿Qué recurso deben compartir realmente varios agentes? | recurso, propietarios, reglas de edición y versión |

No se debe confundir:
- un mensaje con una tarea;
- una tarea con un resultado;
- un evento con una instrucción;
- un artifact con un mensaje;
- una carpeta compartida con una memoria transaccional;
- una asignación publicada con una sesión activada.

### 9.1 Qué hacer con cada directorio

| Directorio actual | Recomendación |
|---|---|
| say/ | Retirar su condición de estructura universal. El mensaje pasa a ser una entidad tipada; el canal es metadato o vista de destino. |
| shared/ | Mantener solo cuando haya recursos genuinamente comunes. No usarlo como sinónimo de inbox, memoria, entregables y decisiones a la vez. |
| inbox/ | Convertirlo en vista de tareas asignadas y pendientes. Puede mantenerse físicamente durante transición. |
| outbox/ | No duplicar por defecto. Registrar autoría/envío en el mismo objeto de tarea o mensaje. |
| entregable/ / deliveries/ / reports/ | Normalizar como artifacts con metadatos y aceptación. Conservar subcarpetas locales si ayudan a la navegación. |
| bitacora/ / logs/ | Registrar eventos relevantes, no transcribir toda la interacción ni duplicar mensajes completos. |
| decisions/ | Mantener decisiones de autoridad y diseño separadas del estado operativo de las tareas. |

### 9.2 Qué no vale la pena implementar ahora

- Un bus de mensajes propio.
- Un agente coordinador central que deba aprobar cada interacción.
- Un event sourcing completo con replay de toda la actividad.
- Directorios inbox/outbox por cada agente si son copias de la misma tarea.
- Una nueva taxonomía profesional solo para representar coordinación.
- Formación extensa obligatoria para todos antes de probar instrucciones mínimas.
- Automatización de activación sin mecanismo real de identidad, permisos y ejecución.

---

## 10. Competencia universal: formación y cambios mínimos

### 10.1 Nivel mínimo para todos los agentes

Toda instancia debería recibir un bloque compacto que le enseñe a:
1. reconocer quién tiene autoridad y qué permisos tiene;
2. declarar qué entendió que debe producir;
3. identificar responsable, dependencias e interfaces;
4. trabajar autónomamente dentro de su alcance;
5. comunicar progreso solo cuando cambie el estado relevante;
6. confirmar recepción y comprensión de asignaciones;
7. rechazar o escalar encargos fuera de competencia;
8. entregar resultado, evidencia, limitaciones y siguiente acción.

### 10.2 Nivel de coordinación entre pares

Cuando el agente trabaja con otros, además:
- acuerda formatos e interfaces antes de producir componentes dependientes;
- no presume que otro agente recibió un mensaje;
- no declara que una tarea está activa solo porque existe un archivo;
- pide confirmación de recepción cuando el plazo o riesgo lo justifique;
- comparte solo el contexto necesario;
- no modifica archivos ajenos fuera de permisos;
- avisa cambios que invalidan dependencias;
- propone ayuda o redistribución sin apropiarse de autoridad.

### 10.3 Nivel de orquestación

Para AgentDIR, coordinadores y responsables de equipos:
- descomposición y estimación de tareas;
- asignación por competencias demostradas y disponibilidad;
- gestión de recursos y dependencias;
- seguimiento de estados;
- resolución de conflictos;
- integración y aceptación;
- escalamiento a gAto;
- evaluación del costo de coordinación.

### 10.4 Formación formal frente a instrucciones pequeñas

Mi recomendación es no elegir entre prompt y formación como si fueran excluyentes.

- **Base universal:** instrucciones breves, repetibles y aplicables al flujo.
- **Formación de rol:** material estructurado para agentes que dirigen equipos, gestionan experimentos o integran resultados.
- **Práctica:** casos de asignación, dependencia, bloqueo, rechazo, interfaz y entrega.
- **Evaluación:** tareas observables; no basta con que el agente recite el protocolo.

La hipótesis de que una formación formal extensa mejora a todos los agentes debe medirse. El conocimiento de coordinación puede transferirse, pero la competencia real exige demostrar conducta bajo restricciones y ambigüedad.

---

## 11. Coordinación según el trabajo

La coordinación es transversal, pero se expresa distinto según el modo.

| Actividad | Qué se coordina | Control clave |
|---|---|---|
| Fábrica | producción, archivos, dependencias, integración y aceptación | owner único por entregable, alcance y criterios claros |
| Fábrica Experimental | hipótesis, variables, condiciones, replicación, resultados y límites | separación entre experimento y producto; no presentar hipótesis como hechos |
| Investigación y Deliberación | fuentes, líneas independientes, contraste, evidencia y síntesis | procedencia, independencia, incertidumbre y decisión pendiente |

La clasificación de tres modos indicada en el mandato es una hipótesis conceptual. No reemplaza ni modifica los modos normativos actuales de SOFTLY.md. La coordinación no debe convertirse en un cuarto modo exclusivo: es una competencia que opera en cualquiera de las actividades.

---

## 12. Experimentos comparativos

No se han ejecutado. Los diseños siguientes son propuestas para obtener evidencia del propio ecosistema.

### 12.1 Experimento A — competencia universal

Condiciones:
- A0: agente actual, sin mejora.
- A1: instrucciones mínimas de coordinación propia.
- A2: formación estructurada en coordinación.
- A3: protocolo explícito de tareas, estados y entregas.

Mantener iguales modelo, herramientas, presupuesto, tarea, contexto inicial y criterios de evaluación. Usar asignación aleatoria de condiciones y varias repeticiones. El tamaño muestral definitivo debe calcularse con la varianza observada en un piloto; no asumir que unas pocas ejecuciones bastan.

Tareas:
- una asignación con dependencia simple;
- dos tareas independientes;
- una interfaz entre dos especialistas;
- un bloqueo que requiere ayuda;
- un encargo fuera de competencia;
- una solicitud con destino de repositorio ambiguo;
- una entrega que necesita aceptación y corrección.

Hipótesis:
- H-A1: A1 reduce omisiones de estado y handoffs incompletos frente a A0.
- H-A2: A2 mejora coordinación en casos complejos, pero puede aumentar contexto y latencia.
- H-A3: A3 reduce errores de transferencia y duplicación, siempre que el protocolo sea breve y aplicado.
- H-A4: la combinación A1+A3 puede igualar o superar A2 con menor costo; debe probarse, no asumirse.

### 12.2 Experimento B — arquitectura

Comparar:
- B-A: estructura conservadora actual normalizada;
- B-B: tarea como unidad primaria, con mensajes/eventos/artifacts vinculados;
- B-C: simulación de arquitectura runtime con workflow y comunicación A2A.

Usar el mismo equipo y las mismas tareas: pipeline, investigación paralela, trabajo con recurso compartido, revisión independiente y transferencia entre repositorios.

No comparar solo “si terminó”. Registrar el costo y los fallos del proceso.

### 12.3 Métricas

| Métrica | Definición operacional |
|---|---|
| Tasa de tareas aceptadas | Entregas aceptadas / tareas asignadas |
| Tiempo de ciclo | Tiempo desde asignación hasta aceptación final |
| Overhead de coordinación | tokens/tiempo dedicados a coordinar dividido por el total, medidos por separado |
| Duplicación | tareas o trabajo repetido sin justificación / trabajo total |
| Pérdida de handoff | asignaciones sin recepción/aceptación verificable |
| Exactitud de estado | proporción de tareas cuyo estado declarado coincide con la evidencia |
| Calidad de entrega | evaluación ciega contra criterio de aceptación |
| Intervención humana | intervenciones necesarias por tarea aceptada |
| Error de enrutamiento | escrituras o asignaciones dirigidas al repositorio/agente incorrecto |
| Conflictos de interfaz | incompatibilidades detectadas entre entregables |
| Recuperación | tiempo y costo para resolver un bloqueo o una entrega fallida |
| Privacidad/permisos | divulgaciones o escrituras fuera del alcance permitido |

Definir un índice de eficiencia como calidad aceptada por unidad de costo de coordinación, pero conservar los componentes individuales para evitar ocultar compensaciones.

### 12.4 Criterios de aceptación

Una arquitectura solo debe reemplazar a otra si:
- no reduce de forma material la calidad aceptada;
- reduce o mantiene el costo total;
- disminuye pérdidas, duplicaciones o estados incorrectos;
- no aumenta errores de permisos ni exposición de datos;
- puede ser mantenida por el equipo sin añadir una carga administrativa desproporcionada.

No se deben declarar resultados a partir de impresiones ni de una única ejecución.

---

## 13. Plan de transición recomendado

### Fase 0 — decisión de gAto

Aprobar o rechazar la dirección task-centric. No cambiar todavía archivos productivos.

### Fase 1 — contrato conceptual

Definir en un documento de investigación:
- entidades mensaje, tarea, evento, artifact y workspace;
- estados mínimos;
- propietario de tarea y de interfaz;
- autoridad de aceptación;
- reglas de privacidad y permisos.

### Fase 2 — piloto sin migración

Aplicar el modelo a un equipo y un proyecto nuevo o acotado. Mantener las carpetas existentes como vistas o referencias de compatibilidad. No borrar archivos históricos.

### Fase 3 — medición

Ejecutar Experimentos A y B. Registrar costo, calidad, duplicación, fallos y aceptación.

### Fase 4 — decisión

Si B mejora el resultado con costo menor o equivalente, formalizar schemas y actualizar moldes con aprobación de gAto. Si no, conservar la estructura local y corregir solo los problemas demostrados.

### Fase 5 — runtime, solo si se justifica

Si la falta de activación, notificaciones o recuperación automática se demuestra como cuello de botella, evaluar A2A + MCP y un workflow engine. No construir un runtime para resolver problemas que una estructura de tareas clara puede resolver documentalmente.

---

## 14. Riesgos e incertidumbres

1. **Sesgo de documentación:** un repositorio puede describir un flujo mejor de lo que realmente se usa.
2. **Sesgo de casos visibles:** los incidentes conservados no representan necesariamente la frecuencia real de errores.
3. **Cambio de modelos:** resultados de coordinación dependen de capacidad del modelo, herramientas y presupuesto.
4. **Concurrencia GitHub:** una estructura documental no garantiza bloqueo, transacción ni entrega exactly-once.
5. **Privacidad:** un espacio compartido puede exponer más información de la necesaria.
6. **Sobrecorrección:** simplificar demasiados directorios puede eliminar señales útiles de procedencia o separación de autoridad.
7. **Burocracia:** convertir cada mensaje en una tarea puede aumentar el costo en vez de reducirlo.
8. **Falsa automatización:** publicar un archivo no equivale a activar un agente.
9. **Evolución de protocolos:** A2A/MCP y frameworks de agentes siguen evolucionando; adoptar versiones sin necesidad puede crear deuda.
10. **Causa raíz del incidente TITAN:** la evidencia disponible no demuestra si el problema principal fue ambigüedad de ruta, sesgo de contexto, ausencia de preflight o una combinación.

---

## 15. Decisiones reservadas a gAto

No tomo ninguna de estas decisiones por cuenta propia:

1. Aprobar o rechazar la arquitectura task-centric.
2. Autorizar un piloto en un proyecto determinado.
3. Aprobar un schema común de tareas, mensajes y eventos.
4. Cambiar moldes, contratos, instrucciones de inicio o directorios.
5. Determinar si la competencia universal se incorpora como requisito normativo.
6. Formalizar la distinción entre coordinación propia y orquestación.
7. Aprobar la transición a A2A/MCP o a un workflow runtime.
8. Autorizar migración o retiro de estructuras históricas.

---

## 16. Conclusión final

La arquitectura actual no está demostrada como un fracaso, pero tampoco está demostrada como un sistema integrado. Hay soluciones locales buenas —el procedimiento de clasificación de Katarina, el task board y la regla single-pass de Auditoría, los logs de Cytryna y el inbox/deliveries/decisions de TITAN— que conviene conservar como evidencia de diseño.

El defecto principal no es “tener muchas carpetas”. Es no tener una definición común y verificable de las entidades que esas carpetas representan. Mensaje, tarea, evento, artifact y workspace se mezclan o se duplican; las rutas no siempre expresan dirección inequívoca; los estados no son universales; y la persistencia documental no garantiza activación ni recepción.

Si diseñara el sistema desde cero, empezaría por un **modelo de tareas y dependencias**, no por un árbol de directorios. Haría que cada integrante se coordine a sí mismo y con sus pares, mientras la orquestación de equipos queda en manos de roles autorizados. Mantendría un único registro de tarea, mensajes vinculados, eventos mínimos y artifacts verificables. Usaría espacios compartidos solo cuando exista una necesidad real de edición o conocimiento común.

No construiría de nuevo say/, shared/, inbox/ y outbox/ como cuatro estructuras obligatorias. Construiría primero las responsabilidades que esas carpetas intentaban representar. Después elegiría las vistas físicas más simples para servirlas.

La recomendación es avanzar hacia la Alternativa B mediante un piloto medido, no mediante una reescritura inmediata. La decisión y la implementación quedan reservadas a gAto.

---

## 17. Bibliografía y fuentes

### Investigación académica y benchmarks

1. Malone, T. W. y Crowston, K. (1994). *The Interdisciplinary Study of Coordination*. ACM Computing Surveys, 26(1), 87–119. https://doi.org/10.1145/174666.174668
2. Hayes-Roth, B. (1985). *A Blackboard Architecture for Control*. Artificial Intelligence, 26(3), 251–321. https://doi.org/10.1016/0004-3702(85)90063-3
3. Salas, E., Sims, D. E. y Burke, C. S. (2005). *Is there a “Big Five” in Teamwork?* Small Group Research, 36(5), 555–599. https://doi.org/10.1177/1046496405277134
4. *The Impact of Cross-Training on Team Effectiveness* (2002). Registro PubMed: https://pubmed.ncbi.nlm.nih.gov/11916213/
5. *Transactive Memory Systems in Context* (2018). Registro PubMed: https://pubmed.ncbi.nlm.nih.gov/30024196/
6. *Measurement Matters: A Meta-Analytic Examination of Transactive Memory Systems and Team Outcomes* (2026). https://doi.org/10.1177/10464964261434540
7. Zhu et al. (2025). *MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents*. ACL 2025. https://aclanthology.org/2025.acl-long.421/
8. Kim et al. (2026). *TeamBench: Evaluating Agent Coordination under Enforced Role Separation*. arXiv:2605.07073. https://arxiv.org/abs/2605.07073
9. Park et al. (2026). *PAC-BENCH: Evaluating Multi-Agent Collaboration under Privacy Constraints*. arXiv:2604.11523. https://arxiv.org/abs/2604.11523
10. Destefanis y Aste (2026). *When Agents Coordinate: Measuring Coordination in Multi-Agent AI Coding*. arXiv:2608.16801. https://arxiv.org/abs/2608.16801
11. Kim, Y. (2026). *When do AI agents benefit from collaboration?* MIT Media Lab. https://www.media.mit.edu/projects/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/overview/
12. Zhu et al. (2026). *LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns*. Future Internet, 18(6), 326. https://doi.org/10.3390/fi18060326
13. Dutta, Goldman y Jennings (2007). *Communicating Effectively in Resource-Constrained Multi-Agent Systems*. IJCAI 2007. https://ijcai.org/proceedings/2007/205

### Protocolos y documentación técnica

14. Agent2Agent Protocol. *Specification*. https://a2a-protocol.org/latest/specification/
15. Model Context Protocol. *Architecture*. https://modelcontextprotocol.io/specification/
16. JADE/FIPA. *JADE Tutorial: FIPA ACL Message Structure*. https://jade.tilab.com/papers/JADETutorialIEEE/JADETutorial_FIPA.pdf
17. Microsoft. *AI Agent Orchestration Patterns*. https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
18. Microsoft AutoGen. *Group Chat* y *Termination*. https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html
19. Akka. *Multi-agent coordination*. https://doc.akka.io/concepts/ai-orchestration-patterns.html
20. Temporal. *Workflows*. https://docs.temporal.io/workflows
21. LangGraph. *Persistence*. https://docs.langchain.com/oss/python/langgraph/persistence
22. AWS. *Event Sourcing Pattern*. https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/event-sourcing-pattern.html

### Evidencia interna principal

- SOFTLY.md, CHECKPOINT.md.
- docs/architecture/coordination-patterns.md.
- docs/architecture/operational-modes-and-autocoordination.md.
- agents/templates/handoff.md y schemas/handoff.schema.json.
- schemas/jsonl-event-schema-proposal.md.
- logs/2026-11-16-incidencia-creacion-katarina-repositorio-equivocado.md.
- observations/OBS-20261116-004-confusion-repositorio-rutas-creacion-katarina-titan.md.
- Katarina/core/CONTRACT.md y Katarina/core/OPERATING-PROCEDURE.md.
- Cytryna/AGENTS.md, Cytryna/coordinator.py, Cytryna/AGENTDEV/policy/WRITE_POLICY.md y LOG_POLICY.md.
- TITAN/eL equipo del gAto/Direccion-Cytryna/CONSTITUCION.md, shared/README.md y reports/06-coordinacion-y-pendientes.md.
- Auditoria/TEAM/COORDINATION.md y TEAM/TASK_BOARD.md.
- Laboratorio-de-agentes/Katarina/Softlysay/structure.md, Katarina/shared/structure.md y Katarina/mancos/shared/structure.md.
