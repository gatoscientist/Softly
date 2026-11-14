# ADR-0001 — Comenzar como laboratorio documental antes de implementar un runtime

- **ID:** ADR-0001
- **Fecha:** 2026-11-13
- **Estado:** Aceptada
- **Tipo:** Decisión de arquitectura y alcance
- **Procedencia:** reconstruida fielmente desde `logs/decisions.jsonl`; no se encontró un archivo ADR independiente en el árbol consultado.
- **Commit relacionado con el registro original:** `b01797cc0f9f2c644293b4b89a9d8594d387f308`

## Contexto

El repositorio Softly estaba vacío y el objetivo inicial era comprender cómo diseñar agentes sólidos mediante investigación y experimentación.

## Decisión

Mantener Softly como laboratorio documental y experimental, sin elegir todavía un framework ni construir un runtime.

## Rationale registrado

- Evitar comprometerse prematuramente con una plataforma.
- Separar evidencia de hipótesis.
- Comparar arquitecturas simples y multiagente mediante experimentos.
- Diseñar evaluación, memoria, seguridad y trazabilidad antes de implementar.

## Condición de revisión

Revisar esta decisión cuando existan preguntas de investigación priorizadas, fuentes suficientes y resultados comparativos.

## Consecuencias y alcance actual

Esta decisión establece el alcance del repositorio como laboratorio de investigación y documentación; no implica que exista un runtime implementado. Cualquier cambio futuro de alcance debe registrarse como una nueva ADR que reemplace o complemente esta decisión, preservando la historia.

## Nota de reconstrucción

El contenido de esta ADR se recuperó de la entrada `ADR-0001` de `logs/decisions.jsonl`. Los apartados de procedencia y alcance actual explicitan cómo se reconstruyó y cómo debe interpretarse; no se atribuyen al registro original detalles que este no contenía.
