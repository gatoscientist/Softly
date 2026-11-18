# Deliberación Softly + PowerShell — Informe final consolidado

**Fecha:** 2026-11-18  
**Directora:** Softly  
**Prioridad:** inmediatez  
**Rondas completadas:** 1) Zoe; 2) Cytryna  
**Tipo de trabajo:** deliberación e inspección documental/estática. No se implementaron cambios en Cytryna ni se ejecutaron pruebas.

## Respuesta ejecutiva

La modificación mínima es **extraer el ejecutor PowerShell que hoy está acoplado a la GUI, convertirlo en una herramienta del registro de Softly y hacer que el runtime la invoque mediante su ciclo de herramientas ya existente**.

El coordinador ya sabe presentar herramientas, recibir `<tool_call>`, ejecutarlas mediante `ToolRegistry` y devolver el resultado al modelo. Lo que falta es registrar una herramienta PowerShell reutilizable y una autorización efectiva para el director solicitante.

No se necesita un servidor, una cola ni PowerShell Remoting si el director y Softly local comparten proceso. Si los directores son procesos independientes, el único componente adicional razonable sería un canal IPC local autenticado.

## Ronda 1 — Zoe: aportes y conclusiones

La documentación de Zoe define cuatro competencias internas útiles:
- AGENTDEV para implementación PowerShell/Python e integración.
- AGENTSEC para identidad, autorización, mínimo privilegio, aislamiento y secretos.
- AGENAUD para revisión adversarial y evidencia.
- AGENTSOFTLY para coherencia con la arquitectura Softly.

El contrato de Zoe asigna al director la responsabilidad de integrar y verificar. Sus especialistas son perfiles internos documentales, no procesos con credenciales o canales operativos propios. El checkpoint declara que Zoe no implementa runtime ni ejecutores PowerShell remotos.

La conclusión de la primera ronda fue reutilizar la ejecución local y evitar infraestructura remota innecesaria. La inmediatez se obtiene eliminando intermediación humana repetitiva, mediante concesiones acotadas, no eliminando controles.

## Ronda 2 — Cytryna: evidencia de implementación

Inspección estática de `SOFTLY.md`, A/B/C, `Cytryna/app.py`, `Cytryna/coordinator.py`, `Cytryna/gui.py`, `tools/base.py`, `tools/builtin.py`, `tools/execution_tools.py`, `guardian/policy.py` y documentación de estado.

### Lo que ya existe

1. `AgentCoordinator` carga las herramientas registradas, procesa llamadas `<tool_call>`, invoca `ToolRegistry.run()` y entrega resultados al modelo.
2. `ToolRegistry` valida esquemas y devuelve `ToolResult`, que puede transportar salida, éxito, verificación y metadatos.
3. La consola de Softly usa el coordinador con ejecución de herramientas habilitada.
4. La GUI conversacional llama a `Cytryna.app.Cytryna.chat_turn()`, que deshabilita explícitamente la ejecución de herramientas.
5. La GUI tiene un botón PowerShell funcional a nivel de código: confirmación humana, `pwsh`/ `powershell`, `subprocess.run`, `shell=False`, timeout 60 s, entorno reducido, salida capturada y redactada, código de salida y duración. Se ejecuta en un hilo y la respuesta vuelve por una cola de GUI.
6. El ejecutor está dentro de `Cytryna/gui.py`; no se ofrece como servicio reutilizable por el runtime.
7. `tools/builtin.py` no registra una herramienta PowerShell. `ProjectCommandTool` es una herramienta separada, enumerada y sin comandos shell libres.
8. Guardian protege rutas, secretos e integridad del Core, pero no es sandbox ni limita los efectos de un proceso PowerShell.
9. Los permisos declarados por herramientas se presentan al modelo, pero el `ToolRegistry` inspeccionado no aplica autorización efectiva por identidad del director o concesión.

### Cuello de botella localizado

El botón PowerShell y el runtime de herramientas son dos caminos separados. La GUI no puede utilizar el registro general de herramientas, y el ejecutor local no puede ser invocado por el coordinador. Los directores no tienen en este repositorio un endpoint operativo comprobado para solicitar PowerShell local.

## Arquitectura recomendada

### Caso A — Director dentro del runtime de Softly

`DIRECTOR → AgentCoordinator → ToolRegistry → PowerShellTool → PowerShell local → ToolResult → DIRECTOR`

Es la opción preferida por latencia y simplicidad. Es una llamada local directa, sin red, servidor ni cola.

### Caso B — Director en proceso independiente

`DIRECTOR → IPC local autenticado → Softly local → PowerShellTool → ToolResult → DIRECTOR`

