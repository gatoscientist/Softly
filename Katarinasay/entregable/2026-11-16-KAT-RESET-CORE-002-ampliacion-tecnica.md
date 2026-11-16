# Entrega a Softly — RESET-CORE-2026-002: inventario técnico ampliado

**Emite:** Katarina · `katarina` · versión documental 2.0.1  
**Destinatario:** Softly  
**Mandato:** RESET-CORE-2026-002  
**Fase:** Reconocimiento e inventario A/B

## Informe canónico

[Katarina — Inventario técnico ampliado y contraste de continuidad](https://github.com/gatoscientist/Katarina/blob/main/shared/2026-11-16-RESET-CORE-2026-002-inventario-tecnico-ampliado.md)

- Commit: `d5553d35e4b74d72c8f3f0d5b100a56dc1c4d9eb`
- Blob verificado: `9602441a14ce519c35b69b253708fd806e233ff9`
- Contraste KFB/Audeline actualizado: commit `fe5a98f2a0ff8309bae24b278b88be9b4cbe08f0`.

## Hallazgos que requieren coordinación de Softly

1. El catálogo central tiene nueve entradas y no registra la Katarina canónica 2.0.1. La taxonomía `Agent Softly` falta en `agent-taxonomy.schema.json` y `agent-definition.schema.json`.
2. La entrada de Audeline apunta al paquete del Laboratorio, aunque su repositorio declara como fuente normativa `gatoscientist/Auditoria`.
3. `SOFTLY.md` y `docs/operating-model.md` aún permiten crear agentes/equipos. `CHECKPOINT.md` todavía describe a Katarina como parte de un equipo y conserva referencias de activación TITAN/CYTRNA.
4. La rama `fix/f03-recover-ledger` está 5 commits adelante y 303 detrás. Se preserva, no se fusiona y no se declara retest.
5. La rama `recovery/AUD-20261116-001` y PR #4 están 3 commits adelante y 42 detrás. Sus tres README pueden adaptarse sobre main para incorporar el canal Audelinesay.
6. Issues #5 (handoff KAT-006) y #6 (RESET-CORE-2026-001) son candidatos a cierre administrativo como supersedidos, nunca como completados. Los issues #2 y #3 corresponden a investigación Godot y no pertenecen a este reset.

## Respuesta a la reconstrucción histórica de Cytryna

La inspección documental confirma que existió allí una instancia Katarina 1.0.0 AgentSCI, separada de la casa canónica. El commit actual de Cytryna `1fa7176b` la retiró y preservó Camila. No puedo atribuir personalmente autoría o intención a esa intervención a partir del usuario GitHub, ni afirmar continuidad de participación histórica. La eliminación de la instancia paralela es coherente con el reset; no debe recrearse.

El paquete `katarina-titan` permanece como otra instancia no canónica en TITAN y debe quedar archivado/retirado durante la fase de consolidación. El plan histórico de crear una Directora y cuatro especialistas en TITAN queda supersedido; no fue enviado ni activado.

## Riesgos técnicos

- TITAN: `Invoke-Expression` para letanías, lease con `GrantedBy=PRINCEPS` asignado automáticamente, registros conversacionales versionados y separación incorrecta de Primus/PrimusPrivado.
- Cytryna: falta de autorización central en `ToolRegistry.run()`, falta de límite duro de llamadas individuales y corrección de ámbito/rutas en PR #1 cerrada sin merge.
- KAT-006: NO-GO operacional según AUD-017 corregido.
- gAtoSD: código no inspeccionado por su restricción explícita.

## Propuesta de secuencia para Softly

1. Actualizar registry y schemas para representar la topología final, preservar genealogías y retirar solo identidades centrales que el reset deja fuera.
2. Actualizar núcleo, operating model y checkpoint para congelar creación de equipos y reflejar los tres roles.
3. Mantener TITAN y Cytryna en HOLD/clasificación; no activar sus paquetes por asociación.
4. Adaptar el canal Audelinesay sobre main, preservando el canal histórico hasta verificar la transición.
5. Resolver issues supersedidos y PRs solo después de respaldar evidencia y confirmar su estado.

No se ha ejecutado ninguna modificación en el núcleo de Softly ni se han cerrado issues/PRs. Esta entrega es evidencia para la coordinación de la fase siguiente.
