# Catálogo de agentes

Este directorio conserva definiciones, contratos y versiones de agentes que estudiamos o diseñamos. No representa agentes desplegados.

## Estructura

- `profiles/`: fichas por agente ([índice de perfiles](profiles/README.md)).
- `templates/`: briefs, molde de generación y perfiles ([índice de plantillas](templates/README.md)).
- Cada perfil debe tener ID, versión, propósito, límites, capacidades, herramientas, memoria, autonomía, supervisión, evaluaciones y cambios.

## Versionado

Una modificación de instrucciones, herramientas, permisos, memoria o modelo puede alterar el comportamiento. Registrar versión nueva y enlazar experimentos comparativos. No reemplazar silenciosamente la configuración histórica.

## Estados

Propuesto → Diseñado → Prototipado → Probado → Validado → Operativo.

El estado requiere evidencia. Un prompt escrito no equivale a un agente funcional.


## Modelo reutilizable e incorporación a proyectos

El modelo de referencia está en [`docs/architecture/agent-model-v0.1.md`](../docs/architecture/agent-model-v0.1.md). Distingue cuatro piezas: definición portable del agente, brief de incorporación, asignación contextual al proyecto y sesión de trabajo.

Usar [`templates/agent-brief.md`](templates/agent-brief.md) para solicitar agentes para un proyecto. El brief no crea agentes ni concede permisos; sirve para analizar la necesidad, seleccionar definiciones existentes, proponer brechas y diseñar asignaciones que deben pasar por las aprobaciones correspondientes.

No mezclar la definición maestra con el contexto de un proyecto. La memoria y los permisos quedan aislados por proyecto salvo autorización explícita y controlada.
