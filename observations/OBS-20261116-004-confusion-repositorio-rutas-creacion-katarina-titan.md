# OBS-20261116-004 — Confusión de repositorio y proliferación de rutas durante la creación de Katarina para TITAN

- **Fecha:** 2026-11-16
- **Agente / modelo / versión:** Softly; versión de ejecución no identificada en este registro
- **Configuración y entorno:** conversación con gAto; cambio solicitado de Modo Fábrica a Modo Investigación
- **Estado de reproducción:** Una vez; no se ha realizado una reproducción controlada
- **Tipo:** observación de comportamiento con incidencia asociada
- **Incidencia relacionada:** INC-20261116-003

## Objetivo y contexto

gAto pidió crear la instancia de Katarina y su equipo dentro del proyecto TITAN, cuyo repositorio correcto es `gatoscientist/TITAN`. La ruta expresada como `/TITAN` debía interpretarse en el contexto del repositorio del proyecto, no como una carpeta dentro de la casa de Softly (`gatoscientist/Softly`).

## Conducta observada y secuencia reconstruida

1. **Resolución inicial equivocada del destino.** Softly interpretó `/TITAN` como una carpeta del repositorio `gatoscientist/Softly`. Creó allí `TITAN/`, con la instancia Katarina y Los Mancos. La creación quedó registrada en commits del repositorio Softly, entre ellos `0e9b9898c235b7aec9773ba7bf4e239221e64ab2` y el cambio de taxonomía `2a3d40e4849610862783e3247d7c57177a08cff5` (antecedentes del error, conservados en la historia Git).
2. **Efecto de alcance.** Además de crear paquetes de agentes, Softly modificó el registro taxonómico de su propio repositorio para reflejar las instancias creadas allí. Esto reforzó documentalmente una ubicación que era incorrecta.
3. **Detección por gAto.** gAto corrigió explícitamente que Katarina debía estar en el proyecto TITAN, repositorio `gatoscientista/TITAN`, y que había sido creado un directorio indebido en Softly.
4. **Inspección del destino correcto.** Softly consultó la estructura existente de `gatoscientista/TITAN` y encontró el espacio `eL equipo del gAto`. Integró la dirección bajo `eL equipo del gAto/Direccion-TITAN/`, respetando el árbol ya existente.
5. **Migración y limpieza.** Se publicaron los paquetes de Katarina y Los Mancos en el repositorio correcto (42 archivos de paquete verificados en el árbol). Se eliminó la copia `TITAN/` de Softly mediante un commit nuevo, se retiraron cuatro entradas de taxonomía y se dejó un evento de corrección en `logs/activity.jsonl`.
6. **Verificación posterior.** La relectura confirmó el commit de TITAN `9a2bd4df5340a15c31f334241824d59f89516f1c`, 42 archivos de paquete bajo el destino correcto, cero rutas residuales `TITAN/` en el árbol actual de Softly y cero entradas de esos cuatro agentes en el registro taxonómico de Softly. El evento `EVT-20261116-013` quedó marcado `verified_readback`.
7. **Complejidad durante la reparación.** El proceso incluyó consultas a rutas equivocadas, intentos de lectura con referencias incorrectas y una construcción de árbol rechazada por un SHA inválido antes de completar el commit correcto. Esos intentos no deben confundirse con cambios persistidos; el resultado válido es el commit verificado indicado arriba.

## Resultado esperado vs. real

- **Esperado:** resolver primero el repositorio canónico y la ruta de destino; crear los paquetes allí; comprobar el resultado antes de cerrar.
- **Real:** Softly escribió primero en su propia casa, extendió el cambio al registro taxonómico local y solo después, tras la corrección de gAto, migró los artefactos y limpió la ubicación equivocada.

## Evidencia disponible

