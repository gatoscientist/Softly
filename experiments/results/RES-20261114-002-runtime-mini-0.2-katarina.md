# RES-20261114-002 — Softly Runtime Mini 0.2 implementado por Katarina

- **Protocolo:** [EXP-20261114-002](../protocols/EXP-20261114-002-runtime-mini-0.2-isolation-ledger.md)
- **Responsable técnica declarada:** Katarina (`agentdev-katarina`)
- **Versión:** Softly Runtime Mini 0.2.0
- **Corte exacto:** `e1014932fcfe9bf5d69c8aaa3ed6adf157bfeef2`
- **Entorno reportado:** Python 3.13.5
- **Resultado reportado:** **6/6 métodos de prueba superados**
- **Estado:** Prototipado / Probado preliminarmente; CODE AUD independiente de Autumn pendiente

## 1. Resultado reportado

Katarina reporta seis métodos de prueba superados en Python 3.13.5 sobre el corte exacto indicado. La suite incluye regresión de escritura/no sobrescritura, escape relativo y absoluto, capacidad/parámetros inválidos, regresión F-02, symlinks de workspace y controles de integridad/concurrencia del ledger.

La inspección de `test_runtime.py` confirma seis métodos de test. El registro de 6/6 corresponde al resultado comunicado por la implementadora; no es una repetición dinámica independiente de Autumn.

## 2. Cambios técnicos observados

### F-01 — Confinamiento

- Recorrido de directorios mediante descriptores `dir_fd`, `O_DIRECTORY` y `O_NOFOLLOW`.
- Comparación de identidad del directorio abierto con la entrada inspeccionada sin seguir symlinks.
- Permisos privados `0700`, verificación de propietario y rechazo de componentes no-directorio.
- Apertura de archivo final relativa al descriptor del workspace.
- Fallo cerrado si faltan las primitivas seguras requeridas.

### F-03 — Ledger

- Protección contra symlinks y objetos no regulares en `events.jsonl` y `events.head`.
- Bloqueo exclusivo con `flock` / `msvcrt` según la implementación.
- Encadenamiento SHA-256 mediante `previous_event_hash` y `event_hash`, iniciado en `GENESIS`.
- Checkpoint `events.head`, cuyo estado inicial versionado es `GENESIS\n`.
- Sincronización de escritura con `fsync` y comprobación mediante `verify_ledger()`.

## 3. Cobertura observada en la suite

| Test | Cobertura | Resultado reportado |
|---|---|---|
| Caso 1 | Escritura autorizada, evento, no sobrescritura | Superado |
| Caso 2 | Escape relativo y absoluto | Superado |
| Caso 3 | `delete_file`, parámetros extra/faltantes | Superado |
| Caso 4 | `PermissionError` posterior a autorización, evento coherente | Superado |
| Caso 5 | Symlink en padre/destino y sustitución del workspace | Superado |
| Caso 6 | Symlink de ledger, hash chain, concurrencia, fallo parcial, truncamiento, reordenamiento, tampering y permisos | Superado |

**Alcance de concurrencia:** el Caso 6 crea dos instancias del runtime y ejecuta 12 escrituras mediante seis threads en un mismo proceso. No debe describirse como prueba multiproceso.

## 4. Huellas de los cinco archivos del corte

Los Git Blob SHA corresponden a la identidad de contenido registrada por GitHub para el corte `e1014932...`. SHA-256 se calcula sobre los bytes UTF-8 del contenido recuperado.

| Archivo | Bytes | SHA-256 | Git Blob SHA |
|---|---:|---|---|
| `softly-runtime/manifest.json` | 356 | `53caa0a9772f06df6cf41899bde4271343185255299db4764a6248ce3a725c5e` | `5ccf4e2969c0c548c8b755ed31a8822987e00880` |
| `softly-runtime/runtime.py` | 22596 | `14dc85bae4b3759bb52177774cdbcb1b27040d98d8dfae76c984461a32bb78f3` | `7cfcef962bde7c26367f8d7d9347dc0099f47593` |
| `softly-runtime/test_runtime.py` | 12422 | `1bbac498162a3e37e4d641c9451cb11ac820506846ab9035516f2695acc146e6` | `efc9bfea49425742f3bdcb75786b413abcfc3e9e` |
| `softly-runtime/events.jsonl` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| `softly-runtime/events.head` | 8 | `741d772c2c79fe41356302cc1cb548b15eb071dee8849c5278d0269a5bc36e71` | `5e3f8f7bb1d656dedade88879ddf86a95550fea9` |

Los cinco archivos se inspeccionaron en modo lectura. Esta intervención documental no modifica, mueve ni formatea contenido de `softly-runtime/`.

## 5. Interpretación y límites

La implementación incorpora controles concretos para los dos hallazgos transferidos del Ciclo 1. La suite reportada cubre casos positivos, negativos, symlinks, concurrencia en threads, fallo parcial y verificación de integridad.

No obstante:
- El resultado 6/6 procede del reporte de Katarina; aún no es validación independiente.
- La concurrencia probada es intraproceso, no multiproceso.
- No se demuestra cobertura exhaustiva de TOCTOU ni de todas las plataformas.
- El encadenamiento y checkpoint SHA-256 no equivalen a anclaje externo ni a inmutabilidad frente a un actor con control total del entorno.
- No se declara sandbox fuerte, Validado ni Operativo para producción.

## 6. Próximo control independiente

**Pendiente obligatorio: CODE AUD de Autumn** sobre el corte `e1014932fcfe9bf5d69c8aaa3ed6adf157bfeef2`, sin modificar los cinco archivos del objeto auditado. El dictamen deberá distinguir:
1. revisión estática de diseño y código;
2. ejecución independiente efectivamente realizada;
3. cobertura y límites del modelo de amenaza;
4. hallazgos, severidad, evidencia y recomendación GO/NO-GO.

**Clasificación actual:** Softly Runtime Mini 0.2 — **Prototipado / Probado preliminarmente**. Auditoría independiente pendiente; no Validado ni Operativo para producción.
