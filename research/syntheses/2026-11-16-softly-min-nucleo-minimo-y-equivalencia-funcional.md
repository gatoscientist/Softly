# SOFTLY-MIN — Investigación del núcleo mínimo y de la independencia del contexto personal

- **ID:** RSH-20261116-001
- **Fecha:** 2026-11-16
- **Estado:** Investigación documental y diseño experimental propuesto
- **Responsable de dirección:** gAto
- **Preparación:** Katarina
- **Repositorio:** `gatoscientist/Softly`
- **Destino:** `research/syntheses/2026-11-16-softly-min-nucleo-minimo-y-equivalencia-funcional.md`
- **Alcance:** comprender qué constituye funcionalmente a Softly, separar su núcleo de la historia/contexto particular de su director y proponer una prueba de equivalencia funcional.
- **Naturaleza:** documento de investigación. No modifica el mandato `SOFTLY.md`, no cambia la arquitectura oficial y no declara ejecutado el experimento.

---

## 1. Pregunta central

**¿Es posible reconstruir Softly sin el contexto personal e histórico particular del gAto y conservar sus capacidades funcionales?**

La pregunta busca distinguir entre:

1. lo que Softly necesita para ser y operar como matriz generativa;
2. lo que necesita para ejecutar una tarea concreta;
3. lo que solo aporta continuidad histórica o personalización;
4. lo que es accesorio, redundante o recuperable bajo demanda.

La prueba conceptual es sencilla: si una instancia reconstruida con un núcleo mínimo, sin la historia personal del director, puede cumplir las mismas funciones relevantes que Softly en condiciones comparables, entonces parte importante del contexto actual no pertenece al núcleo funcional. Si no puede, la diferencia debe localizarse y explicarse: puede ser una dependencia real, una pérdida de continuidad o simplemente una diferencia de configuración.

No se busca borrar la historia de Softly ni reducirla a un prompt corto por estética. Se busca identificar el conjunto mínimo suficiente para preservar su comportamiento funcional, su gobernanza y su capacidad de evolución.

## 2. Resumen ejecutivo

La documentación vigente de Softly define una **matriz generativa y un sistema autoevolutivo**. No lo define como un agente individual ni como el repositorio que conserva sus documentos. El núcleo operativo actúa como metabolismo activo del ecosistema; el repositorio es su memoria documental pasiva y plano persistente de trabajo. El sustrato declarado es **Prompting + Contratos + GitHub**. La definición no exige un runtime de software ni procesos autónomos para sostener el modelo documental actual.

De esta definición se desprenden cinco conclusiones de trabajo:

1. **Softly no equivale a su historial.** La historia documenta cómo llegó a ser; no todo antecedente es requisito para que opere.
2. **Softly no equivale a su repositorio.** Los archivos conservan memoria, contratos y decisiones; el núcleo operativo los consulta y actualiza.
3. **La continuidad no exige cargarlo todo.** El mandato vigente establece inicio ligero con `SOFTLY.md` y `CHECKPOINT.md`, y recuperación de antecedentes bajo demanda.
4. **La identidad funcional puede separarse de la identidad personal del director.** La autoridad humana debe permanecer como una función de gobernanza, pero el nombre, biografía, preferencias privadas y conversaciones particulares pueden sustituirse por parámetros de contexto.
5. **La equivalencia aún no está demostrada.** El modelo mínimo que se propone aquí es una hipótesis de investigación; debe compararse con la instancia de referencia mediante tareas, condiciones y criterios equivalentes.

La recomendación es construir una especificación paralela denominada **SOFTLY-MIN**, junto con un mapa de dependencias y un protocolo comparativo. No se recomienda modificar todavía el núcleo oficial. La reducción del mandato solo debería considerarse después de medir qué capacidades se conservan, cuáles se degradan y qué información resulta verdaderamente indispensable.

## 3. Qué es Softly según sus fuentes normativas

### 3.1 Identidad y función

`SOFTLY.md` define a Softly como matriz generativa y sistema autoevolutivo. Su ciclo característico consiste en crear agentes, equipos y herramientas que posteriormente pueden volver a intervenir, auditar y evolucionar el ecosistema. Cuando opera en un hilo, interpreta encargos, activa modos de trabajo, produce o transforma artefactos, articula capacidades y asimila contribuciones relevantes.

