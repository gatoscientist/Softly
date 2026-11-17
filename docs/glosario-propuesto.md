# Glosario propuesto de Softly

- **Repositorio:** `gatoscientist/Softly`
- **Rama de destino:** `main`
- **Versión de referencia:** Softly 1.1.0 (`bridge-to-2.0`)
- **Estado de este documento:** propuesta para contraste; no es una norma aprobada ni modifica contratos.
- **Fecha:** 2026-11-17
- **Propósito:** establecer un vocabulario común para leer y deliberar sobre Softly sin confundir términos vigentes, diseños conceptuales, propuestas y legado histórico.

## 1. Cómo leer este glosario

Las etiquetas indican el estado del uso documentado, no el grado de verdad universal de una definición:

- **[VIGENTE 1.1]**: término utilizado por los documentos normativos/operativos actuales de Softly 1.1.
- **[CONTRACTUAL]**: término definido en una plantilla, contrato o schema aplicable; revisar siempre la fuente canónica y su versión.
- **[DISEÑO]**: concepto descrito en arquitectura o modelo, sin afirmar implementación.
- **[PROPUESTA]**: alternativa o hipótesis que no debe tratarse como decisión aprobada.
- **[OBSERVADO]**: patrón registrado en una interacción; no equivale a capacidad o norma.
- **[HISTÓRICO]**: término conservado en documentos anteriores, snapshots o material clasificado como inactivo.

Cuando dos documentos usen una palabra de forma distinta, este glosario no borra la diferencia: la señala para contraste. La fuente normativa vigente prevalece sobre un documento histórico o una propuesta.

## 2. Identidad, arquitectura y gobierno

### Agente
**[DISEÑO]** Sistema basado en un modelo que recibe instrucciones/contexto, produce respuestas o acciones y puede utilizar herramientas dentro de límites. En Softly, la definición del agente debe separarse de su asignación a un proyecto y de una sesión concreta. No se debe inferir autonomía, permisos o ejecución a partir de que exista un perfil documental.

### Autoridad
**[VIGENTE 1.1]** Facultad legítima para establecer objetivos, límites, prioridades, permisos o decisiones. La autoridad procede de la fuente de gobierno correspondiente, no del nombre de un agente, de una carpeta, de un commit ni de la capacidad técnica de realizar una acción.

### gAto / Dirección humana
**[VIGENTE 1.1]** Identidad canónica de la dirección humana de Softly. gAto conserva la autoridad humana última sobre propósito, prioridades, permisos y cambios de gobierno. Softly coordina dentro de la autoridad delegada; no debe transferir a gAto la carga de dirigir cada paso rutinario.

### Softly
**[VIGENTE 1.1]** Núcleo operativo y generativo que transforma intención humana autorizada en tareas, trabajo coordinado, entregables verificables y evolución gobernada. En la versión 1.1, el núcleo permitido es **Prompting + Contratos + GitHub**. El repositorio conserva memoria documental, pero no es por sí mismo una sesión activa ni despierta agentes por la mera presencia de archivos.

### Repositorio
**[VIGENTE 1.1]** Contenedor Git de archivos, versiones, commits y ramas. Un repositorio puede ser casa canónica de un agente, proyecto anfitrión o archivo de investigación; esas funciones no son intercambiables. Nombrar una ruta sin identificar el repositorio puede producir errores de destino.

### Casa canónica
**[DISEÑO]** Repositorio que contiene la definición y documentación fuente de una identidad/agente. No debe confundirse con el repositorio del proyecto donde esa identidad trabaja ni con un workspace temporal.

### Identidad
**[DISEÑO]** Sujeto estable al que se atribuyen propósito, responsabilidades, autoridad, límites y continuidad documental. Una identidad no es una especialidad, un perfil de capacidad, una carpeta, una asignación ni una sesión.

### Identidad operativa
**[HISTÓRICO / GOBERNANZA RESET]** En RESET-CORE-2026-002 se fijó un conjunto de tres identidades operativas del ecosistema: Softly, Katarina y Audeline. Esta definición pertenece al alcance de esa orden; no convierte cada perfil histórico o paquete en una identidad operativa.

### Paquete
**[VIGENTE 1.1]** Clase física de artefacto operativo que reúne identidad, mandato, contrato, autoridad, permisos, capacidades, procedimiento e interfaz de un agente. La definición de Softly vive en `SOFTLY.md`. Un paquete documental no demuestra que el agente esté desplegado o ejecutándose.

### Perfil
**[CONTRACTUAL]** Descripción funcional de un agente, su dominio, especialidades, capacidades, límites, evaluación y otros atributos. Un perfil es descriptivo; no concede permisos ni demuestra por sí solo competencias.

### Rol
**[DISEÑO]** Función que una identidad o participante cumple dentro de un trabajo o proyecto, por ejemplo investigación, ingeniería, auditoría o coordinación. El rol no sustituye la identidad ni concede autoridad automáticamente.

### Taxonomía
**[CONTRACTUAL / HISTÓRICO SEGÚN REGISTRO]** Clasificación profesional o funcional usada para ordenar agentes por familia. La taxonomía inicial de Softly contiene AgentDEV, AgentSEC, AgentMUS, AgentSCI y Auditoría. Clasificar no acredita competencia ni concede permisos. El registro 1.0.0 es histórico; consultar el estado del registro aplicable antes de usarlo como catálogo operativo.

### Dominio
**[CONTRACTUAL]** Área profesional o temática concreta en la que se sitúa el trabajo de un agente. Debe distinguirse de la taxonomía, la especialidad y la competencia.

