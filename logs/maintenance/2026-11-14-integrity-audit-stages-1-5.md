# Auditoría de integridad Softly — 2026-11-14

**Estado:** parcial y abierta. Corte verificado en `main`, HEAD `0f00037b60a9f40025d5773cd115c1da0232fb71`.
**Alcance:** árbol Git recursivo, 80 Markdown, índices, archivos estructurados, procedencia documental y diseño preventivo. Sin cambios destructivos ni cambios de configuración Git.

## 1. Inventario y PDF

El árbol recursivo devolvió 128 entradas: 94 blobs y 34 directorios; 80 Markdown y 9 PDF en `eL arenero del gAto/`. Se registraron para los nueve PDF sus rutas, tamaños y Git blob SHA en el README del arenero y en la matriz de procedencia.

**Inspección de contenido de los 9 PDF: NO EJECUTABLE EN ESTE ENTORNO.** La conexión GitHub disponible rechaza la descarga de PDF porque solo admite contenido UTF-8; no se obtuvieron los bytes. No se confunde inventario/hash Git con lectura o validación del documento. Los 8 PDF originales TITAN/Cytryna quedan además pendientes de cotejo con los PDF del arenero. No se declara equivalencia, duplicación ni respaldo independiente. No se borró ni movió ningún archivo.

## 2. Auditoría de 80 Markdown y navegación

Se recuperó el contenido de los 80 Markdown desde sus blobs Git y se comprobaron los destinos relativos de enlaces Markdown inline contra el árbol actual. Resultado: **0 destinos locales inexistentes detectados** en los enlaces capturados.

Límites: esta comprobación no valida URLs externas, fragmentos/anchors, enlaces HTML o referencias Markdown de definición no capturadas por el patrón, ni relaciones semánticas que no estén expresadas como enlaces. El README raíz todavía conserva una referencia operativa a las secciones 17.12/17.14 de una síntesis; conviene comprobar que esos números sigan siendo estables si la síntesis se reordena.

## 3. Archivos huérfanos y scaffolding

Los índices consultados enlazan las áreas principales y los artefactos conocidos; la historia de mantenimiento registra correcciones previas de documentos que carecían de entrada en sus índices. Seis directorios de evaluación/experimentos contienen solo README: `evaluations/datasets/`, `evaluations/plans/`, `evaluations/runs/`, `experiments/cases/`, `experiments/protocols/` y `experiments/results/`. Se clasifican como scaffolding documentado, no basura.

**Límite:** la pasada no ejecutó un grafo exhaustivo de referencias entrantes de cada blob y cada mención semántica. Por tanto, no certifica ausencia absoluta de huérfanos; no se encontró evidencia suficiente para borrar o mover nada. La diferencia de mayúsculas en las dos carpetas de arenero permanece intencional y documentada.

## 4. JSONL y contratos

Se leyeron `logs/activity.jsonl` y `logs/decisions.jsonl`: cada archivo contiene una línea y ambas líneas parsean como JSON válido. El primero registra `EVT-20261113-001`; el segundo `ADR-0001`. No existe contrato de eventos para validar estructura, fechas, unicidad global, referencias a archivos ni coherencia con commits.

`schemas/research-record.schema.json` solo modela fichas `SRC-YYYYMMDD-NNN`, exige URL y no representa fuentes locales/adjuntos ni eventos JSONL. Se conserva intacto. La propuesta de contratos JSONL queda en `schemas/jsonl-event-schema-proposal.md`.

## 5. Namespaces

Existe una propuesta descriptiva en `research/identifier-registry-proposal.md` para SRC, SRCSET, ING, SYN, SOFT-RES, ADR y EVT. No es normativa ni se aplicó migración. La propuesta de JSONL agrega validación de unicidad por namespace, referencias y transición no destructiva de IDs.

## 6. Seguridad Git

HEAD actual `0f00037b60a9f40025d5773cd115c1da0232fb71` tiene verificación de firma `unsigned`. En el historial de mantenimiento, `main` figura sin protección ni checks requeridos. En esta pasada, la API de GitHub rechazó la lectura de branch protection (403 por permisos de integración) y rulesets (403 por plan/privilegios); no se pudo revalidar ese estado en vivo. No se cambió ninguna configuración. Propuesta lista en `docs/security/git-governance-proposal.md`.

## 7. Cambios y límites

No se borraron, movieron ni renombraron archivos; no se modificaron agentes, contratos, JSONL ni esquemas vigentes. Las propuestas nuevas son documentos de diseño y no activan controles. No hay código runtime ni workflows CI en el repositorio, así que no corresponde declarar pruebas de funcionamiento de agentes.

## Criterios aún abiertos

1. Obtener los nueve PDF como archivos descargables y leerlos, registrar páginas/metadatos y hashes SHA-256 calculados sobre bytes.
2. Cotejar los ocho PDF originales contra candidatos concretos, con hash binario independiente.
3. Completar grafo de referencias entrantes, anchors, HTML, URLs externas y menciones semánticas.
4. Aprobar y versionar contratos JSONL y namespaces antes de cualquier validación obligatoria/migración.
5. Aprobar controles Git y probar recuperación desde un respaldo independiente.

**Conclusión:** navegación local Markdown revisada sin destinos rotos detectados; integridad documental global, inspección binaria y protección preventiva de Git siguen abiertas. No declarar Softly íntegra todavía.
