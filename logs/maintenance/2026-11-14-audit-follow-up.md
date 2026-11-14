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

- **Softly HEAD:** `75d870503a050048305eddac22649c9075c05414`.
  - `research/notes/Conocí a Cytryna.md` existe y la copia de raíz ya no existe.
  - `logs/derived/Hiloderivado.md` existe y la copia de raíz ya no existe.
  - El puntero actualizado, índices y este registro de mantenimiento existen.
- **Laboratorio HEAD:** `164719f638d6a1202f10bf1527cc169ad33ee8a1`.
  - README raíz, índice de Auditoría y etiquetas de fuente canónica/snapshot histórico existen.
  - `Proyectos/el gAto estuvo aquí.txt` ya no aparece en el árbol.
  - El snapshot `Auditoras.old/TEAM/TEAM.md` permanece conservado.

**Resultado:** los cambios documentales descritos están publicados en `main` y verificados por lectura de los árboles actuales. No se ejecutaron pruebas runtime ni se certificaron capacidades operativas.