### Especialidad
**[CONTRACTUAL]** Subárea de dominio en la que se concentra el trabajo. Una especialidad declarada no demuestra automáticamente que la competencia esté probada.

### Competencia
**[CONTRACTUAL]** Capacidad concreta para realizar una actividad o producir un resultado. En el modelo de definición portable puede clasificarse como declarada, demostrada o pendiente. La etiqueta de taxonomía no constituye evidencia de competencia.

### No-herencia por defecto
**[VIGENTE COMO REGLA DOCUMENTAL]** Regla según la cual competencias, permisos, herramientas y certificaciones no se heredan por taxonomía, jerarquía, proyecto, parentesco o procedencia. Toda derivación debe justificar dominio, competencia, motivo, evidencia y alcance.

### Derivación entre pares
**[CONTRACTUAL]** Transferencia o recomendación de un encargo a otro agente por correspondencia de dominio y competencia. Debe declarar agente origen/destino, competencia requerida, razón y evidencia. No transfiere autoridad ni permisos.

### Capacidad
**[DISEÑO]** Aptitud o función que una identidad puede ejercer. Debe distinguirse entre capacidad propuesta, declarada, demostrada y autorizada. Que una capacidad aparezca en un documento no prueba que esté disponible en la sesión actual.

### Permiso declarado
**[DISEÑO]** Permiso descrito en un contrato o perfil. Es una afirmación documental, no un control técnico.

### Permiso efectivo
**[DISEÑO]** Acceso realmente concedido y aplicado por el entorno, herramienta o mecanismo de control. No se deduce de un prompt, schema, nombre de rol ni documento.

### Disponibilidad
**[CONTRACTUAL / HISTÓRICO]** Estado que indica si una definición o recurso está disponible para asignación. No debe confundirse con una sesión activa, una instancia ejecutándose o una competencia validada.

### Active Standby
**[HISTÓRICO]** Etiqueta de disponibilidad usada en el registro taxonómico inicial. Significa disponibilidad declarada para una posible asignación; no significa ejecución en segundo plano, proceso vivo, endpoint conectado ni aceptación de una tarea. No usar como sinónimo de “activo” en Softly 1.1.

### Estado de madurez
**[DISEÑO]** Progresión documental/experimental de una definición: Propuesto → Diseñado → Prototipado → Probado → Validado → Operativo. Cada transición exige evidencia apropiada. No confundir madurez del paquete con estado de una asignación o tarea.

### Asignación
**[DISEÑO]** Vínculo contextual entre una definición/version específica y un proyecto/brief. Resuelve responsabilidad, entregables, contexto, herramientas, permisos efectivos, presupuesto, supervisión y condiciones de cierre. Una asignación no debe ampliar permisos globales.

### Sesión de trabajo
**[DISEÑO]** Unidad temporal en la que una instancia realiza una actividad bajo una asignación y contexto concretos. Registra objetivo inmediato, estado, tareas, decisiones, resultados, errores y referencias. No redefine la identidad del agente.

### Agent Definition
**[DISEÑO]** Definición portable y versionada de un agente: identidad, misión, responsabilidades, competencias, instrucciones, herramientas requeridas, política de memoria, autonomía, seguridad y evaluación.

### Project Brief
**[DISEÑO]** Solicitud declarativa de incorporación o trabajo en un proyecto. Describe objetivo, resultado, alcance, exclusiones, fuentes, capacidades requeridas, herramientas, permisos solicitados, coordinación y aceptación. No crea un agente ni concede permisos por sí mismo.

### Project Assignment
**[DISEÑO]** Configuración concreta que vincula una definición de agente con un proyecto y brief, resolviendo contexto, permisos, herramientas, supervisión y entregables.

### Work Session
**[DISEÑO]** Sesión temporal de trabajo de una asignación. No es la identidad ni el paquete del agente.

### Cápsula Directora
**[VIGENTE 1.1]** Organización interna de especialistas que Katarina puede usar como lentes cognitivos o subcontratos dentro de su propia sesión. No son identidades operativas externas: no tienen repositorios, buzones, permisos independientes, commits propios ni autoridad de aceptación. Katarina conserva integración y responsabilidad final.

### AgenteDIR / AgentDIR
**[PROPUESTA / HISTÓRICO DE INVESTIGACIÓN]** Nombre utilizado en material de investigación para referirse a un rol de dirección/coordinación de equipos. No aparece como taxonomía oficial vigente ni crea una identidad autorizada. En Softly 1.1 la orquestación es una dimensión de coordinación, no una nueva identidad por el mero uso de esta etiqueta.

## 3. Arquitectura y coordinación

### Núcleo Prompting + Contratos + GitHub
**[VIGENTE 1.1]** Sustrato documental/operativo declarado para Softly 1.1. Prompting aporta instrucciones; los contratos definen estructuras, responsabilidades e interfaces; GitHub conserva artefactos y trazabilidad. No presupone un runtime.

### Plano
**[VIGENTE 1.1]** Distinción lógica para razonar sobre la arquitectura. Softly 1.1 distingue tres planos: **Definición** (identidad, propósito, autoridad, capacidades, permisos y contratos), **Coordinación** (tareas, responsables, dependencias, estados e interfaces) y **Ejecución** (trabajo realizado y producción de resultados verificables). Los planos no obligan a crear directorios, servicios o subsistemas físicos.