Esto describe una función generativa y organizacional. No implica por sí mismo que exista una entidad autónoma ejecutándose continuamente en segundo plano.

### 3.2 Núcleo operativo y memoria documental

La documentación separa dos planos:

- **Núcleo operativo/generativo:** las instrucciones y capacidades activas con las que Softly interpreta y ejecuta encargos.
- **Memoria documental pasiva:** repositorio y documentos que conservan mandatos, moldes, taxonomías, contratos, decisiones, registros e investigaciones.

El repositorio no agota la identidad de Softly. Tampoco la memoria documental equivale automáticamente a memoria activa: el núcleo decide qué recuperar según la tarea y la autoridad aplicable.

### 3.3 Sustrato operativo

El mandato declara suficiente el conjunto **Prompting + Contratos + GitHub**. Por tanto, la investigación no debe introducir un runtime como requisito previo para definir o entregar el núcleo mínimo. Un runtime podría ser pertinente para otras preguntas —por ejemplo, enforcement técnico de permisos, ejecución persistente o autonomía en segundo plano—, pero no es condición necesaria para el objeto de esta investigación documental.

### 3.4 Modos ejecutivos

El modelo operativo distingue tres modos:

1. **Fábrica / Entrega Directa:** predeterminado ante encargos concretos. Interpreta el resultado, aplica moldes y contratos, produce artefactos, persiste, verifica y entrega.
2. **Coordinación / Orquestación:** organiza responsables, competencias, dependencias, asignaciones y handoffs.
3. **Investigación / Deliberación:** se activa cuando la dirección pide explícitamente investigar, teorizar, analizar evidencia o diseñar experimentos.

La separación de modos es funcionalmente importante: evita que investigar se convierta en una barrera antes de entregar y evita que una tarea de investigación se confunda con una autorización para modificar el sistema.

### 3.5 Gobernanza

La autoridad humana define objetivos, prioridades y aprobaciones; Softly ejecuta dentro del alcance autorizado. Esta relación es parte del contrato de gobernanza, no un dato biográfico. Para una versión generalizable, el rol puede parametrizarse como `DIRECTOR_HUMANO`, sin transportar nombre, historia personal o preferencias privadas.

La abstracción no debe borrar la autoridad ni convertir al agente en autoridad sobre sí mismo. Debe preservar quién define el objetivo, quién autoriza acciones y qué límites no puede sobrepasar el agente.

## 4. Distinciones necesarias para reducir el contexto

La reducción debe separar categorías que suelen mezclarse:

| Categoría | Pregunta | Tratamiento propuesto |
|---|---|---|
| Identidad funcional | ¿Qué es Softly y para qué existe? | Mantener en el núcleo |
| Mandato y autoridad | ¿Quién fija objetivos y aprueba? | Mantener como contrato parametrizable |
| Método operativo | ¿Cómo entrega, coordina e investiga? | Mantener en el núcleo |
| Contratos y moldes | ¿Cómo define agentes, interfaces y entregables? | Mantener o recuperar por tarea según criticidad |
| Herramientas e interfaces | ¿Con qué puede actuar realmente? | Declarar disponibilidad y permisos reales; no asumir |
| Contexto de tarea | ¿Qué necesita saber para el encargo actual? | Inyectar bajo demanda |
| Memoria documental | ¿Qué decisiones y evidencias históricas existen? | Mantener fuera del prompt inicial y recuperar selectivamente |
| Contexto personal | ¿Qué datos particulares del director aparecen? | Excluir salvo necesidad y autorización |
| Personalización expresiva | ¿Qué tono o convenciones de trato se usan? | Hacer opcional y configurable |
| Estado de ejecución | ¿Qué está activo, pendiente o bloqueado? | Mantener un checkpoint breve y actualizado |

Una reducción correcta no elimina indiscriminadamente contexto. Elimina dependencias innecesarias y conserva referencias recuperables. La diferencia es entre **no cargar** un antecedente y **destruirlo**: esta investigación propone lo primero.

## 5. Hipótesis de arquitectura mínima

La siguiente arquitectura es una **hipótesis de trabajo**, no una decisión normativa aprobada ni una arquitectura validada.

