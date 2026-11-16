# Propuesta no normativa — Registro de identidades y capacidades
## RESET-CORE-2026-002

**Fecha:** 2026-11-16  
**Emite:** Softly  
**Estado:** PROPUESTA PARA DELIBERACIÓN; no modifica el registro vigente.  
**Autoridad de aprobación:** gAto.

## 1. Problema observado

El registro actual `schemas/agent-taxonomy-registry.json` (1.0.0) contiene nueve entradas `active-standby`:

- Tiffany / AgentDEV 1.0.0
- Tara / AgentSEC 1.0.0
- Thea / AgentMUS 1.0.0
- Tabata / AgentSCI 1.0.0
- Katarina / AgentDEV 1.1.0
- Melina / AgentMUS 1.0.0
- Audeline / Auditoría 1.0.0
- Aurora / Auditoría 1.0.0
- Autumn / Auditoría 1.0.0

La revisión confirma que:

- Softly no figura como identidad.
- Katarina figura en 1.1.0, mientras su casa canónica está en 2.0.1.
- Audeline apunta al paquete histórico del Laboratorio, no a su casa canónica actual.
- Aurora, Autumn y Melina aparecen disponibles pese a HOLDs y a la regla de identidad única auditora.
- El registro no es inventario exhaustivo de los paquetes TITAN ni de otros proyectos.
- El enum taxonómico admite AgentDEV, AgentSEC, AgentMUS, AgentSCI y Auditoría, pero no una categoría Core/System para Softly.
- `active-standby` describe disponibilidad declarada, no proceso vivo; aun así, puede confundirse con estado operativo.

El problema no se resuelve simplemente borrando seis entradas: sus capacidades, contratos y evidencia histórica deben preservarse.

## 2. Distinción propuesta

Separar cuatro conceptos que hoy están mezclados:

1. **Identidad operativa:** sujeto único que posee autoridad y responsabilidad dentro del ecosistema.
2. **Perfil de capacidad:** conjunto de competencias profesionales o técnicas que una identidad puede ejercer, sin constituir otra identidad invocable.
3. **Paquete documental:** repositorio/versionado que contiene contrato, permisos, capacidades y artefactos de una identidad o perfil.
4. **Instancia de runtime:** proceso concreto, con estado de ejecución, endpoint, lease y evidencia propia. Un paquete diseñado o una disponibilidad declarada no equivalen a una instancia viva.

Esta separación evita que una especialidad, paquete, canal privado o instancia se convierta accidentalmente en una cuarta identidad.

## 3. Modelo objetivo sujeto a aprobación

El RESET-CORE-2026-002 establece exactamente tres identidades operativas finales:

| Identidad | Casa canónica | Responsabilidad principal | Tratamiento del catálogo |
|---|---|---|---|
| Softly | `gatoscientist/Softly` | Núcleo, gobierno y coordinación general | Registrar como identidad Core, sin inventar aún una taxonomía AgentCORE/AgentSYS |
| Katarina | `gatoscientist/Katarina` | Ingeniería y desarrollo | Registrar versión canónica 2.0.1; asociar capacidades de desarrollo aprobadas |
| Audeline | `gatoscientist/Audeline` | Auditoría independiente | Registrar versión canónica vigente desde su casa propia; no depender de Aurora/Autumn |

Zoe se modelaría como **asignación temporal de supervisión**, no como cuarta identidad operativa permanente. Su asignación debe tener condición de término verificable y quedar fuera del catálogo permanente una vez cerrada.

## 4. Tratamiento de los perfiles existentes

Propuesta de preservación, no de eliminación:

