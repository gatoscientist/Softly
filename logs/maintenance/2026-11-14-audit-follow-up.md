# Seguimiento de mantenimiento — 2026-11-14

- **Responsable:** Softly
- **Alcance:** mantenimiento documental de `gatoscientist/Softly` y `gatoscientist/Laboratorio-de-agentes`, a partir de los informes de Auditoría del 2026-11-14.
- **Restricción expresa:** no modificar contratos, perfiles, instrucciones ni archivos de agente. No alterar PDFs/ZIPs ni reordenar el arenero/cajita.

## Cambios realizados

### Softly

1. **Puntero de continuidad corregido:** `SOFTLY.md` ahora prioriza la sección 17.12 del checkpoint vigente (molde de agentes y desarrollo iterativo de TITAN). La sección 17.4 queda identificada como línea anterior, no como punto de reanudación por defecto.
2. **Framing conceptual aclarado:** la síntesis SYN-20261113-002 ahora explicita que el objetivo es crear agentes blandos reales mediante un molde; Softly es el laboratorio de investigación y documentación, no el producto entendido como agentes de software.
3. **Nota histórica de Cytryna clasificada:** `Conocí a Cytryna.md` fue trasladado íntegramente desde la raíz a `research/notes/Conocí a Cytryna.md`; el índice de investigación fue actualizado.
4. **Derivado intermedio clasificado:** `Hiloderivado.md` fue trasladado íntegramente a `logs/derived/Hiloderivado.md`. Se creó un README que explica que un derivado no sustituye la transcripción final de un hilo.
5. **Índices actualizados:** README raíz, índice de investigación e índice de bitácora reflejan el punto de continuidad y las ubicaciones nuevas.

### Laboratorio de Agentes

1. **README raíz creado:** incorpora propósito, mapa de directorios, puntos de entrada y límites de madurez.
2. **Departamento de Auditoría indexado:** se creó `Soft Agents/Auditoria/README.md`.
3. **Fuente canónica distinguida:** `Auditoras/README.md` identifica la ubicación vigente; `Auditoras.old/README.md` identifica el snapshot histórico, explica que se conserva deliberadamente y advierte que no debe usarse para nuevas integraciones. No se borró ni fusionó el snapshot.
4. **Solicitud explícita atendida:** se eliminó `Proyectos/el gAto estuvo aquí.txt`, cuyo contenido pedía directamente su eliminación. El cambio queda trazado en Git.

## Pendientes que no se ejecutan en este mantenimiento

- **Política del arenero y archivos AGENT.md:** los informes detectan diferencias entre la conversación sobre autonomía, el TEAM.md vigente y las instrucciones individuales. No se tocaron TEAM.md, AGENT.md, contratos ni perfiles porque requieren resolver precedencia normativa y quedan fuera de la frontera de cambios solicitada.
- **Manual TITAN criticado:** no se reescribió; la evidencia auditada no contiene criterios de aceptación suficientes para saber qué resultado espera gAto.
- **PDF y ZIP:** siguen sin inspección interna; el acceso disponible permitió inventariar rutas y blobs, no validar contenidos binarios.
- **Pruebas de aceptación/runtime:** no ejecutadas. La auditoría cerró administrativamente, no validó operación.
- **Otras referencias históricas:** no se borraron ni reorganizaron artefactos del arenero/cajita ni documentos cuya condición de respaldo no está demostrada.

## Evidencia de cambios

Los commits de cada archivo están registrados en el historial Git de ambos repositorios. Este documento es un índice de mantenimiento, no una certificación de runtime ni una auditoría nueva. Antes de cerrar el trabajo se verificarán los árboles actuales, las rutas movidas, la ausencia del archivo eliminado y los HEAD de ambas ramas.

## Hallazgos revisados que permanecen abiertos

