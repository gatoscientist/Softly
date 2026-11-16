# Investigación

## Estructura

- `sources/`: fichas de fuentes primarias y secundarias ([índice de fuentes](sources/README.md)).
- `notes/`: notas de lectura y preguntas abiertas ([índice de notas](notes/README.md)).
- `syntheses/`: síntesis temáticas construidas a partir de varias fuentes ([índice de síntesis](syntheses/README.md)).
- [Bibliografía inicial](bibliography.md): índice humano de referencias relevantes.

## Convenciones

ID de fuente: `SRC-YYYYMMDD-NNN`.  
ID de síntesis: `SYN-YYYYMMDD-NNN`.

Cada nota debe enlazar sus fuentes. Las citas textuales deben ser breves y claramente identificadas. Preferir paráfrasis fieles y registrar página/sección.

## Estado inicial

La investigación conjunta Godot (14-11-2026) integra el análisis técnico de Auditoría y la lectura sistémica de Softly. Sus documentos de origen se preservan por separado; ver la [síntesis Parte II](syntheses/2026-11-14-investigacion-conjunta-godot-parte-ii.md) y la [entrega de Auditoría Parte I](../audsay/res/Investigacion_Auditoria_Godot_Parte_I.md).

La primera revisión del panorama está en `sources/2026-11-agent-design-landscape.md`. Es una síntesis exploratoria, no una revisión sistemática ni una conclusión final.

## Notas de investigación

- [Cierre de hilo y traspaso de continuidad — Investigación conjunta Godot](notes/2026-11-14-cierre-hilo-investigacion-godot.md): registra entregables, commits existentes, conclusiones que no deben perderse, solicitud de revisión a Softly y condiciones para abrir la fase experimental.

- [Cruce documental: estructura de agentes Soft y molde de creación (14-11-2026)](notes/2026-11-14-cruce-estructura-agentes-soft.md): compara la investigación y guía del arenero del Laboratorio con el modelo y molde vigentes de Softly. Conserva procedencia y aportes; no modifica el estándar ni implica implementación.
- [SOFT-RES-001 — Anatomía de un agente persistente](notes/2026-11-13-anatomia-agente-persistente.md): ficha exploratoria sobre contrato común, estructura específica e híbrida; hipótesis y preguntas abiertas, no normativa.
- [Conocí a Cytryna](notes/Conocí%20a%20Cytryna.md): registro histórico de la primera revisión de Cytryna, sus componentes y hallazgos estáticos. No equivale a una validación runtime.
- [Material de investigación TITAN y antecedente SOFA Agent (13-11-2026)](notes/2026-11-13-material-titan-sofa-agent.md): ficha de ingesta de documentos aportados sobre TITAN, sus alcances y discrepancias, y registro del antecedente SOFA Agent pendiente de incorporar como artefacto original. Es dataset consultable bajo demanda, no lectura obligatoria.

## Registro de identificadores

- [Propuesta de registro de namespaces y relaciones](identifier-registry-proposal.md): documento descriptivo congelado, no normativo; su revisión queda pospuesta hasta después del tercer ciclo de auditoría.

## Síntesis

- [SYN-20261114-001 — Investigación conjunta Godot: contraste e integración de Auditoría y Softly (Parte II)](syntheses/2026-11-14-investigacion-conjunta-godot-parte-ii.md): integra las investigaciones de ambos equipos sobre agentes de desarrollo y runtime en Godot; distingue evidencia documental, inferencias e hipótesis y registra discrepancias y pruebas pendientes.

- [SYN-20261113-001 — De agentes que construyen agentes: Cytryna, TITAN y gobernanza multiagente](syntheses/2026-11-13-de-agentes-que-construyen-agentes.md): síntesis documental de roles, autoridad, límites técnicos y coordinación entre equipos constructores y sistemas creados.
- [SYN-20261113-002 — Investigación para la creación de agentes blandos mediante un molde](syntheses/2026-11-13-proposito-y-diseno-investigacion-agentes-blandos.md): explica por qué se estudian las experiencias de TITAN y Cytryna y cómo se usarán para construir el molde de agentes, el flujo brief → definición → aprobación → despliegue, la política de no herencia por defecto y la observación de deriva identitaria durante la operación.
- [SYN-20261113-003 — Contaminación por transferencia creador–creado](syntheses/2026-11-13-linea-base-contaminacion-multirrama-titan.md): investigación centrada en cómo un agente creador transmite al agente creado instrucciones, supuestos, arquitectura, memoria, capacidades y patrones no justificados por el brief, y cómo esos rasgos pueden propagarse entre generaciones. La proliferación de ramas queda como línea base operacional secundaria.

- `coordination/`: prompts de investigación independiente sobre coordinación universal, auditoría de say/shared y rediseño del sistema, informes independientes y decisión de dirección para continuar con la Alternativa B. Ver [índice de coordinación](coordination/README.md).