- Tiffany, Tara, Thea y Tabata: conservar paquetes y competencias como perfiles/capacidades históricas. No invocar como identidades separadas bajo el reset.
- Melina: conservar como perfil musical independiente en HOLD, sin invocación ni disponibilidad operativa.
- Aurora y Autumn: conservar como paquetes fuente e historial de auditoría. Sus competencias pueden ser referencia documental, pero no identidades subordinadas ni participantes operativas.
- Paquetes especialistas de TITAN: mantener en el catálogo propio del producto TITAN; no convertirlos en identidades Softly.
- Lucyna y Andy de gAtoSD: pertenecen a un proyecto independiente y quedan fuera del registro Softly.
- PrimusPrivado: canal privado de Primus, no identidad adicional.

No se propone mapear automáticamente cada perfil a una de las tres identidades. La atribución de capacidades requiere decisión y trazabilidad.

## 5. Esquema de datos sugerido para una versión futura

Sin imponer nombres definitivos, una versión 2 podría separar:

- `identities[]`: `identity_id`, `name`, `canonical_repo`, `canonical_version`, `operational_state`, `owner`, `role`.
- `capability_profiles[]`: `profile_id`, `domain`, `capabilities[]`, `source_package`, `status`, `allowed_identity_ids[]`.
- `packages[]`: `package_id`, `repo`, `version`, `maturity`, `blob_or_commit`, `identity_id` o `profile_id`.
- `runtime_instances[]`: `instance_id`, `identity_id`, `runtime_state`, `process_id`, `endpoint`, `started_at`, `lease`, `evidence_refs[]`.
- `temporary_assignments[]`: `assignment_id`, `identity_id`, `scope`, `start_condition`, `end_condition`, `approver`, `status`.

La disponibilidad declarada debe separarse del estado de runtime. Un paquete puede existir y estar preservado sin estar disponible ni ejecutándose.

## 6. Decisión de taxonomía todavía abierta

No se decide aquí si Softly debe tener una taxonomía propia `AgentCORE`/`AgentSYS`, o si su función de gobierno/orquestación se expresa como capacidades del núcleo fuera de la taxonomía profesional.

Tampoco se resuelve si la coordinación sistémica es una capacidad transversal dentro de las tres dimensiones existentes o una dimensión adicional. La pregunta debe deliberarse explícitamente; no se debe alterar el enum para cerrar el debate por accidente.

## 7. Migración propuesta

1. Congelar el registro 1.0.0 como evidencia histórica y calcular SHA.
2. Audeline audita independientemente el modelo y la correspondencia entre identidades, capacidades y paquetes.
3. Katarina, una vez reconciliado su contrato/permisos, prepara una propuesta técnica de schema 2.0 sin tocar el registro vigente.
4. gAto decide taxonomía, asignación de capacidades y tratamiento de perfiles.
5. Validar el nuevo schema y los datos con pruebas positivas, negativas y semánticas.
6. Migrar en una rama separada; conservar el registro 1.0.0 y su historial.
7. Audeline revisa el diff; gAto autoriza la integración.
8. Actualizar índices, contratos, permisos, canales y documentación transversal.

## 8. Criterios de aceptación propuestos

- Exactamente tres identidades operativas finales.
- Softly, Katarina y Audeline tienen casas/versiones canónicas verificables.
- Ningún perfil histórico aparece como identidad operativa invocable.
- Las capacidades históricas se preservan y su procedencia es trazable.
- Zoe aparece solo como asignación temporal con término verificable.
- Paquetes de producto y proyectos independientes no se mezclan con el catálogo Softly.
- Estado de runtime no se infiere de madurez, disponibilidad ni existencia de archivos.
- El schema impide identidades/equipos subordinados no autorizados y valida referencias/evidencia.
- No se eliminan paquetes, ramas, respaldos ni historial como parte de la migración.

## 9. Límites de esta propuesta

Este documento no modifica `agent-taxonomy-registry.json`, sus schemas, contratos ni permisos. No autoriza crear identidades, invocar perfiles, activar agentes, ejecutar runtime, fusionar ramas o borrar paquetes. Toda decisión normativa queda reservada a gAto después de auditoría independiente.