- Repositorio correcto: [gatoscientist/TITAN](https://github.com/gatoscientist/TITAN).
- Entrega: [commit 9a2bd4d en TITAN](https://github.com/gatoscientist/TITAN/commit/9a2bd4df5340a15c31f334241824d59f89516f1c).
- Corrección de Softly: [commit 37756a8](https://github.com/gatoscientist/Softly/commit/37756a8e449e9d3524a8f56acc6eeaed2aba332b).
- Verificación del registro de actividad: [commit b174ed1](https://github.com/gatoscientist/Softly/commit/b174ed1131fbe79b1e3c516e74928705f5b0e8f0).
- Evento de actividad: `EVT-20261116-013`.
- Registro taxonómico: `schemas/agent-taxonomy-registry.json`, releído después de la limpieza.
- Árboles GitHub consultados después de la reparación: `gatoscientist/TITAN` y `gatoscientist/Softly`.

La evidencia confirma presencia y limpieza de rutas, pero no constituye una auditoría semántica exhaustiva de cada referencia interna de los 42 archivos.

## Hipótesis causales (no confirmadas)

1. **Ambigüedad de resolución de ruta:** Softly trató una ruta de proyecto (`/TITAN`) como ruta relativa dentro del repositorio activo, sin confirmar que el usuario estaba nombrando otro repositorio.
2. **Ausencia de preflight obligatorio:** antes de escribir, no fijó y repitió una tupla inequívoca `owner/repo + branch + path` ni comprobó el destino con gAto.
3. **Sesgo de continuidad del repositorio activo:** la disponibilidad inmediata de herramientas sobre `gatoscientist/Softly` pudo favorecer que Softly continuara escribiendo allí en vez de cambiar de repositorio.
4. **Acoplamiento entre creación y registro global:** Softly actualizó su registro taxonómico local como parte de una creación cuyo destino todavía no estaba confirmado.
5. **Complejidad de orquestación sin plan de cambios:** se pasó a operaciones de blobs/árboles y a una migración de múltiples archivos sin un manifiesto de origen-destino validado previamente.

Estas hipótesis describen posibles factores de proceso; no son causas raíz demostradas ni atribuyen intención.

## Impacto provisional

- Escritura de una estructura de proyecto en el repositorio equivocado.
- Cambios transitorios innecesarios en el registro taxonómico de Softly.
- Trabajo adicional de migración, limpieza y verificación.
- Aumento de complejidad y riesgo de divergencia entre copias.
- Pérdida de claridad sobre la diferencia entre casa del agente, repositorio del proyecto y directorio interno.
- Carga de revisión adicional para gAto.

No se observó pérdida de la historia Git: la corrección se hizo con commits nuevos y se conservó el historial previo.

## Principios preliminares para simplificar el trabajo con directorios

Estos son controles propuestos para estudiar, no cambios normativos ya aprobados:

1. **Primero repositorio, después carpeta.** Toda escritura debe comenzar identificando `owner/repo`; una ruta como `/TITAN` no basta por sí sola para elegir repositorio.
2. **Usar una ficha de destino única:** `owner/repo`, rama, ruta raíz y operación solicitada.
3. **Separar tres conceptos:** casa canónica del agente (por ejemplo, `gatoscientista/Katarina`), repositorio del proyecto (por ejemplo, `gatoscientista/TITAN`) y carpeta del agente dentro de ese proyecto.
4. **Preflight antes de escribir:** leer README/índice y árbol de destino; detectar si ya existe; confirmar el destino con gAto cuando haya más de una interpretación plausible.
5. **Manifiesto antes de migrar:** enumerar cada archivo de origen, destino y acción; no copiar ni borrar hasta validar el manifiesto.
6. **Una sola fuente de verdad:** no mantener una copia de proyecto en la casa de Softly por conveniencia.
7. **Verificación de ida y vuelta:** comprobar los archivos y referencias internas del destino, y comprobar que el origen equivocado quedó limpio antes de informar cierre.

## Siguiente prueba discriminante

Realizar una prueba controlada con dos repositorios y una ruta homónima. Antes de cualquier escritura, pedir a Softly que identifique repositorio, rama y carpeta, y comprobar si bloquea la ejecución cuando la instrucción no distingue entre repositorio y directorio. Registrar si el preflight evita la confusión.

## Límite de esta observación

Este registro reconstruye la secuencia observable disponible en la conversación y en los commits consultados. No es una transcripción literal completa ni una demostración de causa raíz. La investigación de simplificación de directorios queda abierta y separada de esta captura.
