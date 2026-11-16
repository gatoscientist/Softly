# Entrega técnica de Katarina — revisión de capacidades y registro v2

**Misión:** KAT-RESET-002-REGISTRY-V2  
**Emite:** Katarina 3.1.0  
**Destinatario:** Softly  
**Mandato:** Dictamen de Dirección — Destrabe de RESET-CORE-2026-002  
**Estado:** entregado; requiere correcciones del registro y revisión independiente.

## Dictamen

**GO CON RESERVAS** para continuar la migración y sus correcciones. **NO-GO** para fusionar el PR #8 en el estado inspeccionado.

Informe técnico completo en la casa canónica de Katarina:

[gatoscientist/Katarina — revisión técnica de capacidades y migración v2](https://github.com/gatoscientist/Katarina/blob/main/shared/2026-11-16-KAT-RESET-002-revision-capacidades-registro-v2.md)

Blob SHA verificado: `571c208a97c685208be843178a20485580a90620`  
Commit de publicación: `ac5341bbc5d808629a058248515ba50a3fa2e1b9`.

## Hallazgos que requieren tratamiento

1. El schema no exige exactamente una aparición de cada una de las tres identidades; cardinalidad 3 más enum permite duplicados. Agregar `contains`/ `minContains`/ `maxContains` por ID y unicidad.
2. `main` conserva otro registro v2 bajo `schemas/identity-capability-registry-v2.json` y su schema. Designar una sola ruta canónica y archivar/retirar la pareja intermedia sin borrar historia.
3. El estado `approved-capability` contradice el campo obligatorio que declara ausencia de autorización. Separar aprobación documental de autorización operativa.
4. Reforzar unicidad de IDs y referencias cruzadas entre dominios, paquetes y perfiles.
5. Los paquetes fuente permanecen sin autoridad y sus competencias no se consideran demostradas por los perfiles declarativos.

## Propuesta de distribución

- **Katarina:** WPF/GUI e integración; PowerShell para automatización/diagnóstico; ingeniería de TLS y aislamiento, siempre bajo asignación técnica específica.
- **Audeline:** auditoría estática PowerShell/AST; análisis de integridad de leases; auditoría TLS/aislamiento; integración de evidencia y control de alcance. No delegar ni reactivar Aurora/Autumn.
- **Softly:** coordinación sistémica transversal, modelos de dependencias y flujos para continuidad y gobierno. Mantener el dominio como candidato hasta definir responsabilidades, observables y límites frente a ingeniería y auditoría.
- **Sin asignación:** música/audio de Thea y Melina; no hay mandato vigente dentro de las tres identidades.

Las propuestas no activan perfiles ni paquetes, no crean identidades y no transfieren proyectos TITAN.

## Salvaguardas y siguientes pasos

- La preservación de v1.0.0 fue verificada por igualdad exacta de blobs del registro y schema archivados.
- La rama del PR #8 estaba divergente (12 commits adelante / 14 detrás) y GitHub informó `mergeable: false` al corte documentado.
- No fusionar hasta corregir el schema, resolver la ruta canónica y recibir dictamen independiente favorable de Audeline.
- Las limitaciones de lectura de protección de `main` (HTTP 403), eliminación de ramas y verificación binaria de ZIP son localizadas; no detienen las tareas independientes.

Zoe permanece en asignación temporal hasta el dictamen final de Audeline y la confirmación expresa de gAto.
