# Evaluación de agentes

## Objetivo

Medir si un agente cumple su tarea de manera fiable, segura, eficiente y consistente. No basta con calificar si la respuesta “suena bien”.

## Dimensiones

- Correctitud y completitud de tarea.
- Cumplimiento de instrucciones y límites.
- Selección y uso correcto de herramientas.
- Calidad de delegación/handoffs.
- Robustez ante entradas ambiguas y adversariales.
- Seguridad, privacidad y permisos.
- Recuperación ante errores e interrupciones.
- Calidad de memoria: utilidad, precisión, procedencia y contaminación.
- Coste, latencia, tokens y número de pasos.
- Calidad de comunicación y calibración de incertidumbre.

## Tipos de evaluación

1. Unit tests de herramientas y políticas.
2. Tests de comportamiento por escenario.
3. Evaluación de trazas completas.
4. Red-team/adversarial.
5. Comparación A/B de modelos, prompts o harnesses.
6. Evaluación humana ciega cuando corresponda.
7. Regresión continua en cada cambio relevante.

## Buenas prácticas

- Construir datasets representativos y versionados.
- Incluir ejemplos positivos, negativos, límite y adversariales.
- Definir rúbricas antes de observar resultados.
- Combinar métricas automáticas con revisión humana.
- Calibrar evaluadores automáticos contra juicio humano.
- Registrar fallos y añadirlos al conjunto de regresión.
- Evitar métricas genéricas como único criterio.
- Comparar contra baseline y controlar variables.

## ID

`EVAL-YYYYMMDD-NNN` para planes; `RUN-YYYYMMDD-NNN` para ejecuciones.

## Índices de trabajo

- [Datasets](datasets/README.md): conjuntos de evaluación versionados.
- [Planes](plans/README.md): criterios y protocolos definidos antes de ejecutar.
- [Ejecuciones](runs/README.md): reportes y resultados de evaluaciones realizadas.

Estos tres subdirectorios contienen actualmente solo sus README de preparación; todavía no hay datasets, planes ni ejecuciones registrados.
