# PROMPT DE INVESTIGACIÓN PROFUNDA — SOFTLY
## Coordinación universal, optimización del sistema y rediseño de la arquitectura de colaboración

**Investigadora:** Softly  
**Dirección humana:** gAto  
**Modalidad:** Modo Investigación  
**Prioridad:** Alta  
**Tipo:** Investigación profunda, auditoría del propio sistema y propuesta arquitectónica  
**Carácter:** Autocrítico, exploratorio e independiente  
**Autorización:** Investigar, consultar fuentes, analizar y proponer. No implementar cambios ni modificar contratos normativos.

## 1. Mandato

Inicia una investigación profunda sobre coordinación entre agentes, coordinación de equipos y coordinación del propio trabajo. Examina críticamente el sistema que tú misma utilizas. No lo defiendas por ser tuyo ni asumas que sus directorios, contratos y flujos son correctos.

Descubre cómo debería funcionar el mejor sistema de coordinación para el ecosistema del gAto, usando evidencia académica, implementaciones reales, ingeniería y antecedentes de repositorios.

El gAto sospecha que el sistema actual, especialmente `say/`, `shared/`, `inbox/` y `outbox/`, podría estar mal diseñado. Investiga sin darlo por cierto. Si es innecesariamente complicado, propón simplificarlo; si tiene defectos estructurales, identifícalos; si está bien, demuéstralo. La lealtad al sistema no significa defender decisiones históricas.

## 2. Fuentes obligatorias

### 2.1 Repositorios autorizados

Investiga exclusivamente:
- `gatoscientist/Katarina`
- `gatoscientist/Cytryna`
- `gatoscientist/TITAN`
- `gatoscientist/Auditoria`
- `gatoscientist/Softly`
- `gatoscientist/Laboratorio-de-agentes`

No explores otros repositorios. Prioriza `gatoscientist/Softly`, reconstruyendo el sistema desde documentos y estructuras. Examina SOFTLY.md, CHECKPOINT.md, moldes, taxonomías, contratos, schemas, Softlysay, otros canales say, shared, inbox/outbox, entregables, bitácoras, actividad, observaciones, incidencias, handoffs y reglas de autoridad. No te limites a archivos centrales. Cuando una regla sea declarada, busca evidencia de aplicación y distingue ambas cosas.

### 2.2 Internet: investigación iterativa

Realiza búsquedas sucesivas en literatura académica, documentación de plataformas, protocolos y experiencias reales. Incluye Multi-Agent Coordination, Agent Orchestration, Distributed Agent Systems, Blackboard Systems, Shared Memory, Message Passing, Event-Driven Architecture, Task Allocation, Delegation Protocols, Workflow Engines, Agent Communication Protocols, Multi-Agent Collaboration, Human-Agent Coordination, Distributed Systems and Consistency, Organizational Theory y Team Cognition.

Busca casos donde arquitecturas hayan fracasado por complejidad, comunicación innecesaria o ambigüedad. Cada hallazgo debe generar nuevas preguntas cuando corresponda. Sigue referencias y registra enlaces. Prioriza fuentes originales verificables.

## 3. Pregunta central

¿Cómo diseñar un ecosistema en el que todos sus integrantes sepan coordinar y coordinarse, sin depender de un coordinador central para cada interacción?

Distingue:
- **Coordinar:** organizar trabajo ajeno, distribuir tareas, sincronizar equipos, gestionar dependencias, supervisar e integrar.
- **Coordinarse:** gestionar el propio trabajo con relación a otros, comprender responsabilidades, comunicar estados, entregar resultados, informar problemas y respetar dependencias.

Investiga si son dimensiones de una competencia o competencias distintas.

## 4. Coordinación como competencia universal

Investiga la hipótesis: todo integrante debe ser competente en coordinación, sin importar especialidad o jerarquía. Incluye Softly, Katarina, Audeline y equipo auditor, dirección, investigación, desarrollo, agentes especializados, gAto y herramientas/capacidades externas.

### 4.1 Formación formal

Evalúa si se necesita formación estructurada, qué debería estudiar un agente, qué modelos/metodologías/protocolos existen, qué conocimientos son transferibles y qué requiere práctica y evaluación.

### 4.2 Mejoras pequeñas

Identifica cambios sencillos en prompt, identidad, contrato, inicio, procedimientos, estructura de entrega, comunicación, estado, dependencias, ayuda y escalamiento que mejoren la coordinación. Busca el conjunto mínimo de alto impacto. Distingue evidencia de hipótesis.

### 4.3 Coordinación y especialización

Define cómo combinar competencia universal con especialidad, sin convertir a todos en coordinadores profesionales ni diluir sus dominios. Incluye herramientas no autónomas.

## 5. Auditoría de tu propio sistema

### 5.1 `Softlysay/`

Evalúa qué necesidad resuelve, si debe existir un canal por agente, si conviene carpeta por destinatario, si fragmenta información, cómo se detectan mensajes que requieren respuesta, cómo se distinguen comunicación informativa y asignación, y cómo se acredita recepción, lectura y aceptación. ¿Es correcta la abstracción say?