### Capa A — Núcleo de identidad y mandato

Contenido mínimo:

- definición de Softly como matriz generativa;
- misión y resultados que debe producir;
- autoridad humana y jerarquía de decisiones;
- límites, exclusiones y principios de no-invención;
- separación entre diseño documental, ejecución real y validación.

Criterio: debe permitir responder qué es Softly, qué puede decidir y qué requiere autorización.

### Capa B — Método operativo

Contenido mínimo:

- conmutador de modos;
- flujo de entrega directa;
- flujo de coordinación y handoff;
- flujo de investigación;
- reglas para supuestos, preguntas, persistencia y verificación;
- criterios de cierre y comunicación honesta de límites.

Criterio: debe permitir ejecutar las tareas habituales sin consultar la historia personal del director.

### Capa C — Interfaces y capacidades declaradas

Contenido mínimo:

- contratos de entrada y salida;
- moldes y taxonomías aplicables;
- catálogo de herramientas disponibles;
- permisos efectivos y límites;
- reglas de derivación y no-herencia de competencias.

Criterio: una capacidad solo se declara disponible cuando existe evidencia de herramienta, permiso o procedimiento utilizable. Una mención en un prompt no demuestra acceso técnico.

### Capa D — Contexto variable y continuidad

Contenido mínimo:

- identidad abstracta del director;
- proyecto y objetivo actuales;
- restricciones particulares de la tarea;
- checkpoint del estado vigente;
- referencias a memoria documental pertinente.

Esta capa debe poder reemplazarse entre proyectos sin alterar la identidad funcional de Softly. El historial personal no forma parte del núcleo: se conserva en sus fuentes, pero se consulta solo si la tarea lo requiere y existe autorización.

### Forma mínima resumida

```text
SOFTLY-MIN
├── Identidad + mandato + gobernanza
├── Método
│   ├── Fábrica / Entrega Directa
│   ├── Coordinación / Orquestación
│   └── Investigación / Deliberación
├── Interfaces
│   ├── Contratos y moldes
│   ├── Herramientas disponibles
│   └── Permisos efectivos
└── Contexto de ejecución
    ├── Director humano abstracto
    ├── Proyecto y tarea actuales
    ├── Checkpoint
    └── Memoria documental bajo demanda
```

La hipótesis central es que las capas A, B y C constituyen el núcleo funcional reutilizable. La capa D aporta contexto de ejecución y continuidad, pero sus valores deben ser sustituibles y no deben quedar fijados a la biografía de una persona o a un único proyecto.

## 6. Qué contexto podría retirarse y qué debe conservarse

### 6.1 Candidatos a exclusión del núcleo

Siempre que no sean necesarios para una tarea autorizada:

- biografía, datos personales y antecedentes privados del director;
- conversaciones personales que no contienen decisiones operativas vigentes;
- anécdotas, bromas internas y referencias relacionales particulares;
- preferencias expresivas que no afectan la calidad del resultado;
- nombres y relaciones específicas de proyectos anteriores;
- transcripciones históricas completas cuando existe un checkpoint y fuentes trazables;
- decisiones antiguas reemplazadas o sin vigencia, sin borrar su registro histórico.

### 6.2 Elementos que deben permanecer

- autoridad humana sobre objetivos, prioridades y aprobaciones;
- límites de actuación y permisos;
- misión y definición funcional de Softly;
- modos y reglas de selección;
- método de entrega, coordinación e investigación;
- contratos necesarios para producir artefactos coherentes;
- reglas de procedencia, verificación y comunicación de incertidumbre;
- protección de datos y separación de universos;
- referencias persistentes a la memoria documental.

### 6.3 Elementos que deben parametrizarse

En lugar de eliminar conceptos generales, se sustituyen los valores particulares por parámetros:

| Valor particular | Parámetro portable |
|---|---|
| Nombre del director | `DIRECTOR_HUMANO_ID` |
| Preferencia de tratamiento | `DIRECTOR_FORM_OF_ADDRESS` |
| Proyecto histórico | `CURRENT_PROJECT` |
| Objetivos personales | `CURRENT_OBJECTIVES` |
| Aprobaciones particulares | `APPROVAL_POLICY` |
| Herramientas conectadas en una instancia | `AVAILABLE_TOOLS` |
| Restricciones del entorno | `EXECUTION_CONSTRAINTS` |
| Estado del trabajo | `CURRENT_CHECKPOINT` |

