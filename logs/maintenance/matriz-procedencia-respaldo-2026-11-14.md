# Matriz de procedencia y respaldo — línea base 2026-11-14

- **Estado:** inventario preliminar; no es certificación de integridad ni de respaldo.
- **Repositorio:** `gatoscientist/Softly`, rama `main`.
- **Corte consultado:** HEAD `e990c9304112167bda1b27210f90f1ab7d18d422`.
- **Objetivo:** registrar origen conocido, identidad Git, inspección, respaldo y decisión segura para los materiales documentales identificados.
- **Regla:** no eliminar, mover ni sobrescribir materiales por similitud de nombre, tamaño o tema. La eliminación exige respaldo verificable y registro de limpieza conforme a las instrucciones del arenero.

## 1. Inventario del arenero

Los tamaños y hashes siguientes provienen del índice `eL arenero del gAto/README.md` y corresponden a blobs Git del repositorio. No demuestran por sí solos el contenido ni la existencia de una copia independiente.

| Archivo | Tipo / tamaño | Blob SHA | Inspección del contenido | Respaldo demostrado | Estado / acción |
|---|---:|---|---|---|---|
| Arquitectura de Agentes Blandos.pdf | PDF · 2.270.214 B | `c8d45d2e48d4605d75671f1afc0f635dad16303c` | No inspeccionado | No | Conservar; inspección pendiente |
| Auditoría TITAN.pdf | PDF · 314.786 B | `f16511bace92cb0ba75a077f8110837f89952409` | Texto indexado consultado; binario exacto no cotejado | Biblioteca: un registro de mismo nombre y tamaño; sin cotejo binario | Coincidencia posible, no demostrada; no borrar |
| Auditoría de Fusión de Agentes.pdf | PDF · 280.377 B | `cfd3479003c1b34d7f8a4682473812f051248096` | No inspeccionado | No | Conservar; inspección pendiente |
| Auditoría y refactorización de código Titan.pdf | PDF · 214.535 B | `2fb15f8097cf866164088dcf3514ffaa06fc9eb7` | No inspeccionado | No | Conservar; inspección pendiente |
| Cytryna fusión de agentes blandos en el agente duro y costo de limpieza.pdf | PDF · 164.558 B | `f771ad179983f2bfcbbef35b62e2ef774f7f702d` | No inspeccionado | No | Conservar; inspección pendiente |
| Informe_Auditoria_TITAN_2026-11-12.pdf | PDF · 44.362 B | `0bb722f46ca991d833221c76b8c268736e02661b` | No inspeccionado | No | Conservar; inspección pendiente |
| Manual de Onboarding Multidisciplinario — Proyecto TITAN.pdf | PDF · 568.084 B | `1f05e1c5e1615f510908f3148c5a4c8a9dbf792b` | No inspeccionado en esta pasada | No demostrado para este blob | Conservar; inspección y cotejo pendientes |
| Revisión de código y consejos - Claude.pdf | PDF · 116.916 B | `1ca24f0f994762aa475b3a2e19363afda4e793aa` | No inspeccionado | No | Conservar; inspección pendiente |
| Revisión de código y consejos.pdf | PDF · 120.359 B | `da9d4f097c29139a61c7ff16c91f964280f85c27` | No inspeccionado | No | Conservar; inspección pendiente |
| el gAto dice.txt | TXT · 358 B | `3275a37e61c651994b63c0525e8da643d0632a2d` | Leído según el índice: pide postergar el orden de la casa y registrar futuras limpiezas | No aplica / no demostrado | Conservar; no confundir con el TXT que gAto dijo haber eliminado |

**Total registrado:** 10 archivos (9 PDF y 1 TXT). La tabla refleja el inventario publicado en el README del arenero; no equivale a un recorrido recursivo certificado de todo el repositorio.

## 2. cAjita

- Ruta comprobada: `cAjita del gAto/`.
- Archivos observados: `README.md` e `iNstrucciones.md`.
- El README declara que actualmente no hay otros archivos registrados.
- La instrucción indica consultar el contenido cuando se necesite contexto o exista una duda.
- No se identificó material adicional en esa ruta durante esta consulta.
- **Acción:** conservar; no tratarla como zona de limpieza. Si se incorpora material, registrar procedencia y enlazarlo desde el documento de trabajo correspondiente.

## 3. Anomalías estructurales y de trazabilidad

### 3.1 Dos rutas de arenero con distinta capitalización

Coexisten:
- `eL arenero del gAto/`: contiene el inventario de materiales y su README.
- `eL aRenero del gAto/`: contiene README e instrucciones de limpieza.

Git distingue mayúsculas y minúsculas. Los README explican la diferencia y enlazan ambas ubicaciones. No se renombra, fusiona ni elimina ninguna ruta sin decisión explícita y verificación de referencias.

### 3.2 Posible duplicación de Auditoría TITAN.pdf

