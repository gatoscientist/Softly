# Especificación inicial del modelo de datos de conocimiento

- **Versión:** 0.1
- **Estado:** propuesta de diseño; pendiente de revisión y validación
- **Fecha:** 2026-11-13
- **Etapa:** 2 — identificadores y campos mínimos
- **Relacionado con:** docs/architecture/knowledge-domain-model.md; docs/architecture/knowledge-architecture.md; SYN-20261113-001, secciones 16 y 17
- **Alcance:** define una estructura lógica mínima y neutral respecto de la tecnología. No selecciona base de datos, formato físico, API ni motor de recuperación.

## 1. Objetivos de diseño

El modelo debe:

1. identificar cada elemento de forma estable, sin depender de nombres o atributos que puedan cambiar;
2. distinguir la identidad de un elemento de cada versión de su contenido;
3. conservar procedencia, contexto, tiempo y permisos;
4. permitir que las afirmaciones se rastreen hasta evidencia original;
5. representar dominios diferentes con un conjunto pequeño de estructuras comunes;
6. permitir evolución del esquema sin invalidar silenciosamente registros anteriores.

Se prioriza un núcleo pequeño. Los campos opcionales o especializados se incorporarán cuando un caso de uso real los justifique.

## 2. Convenciones de identificadores

### 2.1 Identificador primario

Propuesta: usar identificadores opacos, globalmente únicos y no semánticos, con un prefijo corto por familia:

- ENT — entidad
- CON — concepto
- SRC — fuente o registro
- CLM — afirmación
- SYN — síntesis
- ACT — actividad
- CTX — contexto

Forma legible ilustrativa: ENT-<UUID>, CLM-<UUID>, etc. El UUID debe generarse con un mecanismo estándar de alta unicidad; UUIDv7 es una opción candidata por su orden temporal aproximado, pero su adopción definitiva queda pendiente de evaluar compatibilidad y requisitos de privacidad.

El prefijo ayuda a humanos y herramientas a reconocer el tipo, pero no codifica nombre, universo, proyecto, propietario ni estado.

### 2.2 Reglas

- El ID se asigna una sola vez y nunca cambia.
- Un ID eliminado o retirado no se reutiliza.
- El nombre, título, ruta, rol y demás atributos no son identificadores.
- Los IDs externos se conservan como referencias externas, no sustituyen el ID interno.
- El universo y los permisos son atributos separados del ID.
- Una referencia entre registros usa el ID interno exacto.
- Si se fusionan duplicados, se conserva un registro canónico y los IDs anteriores quedan como alias o redirecciones auditables; nunca se reciclan.

### 2.3 Identidad y versión

Cada elemento tiene:
- **id:** identidad estable del elemento lógico.
- **version_id:** identidad única de una revisión concreta.
- **version:** número secuencial legible dentro de ese elemento.

Una nueva revisión conserva el ID lógico y genera un version_id nuevo. No se modifica una versión histórica para simular que siempre tuvo el contenido corregido. Los registros de evidencia original deben preservar además la referencia o huella del contenido capturado.

## 3. Sobre común de todos los registros

Todas las familias comparten un sobre mínimo:

| Campo | Obligatorio | Significado |
|---|---:|---|
| id | Sí | Identidad estable y única |
| record_type | Sí | Familia: entity, concept, source, claim, synthesis, activity o context |
| version_id | Sí | Identificador único de esta revisión |
| version | Sí | Número de revisión |
| schema_version | Sí | Versión del contrato de datos usado |
| created_at | Sí | Momento de creación del registro, en UTC |
| updated_at | Sí | Momento de la última modificación de esta revisión, en UTC |
| status | Sí | Estado del ciclo de vida del registro |
| universe_id | Sí | Universo propietario o de origen principal |
| context_ids | No | Contextos adicionales aplicables |
| access_policy | Sí | Clasificación y regla de acceso |
| provenance | Sí | Cómo y desde dónde se incorporó el registro |
| tags | No | Etiquetas auxiliares, no autoritativas |

