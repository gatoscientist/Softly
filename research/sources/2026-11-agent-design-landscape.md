# Panorama inicial de diseño de agentes — noviembre 2026

**ID:** SRCSET-20261113-001  
**Consultado:** 2026-11-13  
**Tipo:** exploración documental de fuentes oficiales y estándares  
**Estado:** síntesis inicial; requiere lectura profunda y actualización periódica.

## 1. OpenAI — Building agents

URL: https://developers.openai.com/tracks/building-agents

La guía presenta agentes como sistemas que combinan instrucciones, guardrails y herramientas. Sus primitivas incluyen modelos, herramientas, estado/memoria y orquestación. Destaca separación de responsabilidades, handoffs, sesiones y trazabilidad.

**Implicación para Softly:** documentar cada agente como configuración + herramientas + políticas + estado, y registrar el ciclo completo de ejecución.

**Límite:** guía del proveedor sobre su propio ecosistema; no constituye prueba de superioridad de una arquitectura o SDK.

## 2. Anthropic — Building effective agents

URL: https://www.anthropic.com/research/building-effective-agents  
Publicado: 2024-12-19.

Distingue workflows (rutas predefinidas) de agentes (decisión dinámica sobre proceso y uso de herramientas). Recomienda empezar por la solución más simple y aumentar complejidad solo cuando el problema lo requiere. Describe prompt chaining, routing, parallelization, orchestrator-workers y evaluator-optimizer.

**Implicación:** todo experimento multiagente debe compararse con un baseline más simple.

**Límite:** artículo de 2024; la propia página indica que parte del panorama de herramientas evolucionó.

## 3. OpenAI — Evaluation best practices

URL: https://developers.openai.com/api/docs/guides/evaluation-best-practices

Recomienda evaluación dirigida por tareas, datasets representativos, criterios claros, automatización, revisión humana y evaluación continua. Advierte contra métricas genéricas y evaluaciones basadas en impresiones subjetivas.

**Implicación:** conservar casos reales anonimizados y casos adversariales; medir regresiones después de cambios de modelo, instrucciones, herramientas y memoria.

**Nota de vigencia:** la página informa cambios programados en la plataforma Evals API durante octubre/noviembre de 2026. No acoplar el método del laboratorio a una API específica; mantener datasets y criterios exportables.

## 4. OpenAI — Tracing y evaluación de workflows

URLs:
- https://openai.github.io/openai-agents-python/tracing/
- https://developers.openai.com/api/docs/guides/agent-evals

La trazabilidad puede registrar generaciones, llamadas de herramientas, guardrails, handoffs y eventos personalizados. El análisis de trazas ayuda a detectar errores de selección de herramienta, delegación y política.

**Implicación:** Softly debe conservar un esquema de ejecución neutral respecto del proveedor: run, turn, agent, model, tool, handoff, approval, guardrail y outcome.

**Límite:** revisar cuidadosamente retención y exposición de datos antes de habilitar trazas externas.

## 5. Anthropic — Managed Agents y harnesses

URLs:
- https://platform.claude.com/docs/en/managed-agents/overview
- https://www.anthropic.com/research/managed-agents

El modelo conceptual separa configuración de agente, entorno de ejecución, sesión/eventos y sandbox. La publicación sobre harnesses subraya que los supuestos del harness pueden quedar obsoletos cuando los modelos cambian; interfaces estables permiten sustituir implementaciones.

**Implicación:** separar definición del agente, runtime/harness, entorno y registro de eventos. Versionar los supuestos y volver a probarlos con nuevos modelos.

**Límite:** documentación de un producto en beta a la fecha de consulta; no adoptar como arquitectura obligatoria.

## 6. LangGraph — Persistence

URLs:
- https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/
- https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/checkpointers.mdx

Distingue checkpoints de estado de hilo (continuidad, interrupción, recuperación y revisión) de stores de conocimiento de largo plazo compartido entre hilos.

**Implicación:** no llamar “memoria” a un único almacén indiferenciado. Separar historial, estado de ejecución, hechos persistentes, memoria procedural y conocimiento compartido.

**Límite:** descripción de abstracciones del framework; Softly debe evaluar alternativas y evitar dependencia temprana.

## 7. OWASP — Top 10 for Agentic Applications

URL: https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-autonomous-ai/

Taxonomía de riesgos que incluye goal hijacking, tool misuse, identity/privilege abuse, supply-chain vulnerabilities, unexpected code execution, memory/context poisoning, insecure inter-agent communication, cascading failures, human-agent trust exploitation y rogue agents.

**Implicación:** el threat model de Softly debe cubrir no solo prompt injection, sino también herramientas, memoria, comunicación entre agentes y fallos sistémicos.

**Límite:** taxonomía para orientar análisis; la severidad de un caso concreto requiere evidencia y contexto.

## 8. OWASP — AI Agent Security Cheat Sheet

URL: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html

Recomienda mínimo privilegio, validación de entradas externas, supervisión humana, aislamiento de memoria, outputs estructurados, límites de coste/reintentos/cadena de herramientas y pruebas adversariales.

**Implicación:** crear una matriz de abuso repetible y controles verificables, no una lista de instrucciones de prompt.

## 9. MCP — Authorization

URL: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-11-25/basic/authorization.mdx

La especificación de autorización HTTP de MCP contempla OAuth, audience/resource binding, PKCE, almacenamiento seguro de tokens y el problema del confused deputy. La autorización es una capa de protocolo y no sustituye la autorización de cada acción en la aplicación.

**Implicación:** registrar por separado identidad, scopes, permisos de herramienta, autorización de recurso y consentimiento humano.

**Límite:** aplicar solo a transportes y escenarios cubiertos por la especificación; revisar versión vigente antes de implementar.

## 10. NIST — AI RMF Generative AI Profile

URL: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence  
DOI: https://doi.org/10.6028/NIST.AI.600-1

Marco de gestión de riesgos para IA generativa durante el ciclo de vida. Puede aportar estructura de gobernanza, medición, gestión y documentación.

**Implicación:** los riesgos y controles de Softly deben mantenerse durante diseño, pruebas, despliegue y operación.

## Síntesis provisional

1. La arquitectura debe separar modelo, harness/runtime, herramientas, estado/memoria, entorno y observabilidad.
2. No se debe usar multiagente como punto de partida automático; primero medir un agente simple y workflows deterministas.
3. Las autorizaciones reales deben imponerse fuera del modelo.
4. La memoria requiere procedencia, scope y controles contra contaminación.
5. Evaluación y trazabilidad deben diseñarse antes del despliegue.
6. Los harnesses y sus supuestos deben reevaluarse cuando cambia el modelo.
7. La comunicación entre agentes y el contexto compartido son superficies de seguridad.
8. El laboratorio debe permanecer agnóstico a proveedor y framework hasta tener evidencia comparativa.

## Preguntas de investigación pendientes

- ¿Qué taxonomía de memoria ofrece mejor balance entre recuperación, privacidad y contaminación?
- ¿Qué mecanismos reducen errores de delegación en equipos de agentes?
- ¿Cuándo el evaluador aporta señal independiente y cuándo reproduce sesgos del generador?
- ¿Cómo medir autonomía útil versus autonomía riesgosa?
- ¿Qué controles deben ser runtime invariants y cuáles pueden ser políticas configurables?
- ¿Cómo comparar modelos sin confundir diferencias del modelo con diferencias del harness?