- **AUD-01/AUD-02 — política del arenero y sincronización de instrucciones:** no se modificaron `TEAM.md`, `AGENT.md`, contratos ni perfiles. Los informes muestran una decisión posterior del gAto que no está reconciliada con la política compartida y los tres archivos individuales. Requiere una decisión normativa explícita; esta intervención respetó la prohibición de tocar agentes/contratos.
- **AUD-05 — manual de TITAN:** se conserva intacto. El feedback disponible expresa que el manual incluye demasiado contenido, pero no fija criterios de aceptación suficientes para una reescritura autónoma.
- **AUD-07 — hilo de revisión de commits:** se mantiene como síntesis fiel con limitación declarada, no se convierte en transcripción íntegra. Los mensajes que no quedaron disponibles literalmente no pueden reconstruirse sin inventarlos.
- **AUD-09 — identidad histórica:** se conserva sin reescritura, de acuerdo con la regla de preservar la historia.
- **AUD-10 — argumento de gAtoSD:** no se modificó. Las afirmaciones técnicas requieren mediciones/fuentes primarias y las conclusiones jurídicas quedan fuera del mantenimiento documental.
- **Artefactos binarios:** `Audelin.zip` existe en la ruta auditada, pero su contenido no fue inspeccionado. No se declara validado.
- **Política de arenero:** la grafía exacta de las rutas debe respetarse (`eL arenero del gAto`). No se renombraron directorios ni se alteró su contenido.

## Verificación final en GitHub

Se recuperaron nuevamente las ramas `main` y sus árboles recursivos después de los cambios. Ambos árboles respondieron completos (`truncated=false`).

- **Softly:** el HEAD inmediatamente anterior a la última actualización de este registro fue `e6ce1c7f06a51117d0490f925424944451212b08`; el commit que incorpora esta versión final del registro se verificó después como HEAD de `main`.
  - `research/notes/Conocí a Cytryna.md` existe y la copia de raíz ya no existe.
  - `logs/derived/Hiloderivado.md` existe y la copia de raíz ya no existe.
  - El puntero actualizado, índices y este registro de mantenimiento existen.
- **Laboratorio HEAD:** `19a86e0ab219e9792d4f5f36b9f68e07ccbf4b9f`.
  - README raíz, índice de Auditoría y etiquetas de fuente canónica/snapshot histórico existen.
  - `Proyectos/el gAto estuvo aquí.txt` ya no aparece en el árbol.
  - El snapshot `Auditoras.old/TEAM/TEAM.md` permanece conservado.

**Resultado:** los cambios documentales descritos están publicados en `main` y verificados por lectura de los árboles actuales. No se ejecutaron pruebas runtime ni se certificaron capacidades operativas.

## Material posterior al corte de Auditoría

La comparación Git también mostró dos archivos del Laboratorio que no estaban incluidos en el corte auditado y que no fueron creados por este mantenimiento:

- `lA cAjita del gAto/Aurora Hilo Inicial Wachito gAto - no comprueba.md`: se leyó como registro del intercambio inicial con Aurora. Conserva que la copia inicial no se había realizado en ese momento y la evidencia contextual de que la cAjita ya existía. Se respetaron su contenido y nombre históricos.
- `lA cAjita del gAto/iNstrucciones.md`: se leyó como instrucción de gAto que distingue la cAjita como lugar para material interesante/valioso.

Para evitar que ese material vuelva a quedar escondido, se agregó un índice `lA cAjita del gAto/README.md` y se enlazó desde el README raíz del Laboratorio. No se movieron, editaron ni borraron los dos archivos originales.


## Segunda pasada autónoma — índices, inventario y conservación (2026-11-14; hora no registrada)

A petición de gAto, se amplió el mantenimiento a tareas documentales autónomas después de que indicó que había dejado instrucciones nuevas en la cAjita y el arenero de Softly.

### Cambios publicados

**Softly**

