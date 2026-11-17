# Archivo Histórico Inactivo — v1.0-legacy

**Estado:** inactivo para Softly 1.1.  
**Propósito:** preservar genealogía, evidencia y contexto sin contaminar el arranque ni gobernar la operación vigente.

## Regla de carga

Ninguna instancia de Softly 1.1 carga estos materiales al despertar. El arranque se limita a `SOFTLY.md` y `CHECKPOINT.md`. Un documento de este archivo solo se consulta bajo demanda cuando una tarea concreta necesita verificar un antecedente. Su contenido histórico no prevalece sobre los contratos de Softly 1.1 ni sobre una instrucción vigente de gAto.

## Clasificación del legado

Se consideran superficie histórica inactiva, entre otros:

- Mandatos y expedientes de reset: `docs/governance/RESET-CORE-2026-001.md`, `docs/governance/RESET-CORE-2026-002.md`, dictámenes y rectificaciones asociados.
- Expedientes y referencias administrativas KAT-006, incluido `logs/2026-11-16-cierre-administrativo-kat-006-reinicio-integral.md`.
- Logs de hilos antiguos, bitácoras, eventos, registros de incidentes, conteos y consolidaciones históricas de ramas/PR.
- Handoffs anteriores, incluidos `docs/handoff/` y `agents/templates/handoff.md`.
- Canales, buzones y topologías direccionales antiguas, incluidos `*say/`, inbox/outbox físicos o equivalentes si aparecen en materiales históricos.
- Taxonomías, schemas, registros de identidad/capacidad y plantillas operativas deprecadas que no hayan sido adoptados expresamente por los contratos 1.1.
- Experimentos, evaluaciones, observaciones y decisiones antiguas que no formen parte del estado vigente.

Esta clasificación es semántica y de carga: **no mueve, borra ni reescribe** los archivos originales. La historia Git permanece intacta.

## Memoria de investigación preservada

`research/syntheses/` y `research/coordination/` se preservan como fuentes de conocimiento. No se clasifican como estado operativo ni se cargan al arranque. Se consultan bajo demanda, conservando sus referencias y contexto.

## Contratos vigentes

La fuente normativa operativa de Softly 1.1 es `SOFTLY.md`; su estado vivo está en `CHECKPOINT.md`; las únicas plantillas canónicas de artefactos operativos están en `contracts/`.

No reactivar un procedimiento heredado por el solo hecho de que exista en GitHub. Para recuperar una capacidad histórica se requiere una decisión explícita, un contrato vigente y evidencia de utilidad.
