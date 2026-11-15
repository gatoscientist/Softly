# Investigación Auditoría — Agentes de Desarrollo en Godot (Parte I)

- **ID:** AUD-GODOT-20261114-I
- **Equipo:** Auditoría — integración científica y análisis técnico
- **Fecha del corte:** 2026-11-14
- **Fuente primaria de estudio:** *Agentes de Desarrollo en Godot.pdf*, 26 páginas
- **Objeto:** agentes de ingeniería asistida por IA y agentes autónomos en tiempo de ejecución en Godot 4.x
- **Naturaleza:** investigación documental y análisis crítico; no equivale a pruebas independientes de las herramientas.
- **Estado:** estudio documental completo del material recibido; validación externa de versiones, compatibilidad, licencias y benchmarks pendiente.

## 1. Resumen ejecutivo

El documento estudia dos dominios que comparten el motor Godot, pero tienen ciclos de vida y autoridades distintas:

1. **Agentes de ingeniería:** asistentes y agentes que inspeccionan, modifican, ejecutan y depuran proyectos Godot. MCP aparece como protocolo de conexión entre clientes de IA y herramientas del editor o del motor.
2. **Agentes runtime:** entidades del videojuego que perciben el mundo, navegan, deciden, aprenden o conversan durante la ejecución.

