# Tercer ciclo de auditoría — unicidad de IDs y grafo documental

**Fecha:** 2026-11-14  
**Corte inicial:** `main` HEAD `3792bc250dc3a3d0c221758675ba2cd3ab5ff6a8`  
**Verificación posterior:** `main` HEAD `09f9322cbdfa6dc729e828d1b6a83a6a5834a2aa`  
**Alcance:** revisión manual de los 83 Markdown, declaraciones y referencias de IDs, enlaces locales, referencias semánticas y archivos sin referencias entrantes. Sin cambios normativos.

## 1. Unicidad global de identificadores

Se recuperaron y revisaron los 83 archivos Markdown del corte. Se rastrearon los namespaces presentes, sus declaraciones canónicas, repeticiones, referencias cruzadas y plantillas.

**Resultado: cero colisiones entre declaraciones canónicas de IDs en los 83 Markdown.** Los identificadores concretos observados son:

- `SRC-20261113-001` a `SRC-20261113-008`: ocho registros de fuente agrupados en una ficha de ingesta.
- `SRCSET-20261113-001`: un conjunto/panorama, referenciado desde bibliografía y ficha de fuente.
- `ING-20261113-001`: un evento de ingesta.
- `SYN-20261113-001`, `SYN-20261113-002`, `SYN-20261113-003`: tres síntesis, una declaración canónica por documento.
- `SOFT-RES-001`: una nota de investigación.
- `ADR-0001`: una decisión; el Markdown formal y la entrada de `logs/decisions.jsonl` son dos representaciones de la misma decisión, no dos asignaciones distintas.

Las repeticiones de esos valores en índices, matrices, notas, bitácoras y documentos de continuidad son referencias a la entidad canónica, no nuevas declaraciones. `EVT-20261113-001` está registrado en `activity.jsonl`; sus menciones en Markdown son referencias. `EXP-A` a `EXP-F` son etiquetas locales de experimentos dentro de una síntesis, no IDs del patrón fechado. `OBS-YYYYMMDD-NNN`, `EXP-YYYYMMDD-NNN`, `SRC-YYYYMMDD-NNN` y equivalentes son placeholders de plantillas, no asignaciones reales.

**Referencias externas diferenciadas:** `DEC-20261112-001` aparece dentro de una ruta de TITAN externa; no se declara como ID de Softly ni como archivo faltante del repositorio. La ficha de ingesta identifica explícitamente ocho fuentes, pero no hay ocho fichas Markdown separadas: se modelan como registros tabulares en una única nota. No se infiere colisión por esa decisión documental.

## 2. Grafo de referencias entrantes

Se revisaron los enlaces Markdown inline de los 83 documentos: **115 aristas locales** detectadas; todos los destinos resuelven en el árbol Git del corte. No se detectaron enlaces locales rotos.

La revisión de referencias entrantes identificó tres índices existentes que no estaban conectados desde el índice superior:
- `research/notes/README.md`
- `research/syntheses/README.md`
- `logs/derived/README.md`

Se corrigieron las entradas superiores: `research/README.md` enlaza ahora los índices de notas y síntesis; `logs/README.md` enlaza el índice de derivados. Además, el índice de notas lista sus tres notas históricas y el cruce documental. Tras la corrección, **no quedan archivos Markdown sin referencia entrante**, salvo `README.md`, que es la portada/raíz y no requiere un padre.

## 3. Dependencias semánticas identificadas

- `ING-20261113-001` agrupa `SRC-20261113-001` a `SRC-20261113-008`; la ficha de ingesta enlaza a `SYN-20261113-002`.
- `SRCSET-20261113-001` conecta bibliografía con el panorama de fuentes.
- Las tres `SYN` están enlazadas desde los índices y citadas desde los documentos de investigación/continuidad pertinentes.
- `ADR-0001` enlaza el registro JSONL con su artefacto formal reconstruido.
- `SOFT-RES-001` está definido en una nota y listado desde el índice de investigación.
- Las etiquetas `EXP-A` a `EXP-F` describen líneas experimentales dentro de SYN-001; no tienen fichas de experimento independientes y no se presentan como experimentos ejecutados.
- El documento de ingesta deja el original SOFA Agent como artefacto pendiente de incorporación; es una dependencia externa declarada, no un huérfano local oculto.
- Los ocho títulos de fuentes TITAN/Cytryna permanecen como registros declarados; las discrepancias de título con algunos PDF del arenero siguen sin cotejo. Este ciclo no inspeccionó PDF ni cambió esa clasificación.

## 4. Congelamiento de propuestas

Por instrucción de gAto, quedan congeladas y sin aprobación ni implementación:
- `research/identifier-registry-proposal.md`
- `schemas/jsonl-event-schema-proposal.md`
- `docs/security/git-governance-proposal.md`

Los tres documentos indican explícitamente que no son normativos y que no deben revisarse ni activarse hasta después del tercer ciclo de auditoría. No se alteraron schemas vigentes, JSONL, configuración Git, agentes ni contratos.

## 5. Cambios y verificación

Se actualizaron los índices de investigación, notas y bitácora; se marcaron las tres propuestas como congeladas; se creó este informe. Los archivos modificados se releen desde GitHub. Árbol posterior: 131 entradas, 97 blobs, 34 directorios y 83 Markdown. HEAD final verificado: `09f9322cbdfa6dc729e828d1b6a83a6a5834a2aa`.

## Cierre

**Cerrado para el alcance dependiente de Softly:** unicidad de declaraciones canónicas de IDs, navegación local inline, índices faltantes y referencias semánticas internas identificables en los 83 Markdown. No se declara integridad global de fuentes binarias ni se reabren las propuestas. No se detectaron archivos Markdown huérfanos después de corregir los tres índices.