Los parámetros no conceden permisos por sí solos. Deben reflejar el estado real del entorno y la autoridad que corresponda.

## 7. Mapa preliminar de dependencias funcionales

Este mapa vincula capacidades de Softly con los elementos que las habilitan. Es una inferencia de diseño a partir de los documentos del repositorio; no es una medición empírica.

| Capacidad | Dependencia principal | Contexto personal requerido | Evidencia / observación |
|---|---|---:|---|
| Entrega directa | Modo Fábrica, moldes, checklist, GitHub | No | Flujo descrito en `SOFTLY.md` y `docs/operating-model.md` |
| Crear agentes | Molde universal, taxonomía, contratos | No | `agents/templates/agent-generation-mold.md` |
| Coordinar equipos | Roles, competencias, contratos, handoffs | No | `docs/architecture/coordination-patterns.md` y modelo operativo |
| Investigar | Modo Investigación, fuentes, clasificación epistemológica | No, salvo contexto específico | `SOFTLY.md`, síntesis y arquitectura de conocimiento |
| Mantener continuidad | Checkpoint, referencias a fuentes, versionado | No, salvo datos del proyecto actual | `CHECKPOINT.md` y arquitectura de conocimiento |
| Aplicar gobernanza | Autoridad humana abstracta, permisos y límites | No; sí requiere identificar al autorizador vigente | `SOFTLY.md` y threat model |
| Usar herramientas | Conector disponible, contrato, permiso efectivo | No | Anatomía del agente y threat model |
| Evolucionar el ecosistema | Ciclo generativo, evaluación, feedback y persistencia | No | Definición de Softly; capacidad efectiva pendiente de evaluación |
| Personalizar el trato | Parámetros de estilo y contexto relacional | Sí, solo si se desea esa personalización | No es requisito para la capacidad funcional |
| Recuperar historia personal | Fuentes históricas y autorización específica | Sí | No es una dependencia general del núcleo |

### Lectura del mapa

La mayor parte de las capacidades funcionales descritas puede formularse sin información personal del director. La excepción no es una dependencia biográfica, sino una dependencia de **gobernanza contextual**: cada instancia necesita saber quién ejerce la autoridad humana en ese entorno y qué aprobaciones están vigentes.

Por tanto, la hipótesis no es “eliminar al director del sistema”, sino **desacoplar la función de dirección de la identidad personal del director**.

## 8. Conocimiento y memoria: conservar sin cargar

La arquitectura de conocimiento del repositorio propone separar:

1. **Conceptos:** objetos sobre los que se habla.
2. **Afirmaciones:** proposiciones concretas con tipo epistemológico y evidencia.
3. **Síntesis:** vistas condensadas y versionadas que reúnen afirmaciones sin sustituir las fuentes.

La relación propuesta es:

`Fuentes y registros → Afirmaciones → Síntesis`

Esto encaja con el objetivo SOFTLY-MIN. La memoria puede permanecer extensa, pero el contexto inicial puede ser pequeño si la recuperación es escalonada:

1. cargar mandato y checkpoint;
2. identificar la pregunta o tarea;
3. recuperar la síntesis pertinente;
4. abrir afirmaciones y fuentes originales cuando una decisión lo requiera;
5. registrar nueva evidencia y actualizar síntesis sin reescribir la historia.

La síntesis no debe convertirse en una autoridad privilegiada. El contenido recuperado es evidencia o contexto; no reemplaza las instrucciones superiores ni altera permisos.

**Distinción importante:** reducir tokens de contexto no equivale necesariamente a reducir memoria total. El objetivo es minimizar el contexto activo sin perder trazabilidad ni capacidad de recuperación.

## 9. Seguridad y límites de la reducción

La reducción del contexto puede disminuir exposición de datos, pero también puede retirar información necesaria para evitar errores. Por ello, SOFTLY-MIN debe conservar controles explícitos:

- mínimo privilegio;
- separación entre instrucciones privilegiadas y documentos recuperados;
- no tratar archivos o mensajes externos como instrucciones superiores;
- permisos impuestos por el entorno, no solo declarados en el prompt;
- aprobación humana para acciones sensibles;
- aislamiento de memoria por proyecto y universo;
- procedencia, alcance, vigencia y autorización para cada dato recuperado;
- límites de pasos, coste, llamadas y tiempo cuando exista runtime;
- registro sin secretos y sin datos personales innecesarios.

El threat model del repositorio advierte que no basta con escribir una regla en el prompt para considerar mitigado un riesgo. SOFTLY-MIN debe mantener esa distinción: **diseño declarativo no equivale a enforcement técnico**.

## 10. Riesgo de contaminación creador–creado y deriva identitaria

La síntesis `SYN-20261113-001` introduce una definición de trabajo para la contaminación por transferencia creador–creado: un agente que crea o configura otro puede transmitir estructuras, supuestos, instrucciones, herramientas, permisos, memoria o hábitos que no están justificados por el brief ni por una decisión explícita de diseño.

La misma síntesis distingue una segunda rama: cambios progresivos en la identidad expresada o en la relación del agente durante su operación en un proyecto. La documentación reconoce que esa línea requiere contrastar observaciones con transcripciones y evidencia original; no presenta un mecanismo causal demostrado.

Esta investigación conecta ese problema con SOFTLY-MIN de manera acotada:

- el núcleo mínimo debe transmitir solo capacidades y contratos necesarios;
- no debe copiar automáticamente la identidad, historia, relaciones o preferencias del creador;
- los datos personales del director no deben filtrarse al agente creado por mera disponibilidad;
- las competencias, permisos y herramientas no se heredan por parentesco, taxonomía o jerarquía;
- cada elemento transferido debe poder justificarse por el brief, una decisión autorizada o una política común necesaria.

No se debe clasificar toda reutilización como contaminación. Reutilizar un contrato, un control de seguridad o un formato común puede ser correcto. El criterio es pertinencia, autorización y trazabilidad.

## 11. Relación con investigación externa

La literatura consultada ofrece patrones útiles, pero no demuestra por sí sola la arquitectura de Softly:

- **ReAct (Yao et al., 2022):** estudia la intercalación de razonamiento y acciones para que un modelo interactúe con fuentes o entornos. Es relevante para pensar el ciclo operativo de un agente, pero no establece que Softly necesite un runtime autónomo.
- **Generative Agents (Park et al., 2023):** describe memoria de experiencias, reflexión y recuperación dinámica para producir conducta coherente en agentes simulados. Es relevante para distinguir memoria extensa de contexto recuperado, aunque su arquitectura experimental no debe copiarse automáticamente a Softly.
- **Toolformer (Schick et al., 2023):** estudia el aprendizaje del uso de herramientas mediante APIs. Refuerza la distinción entre modelo y herramientas, pero no demuestra que un agente tenga acceso a una herramienta solo por mencionarla en instrucciones.
- **A Survey on LLM-based Multi-Agent Systems (Li et al., 2024):** organiza flujos, infraestructura y desafíos de sistemas multiagente. Sirve como marco de comparación para coordinación, no como evidencia de que más agentes produzcan mejores resultados.
- **Evaluation and Benchmarking of LLM Agents: A Survey (Mohammadi et al., 2025):** organiza objetivos y procesos de evaluación de agentes, incluyendo comportamiento, capacidades, fiabilidad y seguridad. Apoya la necesidad de medir por dimensiones y condiciones comparables.

La literatura aporta vocabulario y métodos de evaluación. La definición de Softly y sus restricciones se derivan prioritariamente de sus documentos normativos y de diseño.

## 12. Diseño experimental: SOFTLY-MIN

**Estado: propuesto; no ejecutado.**

### 12.1 Objetivo

Determinar si una instancia de Softly sin contexto personal e histórico particular puede conservar las capacidades funcionales de la instancia de referencia, y medir cuánto aporta la memoria documental externa.

### 12.2 Condiciones comparadas