### Dimensión de coordinación
**[VIGENTE 1.1]** Perspectiva funcional desde la que se organiza el trabajo. Las tres dimensiones son:
- **Coordinación propia:** una instancia organiza su propio trabajo, contexto, estado y dependencias dentro de su autoridad.
- **Coordinación entre pares:** participantes gestionan interfaces y dependencias horizontales bajo contratos compatibles.
- **Orquestación:** un rol con autoridad distribuye, prioriza, secuencia e integra trabajo.

### Coordinación sistémica
**[VIGENTE 1.1]** Responsabilidad transversal de preservar coherencia entre tareas, contratos, permisos, interfaces, dependencias y evolución del ecosistema. En Softly 1.1 es explícita, pero no constituye una cuarta dimensión.

### Orquestación
**[VIGENTE 1.1]** Dimensión de coordinación en que un rol autorizado organiza trabajo distribuido, asigna responsables, ordena tareas, gestiona dependencias, integra resultados y escala bloqueos dentro de su mandato. No reemplaza la responsabilidad del owner por su propio resultado.

### Task-centric / Coordinación centrada en tareas
**[VIGENTE 1.1]** Modelo en que la tarea es la unidad canónica de coordinación. La tarea concentra objetivo, responsable, estado, dependencias, entradas, restricciones, entregable, evidencia, aceptación y siguiente acción. Mensajes, eventos y artefactos se vinculan a la tarea cuando corresponde, pero no la sustituyen.

### Tarea
**[VIGENTE 1.1]** Unidad canónica de trabajo y coordinación: define resultado esperado, responsable único, autoridad, prioridad, estado, dependencias, contexto, restricciones, entregable y criterios verificables de aceptación. Los cambios de responsable, estado o prioridad se registran en la propia tarea y en el historial Git.

### Owner / Responsable único
**[CONTRACTUAL]** Participante que responde por el resultado de una tarea en su estado actual. Una tarea tiene un responsable único por estado; el owner no es necesariamente quien acepta el resultado ni quien posee autoridad estratégica.

### Aceptación
**[CONTRACTUAL]** Decisión de que un entregable o resultado cumple criterios verificables. Debe identificar criterios, responsable/autoridad de aceptación, decisión y fecha. Entregado no equivale a aceptado.

### Bloqueo
**[CONTRACTUAL]** Condición concreta que impide avanzar una tarea. Debe describirse con causa y, cuando corresponda, responsable de resolución. Retirar un bloqueo no cambia automáticamente el estado de la tarea.

### Dependencia
**[CONTRACTUAL]** Relación por la que una tarea necesita el resultado o condición de otra. La tarea no está lista si una dependencia obligatoria sigue abierta. Un schema puede declarar referencias, pero no necesariamente verificar existencia o ciclos entre tareas.

### Handoff
**[HISTÓRICO / CONCEPTO AUXILIAR]** Transferencia estructurada de contexto, resultado y siguiente acción entre participantes. En Softly 1.1 no es una quinta clase física de artefacto ni requiere un buzón o archivo por separado: la asignación, transferencia, bloqueo, entrega y aceptación se expresan en el ciclo de vida de la tarea y/o en el entregable. Publicar un handoff no demuestra recepción ni activa una sesión.

### Inbox / Outbox
**[VIGENTE 1.1]** Vistas lógicas derivadas de responsable, autoría y estado. No son buzones físicos ni directorios direccionales obligatorios. La presencia de un archivo en una ruta llamada inbox no demuestra recepción.

### Mensaje
**[DISEÑO / PROPUESTA]** Comunicación de un emisor a uno o más destinatarios, con tipo, fecha, contenido y referencia a tarea cuando corresponda. En la investigación de coordinación se considera una entidad conceptual, pero no una clase física operativa canónica de Softly 1.1.

### Evento
**[DISEÑO]** Registro de un cambio o hecho con actor, acción, timestamp, entidad afectada y evidencia. Un evento informa que algo ocurrió; no equivale por sí mismo a una tarea ni a una orden. La propuesta de schema JSONL está congelada y no es normativa.

### Artifact / Artefacto
**[DISEÑO]** Término genérico para un resultado persistente, archivo, referencia o producto de trabajo. No equivale automáticamente a un mensaje ni a una tarea. En Softly 1.1, la clase física oficial de resultado de una tarea es el **Entregable**.

### Entregable
**[VIGENTE 1.1]** Resultado producido por una tarea, con evidencia, verificaciones, referencias, limitaciones y estado de aceptación. Puede incluir o enlazar archivos, rutas, cambios y commits. La existencia del archivo no certifica su calidad.

### Checkpoint
**[VIGENTE 1.1]** Síntesis breve del estado vigente, acuerdos activos, tareas/bloqueos relevantes y próxima acción habilitada. Es un índice operativo compacto, no una bitácora ni un resumen cronológico. Debe reemplazar estado obsoleto en vez de acumular historia.

### Workspace
**[DISEÑO / PROPUESTA]** Espacio de trabajo o recursos que uno o más participantes necesitan utilizar. La investigación de coordinación lo considera una entidad conceptual distinta de tarea, mensaje, evento y artefacto. No es una de las cuatro clases físicas operativas de Softly 1.1; debe existir solo cuando haya una necesidad real de recurso compartido.

### Señal estigmérgica
**[VIGENTE 1.1]** Señal persistente en el entorno compartido (GitHub en Softly) que permite a otros participantes reconocer qué representa, su estado, quién responde y qué acción habilita. La señal coordina indirectamente mediante el entorno; no notifica ni activa automáticamente a otra sesión.

### Estigmergia
**[VIGENTE 1.1 / CONCEPTO]** Coordinación indirecta mediada por señales o trazas persistentes en un entorno compartido. En Softly 1.1, GitHub actúa como superficie de señales estigmérgicas. La señal debe ser interpretable y conservar estado, responsable y acción habilitada.

