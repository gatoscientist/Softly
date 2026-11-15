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
