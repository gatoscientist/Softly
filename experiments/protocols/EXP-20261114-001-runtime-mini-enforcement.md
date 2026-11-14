# EXP-20261114-001 — Enforcement del Softly Runtime Mini 0.1

- **Tipo:** protocolo de experimento de enforcement determinista
- **Responsable de implementación:** Katarina (`agentdev-katarina`, 1.0.0)
- **Objeto:** `softly-runtime/`
- **Versión evaluada:** Softly Runtime Mini 0.1
- **Commit bajo evaluación:** `b112189e3eab4a796ed4c3d0831689b8a04ee985`
- **Entorno informado:** Python 3.13
- **Estado del protocolo:** ejecutado; evaluación independiente pendiente

## 1. Pregunta e hipótesis

**Pregunta:** ¿El prototipo Mini 0.1 aplica por código una autorización explícita antes de crear archivos, impide escapes del workspace y rechaza capacidades no declaradas?

**Hipótesis:** las solicitudes autorizadas crearán un archivo únicamente dentro del workspace; las rutas que escapen del workspace y las operaciones no declaradas serán rechazadas sin producir el efecto solicitado y dejarán un evento de rechazo.

## 2. Alcance y baseline

El objeto de evaluación son exclusivamente los cuatro archivos entregados por Katarina: `manifest.json`, `runtime.py`, `events.jsonl` y `test_runtime.py`. El baseline de código es el commit indicado arriba. No se modifican esos archivos durante la documentación de este experimento.

El manifiesto declara la tarea `runtime-mini-smoke-test`, el workspace `softly-runtime/workspace/` y la única operación permitida `create_text_file`.

## 3. Casos y criterios

1. **Escritura permitida:** crear `hello.txt` dentro del workspace; comprobar existencia, contenido UTF-8 y evento con autorización `authorized`, ejecución `success` y referencia del artefacto.
2. **Escape de workspace:** intentar rutas relativas con traversal y una ruta absoluta externa; comprobar rechazo, ausencia de archivos externos y eventos `denied/rejected`. La implementación utiliza `Path.resolve()` y comprueba la pertenencia mediante `relative_to()`.
3. **Capacidad inexistente:** solicitar `delete_file`, ausente del manifiesto; comprobar rechazo, ausencia de efecto y evento `denied/rejected`.

**Éxito:** los tres casos cumplen sus aserciones observables. El protocolo no considera suficiente comprobar únicamente el mensaje de retorno.

## 4. Evidencia de ejecución registrada

Según el resultado de ejecución entregado para Python 3.13, se superaron **3/3 casos**. El archivo `test_runtime.py` contiene las aserciones de los tres casos. La inspección estática de los archivos confirma la correspondencia entre esos criterios y las pruebas implementadas.

Los tests usan directorios temporales; el `events.jsonl` versionado en el commit evaluado está vacío y las pruebas crean sus registros en el paquete temporal de cada caso. No se interpreta el archivo vacío versionado como ausencia de instrumentación.

## 5. Límites y riesgos

- Resultado preliminar de un prototipo local; no equivale a validación de seguridad.
- `Path.resolve()` y las comprobaciones de rutas no reemplazan un sandbox del sistema operativo.
- El propio código declara límites ante carreras concurrentes y procesos locales comprometidos.
- No se demuestra aislamiento fuerte, resistencia criptográfica del ledger, control de concurrencia ni aptitud para producción.
- No se ejecutó una auditoría independiente en este registro.

## 6. Evaluación independiente y cierre

**Pendiente:** auditoría independiente de Autumn sobre diseño y código, sin modificar el objeto auditado. Hasta recibirla, el resultado se clasifica como **Probado preliminarmente**, no Validado ni Operativo.

La evaluación posterior debe conservar el commit exacto, registrar cualquier discrepancia y separar observaciones estáticas de nuevas ejecuciones.

## 7. Trazabilidad

- Implementación y pruebas: Katarina, `agentdev-katarina` v1.0.0.
- Commit: `b112189e3eab4a796ed4c3d0831689b8a04ee985`.
- Insumos de diseño: `PROP-20261114-001` y `PROP-20261114-002`, repositorio Auditoria.
- Método longitudinal relacionado: `AUR-20261114-008`, tres ciclos de mejora de Softly.
- Resultado asociado: [RES-20261114-001](../results/RES-20261114-001-runtime-mini-katarina.md).
