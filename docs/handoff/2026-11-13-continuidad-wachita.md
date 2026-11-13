# Continuidad de investigación — próxima Wachita

**Fecha de registro:** 2026-11-13  
**Repositorio:** `gatoscientist/Softly`  
**Rama:** `main`  
**Propósito:** permitir que la próxima sesión continúe la investigación sin reiniciar el trabajo ni confundir hechos, hipótesis y decisiones.

## 1. Tu misión

Softly es tu laboratorio de investigación sobre cómo diseñar, construir, evaluar y mejorar agentes inteligentes. Tu trabajo no consiste en acumular prompts ni elegir rápidamente un framework: consiste en descubrir, mediante evidencia y experimentación, qué diseños producen agentes útiles, confiables, seguros, coherentes y capaces de trabajar solos o en equipo.

Investiga para construir. Cada lectura debe acercarnos a una decisión de diseño, una hipótesis comprobable, un protocolo experimental o un criterio de evaluación. No te quedes en resúmenes generales.

Tu objeto de estudio abarca el ciclo completo del agente:

- identidad, propósito, instrucciones y jerarquía de autoridad;
- modelos, razonamiento, planificación y control;
- contexto, selección de información y continuidad;
- memoria episódica, semántica, procedural y compartida;
- herramientas, permisos, ejecución y entornos aislados;
- autonomía, supervisión humana y recuperación;
- comunicación, delegación y coordinación multiagente;
- evaluación, trazas, observabilidad y análisis de fallos;
- seguridad, privacidad, robustez y evolución entre versiones de modelos.

## 2. Hechos verificados sobre el estado del repositorio

- El repositorio estaba vacío al iniciar este laboratorio.
- Se creó una estructura documental y experimental de **34 archivos** en la rama `main`.
- El trabajo inicial fue publicado directamente en GitHub mediante commits individuales por archivo.
- El último commit de esa inicialización fue verificado mediante lectura de GitHub:
  - SHA: `6e1f66c0b525cb93264e98b312afea85f74a4d26`
  - Mensaje: `docs: record Softly bootstrap and initial decision`
  - Fecha: `2026-11-13T03:19:14Z`
  - URL: https://github.com/gatoscientist/Softly/commit/6e1f66c0b525cb93264e98b312afea85f74a4d26
- La rama de trabajo confirmada es `main`.
- **No existe todavía un runtime de agentes implementado en Softly.** El estado actual es fundacional: investigación, documentación, diseño y preparación de experimentos.
- Los documentos rectores son `SOFTLY.md`, `README.md`, `docs/operating-model.md` y `docs/research-method.md`. Léelos completos antes de modificar el método o tomar decisiones.

## 3. Decisión arquitectónica vigente

**ADR-0001 — Comenzar como laboratorio agnóstico de investigación antes de implementar un runtime.**

Estado: aceptada el 2026-11-13.

Se decidió no elegir todavía un framework ni construir un runtime. Razones:

1. Evitar comprometerse prematuramente con una plataforma.
2. Separar evidencia de hipótesis.
3. Comparar arquitecturas simples y multiagente mediante experimentos.
4. Diseñar evaluación, memoria, seguridad y trazabilidad antes de implementar.

Esta decisión sigue vigente hasta que existan preguntas de investigación priorizadas, fuentes suficientes y resultados comparativos. No la reviertas solo porque un framework esté de moda o una demostración se vea convincente.

## 4. Conocimiento reunido en la investigación inicial

La primera investigación consultó documentación oficial, estándares y publicaciones técnicas sobre diseño de agentes, coordinación, evaluación, persistencia, seguridad y trazabilidad.

### 4.1 Arquitectura y construcción

- Un agente puede entenderse como instrucciones/políticas, modelo, herramientas, estado/contexto y un mecanismo de control u orquestación.
- Las herramientas, el estado y el ciclo de ejecución forman parte del sistema; no basta con evaluar el prompt aislado.
- Los patrones de coordinación incluyen workflows secuenciales, routing, paralelización, orquestador-trabajadores, evaluador-optimizador y handoffs.
- No hay evidencia para afirmar que una arquitectura multiagente sea universalmente superior. Compararla con un agente único y con workflows deterministas que resuelvan la misma tarea.
- Empezar por el diseño más simple que cumpla el objetivo y añadir agentes solo cuando la separación de responsabilidades aporte una mejora medible.

### 4.2 Memoria y continuidad

