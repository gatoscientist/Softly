# Migración del registro de identidades y capacidades v1.0.0 → v2.0.0

**Mandato:** Dictamen de Dirección — Destrabe de RESET-CORE-2026-002, 2026-11-16.  
**Responsable:** Softly.  
**Rama:** `migration/registry-v2-reset-core-002`.  
**Estado:** migración documental preparada; revisión independiente de Audeline pendiente.

## 1. Decisión aplicada

Se adopta el modelo v2 como modelo canónico de diseño, sujeto a verificación independiente de Audeline. El registro operativo queda limitado a tres identidades: Softly, Katarina y Audeline. Zoe se conserva exclusivamente como asignación temporal de supervisión y no como identidad del registro.

## 2. Preservación de la versión histórica

La versión 1.0.0 se conserva byte por byte en Git bajo:
- `schemas/archive/agent-taxonomy-registry-1.0.0.json`
- `schemas/archive/agent-taxonomy.schema-1.0.0.json`

El blob SHA del registro fuente antes de la migración fue `ceca667cfb912a0f7c43b32ee0eead86030b4b5f`. No se reescribe el historial. La ruta canónica `schemas/agent-taxonomy-registry.json` pasa a contener v2.0.0.

## 3. Estructura v2

- `identities[]`: exactamente tres identidades operativas, con casa, versión canónica, mandato institucional y dominios.
- `domains[]`: dominios profesionales y de gobierno; distingue dominios establecidos, candidatos e históricos. GUI se representa como disciplina subordinada a UX.
- `capability_profiles[]`: capacidades con procedencia, paquete fuente, destino propuesto y estado de autorización. No crean identidades.
- `packages[]`: repositorio, ruta, versión, madurez documental y autoridad. Los paquetes candidate-unassigned e históricos carecen de autoridad operativa.
- `temporary_assignments[]`: asignaciones temporales con condición de inicio y término verificable.
- `migration`: trazabilidad del origen y estado de revisión independiente.

## 4. Tratamiento de capacidades heredadas

La migración no convierte los paquetes fuente en identidades. Las capacidades reutilizables se proponen, sin activación:
- Tiffany: WPF/GUI, integración y PowerShell → Katarina, pendiente de validación contractual.
- Tara: auditoría AST e integridad de leases → Audeline; TLS/aislamiento queda como capacidad técnica compartida candidata entre ingeniería y auditoría, sin autorización automática.
- Tabata: grafos, flujos, relojes y turnos → Softly/Audeline o Softly/Katarina según capacidad, pendiente de validar el contrato sistémico.
- Thea y Melina: música/audio permanecen candidate-unassigned, sin destino operativo asignado.
- Aurora y Autumn: integración y control de alcance auditor quedan como fuentes históricas candidatas para Audeline; no hay delegación ni autoridad propia.

Todas las propuestas usan `authorization: none-until-explicit-contract-mapping-and-independent-review` y `inheritance: none`.

## 5. Coordinación sistémica

Se registra como dominio candidato `systems-coordination`, no como cuarta identidad ni dimensión adicional ya aprobada. La pregunta de Katarina se conserva: si el contrato de orquestación de Softly cubre coordinación sistémica transversal, la capacidad puede documentarse dentro de Softly; si no, se especificará como capacidad transversal. No se concede competencia hasta contrastar el contrato y la evidencia.

## 6. Versiones canónicas observadas

- Softly: 1.0.0, según SOFTLY.md.
- Katarina: 3.1.0, según core/CONTRACT.md y core/AGENT.md en su casa canónica.
- Audeline: 1.0.0, según README.md y Audeline/AGENT.md en su casa canónica.

La discrepancia histórica de Katarina 1.1.0 queda corregida en el registro v2; no se utiliza la versión antigua del registro como fuente de versión canónica.

## 7. Controles pendientes

1. Audeline debe verificar independientemente el schema, los datos, la exactitud de procedencia, la preservación 1.0.0, el límite de tres identidades y la semántica no operativa de paquetes/capacidades.
2. Katarina debe contrastar que las capacidades propuestas sean técnicamente compatibles con su contrato y señalar exclusiones o conflictos.
3. No se autoriza activar, invocar ni delegar en paquetes históricos.
4. La migración se integra a main solo después del dictamen independiente de Audeline. La autoridad operativa sigue limitada por los contratos vigentes.

## 8. No incluido en esta migración

Runtime y KAT-006 permanecen cerrados administrativamente. No se incluyen ramas externas, PR ajenos, eliminación de ramas ni verificación binaria de ZIP. Esos frentes continúan por vías independientes conforme al mandato de Dirección y las limitaciones técnicas localizadas.