Los timestamps se expresan en ISO 8601 con zona horaria explícita; se recomienda UTC para persistencia. Los tiempos del hecho observado —por ejemplo occurred_at o valid_time— son distintos de created_at y se agregan en las familias que los necesitan.

### 3.1 Estados comunes

Estados iniciales propuestos: draft, active, deprecated, superseded y retracted. No todos los tipos tienen que usar todos los estados. Un registro retracted no desaparece: permanece auditable y debe explicar la razón y la autoridad de la retirada.

### 3.2 Procedencia común

La procedencia debe permitir contestar:
- ¿quién o qué incorporó este registro?;
- ¿de qué fuente, actividad o registro previo proviene?;
- ¿cuándo se obtuvo?;
- ¿fue capturado directamente, importado o derivado?;
- ¿qué transformación relevante se aplicó?

Campos mínimos de provenance:
- origin_type: direct_observation, imported_source, user_input, system_event o derived;
- origin_ref: referencia a la fuente, actividad o evento, cuando exista;
- recorded_by: actor o proceso que realizó la incorporación;
- captured_at: momento de captura;
- method: método o transformación breve, cuando corresponda.

La procedencia no prueba por sí sola que el contenido sea verdadero.

### 3.3 Acceso

access_policy debe incluir, como mínimo:
- classification: public, internal, confidential o restricted;
- allowed_principals o una referencia a una política externa de autorización;
- purpose_limit, cuando el uso esté limitado a una finalidad.

La autorización efectiva debe imponerse fuera del modelo de datos. Guardar una etiqueta de permiso no constituye un control de seguridad por sí solo.

## 4. Campos mínimos por familia

### 4.1 Entity

Representa una instancia identificable.

| Campo | Obligatorio | Descripción |
|---|---:|---|
| name | Sí | Nombre principal legible |
| entity_type | Sí | Tipo de entidad dentro de un vocabulario controlado y extensible |
| description | No | Descripción breve |
| external_ids | No | Identificadores en sistemas externos |
| aliases | No | Otros nombres conocidos |

Las relaciones con otras entidades y conceptos se representan como relaciones explícitas, no como texto libre dentro de description.

### 4.2 Concept

Representa una idea, categoría o definición.

| Campo | Obligatorio | Descripción |
|---|---:|---|
| name | Sí | Término preferido |
| definition | Sí | Definición delimitada |
| concept_type | Sí | Tipo, por ejemplo domain_term, property, method o category |
| synonyms | No | Términos equivalentes o cercanos, distinguidos cuando no sean equivalentes exactos |
| parent_concept_ids | No | Conceptos más generales |

Las definiciones pueden evolucionar por versiones. No se debe asumir que dos términos son sinónimos solo porque se parecen.

### 4.3 Source / Record

Representa un artefacto original o un registro capturado.

| Campo | Obligatorio | Descripción |
|---|---:|---|
| source_type | Sí | document, webpage, repository, message, event, trace, measurement, image, dataset u otro tipo controlado |
| title | Sí | Título o descripción legible |
| locator | Condicional | URI, ruta o referencia recuperable cuando exista |
| content_hash | Condicional | Huella del contenido capturado cuando sea posible calcularla |
| creator | No | Autor o emisor declarado, con su nivel de verificación |
| published_at | No | Fecha de publicación del original |
| occurred_at | No | Momento del evento descrito |
| captured_at | Sí | Momento en que Softly obtuvo el registro |
| media_type | No | Tipo de contenido o formato |
| integrity_status | Sí | Estado conocido de integridad y disponibilidad |

No todos los registros tendrán URL ni contenido descargable. En esos casos, locator puede omitirse y debe conservarse una descripción suficiente para localizar el origen legítimo. No almacenar secretos ni conversaciones privadas completas por defecto.

