# Investigación

## Estructura

- `sources/`: fichas de fuentes primarias y secundarias ([índice de fuentes](sources/README.md)).
- `notes/`: notas de lectura y preguntas abiertas.
- `syntheses/`: síntesis temáticas construidas a partir de varias fuentes.
- [Bibliografía inicial](bibliography.md): índice humano de referencias relevantes.

## Convenciones

ID de fuente: `SRC-YYYYMMDD-NNN`.  
ID de síntesis: `SYN-YYYYMMDD-NNN`.

Cada nota debe enlazar sus fuentes. Las citas textuales deben ser breves y claramente identificadas. Preferir paráfrasis fieles y registrar página/sección.

## Estado inicial

La primera revisión del panorama está en `sources/2026-11-agent-design-landscape.md`. Es una síntesis exploratoria, no una revisión sistemática ni una conclusión final.

## Notas de investigación

- [Cruce documental: estructura de agentes Soft y molde de creación (14-11-2026)](notes/2026-11-14-cruce-estructura-agentes-soft.md): compara la investigación y guía del arenero del Laboratorio con el modelo y molde vigentes de Softly. Conserva procedencia y aportes; no modifica el estándar ni implica implementación.

- [SOFT-RES-001 — Anatomía de un agente persistente](notes/2026-11-13-anatomia-agente-persistente.md): ficha exploratoria sobre contrato común, estructura específica e híbrida; hipótesis y preguntas abiertas, no normativa.
- [Conocí a Cytryna](notes/Conocí%20a%20Cytryna.md): registro histórico de la primera revisión de Cytryna, sus componentes y hallazgos estáticos. No equivale a una validación runtime.

## Material histórico incorporado

- [Material de investigación TITAN y antecedente SOFA Agent (13-11-2026)](notes/2026-11-13-material-titan-sofa-agent.md): ficha de ingesta de documentos aportados sobre TITAN, sus alcances y discrepancias, y registro del antecedente SOFA Agent pendiente de incorporar como artefacto original. Es dataset consultable bajo demanda, no lectura obligatoria.

## Registro de identificadores

- [Propuesta de registro de namespaces y relaciones](identifier-registry-proposal.md): inventario descriptivo y propuesta no normativa; pendiente de revisión antes de modificar el esquema vigente.

## Síntesis

- [SYN-20261113-001 — De agentes que construyen agentes: Cytryna, TITAN y gobernanza multiagente](syntheses/2026-11-13-de-agentes-que-construyen-agentes.md): síntesis documental de roles, autoridad, límites técnicos y coordinación entre equipos constructores y sistemas creados.
- [SYN-20261113-003 — Contaminación por transferencia creador–creado](syntheses/2026-11-13-linea-base-contaminacion-multirrama-titan.md): investigación centrada en cómo un agente creador transmite al agente creado instrucciones, supuestos, arquitectura, memoria, capacidades y patrones no justificados por el brief, y cómo esos rasgos pueden propagarse entre generaciones. La proliferación de ramas queda como línea base operacional secundaria.
- [SYN-20261113-002 — Investigación para la creación de agentes blandos mediante un molde](syntheses/2026-11-13-proposito-y-diseno-investigacion-agentes-blandos.md): explica por qué se estudian las experiencias de TITAN y Cytryna y cómo se usarán para construir el molde de agentes, el flujo brief → definición → aprobación → despliegue, la política de no herencia por defecto y la observación de deriva identitaria durante la operación.
