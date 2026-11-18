# Deliberación Softly + PowerShell — Ronda 2: inspección de Cytryna

**Fecha:** 2026-11-18  
**Repositorio examinado:** `gatoscientist/Cytryna`  
**Alcance:** inspección de `SOFTLY.md`, extensiones A/B/C, `Cytryna/app.py`, `Cytryna/coordinator.py`, `Cytryna/gui.py`, `tools/base.py`, `tools/builtin.py`, `tools/execution_tools.py`, `guardian/policy.py`, `guardian/manifest.json` y README/checkpoint.  
**Estado de verificación:** inspección estática del código. No se ejecutó la aplicación ni la suite de pruebas.

## 1. Hallazgos comprobados

### 1.1 El runtime ya tiene un canal genérico de herramientas

`Cytryna/app.py` construye un `ToolRegistry` mediante `build_default_registry()` y lo entrega a `AgentCoordinator`.

`tools/base.py` define:
- Contrato común `Tool` con `execute()`, `verify()` y `run()`.
- Resultado `ToolResult` con éxito, salida, verificación y metadatos.
- Registro `ToolRegistry` con validación de esquema JSON y ejecución.

`Cytryna/coordinator.py` publica las herramientas registradas en el prompt y procesa bloques `<tool_call>`. Ejecuta cada herramienta a través de `self.tools.run(...)` y devuelve al modelo el resultado, incluido éxito y estado de verificación. El flujo es síncrono dentro del turno del coordinador.

### 1.2 La consola de Softly habilita herramientas; la GUI conversacional no

El bucle de consola llama directamente a `coordinator.chat_turn(...)` con ejecución de herramientas habilitada por defecto.

En cambio, `Cytryna.app.Cytryna.chat_turn()` llama al coordinador con `allow_tool_execution=False`. La GUI usa exactamente esa fachada en su worker (`Cytryna/gui.py`, método `send_message`). Por tanto, la conversación de la GUI no puede invocar las herramientas registradas. Esto coincide con el README: las herramientas generales del runtime permanecen deshabilitadas en GUI.

### 1.3 PowerShell ya se ejecuta localmente, pero solo desde el botón gráfico

`Cytryna/gui.py` contiene un flujo dedicado:
- Botón PowerShell que abre un diálogo.
- Revisión humana del script y confirmación explícita.
- Resolución de `pwsh` o `powershell` mediante PATH.
- Ejecución con `subprocess.run`, `shell=False`, stdin por pipe y timeout de 60 segundos.
- Directorio de trabajo igual al proyecto activo.
- Entorno reducido a PATH y variables de Windows/TEMP seleccionadas.
- Captura de stdout/stderr, código de salida, duración y timeout.
- Redacción de secretos y límite de salida de 12.000 caracteres.
- Hilo de trabajo separado y cola de resultados hacia la GUI.

El resultado vuelve a la interfaz mediante `self._results`; no existe una interfaz pública reutilizable por el coordinador.

### 1.4 El registro de herramientas no contiene PowerShell

`tools/builtin.py` registra herramientas de notas, proyectos, dependencias, búsquedas, verificación Python y comandos de desarrollo. No registra una herramienta PowerShell.

La herramienta `ProjectCommandTool` (`tools/execution_tools.py`) permite un conjunto enumerado de operaciones como tests, compile y consultas Git. Su contrato dice expresamente que no acepta comandos shell libres. Utiliza subprocess de forma acotada y `shell=False`, pero no es un ejecutor PowerShell.

### 1.5 Guardian no es un sandbox de procesos

`guardian/policy.py` media operaciones de archivos, rutas, secretos e integridad del mandato. No intercepta ni restringe las acciones que realiza un proceso PowerShell iniciado directamente por GUI. El propio `SOFTLY.md` advierte que Guardian no es un sandbox.

### 1.6 Los contratos de permisos aún no son autorización efectiva

Las herramientas declaran permisos como `read:project`, `write:project` o `execute:project`, y el coordinador los muestra en el prompt. `ToolRegistry` valida parámetros, pero no aplica una política de autorización por identidad de director, operación o concesión. La presencia de un permiso en el contrato no prueba que el acceso esté efectivamente autorizado.

## 2. Contraste con la ronda 1

La recomendación de Zoe queda confirmada en su punto central: la solución más corta es reutilizar el registro y el ciclo de herramientas existente, no introducir un servicio web ni una cola.