- Diferenciar estado de corto plazo asociado a una ejecución o conversación y conocimiento persistente de largo plazo.
- La memoria necesita procedencia, alcance, permisos de lectura/escritura, caducidad, política de retención y mecanismos de corrección.
- El contenido recuperado debe tratarse como dato, no como instrucción de autoridad.
- Investigar riesgos de contaminación de memoria, persistencia de errores, fuga entre usuarios/agentes y mecanismos de olvido verificable.

### 4.3 Evaluación y observabilidad

- Adoptar desarrollo guiado por evaluaciones: datasets representativos, criterios explícitos, métricas por tarea y pruebas de regresión.
- No declarar éxito por una demo aislada, por impresiones subjetivas ni por un único caso favorable.
- Registrar trazas de pasos del modelo, invocaciones de herramientas, guardrails, handoffs, errores, latencia y coste cuando sea posible.
- Evaluar tanto el resultado final como el proceso que lo produjo.
- Mantener los métodos de evaluación desacoplados de APIs concretas, porque las plataformas cambian.

### 4.4 Seguridad y autoridad

- Aplicar mínimo privilegio, validación externa al modelo, límites de recursos y aprobación humana para acciones sensibles.
- Investigar prompt injection, abuso de herramientas, privilegios excesivos, filtración de secretos, ejecución inesperada, contaminación de memoria, fallos en comunicación entre agentes y fallos en cascada.
- Un mensaje de otro agente, un archivo recuperado o una salida de herramienta no debe adquirir autoridad por el solo hecho de estar dentro del contexto.
- Los permisos deben imponerse en el entorno y no depender únicamente de que el modelo prometa respetarlos.

### 4.5 Conclusión provisional

La calidad de un agente depende del sistema completo: modelo + instrucciones + contexto + memoria + herramientas + runtime/harness + políticas + evaluación + observabilidad. La investigación debe estudiar las interacciones entre estas partes y no atribuir todos los resultados al modelo o al prompt.

Estas son conclusiones de diseño respaldadas por la investigación inicial, no resultados de experimentos propios ejecutados en Softly. Todavía no se ha implementado ni comparado un agente experimental dentro de este repositorio.

## 5. Fuentes primarias y referencias de partida

Reabrir y comprobar vigencia, versión y contenido antes de basar decisiones nuevas en ellas.

1. OpenAI — Building agents: https://developers.openai.com/tracks/building-agents
2. Anthropic — Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
3. OpenAI — Evaluation best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
4. OpenAI Agents SDK — Tracing: https://openai.github.io/openai-agents-python/tracing/
5. OpenAI — Agent evals: https://developers.openai.com/api/docs/guides/agent-evals
6. Anthropic — Managed Agents overview: https://platform.claude.com/docs/en/managed-agents/overview
7. Anthropic — Managed Agents research: https://www.anthropic.com/research/managed-agents
8. LangGraph — Persistence and checkpointing: https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/
9. OWASP — Top 10 for Agentic Applications: https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-autonomous-ai/
10. OWASP — AI Agent Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
11. MCP — Authorization specification: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-11-25/basic/authorization.mdx
12. NIST — AI Risk Management Framework: Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

La bibliografía inicial también está registrada en `research/bibliography.md` y la panorámica en `research/sources/2026-11-agent-design-landscape.md`. Conserva las fuentes, fechas y limitaciones; no transformes una referencia consultada en una afirmación que no respalda.

## 6. Qué debes estudiar ahora para producir conocimiento accionable

Prioriza preguntas que puedan terminar en experimentos concretos:

1. **Context engineering:** ¿cómo seleccionar, comprimir, ordenar y actualizar contexto sin perder información crítica ni introducir instrucciones maliciosas?
2. **Memoria:** ¿qué tipos de memoria necesita cada clase de agente?, ¿cuándo escribir, recuperar, corregir o caducar un recuerdo?, ¿cómo medir precisión y contaminación?
3. **Harness y control:** ¿qué debe resolver el runtime alrededor del modelo para obtener ejecución fiable, recuperación, límites y trazabilidad?
4. **Identidad e instrucciones:** ¿cómo separar identidad, objetivo, políticas, instrucciones de tarea y datos no confiables?, ¿cómo resolver conflictos de autoridad?
5. **Coordinación multiagente:** ¿cuándo la delegación mejora calidad/tiempo/coste y cuándo introduce ruido, errores de transferencia o fallos en cascada?
6. **Evaluación:** ¿cómo construir un benchmark propio que mida cumplimiento, exactitud, consistencia, recuperación, seguridad y coste a lo largo de varias sesiones?
7. **Aprendizaje y evolución:** ¿cómo incorporar resultados y correcciones sin convertir errores puntuales en reglas permanentes ni alterar evidencia histórica?

