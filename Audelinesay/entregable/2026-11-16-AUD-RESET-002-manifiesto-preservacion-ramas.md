# AUD-RESET-002 — manifiesto de preservación de ramas

**Emite:** Audeline  
**Fecha:** 2026-11-16  
**Destino:** Softly / gAto  
**Informe canónico:** [Informe 23 de Audeline](https://github.com/gatoscientist/Audeline/blob/main/reports/RESET-CORE-2026-002/23-AUDELINE-MANIFIESTO-PRESERVACION-RAMAS-2026-11-16.md)  
**Commit del informe:** cbcdaa4e3a00110631e178f11f541e7d40b5b00d

## Resultado

Audeline recuperó el HEAD SHA exacto de las siete ramas adicionales en el corte inicial y recalculó su divergencia contra main. Las siete referencias y sus archivos exclusivos están registrados en el informe 23.

- Softly/F-03: rama histórica con código y pruebas Runtime; no integrar.
- Softly/recovery: tres README de canal supersedidos por versiones actuales en main; no requiere merge.
- Katarina/KAT-006: PR #1 cerrado sin merge; no integrar.
- Auditoria: dos propuestas históricas y una recovery con contenido Aurora/Autumn incompatible; no integrar.
- Laboratorio-de-agentes: propuesta normativa histórica; no adoptar automáticamente.

La octava rama es `migration/registry-v2-reset-core-002` (HEAD `9ed9fabcd44aa33d3e5f25b54c88751ef42c3ed2`, ahead 13 / behind 31), activa bajo NO-GO hasta corregir el PR #8. El total vigente es ocho ramas adicionales: Softly 3, Katarina 1, Auditoria 3 y Laboratorio-de-agentes 1.

No se fusionó ni eliminó ninguna rama. El manifiesto conserva HEAD SHA y base SHA para que el retiro posterior pueda hacerse con verificación de lease y sin borrar commits nuevos.

## Límites

La conexión GitHub usada permite leer ramas y commits, pero no expone operación delete-ref. Por tanto, no se afirma que las ramas hayan sido retiradas ni que la política main única esté físicamente satisfecha.

La verificación binaria de ZIP sigue siendo una tarea independiente: los diez metadatos coinciden, pero no hay descarga binaria en esta conexión.

## Siguiente acción

Softly debe mantener las ramas clasificadas como históricas/supersedidas y, cuando exista conexión autorizada con delete-ref, retirar solo tras comparar cada HEAD actual con el SHA del informe 23. No requiere Runtime ni aprobación adicional para reexaminar los SHA; cualquier cambio inesperado de HEAD exige preservar y reclasificar.
