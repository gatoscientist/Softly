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


## 11. Verificación de referencias externas de investigación

Se extrajeron y comprobaron 14 URLs únicas de `research/bibliography.md` y `research/sources/2026-11-agent-design-landscape.md` (OpenAI, Anthropic, LangGraph, OWASP, MCP y NIST). Doce destinos originales resolvieron directamente. Dos referencias requerían corrección:

- **OWASP Agentic Top 10:** la ruta antigua no resolvía. Se actualizó al artículo oficial [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/), verificado el 2026-11-14.
- **LangGraph Persistence:** la ruta antigua redirigía a documentación heredada. Se actualizó a la página oficial actual [LangGraph Persistence](https://docs.langchain.com/oss/javascript/langgraph/persistence), verificada el 2026-11-14.

Se actualizaron ambos enlaces tanto en la bibliografía como en la ficha de panorama. La guía de Anthropic *Building effective agents* sigue accesible, pero advierte que parte del panorama de herramientas de 2024 ha cambiado; la ficha conserva esa limitación y remite a la documentación actual de Managed Agents para detalles vigentes.

**Alcance:** esta verificación cubre las 14 URLs identificadas en esos dos documentos, no todos los enlaces externos que pudieran existir en el repositorio. No se afirma que los contenidos externos sean inmutables; deben revisarse cuando se reutilicen.


## 12. Navegación completa de índices de directorio

Se cerraron los enlaces de navegación que faltaban entre índices:
- El mapa del `README.md` raíz ahora enlaza los 13 índices de directorios principales.
- `agents/README.md` enlaza el índice de perfiles.
- `evaluations/README.md` enlaza datasets, planes y ejecuciones.
- `experiments/README.md` enlaza protocolos, resultados y casos.

Los seis subdirectorios de evaluaciones/experimentos que solo contienen README quedan identificados explícitamente como estructuras de preparación sin artefactos todavía. Se conservan y no se clasifican como basura.

Los cuatro índices modificados y el mapa raíz fueron leídos nuevamente; sus enlaces locales nuevos resuelven a rutas existentes. La verificación dirigida registró cero destinos rotos.

**Corte inmediatamente anterior a esta ampliación:** `main` HEAD `866bb1e6eb2e6fc04e97b0223fe8f88d283d5dcb`; 126 entradas, 92 blobs, 34 directorios, 78 Markdown y 31 README.


## 12. Reconciliación de inventario y trazabilidad — corte posterior

**Corte Git previo a este registro:** rama `main`, HEAD `7fbec91eaeaf3a6e5e04928053ff87b725206bd0`; árbol recursivo completo, 127 entradas, 93 blobs y 34 directorios. El árbol contiene 79 Markdown, 31 README, 9 PDF, 1 TXT, 2 JSONL, 1 JSON y `.gitattributes`. No hay blobs con SHA repetido.

### Reconciliación del arenero y de la cAjita

- El inventario del arenero en `eL arenero del gAto/README.md` enumera 9 PDF y 1 TXT; coincide con las extensiones y cantidades del árbol actual.
- La cAjita contiene únicamente README e instrucciones, de acuerdo con su índice.
- Las dos rutas de arenero con capitalización distinta siguen separadas y documentadas.
- No se identificó ZIP en el árbol de Softly.
- No se realizó movimiento, renombrado ni eliminación.

### Trazabilidad de investigación: brecha identificada

La nota `research/notes/2026-11-13-material-titan-sofa-agent.md` registra ocho identificadores `SRC-20261113-001` a `SRC-20261113-008` para documentos originales aportados, pero los metadatos y resúmenes están agrupados en una sola nota. No existen ocho fichas individuales correspondientes en `research/sources/`; el índice de fuentes solo enlaza el panorama general. Por ello, las referencias pueden seguirse dentro de la nota, pero no consultarse como registros independientes.

El esquema `schemas/research-record.schema.json` define registros `SRC-YYYYMMDD-NNN` y exige título, URL, tipo, fecha de consulta y estado. Los ocho documentos aportados son archivos locales cuya URL externa puede no existir; antes de crear fichas individuales habrá que decidir cómo representar fuentes internas/adjuntos sin inventar URLs ni debilitar el esquema por conveniencia. El panorama `SRCSET-20261113-001` es un conjunto/síntesis, no debe confundirse con un ID de fuente individual.

**Clasificación:** deuda de trazabilidad documental, no pérdida de archivos ni corrupción. No se modificó el esquema ni se generaron fichas artificiales.

### Otros registros de decisión y actividad

- `logs/decisions.jsonl` contiene una entrada para ADR-0001 y el documento formal correspondiente existe; la ADR declara que fue reconstruida desde el registro.
- `logs/activity.jsonl` contiene el evento de bootstrap y referencia un commit histórico. El campo de actor conserva el valor histórico tal como fue registrado; no se reescribe retrospectivamente.
- Los registros JSONL leídos contienen una línea JSON válida cada uno. No se ejecutó un validador automático del esquema de eventos porque no existe esquema de actividad/decisiones asociado en el árbol.

### Acciones siguientes

1. Definir una convención de procedencia para adjuntos y documentos internos sin URL pública.
2. Crear fichas individuales solo cuando la fuente original esté disponible y se puedan registrar sus metadatos reales; mantener los resúmenes como derivados.
3. Enlazar las fichas desde `research/sources/README.md` y las notas que las utilizan.
4. Evaluar si el esquema debe admitir una ubicación local/referencia de archivo y un campo de procedencia, mediante cambio versionado y ejemplos válidos; no cambiarlo hasta acordar el contrato.
5. Mantener pendiente la inspección binaria de los nueve PDF y el cotejo de respaldos independientes.

**Estado:** inventario de rutas y tipos reconciliado para este corte; trazabilidad de fuentes adjuntas incompleta; inspección binaria pendiente; ninguna limpieza autorizada.


## 13. Auditoría transversal de identificadores y relaciones — 2026-11-14

**Corte consultado:** `main`, HEAD `288569c592d997f205c1b5a14ef6783d48888509`; árbol recursivo completo (`truncated=false`). Se releen los índices de investigación, las tres síntesis, las notas de investigación relevantes, la bibliografía, la ADR-0001, el registro de decisiones y el esquema de registros de investigación.

### Hallazgos confirmados

1. **Colisión de ID de síntesis:** dos documentos distintos declaran `SYN-20261113-001`:
   - `research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md` — Cytryna, TITAN y gobernanza de equipos multiagente.
   - `research/syntheses/2026-11-13-linea-base-contaminacion-multirrama-titan.md` — línea base de contaminación multi-rama en TITAN.
   
   Son artefactos y preguntas diferentes. La colisión está confirmada; no se reasigna ningún ID sin resolver cuál debe conservar el identificador histórico y cómo actualizar sus referencias.

2. **Síntesis no indexada:** `research/README.md` lista dos síntesis y enlaza `SYN-20261113-001` a la línea base multi-rama y `SYN-20261113-002` al propósito/diseño de agentes blandos. No incluye `2026-11-13-de-agentes-que-construyen-agentes.md`, que queda sin entrada en el índice de investigación. Su omisión no implica que el archivo esté perdido.

3. **Correspondencia de fuentes adjuntas y nombres del arenero no resuelta:** la tabla de `research/notes/2026-11-13-material-titan-sofa-agent.md` registra ocho títulos originales. Al contrastarlos con `eL arenero del gAto/README.md`, al menos dos nombres no coinciden literalmente:
   - `SRC-20261113-001`: “Auditoría Total de Código y Estado del Proyecto TITAN.pdf”; el inventario actual incluye “Auditoría TITAN.pdf”.
   - `SRC-20261113-006`: “Arquitectura de Agentes Blandos y Dinámicas de Fusión en Sistemas Multi-Agente Auto-Evolutivos.pdf”; el inventario actual incluye “Arquitectura de Agentes Blandos.pdf”.
   
   La nota declara que los originales fueron adjuntos de conversación y no están replicados como binarios en el repositorio. No se puede inferir que los archivos del arenero sean los mismos documentos renombrados, versiones abreviadas o fuentes distintas. La relación queda **no demostrada**, no se declara pérdida ni equivalencia.

4. **Convención de identificadores incompleta:** `research/README.md` define IDs `SRC-YYYYMMDD-NNN` y `SYN-YYYYMMDD-NNN`, mientras `research/bibliography.md` usa `SRCSET-20261113-001` para un conjunto/panorama y la nota de ingesta usa `ING-20261113-001`; la ficha de anatomía usa `SOFT-RES-001`. Son clases semánticas distintas, pero no existe un registro central que declare sus namespaces, cardinalidad, reglas de unicidad o relaciones. El esquema actual solo modela `SRC-...` y exige `url`; no modela explícitamente conjuntos, ingestas ni fuentes adjuntas locales.

5. **Relaciones registradas y límites:** `ADR-0001` tiene un artefacto formal enlazado desde `decisions/README.md` y una entrada correspondiente en `logs/decisions.jsonl`. La ADR identifica su reconstrucción desde el registro y conserva el commit histórico relacionado. No se detecta una discrepancia en esa relación en los documentos consultados.

### Clasificación y acciones seguras

- Colisión de ID: **ambigüedad de identidad documental**, requiere decisión de asignación antes de corregir referencias.
- Síntesis no indexada: **deuda de navegación**, corrección posterior de bajo riesgo cuando se resuelva cómo citarla sin perpetuar la colisión.
- Correspondencia de nombres de fuentes: **procedencia no demostrada**, requiere cotejar adjuntos originales, metadatos o hashes antes de asociar registros.
- Namespaces: **brecha de gobernanza del modelo documental**, requiere propuesta versionada; no modificar el esquema actual durante esta auditoría.

No se cambió ningún ID, título, esquema, fuente, índice ni artefacto histórico. No se movió ni eliminó material. La revisión fue dirigida a los documentos enumerados y no equivale a un análisis semántico exhaustivo de cada Markdown del repositorio.

### Próximas acciones propuestas

1. Resolver la colisión de `SYN-20261113-001` con una decisión explícita y actualizar todas las referencias afectadas en una sola operación verificable.
2. Incorporar la síntesis actualmente no indexada una vez resuelta la colisión.
3. Cotejar los ocho adjuntos originales con los archivos del arenero y registrar correspondencias solo con evidencia verificable.
4. Diseñar un registro de tipos de identificador y relaciones (fuente, conjunto, ingesta, nota, síntesis, decisión y artefacto derivado), sin alterar aún los contratos vigentes.
5. Mantener separados los hechos históricos, las referencias de procedencia y las instrucciones operativas actuales.

**Estado:** hallazgos confirmados y registrados; no se realizaron cambios estructurales ni limpieza. La trazabilidad transversal sigue abierta.


## 14. Resolución de colisión de síntesis y estado de trazabilidad — 2026-11-14

**Autorización:** gAto autorizó expresamente conservar `SYN-20261113-001` para `2026-11-13-de-agentes-que-construyen-agentes.md` y reasignar la línea base multi-rama al siguiente identificador disponible, `SYN-20261113-003`.

**Cambios ejecutados:** se actualizó el encabezado y las referencias internas del documento `research/syntheses/2026-11-13-linea-base-contaminacion-multirrama-titan.md`; `research/README.md` ahora indexa las tres síntesis con IDs únicos y enlaza la propuesta de registro de namespaces; `research/syntheses/README.md` enumera las tres síntesis. El documento de gobernanza multiagente conserva `SYN-20261113-001`; `SYN-20261113-002` no cambia.

**Límite de rastreo:** se verificaron los documentos de síntesis y los índices de investigación consultados. La búsqueda de código de GitHub no entregó resultados indexados (respuesta incompleta), por lo que no se afirma una búsqueda exhaustiva de cada blob del repositorio. Las referencias adicionales que aparezcan fuera de esos índices/documentos deberán corregirse al detectarse.

**Fuentes TITAN/Cytryna:** gAto indicó que los ocho PDF originales se revisarán después. Se mantiene la relación entre los ocho IDs `SRC-20261113-001` a `SRC-20261113-008` y sus originales como **no cotejada**; los dos títulos divergentes frente al arenero no se equiparan. No se declara inspección binaria ni equivalencia de versiones.

**Modelo documental:** se prepara una propuesta descriptiva de namespaces y relaciones, sin modificar `schemas/research-record.schema.json`, validaciones ni contratos. Los JSONL consultados contienen una línea cada uno y son JSON sintácticamente válido; no existe esquema de eventos asociado, por lo que no se declara validación contra schema.

**Gobernanza Git y alcance:** `main` continúa sin protección ni checks requeridos; el commit consultado previo estaba unsigned. No se modificó la configuración. No se hizo limpieza, movimiento, borrado ni cambio de contratos/agentes. La auditoría sigue siendo documental y no certifica runtime.
