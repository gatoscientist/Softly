# Propuesta de gobernanza y seguridad Git para Softly

**Estado:** CONGELADA por instrucción de gAto. No normativa; sin aprobación ni implementación. No revisar ni activar hasta después del tercer ciclo de auditoría.

## Objetivos

Proteger historia y trazabilidad; evitar cambios accidentales o silenciosos; permitir continuidad del mantenimiento sin bloquear al único responsable del repositorio.

## Política propuesta para `main`

1. Prohibir force-push y eliminación de `main`.
2. Exigir Pull Request para cambios ordinarios; mantener bypass administrativo explícito para recuperación urgente, siempre con registro posterior.
3. Exigir resolución de conversaciones de revisión antes de merge.
4. Exigir checks solo cuando existan workflows CI reales y estables. No configurar checks ficticios.
5. Requerir commits firmados como objetivo gradual; antes, verificar disponibilidad de clave y probar firma en una rama de prueba.
6. Exigir actualización de rama y resolución de conflictos antes de merge cuando corresponda.
7. Mantener permisos mínimos; separar lectura de escritura y limitar tokens.
8. Activar alertas/revisión de cambios de workflows, schemas, instrucciones normativas y archivos de seguridad.

## Modelo de revisión realista

- Para una persona mantenedora: PR + checklist y auto-revisión documentada; no exigir una aprobación humana imposible.
- Cuando exista segundo revisor: exigir una aprobación para cambios normativos, esquemas, seguridad o borrados.
- Cambios destructivos: respaldo verificable, diff revisado y registro de mantenimiento obligatorio.
- Cambios en contratos: ADR/propuesta aprobada, fixtures y migración reversible.

## Respaldo y recuperación

- Mantener al menos una copia independiente del repositorio, fuera de GitHub y con acceso separado.
- Definir frecuencia y retención; registrar fecha, commit, tamaño y SHA-256 del paquete de respaldo.
- Probar restauración en un directorio/repo temporal; comparar árbol y commit recuperados.
- No considerar el historial Git remoto como único respaldo.
- Documentar responsable, credenciales de recuperación y procedimiento sin incluir secretos en el repositorio.

## Implementación por etapas

**Etapa A — preparación:** verificar plan GitHub, permisos disponibles, estrategia de PR y capacidad de firma.  
**Etapa B — controles mínimos:** protección contra force-push/eliminación, PR obligatorio con bypass administrativo y resolución de conversaciones.  
**Etapa C — CI:** añadir checks reales para Markdown links, JSON/JSONL, namespaces y consistencia de índices; solo después hacerlos requeridos.  
**Etapa D — firma y recuperación:** activar verificación de firma tras piloto; realizar respaldo independiente y simulacro de restauración.  
**Etapa E — revisión:** auditar permisos y reglas cada trimestre o tras cambios relevantes.

## Matriz de aprobación

| Control | Recomendación | Requiere visto bueno |
|---|---|---|
| Bloquear force-push y borrado de main | Sí | Sí |
| PR obligatorio con bypass administrativo | Sí | Sí |
| Aprobación obligatoria de otra persona | Solo si hay segundo revisor | Sí |
| Checks requeridos | Después de implementar CI | Sí |
| Commits firmados obligatorios | Tras piloto técnico | Sí |
| Respaldo independiente y simulacro | Sí, prioridad alta | Sí |

**No ejecutar cambios en GitHub hasta aprobación expresa de gAto.**
