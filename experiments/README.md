# Experimentos

Los experimentos convierten hipótesis sobre agentes en resultados que otras personas pueden revisar y reproducir.

## Estructura

- [Protocolos](protocols/README.md): diseño antes de ejecutar.
- [Resultados](results/README.md): resultados y análisis.
- [Casos](cases/README.md): casos de prueba sintéticos/anonimizados.
- Los artefactos no sensibles necesarios para reproducir pueden adjuntarse cuando exista un experimento que los requiera; no hay un directorio `artifacts/` creado actualmente.

## ID

`EXP-YYYYMMDD-NNN`.

## Protocolo mínimo

- Pregunta e hipótesis falsable.
- Agente/configuración versionada.
- Baseline de comparación.
- Modelo, proveedor, harness y parámetros.
- Dataset/casos y origen.
- Variables controladas y variables que cambian.
- Métricas y criterios de éxito/fallo.
- Límites de seguridad y coste.
- Procedimiento reproducible.
- Plan de análisis.

## Resultado mínimo

Fecha de ejecución, entorno, versión exacta, casos ejecutados, fallos, resultados brutos o referencias seguras, desviaciones, limitaciones y conclusión calibrada. Separar diseñado de ejecutado.

No borrar resultados fallidos. Una repetición crea una nueva ejecución enlazada.

Los subdirectorios de protocolos, resultados y casos contienen actualmente solo sus README de preparación; todavía no hay artefactos experimentales registrados.
