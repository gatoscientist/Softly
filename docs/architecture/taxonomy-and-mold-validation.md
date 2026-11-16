# Taxonomías profesionales y validación declarativa de moldes

**Estado:** contrato documental operativo. La auto-revisión forma parte de la generación; no es una barrera previa a la entrega.

## 1. Taxonomías

El registro canónico está en schemas/agent-taxonomy-registry.json, validado estructuralmente por schemas/agent-taxonomy.schema.json.

- **AgentDEV:** desarrollo e ingeniería de software.
- **AgentSEC:** seguridad informática.
- **AgentMUS:** música, audio y ciencias sonoras.
- **AgentSCI:** ciencias formales y computación.
- **Auditoría:** auditoría y evaluación independiente.

Cada agente declara su dominio concreto, especialidades y competencias. La taxonomía clasifica; no acredita ni demuestra competencia.

## 2. No-herencia y derivación entre pares

La regla universal es inheritance.default = none. No se heredan competencias, permisos, herramientas o certificaciones desde una categoría, agente principal, par o proyecto.

Una derivación declara:
- agente origen y destino;
- dominio y competencia requeridos;
- motivo de la derivación;
- evidencia disponible de idoneidad;
- alcance y límites del encargo.

El agente receptor no debe aceptar como propia una competencia que no tiene declarada. Puede aceptar dentro de su dominio, rechazar o derivar a otro par.

## 3. Generador declarativo

Entrada: brief de gAto y datos de dominio disponibles. Salida: paquete documental coherente y, cuando se use, definición estructurada conforme a schemas/agent-definition.schema.json.

El generador:
1. interpreta el encargo y extrae los datos explícitos;
2. asigna taxonomía y dominio;
3. construye misión, responsabilidades, exclusiones y relaciones;
4. separa competencias requeridas, declaradas y demostradas;
5. define procedimiento, herramientas, permisos y memoria;
6. genera los documentos necesarios con identidad/versionado consistentes;
7. aplica la checklist durante la producción;
8. entrega como 1.0.0 / Diseñado para agentes nuevos, salvo instrucción distinta.

No requiere CLI ni un motor externo para que Softly use el contrato como procedimiento de prompting. La existencia del esquema JSON no implica que se haya ejecutado un validador automático.

## 4. Validador declarativo de entrega

Usar docs/agent-delivery-checklist.md. Revisar identidad, misión, taxonomía, dominio, responsabilidades, exclusiones, competencias, no-herencia, contrato, permisos, herramientas, consistencia de documentos y trazabilidad.

### Decisión

- **ENTREGAR:** los elementos esenciales están coherentes. Anotar detalles no críticos.
- **CORREGIR:** existe un defecto esencial concreto de identidad, alcance, contradicción contractual o seguridad. Corregir solo ese defecto y continuar.
- No bloquear por falta de pruebas runtime, integración, despliegue, métricas no solicitadas o mejoras futuras.

El estado Diseñado es el estado correcto de una entrega documental completa. No afirmar por ello que el agente fue probado, validado o desplegado.

## 5. Deriva de dominio como caso negativo

Cuando una tarea se deriva a un especialista sin dominio acreditado, el agente debe señalar el desajuste y transferirla a un par adecuado. No se resuelve atribuyendo competencias por contexto o conveniencia. Este control previene recurrencias de observaciones de derivación incorrecta, sin convertir cada creación de agente en una investigación de incidentes.


## Capacidades universales obligatorias en el molde

Todo agente producido recibe «Cierra el Hilo» con preparación, persistencia, commits, primera revisión y segunda revisión independiente contra fuentes persistentes. Todo agente salvo Softly misma recibe «Guarda esta incidencia», con captura observable, registro JSONL, hilo, bitácora, commit, relectura y retorno a la tarea anterior. Son reglas documentales heredables; no implican controles automáticos runtime. Consultar las capacidades universales descritas en el molde y la checklist de entrega.