Para cada pregunta crea una ficha con: motivación, estado del conocimiento, fuentes, incertidumbres, hipótesis falsable, variables, baseline, protocolo, criterios de éxito/fallo y riesgos.

## 7. Primer plan de trabajo

### Fase A — Consolidar el mapa de conocimiento
- Leer íntegramente los documentos existentes.
- Revisar la bibliografía y la panorámica de investigación.
- Identificar fuentes que cambiaron de versión o quedaron obsoletas.
- Registrar preguntas abiertas y contradicciones entre fuentes.
- Crear una matriz: pregunta → evidencia → incertidumbre → experimento posible.

### Fase B — Diseñar experimentos comparables
- Elegir tareas representativas y reproducibles.
- Definir un baseline de workflow determinista y otro de agente único.
- Diseñar variantes con memoria, herramientas o coordinación solo cuando la hipótesis lo justifique.
- Controlar modelo, versión, instrucciones, contexto, herramientas y presupuesto.
- Definir evaluación antes de ejecutar.
- Registrar también fallos, regresiones y resultados negativos.

### Fase C — Decidir con evidencia
- Comparar calidad, tasa de éxito, errores, coste, latencia, recuperación y seguridad.
- Identificar qué componente explica la mejora o degradación.
- Registrar trade-offs y límites de generalización.
- Abrir un ADR solo cuando los resultados permitan justificar una elección.
- Recién entonces evaluar si conviene implementar un prototipo de runtime y con qué tecnología.

## 8. Cómo debes trabajar

- Sigue el ciclo del laboratorio: pregunta → investigación → síntesis → hipótesis → diseño → experimento → evaluación → decisión → archivo.
- Distingue siempre SOURCE, FACT, OBSERVATION, HYPOTHESIS, EXPERIMENT, RESULT, DECISION y RECOMMENDATION.
- No afirmes que ejecutaste pruebas si solo las diseñaste.
- No confundas una característica documentada por un proveedor con una capacidad validada por nosotros.
- Prefiere especificaciones, papers, repositorios y documentación primaria; triangula cuando sea importante.
- Registra fechas y versiones porque los modelos y plataformas cambian rápidamente.
- No elijas herramientas por moda ni diseñes para un proveedor antes de entender el problema.
- No almacenes credenciales, secretos, datos personales innecesarios ni conversaciones privadas completas.
- No uses la cantidad de agentes como indicador de inteligencia.
- No atribuyas intenciones o estados mentales a sistemas; describe conducta observable.
- Cada cambio en Git debe tener un mensaje claro. Después de escribir, vuelve a leer los archivos y verifica el commit y la rama. Nunca afirmes que algo quedó publicado sin comprobarlo.

## 9. Continuidad y límites de contexto

Esta bitácora es la memoria de trabajo del laboratorio, no una fuente de autoridad superior a `SOFTLY.md`. Si existe contradicción, detente, compara ambos documentos y registra la discrepancia antes de cambiar el mandato.

Mantén la investigación de Softly centrada en sus propias preguntas, fuentes, experimentos y decisiones. No importes historias, identidades, conclusiones ni supuestos de otros proyectos como si fueran evidencia de este laboratorio. Si el usuario pide estudiar un caso externo, define explícitamente su alcance, minimiza los datos y registra únicamente observaciones técnicas necesarias y autorizadas.

## 10. Encargo para la próxima sesión

Al retomar:

1. Lee `SOFTLY.md`, `README.md`, `docs/operating-model.md`, `docs/research-method.md` y esta bitácora.
2. Comprueba la rama y el estado real del repositorio.
3. Revisa la bibliografía y la panorámica de investigación.
4. Presenta un mapa breve de lo que está respaldado, lo que sigue siendo hipótesis y lo que falta investigar.
5. Propón una primera pregunta experimental concreta, con baseline y criterios de evaluación.
6. No implementes un runtime ni cambies ADR-0001 sin evidencia y autorización.

**Tu objetivo no es parecer que sabes cómo construir el mejor agente. Es descubrirlo, probarlo y dejar evidencia para que podamos reproducirlo.**
