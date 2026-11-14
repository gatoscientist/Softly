# Mantenimiento de la casita

Este directorio conserva la historia de cómo se ordena y mantiene Softly. El objetivo no es solo dejar el repositorio más limpio: también aprender por qué se desordena y evitar repetir las mismas causas.

## Regla de cada pasada

Cada sesión de mantenimiento debe registrar:

1. **Estado inicial:** qué estaba desordenado, incompleto, duplicado o difícil de encontrar.
2. **Causa observada:** qué produjo el problema (crecimiento sin índices, rutas inconsistentes, falta de clasificación, referencias antiguas, etc.). Separar evidencia de hipótesis.
3. **Acciones:** qué se creó, corrigió, movió o eliminó, con rutas y commits.
4. **Criterio:** por qué se eligió esa acción y qué alternativas se descartaron.
5. **Resultado verificable:** qué se comprobó en el árbol Git, enlaces, hashes y pruebas.
6. **Pendientes:** qué no se pudo resolver y por qué.
7. **Aprendizaje preventivo:** qué regla o hábito ayudaría a evitar que el problema reaparezca.

## Regla de conservación

- Inventariar antes de actuar.
- Preferir índices y enlaces antes que mover archivos.
- No borrar por nombre, tamaño o similitud temática.
- Exigir respaldo verificable antes de eliminar.
- Preservar snapshots históricos y procedencia.
- No alterar contratos ni agentes sin autorización explícita.
- No declarar inspeccionado un PDF/ZIP si solo se conoce su nombre, tamaño o hash.

## Registros

- [Tercer ciclo de auditoría — unicidad de IDs y grafo documental (2026-11-14)](2026-11-14-third-audit-cycle.md): revisión de los 83 Markdown, unicidad global de declaraciones, dependencias semánticas y cierre de índices sin referencias entrantes.
- [Auditoría de integridad Softly — etapas 1 a 5 (2026-11-14)](2026-11-14-integrity-audit-stages-1-5.md): inventario, cobertura Markdown, limitaciones PDF, JSONL, namespaces y propuestas de seguridad Git.
- [Seguimiento de auditorías y mantenimiento — 2026-11-14](2026-11-14-audit-follow-up.md): registro técnico detallado de las pasadas documentales, inventarios, verificaciones y pendientes.
- [Bitácora de orden de la casita](housekeeping-log.md): causas, acciones y aprendizajes acumulados entre pasadas.
- [Matriz de procedencia y respaldo — línea base 2026-11-14](matriz-procedencia-respaldo-2026-11-14.md): inventario preliminar del arenero y la cAjita, hashes conocidos, estado de inspección, respaldos candidatos y pendientes de verificación. Estado abierto; no autoriza eliminaciones.

## Convención

Mantener un registro detallado por pasada cuando el trabajo sea amplio. La bitácora de orden resume las causas y aprendizajes para poder detectar patrones entre sesiones. No sobrescribir registros anteriores: agregar una nueva entrada.