### 5.2 `shared/`

Evalúa qué debe compartirse, qué no, autoría, versiones, sobrescrituras, borradores, entregas, integración y recuperación. ¿Es buena abstracción o conviene reemplazarla?

### 5.3 Inbox, outbox y flujo documental

Reconstruye el ciclo de comunicación y trabajo. Examina `inbox/`, `outbox/`, `shared/`, `say/`, `entregable/` y `bitacora/`. Pregunta si necesitamos todos. Evalúa si se parece demasiado a correo cuando podría convenir una arquitectura de tareas, eventos, contratos o estados. Distingue mensaje, tarea, evento y documento persistente. No confundas contenedores físicos con responsabilidades.

### 5.4 Costo de coordinar

Examina tiempo de escribir/leer, duplicación, carga de contexto, búsqueda, pasos de transferencia, ambigüedad, errores, dependencia humana y retrabajo. Pregunta: ¿el sistema ayuda a trabajar o trabajamos para mantener el sistema?

### 5.5 Autocrítica sobre tu comportamiento

Busca episodios de interpretación incorrecta, confusión de destinos, delegaciones incompletas, lecturas insuficientes, actualizaciones prematuras, comunicación redundante, supuestos sobre estado ajeno, entregas poco accionables y dificultades para distinguir investigación y producción.

Determina si se relacionan con arquitectura, instrucciones, herramientas o interpretación. Separa causas inmediatas, factores contribuyentes e hipótesis de causa raíz. No atribuyas todo error a la arquitectura.

## 6. Coordinación y modos de trabajo

Considera como hipótesis los modos Fábrica, Fábrica Experimental e Investigación y Deliberación. Investiga si coordinación debe ser competencia transversal a todos. Evalúa cómo cambia al coordinar producción, experimento, investigación y proyectos múltiples. No conviertas aún esta clasificación en normativa.

## 7. Arquitecturas alternativas

Diseña:
- **A — Conservadora:** conservar estructura y corregir.
- **B — Simplificación:** reducir directorios, pasos y convenciones.
- **C — Nueva arquitectura:** rediseñar si la evidencia lo exige.

Para cada una incluye componentes, diagrama, flujo, comunicación, responsabilidades, estados, conflictos, entregas, aceptación, costos, ventajas, riesgos y compatibilidad. Recomienda una.

## 8. Optimización

Ordena mejoras por prioridad. Identifica qué puede cambiarse sin tocar arquitectura, qué requiere prompts, contratos, schemas, directorios o herramientas, y qué no vale la pena implementar. Prioriza alto impacto y bajo costo. No confundas elegancia con utilidad operacional.

## 9. Experimentación

Diseña pruebas comparativas entre agente sin mejoras, agente con instrucciones mínimas, agente con formación estructurada, agente con protocolos explícitos y equipos con arquitecturas diferentes.

Mide tiempo, errores, duplicación, calidad de entregas, pérdida de información, intervención humana, delegación, contexto e integración. Define hipótesis, variables, condiciones y criterios. No afirmes resultados no medidos.

## 10. Reglas de investigación

Distingue HECHOS, HALLAZGOS, INFERENCIAS, HIPÓTESIS, PROPUESTAS e INCERTIDUMBRES. Rastrea afirmaciones a fuentes. No conviertas preferencias en conclusiones. No supongas que el diseño es bueno por haberlo usado ni malo por presentar problemas. No confundas documentación con ejecución ni competencia declarada con demostrada. No busques complacer al gAto.

## 11. Entregables

Informe con resumen ejecutivo, metodología, bibliografía, estado de investigación, modelo de competencias, formación versus mejoras simples, auditoría del sistema, análisis say/shared/inbox/outbox, reconstrucción de flujo, problemas y causas, alternativas, optimización, experimentos, métricas, plan de transición, riesgos, incertidumbres y decisiones reservadas al gAto. Incluye diagramas y tablas cuando aporten. Debe permitir una decisión arquitectónica.

## 12. Independencia y límites

Investiga independientemente de Katarina. No solicites sus conclusiones ni adaptes tu informe para coincidir. No modifiques tu arquitectura, SOFTLY.md, schemas, moldes, contratos, taxonomías ni directorios. No implementes ni declares aprobadas propuestas. Tu responsabilidad es investigar, cuestionar, fundamentar y recomendar.

## 13. Preguntas finales

Si diseñaras desde cero el sistema de coordinación de Softly y del ecosistema:
1. ¿Construirías nuevamente `say/`, `shared/`, `inbox/` y `outbox/`, o elegirías otra arquitectura?
2. ¿Qué modificaciones mínimas harías para que cualquier agente, desde que es instanciado, sepa coordinar y coordinarse mucho mejor?

No protejas tu propio diseño. Investiga hasta encontrar la respuesta más sólida.