- Se creó `cAjita del gAto/README.md` como índice de conservación y consulta.
- Se creó `eL arenero del gAto/README.md` con inventario de los nueve PDF y el TXT presente en el árbol, tamaños y estado de inspección.
- Se creó `eL aRenero del gAto/README.md` para documentar que esta carpeta distinta contiene la instrucción de limpieza.
- Se actualizó el README raíz para enlazar la cAjita y el arenero.
- Se documentó explícitamente la diferencia de capitalización entre `eL aRenero del gAto/` y `eL arenero del gAto/`. No se renombraron ni fusionaron.
- El archivo `eL arenero del gAto/el gAto dice.txt` sigue presente en el HEAD consultado. Su contenido leído pide postergar el orden de la casa y registrar futuras limpiezas; no contiene la frase «pico pal que lee». No se eliminó ni modificó. La eliminación mencionada por gAto no pudo asociarse a este archivo ni verificarse en el árbol consultado.

**Laboratorio de Agentes**

- Se creó `eL arenero del gAto/README.md` con índice de primer nivel, instrucciones y cautelas sobre ZIPs no inspeccionados.
- Se actualizó el README raíz para enlazar el índice.

### Verificaciones realizadas

- Se recuperaron árboles recursivos completos de ambos repositorios (`truncated=false`).
- Se compararon hashes SHA de blobs entre y dentro de los repositorios. Se detectaron coincidencias exactas entre snapshots `.old` y sus directorios vigentes de Auditoría y TITAN; se conservaron intencionalmente porque documentan historia/versiones. También coinciden archivos de instrucciones de cAjita entre Softly y Laboratorio. No se borró ningún duplicado.
- Se verificaron los enlaces Markdown locales de los README de navegación tocados y de los índices de investigación/bitácora seleccionados: todos los destinos comprobados existen en el árbol actual. Esto no constituye auditoría exhaustiva de todos los enlaces del repositorio.
- No se modificaron `AGENT.md`, `CONTRACT.md`, `PROFILE.md`, `PERMISSIONS.md`, `TEAM` ni procedimientos de agentes.
- No se borró ni movió material del arenero o de la cAjita.
- Los PDF y ZIP permanecen sin inspección interna; el inventario por tamaño y SHA no prueba que su contenido esté respaldado.
- No se ejecutaron pruebas runtime ni pruebas de aceptación.

### Pendientes explícitos

1. Identificar con gAto cuál era exactamente el TXT eliminado que contenía «pico pal que lee», porque no corresponde al TXT que sigue presente en la ruta inventariada.
2. Resolver si `eL aRenero del gAto/` es una carpeta intencional separada o un error histórico de capitalización. Hasta entonces, conservar ambas.
3. Inspeccionar PDF/ZIP y comparar su contenido con artefactos canónicos antes de considerar cualquier limpieza.
4. Completar auditoría de enlaces de todos los Markdown, no solo de los índices principales.
5. Revisar el registro de hilos/checkpoint para identificar si falta archivar el hilo actual cuando gAto lo cierre.

Esta pasada fue de indexación, clasificación y verificación estática. No se realizó limpieza destructiva.


### Ampliación de navegación del Laboratorio

Durante la misma pasada se completó también la entrada de proyectos del repositorio `gatoscientist/Laboratorio-de-agentes`:

- Se creó `Proyectos/README.md` como índice de proyectos.
- Se creó `Proyectos/TITAN/README.md` con inventario de los ocho ZIP, tamaños y blob SHAs.
- Se actualizó el README raíz para enlazar el índice de proyectos.
- Los ZIP siguen sin inspección interna; los nombres solo permiten una clasificación provisional. No se borró ni se declaró redundante ningún paquete.


## Corte de verificación de esta pasada

Comparación de ramas contra el estado previo a esta segunda pasada:

- Softly: `feef2301d322cd226c265a70f1f19d3c2a22aef1` → `e3596a172aee05fb5ca3c3590fce5794d87bbb56`; 7 commits, 5 rutas modificadas/añadidas, rama adelantada y sin commits detrás.
- Laboratorio de Agentes: `19a86e0ab219e9792d4f5f36b9f68e07ccbf4b9f` → `3d58eb013915203b43641d1ad881d910c01dc2cc`; 5 commits, 4 rutas modificadas/añadidas, rama adelantada y sin commits detrás.