### 4.4 Claim

Representa una proposición delimitada.

| Campo | Obligatorio | Descripción |
|---|---:|---|
| statement | Sí | Contenido de la afirmación, expresado de forma atómica cuando sea posible |
| epistemic_type | Sí | FACT, OBSERVATION, INFERENCE, HYPOTHESIS, RESULT, DECISION o RECOMMENDATION |
| subject_refs | Sí | Una o más referencias a entidades o conceptos sobre los que trata |
| evidence_refs | No | Fuentes/registros que la respaldan, contradicen o matizan |
| assessment_status | Sí | Estado de evaluación: unassessed, supported, contested, inconclusive o rejected |
| confidence | No | Estimación explícita y calibrada, nunca inventada por defecto |
| valid_from / valid_until | No | Periodo en que la afirmación aplica, si puede determinarse |
| scope_note | No | Condiciones y límites de validez |

La relación con cada evidencia debe indicar su papel: supports, contradicts, qualifies o contextualizes. Una afirmación puede tener evidencia mixta. confidence no reemplaza assessment_status ni una explicación de la evidencia.

### 4.5 Synthesis

Representa una vista condensada y trazable.

| Campo | Obligatorio | Descripción |
|---|---:|---|
| title | Sí | Título legible |
| purpose | Sí | Pregunta, tarea o finalidad que organiza la síntesis |
| body | Sí | Contenido condensado |
| claim_refs | Sí | Afirmaciones incluidas o utilizadas |
| coverage | Sí | Alcance, periodo y universo cubiertos |
| limitations | Sí | Vacíos, incertidumbres y exclusiones relevantes |
| freshness_status | Sí | current, review_needed o stale |
| reviewed_at | No | Momento de la última revisión de vigencia |

Una síntesis nueva genera una nueva versión. Debe ser posible identificar qué afirmaciones sustentaban cada versión histórica.

### 4.6 Activity

Representa una investigación, experimento, evaluación, auditoría o tarea delimitada.

| Campo | Obligatorio | Descripción |
|---|---:|---|
| activity_type | Sí | Tipo de actividad |
| title | Sí | Nombre legible |
| objective | Sí | Objetivo verificable |
| status | Sí | proposed, planned, running, completed, failed o cancelled |
| input_refs | No | Fuentes, entidades o síntesis utilizadas |
| output_refs | No | Registros, afirmaciones o síntesis producidas |
| started_at / ended_at | No | Tiempos reales de ejecución, cuando existan |
| method | No | Método o protocolo |
| outcome_summary | No | Resultado breve, sin sustituir registros detallados |

Una actividad propuesta no puede marcarse como completed sin evidencia de ejecución.

### 4.7 Context

Representa el ámbito que delimita interpretación, validez o acceso.

| Campo | Obligatorio | Descripción |
|---|---:|---|
| name | Sí | Nombre del contexto |
| context_type | Sí | universe, project, environment, time_period, experiment_condition u otro tipo definido |
| description | Sí | Qué delimita |
| parent_context_ids | No | Contextos contenedores |
| valid_from / valid_until | No | Periodo de vigencia, cuando corresponda |

Los universos Softly, DEVAGENTS y TITAN deben representarse como contextos separados. Una relación de acceso entre ellos debe ser explícita y autorizada; no se deduce de que dos registros compartan tema.

## 5. Ejemplos ilustrativos

Los valores siguientes son ficticios y muestran la forma lógica, no una serialización definitiva.

### 5.1 Entidad

    id: ENT-<UUID>
    record_type: entity
    name: Primus
    entity_type: software_agent
    universe_id: CTX-TITAN
    status: active
    version: 1

### 5.2 Fuente

    id: SRC-<UUID>
    record_type: source
    source_type: repository
    title: Contrato de Primus
    locator: referencia al archivo original
    captured_at: 2026-11-13T00:00:00Z
    integrity_status: captured
    universe_id: CTX-TITAN
    status: active
    version: 1

