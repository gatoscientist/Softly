# ADR-0002 — Incorporar Softly Runtime Mini 0.1 como prototipo

- **ID:** ADR-0002
- **Fecha:** 2026-11-14
- **Estado:** Aceptada
- **Tipo:** Decisión de arquitectura y alcance
- **Responsable técnica:** Katarina (`agentdev-katarina`), versión 1.0.0, estado Diseñado
- **Implementación:** Softly Runtime Mini 0.1
- **Commit de implementación:** `b112189e3eab4a796ed4c3d0831689b8a04ee985`
- **Reemplaza parcialmente:** [ADR-0001](ADR-0001-laboratorio-documental-antes-de-runtime.md)

## Contexto

ADR-0001 estableció que Softly comenzaría como laboratorio documental y experimental, sin elegir framework ni construir runtime. Posteriormente, las propuestas técnicas de Auditoria definieron un alcance mínimo para demostrar enforcement determinista. Katarina implementó Softly Runtime Mini 0.1 en `softly-runtime/` y entregó pruebas para Python 3.13.

## Decisión

Incorporar `softly-runtime/` como prototipo experimental del laboratorio, bajo responsabilidad técnica de Katarina. La capacidad observada se limita a una operación autorizada de creación de archivos de texto dentro de un workspace confinado, rechazo de rutas que escapan del workspace y rechazo de capacidades no declaradas.

El estado del runtime es **Prototipado** y **Probado preliminarmente** (3/3 casos informados como superados). No se declara **Validado** ni **Operativo** para producción.

## Rationale y evidencia

- El prototipo convierte una parte acotada de las reglas declarativas en enforcement determinista.
- El manifiesto limita la operación permitida a `create_text_file`.
- La implementación valida la tarea, la operación y los parámetros; utiliza `Path.resolve()` y comprueba que el destino permanezca dentro del workspace.
- La suite cubre escritura permitida, escape relativo/absoluto del workspace y capacidad inexistente `delete_file`.
- El resultado se conserva en [EXP-20261114-001](../experiments/protocols/EXP-20261114-001-runtime-mini-enforcement.md) y [RES-20261114-001](../experiments/results/RES-20261114-001-runtime-mini-katarina.md).

## Consecuencias y límites

- ADR-0001 deja de describir el estado técnico actual en cuanto a ausencia de runtime, pero conserva su validez histórica como decisión de alcance inicial.
- Mini 0.1 no es un framework general ni un sandbox fuerte. No demuestra protección completa frente a carreras concurrentes, procesos comprometidos, manipulación local del ledger ni aptitud para producción.
- La auditoría independiente de Autumn está pendiente y es necesaria antes de considerar validación.
- Los archivos de `softly-runtime/` quedan fuera del alcance de esta actualización documental y no se modifican.

## Condición de revisión

Revisar cuando exista el informe independiente de Autumn o evidencia nueva obtenida en pruebas de aislamiento, concurrencia, integridad del ledger y recuperación. No reabrir esta decisión sin esa evidencia.

## Transición desde ADR-0001

ADR-0001 documentó la decisión inicial de mantener Softly como laboratorio documental. ADR-0002 registra una evolución deliberada y acotada: el laboratorio conserva su propósito de investigación, pero ahora incluye un prototipo de runtime. La decisión anterior no se borra ni se reescribe; su alcance histórico queda preservado.