La conclusión arquitectónica más robusta es que no existe una única tecnología que resuelva ambos dominios ni todas las formas de inteligencia runtime. La selección debe responder al problema, a la versión de Godot, al lenguaje (GDScript o C#/.NET), a la plataforma de despliegue, al presupuesto de rendimiento y al nivel de autonomía permitido.

El estudio describe un continuo de verificación para ingeniería: edición de archivos, interacción con el editor, ejecución de escenas, observación de errores y comprobación posterior a los cambios. Para agentes runtime describe una composición de navegación, decisión simbólica, aprendizaje por refuerzo e interfaces generativas. En ambos dominios aparece un principio común: **la capacidad de producir una salida no demuestra que el comportamiento sea correcto; hace falta una forma observable y reproducible de validación**.

La investigación también identifica límites importantes: las cifras de herramientas y compatibilidad son sensibles a versiones; los benchmarks de navegación proceden de terceros; el despliegue ONNX depende de Godot .NET y de las plataformas soportadas; los LLM pueden desviarse de la verdad narrativa; y las herramientas de desarrollo con acceso al proyecto requieren controles de permisos y aprobación.

## 2. Alcance, método y categorías epistemológicas

### 2.1 Alcance

Se revisaron las 26 páginas del PDF, incluyendo:
- los dos dominios de agentes y su arquitectura;
- comparativas de servidores MCP y plugins de editor;
- el caso de reparación de Star Catcher;
- el ejemplo de navegación 3D y la discusión de RVO;
- las recomendaciones de optimización y Flow Fields;
- Behavior Trees, máquinas de estado, GOAP y Utility AI;
- Godot RL Agents, sensores, entrenamiento Python y despliegue ONNX;
- NobodyWho y otras alternativas de LLM local;
- la matriz de decisión, hoja de ruta y bibliografía numerada.

Se consideran también los gráficos y tablas embebidos. En particular, el gráfico de la página 13 compara consultas individuales y Flow Fields, y presenta por separado el costo de restricciones gramaticales en inferencia local.

### 2.2 Método

1. Extraer y organizar las afirmaciones técnicas del documento.
2. Conservar nombres, versiones, cifras, licencias y referencias tal como aparecen en la fuente.
3. Separar descripción del documento de inferencia arquitectónica.
4. Identificar supuestos, límites de generalización, dependencias y preguntas que requieren comprobación.
5. No convertir cifras o afirmaciones de proveedores en hechos verificados por Auditoría sin una reproducción independiente.

### 2.3 Convenciones epistemológicas

- **[F-PDF] Hecho documental:** el PDF afirma o describe explícitamente el punto. Esto acredita lo que dice la fuente, no necesariamente su verdad externa.
- **[E-PDF] Evidencia citada:** dato, ejemplo, gráfico, código o referencia que el PDF utiliza para respaldar una afirmación.
- **[I] Inferencia:** interpretación razonada derivada del material.
- **[H] Hipótesis:** explicación o diseño candidato que requiere pruebas.
- **[P] Pendiente:** asunto que no puede resolverse con el PDF por sí solo.

## 3. Dos dominios de agentes: separación de responsabilidades

### 3.1 Agentes de ingeniería y desarrollo

**[F-PDF]** El documento caracteriza MCP como una capa de abstracción para que clientes compatibles —por ejemplo Claude Code, Cursor, Windsurf o Cline— invoquen herramientas específicas sobre un proyecto Godot.

Distingue dos niveles:

- **File-Level:** inspección y modificación de archivos `.gd`, `.tscn`, `.tres` y configuración del proyecto. Puede comprender jerarquías estáticas y reescribir código, pero no observa por sí mismo el comportamiento dinámico del motor.
- **Engine-Level:** conexión con una instancia activa del editor o runtime. Puede ejecutar escenas, inyectar entradas, capturar imágenes, leer errores y, según la herramienta, modificar objetos del editor y aprovechar UndoRedo.

**[I]** La distinción no debe interpretarse como una clasificación binaria de calidad. File-Level es útil para lectura, cambios acotados y automatización reproducible; Engine-Level agrega observabilidad del comportamiento. Una arquitectura robusta puede necesitar ambos y debe registrar cuál produjo cada cambio y cuál verificó el resultado.

**[H]** Un agente de ingeniería confiable debería operar con un ciclo explícito: planificar → inspeccionar → proponer diff → obtener autorización según riesgo → aplicar → ejecutar pruebas → comparar resultado esperado y observado → registrar evidencia. La ejecución de una escena y la ausencia de errores no prueban por sí solas que el juego sea funcional.

### 3.2 Agentes autónomos dentro del juego

**[F-PDF]** El documento agrupa las técnicas runtime en cuatro capas:

1. Navegación y evasión espacial: NavigationServer, NavigationAgent, RVO y Flow Fields.
2. Decisión simbólica/reactiva: Behavior Trees, State Charts, GOAP y Utility AI.
3. Aprendizaje por refuerzo: entrenamiento Python con Godot RL Agents y posible inferencia ONNX.
4. Agentes conversacionales: modelos locales, tool calling, voz y multimodalidad.

**[I]** Son capas funcionales, no necesariamente cuatro subsistemas obligatorios. Un NPC puede usar navegación y una máquina de estados sin RL ni LLM. Un LLM puede redactar diálogo sin gobernar movimiento o reglas de combate. La arquitectura debe introducir cada técnica solo cuando resuelva una necesidad medible.

### 3.3 Frontera entre ambos dominios

**[I]** El agente que desarrolla el juego y el agente que vive dentro del juego no deben compartir indiscriminadamente credenciales, herramientas ni autoridad. El primero puede tener acceso al repositorio y al editor; el segundo debe operar sobre una API de juego acotada. El LLM runtime no debe heredar las capacidades de edición del agente de desarrollo.

## 4. MCP y herramientas de ingeniería: inventario y contraste

### 4.1 Soluciones descritas

El PDF presenta las siguientes herramientas y características (estado atribuido por el documento a noviembre de 2026):

| Herramienta | Arquitectura y capacidades descritas | Restricciones o cautelas indicadas |
|---|---|---|
| Ziva | Dock de editor y MCP local; `run_scene`, entradas temporizadas, captura final, errores y perfilado | Captura un fotograma final, no vídeo continuo; limitaciones de gamepad/táctil; no headless CI según el documento; requiere sesión para capturas |
| Godot MCP Pro (y1uda) | Plugin + servidor Node/WebSocket; catálogo granular de herramientas para escenas, nodos, animación, física, navegación, UI, shaders y QA; UndoRedo y Lite Mode | Comercial; Godot 4.4+ y Node.js 18+; cifras del catálogo difieren entre Asset Library y sitio del proveedor |
| Coding-Solo/godot-mcp y variante bradypp | Servidor Node y operaciones CLI/GDScript; edición de escenas y recursos; modo Read-Only | Requiere Node.js; el PDF destaca diferencias de arquitectura entre operaciones CLI y script empaquetado |
| Erodenn/godot-mcp-runtime | Inyección temporal de Autoload para pruebas runtime, captura, inputs y ejecución GDScript | Node.js 20+ y configuración de ruta; la inyección runtime requiere inspeccionar cuidadosamente el alcance de ejecución |
| Godot AI (hi-godot) | MCP dual stdio/HTTP, docks y herramientas de editor; simulación de gamepad | El PDF indica que C# se limita a edición textual sin compilación .NET |
| IvanMurzak Godot-MCP | Integración C#/.NET, reflexión y consultas/mutaciones RQL | Requiere Godot .NET, .NET 8 y dependencias NuGet |
| AI Copilot | Agente nativo de editor, rondas de edición, diffs y ejecución/captura | Godot 4.7+ según el documento; validar aislamiento real y alcance de API |
| Orca | Modos Plan de solo lectura y Work con aprobación por cambio | La aprobación humana es parte central del flujo descrito |
| AI Assistant Hub | Asistentes del editor, foco en modelos locales | Confirmar mantenimiento y compatibilidad de cada backend |
| GDLLM / Flatten for LLM | Harness de LLM y empaquetado de contexto del proyecto | Preparar contexto no equivale a validar cambios ni a ejecutar el motor |

**[E-PDF]** Las páginas 3–8 incluyen una matriz comparativa y tablas de herramientas. El documento reporta 42+ herramientas para Ziva, 46 herramientas/120+ operaciones para Godot AI y cifras de 163–187 herramientas para Godot MCP Pro, dependiendo del corte o catálogo citado.

### 4.2 Lectura crítica de la comparación

- **[F-PDF]** Los catálogos, requisitos y capacidades no son homogéneos: algunas cifras cuentan herramientas, otras operaciones o familias.
- **[I]** El número bruto de herramientas no es una métrica suficiente de calidad. Importan la semántica de las operaciones, validación de argumentos, idempotencia, reversibilidad, trazabilidad, cobertura de pruebas y límites de permisos.
- **[P]** Las versiones, precios, licencias y compatibilidades deben comprobarse contra repositorios y páginas oficiales en el momento de elegir. Una tabla fechada no garantiza que el proyecto siga activo ni que el binario publicado corresponda al código fuente.
- **[I]** Un modo de solo lectura y un sistema de aprobación por mutación son controles valiosos, pero no sustituyen aislamiento de procesos, límites de filesystem, validación de comandos ni auditoría de resultados.
- **[H]** Para una primera prueba de concepto conviene preferir un puente pequeño, observable y reversible antes que habilitar un catálogo extenso de operaciones.

### 4.3 Seguridad y gobernanza de herramientas MCP

**[I]** Un servidor conectado al proyecto puede modificar código, escenas y recursos o ejecutar procesos. Por tanto, debe tratarse como una superficie de autoridad, no como un simple plugin conversacional.

Controles propuestos:
1. Separar lectura de escritura y aplicar mínimo privilegio.
2. Restringir rutas a un workspace explícito; impedir escapes por rutas relativas o enlaces simbólicos.
3. Exigir aprobación humana para borrados, exportaciones, cambios de configuración, instalación de dependencias y operaciones fuera del proyecto.
4. Registrar herramienta, argumentos, actor, archivo afectado, diff y resultado.
5. Ejecutar pruebas en una copia o rama aislada.
6. Limitar duración, procesos, red y recursos.
7. Mantener rollback mediante commits y/o UndoRedo.
8. No exponer secretos del entorno a prompts ni logs.

Estos controles son recomendaciones de Auditoría, no capacidades verificadas de cada producto.

## 5. Bucle cerrado de diagnóstico y reparación

**[F-PDF]** En las páginas 8–9 se describe un caso de Ziva con Claude Code y Godot 4.7.2 sobre Star Catcher:

1. Diagnóstico: consulta de información del proyecto y ejecución de `main.tscn` durante 4.000 ms, con `ui_right` mantenido durante 2.000 ms.
2. Observación: error de nodo `%ScoreLabel` no encontrado desde `/root/Main`, seguido de acceso a instancia nula.
3. Reparación: cambio de `@onready var score_label: Label = %ScoreLabel` a `$HUD/%ScoreLabel`.
4. Verificación: nueva ejecución y captura donde aparece `Score: 1`, sin errores reportados.

**[E-PDF]** Es una demostración concreta del ciclo ejecutar-observar-corregir-ejecutar, no una evaluación estadística de tasa de éxito.

**[I]** El ejemplo respalda la utilidad de conectar el agente al motor: el error solo se vuelve evidente en el contexto de escena y ejecución. Sin embargo, la captura de un único estado final no demuestra que todas las rutas de interacción funcionen.

**[H]** La verificación de agentes de desarrollo debería combinar:
- pruebas unitarias de lógica;
- pruebas de escena y carga de recursos;
- pruebas de integración;
- pruebas de interacción con entradas deterministas;
- inspección de errores y warnings;
- aserciones sobre el estado del juego;
- pruebas de regresión sobre escenarios previos.

**[P]** Se necesita conocer si el caso de estudio fue reproducido independientemente, qué commit exacto se probó, si el error estaba aislado y qué pruebas adicionales se ejecutaron.

## 6. Navegación, evasión y escalabilidad

### 6.1 Navegación individual

**[F-PDF]** El documento presenta un ejemplo de `CharacterBody3D` y `NavigationAgent3D` que:
- espera a que el mapa de navegación esté sincronizado;
- ajusta el objetivo a un punto navegable;
- obtiene el siguiente punto de ruta;
- suaviza velocidad horizontal mediante aceleración;
- usa `velocity_computed` cuando RVO está activo;
- llama `move_and_slide()` con la velocidad segura.

También indica que un `NavigationObstacle3D` dinámico debe publicar su velocidad real para que RVO pueda anticipar el movimiento del obstáculo.

**[I]** La sincronización del mapa y la separación entre ruta global y evasión local son aspectos importantes. Aun así, el ejemplo es un patrón ilustrativo, no una implementación universal. Deben probarse mapas vacíos, objetivos fuera de la malla, regiones desconectadas, agentes atascados, cambios de mapa y obstáculos móviles.

**[P]** Verificar contra la documentación de la versión objetivo las APIs exactas usadas en el snippet, en especial la comprobación de regiones/iteración del mapa y las condiciones de disponibilidad del NavigationServer.

### 6.2 Optimización del subsistema de navegación

**[F-PDF]** El documento resume recomendaciones atribuidas a la documentación de Godot 4.6:
- no hornear navegación desde mallas visuales complejas que obliguen a recuperar datos desde GPU;
- preferir geometría de colisión simple;
- hornear en segundo plano con una copia del NavigationMesh;
- ajustar resolución de voxelización y tipo de partición;
- evitar escalar nodos fuente para el horneado;
- usar recursos binarios y herramientas propias en terrenos grandes cuando corresponda;
- evitar recalcular rutas o reasignar `target_position` cada frame;
- escalonar consultas y evitar pruebas redundantes de alcanzabilidad;
- observar el costo de polígonos/aristas y la sincronización del mapa.

**[I]** La optimización debe basarse en perfiles de la escena real. No es correcto traducir estas recomendaciones en reglas absolutas sin considerar topología, frecuencia de cambios, número de agentes y plataforma.

### 6.3 Flow Fields: evidencia de escalabilidad

**[E-PDF]** El gráfico de la página 13 y el texto de las páginas 13–14 citan mediciones de Vav Labs en Godot 4.6. Para 500 agentes:
- consultas individuales con `AStarGrid2D.get_id_path()` por agente y frame: mediana de 670,291 ms por cuadro; p95 4.581,507 ms; p99 4.870,586 ms; máximo 5.770,735 ms;
- campo de flujo compartido programado: mediana 2,028 ms; p95 6,849 ms; p99 8,190 ms; máximo 9,956 ms.

Para el campo compartido, el documento informa:
- 5.000 agentes: mediana 2,622 ms;
- 10.000 agentes: mediana 5,022 ms;
- 20.000 agentes: mediana 9,541 ms, p99 14,408 ms y 0,14% de cuadros por encima de 16,6 ms.

El método reconstruye el campo bajo un presupuesto fijo de pasos por cuadro, mientras los agentes siguen leyendo el último campo completado.

**[I]** La evidencia ilustra una ventaja potencial grande cuando muchos agentes comparten destino o estructura de navegación. No demuestra que Flow Fields sean superiores en todos los escenarios: los agentes con objetivos individuales, geometría dinámica o necesidades de precisión local pueden requerir otros métodos o un enfoque híbrido.

**[P]** Para reutilizar esas cifras como compromiso de rendimiento hay que reproducir el benchmark: hardware, resolución de grilla, implementación, cantidad de obstáculos, costo de reconstrucción, distribución de agentes, frecuencia de cambio de objetivo, warm-up y configuración de exportación. El resultado de un artículo de proveedor/tercero no es una garantía para cualquier juego.

**[H]** Arquitectura candidata: Flow Field para multitudes con objetivos compartidos y rutas individuales para entidades heroicas o de alta prioridad; validar el umbral de conmutación con mediciones propias.

## 7. Decisión simbólica: BT, State Charts, GOAP y Utility AI

### 7.1 LimboAI

**[F-PDF]** LimboAI combina Behavior Trees y LimboHSM; su núcleo C++ puede usarse como módulo o GDExtension y admite tareas personalizadas en GDScript. Los árboles se guardan como recursos y se ejecutan mediante BTPlayer. El documento destaca Blackboard, scopes, subárboles y depuración visual.

**[I]** Su orientación basada en recursos puede reducir la proliferación de nodos en escenas y resultar atractiva para árboles grandes o muchos NPCs. La elección debe considerar exportaciones por plataforma, binarios disponibles y curva de aprendizaje.

### 7.2 Beehave

**[F-PDF]** Beehave se describe como implementación en GDScript basada en nodos. Sus nodos devuelven SUCCESS, RUNNING o FAILURE; incluye Selector/Sequence, variantes Star, decoradores, paralelo y herramientas de depuración.

**[I]** Es atractivo para prototipos y equipos que prefieren lógica visible en el árbol de escena. El costo potencial es la cantidad de nodos y evaluación en GDScript. El dato comunitario de ~100 agentes citado por el PDF corresponde a un reporte histórico en Godot 3.2 y no debe tratarse como benchmark vigente de Godot 4.7.

### 7.3 Godot State Charts

**[F-PDF]** State Charts proporciona estados atómicos, compuestos, paralelos y de memoria, con transiciones por eventos, guardas declarativas y cola transaccional. El código interactúa con el nodo StateChart mediante eventos y propiedades de expresión.

**[I]** Es apropiado cuando el problema central es la gestión explícita de estados, subestados y comportamientos ortogonales. No reemplaza automáticamente a GOAP ni a Behavior Trees: organiza transiciones, no planifica por sí solo secuencias emergentes largas.

### 7.4 GOAP

**[F-PDF]** GOAP representa el mundo mediante variables de estado y acciones con precondiciones, efectos y costos. El documento menciona implementaciones GDScript y un plugin con planificación A*, encadenamiento hacia atrás, prioridades, replanificación y depuración.

**[I]** Puede ser útil cuando el agente debe construir planes variables para alcanzar objetivos a partir de acciones disponibles. El espacio de búsqueda crece con acciones y estados; requiere controlar costos, profundidad, ciclos, relevancia y frecuencia de replanificación.

### 7.5 Utility AI

**[F-PDF]** Utility AI puntúa opciones mediante consideraciones continuas y curvas de respuesta. El PDF destaca una GDExtension C++ con NQS y presupuesto temporal, además de alternativas GDScript.

**[I]** Es útil cuando las acciones compiten por conveniencia gradual —hambre, amenaza, distancia, recursos— y no existe una prioridad rígida simple. Deben inspeccionarse curvas, normalización, sensibilidad y estabilidad para evitar oscilaciones o comportamientos dominados por una sola consideración.

### 7.6 Composición de paradigmas

**[I]** Los paradigmas no son mutuamente excluyentes. Una arquitectura candidata podría usar:
- State Chart para macroestados (explorar, combatir, huir);
- Utility AI para seleccionar intención dentro de un estado;
- Behavior Tree para ejecutar la intención;
- navegación/steering para movimiento;
- GOAP solo donde sea necesario planificar cadenas de acciones con precondiciones y efectos.

**[H]** La composición debe justificarse por complejidad real; combinar frameworks por anticipación puede aumentar acoplamiento y dificultar depuración.

## 8. Aprendizaje por refuerzo y despliegue ONNX

### 8.1 Arquitectura Python–Godot

**[F-PDF]** Godot RL Agents conecta el motor con algoritmos de entrenamiento Python mediante TCP y un nodo Sync. El documento enumera StableBaselines3, Sample Factory, Ray RLlib y CleanRL; entornos 2D/3D, memoria LSTM/atención, ejecución paralela y aceleración de simulación.

El flujo descrito incluye:
1. añadir AIController2D/3D al personaje;
2. inicializarlo con el actor;
3. definir observaciones normalizadas en `get_obs()`;
4. acumular recompensas en `get_reward()`;
5. definir espacio de acciones y aplicar `set_action()`;
6. reiniciar episodios y manejar `needs_reset`;
7. configurar sensores como RayCastSensor3D y PositionSensor3D.

**[I]** La definición del espacio de observación y de la recompensa es una decisión de modelado, no un detalle de integración. Observaciones incompletas, escalas inconsistentes o recompensas mal diseñadas pueden generar políticas frágiles aunque el entrenamiento converja.

### 8.2 Despliegue ONNX

**[F-PDF]** El documento describe exportar el modelo a `.onnx` y ejecutar inferencia en Godot .NET mediante ONNX Runtime, con tensores de observación y estado recurrente. Advierte que no todas las plataformas de exportación soportan el runtime C#.

**[I]** Hay que separar claramente:
- entorno de entrenamiento;
- artefacto del modelo;
- runtime de inferencia;
- plataforma de distribución;
- pre/postprocesamiento de observaciones y acciones.

El modelo no es intercambiable si cambia el orden, dimensión, normalización o semántica del vector de observación.

**[P]** Verificar compatibilidad por plataforma, arquitectura CPU, versión de ONNX Runtime, tamaño del modelo, latencia y consumo de memoria. También probar que el preprocesamiento en producción reproduce el usado durante entrenamiento.

## 9. LLMs locales y NPCs conversacionales

### 9.1 NobodyWho y alternativas

**[F-PDF]** El documento presenta NobodyWho como GDExtension Rust que envuelve llama.cpp y ONNX Runtime, ejecuta modelos GGUF localmente y ofrece capacidades de chat, tool calling, audio e imagen. Enumera soporte de escritorio y Android, con ausencia de iOS/Web y de Windows ARM64 según el corte estudiado. Describe licencia EUPL-1.2 y condiciones de uso comercial.

También compara:
- Godot LLM/GDLlama, con nodos para llama.cpp, embeddings, visión y base vectorial, pero con actividad de repositorio que el documento considera antigua;
- Player2 AI NPC Plugin, dependiente de nube, cuenta y créditos;
- SDK comunitario de Inworld, listado sobre una plataforma que el PDF señala como retirada.

**[I]** La selección depende de latencia, memoria, GPU, distribución, licencia, privacidad, soporte de plataforma, tamaño del modelo y mantenimiento real. “Local” no significa automáticamente viable en el hardware mínimo del público objetivo.

### 9.2 Tool calling y latencia

**[F-PDF]** NobodyWho genera gramáticas estructuradas desde firmas tipadas de GDScript, valida marcadores especiales de formato y evita ejecutar llamadas truncadas. El PDF reporta que la restricción gramatical puede aumentar el TTFT:
- Qwen3 0.6B: 20 ms sin gramática frente a 240 ms con gramática;
- Qwen3 4B: 140 ms frente a 250 ms.

También recoge advertencias sobre bucles de pensamiento en algunas versiones de Qwen y sobre la necesidad de ajustar parámetros y contexto.

**[I]** Tool calling tipado reduce errores de formato, pero no convierte una solicitud del modelo en una acción segura. El juego debe validar autorización, estado, límites y efectos de cada herramienta. La latencia de primer token debe medirse en el hardware real y con la gramática y modelo que se distribuirán.

### 9.3 Verdad narrativa y autoridad determinista

**[F-PDF]** El documento cita experiencias comunitarias donde un NPC LLM puede mostrar complacencia y abandonar la verdad narrativa bajo presión del jugador. Recomienda mantener hechos, secretos y reglas de negocio en código determinista y utilizar el LLM para verbalizar o solicitar operaciones validadas.

**[I]** Este es uno de los principios de mayor importancia para diseño de sistemas: el modelo generativo no debe ser la fuente de verdad del mundo. Puede producir lenguaje, pero la autoridad sobre inventario, misión, secretos, combate, economía y consecuencias debe permanecer en sistemas deterministas.

**[H]** Patrón candidato: estado narrativo autoritativo → política de permisos → selección de hechos permitidos → generación de respuesta → validación de tool calls → ejecución determinista → registro de resultado. Se deben probar prompt injection, insistencia, contradicciones, alucinación de hechos, llamadas repetidas y acciones fuera de contexto.

## 10. Principios arquitectónicos extraídos

El PDF recomienda GDScript 2.0 con tipado estático, `class_name`, composición de nodos, señales para comunicación ascendente, Autoloads limitados a servicios globales y asignación de propiedades antes de `add_child()`.

Auditoría organiza los principios en tres grupos:

### 10.1 Principios de ingeniería
- Código y escenas deben inspeccionarse y validarse dentro de la versión real del motor.
- Mantener reglas persistentes de proyecto para reducir errores de versión y estilo.
- Preferir cambios pequeños, revisables y reversibles.
- Registrar evidencia de ejecución y pruebas; no equiparar “sin error visible” con aceptación funcional.

### 10.2 Principios de agentes runtime
- Separar percepción, decisión, navegación, ejecución y presentación.
- Usar técnicas deterministas cuando sean suficientes.
- Reservar RL para comportamientos cuya política sea difícil de especificar manualmente y pueda evaluarse con recompensas.
- Mantener el LLM fuera de la autoridad sobre reglas y estado verdadero del juego.
- Presupuestar cómputo y medir en el hardware objetivo.

### 10.3 Principios de gobernanza
- Separar permisos de agentes de desarrollo y agentes runtime.
- Exigir autorización proporcional al impacto de la operación.
- Mantener trazabilidad de acciones, cambios y resultados.
- Definir un criterio de aceptación observable por cada tarea.

## 11. Preguntas abiertas y riesgos de evidencia

1. ¿Qué herramientas MCP siguen mantenidas y compatibles con la versión exacta de Godot que se utilizará?
2. ¿Qué capacidades son ejecutables sin nube, cuenta externa o telemetría?
3. ¿Qué servidor puede operar en un entorno aislado, con mínimo privilegio y pruebas CI?
4. ¿Qué benchmark propio representa la carga real de agentes y geometría del juego?
5. ¿Cuál es el umbral medido para usar navegación individual, Flow Fields o un híbrido?
6. ¿Qué framework simbólico ofrece la mejor relación entre expresividad, depuración, rendimiento y mantenimiento?
7. ¿Qué tareas justifican RL frente a una política determinista?
8. ¿Qué plataformas pueden distribuir la inferencia ONNX y los modelos locales con latencia aceptable?
9. ¿Cómo se protegen tool calls, secretos narrativos y acciones económicas o irreversibles?
10. ¿Qué pruebas demuestran que un NPC mantiene su verdad narrativa bajo presión adversarial?

### Riesgos de interpretación detectados

- **Cifras de catálogo:** 163 frente a 187 herramientas para Godot MCP Pro aparecen en distintos cortes o fuentes; no deben presentarse como una cifra única estable.
- **Compatibilidad:** el documento mezcla versiones de Godot y fechas de publicación. Las afirmaciones de compatibilidad necesitan verificación al fijar versión.
- **Benchmarks:** los resultados de Flow Fields son evidencia de un benchmark externo concreto, no una promesa de rendimiento universal.
- **Comparación histórica:** la cifra comunitaria sobre Beehave en Godot 3.2 no permite comparar directamente con herramientas actuales.
- **Proveedores:** métricas, soporte y ventajas publicados por los propios proyectos requieren contraste independiente.
- **Referencias:** la bibliografía contiene enlaces oficiales, repositorios, artículos de proveedores, comunidad y tutoriales; no todas las fuentes tienen el mismo peso probatorio.
- **Ejemplos de código:** deben compilarse y probarse en el proyecto objetivo antes de adoptarse.

## 12. Conclusiones de Auditoría

1. **[I] No existe un agente universal para Godot.** El desarrollo asistido y la autonomía runtime son dominios distintos, y dentro de runtime existen problemas que requieren técnicas diferentes.
2. **[I] La observabilidad cierra una brecha central.** MCP de nivel motor puede permitir que el agente contraste sus cambios con el comportamiento del proyecto, pero la verificación debe ser más amplia que una captura final.
3. **[I] La escalabilidad depende de evitar trabajo redundante.** Flow Fields son prometedores cuando existe un destino compartido; la evidencia requiere reproducción antes de fijar objetivos de rendimiento.
4. **[I] Las arquitecturas simbólicas son complementarias.** State Charts, BT, GOAP y Utility AI responden a problemas distintos y pueden combinarse si el diseño lo justifica.
5. **[I] RL añade un ciclo de entrenamiento y despliegue separado.** La política debe conservar compatibilidad entre observaciones de entrenamiento y producción.
6. **[I] Los LLM deben ser una capa de lenguaje y razonamiento acotado, no la autoridad del mundo.** El estado verdadero y las acciones deben validarse fuera del modelo.
7. **[I] Gobernanza y seguridad son parte de la arquitectura.** Las herramientas que escriben archivos o ejecutan el motor requieren mínimo privilegio, autorización, aislamiento, reversibilidad y logs.

### Recomendación de investigación

Antes de elegir herramientas o construir el ecosistema multiagente, definir:
- el caso de uso del videojuego;
- el tipo y cantidad de agentes runtime;
- lenguaje y versión de Godot;
- plataformas objetivo;
- nivel de autonomía del agente de desarrollo;
- política de permisos y aprobación;
- métricas y pruebas de aceptación.

La selección tecnológica debe ser consecuencia de esos requisitos, no el punto de partida.

## 13. Referencias del documento fuente

Las referencias siguientes conservan la numeración del PDF *Agentes de Desarrollo en Godot.pdf*. Se listan las fuentes más directamente relacionadas con las afirmaciones principales; la bibliografía completa está en las páginas 23–26 del PDF.

1. Summer Engine, “Qué es Godot MCP? Una explicación clara para 2026”, https://www.summerengine.com/es/blog/what-is-godot-mcp
2. LimboAI, repositorio y documentación, https://github.com/limbonaut/limboai
3. Godot RL Agents, https://github.com/edbeeching/godot_rl_agents
4. NobodyWho, documentación Godot, https://docs.nobodywho.ooo/godot/
5. Ziva, servidor MCP para Claude Code y Cursor, https://ziva.sh/blogs/godot-mcp-server-claude-code-cursor
6. Vav Labs, benchmark de navegación y Flow Fields, https://vav-labs.com/blog/moving-10000-agents-in-godot/
7. Summer Engine, panorama de plugins Godot AI, https://www.summerengine.com/blog/godot-ai-plugin
10. Godot MCP Pro, Asset Library, https://godotengine.org/asset-library/asset/4961
15. Godot Docs, NavigationAgent3D, https://docs.godotengine.org/en/stable/classes/class_navigationagent3d.html
17. Beehave, Asset Library/Store y releases, https://github.com/bitbrain/beehave/releases/
18. Godot State Charts, https://github.com/derkork/godot-statecharts
19. GOAP, Godot Asset Library, https://godotengine.org/asset-library/asset/4888
20. Utility AI (GDExtension), Godot Asset Library, https://godotengine.org/asset-library/asset/2260
21. Godot RL Agents, implementación ONNXInference.cs, https://huggingface.co/datasets/edbeeching/godot_rl_FPS/blob/686ab1a4ddc45612a7feccf54b6397bf93930a40/addons/godot_rl_agents/onnx/csharp/ONNXInference.cs
23–24. NobodyWho, Asset Store y repositorio, https://github.com/nobodywho-ooo/nobodywho
25. bradypp/godot-mcp, https://github.com/bradypp/godot-mcp
26–28. IvanMurzak Godot-MCP y documentación técnica, https://ai-game.dev/docs/wiki/godot
35–39. Vav Labs, GDQuest y documentación oficial de optimización de navegación:
   - https://vav-labs.com/blog/3d-pathfinding-in-godot/
   - https://www.gdquest.com/library/intro_to_steering_behaviors/
   - https://docs.godotengine.org/en/4.6/tutorials/navigation/navigation_optimizing_performance.html
52–54. Implementaciones GOAP, Utility AI y Game AI Kit:
   - https://github.com/RodZill4/godot-goap
   - https://pennycook.itch.io/godot-utility-ai
   - https://godotengine.org/asset-library/asset/2260
63–67. Comparativa de NPCs y referencias de NobodyWho:
   - https://neocortex.link/blog/ai-npc-tools-for-godot
   - https://producthunt.com/products/nobodywho
   - https://www.reddit.com/r/godot/comments/1hcgjl5/nobodywho_local_llm_integration_in_godot/

**Nota de integridad bibliográfica:** los enlaces y la numeración se transcriben del PDF. Esta investigación no afirma haber abierto ni revalidado individualmente cada enlace. Para la decisión de implementación, se debe consultar la fuente primaria vigente y registrar fecha, versión y commit/tag.

---
**Cierre de Parte I:** investigación documental de Auditoría preservada como perspectiva independiente. No constituye selección final de herramientas, aprobación de arquitectura ni prueba de runtime.