### Plano de coordinación documental
**[DISEÑO]** Parte del modelo que conserva tareas, responsables, dependencias, estados, interfaces y coherencia mediante artefactos persistentes. No debe confundirse con una ejecución automática de workflow.

### Modo operativo
**[VIGENTE 1.1]** Selección de la forma de trabajo según el encargo de gAto; no es personalidad, permiso ni proceso runtime. Softly 1.1 define Fábrica/Entrega Directa, Coordinación/Orquestación e Investigación/Deliberación.

### Fábrica / Entrega Directa
**[VIGENTE 1.1]** Modo predeterminado para producir o modificar directamente un artefacto autorizado. Aplica el molde y la auto-revisión durante la producción; entrega el resultado verificable sin convertir investigación o pruebas no solicitadas en requisitos previos.

### Coordinación / Orquestación (modo)
**[VIGENTE 1.1]** Modo para preparar briefs, organizar asignaciones, resolver dependencias, coordinar responsables y emitir transferencias accionables dentro de la autoridad concedida. No debe confundirse con la dimensión de orquestación: uno es modo de trabajo; la otra, dimensión funcional.

### Investigación / Deliberación
**[VIGENTE 1.1]** Modo que se activa cuando gAto pide investigar, teorizar, analizar evidencia o diseñar experimentos. No es etapa obligatoria previa a una entrega concreta.

### Modo Laboratorio / Modo Diseño / Modo Creación de Agentes
**[OBSERVADO / HISTÓRICO]** Nombres usados en interacciones anteriores y registrados como fenómenos emergentes. No fueron formalizados como modos normativos en el registro de observación citado. No deben confundirse con los tres modos vigentes de Softly 1.1.

### Cápsula de contexto
**[DISEÑO]** Conjunto de información seleccionada para una tarea/sesión. La selección debe respetar propósito, alcance, procedencia, permisos y minimización; no debe cargar historia completa por defecto.

## 4. Conocimiento, evidencia y memoria

### Entidad
**[DISEÑO]** Instancia identificable sobre la que se puede hablar, como un agente, proyecto, organización, modelo, herramienta o experimento. No es su categoría ni una afirmación acerca de ella.

### Concepto
**[DISEÑO]** Idea, categoría, propiedad o definición usada para organizar e interpretar entidades y afirmaciones. “Memoria” es un concepto; una memoria concreta de un proyecto puede ser una entidad o componente.

### Fuente
**[CONTRACTUAL]** Artefacto original o referencia de origen de la que se obtiene información: documento, publicación, repositorio, mensaje autorizado, evento, traza, medición, imagen o dataset. La fuente no es automáticamente verdadera ni confiable.

### Registro
**[DISEÑO]** Representación persistente de una fuente, evento, afirmación u otro objeto con metadatos, estado y procedencia. Debe distinguirse el original de sus extractos y derivados.

### Afirmación / Claim
**[DISEÑO]** Proposición delimitada acerca de entidades, conceptos, actividades o relaciones. Debe expresar su tipo epistemológico, alcance y evidencia disponible.

### Tipo epistemológico
**[DISEÑO]** Categoría que describe qué clase de afirmación se está formulando:
- **FACT:** afirmación respaldada directamente por evidencia verificable.
- **OBSERVATION:** descripción de algo observado en un contexto/ejecución.
- **INFERENCE:** interpretación derivada de observaciones o evidencia.
- **HYPOTHESIS:** explicación provisional que requiere prueba.
- **RESULT:** resultado registrado de una actividad/experimento.
- **DECISION:** elección adoptada con alcance y rationale.
- **RECOMMENDATION:** propuesta todavía no adoptada.

El tipo epistemológico no es lo mismo que confianza ni estado de evaluación.

### Estado de evaluación
**[DISEÑO]** Estado del soporte de una afirmación: unassessed, supported, contested, inconclusive o rejected en la propuesta de modelo de datos. No debe confundirse con el tipo epistemológico.

### Confianza
**[DISEÑO]** Estimación explícita de cuán sólida se considera una afirmación. No reemplaza la evidencia ni el estado de evaluación. No asignar porcentajes sin un método definido.

### Síntesis
**[DISEÑO]** Vista condensada y versionada que agrupa afirmaciones para responder una pregunta o describir un tema. Debe explicitar propósito, cobertura, limitaciones, incertidumbre y vigencia, y permitir llegar a afirmaciones y fuentes originales. No sustituye la evidencia primaria.

### Recuperación escalonada
**[DISEÑO]** Estrategia de consulta que comienza por la síntesis pertinente, abre las afirmaciones asociadas y recupera fuentes originales cuando la tarea lo requiere. Evita cargar historia completa por rutina sin perder trazabilidad.

### Memoria
**[DISEÑO]** Información persistente utilizable para continuidad o conocimiento. No debe tratarse como un almacén indiferenciado: el repositorio distingue historial, estado de sesión, conocimiento, contexto y procedimientos. La política de memoria debe indicar scope, procedencia, acceso, retención y uso.

### Memoria episódica
**[DISEÑO / FUENTE EXTERNA REGISTRADA]** Memoria de episodios o experiencias concretas. En Softly aparece como categoría de investigación, no como subsistema implementado.

### Memoria semántica
**[DISEÑO / FUENTE EXTERNA REGISTRADA]** Conocimiento generalizado sobre conceptos, entidades y relaciones. No equivale al historial literal de conversaciones.

