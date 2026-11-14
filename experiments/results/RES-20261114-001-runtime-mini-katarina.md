# RES-20261114-001 — Softly Runtime Mini 0.1 implementado por Katarina

- **Protocolo:** [EXP-20261114-001](../protocols/EXP-20261114-001-runtime-mini-enforcement.md)
- **Responsable técnica:** Katarina (`agentdev-katarina`, versión 1.0.0, estado `Diseñado`)
- **Versión evaluada:** Softly Runtime Mini 0.1
- **Commit evaluado:** `b112189e3eab4a796ed4c3d0831689b8a04ee985`
- **Entorno de pruebas informado:** Python 3.13
- **Estado:** 3/3 casos superados; pendiente auditoría independiente de Autumn

## Resultado

**3/3 casos superados**

| Caso | Comportamiento | Resultado |
|---|---|---|
| 1 | Escritura permitida de archivo dentro del workspace | Superado |
| 2 | Bloqueo de escape relativo y absoluto mediante resolución y comprobación de ruta | Superado |
| 3 | Rechazo de capacidad no declarada `delete_file` | Superado |

La suite `softly-runtime/test_runtime.py` verifica los efectos sobre el sistema de archivos temporal y los eventos registrados, no solo el valor de retorno. En el caso 2 comprueba tanto traversal relativo como ruta absoluta externa. En el caso 3 comprueba que el archivo objetivo no se crea y que el evento registra denegación y rechazo.

## Evidencia técnica observada

- `manifest.json` declara una única operación: `create_text_file`.
- `runtime.py` valida tarea y operación, rechaza parámetros ausentes o desconocidos, resuelve rutas con `Path.resolve()` y exige que el destino permanezca dentro del workspace.
- La creación usa apertura exclusiva (`O_EXCL`) y, cuando está disponible, `O_NOFOLLOW`.
- Cada solicitud intenta registrar un evento JSONL con decisión de autorización, resultado y referencia al artefacto.
- `events.jsonl` en el commit evaluado está vacío; las pruebas usan paquetes temporales y verifican allí la creación de eventos.

## Interpretación

El resultado demuestra preliminarmente enforcement determinista para el alcance reducido de Mini 0.1: escritura autorizada dentro del workspace, rechazo de rutas externas y rechazo de una capacidad inexistente. No demuestra seguridad integral ni aptitud para producción.

## Limitaciones y pendientes

- No hay sandbox del sistema operativo ni aislamiento fuerte frente a procesos comprometidos.
- No se demuestra protección completa ante carreras concurrentes, manipulación local del ledger, red, secretos o ejecución arbitraria.
- No se ha completado validación independiente.
- **Pendiente obligatorio:** auditoría independiente de Autumn sobre el diseño y el código, sin alterar el objeto auditado.

**Clasificación actual del runtime:** Prototipado / Probado preliminarmente. No Validado ni Operativo para producción.