Solo si la topología real exige separar procesos. En Windows, evaluar named pipes con ACL; en otros sistemas, Unix domain sockets con permisos del sistema. Mensajes estructurados, identidad autenticada, correlación, timeout y respuesta. No abrir un servicio de red por defecto.

## Política para lograr inmediatez

No confundir inmediatez con ejecución irrestricta.

- **Automático:** operaciones allowlisted, de bajo riesgo y dentro de una concesión vigente para ese director y proyecto.
- **Concesión explícita:** permitir que gAto autorice por sesión un conjunto limitado de operaciones, con alcance, expiración y revocación. Evita pedir permiso por cada operación inocua.
- **Confirmación humana:** acciones destructivas, cambios de seguridad, credenciales, elevación, alcance global o script arbitrario fuera de la concesión.
- **Denegado por defecto:** operaciones no reconocidas, parámetros fuera de esquema, identidad no autenticada o concesión vencida.

La identidad del director no debe inferirse de texto generado por el modelo. Si hay IPC, autenticar el proceso/cliente local. El control de autorización debe ejecutarse en el servicio/herramienta, no en el prompt.

PowerShell interpreta el script aunque se use `shell=False`. Un directorio de trabajo y un entorno reducido no forman un sandbox. Los timeouts no revierten efectos secundarios. Redactar y limitar salida, registrar actor, operación, destino, resultado, duración y correlación sin secretos. Mantener el proceso sin elevación automática y definir cancelación.

## Secuencia mínima de implementación

1. **Extraer sin cambiar comportamiento:** mover la lógica de `CytrynaGUI._execute_powershell` a un ejecutor reutilizable sin Tkinter, devolviendo `ToolResult`. Mantener el botón actual y su confirmación usando ese mismo ejecutor.
2. **Registrar herramienta:** implementar `PowerShellTool` y agregarla a `build_default_registry()`. Empezar con operaciones tipadas/allowlisted, no script libre para cualquier modelo.
3. **Aplicar autorización real:** añadir un proveedor de concesiones/capacidades validado por el ejecutor: director, operaciones, proyecto/raíces, expiración y límites. Los permisos declarativos existentes no bastan.
4. **Conectar directores:** llamada directa al runtime cuando compartan proceso. Añadir IPC local autenticado únicamente si se confirma que corren en procesos separados.
5. **Devolver resultado:** usar `ToolResult` con stdout/stderr redactados, exit code, duración, timeout, autorización y correlation ID. El coordinador ya puede devolver el resultado al director.
6. **Probar:** pruebas unitarias para validación, autorización, timeout, cancelación, redacción y salidas; prueba integrada desde un director real hacia Softly local; medición de latencia de extremo a extremo. Distinguir ejecución y validación real.

## No hacer

- No habilitar todas las herramientas de la GUI indiscriminadamente para resolver PowerShell.
- No duplicar el ejecutor dentro del coordinador.
- No diseñar REST, WebSocket, brokers o colas sin necesidad demostrada.
- No habilitar script arbitrario para todos los directores.
- No tratar Guardian, `shell=False` ni el directorio de trabajo como sandbox.
- No añadir una confirmación humana por cada llamada inocua si existe una concesión explícita y acotada.

## Incertidumbres que quedan abiertas

- No se inspeccionó el computador del gAto ni se ejecutó PowerShell allí.
- No se midió la latencia actual ni la potencial.
- No se verificó cómo los directores locales se comunican hoy con la instancia instalada de Softly.
- No se ejecutó la suite de pruebas.
- No se puede afirmar que los agentes directores estén desplegados dentro del mismo proceso o en procesos separados basándose solo en estos repositorios.

Estas incertidumbres no impiden decidir el primer paso: extraer el ejecutor y registrarlo como herramienta local. La decisión sobre IPC se toma después de confirmar la topología de los directores.

## Dictamen final

**Recomendación:** reutilizar el runtime actual de Softly y convertir la ejecución PowerShell de la GUI en una herramienta de primera clase, con autorización por capacidad y resultados estructurados. La llamada directa del coordinador a esa herramienta es el trayecto de menor latencia y menor complejidad que el código inspeccionado permite justificar.

La primera entrega debe limitarse a operaciones seguras y preautorizables. Una vez comprobada la integración con un director real, se amplía el catálogo de operaciones según necesidad. No se requiere modificar el mandato normativo para probar esta arquitectura.

## Persistencia y verificación

Se guardaron los informes de ambas rondas y este informe consolidado en `gatoscientist/Softly`, bajo `research/coordination/`.

La persistencia se verificó mediante respuestas de creación de archivos/commits de GitHub. No se modificaron `SOFTLY.md`, `CHECKPOINT.md` ni el código de Cytryna. No se ejecutaron pruebas ni se implementó la solución.