### 5.3 Afirmación

    id: CLM-<UUID>
    record_type: claim
    statement: Primus tiene un contrato operativo separado del Dev Team.
    epistemic_type: FACT
    subject_refs: [ENT-<UUID>]
    evidence_refs:
      - ref: SRC-<UUID>
        relation: supports
    assessment_status: supported
    universe_id: CTX-TITAN
    status: active
    version: 1

### 5.4 Actividad

    id: ACT-<UUID>
    record_type: activity
    activity_type: research
    title: Análisis de contratos de TITAN
    objective: Identificar límites entre desarrollo y runtime.
    status: completed
    output_refs: [CLM-<UUID>]
    universe_id: SOFTLY
    status: active
    version: 1

Los IDs de ejemplo son marcadores, no identificadores asignados a objetos reales. El ejemplo de actividad ilustra que el universo que ejecuta una investigación puede diferir del universo sobre el que trata la evidencia.

## 6. Relaciones y cardinalidades iniciales

- Una afirmación debe referirse a una o más entidades o conceptos.
- Una afirmación puede tener cero o más referencias de evidencia; si carece de evidencia, su estado debe reflejar que no está evaluada o que su soporte es insuficiente.
- Una evidencia puede respaldar o contradecir múltiples afirmaciones.
- Una síntesis debe referenciar una o más afirmaciones.
- Una actividad puede consumir y producir múltiples registros.
- Una entidad puede participar en múltiples actividades y relacionarse con múltiples conceptos.
- Un contexto puede contener múltiples registros; un registro puede estar asociado a más de un contexto, sujeto a permisos.

Las relaciones se almacenan conceptualmente como referencias tipadas. La representación física queda pendiente.

## 7. Reglas de calidad y evolución

1. No usar nombres, rutas ni títulos como claves primarias.
2. No sobrescribir versiones históricas.
3. No elevar automáticamente una hipótesis a hecho por acumulación de menciones.
4. No tratar ausencia de evidencia como evidencia de ausencia.
5. No asumir que un origen declarado está verificado.
6. No mezclar tiempo de captura, tiempo del evento y periodo de validez.
7. No propagar acceso entre universos por similitud temática.
8. No incluir secretos, credenciales ni datos personales innecesarios.
9. Marcar referencias rotas, evidencia retirada y síntesis que requieran revisión.
10. Registrar cambios de esquema mediante schema_version y un proceso de migración explícito.

## 8. Decisiones pendientes

- Confirmar UUIDv7 u otro generador de IDs.
- Definir vocabularios controlados y mecanismo de extensibilidad.
- Precisar cardinalidades y tipos de relación.
- Definir si el version_id será UUID independiente o derivado del historial.
- Especificar el modelo formal de políticas de acceso y retención.
- Elegir serialización y almacenamiento solo después de validar los casos de uso.

## 9. Criterios de aceptación de esta etapa

La propuesta será aceptable cuando:
1. cada familia pueda representarse con los campos mínimos definidos;
2. los IDs permanezcan estables ante cambios de nombre y clasificación;
3. una versión histórica pueda reconstruirse sin sobrescribirla;
4. una afirmación pueda rastrearse hasta su evidencia;
5. una síntesis pueda reconstruirse desde las afirmaciones que utilizó;
6. los universos y permisos se mantengan separados;
7. ejemplos de al menos tres dominios distintos puedan expresarse sin alterar el núcleo.

## 10. Estado y siguiente paso

Esta especificación es una propuesta lógica v0.1. No demuestra que exista un sistema de persistencia, autorización, versionado o recuperación implementado.

El siguiente trabajo será revisar el modelo con casos representativos de Softly, TITAN y un dominio no relacionado con agentes; resolver las decisiones pendientes y después especificar relaciones, procedencia y versionado con mayor precisión.