### Memoria procedural
**[DISEÑO / FUENTE EXTERNA REGISTRADA]** Conocimiento sobre cómo ejecutar procedimientos o métodos. Debe distinguirse de datos episódicos y hechos del dominio.

### Contexto
**[DISEÑO]** Información y condiciones que delimitan la interpretación, validez o acceso a un trabajo. Incluye proyecto, universo, entorno, periodo, versión, condiciones experimentales y finalidad.

### Universo
**[DISEÑO]** Ámbito de pertenencia y autorización que agrupa identidades, proyectos o registros. Softly, DEVAGENTS y TITAN aparecen como universos que deben mantenerse diferenciados en el modelo general. Compartir tema no concede acceso entre universos.

### Namespace
**[DISEÑO]** Espacio de nombres que separa identificadores, memoria o registros para evitar colisiones y controlar alcance. Un ID externo no reemplaza el ID interno del sistema.

### Procedencia
**[CONTRACTUAL]** Información que permite reconstruir de dónde viene un registro, quién/qué lo incorporó, cuándo se capturó y qué transformación se aplicó. Procedencia no demuestra por sí sola que el contenido sea verdadero.

### Vigencia
**[DISEÑO]** Periodo o estado durante el cual una afirmación, documento o síntesis se considera aplicable. Debe distinguirse de fecha de creación, actualización o captura.

### Obsolescencia
**[DISEÑO]** Condición en que un registro o síntesis ya no representa el estado aplicable por nueva evidencia, cambio de alcance o reemplazo. La obsolescencia no exige borrar la historia.

### Fuente primaria
**[MÉTODO DE INVESTIGACIÓN]** Fuente original más cercana al hecho o especificación que se intenta verificar. Debe abrirse y leerse directamente cuando una afirmación importante depende de ella; un snippet de buscador no equivale a lectura completa.

### Evidencia
**[CONTRACTUAL]** Material verificable que respalda, contradice o matiza una afirmación o resultado: fuente, sección, archivo, commit, prueba, traza o medición. Una declaración de que se hizo algo no sustituye la evidencia observable.

### Integridad
**[DISEÑO]** Propiedad de que un artefacto o registro conserve su contenido esperado y que las alteraciones puedan detectarse según controles definidos. Una ruta existente o un hash aislado no demuestran todas las propiedades de seguridad.

### Trazabilidad
**[VIGENTE 1.1]** Capacidad documental para seguir la relación entre encargo, responsable, fuentes, tarea, entregable, verificaciones, decisiones y commits. Git aporta historial; no demuestra por sí solo recepción, aceptación ni calidad.

### Checkpoint vs. historial
**[VIGENTE 1.1]** El checkpoint resume el estado necesario para continuar; el historial conserva la secuencia de hechos. Uno no reemplaza al otro.

## 5. Investigación, experimentación y evaluación

### Investigación
**[VIGENTE 1.1]** Actividad solicitada explícitamente para examinar fuentes, evidencia, alternativas o preguntas. Debe separar lo que dice la fuente de la interpretación de Softly.

### Actividad
**[DISEÑO]** Proceso delimitado que consume información y puede producir registros, afirmaciones, resultados o síntesis: investigación, experimento, evaluación, auditoría, desarrollo, revisión o sesión de observación. Diseñar una actividad no significa ejecutarla.

### Hipótesis
**[MÉTODO DE INVESTIGACIÓN]** Explicación provisional que requiere contraste. Debe ser lo bastante concreta como para identificar qué evidencia podría apoyarla o refutarla.

### Experimento
**[MÉTODO DE INVESTIGACIÓN]** Procedimiento reproducible que contrasta una hipótesis o compara alternativas bajo condiciones y criterios definidos antes de observar resultados. Un protocolo diseñado no equivale a un experimento ejecutado.

### Baseline
**[DISEÑO / EVALUACIÓN]** Solución de referencia con la que se compara una alternativa. En coordinación, el repositorio recomienda comparar multiagente con single-agent + tools y workflows deterministas cuando sea viable.

### Evaluación
**[MÉTODO DE INVESTIGACIÓN]** Medición sistemática de desempeño, seguridad, fiabilidad, eficiencia o calidad frente a criterios predefinidos. No basta con que una respuesta “suene bien”.

### Dataset
**[EVALUACIÓN]** Conjunto versionado de casos/datos que se utiliza para ejecutar una evaluación. Debe conservar procedencia, criterios y límites de uso; usar datos sintéticos o anonimizados cuando corresponda.

### Métrica
**[EVALUACIÓN]** Medida operacional asociada a una dimensión de desempeño. Debe definirse antes de observar resultados y no reemplaza la interpretación cualitativa ni las métricas complementarias.

### Observación
**[OBSERVADO / MÉTODO]** Registro de un comportamiento visible en un contexto concreto. No demuestra por sí solo defecto, repetibilidad ni causa.

### Auditoría independiente
**[DISEÑO / GOBERNANZA]** Revisión realizada por una función distinta de quien produjo el objeto auditado, con alcance, evidencia y criterio propios. La independencia exige evitar que el mismo responsable sea la única fuente de validación de su trabajo.

### Revisión de fuente
**[MÉTODO DE INVESTIGACIÓN]** Evaluación de procedencia, autoridad, actualidad, método, evidencia, limitaciones, sesgos e intereses de una fuente. No debe confundirse con resumir su contenido.

### Resultado
**[MÉTODO DE INVESTIGACIÓN]** Salida observada de una actividad o experimento, con datos, casos, condiciones y limitaciones. No se puede declarar un resultado ejecutado si solo existe un protocolo.

