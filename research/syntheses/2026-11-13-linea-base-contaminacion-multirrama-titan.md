# SYN-20261113-001 — Línea base de contaminación multi-rama en TITAN

**Fecha de observación:** 2026-11-13 (America/Santiago)  
**Repositorio observado:** `gatoscientist/TITAN`  
**Rama principal:** `main`  
**Propósito:** establecer una línea base reproducible antes del ingreso de una nueva generación de agentes.  
**Estado:** investigación preliminar; no es auditoría final ni autorización de limpieza.

## 1. Pregunta de investigación

¿Qué residuos estructurales, documentales y organizacionales dejaron los agentes de desarrollo de TITAN, y qué parte de ese residuo se explica por la proliferación de ramas?

La hipótesis de trabajo es que la contaminación no se limita a archivos sobrantes: también puede incluir ramas paralelas, trabajo divergente, documentación distribuida, duplicación de entregables, autoridad de escritura ambigua y contexto histórico que los agentes entrantes podrían interpretar como precedente operativo.

Esta hipótesis debe contrastarse con el contenido de los ZIP históricos y con una nueva medición posterior a la limpieza.

## 2. Snapshot observado

El inventario se obtuvo leyendo las referencias de las siete ramas visibles en GitHub y recorriendo recursivamente sus árboles Git. Los conteos son archivos versionados por árbol; no son tamaños en disco ni conteos de archivos únicos globales.

| Rama | Archivos totales | DEVAGENTS/ | devteam/ | audit/ | logs/ | tests/ |
|---|---:|---:|---:|---:|---:|---:|
| main | 28 | 0 | 0 | 0 | 6 | 4 |
| audit/tania-pre-audeline-20261112 | 68 | 40 | 0 | 5 | 3 | 3 |
| debug/inferencia-deliberacion | 38 | 0 | 0 | 0 | 3 | 6 |
| feat/capacidades-por-dominio | 32 | 0 | 0 | 0 | 3 | 3 |
| feature/autonomia-agentes | 12 | 0 | 0 | 0 | 2 | 0 |
| work/devteam-governance-20261112 | 87 | 47 | 6 | 7 | 5 | 3 |
| work/tania-core-recovery-20261112 | 95 | 50 | 0 | 5 | 16 | 3 |

**Lectura inmediata:**
- Hay seis ramas además de `main`.
- Tres ramas históricas conservan entre 40 y 50 archivos bajo `DEVAGENTS/`.
- `work/devteam-governance-20261112` conserva además seis archivos bajo `devteam/`.
- Las dos ramas de trabajo conservan registros de auditoría y logs que no están en el árbol actual de `main`.
- La rama `audit/tania-pre-audeline-20261112` conserva un expediente específico de preparación de auditoría externa.
- Las tres ramas `debug/`, `feat/` y `feature/` no contienen `DEVAGENTS/` en sus árboles actuales, pero siguen siendo ramas históricas independientes.

Los árboles se identificaron mediante estos commits:
- `main`: `e5f00544023d2fa9e78367bf50e8e56e77ad20d6`
- `audit/tania-pre-audeline-20261112`: `57b460073c49b1c6074042b7158515ac7bf0e42d`
- `debug/inferencia-deliberacion`: `3635a0983826cdcd18f83562a169bf0aebe858d5`
- `feat/capacidades-por-dominio`: `358bc98934ee1e5982bbc12635b39dfe44c4e2c3`
- `feature/autonomia-agentes`: `3aed1462ad5268562d92bbec6dcdede05fb78e91`
- `work/devteam-governance-20261112`: `15f175da3ac4b7f9ed83faba92bdefc16ef525fe`
- `work/tania-core-recovery-20261112`: `08b75de0a22f6a39ef9153811d7ed3046af6c99b`

## 3. Evidencia organizacional encontrada

### 3.1 Aislamiento por ramas como regla de trabajo

El expediente `DEVAGENTS/AGENTEDEV/work/DEV-20261112-CORE-001-recuperacion-nucleo.md`, preservado en `work/tania-core-recovery-20261112`, declara:
- una rama aislada de recuperación como parte de la fase de integridad y baseline;
- límites de alcance entre Tania (motor), Teresa (GUI) y Trinidad (modelos matemáticos);
- cambios de contratos e interfaces compartidas sujetos a propuesta de impacto y coordinación;
- cambios pequeños y revisables;
- prohibición de fusionar a `main` o declarar entrega sin pruebas en el entorno objetivo y revisión cruzada.

Esto evidencia una estrategia de aislamiento y coordinación. Por sí sola no demuestra que cada rama haya sido creada por un agente sin autorización ni que toda rama fuera innecesaria.

### 3.2 Advertencias explícitas sobre integración

El expediente `DEVAGENTS/AGENTEDEV/audit/AUD-20261112-002-pre-audeline.md`, preservado en `audit/tania-pre-audeline-20261112`, registra que, al preparar esa auditoría:
- `work/tania-core-recovery-20261112` estaba 35 commits por delante y 2 por detrás de `main`;
- PR #1 (`feature/autonomia-agentes`), PR #2 (`debug/inferencia-deliberacion`) y PR #3 (`feat/capacidades-por-dominio`) aparecían abiertas y no fusionadas;
- las tres PR reportaban `mergeable=false`;
- se recomendaba reconciliar ramas divergentes y revisar PR antes de integrar.