El inventario actual de la Biblioteca muestra un único registro `Auditoría TITAN.pdf` de 314.786 bytes; no aparece un segundo registro `Auditoría TITAN(1).pdf`. El índice de texto ofrece fragmentos de un informe de cuatro páginas. El PDF del arenero tiene el mismo tamaño, pero no se pudo comparar el contenido binario ni calcular un hash independiente. Se corrige la anotación previa que afirmaba la existencia de dos registros. No se declara duplicación binaria ni se elimina ninguna copia.

### 3.3 Materiales mencionados fuera del inventario

Un registro anterior de mantenimiento menciona `Audelin.zip` en una ruta auditada, pero no aporta en esta matriz una ruta verificable dentro del arenero de Softly ni inspección de su contenido. Se mantiene como pista pendiente de localizar, no como elemento confirmado de este inventario.

### 3.4 Archivo TXT eliminado no identificado

El README del arenero declara expresamente que `el gAto dice.txt` permanece y no contiene la frase «pico pal que lee». Por tanto, no debe confundirse con el TXT que gAto dijo haber eliminado. La identidad y ruta de ese archivo eliminado no están demostradas en este árbol.

## 4. Hallazgos de la línea base

1. Existe inventario de 10 elementos del arenero, pero la mayoría de los binarios aún no están inspeccionados.
2. La trazabilidad es parcial: hay hashes Git y tamaños para los archivos del arenero, pero faltan fecha de incorporación, aportante/origen específico, finalidad, referencias de uso y estado de respaldo verificable por elemento.
3. La cAjita tiene una política de conservación clara y un inventario pequeño.
4. Las dos rutas del arenero están documentadas como distintas; la duplicidad nominal es una fuente de error operativo, no autorización para fusionarlas.
5. Hay una coincidencia de nombre y tamaño entre el PDF del arenero y un único registro de Biblioteca; requiere cotejo binario y no prueba duplicación.
6. No hay evidencia suficiente para eliminar ningún archivo del inventario.

## 5. Próximas acciones seguras

1. **Completado:** obtener la enumeración recursiva completa de `main` y reconciliarla con los índices principales.
2. Inspeccionar internamente los nueve PDF, registrar páginas, contenido, metadatos útiles y hash criptográfico calculado sobre cada archivo descargado. No hay ZIP en el árbol actual de Softly.
3. Localizar el origen y destino de cada artefacto y buscar respaldos independientes; registrar rutas, hashes y versiones.
4. **Completado parcialmente:** se detectaron y enlazaron tres documentos sin enlace desde sus índices. Se comprobaron todos los enlaces Markdown locales en los 76 archivos y no se encontraron destinos locales rotos; quedan pendientes referencias externas, relaciones semánticas y dependencias no expresadas como enlaces.
5. Añadir metadatos de procedencia solo cuando estén respaldados por evidencia; marcar desconocidos como desconocidos.
6. Proponer acciones de clasificación o limpieza por separado. No ejecutar borrados hasta demostrar respaldo, identidad y ausencia de dependencias.

## 6. Criterio de cierre

Esta matriz solo podrá declararse completa cuando:
- el inventario recursivo del árbol esté reconciliado con los índices;
- cada archivo relevante tenga origen, propósito, versión, hash y estado de respaldo o una declaración explícita de desconocido;
- los binarios hayan sido inspeccionados o estén justificados como no inspeccionables;
- enlaces y referencias hayan sido comprobados;
- los hallazgos y decisiones tengan evidencia reproducible;
- toda intervención esté registrada y verificada en Git.

**Estado actual: ABIERTO.** No se ha certificado la integridad total del repositorio, no se han validado los PDF/ZIP y no se ha autorizado ninguna eliminación.


## 7. Auditoría recursiva del árbol Git — corte 2026-11-14

Árbol consultado: `main`, HEAD `99783ed48aec2e289b26c94d6a7966a9fdb27335`; respuesta recursiva completa (`truncated=false`).

- 125 entradas: 91 blobs y 34 directorios.
- 77 archivos Markdown, incluidos 31 README.
- 9 PDF, 1 TXT, 2 JSONL y 1 JSON; 1 archivo `.gitattributes`.
- No hay archivos ZIP en el árbol de Softly.
- No se encontraron dos blobs con el mismo SHA dentro del árbol actual.
- La única colisión de rutas ignorando mayúsculas/minúsculas corresponde a `eL aRenero del gAto/` y `eL arenero del gAto/`, incluidas sus respectivas README. Es una diferencia ya conocida y documentada; no se fusionó.
- Seis directorios contienen únicamente README: `evaluations/datasets/`, `evaluations/plans/`, `evaluations/runs/`, `experiments/cases/`, `experiments/protocols/` y `experiments/results/`. Se clasifican como estructuras preparadas sin artefactos todavía, no como archivos huérfanos ni basura. Se conservan.

### Archivos que estaban sin enlace desde sus índices

