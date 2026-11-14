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
| Auditoría TITAN.pdf | PDF · 314.786 B | `f16511bace92cb0ba75a077f8110837f89952409` | Texto indexado consultado; binario exacto no cotejado | Candidato: dos registros de Biblioteca con mismo tamaño y fragmentos coincidentes; sin hash binario independiente | Posible duplicado lógico, no confirmado; no borrar |
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

El inventario previo registra dos elementos de Biblioteca (`Auditoría TITAN.pdf` y `Auditoría TITAN(1).pdf`) con igual tamaño y fragmentos de texto indexado coincidentes. Esto respalda una hipótesis de duplicación de contenido, pero no prueba identidad binaria. El PDF del arenero tiene el mismo tamaño; tampoco se ha probado que sea el mismo binario. No eliminar ninguna copia.

### 3.3 Materiales mencionados fuera del inventario

Un registro anterior de mantenimiento menciona `Audelin.zip` en una ruta auditada, pero no aporta en esta matriz una ruta verificable dentro del arenero de Softly ni inspección de su contenido. Se mantiene como pista pendiente de localizar, no como elemento confirmado de este inventario.

### 3.4 Archivo TXT eliminado no identificado

El README del arenero declara expresamente que `el gAto dice.txt` permanece y no contiene la frase «pico pal que lee». Por tanto, no debe confundirse con el TXT que gAto dijo haber eliminado. La identidad y ruta de ese archivo eliminado no están demostradas en este árbol.

## 4. Hallazgos de la línea base

1. Existe inventario de 10 elementos del arenero, pero la mayoría de los binarios aún no están inspeccionados.
2. La trazabilidad es parcial: hay hashes Git y tamaños para los archivos del arenero, pero faltan fecha de incorporación, aportante/origen específico, finalidad, referencias de uso y estado de respaldo verificable por elemento.
3. La cAjita tiene una política de conservación clara y un inventario pequeño.
4. Las dos rutas del arenero están documentadas como distintas; la duplicidad nominal es una fuente de error operativo, no autorización para fusionarlas.
5. Hay una hipótesis de duplicación de Auditoría TITAN que requiere cotejo binario.
6. No hay evidencia suficiente para eliminar ningún archivo del inventario.

## 5. Próximas acciones seguras

1. Obtener una enumeración recursiva completa del árbol `main` y compararla con todos los README/índices.
2. Inspeccionar internamente cada PDF y ZIP, registrar páginas/entradas, contenido, metadatos útiles y hash criptográfico calculado sobre el archivo descargado.
3. Localizar el origen y destino de cada artefacto y buscar respaldos independientes; registrar rutas, hashes y versiones.
4. Resolver referencias entrantes/salientes, enlaces rotos, archivos huérfanos y duplicados candidatos.
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
