# HANDOFF-20261116-KAT-006 — Implementación de arquitectura de coordinación task-centric

**ID:** HANDOFF-20261116-KAT-006  
**Emite:** Katarina 2.0.1 — Agent Softly  
**Dirección:** gAto  
**Proyecto:** Softly  
**Repositorio de destino:** `gatoscientist/Softly`  
**Modo:** Fábrica / Entrega Directa  
**Estado:** ready — handoff documental publicado; activación de sesión pendiente

## Handoff compacto

```text
HANDOFF HANDOFF-20261116-KAT-006 | ready
FROM: katarina@2.0.1 -> agentdev-katarina@1.1.0
TASK: COORD-2026-11-16-STAGE1 — implementar coordinación task-centric en Softly
RESULT: este encargo y sus criterios, en Katarinasay/inbox/
EVIDENCE: decisión task-centric de gAto; investigación de Softly y comparación de Katarina
DECISIONS: tres dimensiones como estructura inicial; coordinación sistémica permanece abierta
OPEN: determinar si la coordinación sistémica queda dentro de orquestación o requiere responsabilidad diferenciada
NEXT: revisar fuentes, diagnosticar, implementar cambios mínimos, validar y entregar commits
ACCEPT: Softly puede verificar y adaptar la arquitectura a Katarina sin explicación oral
CONTEXT: solo gatoscientist/Softly; no modificar gatoscientist/Katarina
```

## 1. Destinataria y asignación

La destinataria técnica solicitada por el paquete de ejecución es **Dra. Katarina**, identificada en el registro profesional de Softly como `agentdev-katarina@1.1.0` (AgentDEV; ingeniería de software y runtime de agentes; arquitectura operativa, orquestación, herramientas y persistencia). El registro la declara `active-standby`; eso representa disponibilidad documental, no una sesión activa ni una ejecución en segundo plano.

Se solicita a Softly que tome este handoff y lo despache a esa destinataria. La publicación de este documento no activa automáticamente una sesión. No se afirma que la destinataria haya recibido, aceptado o comenzado el encargo.

## 2. Objetivo

Implementar en `gatoscientist/Softly` el modelo de coordinación centrado en tareas y dependencias, usando como estructura inicial las tres dimensiones acordadas:

1. **Coordinación propia:** el agente organiza y conduce su propio trabajo dentro de su autoridad, alcance y restricciones.
2. **Coordinación entre pares:** los participantes gestionan dependencias, interfaces, recursos e intercambios necesarios para colaborar.
3. **Orquestación:** una instancia o rol con autoridad organiza trabajo distribuido, asigna responsables, gestiona dependencias, integra resultados y conduce el avance hacia el objetivo.

La tarea parte de la dirección de trabajo ya adoptada por gAto. No reabre la decisión task-centric ni convierte la preferencia por tres dimensiones en una cuarta dimensión.

## 3. Fuentes obligatorias antes de modificar

Leer los mandatos y la arquitectura vigentes de Softly, con atención especial a:

- `SOFTLY.md` y `CHECKPOINT.md`.
- `docs/architecture/coordination-patterns.md`.
- `docs/architecture/operational-modes-and-autocoordination.md`.
- `docs/architecture/agent-model-v0.1.md`.
- `docs/architecture/agent-model-handoff-2026-11-13.md`, cuando aporte contexto pertinente.
- `schemas/handoff.schema.json` y los demás schemas relacionados que resulten pertinentes.
- `agents/templates/handoff.md`, briefs y plantillas que correspondan.
- `research/coordination/2026-11-16-decision-direccion-task-centric-tres-dimensiones.md`.
- `research/coordination/2026-11-16-investigacion-coordinacion-universal-y-redisenio-arquitectura.md`.
- Los informes comparativos de Katarina conservados en `gatoscientist/Katarina/shared/`, únicamente como fuentes de diseño ya entregadas.

La decisión de dirección establece la Alternativa B como base de trabajo: tarea como punto de partida; mensajes, eventos, artefactos y espacios de trabajo como responsabilidades conceptuales diferenciadas, vinculadas a tareas cuando corresponda. No impone una estructura física de directorios ni una migración automática.

## 4. Trabajo requerido

