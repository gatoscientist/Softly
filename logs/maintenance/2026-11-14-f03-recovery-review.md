# Revisión de implementación F-03 — recuperación conservadora del ledger

- **Fecha:** 2026-11-14
- **Responsable de implementación:** Katarina / AgentDEV
- **Revisor independiente previsto:** Autumn
- **Estado:** revisión interna inconclusa; no listo para retest de aceptación
- **Rama:** `fix/f03-recover-ledger`
- **Base inmutable:** `9e8bc1015cc60d3cb097d3497459d1cd28b57d69`
- **HEAD revisado:** `d9982cf764b71a0aeeada491ef19acad7a4c7b44`

## 1. Alcance y procedencia

La revisión se realizó leyendo desde GitHub los archivos publicados en el HEAD indicado, no copias locales ni adjuntos:

| Archivo | Git blob SHA |
|---|---|
| `softly-runtime/runtime.py` | `07e0accab4398d984d7df8c4dda8bd44ebf0b4aa` |
| `softly-runtime/test_runtime.py` | `a5eb42d1ca29151728f270a2480005033cd4ecf4` |
| `softly-runtime/manifest.json` | `5ccf4e2969c0c548c8b755ed31a8822987e00880` |

Comparación Git confirmada: HEAD candidato está 2 commits adelante de la base, 0 detrás. El diff afecta exclusivamente `runtime.py` y `test_runtime.py` (186 y 75 líneas añadidas, respectivamente). No se observaron cambios en `main`, manifiesto, ledger, checkpoint ni artefactos del workspace.

La rama fue creada directamente desde la base autorizada. Los commits auditados no fueron reescritos.

## 2. Inspección del bloqueo actual

En la base, `execute()` entra a `_locked_ledger()` y conserva el lock exclusivo durante verificación, autorización, creación del artefacto y persistencia del evento. `_locked_ledger()` abre `events.jsonl`, adquiere `flock(LOCK_EX)` sobre ese descriptor y mantiene el bloqueo hasta salir del contexto.

Por tanto, `recover_ledger()` comparte actualmente el mismo mecanismo y orden de lock si utiliza `_locked_ledger()`. No se identificó una segunda jerarquía de locks dentro de estas rutas.

**Limitación importante:** el lock se asocia al inode de `events.jsonl`, no a un archivo de lock independiente. Si un actor externo sustituye el path del ledger, procesos distintos podrían abrir y bloquear inodes diferentes. La comprobación de identidad reduce la ventana, pero una validación de path seguida de `ftruncate()` no es una operación atómica frente a un actor que pueda sustituir el nombre en ese intervalo. Esto debe permanecer como limitación explícita o resolverse mediante un cambio de diseño revisado; no se debe afirmar que `flock` evita por sí solo esta clase de sustitución.

## 3. Funcionalidad presente en el candidato

La lectura del código confirma que se añadió:

- método administrativo `recover_ledger()`, fuera de `allowed_operations`;
- validación de formato del checkpoint y recorrido de prefijo íntegro;
- rechazo cuando no se encuentra un checkpoint confirmado;
- respaldo exclusivo con escritura, lectura de comprobación, hash y sincronización;
- comprobación de identidad de descriptor/path antes de truncar;
- truncamiento del sufijo posterior al checkpoint, sin reescribir `events.head`;
- verificación byte a byte y verificación del ledger después del truncamiento;
- informe administrativo separado;
- cinco pruebas nuevas: recuperación/idempotencia, checkpoint ajeno, corrupción previa al checkpoint, checkpoint GENESIS y conservación de artefactos.

## 4. Bloqueadores de aceptación identificados

### B-01 — Un fallo de fsync puede permitir que execute() opere después

En `recover_ledger()`, después de `ftruncate()`, si `fsync(ledger_fd)` lanza `OSError`, el método devuelve `status='failed'`. Sin embargo, no persiste un estado de cuarentena ni un marcador que `execute()` consulte.

Si el truncamiento dejó los bytes exactamente en el prefijo y una verificación posterior resulta positiva, `execute()` puede aceptar el ledger y continuar. Eso no satisface el criterio estricto de Autumn: un fallo de truncamiento/fsync debe mantener las operaciones bloqueadas hasta una reexaminación administrativa explícita que determine el estado real y su durabilidad.