Las rutas cambiadas en Softly fueron README raíz, los tres índices de cAjita/arenero y este registro. En Laboratorio fueron README raíz, índices de `Proyectos/`, `Proyectos/TITAN/` y arenero. Las comparaciones no muestran cambios en archivos de agentes, perfiles, contratos, permisos, equipos ni procedimientos.

Se verificó además que los enlaces Markdown locales de los índices y portadas seleccionados resuelven a rutas presentes en los árboles actuales. Los árboles completos se recuperaron sin truncamiento. Este corte documenta verificación estática de Git y navegación, no ejecución de pruebas.

El commit que añade este propio corte hará avanzar el HEAD de Softly una vez más; la verificación terminal de la rama se realiza inmediatamente después de publicarlo.


## Tercera pasada — inspección de evidencias disponibles y enlaces (2026-11-14; hora no registrada)

### Inspección de PDF y ZIP: alcance real

- El árbol de Softly contiene nueve PDF en `eL arenero del gAto/`. Se registraron sus Git blob SHAs en el README del arenero. Los hashes permiten reconocer exactamente los blobs dentro de Git, pero no sustituyen lectura del documento.
- La Biblioteca de ChatGPT contiene dos registros (`Auditoría TITAN.pdf` y `Auditoría TITAN(1).pdf`) de 314.786 bytes, con fragmentos de texto indexado coincidentes y el mismo informe de cuatro páginas. Es evidencia fuerte de duplicación de contenido en Biblioteca, pero no se pudo obtener el binario para comparar hashes. No se eliminó ninguna copia ni se afirma identidad binaria.
- El informe indexado declara TITAN v0.2.0-alpha, enumera commits y cambios de multi-API/failover, controles GUI y HopCount, y reporta que determinados jobs de Actions no iniciaron por una restricción administrativa de facturación. Es un documento histórico con afirmaciones de su autor; no prueba por sí solo el estado actual ni reemplaza la verificación de código y pruebas.
- La Biblioteca consultada no expuso copias verificables de los otros ocho PDF del arenero. Tampoco expuso los ZIP de TITAN del Laboratorio. Los ZIP de `Proyectos/TITAN/` siguen sin inspección interna. No se eliminó ni modificó ningún PDF o ZIP.
- Se intentó acceder a los binarios del repositorio mediante las capacidades disponibles, pero no hubo una vía autorizada de materialización de bytes. Por eso no se declara inspección interna completa.

### Auditoría de enlaces Markdown

- Se revisaron los enlaces Markdown locales de los 66 archivos Markdown de Softly (64 presentes antes de crear el índice y la bitácora de mantenimiento, más esos dos archivos nuevos). No se detectaron destinos locales rotos.
- Se revisaron los 71 archivos Markdown vigentes del Laboratorio (excluidos los snapshots históricos bajo `.old/`). Se detectó un enlace roto en `eL arenero del gAto/AUDITORIA/README.md`: apuntaba a `../Soft Agents/Auditoria/README.md`, resolviendo dentro del arenero. Se corrigió a `../../Soft Agents/Auditoria/README.md` y se publicó el cambio.
- Los snapshots históricos `.old/` y los destinos externos no se incluyeron en esta auditoría. Los archivos de agentes/contratos se revisaron solo para sus enlaces locales y no se modificaron.

### Inventario TXT y discrepancia de eliminación

El árbol actual de Softly contiene un único TXT: `eL arenero del gAto/el gAto dice.txt` (358 bytes, blob `3275a37e61c651994b63c0525e8da643d0632a2d`). Su texto indica dejar pendiente el orden de la casa y registrar las futuras limpiezas; no contiene «pico pal que lee». No aparece otro TXT en el árbol de Softly. Por lo tanto, el archivo que gAto dice haber eliminado no está identificado en el HEAD consultado; no se recreó ni se alteró el TXT que sí permanece.

### Publicaciones de esta pasada