### Calibración epistemológica
**[MÉTODO DE INVESTIGACIÓN]** Disciplina para marcar afirmaciones como verificadas, corroboradas, plausibles, hipótesis, disputadas, refutadas o no evaluadas. No asignar porcentajes de confianza sin método.

## 6. Seguridad y límites técnicos

### Límite de confianza
**[DISEÑO DE SEGURIDAD]** Frontera entre componentes o actores con diferentes niveles de confianza: usuario/sistema, modelo/runtime, instrucciones/contenido recuperado, agente/herramienta, coordinador/delegado, sesión/memoria y sistema/proveedor externo.

### Prompt injection
**[SEGURIDAD]** Intento de introducir instrucciones maliciosas o no autorizadas en entradas directas o contenido recuperado para desviar el comportamiento del agente. El contenido recuperado debe tratarse como dato, no como instrucción superior.

### Goal hijacking
**[SEGURIDAD]** Desvío del objetivo autorizado hacia otro objetivo introducido por una fuente, mensaje o contexto no autorizado.

### Memory / Context poisoning
**[SEGURIDAD]** Contaminación de memoria o contexto con datos/instrucciones falsos, maliciosos, descontextualizados o de procedencia no confiable que pueden influir en decisiones posteriores.

### Abuso de herramientas
**[SEGURIDAD]** Uso de una herramienta fuera de su finalidad, alcance, permisos o parámetros autorizados. La declaración de permisos en el prompt no sustituye validación y enforcement externo.

### Mínimo privilegio
**[SEGURIDAD]** Conceder solo los permisos necesarios para una tarea, proyecto y periodo concretos. Separar lectura, escritura y ejecución; revocar accesos temporales al cerrar la asignación.

### Sandbox
**[DISEÑO DE SEGURIDAD]** Entorno de ejecución confinado que limita recursos y efectos de una operación. Una carpeta separada o un contrato Markdown no constituyen por sí solos un sandbox.

### Allowlist
**[DISEÑO DE SEGURIDAD]** Lista explícita de rutas, herramientas, dominios o acciones permitidas. Debe aplicarse mediante controles efectivos, no solo declararse.

### Guardrails
**[DISEÑO]** Políticas o controles que restringen entradas, salidas o acciones. Cuando se habla de controles de seguridad, debe precisarse si son instrucciones del modelo o enforcement externo.

### Runtime
**[HISTÓRICO / EXCLUIDO EN SOFTLY 1.1]** Entorno o componente que ejecutaría operaciones, impondría permisos, administraría estado y manejaría errores. Aunque aparece en diseños y experimentos anteriores, SOFTLY.md 1.1 lo excluye expresamente de la arquitectura y lo deja fuera de norma. No diseñar, implementar, invocar, probar ni desplegar Runtime como parte del modelo Softly 1.1.

### Harness
**[DISEÑO / HISTÓRICO]** Capa que envuelve al modelo y organiza su ciclo de interacción, herramientas, estado y manejo de errores. Aparece en el modelo general y fuentes externas; no es un componente implementado ni permitido por el núcleo Softly 1.1.

### Idempotencia
**[DISEÑO]** Propiedad por la que repetir una misma solicitud/evento no produce efectos duplicados no deseados. La plantilla de handoff histórica exige que un evento repetido con el mismo `event_id` no dispare una segunda ejecución; esa regla no demuestra que exista enforcement en Softly 1.1.

### Replay
**[SEGURIDAD / HISTÓRICO]** Repetición de un mensaje o evento previamente válido para intentar reproducir su efecto. Se mitiga con identidad de evento, vigencia, nonce/estado consumible y controles adecuados; no se declara implementado en Softly 1.1.

### Lease
**[HISTÓRICO / DISEÑO TÉCNICO]** Concesión temporal y acotada de una capacidad o recurso, con identificador y expiración. Aparece en antecedentes de Runtime Mini y diseños de TITAN; no forma parte del núcleo operativo Softly 1.1.

### Ledger
**[HISTÓRICO / DISEÑO TÉCNICO]** Registro secuencial de eventos, en algunos diseños encadenado mediante hashes para detectar alteraciones. El ledger de Runtime Mini pertenece a antecedentes experimentales fuera de la arquitectura vigente de Softly 1.1.

### Hash
**[SEGURIDAD / INTEGRIDAD]** Huella calculada sobre datos para comparar contenido o detectar cambios. Un hash no autentica por sí solo al autor, no prueba autorización y no impide que alguien con control suficiente reescriba datos y hashes.

### Firma digital
**[SEGURIDAD]** Mecanismo criptográfico que vincula un contenido con una clave privada y permite verificar autenticidad/integridad bajo un modelo de confianza. No debe confundirse con un hash simple.

### TOCTOU
**[SEGURIDAD]** “Time of check to time of use”: condición de carrera en que un recurso cambia entre la comprobación de seguridad y su uso. Aparece en antecedentes de seguridad de Runtime; no es un componente del núcleo Softly 1.1.

### Retención
**[GOBERNANZA DE DATOS]** Periodo y condiciones bajo los que se conserva información. Debe especificar finalidad, responsable, sensibilidad, acceso, expiración y tratamiento histórico. Retirar algo del contexto activo no implica destruir su evidencia.

## 7. Ciclo de vida documental e identificadores

### Versión
**[VIGENTE 1.1]** Identificador legible de una revisión de un paquete o documento. Una versión nueva debe conservar la genealogía y explicar el cambio; no se reemplaza silenciosamente una versión histórica.

