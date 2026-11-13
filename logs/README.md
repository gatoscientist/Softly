# Bitácora del laboratorio

La bitácora conserva eventos de trabajo, no conclusiones implícitas.

## Archivos

- `activity.jsonl`: acciones y eventos relevantes.
- `decisions.jsonl`: referencias a decisiones formales.
- `incidents.jsonl`: fallos metodológicos o de experimentación.
- `observations.jsonl`: referencias a observaciones.

## Reglas

- Una línea JSON por evento.
- Fecha ISO 8601 con zona horaria.
- ID único y tipo de evento.
- Enlaces a artefactos, no duplicados extensos.
- Nunca registrar secretos ni conversaciones completas.
- Corregir mediante evento nuevo; no reescribir historia sin dejar rastro.

La bitácora es trazabilidad documental. No es un sistema inmutable ni una garantía criptográfica.