Se detectaron y enlazaron desde sus índices:
- `archive/threads/2026-11-13-hilo-audelin.md` desde `archive/README.md`.
- `logs/2026-11-13-identity-directive-and-thread-closure.md` desde `logs/README.md`.
- `research/bibliography.md` desde `research/README.md`.
- `agents/profiles/audelin.md` desde `agents/profiles/README.md`.
- `decisions/template-adr.md` desde `decisions/README.md`.
- `logs/derived/Hiloderivado.md` desde `logs/derived/README.md`.
- `observations/template-observation.md` desde `observations/README.md`.
- `schemas/research-record.schema.json` desde el nuevo `schemas/README.md`.
- `decisions/ADR-0001-laboratorio-documental-antes-de-runtime.md` desde `decisions/README.md`; el documento se reconstruyó desde la entrada `ADR-0001` de `logs/decisions.jsonl` porque faltaba el artefacto formal.

No se movieron ni eliminaron estos archivos; la corrección fue de navegación.

### Referencias a estructuras inexistentes corregidas

- `README.md` todavía señalaba la sección 17.12 como prioridad inmediata; se alineó con la prioridad vigente de integridad de Softly y la pausa del desarrollo de agentes.
- `logs/README.md` enumeraba `incidents.jsonl` y `observations.jsonl` como archivos presentes, aunque no existen en el árbol. Ahora se declara explícitamente que aún no existen.
- `experiments/README.md` describía un directorio `artifacts/` que no existe; ahora aclara que los artefactos se incorporarán cuando un experimento los requiera.

### Límite de inspección binaria

La API de GitHub permite recuperar los PDF como base64, pero el entorno de inspección disponible no permite materializar esos bytes directamente desde el conector. La Biblioteca ofrece texto indexado para un único `Auditoría TITAN.pdf`, pero no permite cotejar el binario del repositorio. Los otros ocho PDF no tienen una copia identificada en el inventario de Biblioteca consultado. Por tanto, el contenido binario de los nueve PDF sigue pendiente de inspección; no se declaran validados.

**Resultado de esta pasada:** inventario recursivo completo y clasificaciones estructurales verificadas; navegación e instrucciones de prioridad corregidas; ninguna eliminación realizada. La auditoría de enlaces Markdown locales se ejecutó sobre los 77 archivos del árbol en siete lotes y no detectó destinos locales rotos. Tras recuperar ADR-0001, se verificó de forma dirigida el enlace actualizado de `decisions/README.md` y el nuevo documento, completando la cobertura local de los 78 Markdown actuales. El análisis no valida URLs externas, enlaces de referencia no capturados por el patrón de enlaces inline ni dependencias semánticas no expresadas como enlaces.


## 8. Verificación de enlaces Markdown locales

Se inspeccionaron los 77 archivos `.md` del árbol de corte mediante lectura desde GitHub y resolución de destinos relativos de enlaces Markdown inline. **Resultado: 0 destinos locales rotos detectados.** Después de crear ADR-0001, se comprobó también el único enlace nuevo y la existencia del documento; no se detectaron destinos locales rotos en los 78 Markdown actuales. Los destinos absolutos HTTP/HTTPS y las referencias externas se excluyeron de esta comprobación y no se consideran validados. Tampoco se certifican dependencias semánticas que no estén expresadas como enlaces.


## 9. Índices complementarios y recuento final de enlaces

Se añadieron referencias directas para el perfil Audelin, la plantilla ADR, el derivado Hiloderivado, la plantilla de observación y el esquema JSON de investigación. Se creó `schemas/README.md` para que el esquema no quede como artefacto sin índice.

La auditoría completa inicial cubrió 77 Markdown en siete lotes; tras la creación de ADR-0001 se verificó de forma dirigida el enlace de su índice y el documento nuevo. La cobertura resultante comprende los **78 archivos Markdown actuales**. **Resultado: cero destinos locales rotos detectados.** Las URLs externas y las dependencias no expresadas como enlaces siguen fuera de alcance.


## 10. Recuperación de ADR-0001 y perfil operativo del repositorio

El registro `logs/decisions.jsonl` declaraba una decisión aceptada `ADR-0001`, pero el archivo correspondiente no existía. Se reconstruyó `decisions/ADR-0001-laboratorio-documental-antes-de-runtime.md` usando exclusivamente los campos de esa entrada (fecha, estado, título, contexto, decisión, rationale, condición de revisión y commit relacionado), se explicitó la procedencia de la reconstrucción y se enlazó desde `decisions/README.md`. El ID de decisión ahora tiene su artefacto documental.

El árbol contiene Markdown, PDF, TXT, JSONL, JSON y `.gitattributes`; no contiene código ejecutable ni workflows de CI. Softly se define como laboratorio documental y de investigación, no como runtime. Por tanto, esta auditoría puede verificar integridad documental y de Git, pero no certificar un funcionamiento runtime inexistente en este repositorio.

El registro de actividad lista rutas de directorios como artefactos del bootstrap. Esas rutas están presentes como árboles Git; no son archivos faltantes.


**Recuento tras la recuperación de ADR-0001:** en la verificación posterior, `main` contenía 126 entradas (92 blobs y 34 directorios), 78 Markdown y 31 README. La ADR reconstruida y su índice están presentes. No se encontraron blobs duplicados por SHA. Este recuento corresponde al árbol verificado antes de la actualización actual de esta matriz; los commits de mantenimiento posteriores preservan el mismo conjunto de rutas salvo esta revisión documental.