Se precisa una distinción importante: el flujo de herramientas existe en la consola, pero la fachada pública usada por la GUI lo deshabilita. Además, el ejecutor PowerShell actual está acoplado a la GUI y a su diálogo de confirmación. No basta con habilitar herramientas en GUI: primero hay que extraer el ejecutor y definir su política de autorización.

Tampoco se encontró evidencia en el repositorio de agentes directores persistentes ni de un canal IPC que permita a procesos de directores independientes invocar el runtime. El mandato normativo advierte que la coordinación de turnos y herramientas no debe confundirse con agentes autónomos persistentes.

## 3. Modificación mínima recomendada

### Paso 1 — Extraer el ejecutor existente

Mover la lógica de `CytrynaGUI._execute_powershell` a un componente reutilizable sin dependencias de Tkinter, por ejemplo `tools/powershell_executor.py` o `tools/powershell_tool.py`.

Debe devolver `ToolResult` con stdout/stderr redactados, código de salida, duración, timeout y límites de salida. Mantener `shell=False`, entorno explícito y timeout. El GUI puede seguir llamando a este mismo componente y mostrar el diálogo de confirmación actual.

### Paso 2 — Registrar una herramienta PowerShell en el runtime

Añadir una herramienta a `build_default_registry()`. El coordinador ya sabe describir, invocar y devolver resultados de herramientas; no necesita una nueva arquitectura de orquestación.

La primera versión debe ofrecer operaciones tipadas/allowlisted (por ejemplo, diagnóstico de entorno, lectura acotada o comandos de desarrollo concretos), no una entrada de script arbitrario disponible para cualquier llamada del modelo.

### Paso 3 — Crear una autorización efectiva, no solo declarativa

Antes de ejecutar, validar una concesión local que identifique director/instancia, operaciones permitidas, proyecto o rutas, expiración y límites. La política debe aplicarse en el ejecutor, no confiar en el prompt ni en el nombre del agente.

Para que la experiencia sea inmediata, las operaciones inocuas incluidas en una concesión activa no deben abrir diálogos por cada llamada. Operaciones destructivas, cambios de seguridad, credenciales, elevación o fuera del alcance deben exigir confirmación humana. La concesión debe poder revocarse.

### Paso 4 — Conectar directores

- Si el director ejecuta dentro del mismo proceso/runtime de Softly: llamada directa al servicio/herramienta registrada; no hace falta IPC.
- Si los directores viven en procesos separados: añadir un único adaptador IPC local autenticado (named pipe con ACL de Windows o Unix domain socket), con solicitudes estructuradas y respuestas correlacionadas. No abrir un endpoint de red ni construir colas distribuidas.

### Paso 5 — Devolver resultados

Reutilizar el formato `ToolResult` y el ciclo del coordinador. La respuesta debe incluir salida, código de salida, duración, timeout, estado de autorización y un identificador de correlación. Diferenciar proceso terminado con código cero de verificación semántica de los efectos.

## 4. Lo que no se debe hacer

- No activar indiscriminadamente `allow_tool_execution=True` en la GUI: eso habilitaría todas las herramientas generales, no solo PowerShell.
- No convertir el botón actual en un canal de script libre para todo agente.
- No tratar `shell=False` como sandbox de PowerShell.
- No asumir que Guardian controla los efectos del proceso hijo.
- No construir REST, WebSocket, broker, cola o servicio remoto antes de demostrar que se necesita comunicación entre procesos.
- No pedir autorización humana para cada operación inocua cuando ya exista una concesión explícita, limitada y vigente.

## 5. Evidencia y límites

La inspección confirma el código y los flujos descritos, pero no demuestra comportamiento en ejecución. No se ejecutaron pruebas, no se midió latencia y no se validó el entorno Windows del usuario. La inspección de este repositorio tampoco demuestra cómo se conectan actualmente las instancias locales de Zoe, Lina u otros directores.

**Conclusión de ronda:** el cuello de botella técnico está bien localizado. Softly ya tiene un coordinador de herramientas y Cytryna ya contiene una implementación local de subprocess para PowerShell; están separados. La mejora mínima es extraer el ejecutor de la GUI, registrarlo como herramienta del runtime y aplicar una concesión de autorización efectiva. IPC es una extensión condicional, no el punto de partida.
