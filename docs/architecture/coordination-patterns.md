# Patrones de coordinación de agentes

## Patrones a estudiar

### Single agent + tools
Un agente usa herramientas especializadas. Es el baseline obligatorio para comparar complejidad adicional.

### Prompt chain
Secuencia fija de etapas; cada salida alimenta la siguiente. Útil cuando las subtareas son conocidas y hay validaciones intermedias.

### Router
Clasifica la solicitud y la deriva a un flujo/agente especializado. Medir falsos enrutamientos y recuperación.

### Parallel workers
Varios especialistas trabajan en subtareas independientes. Requiere controlar redundancia, coste y síntesis.

### Orchestrator-workers
Un coordinador descompone dinámicamente y delega. Adecuado cuando no se conocen de antemano las subtareas.

### Evaluator-optimizer
Un generador produce y un evaluador critica contra criterios explícitos. Evitar ciclos sin límite y evaluadores correlacionados con el generador.

### Handoff
El especialista toma el control de la interacción. Definir qué contexto se transfiere y quién conserva responsabilidad por la respuesta final.

### Agent-as-tool
El coordinador conserva el control y consume al especialista como capacidad acotada.

## Criterios comparativos

- éxito en la tarea y calidad;
- tasa de errores y recuperación;
- coste, tokens y latencia;
- número de pasos y llamadas;
- claridad de trazabilidad;
- exposición de datos;
- superficie de permisos;
- facilidad de pruebas y mantenimiento.

No asumir que más agentes implican más inteligencia. Comparar siempre contra un baseline de un solo agente y contra un workflow sin LLM cuando sea viable.
