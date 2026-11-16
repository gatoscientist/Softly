# PROMPT DE INVESTIGACIÓN PROFUNDA — KATARINA
## Arquitectura de coordinación entre agentes: fundamentos, evaluación y rediseño del sistema Softly

**Destinataria:** Katarina  
**Emisor:** gAto  
**Modalidad:** Modo Investigación  
**Prioridad:** Alta  
**Tipo:** Investigación profunda, revisión arquitectónica y propuesta de optimización  
**Carácter:** Independiente, crítico y exploratorio  
**Autorización:** Investigar, consultar fuentes, analizar y proponer. No implementar cambios ni modificar contratos normativos.

## 1. Mandato

Inicia una investigación profunda sobre coordinación entre agentes de inteligencia artificial, con especial atención a cómo construir sistemas en los que múltiples agentes puedan coordinar su trabajo, coordinarse entre sí y colaborar eficazmente sin generar burocracia innecesaria.

No partas de que la arquitectura actual de Softly es correcta ni de que está equivocada. Investiga, contrasta evidencia, identifica problemas y propone la mejor arquitectura fundamentada.

El gAto sospecha que el sistema actual de directorios, canales y flujos de comunicación podría estar mal diseñado o tener complejidad innecesaria. Si está mal, dilo claramente; si está bien, demuéstralo; si algunas partes sirven y otras no, identifica cuáles y por qué. No protejas decisiones anteriores por razones históricas o de autoría.

## 2. Fuentes obligatorias

### 2.1 Repositorios autorizados

Investiga exclusivamente:
- `gatoscientist/Katarina`
- `gatoscientist/Cytryna`
- `gatoscientist/TITAN`
- `gatoscientist/Auditoria`
- `gatoscientist/Softly`
- `gatoscientist/Laboratorio-de-agentes`

No explores otros repositorios del ecosistema. Examina identidades, responsabilidades, taxonomías, competencias, contratos, canales, espacios compartidos, asignaciones, handoffs, bitácoras, registros, autoridad, aceptación e incidencias. No te limites a README: inspecciona archivos y relaciones pertinentes.

### 2.2 Investigación iterativa en Internet

Realiza búsquedas iterativas. Investiga literatura académica, documentación técnica, arquitecturas implementadas y evaluaciones. Explora Multi-Agent Systems, Multi-Agent Coordination, Distributed Systems, Agent Communication Protocols, Organizational Design for AI Agents, Blackboard Architectures, Shared Memory, Message Passing, Workflow Orchestration, Task Allocation, Scheduling, Consensus, Conflict Resolution, Agent Communication Languages, Handoff and Delegation, Multi-Agent Collaboration Evaluation y Human-Agent Teaming.

Amplía las categorías según los hallazgos. Sigue referencias, compara enfoques y busca evidencia contraria a tus primeras conclusiones. Prioriza fuentes originales verificables. Distingue publicaciones académicas, documentación de fabricantes, experimentos y opiniones. Registra referencias y enlaces.

## 3. Pregunta central

¿Cómo conseguimos que todos los integrantes de un ecosistema de agentes sean buenos coordinadores y, al mismo tiempo, sepan coordinarse eficazmente?

Distingue:

**Coordinar:** organizar trabajo, distribuir responsabilidades, asignar tareas, gestionar dependencias, sincronizar participantes, supervisar, integrar resultados, resolver conflictos, escalar y administrar prioridades.

**Coordinarse:** comprender el propio rol, comunicar estado, respetar contratos, identificar dependencias, solicitar colaboración, entregar resultados utilizables, informar bloqueos, evitar duplicaciones, reconocer límites e integrarse con otros.

Investiga si esta distinción está respaldada por literatura y si debe ampliarse, modificarse o dividirse.

## 4. Líneas obligatorias

### 4.1 ¿La coordinación se enseña o se incorpora al diseño?

Compara formación formal, competencias en identidad/contrato, procedimientos y protocolos, cambios de prompt, herramientas de orquestación y combinaciones. Evalúa resultados y circunstancias. ¿Necesitamos estudios formales o bastan instrucciones y prácticas pequeñas? No supongas que más formación implica mejor coordinación.

### 4.2 Cambios pequeños de alto impacto

Investiga cambios sencillos: declarar objetivo, responsable, estado y progreso; identificar dependencias; informar bloqueos; definir entregas; no asumir lectura de mensajes; distinguir publicación, recepción, lectura y aceptación; aclarar asignaciones ambiguas; evitar duplicación; registrar decisiones y evidencias; escalar cuando corresponda. Descubre cuáles importan realmente. Clasifica impacto, costo, facilidad y riesgos.

### 4.3 Coordinación universal y especialización

Evalúa si todos los agentes deberían compartir un núcleo de competencias y qué debe ser universal frente a específico de roles. Incluye herramientas y capacidades no autónomas.