- Softly: README del arenero ampliado con Git blob SHAs y nota de comparación prudente con Biblioteca; registro de mantenimiento actualizado.
- Laboratorio: enlace relativo corregido en el índice `eL arenero del gAto/AUDITORIA/README.md`.

La revisión es estática y documental. No se inspeccionaron todos los PDF/ZIP, no se ejecutaron pruebas de runtime y no se realizaron borrados.


### Contraste externo con el repositorio TITAN

Como el informe `Auditoría TITAN.pdf` describe el estado de `gatoscientist/TITAN`, se consultó su estado actual para evitar tratar el informe del 12 de noviembre como vigente sin contraste:

- `main` estaba en `58d11dcf9bbf0881ed308efe7767033cd32ea7c3` al momento de la consulta, con último commit del 14 de noviembre de 2026 a las 07:19:49 UTC (mensaje: «eL gAto agregando a su equipo»).
- El archivo `VERSION` sigue indicando `0.2.0-alpha`.
- La consulta del historial mostró commits posteriores al informe, incluidos «Limpieza Agentes Soft» (14 de noviembre) y otros cambios de auditoría/coordinación (13 de noviembre). Por lo tanto, el informe histórico no representa por sí solo el árbol actual.
- La consulta de Actions devolvió 179 ejecuciones. Las 15 más recientes listadas estaban en estado completado con conclusión `failure`; incluyen ejecuciones del 12 y 13 de noviembre. No se encontró evidencia de una ejecución exitosa entre esas 15.
- La ejecución más reciente listada (#179, run ID `43348076033`) corresponde a `dbf47c91c2f75b752f483bda204ec0fda1db8dda`, no al HEAD actual `58d11dcf9bbf0881ed308efe7767033cd32ea7c3`. La descarga de logs devolvió 404 y no se pudieron inspeccionar los pasos; por eso no se atribuye la causa de los fallos a facturación, aunque el informe previo lo afirmaba para ejecuciones anteriores.
- La rama `main` no tiene protección ni checks obligatorios configurados en la respuesta consultada. Esto es una observación de configuración, no una recomendación de cambiarla en esta tarea.

**Conclusión prudente:** el identificador de versión sigue en 0.2.0-alpha, pero la afirmación histórica de que TITAN estaba «operativo» no queda respaldada por CI exitoso reciente en las ejecuciones consultadas. Tampoco se ejecutó runtime local ni se validó el HEAD actual. No se modificó el repositorio TITAN.

### Comparación de paquetes ZIP

En `Proyectos/TITAN/` del Laboratorio, los ocho ZIP tienen Git blob SHAs distintos: no existen duplicados binarios exactos entre esos ocho archivos. Se añadió esta conclusión al índice del directorio. La equivalencia parcial o funcional solo puede evaluarse inspeccionando el contenido interno; no se eliminó ningún ZIP.


### Recuperación y cruce de investigación sobre agentes Soft

Se leyeron los dos documentos del arenero del Laboratorio:

- `eL arenero del gAto/INVESTIGACION/estructura-de-agentes-soft.md` (blob `431949c2ddbdef8834b2e0365f4bae369f85d9f4`).
- `eL arenero del gAto/INSTRUCCIONES-PARA-CREAR-AGENTES-SOFT.md` (blob `42b20aabb961a90a4d9eb3e078a2d2c82512800c`).

Se compararon con `docs/architecture/agent-model-v0.1.md`, `agents/templates/agent-generation-mold.md` y `agents/templates/agent-profile.md` de Softly. No son duplicados exactos: la investigación aporta fundamentos y separación de espacios; la guía aporta crecimiento por etapas y reglas operativas; Softly contiene el modelo lógico de definición/brief/asignación/sesión y el molde de generación desde brief.

Se creó `research/notes/2026-11-14-cruce-estructura-agentes-soft.md` con síntesis, procedencia, aportes, diferencias y límites. Se enlazó desde `research/README.md` y `research/notes/README.md`. En el Laboratorio se actualizaron los estados de ambos elementos en el índice del arenero y se enlazó la síntesis de Softly. Los originales permanecen intactos; no se movieron ni se modificaron agentes, contratos o plantillas.

Aporte recuperado especialmente útil: estructura física progresiva por etapas (definición mínima → trabajo → continuidad → evaluación), sin crear carpetas vacías para aparentar madurez. Se deja como recomendación a evaluar, no como cambio normativo aprobado.


### Cobertura de índices y navegación de directorios

Se revisó qué directorios con archivos carecían de README y se añadieron índices en los espacios de navegación que concentran varios documentos o requieren orientación:

**Softly:** `docs/README.md`, `docs/architecture/README.md`, `docs/governance/README.md`, `agents/templates/README.md`, `logs/threads/README.md`, `templates/README.md` y `research/sources/README.md`. Se enlazaron desde las portadas correspondientes. Los directorios restantes sin README contienen un solo archivo (handoff, research, security, schema o hilo archivado); se dejaron sin índice adicional para evitar ruido.

**Laboratorio:** se crearon índices en `Soft Agents/README.md`, `Soft Agents/TITAN/README.md`, `Soft Agents/Cytryna/README.md`, `Soft Agents/GatoSD/README.md`, `Soft Agents/gAtoSD/README.md` y `eL arenero del gAto/AUDITORIA/agentes/README.md`. Se enlazó el índice general de Soft Agents desde la portada y se incorporaron enlaces a dos notas de gAto que estaban sin indexar: el comentario de que la estructura de auditoras ya había quedado obsoleta y el feedback sobre el manual de TITAN.

Se preservaron los textos originales. El argumento de `Soft Agents/gAtoSD/Argumento malo pero con fundamentos.txt` quedó clasificado como borrador argumental con afirmaciones técnicas y jurídicas no verificadas; no se trata como conclusión legal. Las carpetas de Cytryna y GatoSD solo contienen marcadores `gitkeep` en sus equipos actual e histórico; los índices declaran esa limitación y no infieren despliegue.

No se añadieron README a directorios `TEAM`, snapshots históricos o carpetas de un solo archivo donde un índice no aportaría navegación significativa. Los enlaces locales de los nuevos índices y portadas actualizadas se comprobaron contra los árboles actuales.


## Verificación terminal de navegación y alcance (antes del commit de este cierre)

- Softly: el árbol contiene 74 archivos Markdown y 30 README. Se comprobaron los enlaces locales de los índices, documentos de navegación y registros creados/actualizados; la auditoría previa cubrió los 66 Markdown existentes antes de la ampliación de índices y los archivos nuevos se comprobaron individualmente. No quedan destinos locales rotos identificados.
- Laboratorio: el árbol contiene 127 archivos Markdown en total; 77 corresponden a la estructura vigente excluyendo snapshots `.old/`. Se comprobaron los enlaces locales de los 71 Markdown vigentes de la pasada inicial y los seis índices nuevos/actualizados de forma individual. El único enlace roto detectado fue corregido; no quedan destinos locales rotos identificados en ese alcance.
- Softly mantiene 30 README y Laboratorio 37 README. Los directorios sin README restantes son archivos individuales, snapshots o carpetas TEAM deliberadamente no alteradas; no se persigue crear un índice en cada carpeta por obligación mecánica.
- Los árboles recursivos de ambos repositorios se recuperaron completos (`truncated=false`).
- La comparación de cambios contra los HEAD iniciales de esta pasada no muestra modificaciones a `AGENT.md`, `CONTRACT.md`, `PROFILE.md`, `PERMISSIONS.md`, archivos `TEAM/` ni procedimientos de agentes.
- HEAD consultado antes de registrar esta verificación: Softly `d3ddc6c25a0c2f49b7274d144761732fc2336ebe`; Laboratorio `4d1d1da87c9b368cbc2115d7622778598a0f4c69`.

El presente registro se actualizará mediante un commit adicional en Softly; la rama y el árbol se vuelven a consultar inmediatamente después para confirmar el HEAD final.


## 2026-11-14 — Revisión de integridad posterior al último cierre

**Corte consultado:** rama `main`, HEAD `6741969a49d71389104c2debf6174f572b73b16c` (commit `docs(maintenance): record thread archive and closure`).

### Estado del árbol

- Árbol recursivo completo: 127 entradas, 93 blobs y 34 directorios.
- 79 Markdown, incluidos 31 README; 9 PDF, 1 TXT, 2 JSONL, 1 JSON y 1 `.gitattributes`.
- No se encontraron blobs con SHA repetido.
- No hay rutas bajo `.github/`; no se encontraron workflows de CI.
- No hay archivos de código ejecutable en el inventario.
- Los nueve PDF y el TXT del arenero siguen presentes. No se modificó ni eliminó ningún material.

### Continuidad e índices

Se revisaron nuevamente el mandato, el README raíz, el modelo operativo, el protocolo de comunicación, los índices de mantenimiento, hilos, documentación, investigación, agentes y experimentos, además del README del arenero y sus instrucciones. La prioridad vigente sigue siendo la integridad de Softly y la pausa de agentes está correctamente reflejada en los puntos de entrada revisados.

El índice de hilos incluye el registro incorporado en el último cierre. La ruta histórica `docs/handoff/2026-11-13-continuidad-wachita.md` sigue enlazada desde documentación como antecedente histórico; no se altera porque su nombre forma parte de la procedencia del registro, no de la identidad vigente.

### Hallazgo de gobernanza Git

La consulta de la rama indica que `main` no está protegida y que los checks requeridos están desactivados. El último commit consultado aparece como no verificado por estar sin firma. Esto **no demuestra corrupción ni pérdida de contenido**, pero sí deja menos barreras preventivas ante pushes accidentales o cambios no revisados.

**Recomendación pendiente de autorización:** evaluar protección de `main` (pull request o revisión requerida, checks cuando existan y restricciones de force-push/deleción) y firma de commits. No se modificó la configuración del repositorio.

### Límites y siguientes pasos

1. La comprobación estructural no sustituye la inspección binaria de los nueve PDF ni la comparación con respaldos independientes.
2. No se certificó runtime: el repositorio sigue sin código ejecutable ni CI.
3. La revisión de contenido documental fue dirigida; no equivale a una nueva lectura íntegra de los 79 Markdown ni a repetir desde cero la auditoría automatizada de enlaces.
4. No se ejecutó limpieza, movimiento, renombrado ni modificación de contratos/agentes.

**Estado:** integridad estructural del árbol confirmada para este corte; trazabilidad binaria y controles preventivos de rama siguen abiertos. No se declara cerrada la auditoría global.


## 2026-11-14 — Cierre de tareas documentales autorizadas en este ciclo

- Se resolvió la colisión de IDs por autorización expresa: `SYN-20261113-001` queda en la síntesis de gobernanza multiagente y `SYN-20261113-003` identifica la línea base multi-rama. Se actualizaron el documento reasignado y los índices `research/README.md` y `research/syntheses/README.md`.
- Se incorporó una propuesta no normativa de registro de namespaces, cardinalidad y relaciones; el esquema vigente permanece intacto.
- Se revisaron los dos JSONL: cada uno contiene una línea JSON sintácticamente válida. No hay esquema de eventos para validar semántica ni unicidad automáticamente.
- Los ocho PDF originales de TITAN/Cytryna quedan expresamente pendientes de cotejo. No se afirma identidad con archivos del arenero ni se inspeccionan binarios por hash solamente.
- La revisión de enlaces externos se limita a las 14 URLs registradas previamente en bibliografía y panorama; no se declara verificación global de todos los enlaces del repositorio. La cobertura local histórica de 78 Markdown queda como último alcance registrado; los índices y archivos tocados en este ciclo se verifican de forma dirigida.
- La rama `main` sigue sin protección y sin checks requeridos; no se cambió esa configuración. No existe runtime ni CI en el árbol, por lo que no hay pruebas de ejecución que reportar.
- No se movió ni eliminó material, ni se alteraron contratos, agentes o esquemas.
