# ADR-0003 — Aislamiento y ledger encadenado en Softly Runtime Mini 0.2

- **ID:** ADR-0003
- **Fecha:** 2026-11-14
- **Estado:** Aceptada
- **Tipo:** Decisión de arquitectura y evolución experimental
- **Responsable técnica declarada:** Katarina (`agentdev-katarina`)
- **Versión:** Softly Runtime Mini 0.2.0
- **Corte de implementación:** `e1014932fcfe9bf5d69c8aaa3ed6adf157bfeef2`
- **Evoluciona:** [ADR-0002 — Runtime Mini 0.1](ADR-0002-incorporacion-runtime-mini-0.1.md)

## Contexto

El Ciclo 1 incorporó Mini 0.1 como prototipo de enforcement acotado. El retest de Autumn `AUT-20261114-009` cerró F-02 por revisión estática y concedió GO con limitaciones para avanzar. F-01 (TOCTOU/symlinks en directorios padres) y F-03 (protección, integridad y concurrencia del ledger) quedaron abiertos y fueron transferidos al Ciclo 2. El cierre de ciclo quedó integrado por Audeline en `AUD-20261114-011`.

Katarina implementó Mini 0.2 y reportó 6/6 métodos de prueba superados en Python 3.13.5 sobre el corte indicado.

## Decisión

Incorporar el corte `e1014932...` como **Softly Runtime Mini 0.2**, prototipo que añade controles de aislamiento del workspace y de integridad verificable del ledger, manteniendo la capacidad declarada única `create_text_file`.

### F-01 — Aislamiento

- Recorrido de directorios mediante descriptores `dir_fd`, `O_DIRECTORY` y `O_NOFOLLOW`.
- Comparación de identidad de directorios abiertos y verificación de permisos/propietario.
- Directorios privados con permisos `0700`.
- Apertura del destino relativa al descriptor del workspace y rechazo de symlinks.
- Fallo cerrado cuando faltan las primitivas de confinamiento requeridas.

### F-03 — Ledger encadenado

- Apertura protegida de `events.jsonl` y `events.head`, rechazando symlinks y objetos no regulares.
- Bloqueo exclusivo con `flock` / `msvcrt` según la implementación.
- Cadena SHA-256 por evento con `previous_event_hash` y `event_hash`.
- Checkpoint `events.head`, cuyo estado inicial es `GENESIS\n`.
- Sincronización mediante `fsync` y verificación por `verify_ledger()`.

## Evidencia y estado

El registro [EXP-20261114-002](../experiments/protocols/EXP-20261114-002-runtime-mini-0.2-isolation-ledger.md) define el alcance y los criterios. [RES-20261114-002](../experiments/results/RES-20261114-002-runtime-mini-0.2-katarina.md) conserva el resultado reportado de 6/6 y las huellas SHA-256/Git Blob SHA de los cinco archivos del corte.

**Clasificación:** Prototipado / Probado preliminarmente. La ejecución 6/6 es reportada por Katarina; CODE AUD independiente de Autumn está pendiente. No se declara Validado ni Operativo para producción.

## Límites y riesgos residuales

- La prueba de concurrencia usa dos instancias y seis threads dentro de un proceso; no demuestra concurrencia multiproceso ni estrés prolongado.
- La suite no demuestra cobertura exhaustiva de carreras TOCTOU ni de todas las plataformas.
- El código exige primitivas POSIX para el confinamiento y falla cerrado cuando no están disponibles.
- Una cadena SHA-256 y un checkpoint local detectan determinadas alteraciones, pero no equivalen a firma externa, anclaje remoto ni inmutabilidad frente a un actor con control total del entorno.
- No se demuestra sandbox fuerte, aislamiento frente a procesos comprometidos ni aptitud productiva.

## Condición de revisión

La auditoría CODE AUD independiente de Autumn debe evaluar el corte exacto, el modelo de amenaza, los controles, la suite y los límites, sin modificar los cinco archivos de `softly-runtime/`. Registrar por separado revisión estática y cualquier ejecución dinámica independiente. Solo evidencia adicional podrá justificar cambio de clasificación.

## Transición desde ADR-0002

ADR-0002 permanece como registro histórico de Mini 0.1 y del primer alcance de enforcement. ADR-0003 incorpora la evolución experimental de Mini 0.2 para abordar F-01 y F-03, sin borrar la secuencia de decisiones ni convertir el resultado de la implementadora en validación independiente.
