# EXP-20261114-002 — Softly Runtime Mini 0.2: aislamiento y ledger encadenado

- **Ciclo:** 2 — aislamiento e integridad de ledger
- **Responsable de implementación:** Katarina (`agentdev-katarina`)
- **Objeto:** Softly Runtime Mini 0.2 en `softly-runtime/`
- **Corte evaluado:** `e1014932fcfe9bf5d69c8aaa3ed6adf157bfeef2`
- **Entorno reportado:** Python 3.13.5
- **Estado:** ejecución reportada por la implementadora; CODE AUD independiente de Autumn pendiente

## 1. Pregunta e hipótesis

¿La versión Mini 0.2 reduce los riesgos F-01 y F-03 del Ciclo 1 mediante confinamiento basado en descriptores de directorio y un ledger protegido, bloqueado y verificable por encadenamiento de hashes?

- **H1 — F-01:** la resolución/travesía relativa a descriptores, con `O_NOFOLLOW` en cada componente, impide que symlinks en directorios padres o en el destino redirijan escrituras fuera del workspace. Si no están disponibles las primitivas requeridas, el runtime debe fallar cerrado.
- **H2 — F-03:** la apertura segura del ledger, bloqueo exclusivo, escritura durable y encadenamiento/checkpoint permiten detectar sustitución, truncamiento, reordenamiento y alteración; una falla de persistencia no debe comunicar éxito.
- **H3 — Regresión:** los comportamientos de Mini 0.1, incluida la distinción F-02 entre política y error del filesystem, permanecen consistentes.

## 2. Baseline y alcance

El baseline es el commit exacto `e1014932fcfe9bf5d69c8aaa3ed6adf157bfeef2`. Se inspeccionan solo estos cinco archivos, sin modificarlos:
- `softly-runtime/manifest.json`
- `softly-runtime/runtime.py`
- `softly-runtime/test_runtime.py`
- `softly-runtime/events.jsonl`
- `softly-runtime/events.head`

El manifiesto declara una sola capacidad: `create_text_file`, tarea `runtime-mini-smoke-test` y workspace `softly-runtime/workspace/`.

## 3. Controles que se examinan

### F-01 — Confinamiento de workspace

- Rechazo de plataforma cuando no se dispone de las primitivas seguras requeridas.
- Apertura y recorrido de directorios con descriptores `dir_fd`, `O_DIRECTORY` y `O_NOFOLLOW`.
- Comprobación de identidad del directorio abierto mediante `fstat` frente a la inspección previa sin seguir symlinks.
- Directorios privados con permisos `0700`, comprobación de propietario y rechazo de componentes que no sean directorios regulares.
- Apertura del archivo final relativa al descriptor del workspace, sin seguir symlinks.

### F-03 — Integridad del ledger

- Rechazo de symlinks y de objetos que no sean archivos regulares para `events.jsonl` y `events.head`.
- Bloqueo exclusivo durante operaciones de ledger (`flock` en POSIX o alternativa `msvcrt` cuando corresponda).
- Registro JSONL con `previous_event_hash` y `event_hash`; el primer evento parte de `GENESIS`.
- Checkpoint `events.head`, inicializado como `GENESIS\n`, actualizado de forma controlada.
- Escritura y sincronización con `fsync`; verificación de cadena y checkpoint mediante `verify_ledger()`.
- Ante un error de escritura parcial, no confirmar la operación como exitosa y comprobar recuperación/restauración del ledger según el comportamiento implementado.

## 4. Casos y criterios observables

La suite declara seis métodos de prueba:

1. **Regresión de escritura y no sobrescritura:** creación autorizada, evento íntegro y rechazo de segundo intento sobre archivo existente sin alterar su contenido.
2. **Escape de workspace:** rechazo de traversal relativo y ruta absoluta externa, sin escritura externa.
3. **Capacidad y parámetros:** rechazo de `delete_file`, parámetro adicional y parámetro faltante.
4. **F-02:** error `PermissionError` posterior a autorización produce exactamente un evento `authorized/error`, sin artefacto.
5. **F-01:** symlink en directorio padre y en archivo destino no permite escritura externa; reemplazo del workspace por symlink debe impedir inicialización segura.
6. **F-03:** ledger symlink rechazado sin tocar destino externo; encadenamiento desde `GENESIS`; verificación; concurrencia de 12 escrituras entre dos instancias y seis threads; fallo parcial simulado; detección de truncamiento, reordenamiento y alteración; rechazo de permisos inseguros.

**Criterio de éxito informado:** los seis métodos de prueba pasan en el entorno reportado. La suite automatizada no sustituye la auditoría adversarial independiente ni demuestra todas las condiciones de carrera posibles.

## 5. Límites del protocolo

- La implementación exige primitivas POSIX para el confinamiento; otras plataformas deben fallar cerradamente según el código y no se consideran soportadas por inferencia.
- La prueba concurrente descrita usa dos instancias del runtime y threads dentro de un proceso; no equivale a una prueba multiproceso ni a una campaña de estrés prolongada.
- Las pruebas de symlink y monkeypatch no cubren todos los patrones posibles de carrera TOCTOU.
- Hashes encadenados y checkpoint detectan alteraciones respecto del estado esperado, pero no constituyen por sí solos una firma externa, un anclaje remoto ni inmutabilidad frente a un actor con control total del directorio y del proceso.
- El runtime no se clasifica como sandbox fuerte, Validado ni Operativo para producción por la sola aprobación de su suite local.

## 6. Evidencia, procedencia y evaluación independiente

La ejecución **6/6** en Python 3.13.5 es un resultado reportado por Katarina para el corte exacto indicado. Los hashes SHA-256 y Git Blob SHA de los cinco archivos se registran en `RES-20261114-002-runtime-mini-0.2-katarina.md`.

**Pendiente:** CODE AUD independiente de Autumn. La evaluadora debe fijar el corte, revisar el modelo de amenaza, reproducir las pruebas que considere necesarias y separar revisión estática de ejecución dinámica. No modificar el objeto auditado.

## 7. Resultado asociado

[RES-20261114-002 — Runtime Mini 0.2 / Katarina](../results/RES-20261114-002-runtime-mini-0.2-katarina.md).