1. Examinar patrones actuales de coordinación, modelo de agentes, contratos de handoff, esquemas, plantillas, mandatos y documentación.
2. Reconstruir cómo se representan hoy las tareas, dependencias, responsables, mensajes, eventos, artefactos, workspaces, estados, bloqueos, integración y aceptación.
3. Entregar un diagnóstico del estado inicial e inventariar qué componentes deben modificarse, mantenerse o crearse.
4. Implementar el modelo centrado en tareas y dependencias de forma coherente en los documentos, contratos, schemas, plantillas y mecanismos declarativos que realmente lo requieran.
5. Distinguir expresamente **coordinación** de **comunicación**. No convertir canales o mensajes en sustitutos de tareas ni duplicar la misma responsabilidad en varias estructuras.
6. Hacer trazables tareas, dependencias, responsables, estados, resultados, bloqueos, decisiones, evidencias y siguientes acciones.
7. Documentar las tres dimensiones, sus límites de autoridad, interfaces y relación mutua. La coordinación propia y la coordinación entre pares deben poder operar sin asumir automáticamente autoridad de orquestación.
8. Evitar duplicar mecanismos existentes, imponer directorios innecesarios o modificar componentes que no aporten al objetivo.
9. Ejecutar las validaciones de consistencia pertinentes entre documentación, contratos, schemas y plantillas. Diferenciar validaciones estáticas de pruebas runtime.
10. Registrar decisiones tomadas, alternativas descartadas, riesgos y asuntos pendientes.
11. Realizar commits identificables y releer desde GitHub todos los archivos modificados para verificar persistencia e integridad.

## 5. Pregunta sistémica que debe permanecer abierta

**¿La orquestación cubre realmente la coordinación sistémica o existe una responsabilidad sistémica autónoma que debe reconocerse explícitamente en la arquitectura?**

No declarar resuelta esta pregunta por el solo hecho de implementar las tres dimensiones. Analizar y documentar, al menos, estas posibilidades:

- la coordinación sistémica está comprendida dentro de la orquestación;
- es una especialización o responsabilidad transversal de la orquestación;
- requiere describirse como una capacidad/responsabilidad diferenciada, sin que eso obligue a convertirla en una cuarta dimensión principal;
- una combinación de las anteriores.

Considerar coherencia global, gobernanza, interoperabilidad, recursos compartidos, evolución, dependencias entre equipos y resolución de conflictos sistémicos. Exponer consecuencias, ventajas, límites e incertidumbres de cada interpretación. No forzar una conclusión si la evidencia no alcanza.

## 6. Restricciones y límites de autoría

- Trabajar exclusivamente en `gatoscientist/Softly`, respetando sus rutas y convenciones.
- **No modificar `gatoscientist/Katarina`**: la segunda implementación corresponde a Softly en la etapa siguiente.
- No copiar documentos literalmente entre repositorios.
- No modificar componentes que no sean necesarios.
- Preservar historia, decisiones y commits; corregir mediante nuevos commits.
- No confundir canales de comunicación con dimensiones de coordinación.
- No presentar la coordinación sistémica como resuelta.
- No declarar pruebas, despliegues, activaciones o validaciones que no hayan ocurrido.
- No asumir que un handoff publicado activa por sí solo una sesión.
- La auditoría independiente posterior corresponde exclusivamente a Audeline; esta etapa no debe anticiparla ni sustituirla.

## 7. Entrega obligatoria

La entrega final debe incluir:

- resumen ejecutivo;
- diagnóstico de la arquitectura inicial;
- inventario de archivos modificados, mantenidos y creados;
- justificación de cada modificación relevante;
- descripción operativa de las tres dimensiones;
- modelo de tareas y dependencias y su relación con mensajes, eventos, artefactos y workspaces;
- decisiones tomadas y alternativas descartadas;
- pruebas y validaciones ejecutadas, con resultados y límites;
- riesgos y asuntos pendientes;
- análisis explícito de la pregunta de coordinación sistémica, manteniéndola abierta si no hay evidencia suficiente;
- identificadores de commits;
- handoff formal de vuelta a Softly, con rutas, evidencia, siguiente acción y criterios verificables.

## 8. Criterio de aceptación

Softly debe poder comprender, verificar y adaptar la arquitectura a su propia implementación en Katarina sin depender de explicaciones orales de Katarina. La entrega no se considera completa por la sola existencia de commits: debe incluir trazabilidad, validaciones realmente ejecutadas y relectura verificable de los archivos modificados.

**Secuencia:** Katarina/Dra. Katarina implementa en Softly → Softly verifica la entrega → Softly adapta e implementa en Katarina → Audeline audita ambas implementaciones → gAto decide la aceptación final.

**Estado al emitir este handoff:** encargo preparado y publicado. Implementación, commits de implementación, validaciones y aceptación siguen pendientes de la ejecución y evidencia de la destinataria.
