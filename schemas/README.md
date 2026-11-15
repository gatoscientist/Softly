# Esquemas de datos

Contratos estructurales para validar registros del laboratorio. La presencia de un esquema no implica que exista un validador automático en ejecución.

- [Research Record JSON Schema](research-record.schema.json): estructura de fichas de fuentes, identificador `SRC-YYYYMMDD-NNN`, procedencia, estado y limitaciones.
- [Propuesta de esquemas para JSONL](jsonl-event-schema-proposal.md): diseño no normativo para `activity.jsonl` y `decisions.jsonl`; pendiente de aprobación. No modifica los registros ni el esquema vigente.

- [Handoff](handoff.schema.json): contrato de transferencia estructurada entre agentes.
- [Taxonomía profesional](agent-taxonomy.schema.json): validación de identidad profesional, dominio y derivaciones.
- [Registro inicial de taxonomías](agent-taxonomy-registry.json): catálogo de agentes y disponibilidad declarada.
- [Estado de modo operativo](operating-mode-state.example.json): ejemplo declarativo del conmutador Laboratorio/Fábrica; no es un ejecutor.
