# Anatomía de un agente: modelo de referencia

Este documento es un mapa de investigación, no una prescripción de implementación.

## Componentes conceptuales

1. **Identity / Role:** quién es el agente en términos funcionales, límites y responsabilidad.
2. **Instructions / Policy:** objetivos, prioridades, reglas y jerarquía de autoridad.
3. **Model:** motor de inferencia, versión, proveedor y parámetros.
4. **Context assembler:** selección y orden del contexto relevante.
5. **Memory:** estado de sesión, conocimiento persistente y memoria procedural.
6. **Planner / Controller:** decide el siguiente paso y cuándo detenerse.
7. **Tools:** capacidades externas con contratos y permisos.
8. **Runtime / Harness:** ejecuta el loop, impone presupuestos y maneja errores.
9. **Orchestrator:** delegación, handoffs y estado multiagente, si se necesita.
10. **Guardrails:** validación de entrada/salida y políticas fuera del modelo.
11. **Human approval:** revisión y autorización de acciones de riesgo.
12. **Observability:** trazas, eventos, costes, latencia y resultados.
13. **Evaluation:** pruebas de capacidad, regresión, robustez y seguridad.

## Separación crítica

El modelo puede proponer una acción; el runtime decide si está permitida. El texto del prompt no reemplaza un control de acceso. La memoria aporta contexto, pero no debe convertirse en una fuente de instrucciones privilegiadas. La observabilidad registra, pero no debe filtrar secretos.

## Workflow versus agente

Un workflow usa rutas predefinidas y controles explícitos. Un agente dinámico decide qué pasos y herramientas usar. Elegir workflow cuando el proceso es predecible; añadir autonomía solo cuando la variabilidad de la tarea lo justifique.

## Preguntas abiertas

- ¿Qué tareas se benefician realmente de planificación dinámica?
- ¿Qué parte del estado debe vivir fuera de la ventana de contexto?
- ¿Qué operaciones deben ser idempotentes?
- ¿Qué señales permiten detectar bucles o deriva?
- ¿Cómo medir utilidad de memoria frente a contaminación?
- ¿Cuándo un handoff es mejor que llamar a un especialista como herramienta?