### Commit
**[VIGENTE 1.1]** Registro Git de un conjunto de cambios con identificador SHA y relación con commits anteriores. Aporta trazabilidad del contenido persistido; no demuestra por sí solo que otro agente lo haya leído o aceptado.

### Rama
**[GIT]** Línea de desarrollo que referencia una secuencia de commits. La existencia de una rama no convierte su contenido en estado canónico.

### Pull Request (PR)
**[GIT]** Solicitud de integración/revisión de cambios entre ramas. Un PR abierto, cerrado o fusionado debe clasificarse por su estado real; su existencia no equivale a aceptación técnica.

### Fuente SRC
**[CONTRACTUAL]** Identificador de ficha de fuente con patrón `SRC-YYYYMMDD-NNN`. La ficha registra título, autor/organización, URL, fechas, tipo, afirmaciones, limitaciones y estado.

### Conjunto SRCSET
**[HISTÓRICO / CONVENCIÓN DE INVESTIGACIÓN]** Identificador usado para un conjunto curado de fuentes, como el panorama inicial. No sustituye las fichas individuales SRC.

### Ingesta ING
**[PROPUESTA CONGELADA]** Identificador propuesto para un evento de recepción/incorporación de fuentes. No es namespace normativo aprobado.

### Síntesis SYN
**[CONVENCIÓN DE INVESTIGACIÓN]** Identificador de síntesis temática con patrón `SYN-YYYYMMDD-NNN`. Una síntesis debe enlazar las fuentes/afirmaciones que la sustentan y declarar alcance y límites.

### Decisión ADR
**[CONTRACTUAL]** Registro de decisión de arquitectura con contexto, opciones, evidencia, decisión, rationale, consecuencias, riesgos y condición de revisión. Una decisión reemplazada se enlaza con su sucesora; no se reescribe como si siempre hubiera sido así.

### Evento EVT
**[PROPUESTA CONGELADA]** Namespace sugerido para eventos de actividad (`EVT-YYYYMMDD-NNN`). La propuesta de schema JSONL está congelada y no normativa.

### Experimento EXP
**[MÉTODO DE INVESTIGACIÓN]** Identificador de protocolo experimental con patrón `EXP-YYYYMMDD-NNN`. El protocolo define hipótesis, baseline, configuración, casos, variables, criterios, límites y análisis.

### Evaluación EVAL / Ejecución RUN
**[EVALUACIÓN]** IDs propuestos por la estructura de evaluación: `EVAL-YYYYMMDD-NNN` para planes y `RUN-YYYYMMDD-NNN` para ejecuciones. Los directorios actuales contienen solo índices de preparación, no datasets, planes o ejecuciones registrados.

### Entregable DEL
**[CONTRACTUAL]** La plantilla de Entregable usa IDs con patrón ilustrativo `DEL-AAAA-NNN`. No confundir con un ID de tarea.

### ID estable
**[DISEÑO]** Identificador que no cambia durante la vida lógica del objeto y no se recicla. El nombre, título, ruta o rol no deben usarse como sustitutos del ID.

### version_id
**[PROPUESTA DE MODELO DE DATOS]** Identificador único de una revisión específica, distinto del ID estable del objeto y del número de versión legible. La propuesta v0.1 aún no es contrato físico implementado.

## 8. Distinciones que no se deben colapsar

| No confundir | Diferencia |
|---|---|
| Identidad / paquete / perfil | La identidad es el sujeto; el paquete reúne su contrato; el perfil describe características. |
| Dominio / especialidad / competencia | Área general; subárea; capacidad concreta demostrable. |
| Competencia / permiso | Saber hacer algo no significa estar autorizado a hacerlo. |
| Permiso declarado / efectivo | Texto documental versus acceso realmente aplicado. |
| Disponibilidad / activación | Estar disponible para asignación no significa estar ejecutándose. |
| Definición / asignación / sesión | Qué es el agente; dónde y con qué permisos trabaja; qué hace ahora. |
| Modo / personalidad / permiso | El modo organiza el trabajo; no cambia identidad ni concede autoridad. |
| Plano / dimensión | El plano distingue capas lógicas; la dimensión describe forma de coordinación. |
| Coordinación sistémica / cuarta dimensión | La primera es transversal; en Softly 1.1 no es cuarta dimensión. |
| Tarea / mensaje / evento / entregable | Resultado de trabajo; comunicación; cambio registrado; producto verificable. |
| Entregable / aceptación | Producir no significa que el resultado haya sido aceptado. |
| Handoff / sesión | Transferir contexto no inicia una sesión automáticamente. |
| Archivo persistido / recepción | Publicar un archivo no demuestra que el destinatario lo haya leído. |
| Síntesis / fuente | La síntesis condensa; la fuente conserva el origen probatorio. |
| Afirmación / tipo epistemológico / confianza | Proposición; clase de proposición; grado de soporte estimado. |
| Evidencia / procedencia | El material que respalda; el rastro de origen y transformación. |
| Hash / firma / autorización | Huella; autenticación criptográfica; permiso para actuar. |
| Runtime / Prompting + Contratos + GitHub | Runtime pertenece a antecedentes; el núcleo Softly 1.1 lo excluye. |
| Artefacto conceptual / clase física | Una entidad conceptual no obliga a crear un archivo o directorio. |
| Checkpoint / bitácora | Estado breve para continuar; registro histórico de eventos. |
| Adaptación contextual / modificación propia | Ajuste de respuesta durante una interacción; cambio persistente verificable de instrucciones/configuración/código. |

## 9. Términos de versiones anteriores y cautelas

