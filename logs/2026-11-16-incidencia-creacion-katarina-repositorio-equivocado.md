# INC-20261116-003 — Creación de Katarina en el repositorio equivocado

- **Fecha:** 2026-11-16
- **Actor:** Softly
- **Solicitante:** gAto
- **Tipo:** ejecución / resolución de repositorio / trazabilidad
- **Estado:** ubicación corregida y verificada; análisis causal pendiente
- **Severidad provisional:** alta para integridad de ubicación y confianza operativa
- **Observación asociada:** [OBS-20261116-004](../observations/OBS-20261116-004-confusion-repositorio-rutas-creacion-katarina-titan.md)

## Hecho

gAto pidió crear a Katarina en el proyecto TITAN, repositorio `gatoscientista/TITAN`. Softly interpretó inicialmente `/TITAN` como un directorio dentro de `gatoscientista/Softly` y creó allí la estructura de Katarina y Los Mancos. Además, actualizó el registro taxonómico de Softly para reflejar esa ubicación incorrecta.

## Consecuencias

- Se crearon 42 archivos bajo `TITAN/` en el repositorio Softly.
- Se modificó el registro taxonómico local para cuatro agentes.
- gAto tuvo que detectar y corregir la ubicación.
- Fue necesario migrar los paquetes, eliminar la copia equivocada y limpiar el registro local.
- La reparación incluyó consultas fallidas y una creación de árbol rechazada antes de completar el commit correcto.

## Corrección ejecutada y verificada

1. Paquetes publicados en `gatoscientista/TITAN/eL equipo del gAto/Direccion-TITAN/`.
2. Commit de TITAN: `9a2bd4df5340a15c31f334241824d59f89516f1c`.
3. Se eliminaron las 42 rutas de archivo de `TITAN/` en Softly mediante un commit nuevo; el historial previo se conservó.
4. Se retiraron cuatro entradas del registro `schemas/agent-taxonomy-registry.json` de Softly.
5. Se verificó que el árbol actual de Softly no conserva rutas `TITAN/`, que el registro ya no contiene esas cuatro entradas y que el paquete está presente en TITAN.
6. Evento de actividad: `EVT-20261116-013`, estado `verified_readback`.

Commits:
- [TITAN — 9a2bd4d](https://github.com/gatoscientist/TITAN/commit/9a2bd4df5340a15c31f334241824d59f89516f1c)
- [Softly — 37756a8](https://github.com/gatoscientist/Softly/commit/37756a8e449e9d3524a8f56acc6eeaed2aba332b)
- [Softly — verificación b174ed1](https://github.com/gatoscientist/Softly/commit/b174ed1131fbe79b1e3c516e74928705f5b0e8f0)

## Causa

La causa raíz no está demostrada. La observación asociada documenta hipótesis sobre ambigüedad de rutas, falta de preflight, continuidad del repositorio activo y actualización prematura de la taxonomía.

## Pendientes

- Diseñar una convención mínima de destinos: repositorio, rama y ruta.
- Definir un preflight obligatorio antes de escribir.
- Simplificar el mapa de casas canónicas, proyectos y directorios internos.
- Probar el procedimiento antes de declararlo eficaz.

**Criterio de cierre:** la ubicación incorrecta está corregida; el problema de proceso sigue abierto hasta que el mecanismo preventivo sea diseñado, acordado y probado.
