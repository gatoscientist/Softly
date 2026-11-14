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

---

## Adenda de cierre — Ciclo 1 / retest independiente AUT-20261114-009

**Fecha de sincronización:** 2026-11-14  
**Corte de remediación:** `fea471a2eaff56d3c90117e1008bf1dfaa66d348`  
**Informe de retest:** [AUT-20261114-009 — Retest CODE AUD](https://github.com/gatoscientist/Auditoria/blob/main/Autumn/reports/AUT-20261114-009-retest-runtime-mini-0.1.md)  
**Integración de cierre:** [AUD-20261114-011 — Audeline](https://github.com/gatoscientist/Auditoria/blob/main/Audeline/reports/AUD-20261114-011-integracion-cierre-ciclo-1-runtime-mini-0.1.md)

### Remediación F-02

Katarina corrigió la distinción entre denegación de política y error del sistema de archivos en el commit `fea471a2eaff56d3c90117e1008bf1dfaa66d348`. La remediación separa `_PolicyDenied` de los errores `OSError`, preservando la autorización ya concedida cuando la creación falla por `PermissionError`.

La evidencia de regresión incorporó el Caso 4. El resultado reportado para el parche fue **4/4 pruebas OK**, con el evento posterior a autorización manteniendo:
- `authorization_result: "authorized"`;
- `execution_result: "error"`;
- `artifact_reference: null`.

Autumn revisó estáticamente el diff, el flujo de emisión única y las aserciones. **Autumn no ejecutó Python ni repitió dinámicamente la suite** en este retest.

### Dictamen y límites

**AUT-20261114-009: GO concedido con limitaciones** para cerrar la remediación F-02 y avanzar al diseño/implementación de Mini 0.2. El GO no certifica sandbox, aislamiento fuerte, seguridad integral ni aptitud para producción.

- **F-02:** cerrado por revisión estática independiente.
- **F-01:** permanecía abierto — TOCTOU y symlinks en directorios padres.
- **F-03:** permanecía abierto — protección, integridad, concurrencia y fallos del ledger.
- El `events.jsonl` versionado en el corte de remediación conservaba tamaño cero bytes; los tests trabajaban con ledgers temporales.

Audeline, en AUD-20261114-011, declara cerrado administrativamente el Ciclo 1 dentro del alcance de evidencia disponible y transfiere F-01/F-03 como núcleo del Ciclo 2. No convierte el retest estático en ejecución independiente ni declara Mini 0.1 Validado u Operativo.

**Estado de cierre del Ciclo 1:** F-02 superado estáticamente; GO limitado concedido; Mini 0.1 permanece como prototipo no productivo. Esta adenda complementa el resultado original sin reescribirlo.
