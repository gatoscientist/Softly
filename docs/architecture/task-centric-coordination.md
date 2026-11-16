# Modelo de coordinación task-centric de Softly

**Estado:** contrato documental operativo de la etapa 1 de KAT-006.  
**Base de dirección:** Alternativa B, adoptada por gAto el 2026-11-16.  
**Alcance:** coordinación documental basada en tareas y dependencias; no implementa un runtime ni migra directorios.

## 1. Principio organizador

La tarea es la unidad primaria de coordinación: expresa un resultado esperado, una responsabilidad, un estado y condiciones de aceptación. Las dependencias explicitan qué trabajo debe preceder a otro. Mensajes, eventos, handoffs, artefactos y espacios de trabajo son elementos relacionados con tareas; no sustituyen la tarea ni se convierten automáticamente en unidades organizativas o directorios.

Una tarea debe permitir responder: qué resultado se busca, quién responde por él, de qué depende, qué produjo, qué la bloquea y cómo se acepta.

## 2. Modelo mínimo de tarea

El contrato estructural está en [schemas/task.schema.json](../../schemas/task.schema.json). Sus campos obligatorios son:

- `task_id`: identidad estable de la tarea.
- `title`: resultado o trabajo expresado de forma breve.
- `status`: `proposed`, `ready`, `in_progress`, `blocked`, `done` o `cancelled`.
- `dimension`: dimensión de coordinación predominante.
- `owner`: responsable explícito (agente, humano, herramienta o equipo).
- `created_at` y `updated_at`: trazabilidad temporal.
- `depends_on`: IDs de tareas predecesoras.
- `acceptance`: criterios verificables de terminación.

Los campos opcionales permiten describir propósito, creador, fecha objetivo, tarea padre, resultados/artefactos, bloqueos, handoffs relacionados y referencias contextuales. El tipo genérico `team` permanece en el schema por portabilidad del modelo; no autoriza equipos activos. Durante RESET-CORE-2026-002 no se asignan tareas operativas a equipos.

### Reglas de estado y dependencia

1. `done` significa que los criterios de aceptación se comprobaron y los resultados quedaron registrados; no es sinónimo de que alguien haya enviado un mensaje de término.
2. `blocked` requiere al menos un bloqueo descrito en `blockers`; retirar el bloqueo no marca automáticamente la tarea como `ready`.
3. `ready` exige que las dependencias obligatorias estén satisfechas y que exista responsable y criterio de aceptación.
4. Las dependencias apuntan a IDs de tareas, no a nombres de agentes ni a mensajes. El contrato no valida por sí solo existencia, ciclos ni cierre de dependencias: eso requiere comprobación del conjunto de tareas.
5. No marcar una tarea como `done` si quedan dependencias obligatorias pendientes o criterios de aceptación sin evidencia.
6. Un handoff transfiere contexto/responsabilidad operativa; no crea por sí solo una tarea ni demuestra aceptación del receptor.

## 3. Las tres dimensiones

### 3.1 Coordinación propia

Cada participante organiza su propio trabajo dentro de su autoridad y capacidad declarada. Descompone una asignación en tareas, ordena su secuencia, identifica dependencias, actualiza estados, registra resultados y expone bloqueos. No reasigna trabajo ajeno ni amplía su autoridad por autocoordinación.

### 3.2 Coordinación entre pares

Dos o más participantes gestionan interfaces y dependencias horizontales: acuerdan entradas/salidas, sincronizan secuencias, declaran compromisos, negocian cambios y resuelven incompatibilidades dentro de sus ámbitos autorizados. Ningún par adquiere autoridad jerárquica sobre otro por el solo hecho de coordinarse. La derivación respeta competencias y la regla de no-herencia.

### 3.3 Orquestación

Un rol o instancia con autoridad explícita organiza el trabajo distribuido para alcanzar un objetivo: define/ordena tareas, asigna responsables, explicita dependencias, resuelve prioridades dentro de su mandato, integra resultados y escala bloqueos o decisiones fuera de su autoridad. La orquestación coordina el conjunto de tareas, pero no reemplaza la responsabilidad de cada owner por la calidad y evidencia de su resultado.

La dimensión registrada es la predominante para describir el acto de coordinación; no implica que una tarea completa pertenezca exclusivamente a un solo participante o nivel.

## 4. Relación con mecanismos existentes

- **Handoff:** se mantiene el contrato existente `schemas/handoff.schema.json` y la plantilla `agents/templates/handoff.md`. Cuando el handoff está vinculado a una tarea registrada, usa el campo opcional `task_id`; `task` sigue siendo el resumen legible y no sustituye el ID estable. No se duplica el handoff como otro modelo de tarea.
- **Eventos y mensajes:** comunican cambios o solicitudes; deben referenciar el `task_id` cuando estén vinculados a una tarea. Un evento no equivale a una tarea.
- **Artefactos/resultados:** se registran como rutas o referencias en `outputs`; la existencia de una ruta no certifica por sí sola la calidad del resultado.
- **Bloqueos:** se registran en la tarea afectada y se escalan al responsable con autoridad para resolverlos.
- **GitHub:** conserva la memoria documental y evidencia persistente. No despierta sesiones ni ejecuta dependencias automáticamente.

## 5. Límites de autoridad y control

La coordinación no concede permisos, competencias, autoridad ni acceso. El owner responde por su tarea; quien orquesta responde por la coherencia de la asignación, las dependencias y la integración dentro de su mandato. gAto conserva las decisiones y aprobaciones que le corresponden. La asignación a una herramienta no presupone que esté conectada o disponible.

## 6. Pregunta sistémica abierta — no resuelta

**¿La orquestación cubre suficientemente la coordinación sistémica, o esta constituye una responsabilidad/capacidad diferenciada que no queda completamente expresada dentro de la orquestación?**

Se conservan abiertas, sin elegir entre ellas, estas interpretaciones:

1. La coordinación sistémica queda comprendida dentro de la orquestación.
2. Es una responsabilidad transversal o especialización de la orquestación.
3. Requiere una descripción/capacidad diferenciada, sin que ello obligue a crear una cuarta dimensión principal.

Esta implementación no responde la pregunta por inferencia. Se requiere análisis explícito y decisión de gAto.

## 7. Límites de implementación

Este documento y los schemas son contratos declarativos. No hay aquí motor de workflow, scheduler, ejecución automática, detección automática de ciclos, persistencia transaccional, enforcement de permisos ni validador runtime. La validación estructural de los JSON Schema y las reglas de conjunto deben ejecutarse por herramientas externas cuando se habilite esa etapa.

## 8. Referencias

- [Decisión de dirección task-centric y tres dimensiones](../../research/coordination/2026-11-16-decision-direccion-task-centric-tres-dimensiones.md).
- [Modelo operativo](../operating-model.md).
- [Contrato de handoff](../../schemas/handoff.schema.json).
- [Plantilla de handoff](../../agents/templates/handoff.md).