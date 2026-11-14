# Propuesta de esquemas para registros JSONL

**Estado:** CONGELADA por instrucción de gAto. No normativa; sin aprobación ni implementación. No revisar ni activar hasta después del tercer ciclo de auditoría.

## Diagnóstico

- `activity.jsonl`: una línea JSON válida, ID `EVT-20261113-001`; evento de bootstrap con timestamp ISO 8601 UTC, actor, resumen, artefactos, commit y estado.
- `decisions.jsonl`: una línea JSON válida, ID `ADR-0001`; decisión aceptada con fecha, contexto, decisión, rationale, condición de revisión y commit relacionado.
- Ambos archivos cumplen la regla documental de una línea JSON por evento, pero no hay esquema de eventos ni validador. La validez sintáctica no demuestra integridad semántica.

## Propuesta A — Activity Event

JSON Schema Draft 2020-12 recomendado, con estos campos:

| Campo | Tipo | Regla |
|---|---|---|
| `id` | string | `^EVT-[0-9]{8}-[0-9]{3,}$`; único en activity |
| `timestamp` | string | date-time RFC 3339 con zona explícita |
| `type` | string | catálogo versionado; permitir `other` con detalle |
| `actor` | string | identidad operativa no vacía |
| `summary` | string | descripción breve no vacía |
| `artifacts` | array[string] | rutas relativas existentes o referencias externas declaradas |
| `final_commit` | string/null | SHA Git completo si se conoce |
| `status` | string | estado de resultado controlado |
| `schema_version` | string | versión explícita del contrato |

## Propuesta B — Decision Record

| Campo | Tipo | Regla |
|---|---|---|
| `id` | string | `^ADR-[0-9]{4,}$`; único en decisions |
| `date` | string | fecha ISO 8601 |
| `status` | enum | proposed, accepted, rejected, superseded |
| `title` | string | no vacío |
| `context` | string | no vacío |
| `decision` | string | no vacío |
| `rationale` | array[string] | razones verificables |
| `review_condition` | string | condición de revisión |
| `related_commit` | string/null | SHA completo cuando exista |
| `supersedes` / `superseded_by` | string/null | relaciones ADR explícitas |
| `schema_version` | string | versión del contrato |

## Reglas comunes de validación

1. Exactamente un objeto JSON por línea; rechazar líneas vacías, JSON truncado y propiedades no permitidas.
2. Validar cada línea contra el schema correspondiente y reportar número de línea y ruta.
3. Comprobar unicidad de IDs dentro de cada namespace en todo el historial; nunca reciclar IDs.
4. Verificar timestamps/fechas, formato SHA y existencia de rutas/commits cuando sean verificables.
5. Las referencias no verificables se marcan como desconocidas; no se completan por inferencia.
6. Correcciones históricas mediante nuevo evento/versionado, no reescritura silenciosa.
7. Validación en modo informe primero; convertirla en bloqueo de CI solo tras aprobación, ejemplos de fixtures y período sin falsos positivos.

## Plan de adopción

1. Aprobar campos, catálogos y política de compatibilidad.
2. Crear schemas JSON independientes versionados y fixtures válidos/ inválidos.
3. Ejecutar validador en modo lectura sobre el historial.
4. Resolver errores documentando excepciones; no reescribir el pasado sin decisión.
5. Añadir CI y política de bloqueo después de validar el proceso.

**Decisión requerida:** aprobar, corregir o rechazar la propuesta. Hasta entonces, los JSONL y el esquema vigente permanecen intactos.