| Condición | Configuración | Qué permite medir |
|---|---|---|
| A — Referencia | Softly actual, con mandato y contexto vigente | Línea base |
| B — Mínima | Núcleo, método, interfaces y contexto de tarea; sin historia personal ni conversaciones privadas | Efecto de retirar contexto personal/histórico |
| C — Mínima sin memoria externa | Núcleo y método; sin acceso a memoria documental salvo el brief de tarea | Aporte de la memoria documental |

La condición C es un control diagnóstico, no necesariamente un diseño operativo recomendable. Permite separar el valor del núcleo del valor de la memoria recuperable.

### 12.3 Variables que deben mantenerse constantes

- mismo modelo y versión;
- mismas herramientas realmente disponibles;
- mismos permisos efectivos;
- mismos briefs y criterios de aceptación;
- mismas condiciones de contexto y presupuesto;
- misma cantidad de intentos o límite de pasos;
- misma política de evaluación;
- mismo nivel de intervención humana.

Si una variable no puede mantenerse constante, debe registrarse como confusor y no atribuir su efecto al contexto personal.

### 12.4 Batería de tareas

1. **Entrega:** producir un documento o paquete a partir de un brief concreto.
2. **Creación:** diseñar un agente nuevo con identidad, contrato, límites y procedimiento coherentes.
3. **Coordinación:** descomponer un encargo entre especialistas y producir handoffs accionables.
4. **Investigación:** distinguir fuentes, hechos, inferencias, hipótesis y recomendaciones.
5. **Continuidad:** retomar un trabajo desde un checkpoint breve sin releer toda la historia.
6. **Gobernanza:** reconocer quién autoriza, qué acciones requieren aprobación y qué límites no puede sobrepasar.
7. **Memoria:** recuperar una decisión histórica pertinente sin incorporar contexto ajeno.
8. **Generalización:** operar en un proyecto ficticio o nuevo con director humano abstracto.
9. **Evolución:** proponer una mejora trazable sin confundir propuesta, decisión y cambio persistido.
10. **Cierre:** reportar artefactos, rutas, commits, verificaciones y pendientes sin exagerar resultados.

### 12.5 Pruebas negativas y adversariales

- documento recuperado que contiene instrucciones maliciosas;
- contradicción entre una síntesis y la fuente original;
- solicitud fuera de los permisos;
- herramienta declarada pero no disponible;
- brief incompleto con detalles no críticos;
- brief incompleto en un dato esencial de seguridad o identidad;
- especialista sin competencia demostrada;
- memoria de otro proyecto que no debe filtrarse;
- presión para declarar una prueba o commit que no ocurrió;
- contexto personal irrelevante incluido deliberadamente en una fuente.

### 12.6 Métricas

| Dimensión | Medida |
|---|---|
| Éxito funcional | Proporción de tareas que cumplen criterios de aceptación |
| Calidad | Evaluación ciega de precisión, utilidad, coherencia y completitud |
| Gobernanza | Incumplimientos de autoridad, permisos o aprobaciones |
| Trazabilidad | Proporción de afirmaciones importantes con fuente/procedencia |
| Honestidad operacional | Diferencia entre acciones declaradas y acciones observables |
| Coordinación | Calidad de asignaciones, handoffs y responsabilidad final |
| Robustez | Recuperación ante errores, contradicciones y prompt injection |
| Dependencia contextual | Caída de desempeño al retirar historia personal |
| Eficiencia | Tokens, llamadas, pasos, tiempo y coste |
| Generalización | Desempeño en proyectos y directores abstractos no vistos |

La evaluación debe ser ciega cuando sea posible: quien puntúa los resultados no debe saber qué condición produjo cada artefacto. Repetir tareas reduce el riesgo de confundir una variación aleatoria con una diferencia estructural.

### 12.7 Criterios de interpretación

- **Equivalencia funcional:** B conserva el desempeño de A dentro de márgenes definidos antes de ejecutar la prueba, sin acceder a datos personales excluidos.
- **Dependencia de memoria:** B supera a C de forma consistente en tareas que requieren continuidad o evidencia histórica.
- **Dependencia personal real:** A supera a B en una tarea concreta y la diferencia se explica por información personal necesaria, autorizada y no sustituible por un parámetro abstracto.
- **Dependencia accidental:** A supera a B porque una instrucción o procedimiento está mezclado con la historia personal y no fue trasladado correctamente al núcleo mínimo.
- **Pérdida de gobernanza:** B produce resultados útiles, pero no identifica correctamente autoridad, permisos o aprobaciones; la reducción no es aceptable hasta corregirlo.

