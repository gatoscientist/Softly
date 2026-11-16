# Migración transversal — capacidades universales

**Fecha:** 2026-11-16  
**Repositorio auditado:** `gatoscientist/Softly` (rama `main`)  
**Mandato:** integrar «Guarda esta incidencia» y «Cierra el Hilo» en núcleo, molde y agentes existentes.

## Directivas fuente leídas íntegramente

- [Directiva de registro universal de incidencias](../Katarinasay/entregable/directiva-registro-universal-incidencias.md)
- [Directiva de cierre universal de hilos](../Katarinasay/entregable/directiva-cierre-universal-de-hilos.md)

## Cambios documentales persistidos

- `SOFTLY.md`: exclusión de Softly respecto del registro; obligación universal de cierre.
- `agents/templates/agent-generation-mold.md`: herencia de ambos procedimientos, con excepción de Softly para incidencias.
- `docs/agent-delivery-checklist.md`: checklist de integración de logs, bitácora, commit/relectura y doble revisión de cierre.
- `docs/architecture/taxonomy-and-mold-validation.md`: capacidad heredada y límites de implementación.
- `docs/architecture/agent-model-v0.1.md`: protocolos transversales del agente portable.
- `agents/profiles/audelin.md`: migración documental de Audelin a ambos protocolos.
- `logs/README.md` y `logs/threads/README.md`: guía y regla de capacidades universales.
- Este informe: inventario, alcance, commits y límites.

## Inventario y estado de migración en este repositorio

| Agente / componente | Ubicación observada | Registro de incidencias | Cierre universal | Estado |
|---|---|---|---|---|
| Softly (núcleo operativo/documental) | `SOFTLY.md`, `CHECKPOINT.md`, moldes y runtime mini | Excluida por mandato | Incorporado documentalmente en `SOFTLY.md` y checklist | Parcial: regla documental; no runtime |
| Audelin (perfil de agente) | `agents/profiles/audelin.md` | Incorporado en perfil | Incorporado en perfil | Migrado documentalmente; sin instancia runtime demostrada |
| Katarina 2.0.0 | Canal `Katarinasay/`, entregables y referencias; paquete canónico no presente en este repo | Pendiente en su repositorio/paquete fuente | Pendiente en su repositorio/paquete fuente | No migrada desde Softly |
| Agentes/equipos de otros repositorios (p. ej., Dra. Katarina, Cytryna, Laboratorio de Agentes) | Referenciados por contexto, pero paquetes fuente no contenidos en este repo | Pendiente de inventario externo | Pendiente de inventario externo | No migrados; requieren inspección y escritura en repositorios fuente |

El inventario GitHub de `gatoscientist/Softly` contiene un perfil activo bajo `agents/profiles/`: Audelin. No se encontraron paquetes canónicos completos `AGENT.md/CONTRACT.md/OPERATING-PROCEDURE.md` de otros agentes en este repositorio. Los documentos de `Katarinasay/` son canales y entregables, no equivalen a un paquete portable. Los directorios de proyectos/experimentos no se han contado automáticamente como agentes.

## Contratos operativos sintetizados

### «Guarda esta incidencia»
La orden captura evidencia observable, metadatos del agente/instancia/participantes y archivos/referencias disponibles. Persiste en `logs/incidents.jsonl`, `logs/activity.jsonl`, los README de logs/hilos, `shared/bitacora.md` e hilo en `logs/threads/`; exige commit y relectura verificable. Namespacing si el repositorio es compartido. La confirmación es breve; luego se retoma la tarea previa. No investiga, diagnostica, corrige, disculpa ni altera prioridades. Se excluyen secretos, datos privados innecesarios y cadena de pensamiento privada; se declaran vacíos de captura.

### «Cierra el Hilo»
Aplica a Softly y todos los agentes. Recupera compromisos y pendientes, completa lo autorizado, guarda artefactos, actualiza índices/bitácoras, realiza commits y pruebas requeridas, ejecuta primera revisión integral y segunda revisión independiente desde fuentes persistentes. Ante cualquier discrepancia se corrige y se repiten verificaciones. Si queda un bloqueo, no se declara cerrado. No autoriza borrar historia ni cerrar recursos externos.

