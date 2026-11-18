# Deliberación Softly + PowerShell — Ronda 1: Zoe

**Fecha:** 2026-11-18  
**Repositorio examinado:** `gatoscientist/Zoe`  
**Alcance:** lectura documental de identidad, contratos del director, especialistas, colaboración, seguridad y aceptación.  
**Estado de verificación:** inspección documental; no se ejecutó código de Zoe.

## 1. Hallazgos comprobados

Zoe está definida como agente directora de ingeniería, automatización, seguridad e integración mediante PowerShell, Python y APIs. Su cápsula documental contiene cuatro perfiles internos:

- **AGENTDEV:** PowerShell, Python, APIs, automatización, servicios y comunicación entre procesos.
- **AGENTSEC:** PowerShell Remoting, WinRM, autenticación, autorización, mínimo privilegio, secretos, aislamiento y auditoría.
- **AGENAUD:** revisión adversarial, pruebas, vulnerabilidades, regresiones y evidencia.
- **AGENTSOFTLY:** compatibilidad con contratos y arquitectura Softly.

El contrato del director asigna a Zoe la responsabilidad indivisible de delimitar, coordinar, integrar y verificar. Los especialistas no son agentes externos autónomos ni poseen credenciales, buzones o autoridad independiente.

El contrato de seguridad exige autorización por operación sensible, validación de entradas, límites de sesión, timeouts, cancelación, trazabilidad sin secretos y reducción de privilegios. Para PowerShell remoto recomienda endpoints restringidos/JEA y advierte contra exponer una consola remota arbitraria.

El checkpoint de Zoe dice expresamente que su inicialización es documental: no implementa runtime, ejecutores PowerShell remotos ni servicios API.

## 2. Consecuencias para la integración

La cápsula de Zoe aporta las competencias para diseñar y auditar el puente, pero no aporta por sí misma un canal de ejecución. La integración debe residir en Softly local, que es el equipo donde existe el proceso PowerShell y donde se pueden aplicar los permisos efectivos del sistema operativo.

La separación de responsabilidades más corta es:

1. El director formula una solicitud estructurada.
2. Softly local valida identidad, alcance y autorización.
3. Un ejecutor local invoca PowerShell sin shell intermedio, con directorio de trabajo, entorno y timeout definidos.
4. Softly devuelve stdout, stderr, código de salida, duración y estado de timeout.
5. El director integra el resultado y conserva la trazabilidad.

No se necesita PowerShell Remoting si el proceso se ejecuta en el mismo computador. Tampoco se necesita un servicio HTTP, una cola o un servidor adicional si los directores pueden llamar directamente a una herramienta del runtime local.

## 3. Arquitectura mínima propuesta

**Primera opción: herramienta local del runtime.** Exponer un ejecutor PowerShell como herramienta registrada en Softly, siguiendo el contrato existente de herramientas: esquema de parámetros, permisos declarativos, resultado estructurado y verificación. El coordinador ya tiene un mecanismo genérico para ejecutar herramientas y devolver sus resultados al modelo solicitante.

**Segunda opción, solo si los directores viven en procesos independientes:** un canal IPC local autenticado (por ejemplo, named pipe con ACL de Windows o Unix domain socket con permisos de sistema). Debe transportar solicitudes estructuradas y respuestas correlacionadas. No introducir un servidor de red si IPC resuelve la comunicación.

La herramienta debe recibir operaciones tipadas y acotadas por defecto. Un campo de script libre no puede considerarse seguro solo porque se ejecute localmente o use `shell=False`: PowerShell interpreta el contenido y puede modificar el sistema con los privilegios del usuario.

## 4. Prioridad: inmediatez sin confirmaciones repetitivas

La latencia de coordinación se reduce eliminando la ida y vuelta humana, no eliminando la autorización. Se recomienda un modelo de capacidades:

- **Lectura/diagnóstico de bajo riesgo:** ejecución automática si la operación pertenece a una allowlist explícita y al alcance concedido al director.
- **Escritura acotada:** automática solo cuando el director recibió autorización explícita para ese proyecto y tipo de cambio.
- **Acciones destructivas, cambios de seguridad, credenciales, elevación o alcance del sistema:** confirmación humana explícita.
- **Script arbitrario:** no habilitarlo como permiso general de todos los directores. Si se necesita, exigir autorización puntual o una concesión temporal, visible y revocable.

Una concesión de sesión evita preguntar por cada comando inocuo. Debe identificar director, operaciones permitidas, proyecto/raíz, expiración y límite de recursos.

## 5. Riesgos y controles

- La identidad declarada por un agente no autentica un proceso local.
- Un permiso textual como `execute:project` no basta si el registro no lo aplica.
- El directorio de trabajo restringido no impide que un script acceda a otras rutas.
- Ocultar variables de entorno reduce exposición de secretos, pero no constituye sandbox.
- Un timeout limita duración, no efectos secundarios ya realizados.
- La salida capturada puede contener secretos; debe redactarse y limitarse.
- Debe existir cancelación real del proceso y registro de actor, operación, destino, resultado y correlación.

## 6. Conclusión de ronda

La arquitectura recomendada es una herramienta PowerShell nativa dentro del runtime de Softly, con ejecución local directa y resultado estructurado. IPC solo es necesario si el director no comparte proceso con Softly.

La prioridad de implementación es comprobar el flujo real del runtime y extraer el ejecutor ya existente de la GUI, evitando duplicar la lógica de subprocess. La seguridad debe residir en el ejecutor/servicio y no depender de instrucciones del modelo.

**Limitación:** esta ronda solo inspeccionó los contratos de Zoe. La propuesta debe contrastarse con el código real de Softly/Cytryna en la ronda 2.
