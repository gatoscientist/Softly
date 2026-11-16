# ENCARGO DE AUDITORÍA INDEPENDIENTE — REGISTRO V2

**Misión:** AUD-RESET-002-REGISTRY-V2  
**Emisor:** Softly, bajo Dictamen de Dirección de 2026-11-16  
**Destinataria:** Audeline  
**Prioridad:** Alta  
**Estado:** revisión solicitada; no asumir aprobación.

## Mandato

Auditar independientemente la migración documental del registro histórico 1.0.0 al modelo v2 preparada en la rama `migration/registry-v2-reset-core-002` del repositorio `gatoscientist/Softly`.

## Artefactos

- `schemas/agent-taxonomy-registry.json` (v2.0.0 propuesto)
- `schemas/agent-taxonomy.schema.json` (schema v2)
- `schemas/archive/agent-taxonomy-registry-1.0.0.json`
- `schemas/archive/agent-taxonomy.schema-1.0.0.json`
- `docs/governance/MIGRACION-REGISTRO-IDENTIDADES-V2-RESET-CORE-002.md`
- PR de migración, que se publicará en Softly.

## Verificaciones obligatorias

1. Exactamente tres identidades operativas: Softly, Katarina y Audeline; casas y versiones canónicas contrastadas directamente en sus repositorios.
2. Zoe figura únicamente como asignación temporal, con condición de término doble: dictamen final de Audeline y confirmación expresa de gAto.
3. Paquetes candidate-unassigned e históricos sin autoridad operativa; ninguna capacidad implica identidad, invocación, herencia o permiso.
4. Correspondencia de dominios, especialidades y capacidades con las fuentes; identificar cualquier atribución errónea, exagerada o sin evidencia.
5. Revisar la propuesta de capacidades de Tiffany, Tara, Thea, Tabata, Melina, Aurora y Autumn. Confirmar qué es reutilizable, qué debe quedar sin asignar y qué destino propuesto contradice contratos.
6. Revisar explícitamente la capacidad candidata de coordinación sistémica y la pregunta de Katarina sobre cobertura de la orquestación.
7. Validar el JSON contra el schema, incluidos límites de cardinalidad, IDs, referencias y estados.
8. Confirmar que la versión histórica 1.0.0 se preserva íntegramente y que su blob SHA coincide con el origen.
9. Confirmar que Runtime y KAT-006 no reaparecen como requisitos ni dependencias.
10. Emitir dictamen GO / GO CON RESERVAS / NO-GO con evidencias, SHA, hallazgos y correcciones requeridas.

No modificar la rama de migración ni autoaprobarla. La revisión debe ser independiente y quedar persistida en la casa canónica de Audeline y referenciada en el issue #7. Si hay correcciones, entregar hallazgos concretos a Softly/Katarina.

## Criterio

La migración no se integra a `main` hasta contar con dictamen independiente favorable. La auditoría no debe bloquear ni detener tareas paralelas de ramas, PR y respaldos.
