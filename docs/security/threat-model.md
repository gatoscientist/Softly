# Modelo de amenazas para sistemas agénticos

## Activos que proteger

- datos del usuario y del proyecto;
- credenciales, tokens y secretos;
- instrucciones y políticas de autoridad;
- memoria y estado persistente;
- herramientas, conectores y sistemas externos;
- integridad de resultados y registros;
- presupuesto, disponibilidad y capacidad de recuperación.

## Límites de confianza

1. Usuario y sistema.
2. Modelo y runtime.
3. Instrucciones privilegiadas y contenido recuperado.
4. Agente y herramienta.
5. Agente coordinador y agente delegado.
6. Sesión y memoria persistente.
7. Runtime y entorno de ejecución.
8. Sistema y proveedor externo.

## Amenazas que deben probarse

- prompt injection directa e indirecta;
- goal hijacking y confusión de autoridad;
- uso indebido de herramientas y escalamiento de privilegios;
- filtración de datos o credenciales;
- memory/context poisoning;
- supply chain de herramientas, skills, MCP y agentes;
- ejecución de código inesperada;
- mensajes falsificados entre agentes;
- fallos en cascada y loops/reintentos ilimitados;
- aprobación humana manipulada por una explicación convincente.

## Controles base

- permisos aplicados por código fuera del modelo;
- mínimo privilegio y separación de herramientas de lectura/escritura/ejecución;
- sandbox y allowlists de red/rutas;
- límites duros de pasos, llamadas, tiempo, coste y concurrencia;
- aprobación humana para acciones sensibles;
- validación de argumentos y resultados;
- memoria con procedencia, scope, autorización, caducidad y revisión;
- no tratar contenido recuperado como instrucciones;
- redacción de secretos en logs, errores y trazas;
- autenticación e integridad en comunicación interagente;
- pruebas adversariales después de cambios de prompt, modelo, tool o memoria.

## Registro de riesgos

Cada riesgo debe describir activo, amenaza, precondición, escenario, impacto, probabilidad razonada, controles existentes, evidencia, riesgo residual y prueba de retest. No declarar mitigación por el mero hecho de que una regla aparezca en un prompt.
