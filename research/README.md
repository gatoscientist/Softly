# Investigación

## Estructura

- `sources/`: fichas de fuentes primarias y secundarias.
- `notes/`: notas de lectura y preguntas abiertas.
- `syntheses/`: síntesis temáticas construidas a partir de varias fuentes.
- `bibliography.md`: índice humano de referencias relevantes.

## Convenciones

ID de fuente: `SRC-YYYYMMDD-NNN`.  
ID de síntesis: `SYN-YYYYMMDD-NNN`.

Cada nota debe enlazar sus fuentes. Las citas textuales deben ser breves y claramente identificadas. Preferir paráfrasis fieles y registrar página/sección.

## Estado inicial

La primera revisión del panorama está en `sources/2026-11-agent-design-landscape.md`. Es una síntesis exploratoria, no una revisión sistemática ni una conclusión final.

## Notas de investigación

- [SOFT-RES-001 — Anatomía de un agente persistente](notes/2026-11-13-anatomia-agente-persistente.md): ficha exploratoria sobre contrato común, estructura específica e híbrida; hipótesis y preguntas abiertas, no normativa.
- [Conocí a Cytryna](notes/Conocí%20a%20Cytryna.md): registro histórico de la primera revisión de Cytryna, sus componentes y hallazgos estáticos. No equivale a una validación runtime.

## Material histórico incorporado

- [Material de investigación TITAN y antecedente SOFA Agent (13-11-2026)](notes/2026-11-13-material-titan-sofa-agent.md): ficha de ingesta de documentos aportados sobre TITAN, sus alcances y discrepancias, y registro del antecedente SOFA Agent pendiente de incorporar como artefacto original. Es dataset consultable bajo demanda, no lectura obligatoria.

## Síntesis

- [SYN-20261113-001 — Contaminación por transferencia creador–creado](syntheses/2026-11-13-linea-base-contaminacion-multirrama-titan.md): investigación centrada en cómo un agente creador transmite al agente creado instrucciones, supuestos, arquitectura, memoria, capacidades y patrones no justificados por el brief, y cómo esos rasgos pueden propagarse entre generaciones. La proliferación de ramas queda como línea base operacional secundaria.
- [SYN-20261113-002 — Propósito y diseño de investigación para la construcción de agentes blandos](syntheses/2026-11-13-proposito-y-diseno-investigacion-agentes-blandos.md): explica por qué se estudian las experiencias de TITAN y Cytryna y cómo se usarán para construir el molde de agentes, el flujo brief → definición → aprobación → despliegue, la política de no herencia por defecto y la observación de deriva identitaria durante la operación.
