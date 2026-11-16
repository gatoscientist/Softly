# Informe de reanudación — corrección inicial del registro v2

**Fecha:** 2026-11-16  
**Rama:** `fix/registry-v2-regv2-2026-11-16`  
**Estado:** CORRECCIÓN INICIAL PUBLICADA; VALIDACIÓN INDEPENDIENTE PENDIENTE.

## Acciones ejecutadas
- Se creó la rama desde `migration/registry-v2-reset-core-002`; PR #8 y main no fueron modificados.
- Se corrigió el schema para admitir la propiedad raíz `$schema` declarada por el registro.
- Se trasladaron las condiciones de cardinalidad de identidades al array `identities`, exigiendo una ocurrencia de softly, katarina y audeline.
- Se retiraron atribuciones globales sin respaldo: implementación TLS/aislamiento a Katarina, integración heredada Aurora/Autumn y capacidad separada de coordinación sistémica.
- Las capacidades procedentes de paquetes TITAN se dejaron como candidatas no asignadas, sin autorización ni herencia.
- La coordinación sistémica se reconcilió con `core-governance`, conforme a RESET sección 3.2.
- Se añadieron restricciones de coherencia entre estado y autoridad de paquetes y se eliminaron estados de capacidad aprobada incompatibles con autorización no concedida.

## Verificaciones locales ejecutadas

- PASS — json_parse
- PASS — schema_parse
- PASS — identity_count
- PASS — identity_set
- PASS — domain_ids_unique
- PASS — package_ids_unique
- PASS — capability_ids_unique
- PASS — capability_domains_exist
- PASS — capability_packages_exist
- PASS — identity_domains_exist
- PASS — parent_domains_exist
- PASS — candidate_packages_non_authoritative
- PASS — packages_authority_consistent
- PASS — no_approved_capability
- PASS — zoe_temporary_only
- PASS — schema_has_root_schema_property
- PASS — schema_identity_exactness

Estas comprobaciones se ejecutaron sobre los documentos recuperados de la rama. **No equivalen a ejecutar un validador JSON Schema Draft 2020-12**. No hay workflow CI asociado a los commits correctivos al momento del corte.

## Pendientes bloqueantes
1. Resolver las cuatro rutas de paquetes TITAN usando el árbol fuente exacto; no se inventaron rutas.
2. Implementar y ejecutar validación real Draft 2020-12, incluidos IDs duplicados e integridad referencial. `uniqueItems` solo evita objetos idénticos, no IDs repetidos.
3. Revisión técnica de Katarina sobre el nuevo HEAD.
4. Segunda auditoría independiente de Audeline sobre el HEAD corregido y validado.
5. No fusionar PR #8 ni esta rama hasta cumplir las condiciones anteriores y recibir GO independiente.

## Commits
- Registro: `7cbad239117aceda982435da27d7465c4239bcb5`.
- Schema: `7df09bac799fecbbe23341946dd17e6b0f560376`.

## Preservaciones
No se modificó `main`, PR #8, el registro histórico 1.0.0, Runtime, KAT-006 ni TITAN. No se activaron paquetes ni se concedió autoridad operativa.
