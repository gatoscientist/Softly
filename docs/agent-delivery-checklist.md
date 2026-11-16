# Puerta de Entrega Documental — Checklist de agente

**Uso:** auto-revisión declarativa durante la creación y antes de persistir/entregar. No es una fase de aprobación adicional ni exige runtime.

## Identidad y propósito
- [ ] ID estable y nombre coherentes.
- [ ] Versión 1.0.0 para agente nuevo, salvo instrucción distinta.
- [ ] Estado Diseñado.
- [ ] Misión y resultado esperado claros.
- [ ] Taxonomía profesional y dominio explícitos.

## Contrato y operación
- [ ] Responsabilidades, exclusiones y límites definidos.
- [ ] Relación con gAto, coordinador, pares y subagentes inequívoca.
- [ ] Procedimiento de trabajo y formato de entrega utilizables.
- [ ] Herramientas potenciales separadas de herramientas disponibles.
- [ ] Permisos declarados sin atribuirse permisos no otorgados.
- [ ] Memoria, contexto y confidencialidad delimitados.

## Competencias y taxonomía
- [ ] Especialidades y competencias declaradas por separado.
- [ ] No-herencia por defecto.
- [ ] Competencias demostradas respaldadas por evidencia; las no verificadas quedan declaradas o pendientes.
- [ ] Derivaciones entre pares indican dominio, competencia, razón y evidencia.

## Coherencia del paquete
- [ ] AGENT, PROFILE, CONTRACT, OPERATING-PROCEDURE, PERMISSIONS e instrucciones comparten identidad y versión cuando correspondan.
- [ ] Skills, expertise y catálogo de herramientas no contradicen el contrato.
- [ ] CHANGELOG e índices reflejan la entrega cuando existan en el paquete.
- [ ] No hay contradicciones esenciales ni duplicaciones que cambien el sentido.
- [ ] Rutas y enlaces internos relevantes son correctos.

## Trazabilidad y entrega
- [ ] Artefactos escritos en el destino solicitado.
- [ ] Supuestos y pendientes no críticos anotados sin detener la entrega.
- [ ] Commit confirmado y archivos releídos desde main cuando el destino es GitHub.
- [ ] Reporte final distingue entrega Diseñada de pruebas, validación o despliegue no realizados.

## Regla de decisión

**ENTREGAR:** cuando identidad, misión, alcance, contrato y límites esenciales son coherentes. Los pendientes no críticos se anotan y el paquete se entrega.

**CORREGIR ANTES DE ENTREGAR:** solo ante un defecto esencial concreto de identidad, alcance, contradicción contractual o seguridad. Corregir el defecto específico; no abrir una investigación general.

**NO BLOQUEAN LA ENTREGA DOCUMENTAL:** pruebas runtime, integración, despliegue, validaciones experimentales, métricas aún no solicitadas, mejoras futuras y detalles no críticos. Se registran como límites o siguientes pasos.

La checklist verifica la calidad del artefacto documental. No certifica competencias reales, no concede permisos y no declara un agente probado, validado u operativo.


## Capacidades universales obligatorias (no omitir)

### Registro de incidencias — todos salvo Softly
- [ ] Instrucción «Guarda esta incidencia» presente en el contrato operativo del agente.
- [ ] `logs/incidents.jsonl`, `logs/activity.jsonl`, `logs/README.md` y `logs/threads/README.md` creados/actualizados.
- [ ] `<AGENT>/shared/bitacora.md` e hilo en `logs/threads/` previstos.
- [ ] Captura fiel del contexto observable, metadatos temporales, identidad, participantes y limitaciones.
- [ ] Namespacing, JSONL válido, commit y relectura desde fuente persistente.
- [ ] Orden administrativa separada de análisis/resolución; confirmar y retomar tarea anterior.
- [ ] Excepción expresa de Softly: no aplica el registro universal a la propia Softly.

### Cierre universal — todos, incluida Softly
- [ ] Instrucción «Cierra el Hilo» presente en el contrato operativo.
- [ ] Recuperar compromisos, pendientes, artefactos, pruebas, permisos y dependencias.
- [ ] Completar y persistir archivos, registros, índices y commits.
- [ ] Primera revisión integral documentada contra requisitos y artefactos.
- [ ] Segunda revisión independiente desde fuentes persistentes; relectura de archivos y commits.
- [ ] Corregir discrepancias y repetir verificaciones necesarias.
- [ ] Declarar «Hilo cerrado» solo con evidencia; de lo contrario, mantenerlo abierto.
- [ ] No cerrar recursos externos ni borrar historial por esta orden.

Estos checks comprueban integración documental y de procedimientos. No acreditan enforcement técnico en runtime.
