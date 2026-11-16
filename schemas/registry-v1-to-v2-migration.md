# Migración documental del registro 1.0.0 al modelo v2

**Orden:** RESET-CORE-2026-002  
**Autorización:** Dictamen de Dirección — Destrabe de RESET-CORE-2026-002, 2026-11-16  
**Responsable de coordinación:** Softly  
**Estado:** Mapeo documental inicial; sujeto a verificación independiente de Audeline.

## Fuentes preservadas

- Origen histórico, sin modificación: `schemas/agent-taxonomy-registry.json`, `registry_version: 1.0.0`.
- Destino canónico: `schemas/identity-capability-registry-v2.json`, `registry_version: 2.0.0`.
- Contrato del destino: `schemas/identity-capability-registry-v2.schema.json`.

La migración no sobrescribe ni elimina el origen. La fuente 1.0.0 conserva su valor probatorio histórico; sus estados `active-standby` no se trasladan como autoridad operativa.

## Correspondencia de registros

| Entrada histórica 1.0.0 | Tratamiento en v2 | Observación |
|---|---|---|
| Tiffany / `agentdev-tiffany` | Paquete `candidate-unassigned` | Competencia PowerShell avanzado; sin autoridad ni asignación. |
| Tara / `agentsec-tara` | Paquete `candidate-unassigned` | Seguridad, AST, leases, TLS y aislamiento; sin autoridad ni asignación. |
| Thea / `agentmus-thea` | Paquete `candidate-unassigned` | Dominio musical; competencias aún no detalladas. |
| Tábata / `agentsci-tabata` | Paquete `candidate-unassigned` | Grafos, flujos de información, relojes y turnos; sin autoridad. |
| Katarina / `agentdev-katarina` | Identidad operativa `katarina` | Rol único de ingeniería y desarrollo; versión vigente registrada en v2. La entrada histórica 1.1.0 no se reescribe. |
| Melina / `agentmus-melina` | Paquete `candidate-unassigned` | Capacidades musicales preservadas como paquete sin autoridad. |
| Audeline / `audeline` | Identidad operativa `audeline` | Rol único de auditoría independiente. |
| Aurora / `aurora` | Paquete histórico | Sin identidad ni autoridad operativa vigente. |
| Autumn / `autumn` | Paquete histórico | Sin identidad ni autoridad operativa vigente. |

## Identidades normativas incorporadas por RESET

- Softly se registra como identidad operativa de coordinación general. Su ausencia en el registro 1.0.0 no limita su autoridad, que procede de RESET-CORE-2026-002.
- Katarina y Audeline quedan delimitadas por sus roles únicos en el modelo v2.
- Zoe no se migra como identidad: se representa únicamente como asignación temporal de supervisión, no operativa y sujeta a doble condición de cierre: dictamen final independiente de Audeline y confirmación expresa de gAto.

## Controles de migración

1. No activar, despachar ni conceder permisos a paquetes candidate-unassigned.
2. No inferir herencia de permisos, herramientas, certificaciones o competencias desde el registro 1.0.0.
3. Mantener el archivo 1.0.0 intacto y accesible como antecedente.
4. Audeline debe contrastar cada correspondencia con los paquetes fuente y verificar que el destino conserva exactamente tres identidades operativas.
5. No declarar validación automatizada del schema salvo ejecución comprobable de un validador compatible.
6. Registrar diferencias, datos no trasladados y limitaciones como parte del expediente de auditoría.

## Límite de esta entrega

Este documento materializa el mapeo documental autorizado y enlaza origen y destino. No acredita por sí solo que todas las competencias estén técnicamente verificadas, que los paquetes hayan sido integrados a una identidad ni que la auditoría independiente haya concluido.
