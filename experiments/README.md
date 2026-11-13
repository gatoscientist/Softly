# Experimentos

Los experimentos convierten hipótesis sobre agentes en resultados que otras personas pueden revisar y reproducir.

## Estructura

- `protocols/`: diseño antes de ejecutar.
- `results/`: resultados y análisis.
- `cases/`: casos de prueba sintéticos/anonimizados.
- `artifacts/`: solo artefactos no sensibles necesarios para reproducir.

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
