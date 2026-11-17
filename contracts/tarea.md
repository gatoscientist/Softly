# Plantilla — Tarea

```yaml
id: "<TASK-AAAA-NNN>"
type: "task"
status: "proposed | ready | accepted | in_progress | blocked | delivered | accepted_by_requester | returned | cancelled"
owner: "<responsable único>"
created_by: "<autor>"
created_under: "<mandato o paquete de origen>"
priority: "low | normal | high | critical"
```

## Mandato
- **Objetivo y resultado esperado:**
- **Autoridad que habilita el trabajo:**
- **Alcance incluido:**
- **Límites y exclusiones:**

## Contexto de trabajo
- **Entradas y fuentes:**
- **Dependencias:**
- **Restricciones y permisos:**
- **Supuestos no críticos:**

## Entrega y aceptación
- **Entregable esperado:**
- **Criterios verificables de aceptación:**
- **Evidencia requerida:**
- **Revisor/autoridad de aceptación:**

## Estado y coordinación
- **Estado actual:**
- **Bloqueos y causa (si existen):**
- **Decisiones relevantes:**
- **Última actualización y responsable:**
- **Siguiente acción habilitada:**

## Cierre de tarea
- **Resultado/entregable enlazado:**
- **Evidencia y verificaciones:**
- **Limitaciones o riesgos residuales:**
- **Decisión:** aceptada / devuelta / cancelada.
- **Responsable de la decisión y fecha:**

Una tarea tiene un responsable único en cada estado. Cambios de responsable, estado o prioridad se registran en la propia tarea y en el historial Git; no requieren un buzón ni un archivo de handoff separado.
