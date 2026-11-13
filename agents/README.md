# Catálogo de agentes

Este directorio conserva definiciones, contratos y versiones de agentes que estudiamos o diseñamos. No representa agentes desplegados.

## Estructura

- `profiles/`: fichas por agente.
- `templates/`: plantilla común.
- Cada perfil debe tener ID, versión, propósito, límites, capacidades, herramientas, memoria, autonomía, supervisión, evaluaciones y cambios.

## Versionado

Una modificación de instrucciones, herramientas, permisos, memoria o modelo puede alterar el comportamiento. Registrar versión nueva y enlazar experimentos comparativos. No reemplazar silenciosamente la configuración histórica.

## Estados

Propuesto → Diseñado → Prototipado → Probado → Validado → Operativo.

El estado requiere evidencia. Un prompt escrito no equivale a un agente funcional.
