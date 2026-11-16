# Matriz de consolidación de ramas — RESET-CORE-2026-002

**Corte:** 2026-11-16  
**Responsable:** Softly  
**Mandato:** Dictamen de Dirección — destrabe de RESET-CORE-2026-002.  
**Criterio:** rama única `main` para repositorios activos; no descartar commits exclusivos; no fusionar ramas divergidas por nombre, antigüedad o conveniencia.

## 1. Estado por rama

| Repositorio | Rama | Ahead | Behind | Cambios exclusivos | Tratamiento |
|---|---|---:|---:|---|---|
| Softly | `fix/f03-recover-ledger` | 5 | 423 | SOFTLY.md, logs F-03 y componentes softly-runtime | Runtime fuera de norma; no fusionar. Preservar historia. |
| Softly | `recovery/AUD-20261116-001` | 3 | 171 | README/estructura Audelinesay | PR #4 cerrado sin merge; contenido equivalente ya creado en main. Preservar rama como evidencia. |
| Katarina | `kat-006-stage3-softly-2026-11-16` | 8 | 89 | coordinación task-centric y expediente KAT-006 | PR #1 cerrado sin merge; KAT-006 cerrado administrativamente. Preservar evidencia; no reactivar. |
| Auditoria | `amelia/propuesta-mejora-auditoria-2026-11-15` | 2 | 32 | propuesta estratégica y anexo | Propuesta histórica; no adoptar automáticamente. Preservar. |
| Auditoria | `proposal/AUD-20261115-001-refactor-equipo-auditoria` | 2 | 32 | propuesta de refactor y tablero | PR #1 cerrado sin merge por supersesión normativa; preservar propuesta. |
| Auditoria | `recovery/AUD-20261116-001` | 19 | 26 | cambios de contratos/perfiles Aurora y Autumn, informe de recuperación | PR #1 cerrado sin merge por conflicto con identidad única Audeline; preservar commits como historia. |
| Laboratorio-de-agentes | `proposal/auditoria-reforma-normativa-2026-11-15` | 1 | 176 | propuesta normativa de reforma | Propuesta histórica; no adoptar automáticamente. Preservar. |

Todas las comparaciones son contra el `main` consultado en el corte y muestran ramas divergidas. No hay fast-forward seguro ni se recomienda merge automático.

## 2. PR

- Softly #4: CLOSED, NOT MERGED. La estructura Audelinesay ya fue creada directamente en main.
- Katarina #1: CLOSED, NOT MERGED. KAT-006 está cerrado administrativamente.
- Auditoria #1: CLOSED, NOT MERGED. La propuesta de equipo auditor contradice el límite de identidad única.
- Softly #8: OPEN, MERGEABLE. Es el PR de migración del registro v2; no es una rama histórica y no debe fusionarse hasta dictamen independiente favorable de Audeline.

## 3. Protección de main y refs

La conexión GitHub disponible no concede acceso a los endpoints de branch protection (403 Resource not accessible by integration) ni expone operación para eliminar refs. Por tanto:
- no se modificó ni se afirma modificada la protección de `main`;
- no se eliminaron ramas;
- no se ocultaron ni descartaron commits exclusivos;
- la limitación queda localizada en protección/eliminación de refs, sin detener migración, revisión documental, inventario ni trabajo independiente.

## 4. Acciones siguientes

1. Audeline revisa PR #8 de forma independiente.
2. Katarina entrega evaluación técnica de las capacidades candidatas.
3. Mantener las siete ramas clasificadas y preservadas hasta disponer de permisos de administración de refs o un procedimiento de archivo verificable.
4. Una vez habilitado el permiso, preservar refs/commits exclusivos, cerrar/archivar ramas según clasificación y verificar que solo `main` permanezca en cada repositorio activo.
5. Aplicar branch protection/rulesets a `main` con aprobación requerida, checks y restricción de force-push/deletion, una vez disponible permiso administrativo.

## 5. Dictamen de corte

La clasificación documental de las siete ramas está completada. La consolidación física no está completada: las ramas siguen presentes. La protección de `main` no pudo leerse ni modificarse por falta de permiso. Ninguna de estas limitaciones justifica detener tareas independientes ni altera el cierre administrativo de Runtime o KAT-006.


## Revalidación de divergencia — corte posterior a los commits de coordinación (2026-11-16)

Se repitieron las comparaciones contra `main` después de registrar los handoffs, checkpoint y matriz. Los conteos actualizados son:

| Repositorio | Rama | Ahead | Behind | Estado |
|---|---|---:|---:|---|
| Softly | `fix/f03-recover-ledger` | 5 | 426 | diverged |
| Softly | `recovery/AUD-20261116-001` | 3 | 174 | diverged |
| Katarina | `kat-006-stage3-softly-2026-11-16` | 8 | 89 | diverged |
| Auditoria | `amelia/propuesta-mejora-auditoria-2026-11-15` | 2 | 32 | diverged |
| Auditoria | `proposal/AUD-20261115-001-refactor-equipo-auditoria` | 2 | 32 | diverged |
| Auditoria | `recovery/AUD-20261116-001` | 19 | 26 | diverged |
| Laboratorio-de-agentes | `proposal/auditoria-reforma-normativa-2026-11-15` | 1 | 176 | diverged |

Los siete casos continúan divergidos. Los conteos anteriores de Softly se reemplazan por estos valores actualizados; no se ha borrado ni fusionado ninguna rama.
