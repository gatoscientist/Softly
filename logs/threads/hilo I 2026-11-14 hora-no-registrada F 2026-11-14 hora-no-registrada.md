# Registro de hilo — recuperación F-03 de Softly Runtime Mini 0.2

- **Fecha de inicio:** 2026-11-14 (hora no registrada)
- **Corte documental:** 2026-11-14 (hora no registrada)
- **Estado:** snapshot de continuidad; el hilo no se declara cerrado
- **Fuente:** conversación disponible en ChatGPT y estado GitHub consultado durante este hilo
- **Fidelidad:** síntesis cronológica; no es transcripción literal completa. Las horas no están disponibles y no se estiman.

## Propósito

Completar F-03 (integridad del ledger) mediante una recuperación explícita y conservadora de `events.jsonl`, limitada por `events.head`, sin alterar los commits auditados ni habilitar operaciones cuando la evidencia sea insuficiente.

## Secuencia y decisiones

### 1. Aprobación condicionada del diseño

Autumn revisó la primera propuesta y aprobó el diseño con seis condiciones previas a programar:
1. protocolo durable y exclusivo de respaldo;
2. identidad estable de archivos mediante descriptores y revalidación;
3. comprobar que `execute()` comparte el mismo lock y lo mantiene durante toda la sección crítica;
4. tratar truncamientos parciales y fallos de sincronización como estados que requieren inspección real;
5. separar integridad operativa del informe administrativo;
6. distinguir `rejected` (sin modificaciones) de `failed` (pudo comenzar modificación y exige reexamen).

Katarina entregó una revisión del diseño con creación exclusiva, hash, `fsync` de archivo/directorio, identidad por `fstat`, lock compartido, inspección del ledger tras interrupciones, informe separado y semántica de resultados.

### 2. Aprobación para implementación acotada

Autumn aprobó el diseño revisado y autorizó:
- rama derivada exactamente de `9e8bc1015cc60d3cb097d3497459d1cd28b57d69`;
- implementación exclusiva de `recover_ledger()` y pruebas;
- cambios iniciales limitados a `softly-runtime/runtime.py` y `softly-runtime/test_runtime.py`;
- conservar seis pruebas originales y agregar regresiones;
- presentar commit candidato para revisión independiente.

Autumn reiteró que el respaldo conserva evidencia, pero no garantiza recuperación tras cualquier interrupción. Quedó como regla no negociable: ante truncamiento parcial, discrepancia de identidad o estado que no coincida exactamente con el prefijo confirmado, rechazar y mantener el runtime bloqueado; nunca restaurar automáticamente el respaldo ni reconstruir `events.head`.

No se autorizó modificar `main`, reescribir commits auditados, cambiar el formato del ledger/checkpoint, tocar artefactos, avanzar a Mini 0.3 ni desplegar en producción.

### 3. Inspección del lock y creación de rama

Katarina recuperó desde GitHub los blobs del commit base y comprobó que `execute()` entra en `_locked_ledger()`. Ese contexto abre `events.jsonl`, toma `flock(LOCK_EX)` y mantiene el bloqueo durante verificación, creación del artefacto y persistencia del evento.

Se creó la rama:
- `fix/f03-recover-ledger`
- base exacta: `9e8bc1015cc60d3cb097d3497459d1cd28b57d69`

Se identificó una limitación: el lock está asociado al inode del ledger, no a un archivo independiente y estable. Una sustitución externa del path puede permitir que dos procesos bloqueen inodes diferentes. La revalidación de identidad reduce el riesgo, pero no vuelve atómica la comprobación del path y el truncamiento.

### 4. Commits de implementación publicados

Primer commit:
- `139f42eab83caf0cb8598cfa348caa0cf4c94f95`
- añadió `recover_ledger()`, respaldo, informe y cinco pruebas nuevas.

Segundo commit:
- `d9982cf764b71a0aeeada491ef19acad7a4c7b44`
- corrigió los literales de límites de línea que habían quedado escapados incorrectamente en el primer commit.

HEAD actual al corte:
- `d9982cf764b71a0aeeada491ef19acad7a4c7b44`
- comparación con la base: 2 commits adelante, 0 detrás.
- únicos archivos modificados: `softly-runtime/runtime.py` y `softly-runtime/test_runtime.py`.
- blobs: runtime `07e0accab4398d984d7df8c4dda8bd44ebf0b4aa`; tests `a5eb42d1ca29151728f270a2480005033cd4ecf4`.

### 5. Revisión interna posterior

Katarina volvió a leer los blobs publicados y detectó bloqueadores:
- **B-01:** si `fsync(ledger_fd)` falla después de truncar, `recover_ledger()` devuelve `failed`, pero no persiste una cuarentena. Si el ledger se ve como prefijo válido, `execute()` podría verificarlo y operar. Esto contradice el criterio de mantener bloqueo después de un fallo de sincronización hasta reexamen administrativo explícito.
- **B-02:** la revalidación de path y el `ftruncate()` no son atómicos frente a sustitución externa del nombre; el lock por inode no serializa necesariamente al proceso que abre el inode nuevo.
- **B-03:** faltan pruebas para fallos del respaldo, colisión, `ftruncate`, `fsync`, interrupciones, persistencia del informe y concurrencia multiproceso.
- **B-04:** Katarina no ejecutó `py_compile` ni `python -m unittest -v test_runtime` sobre los blobs exactos; no existe resultado de suite atribuible a este corte.
- **B-05:** si falla el `fsync` del directorio después de crear el respaldo, el respaldo podría quedar presente pero la respuesta no conservar su nombre.
- **B-06:** el método está fuera del manifiesto, pero la frontera de quién puede invocarlo administrativamente no está definida en el código.

Se publicó un informe detallado en `logs/maintenance/2026-11-14-f03-recovery-review.md`.

## Archivos y rutas documentales de este corte

- Informe técnico: `logs/maintenance/2026-11-14-f03-recovery-review.md`
- Este registro: `logs/threads/hilo I 2026-11-14 hora-no-registrada F 2026-11-14 hora-no-registrada.md`
- Implementación: `softly-runtime/runtime.py`
- Pruebas: `softly-runtime/test_runtime.py`

## Estado al corte

- Diseño de recuperación: aprobado por Autumn.
- Implementación acotada: autorizada y publicada en rama aislada.
- Revisión interna: encontró seis bloqueadores/pendientes.
- Retest independiente de Autumn: pendiente.
- Integración de Audeline: pendiente de retest satisfactorio.
- F-03: abierto.
- Mini 0.2: no validado globalmente.
- Mini 0.3 y producción: no autorizados.
- `main`: intacta.
- Commits auditados: no reescritos.

## Punto exacto para continuar

No añadir más cambios de código todavía. Presentar a Autumn B-01 y B-02 con propuesta técnica para resolver cuarentena durable y semántica del lock; pedir decisión sobre B-05 y B-06. Después completar la matriz de pruebas, ejecutar pruebas sobre blobs exactos, registrar hashes y resultados, y recién entonces entregar el candidato a retest independiente.

## Límites del registro

Este archivo resume los mensajes disponibles y las acciones confirmadas por respuestas de herramientas. No conserva una transcripción completa del chat ni horas no registradas. No incluye cadena de pensamiento privada. Los resultados reportados históricamente por Autumn se mantienen atribuidos a Autumn; las acciones de Katarina se limitan a lo comprobado en este hilo.