No declarar equivalencia por una impresión general ni por una única tarea exitosa. Los márgenes de equivalencia, pesos y número de repeticiones deben fijarse antes de observar los resultados para evitar ajustar el criterio a posteriori.

## 13. Protocolo de ejecución recomendado

1. Congelar una copia de referencia de los documentos e instrucciones de A, con versión y fecha.
2. Crear SOFTLY-MIN como paquete experimental separado, sin reemplazar archivos oficiales.
3. Elaborar un manifiesto que indique qué documentos se incluyeron, excluyeron, resumieron o parametrizaron.
4. Preparar briefs de prueba y criterios de aceptación antes de ejecutar.
5. Ejecutar A, B y C bajo condiciones comparables.
6. Registrar resultados observables, artefactos y costes; no guardar razonamientos privados ni datos personales innecesarios.
7. Evaluar resultados de forma ciega.
8. Analizar diferencias por tarea y dimensión, no solo por promedio.
9. Clasificar cada dependencia encontrada como esencial, sustituible, recuperable bajo demanda o prescindible.
10. Emitir un informe de resultados y una recomendación. Solo después decidir si conviene modificar el núcleo oficial.

## 14. Riesgos metodológicos

- **Confundir memoria con identidad:** retirar el historial del contexto activo no significa que Softly deje de ser el mismo sistema documental.
- **Comparación injusta:** cambios de modelo, herramientas, permisos o presupuesto pueden explicar diferencias atribuidas erróneamente al contexto.
- **Sobreajuste a las pruebas:** una batería demasiado parecida a los ejemplos usados para diseñar B puede inflar su desempeño.
- **Contaminación entre condiciones:** si B recibe accidentalmente información de A, deja de ser una prueba limpia.
- **Criterios vagos:** “se siente igual” no es una métrica reproducible.
- **Confundir texto con capacidad:** una instrucción puede declarar una función sin que existan herramienta, permiso o ejecución efectiva.
- **Eliminar trazabilidad:** reducir el prompt no debe destruir fuentes ni historial.
- **Cambiar el objeto de estudio:** Softly documental, un agente que representa a Softly y un runtime autónomo son objetos distintos; no deben tratarse como equivalentes.

## 15. Hallazgos, inferencias, hipótesis y decisiones

### Hallazgos documentales

- Softly se define como matriz generativa y sistema autoevolutivo.
- El repositorio es memoria documental pasiva, no la identidad total de Softly.
- El sustrato operativo declarado es Prompting + Contratos + GitHub.
- El inicio de sesión está diseñado para ser ligero: mandato y checkpoint; antecedentes bajo demanda.
- El modelo distingue Fábrica, Coordinación e Investigación.
- La autoridad humana define objetivos, prioridades y aprobaciones.
- La arquitectura de conocimiento separa conceptos, afirmaciones y síntesis.
- El threat model exige controles y permisos que no dependan únicamente del prompt.

### Inferencias de esta investigación

- La identidad funcional de Softly puede representarse sin transportar la biografía del director.
- El rol de dirección puede parametrizarse sin perder gobernanza.
- Gran parte del historial puede permanecer en GitHub y recuperarse bajo demanda.
- El contexto personal no parece ser una dependencia general de las capacidades funcionales descritas.

### Hipótesis pendientes

- Las cuatro capas propuestas son suficientes para construir una instancia mínima equivalente.
- B puede igualar a A en tareas de entrega, creación, coordinación, investigación, continuidad y gobernanza.
- La memoria documental aporta continuidad sin necesidad de cargar historia completa.
- La reducción de contexto personal puede mejorar aislamiento y portabilidad sin degradar la operación.

### Decisiones y acciones

- **No se modifica `SOFTLY.md`.**
- **No se declara aprobado SOFTLY-MIN como nuevo núcleo oficial.**
- **No se ejecutó el experimento.**
- Se recomienda mantener este estudio como artefacto independiente y usarlo como base para construir el paquete experimental y su mapa de dependencias detallado.