### 4.4 Arquitecturas

Compara arquitecturas centralizadas, jerárquicas, descentralizadas, distribuidas, híbridas, basadas en mensajes, memoria compartida, eventos, contratos y workflows. Evalúa ventajas, desventajas, costos, escalabilidad, tolerancia a fallos y complejidad. Elige por ajuste al ecosistema, no por popularidad.

## 5. Auditoría profunda del sistema actual de Softly

### 5.1 Directorios `say/`

Evalúa canales como `Softlysay`, `Katarinasay`, `Audelinesay` y otros existentes. ¿Qué necesidad resuelven? ¿Son necesarios? ¿Duplican información o fragmentan búsqueda? ¿Deberían ser directorios, buzones, eventos, mensajes u otra abstracción? No asumas que son correctos.

### 5.2 Directorios `shared/`

Evalúa qué se comparte, quién escribe y lee, cómo se organizan trabajos, evitan sobrescrituras, identifican responsables, distinguen borradores/entregas y gestionan versiones y conflictos. Determina si `shared/` y `say/` resuelven problemas distintos o se superponen.

### 5.3 Inbox, outbox y flujos

Audita `inbox/`, `outbox/`, `shared/`, `say/`, `entregable/`, `bitacora/` y equivalentes. Reconstruye el recorrido: necesidad, asignación, comunicación, recepción, trabajo, entrega, verificación, aceptación/observación/rechazo, registro y continuación/cierre. Identifica duplicaciones, ambigüedades, pasos innecesarios y pérdidas.

Pregunta: ¿diseñamos un sistema demasiado complicado para el problema? Si sí, propón una alternativa más sencilla.

### 5.4 Handoffs y continuidad

Evalúa contratos y transferencias. Distingue asignación, inicio, ejecución, publicación, recepción, lectura, aceptación, rechazo, retrabajo y cierre. Determina estados necesarios y contenido mínimo. No confundas contrato documental con enforcement técnico.

### 5.5 Sistema completo

Evalúa comunicación clara, coordinación, continuidad, trazabilidad, baja duplicación, costo de contexto, escalabilidad, tolerancia a errores y facilidad de adopción. No intentes salvar todos los directorios: elimina conceptualmente lo que sobre.

## 6. Propuestas de rediseño

Desarrolla al menos tres alternativas:

- **A — Conservadora:** conservar arquitectura y corregir deficiencias.
- **B — Simplificada:** reducir directorios, convenciones y pasos, manteniendo funciones esenciales.
- **C — Rediseño:** arquitectura distinta si la evidencia lo exige.

Para cada una: diagrama, componentes, flujo, responsabilidades, ventajas, desventajas, riesgos, costo, compatibilidad, manejo de errores y facilidad de adopción. Recomienda una.

## 7. Experimentación y validación

Propón pruebas de asignación, delegación, comunicación, recuperación de contexto, handoff, conflictos, duplicación, bloqueos, entregas incompletas e integración de resultados incompatibles. Define métricas: tiempo, intervención humana, duplicación, errores de asignación, rechazos, pérdida de información, retrabajo y costo de contexto. Distingue métricas propuestas de resultados medidos.

## 8. Reglas epistemológicas

Distingue HECHOS, HALLAZGOS, INFERENCIAS, HIPÓTESIS, PROPUESTAS e INCERTIDUMBRES. Conserva contradicciones y analiza su origen. No inventes funcionalidades, pruebas ni capacidades. No confundas archivo con aplicación, competencia declarada con validada ni arquitectura documentada con sistema ejecutado. No confirmes sospechas para complacer al gAto; contradícelas si la evidencia lo exige.

## 9. Entregables

Informe profundo con: resumen ejecutivo; metodología y fuentes; estado de investigación académica/técnica; definición de coordinación y coordinación propia; competencias universales y especializadas; formación formal versus cambios simples; auditoría de say/shared/inbox/outbox; reconstrucción del flujo; problemas y evidencia; comparación de arquitecturas; tres alternativas; recomendación; experimentos y métricas; riesgos e incertidumbres; decisiones reservadas al gAto; bibliografía y enlaces. Incluye diagramas cuando ayuden. Debe permitir decisiones reales, no ser una recopilación superficial.

## 10. Independencia y límites

Investiga independientemente de Softly. No coordines conclusiones antes de terminar ni adoptes las conclusiones de otro agente. No modifiques repositorios, contratos, schemas, directorios, prompts normativos ni producción. No implementes el rediseño. El gAto decide qué se adopta.

## 11. Pregunta final

Si diseñaras desde cero el sistema de coordinación de este ecosistema, ¿qué conservarías, eliminarías, simplificarías y construirías de otra manera? No temas concluir que ideas originales estaban equivocadas.