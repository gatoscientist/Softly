# Plantilla de handoff Softly (5–12 líneas)

Usar un único bloque compacto por transferencia. No incluir credenciales, memoria privada ni contexto completo. Cuando el handoff corresponda a una tarea registrada, incluir su ID estable.

```text
HANDOFF <handoff_id> | ready
FROM: <agent_id>@<version> -> TO: <agent_id|taxonomy>
TASK_ID: <task_id|none>
TASK: <assignment_id> — <resultado esperado>
RESULT: <ruta/artefacto/commit>
EVIDENCE: <fuentes/pruebas/referencias>
DECISIONS: <decisiones o none>
OPEN: <riesgos/bloqueos o none>
NEXT: <acción concreta del receptor>
ACCEPT: <criterio verificable>
CONTEXT: <referencias mínimas y límites>
```

Estados de respuesta: `accepted`, `rejected` con motivo, o `blocked` con requisito faltante. El emisor mantiene responsabilidad por la exactitud de lo entregado; el receptor verifica antes de continuar. Un evento repetido con el mismo `event_id` no debe disparar una segunda ejecución.