Estos son datos declarados por el expediente en su fecha de elaboración. No se presentan como estado actual de PR ni como comparación actual de commits.

### 3.3 Ambigüedad de autoridad

La documentación disponible muestra separación de dominios y restricciones de cambios compartidos, pero aún no permite concluir por sí sola que existiera una contradicción formal de permisos. La hipótesis de que los agentes respondieron a ambigüedad de autoridad creando ramas debe comprobarse leyendo los contratos, instrucciones de cada agente, reglas de escritura y comentarios de commits de cada línea histórica.

## 4. Limpieza registrada en main

El commit `e5f00544023d2fa9e78367bf50e8e56e77ad20d6` (`Limpieza Agentes Soft`) eliminó:
- 86 archivos de `DEVAGENTS/`;
- 10 archivos de `audit/` en la raíz;
- total: 96 archivos y 5.829 líneas eliminadas.

El árbol actual de `main` no contiene `DEVAGENTS/`, `devteam/` ni `audit/`.

**Importante:** la limpieza de `main` no elimina el contenido de las otras ramas ni el historial Git. Este snapshot registra que las seis ramas históricas seguían existiendo al momento de la observación.

## 5. Qué medir cuando se retiren las ramas históricas

La comparación posterior debe distinguir:

1. **Residuo de ramas:** número de ramas no principales antes/después; nombres y referencias archivadas.
2. **Residuo documental:** archivos y bytes bajo `DEVAGENTS/`, `devteam/`, auditorías, handoffs, work, research, logs y artefactos auxiliares.
3. **Duplicación:** mismo contenido/hash bajo distintas rutas o ramas; entregables repetidos con nombres distintos.
4. **Divergencia:** commits exclusivos por rama, commits sin integrar y cambios que no llegaron a `main`.
5. **Residuo de autoridad:** instrucciones incompatibles, permisos contradictorios, límites de escritura y reglas de integración.
6. **Residuo operativo:** scripts temporales, diagnósticos, logs, respaldos y datos sensibles que queden en áreas compartidas.
7. **Exposición histórica:** qué puede leer un agente nuevo desde la rama principal, desde archivos del proyecto y desde archivos de respaldo.

No se debe sumar el número de archivos de todas las ramas como si fueran únicos: los árboles comparten muchos archivos. Para medir volumen real se necesitan hashes de blobs, tamaños y comparación de conjuntos.

## 6. Protocolo para la próxima generación de agentes

La línea base sugiere probar una política explícita y observable:
- trabajar exclusivamente en la rama principal, salvo autorización humana explícita para una excepción;
- no crear ramas por iniciativa propia;
- no crear copias o snapshots dentro del repositorio de trabajo como sustituto de control de cambios;
- solicitar permiso antes de modificar archivos fuera del dominio asignado;
- registrar bloqueos de autoridad como incidencias, no resolverlos creando ramas;
- dejar un registro de cambios y entregables acotado, con rutas y motivo;
- al terminar, reportar archivos creados, modificados y eliminados, además de pruebas ejecutadas y no ejecutadas.

Esta es una propuesta experimental para el siguiente ciclo, no una política ya aprobada.

## 7. Límites y próximos pasos

- No se han inspeccionado internamente todos los ZIP de ramas depositados en Laboratorio de Agentes.
- No se ha comparado el conjunto completo de blobs para determinar archivos únicos y duplicados.
- No se ha reconstruido todavía el grafo completo de commits ni el contenido de todas las PR históricas.
- No se ha demostrado causalidad entre ambigüedad de autoridad y creación de ramas.
- No se ha medido aún el comportamiento de los nuevos agentes; esta nota solo prepara la línea base.

**Próximo paso:** cuando el responsable termine de archivar y eliminar las ramas históricas, verificar que quede solo `main`, inspeccionar cada ZIP con nombre de rama, extraer manifiestos y hashes, y contrastar los resultados con esta línea base antes de iniciar el nuevo experimento.

## 8. Fuentes primarias consultadas

- GitHub API: ramas y árboles recursivos de `gatoscientist/TITAN`, observación del 2026-11-13.
- Commit TITAN `e5f00544023d2fa9e78367bf50e8e56e77ad20d6`: limpieza de `DEVAGENTS/` y `audit/`.
- `DEVAGENTS/AGENTEDEV/work/DEV-20261112-CORE-001-recuperacion-nucleo.md`, rama `work/tania-core-recovery-20261112`.
- `DEVAGENTS/AGENTEDEV/audit/AUD-20261112-002-pre-audeline.md`, rama `audit/tania-pre-audeline-20261112`.
- `DEVAGENTS/AGENTEGUI/audit/AUDIT-20261112-002-validacion-runtime-gui.md`, rama `work/tania-core-recovery-20261112`.