1. **Runtime Mini, ADR-0002/0003, leases y ledger:** conservar como historia de experimentación. No describen el núcleo vigente de Softly 1.1, que excluye Runtime.
2. **Laboratorio/Fábrica como conmutador anterior:** el ejemplo `operating-mode-state.example.json` conserva `laboratory/factory`; no debe prevalecer sobre los tres modos normativos de Softly 1.1.
3. **Handoffs físicos, inbox/outbox y directorios `*say/`:** son convenciones anteriores. Softly 1.1 conserva vistas lógicas y expresa la coordinación en tarea, entregable, paquete y checkpoint.
4. **Registro taxonómico 1.0.0 y Active Standby:** fuente histórica; no usar sus etiquetas como prueba de identidades activas ni competencias.
5. **Mensajes, eventos, artifacts y workspaces:** son entidades conceptuales útiles para investigación; no se suman a las cuatro clases físicas operativas de Softly 1.1.
6. **AgentDIR y modos emergentes:** aparecen en investigación/observaciones, no como taxonomía o modo normativo aprobado.
7. **Propuestas congeladas:** `research/identifier-registry-proposal.md`, `schemas/jsonl-event-schema-proposal.md` y `docs/security/git-governance-proposal.md` no deben activarse por el solo hecho de aparecer en el repositorio.

## 10. Ambigüedades y puntos para contraste con Softly

Estos puntos requieren una segunda lectura/decisión conjunta antes de convertir el glosario en norma:

1. **Tarea y estados:** `contracts/tarea.md` usa estados más detallados que `schemas/task.schema.json`. Confirmar si el schema es legado, auxiliar o necesita reconciliación futura. Este glosario no elige por inferencia.
2. **Handoff:** hay una plantilla y schema históricos todavía presentes, pero el contrato Softly 1.1 evita la clase física independiente. Acordar si el término se conserva solo como operación conceptual de transferencia o si alguna referencia debe actualizarse.
3. **Registro de taxonomía:** el README referencia el registro inicial 1.0.0, mientras la documentación de RESET menciona un modelo v2 y su estado de revisión. Confirmar qué archivos son referencia histórica, no normativa o canónica a la fecha de contraste.
4. **Modos:** el JSON de estado de modo conserva `laboratory/factory`, mientras SOFTLY.md 1.1 define tres modos. Marcar el ejemplo como histórico/obsoleto o actualizarlo solo mediante decisión.
5. **AgenteDIR:** precisar si es solo una etiqueta de investigación para una función/rol o si debe desaparecer del vocabulario de diseño.
6. **Cápsula Directora:** confirmar si el nombre se conserva como término oficial de la interfaz Softly–Katarina o si se prefiere otro término.
7. **Runtime/Harness:** mantener claramente la frontera entre el modelo general de agentes, los antecedentes técnicos y la exclusión normativa de Runtime en Softly 1.1.
8. **Estigmergia:** precisar qué clases de señales se consideran operativas y qué condiciones mínimas de estado, responsable, vigencia y acción habilitada se exigirán, sin inventar mecanismos de notificación.
9. **Vigencia/expiración/archivo:** distinguir señal vencida, reemplazada, invalidada y archivada. El retiro de la superficie activa no debe confundirse con destrucción de evidencia.
10. **Modelo de conocimiento:** las siete familias conceptuales están documentadas, pero el modelo de datos v0.1 sigue siendo propuesta. No describir almacenamiento o recuperación como implementación existente.

## 11. Fuentes internas principales

El glosario se construyó a partir de la lectura del árbol completo de `gatoscientist/Softly` en `main` (202 archivos, sin truncamiento del árbol) y de sus documentos de referencia principales:

- `README.md`, `SOFTLY.md`, `CHECKPOINT.md`.
- `contracts/README.md` y las plantillas `paquete.md`, `tarea.md`, `entregable.md`, `checkpoint.md`.
- `docs/operating-model.md`, `docs/architecture/*`, `docs/agent-delivery-checklist.md`, `docs/research-method.md`.
- `agents/README.md`, perfiles y plantillas de agente.
- `schemas/*`, registros y propuestas de esquema.
- `docs/governance/*`, `docs/security/*`, `docs/universal-capabilities-migration-2026-11-16.md`.
- `research/README.md`, bibliografía, fuentes, notas, coordinación y síntesis.
- `observations/*`, índices de `logs/*`, archivo histórico y documentación de experimentos/evaluaciones.

**Límite de cobertura:** el árbol se enumeró completo y se leyeron las fuentes normativas, contratos, schemas, índices y documentos de investigación/seguridad pertinentes. Los hilos cerrados y algunos registros históricos extensos se trataron como archivo de consulta bajo demanda, conforme a la propia regla de Softly; no se afirma una lectura literal línea por línea de cada conversación histórica. La propuesta prioriza vocabulario operativo y arquitectónico reutilizable, no un inventario de cada nombre propio o incidente.

## 12. Estado de la propuesta

Este documento es una **propuesta inicial de vocabulario común** para que Softly y Katarina la contrasten con la propuesta independiente de Softly. No modifica `SOFTLY.md`, `CHECKPOINT.md`, contratos, schemas, taxonomías ni permisos. Las definiciones etiquetadas como diseño/propuesta/histórico no deben citarse como reglas vigentes sin consultar su fuente y estado.

**Criterio para aprobar una versión normativa:** resolver los puntos de contraste, comprobar coherencia con los cuatro artefactos operativos canónicos y emitir una nueva versión con cambios trazables. No convertir automáticamente este borrador en una norma por el hecho de persistirlo.