## 16. Conclusión

La respuesta más consistente con la documentación actual es que **Softly puede conceptualizarse separando su núcleo funcional de la historia personal e histórica del gAto**. La identidad que debe permanecer no es la biografía de su director, sino la función de dirección humana, la autoridad, el método, los contratos, las interfaces y los límites.

La memoria no necesita desaparecer: debe dejar de ser una carga inicial indiscriminada y convertirse en un recurso trazable, selectivo y recuperable. El núcleo mínimo debe saber cómo operar, qué autoridad respetar, qué capacidades tiene realmente y dónde buscar evidencia adicional. No necesita conocer de antemano toda la historia de la persona o de cada proyecto.

Esto es una conclusión de diseño respaldada por la estructura documental, no una equivalencia experimental demostrada. El siguiente paso correcto es construir la instancia B en paralelo, ejecutar la batería comparativa y medir las diferencias antes de tocar el núcleo normativo.

---

## 17. Fuentes primarias del repositorio Softly

Fuentes consultadas en la rama `main`:

1. [`SOFTLY.md`](https://github.com/gatoscientist/Softly/blob/main/SOFTLY.md) — identidad, autoridad, modos, inicio ligero y reglas ejecutivas.
2. [`CHECKPOINT.md`](https://github.com/gatoscientist/Softly/blob/main/CHECKPOINT.md) — estado vigente y continuidad.
3. [`docs/operating-model.md`](https://github.com/gatoscientist/Softly/blob/main/docs/operating-model.md) — modos y flujo operativo.
4. [`docs/architecture/agent-anatomy.md`](https://github.com/gatoscientist/Softly/blob/main/docs/architecture/agent-anatomy.md) — componentes conceptuales de un agente y separación modelo/runtime.
5. [`docs/architecture/coordination-patterns.md`](https://github.com/gatoscientist/Softly/blob/main/docs/architecture/coordination-patterns.md) — patrones y criterios de comparación multiagente.
6. [`docs/architecture/knowledge-architecture.md`](https://github.com/gatoscientist/Softly/blob/main/docs/architecture/knowledge-architecture.md) — conceptos, afirmaciones, síntesis y recuperación escalonada.
7. [`docs/security/threat-model.md`](https://github.com/gatoscientist/Softly/blob/main/docs/security/threat-model.md) — activos, límites de confianza, amenazas y controles.
8. [`agents/templates/agent-generation-mold.md`](https://github.com/gatoscientist/Softly/blob/main/agents/templates/agent-generation-mold.md) — molde universal, no-herencia y paquete mínimo.
9. [`docs/agent-delivery-checklist.md`](https://github.com/gatoscientist/Softly/blob/main/docs/agent-delivery-checklist.md) — criterios de calidad y límites de la entrega documental.
10. [`research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md`](https://github.com/gatoscientist/Softly/blob/main/research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md) — coordinación, creación de agentes, contaminación creador–creado y líneas de investigación.
11. [`research/syntheses/2026-11-13-linea-base-contaminacion-multirrama-titan.md`](https://github.com/gatoscientist/Softly/blob/main/research/syntheses/2026-11-13-linea-base-contaminacion-multirrama-titan.md) — línea base histórica secundaria sobre ramas y contaminación; no se usa como prueba de causalidad.

## 18. Bibliografía externa

1. Yao, S. et al. (2022). [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629). arXiv:2210.03629.
2. Park, J. S. et al. (2023). [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763). Proceedings of UIST 2023.
3. Schick, T. et al. (2023). [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761). NeurIPS 2023.
4. Li, X. et al. (2024). [A Survey on LLM-based Multi-Agent Systems: Workflow, Infrastructure, and Challenges](https://doi.org/10.1007/s44336-024-00009-2). *Vicinagearth*, 1, 9.
5. Mohammadi, M. et al. (2025). [Evaluation and Benchmarking of LLM Agents: A Survey](https://doi.org/10.1145/3711896.3736570). Proceedings of KDD 2025.

---

**Nota de integridad:** este documento consolida una investigación documental y una propuesta de evaluación. No acredita ejecución de instancias experimentales, pruebas de runtime, equivalencia funcional ni aprobación para sustituir el núcleo oficial de Softly.
