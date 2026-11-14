# Cruce documental: estructura de agentes Soft y molde de creación

**Fecha de revisión:** 2026-11-14  
**Tipo:** síntesis interna de documentos entre repositorios  
**Estado:** análisis documental; no es un estándar aprobado ni una implementación.

## Propósito

Recuperar dos documentos valiosos que estaban en el arenero del repositorio Laboratorio de Agentes y compararlos con el modelo y el molde que ya viven en Softly. La meta es conservar la procedencia, evitar duplicar documentos completos y detectar aportes que merecen consideración.

## Documentos originales revisados

1. [Investigación: estructura física y documental de agentes](https://github.com/gatoscientist/Laboratorio-de-agentes/blob/main/eL%20arenero%20del%20gAto/INVESTIGACION/estructura-de-agentes-soft.md) — SHA del blob Git: `431949c2ddbdef8834b2e0365f4bae369f85d9f4`. Investigación fechada el 13-11-2026; se declara expresamente como propuesta arquitectónica pendiente, no como estándar ni runtime.
2. [Instrucciones para crear y mantener agentes Soft](https://github.com/gatoscientist/Laboratorio-de-agentes/blob/main/eL%20arenero%20del%20gAto/INSTRUCCIONES-PARA-CREAR-AGENTES-SOFT.md) — SHA del blob Git: `42b20aabb961a90a4d9eb3e078a2d2c82512800c`. Guía operativa inicial que complementa la investigación anterior.

## Documentos canónicos relacionados en Softly

- [Modelo de agentes reutilizables v0.1](../../docs/architecture/agent-model-v0.1.md): separa Agent Definition, Project Brief, Project Assignment y Work Session.
- [Molde universal de creación de agentes v0.1](../../agents/templates/agent-generation-mold.md): transforma un brief en una definición de agente portable, con autoridad, capacidades, memoria, herramientas, evaluación y aprobación.
- [Plantilla de perfil](../../agents/templates/agent-profile.md): estructura mínima del perfil profesional y sus límites.

Los documentos de Laboratorio no son copias idénticas de estos artefactos. Se complementan: la investigación explica fundamentos y separación de espacios; la guía describe una estructura física progresiva y criterios operativos; Softly formaliza el modelo lógico y el procedimiento de generación desde un brief.

## Aportes relevantes recuperados

### 1. Casa del agente y workspace del proyecto

La investigación distingue cuatro espacios: casa del agente, runtime/harness, workspace del proyecto y espacio común de equipo. La guía refuerza que el proyecto no es la casa del agente, que los agentes no necesitan acceder a las casas de otros y que los entregables pertenecen al proyecto.

Esto es coherente con el modelo de Softly, que separa definición portable, brief, asignación y sesión. La distinción debe mantenerse tanto en el diseño documental como en la futura implementación.

### 2. Crecimiento por etapas

La guía propone una estructura mínima y ampliable:

- **Etapa 0 — agente definido:** README, AGENT, PROFILE, CONTRACT y version.json.
- **Etapa 1 — preparado para trabajar:** instrucciones, expertise, skills, herramientas y permisos, cuando haya necesidad real.
- **Etapa 2 — continuidad:** memoria, estado, registros y changelog, cuando el agente requiera persistencia.
- **Etapa 3 — evaluación:** mapas de capacidades, casos, criterios y resultados cuando exista evidencia suficiente.

Aporte importante: no crear carpetas vacías para aparentar madurez. Incorporar componentes solo cuando tengan función, responsable y política.

### 3. Separación epistemológica y operacional

Los documentos distinguen conocimiento, memoria semántica, episódica y procedimental, estado temporal, registros de actividad y evaluación. Esta distinción evita convertir cualquier conversación o log en memoria indiscriminada.

La investigación también advierte que los logs autoritativos pueden requerir un servicio externo append-only; no deben depender de que el propio agente pueda reescribirlos.

### 4. Permisos y seguridad

La guía expresa con claridad que una instrucción de texto no es un control de seguridad. Los permisos deben aplicarse fuera del modelo mediante runtime, sandbox, ACL, herramientas intermediarias o mecanismos equivalentes.

La matriz propuesta diferencia lectura, escritura, propuesta de cambios, acceso a workspace y acceso a la casa de otros agentes. Es una referencia útil para futuras decisiones, pero no concede permisos por sí misma.

### 5. Contratos de herramientas y skills

Se recupera la distinción entre herramienta (operación concreta) y skill (procedimiento). Cada herramienta debe declarar entradas, salidas, permisos, efectos secundarios, errores, límites, responsable y versión.

### 6. Versionado y retiro

La guía enfatiza preservar versiones evaluadas, resultados históricos, entregables y aprendizajes al retirar generaciones. Esto refuerza el principio de Softly de no sobrescribir evidencia antigua.

## Relación y diferencias con el diseño actual

| Tema | Aporte de los documentos de Laboratorio | Estado en Softly |
|---|---|---|
| Separación casa/proyecto/runtime/equipo | Explicación explícita de cuatro espacios | Coherente con el modelo lógico; conviene mantenerlo como distinción transversal |
| Etapas de estructura | Progresión de Etapa 0 a 3 | No está formalizada como ciclo de estructura en el molde actual |
| Archivos mínimos | README, AGENT, PROFILE, CONTRACT, version.json | Coherente con el catálogo y plantillas actuales |
| Permisos técnicos | Matriz orientativa y enforcement fuera del modelo | El modelo lo declara; implementación pendiente |
| Memoria y estado | Tipos separados y retención | Coherente con el modelo, requiere pruebas y diseño operacional |
| Herramientas y skills | Contratos explícitos y distinción conceptual | Coherente con principios de Softly |
| Retiro/versionado | Preservación de generaciones y resultados | Coherente con gobierno y trazabilidad actuales |

## Límites de la revisión

- Se revisó el texto de los dos documentos internos y se contrastó con los documentos canónicos indicados.
- No se revalidaron en esta pasada todas las fuentes externas citadas en la investigación.
- No se inspeccionaron runtimes ni se ejecutaron pruebas.
- No se cambió el molde, el modelo, perfiles, contratos ni agentes.
- Los documentos originales permanecen intactos en el arenero del Laboratorio.

## Conclusiones provisionales

1. Los documentos aportan valor y no deben eliminarse como duplicados.
2. La guía es un complemento operativo del molde de Softly, no un reemplazo.
3. La progresión por etapas es un aporte concreto que conviene evaluar antes de incorporarlo a plantillas.
4. La separación entre casa, runtime, workspace y coordinación debe seguir siendo explícita.
5. La próxima validación útil es contrastar el molde con briefs reales y observar qué componentes de la estructura progresiva se necesitan de verdad.

**Estado:** síntesis documental incorporada a Softly; decisiones normativas e implementación pendientes.