## Runtime — estado real observado

`softly-runtime/runtime.py` y `manifest.json` describen Softly Runtime Mini 0.2.0. El manifiesto solo permite `create_text_file`; el runtime valida exactamente esa operación y un ledger técnico propio `events.jsonl`/`events.head`. Sus pruebas existentes cubren escritura confinada, autorización y ledger encadenado.

No se encontró en ese contrato runtime una operación de captura de conversación, append de incidencias JSONL, actualización de bitácoras, doble revisión de cierre, Git commit, lectura remota GitHub ni cierre conversacional. Por tanto:
- **Implementación documental:** integrada en núcleo, molde, checklist, modelo y perfil Audelin.
- **Implementación runtime:** no implementada por estos cambios.
- **Comportamiento efectivo:** los agentes que reciben estos contratos deben seguir el procedimiento manualmente solo cuando tengan acceso real a sus repositorios/herramientas. No existe enforcement automático demostrado.

No se modificó el runtime, su manifiesto, schema ni suite de pruebas, porque el runtime actual no ofrece esas capacidades y una ampliación requeriría diseño e implementación técnica separados, permisos de filesystem/Git y pruebas de seguridad.

## Commits

| Archivo | Commit |
|---|---|
| `SOFTLY.md` | `fc9c12db0827770f88c95c3571eecbf3ec6e2b39` |
| `agents/templates/agent-generation-mold.md` | `abbef477f685db1f8e3dd11f858e7c96c382d27a` |
| `docs/agent-delivery-checklist.md` | `f480b4ce5059fb534796f8f17739069da0daa559` |
| `docs/architecture/taxonomy-and-mold-validation.md` | `ba357b6ca36c9e744d0859c31c533c0cf9e7c75c` |
| `logs/README.md` | `70366f9808bf58c3b90746d62303f5106f5ba283` |
| `logs/threads/README.md` | `aa81cd2e3ac416685d9e943d7b4a9d7340d017d8` |
| `agents/profiles/audelin.md` | `ca805b569ce0d6b1a8df3f1534c9b879fd87fd30` |
| `docs/architecture/agent-model-v0.1.md` | `d7901f191829752aef3a10a3a0a2cdabf0e9ebec` |

## Validaciones realizadas

- Las dos directivas originales se leyeron completas desde GitHub.
- El árbol del repositorio se consultó recursivamente; la respuesta indicó `truncated=false`.
- Los ocho commits indicados fueron devueltos por GitHub al escribir cada archivo.
- No se ejecutó una segunda lectura verificadora post-escritura de todos los archivos ni se ejecutó la suite de runtime tras estas modificaciones documentales.
- No se ejecutaron pruebas de comportamiento de agentes ni pruebas de runtime para estas nuevas capacidades.
- No se revisaron ni migraron los repositorios externos que contienen otros agentes.

## Pendientes explícitos

1. Releer desde GitHub los ocho archivos cambiados y comprobar commits/paths.
2. Inspeccionar la ubicación canónica y migrar Katarina 2.0.0 en su repositorio fuente.
3. Identificar todos los repositorios/paquetes externos de agentes administrados por Softly y migrarlos en su origen.
4. Diseñar, implementar y probar por separado una extensión del runtime para incidencias/cierre si gAto decide hacerlas ejecutables; no dar por supuesto enforcement.
5. Ejecutar las pruebas ya existentes del runtime y verificar que estas actualizaciones documentales no alteraron el código (no se espera cambio de código).

**Conclusión:** la integración documental del núcleo/molde/checklist y la migración del perfil Audelin están persistidas. La migración transversal de todos los agentes externos y la implementación runtime no están completas. Por honestidad probatoria, no se declara todo el ecosistema migrado ni comportamiento automático implementado.