**Resolución requerida:** proponer y revisar un mecanismo de bloqueo durable o una regla equivalente que sobreviva al proceso y al reinicio. No usar un flag solo en memoria. No borrar ni reconstruir evidencia. Si no se puede demostrar el estado tras un fallo de sincronización, mantener el runtime bloqueado.

### B-02 — Carrera residual entre revalidación de path y truncamiento

El candidato vuelve a comprobar dispositivo/inode y nombre antes de truncar, pero la comparación y `ftruncate()` no son atómicas respecto de la sustitución externa del path. El lock sobre el inode antiguo no serializa a un proceso que abra un inode nuevo tras reemplazo.

**Resolución requerida:** Autumn debe decidir si el modelo de amenaza permite acotar esto a actores cooperativos y permisos privados, o si requiere un lock estable independiente y protección de la entrada del directorio. Cualquier cambio a la semántica del lock requiere revisión antes de implementarse.

### B-03 — Pruebas insuficientes respecto de la matriz aprobada

Las cinco pruebas nuevas no cubren aún:
- fallo de creación/escritura/fsync del respaldo;
- colisión y preservación de respaldo previo;
- fallo de `ftruncate()`;
- fallo de `fsync()` después del truncamiento y bloqueo posterior de `execute()`;
- interrupción/reintento con ledger intacto, exactamente truncado y parcialmente truncado;
- fallo de persistencia del informe y su semántica posterior;
- concurrencia entre procesos de `execute()` y `recover_ledger()`;
- inspección de bytes, hashes, checkpoint y estado de bloqueo en cada escenario.

La prueba de concurrencia original usa hilos y no sustituye la prueba multiproceso exigida.

### B-04 — Pruebas no ejecutadas por Katarina en este corte

No se ejecutó `python -m unittest -v test_runtime`, `py_compile` ni otra suite sobre estos blobs exactos. Por tanto no hay resultado de ejecución atribuible a Katarina para el HEAD candidato. El informe no infiere éxito a partir de la inspección estática.

### B-05 — Referencia de respaldo si falla fsync del directorio

Si la copia se crea y su archivo se sincroniza, pero falla el `fsync` del directorio, el archivo de respaldo puede quedar presente aunque `_preserve_recovery_evidence()` lance antes de devolver su nombre. La respuesta de `recover_ledger()` puede indicar `backup=None` aunque haya quedado un archivo de evidencia. La recuperación no trunca en ese camino, pero el resultado no identifica con precisión el residuo preservado.

**Resolución requerida:** definir el resultado y la referencia recuperable del respaldo ante fallo de sincronización del directorio. No borrar evidencia válida para simplificar el estado.

### B-06 — Frontera administrativa de la API

El método no está en el manifiesto, pero es un método público del objeto runtime. La frontera que autoriza quién puede invocarlo administrativamente no está implementada ni definida en el código. Confirmar si la autorización se garantiza exclusivamente por el proceso/llamador confiable o si se requiere un capability/entrypoint administrativo explícito.

## 5. Dictamen de esta revisión

**NO LISTO para retest de aceptación ni para cerrar F-03.**

La rama y el alcance Git están dentro de la autorización. La implementación es un primer candidato útil, no una versión validada. Los bloqueadores B-01 y B-02 son de diseño/seguridad; B-03 a B-06 requieren implementación, pruebas o decisión explícita.

No se ejecutaron pruebas. No se creó PR. No se integró a `main`. No se modificó Mini 0.3 ni se desplegó en producción.

## 6. Próximos pasos obligatorios

1. Presentar a Autumn B-01 y B-02 con propuesta concreta antes de modificar su solución.
2. Resolver B-05 y B-06 por escrito.
3. Completar la matriz de regresión B-03.
4. Ejecutar pruebas sobre blobs exactos y registrar entorno, versión de Python, comandos, salidas y hashes.
5. Revisar diff y blobs de nuevo; luego entregar el commit candidato a Autumn para retest independiente.
6. Mantener F-03 abierto hasta el retest independiente satisfactorio y la integración autorizada.

## 7. Límites vigentes

- `main` intacta.
- Base auditada `9e8bc1015cc60d3cb097d3497459d1cd28b57d69` inmutable.
- Rama de trabajo aislada.
- No cambiar formato del ledger/checkpoint.
- No restaurar respaldo automáticamente ni reconstruir `events.head`.
- No borrar/modificar artefactos del workspace.
- No avanzar a Mini 0.3 ni producción.
