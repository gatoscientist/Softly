# SYN-20261114-001 — Investigación conjunta Godot: contraste e integración de Auditoría y Softly (Parte II)

- **Fecha:** 2026-11-14
- **Equipos:** Auditoría y Softly
- **Fuente técnica común:** Agentes de Desarrollo en Godot.pdf (26 páginas)
- **Investigación Auditoría:** [Parte I](../../audsay/res/Investigacion_Auditoria_Godot_Parte_I.md)
- **Investigación Softly:** [Investigación Softly — iniciativa Godot](https://github.com/gatoscientist/Auditoria/blob/main/Softlysay/res/Investigacion_Softly_Iniciativa_Godot.md)
- **Estado:** síntesis documental integrada; no equivale a validación experimental de herramientas ni a aprobación de arquitectura.

## 1. Resumen ejecutivo

Auditoría y Softly estudiaron el mismo documento, Agentes de Desarrollo en Godot.pdf, pero produjeron entregables con énfasis y profundidad diferentes.

- **Softly** construyó una lectura de conjunto: separó agentes que desarrollan el videojuego de agentes autónomos que operan dentro de él; destacó el bucle cerrado de ingeniería; interpretó las técnicas runtime como componentes complementarios; y propuso una organización multiagente futura junto con preguntas de coordinación aún abiertas.
- **Auditoría** desarrolló un análisis técnico más granular: conservó el inventario de herramientas, capacidades y restricciones; examinó navegación y Flow Fields, frameworks de decisión, RL/ONNX y LLM locales; y explicitó límites probatorios, riesgos de seguridad, condiciones de adopción y verificaciones pendientes.

La integración no consiste en sumar dos confirmaciones independientes de los mismos hechos: ambas investigaciones dependen del mismo PDF. Su valor conjunto está en la complementariedad analítica. Softly aporta una abstracción organizadora y una hipótesis de ecosistema multiagente; Auditoría aporta detalle técnico, crítica de evidencia y condiciones de implementación.

**Conclusión central:** Godot puede ser el punto de encuentro de dos ecosistemas de agentes, pero sus autoridades deben permanecer separadas: agentes de ingeniería con permisos sobre proyecto/editor y agentes runtime con APIs acotadas sobre el mundo del juego. La arquitectura runtime debe componerse por necesidad —navegación, decisión, RL o lenguaje— y mantener el estado verdadero y las reglas de negocio bajo control determinista.

No se selecciona todavía un plugin, framework ni topología multiagente definitiva. Faltan requisitos del juego, validación de compatibilidad, pruebas de rendimiento, pruebas de seguridad y criterios de aceptación.

## 2. Procedencia, alcance y método de contraste

### 2.1 Fuentes comparadas

1. **PDF común:** Agentes de Desarrollo en Godot.pdf, 26 páginas. Es la fuente primaria compartida por ambos equipos para esta fase.
2. **Softly:** Auditoria/Softlysay/res/Investigacion_Softly_Iniciativa_Godot.md. El propio documento declara que conserva una transcripción de la respuesta investigativa de Softly en su hilo.
3. **Auditoría:** Softly/audsay/res/Investigacion_Auditoria_Godot_Parte_I.md. Análisis documental detallado elaborado para esta fase.

### 2.2 Qué significa “evidencia” en esta síntesis

- **Hecho del PDF:** afirmación que el documento fuente contiene.
- **Evidencia citada por el PDF:** ejemplo, tabla, gráfico, snippet o referencia usado en el documento. Su existencia en el PDF es verificable; la validez externa de la afirmación puede requerir reproducción.
- **Aporte interpretativo de Softly:** lectura, organización o hipótesis formulada por Softly a partir del PDF.
- **Aporte analítico de Auditoría:** contraste técnico, inferencia o cautela desarrollada por Auditoría a partir del mismo PDF.
- **Inferencia conjunta:** conclusión que surge al relacionar ambos análisis.
- **Hipótesis pendiente:** propuesta que requiere prueba y puede ser refutada.

### 2.3 Limitación de independencia

Las dos investigaciones no constituyen dos fuentes experimentales independientes. Ambas leyeron el mismo PDF y no documentan una reproducción independiente de benchmarks ni pruebas propias de los plugins. La coincidencia entre equipos demuestra convergencia interpretativa, no replicación empírica.

## 3. Coincidencias principales

### 3.1 Dos dominios de agentes

**Coincidencia:** ambos equipos separan:
- agentes que ayudan a construir, modificar, ejecutar y depurar proyectos Godot;
- agentes autónomos que perciben, deciden, navegan, aprenden o conversan dentro del juego.

**Base documental:** el PDF abre con esta distinción y desarrolla MCP/copilotos por un lado y navegación, decisión, RL y LLM runtime por otro. Softly la convierte en los diagramas conceptuales “Agente → Proyecto → Motor → Verificación” y “Percepción → Decisión → Acción → Mundo virtual”. Auditoría añade que los dos dominios deben tener permisos, ciclos de vida y autoridades diferentes.

**Inferencia conjunta:** compartir motor no significa compartir autoridad. Un agente de desarrollo puede tener capacidad de editar archivos o ejecutar procesos; un NPC no debe heredar esos privilegios. Las interfaces entre ambos deben ser explícitas y mínimas.

### 3.2 La verificación empírica importa más que la generación de código

**Coincidencia:** los equipos destacan el bucle cerrado de diagnóstico, reparación y verificación.

**Evidencia del PDF:** el caso Star Catcher de las páginas 8–9 describe un error de ruta de nodo ScoreLabel, una corrección en main.gd y una segunda ejecución que muestra Score: 1.

**Aporte Softly:** interpreta el caso como el salto de “producir código” a “verificar comportamiento”.

**Aporte Auditoría:** advierte que un fotograma final sin errores visibles no demuestra cobertura funcional completa. Propone combinar pruebas unitarias, de escena, integración, interacción, regresión y aserciones de estado.

**Inferencia conjunta:** la capacidad de observar el motor es un requisito importante para un agente de ingeniería fiable, pero la observabilidad debe traducirse en criterios de aceptación explícitos. “El juego arrancó” y “la funcionalidad está correcta” son afirmaciones diferentes.

### 3.3 Las técnicas runtime son complementarias

**Coincidencia:** ambos equipos rechazan la idea de que una sola técnica de IA resuelva todos los comportamientos.

- State Charts administra estados y transiciones.
- Behavior Trees organiza tareas y comportamiento reactivo.
- GOAP construye planes a partir de precondiciones, efectos y costos.
- Utility AI puntúa opciones de forma continua.
- Navegación y steering resuelven movimiento y evasión.
- RL aprende políticas desde interacción y recompensas.
- LLMs aportan lenguaje e interfaces conversacionales.

**Aporte Softly:** propone una lectura funcional de los motores de decisión y señala que no son necesariamente excluyentes.

**Aporte Auditoría:** agrega condiciones de composición, costos de búsqueda, rendimiento, depuración y riesgos de combinar frameworks sin necesidad.

**Inferencia conjunta:** seleccionar por problema y no por moda. La composición puede ser útil, pero cada capa adicional debe justificar su costo y su interfaz.

### 3.4 La verdad del juego no debe depender del LLM

**Coincidencia:** ambos equipos identifican la complacencia de modelos generativos como riesgo narrativo y recomiendan que las reglas del juego permanezcan en sistemas deterministas.

**Evidencia del PDF:** la sección de NPCs describe casos comunitarios donde un personaje puede abandonar un secreto bajo presión conversacional y recomienda que el estado verdadero se mantenga en código, mientras el LLM verbaliza o solicita operaciones validadas.

**Aporte Softly:** formula que el LLM puede interpretar y conversar, pero no debe ser la autoridad sobre reglas fundamentales.

**Aporte Auditoría:** deriva controles adicionales: API acotada, autorización, validación de estado, límites de efectos, protección frente a prompt injection y registro de tool calls.

**Inferencia conjunta:** el modelo puede proponer una acción o respuesta; el juego decide si esa acción está permitida y cuál es el resultado real.

## 4. Diferencias de énfasis e interpretación

| Tema | Softly | Auditoría | Lectura integrada |
|---|---|---|---|
| Propósito | Entender el ecosistema y preparar el diseño de un equipo constructor de juegos | Descomponer tecnologías, evidencia, restricciones y riesgos | Visión de sistema + base técnica para decisiones |
| MCP | Diferencia File-Level y Engine-Level y prioriza el bucle cerrado | Detalla productos, versiones, protocolos, limitaciones y controles | No elegir por cantidad de herramientas; evaluar observabilidad, permisos y reversibilidad |
| Herramientas | Inventario resumido de diez soluciones | Matriz más granular, con compatibilidad, costos y advertencias | Inventario exploratorio, sujeto a validación de vigencia |
| Navegación | Explica Flow Fields como solución a cálculos redundantes | Examina cifras, percentiles, presupuesto incremental y límites del benchmark | Técnica prometedora en destinos compartidos; reproducir en la carga propia |
| Decisión simbólica | Resumen conceptual de BT, State Charts, GOAP y Utility AI | Añade tradeoffs, arquitectura y criterios de composición | Paradigmas complementarios; evitar sobrearquitectura |
| RL | Resume flujo Python → entrenamiento → ONNX | Añade observaciones, sensores, recompensa, tensores y límites de plataforma | El contrato de observación/acción debe mantenerse idéntico entre entrenamiento y producción |
| LLM local | Destaca capacidades y verdad narrativa determinista | Añade licencia, plataformas, gramáticas, TTFT y seguridad de tools | Evaluar hardware, latencia, licencias y autoridad de acciones |
| Multiagente | Propone roles (coordinación, código, escenas, visual, QA) y preguntas abiertas | No propone un organigrama como conclusión técnica; enfatiza límites y verificabilidad | La propuesta de Softly es una hipótesis organizativa, no resultado demostrado por el PDF |
| Evidencia | Reconoce que compatibilidad y cifras requieren verificación | Separa hechos documentales, evidencia citada, inferencias e hipótesis | Mantener un registro de procedencia y reproducibilidad por afirmación |

### 4.1 Diferencia más importante

Softly extiende la investigación hacia la pregunta “¿cómo organizamos un equipo de agentes para desarrollar videojuegos?”. Esa pregunta no está resuelta por el PDF. Es una extrapolación útil para la iniciativa, pero debe conservarse como línea de investigación y no confundirse con una arquitectura probada.

Auditoría concentra el análisis en “¿qué componentes existen, qué problema resuelven, qué límites declaran y qué evidencia tenemos para elegirlos?”. Esta profundidad permite que la propuesta organizativa de Softly no se construya sobre supuestos técnicos invisibles.

## 5. Aportes complementarios que unifican la comprensión

### 5.1 Organización de un ecosistema de ingeniería

Softly propone roles candidatos:
- dirección y coordinación;
- agente de código;
- agente de escenas;
- agente visual;
- agente QA;
- Godot Engine como entorno de integración.

Auditoría agrega las propiedades que cada rol debería tener:
- contrato de entrada y salida;
- permisos mínimos;
- ámbito de archivos o recursos;
- herramientas explícitas;
- criterios de aceptación;
- registro de cambios;
- estrategia de rollback;
- pruebas que debe ejecutar o solicitar.

**Síntesis:** no basta con dividir agentes por especialidad. Se necesita un protocolo de coordinación que determine quién puede cambiar qué, cómo se comparten decisiones, cómo se resuelven conflictos y quién certifica el resultado.

### 5.2 Selección de arquitectura runtime

Softly explica qué aporta cada paradigma. Auditoría aclara cuándo puede ser razonable usarlo y qué costo introduce.

**Síntesis candidata, no decisión final:**
- State Charts para estados de alto nivel y transiciones explícitas.
- Utility AI para elegir prioridades cuando varias necesidades compiten continuamente.
- Behavior Tree para ejecutar secuencias reactivas modulares.
- GOAP para planificación de cadenas de acciones con precondiciones y efectos.
- NavigationAgent/RVO o Flow Fields según número de agentes, destino y geometría.
- RL cuando exista una tarea de control difícil de especificar y una métrica de recompensa defendible.
- LLM para lenguaje, interpretación contextual o interacción acotada, nunca como autoridad única del estado.

### 5.3 Ingeniería verificable

Softly identifica el bucle cerrado. Auditoría lo amplía con controles de proceso.

**Síntesis:** cada tarea agéntica debe tener un resultado observable y una prueba que pueda fallar. El agente no debe declararse exitoso solo por haber escrito archivos o terminado una llamada a herramienta.

## 6. Evidencias y fuerza probatoria

| Afirmación | Soporte disponible en el PDF | Fuerza actual | Qué falta |
|---|---|---|---|
| MCP File-Level no observa por sí solo el comportamiento runtime | Descripción arquitectónica de páginas 1–2 | Alta como distinción conceptual del documento | Probar límites de cada implementación concreta |
| Engine-Level permite ejecutar y observar escenas | Descripción y matriz de páginas 2–8; caso Star Catcher | Media-alta como capacidad descrita | Reproducir con herramientas y versiones elegidas |
| Ziva puede cerrar un ciclo de reparación | Caso Star Catcher, páginas 8–9 | Evidencia ilustrativa | Repeticiones, tasa de éxito y pruebas de regresión |
| Flow Fields pueden reducir el costo de navegación masiva | Gráfico y mediciones de Vav Labs, páginas 13–14 | Evidencia cuantitativa externa, contextual | Reproducir hardware, escena, algoritmo y carga |
| Los paradigmas simbólicos cubren problemas distintos | Descripción comparativa, páginas 14–17 | Alta como taxonomía técnica | Benchmark comparativo con un mismo escenario |
| Godot RL Agents conecta Godot y entrenamiento Python | Arquitectura, sensores y código descritos, páginas 18–19 | Media-alta como documentación citada | Ejecutar pipeline y verificar plataformas actuales |
| ONNX requiere considerar Godot .NET y soporte de plataforma | Descripción de despliegue, páginas 19–20 | Media | Matriz actual de builds y prueba en dispositivos objetivo |
| NobodyWho permite inferencia local y tool calling tipado | Documentación citada y sección técnica, páginas 20–21 | Media, dependiente de versión | Verificar release, modelos, licencia, latencia y seguridad |
| LLM puede abandonar verdad narrativa bajo presión | Reportes comunitarios citados, página 21 | Señal de riesgo cualitativa | Diseñar evaluación adversarial reproducible |
| Un equipo multiagente constructor mejorará desarrollo Godot | Propuesta de Softly | Hipótesis | Prototipo comparativo con métricas y línea base |

## 7. Contradicciones, omisiones y puntos que requieren cuidado

### 7.1 No hay contradicción directa entre los equipos

Las diferencias observadas son principalmente de profundidad y propósito. Softly no niega los detalles técnicos de Auditoría; los resume. Auditoría no refuta la propuesta organizativa de Softly; la delimita como hipótesis no demostrada por la fuente común.

### 7.2 Diferencias internas del propio PDF

1. **Catálogo de Godot MCP Pro:** se reportan 163 herramientas en un corte de Asset Library y hasta 187 en el sitio del proveedor. No consolidar como una cifra estable sin fecha y definición de conteo.
2. **Versiones:** el documento combina Godot 4.1, 4.2, 4.3, 4.4, 4.5, 4.6 y 4.7+, y releases de plugins en distintos meses. No extrapolar compatibilidad entre versiones.
3. **Benchmarks:** la sección de Flow Fields cita una prueba de terceros. Los resultados son dependientes de escenario, hardware y configuración.
4. **Beehave:** la referencia de rendimiento aproximado de 100 agentes corresponde a reportes comunitarios de Godot 3.2; no es una comparación contemporánea controlada.
5. **Licencias:** la licencia del motor, plugin, wrapper, modelos y dependencias puede ser distinta. Revisar el conjunto completo antes de distribuir.
6. **Código de ejemplo:** los snippets deben compilarse y verificarse en la versión de Godot elegida. El PDF no sustituye pruebas de integración.
7. **Fuentes heterogéneas:** el corpus incluye documentación oficial, repositorios, proveedores, tiendas, tutoriales y Reddit. No poseen la misma fuerza probatoria.

### 7.3 Omisiones compartidas

Ambos trabajos dejan abiertas cuestiones relevantes:
- protocolo formal de coordinación multiagente;
- modelo de memoria/contexto compartido y control de versiones;
- resolución de conflictos entre agentes;
- autorización y trazabilidad de acciones;
- evaluación comparativa de agentes constructores;
- definición de un caso de uso de videojuego concreto;
- presupuesto de CPU, GPU, memoria y latencia;
- compatibilidad por plataforma y requisitos de distribución;
- estrategia de observabilidad y telemetría;
- plan de pruebas adversariales para NPCs LLM;
- política de datos, privacidad y actualizaciones de modelos.

Auditoría añade que la seguridad de los puentes MCP merece una revisión específica: una herramienta capaz de escribir archivos o ejecutar procesos es una superficie privilegiada.

## 8. Implicaciones técnicas y arquitectónicas para la iniciativa

### 8.1 Arquitectura de ingeniería asistida

**Inferencia conjunta:** separar orquestación, especialidades y verificación. Un flujo inicial posible:

1. El coordinador recibe objetivo, alcance y criterios de aceptación.
2. Un agente de planificación descompone tareas y dependencias.
3. Agentes especialistas trabajan en ámbitos delimitados.
4. Los cambios se presentan como diffs y se integran en una rama de trabajo.
5. Un agente QA ejecuta pruebas con herramientas de motor.
6. Un responsable integra resultados, conflictos y evidencia.
7. El cierre registra commit, pruebas, limitaciones y pendientes.

**Hipótesis:** esta organización reducirá errores de coordinación frente a un agente monolítico. Debe compararse con una línea base simple.

### 8.2 Arquitectura runtime

**Inferencia conjunta:** mantener módulos separados:
- percepción/sensores;
- estado autoritativo del mundo;
- decisión simbólica;
- planificación opcional;
- navegación y locomoción;
- política RL opcional;
- diálogo LLM opcional;
- validación de acciones y eventos.

No todos los NPCs necesitan todos los módulos. La arquitectura debería permitir perfiles de agente distintos según importancia, costo y función.

### 8.3 Contratos entre módulos

**Hipótesis de diseño:** cada módulo expone entradas/salidas tipadas y no modifica directamente estado ajeno sin pasar por una interfaz controlada. Ejemplos:
- navegación recibe objetivo válido y entrega velocidad/destino/estado de ruta;
- decisión recibe observaciones y entrega intención;
- planificador entrega una secuencia de acciones con precondiciones;
- LLM entrega texto o una propuesta de tool call;
- validador de juego autoriza o rechaza la acción;
- estado del mundo confirma el resultado.

### 8.4 Seguridad y autoridad

La iniciativa debe diferenciar:
- permisos del agente que modifica el proyecto;
- permisos del agente que prueba el juego;
- permisos del NPC runtime;
- permisos del jugador;
- autoridad del estado determinista.

No deben compartir secretos ni herramientas por comodidad. La acción de mayor riesgo debe tener el control más estricto y evidencia posterior.

## 9. Hipótesis de investigación conjunta

Estas hipótesis no son conclusiones:

- **H-GODOT-01 — Especialización verificable:** un conjunto pequeño de agentes con contratos y ámbitos delimitados puede superar a un agente generalista en calidad de cambios y trazabilidad.
- **H-GODOT-02 — Verificación engine-level:** el acceso controlado a ejecución y observabilidad reduce defectos que sobreviven a revisión estática.
- **H-GODOT-03 — Arquitectura híbrida runtime:** combinar decisión simbólica con navegación y módulos especializados produce comportamientos más controlables que delegar toda decisión a un LLM.
- **H-GODOT-04 — Flow Fields por régimen de carga:** los campos compartidos mejoran el rendimiento cuando muchos agentes comparten destinos; la estrategia híbrida será superior cuando los objetivos sean heterogéneos.
- **H-GODOT-05 — Autoridad determinista:** mantener reglas y estado verdadero fuera del LLM reduce contradicciones narrativas y acciones no autorizadas.
- **H-GODOT-06 — Contratos y memoria:** un registro explícito de decisiones, permisos y dependencias reduce conflictos y repetición de trabajo entre agentes.

Cada hipótesis necesita variables, línea base, condiciones de prueba, métricas y criterio de refutación antes de ser considerada confirmada.

## 10. Plan de investigación pendiente

| Prioridad | Actividad | Evidencia/entregable esperado |
|---|---|---|
| P0 | Definir videojuego objetivo, versión Godot, lenguaje y plataformas | Brief técnico y criterios de aceptación |
| P0 | Verificar vigencia, licencia y compatibilidad de 2–3 herramientas MCP candidatas | Matriz fechada con tags/commits y pruebas mínimas |
| P0 | Diseñar política de permisos del agente de desarrollo | Matriz de capacidades, aprobaciones y límites |
| P1 | Reproducir el caso de bucle cerrado | Registro de ejecución, diff, errores y pruebas |
| P1 | Construir benchmark de navegación con carga representativa | FPS, p50/p95/p99, CPU, memoria y costo de actualización |
| P1 | Prototipar un NPC determinista y uno híbrido LLM | Suite de diálogo, seguridad y consistencia narrativa |
| P2 | Evaluar BT/State Charts/GOAP/Utility AI en un mismo escenario | Complejidad, latencia, depuración y mantenibilidad |
| P2 | Evaluar RL solo para una tarea delimitada | Curva de aprendizaje, generalización y costo de inferencia |
| P2 | Probar coordinación de agentes constructores | Calidad, tiempo, conflictos, retrabajo y trazabilidad |

## 11. Criterios para aceptar futuras conclusiones

Una afirmación técnica no debería promoverse a conclusión de proyecto sin:
1. fuente identificable y fecha;
2. versión exacta de Godot, plugin, modelo y dependencias;
3. condiciones de ejecución reproducibles;
4. métrica y criterio de éxito definidos;
5. evidencia primaria (log, commit, prueba, benchmark o documentación oficial);
6. limitaciones declaradas;
7. revisión de efectos colaterales y seguridad;
8. posibilidad de refutación.

Las comparaciones entre alternativas deben utilizar el mismo escenario y presupuesto, salvo que se declare expresamente por qué no son comparables.

## 12. Conclusiones finales

1. Softly y Auditoría coinciden en la separación de agentes de ingeniería y agentes runtime, y en la necesidad de verificar comportamiento, no solo generar código.
2. Softly aporta una visión sistémica y una propuesta de roles multiagente; Auditoría aporta el detalle técnico, las cautelas de evidencia y los controles necesarios para llevar esa propuesta a prueba.
3. Los paradigmas runtime son complementarios y deben seleccionarse por problema, no acumularse como catálogo.
4. Flow Fields, RL y LLM local son opciones especializadas con beneficios y costos; ninguna debe adoptarse sin pruebas en el escenario objetivo.
5. La autoridad del estado del juego debe seguir siendo determinista y separada de la generación conversacional.
6. Los agentes de ingeniería requieren mínimo privilegio, aprobación proporcional al riesgo, cambios reversibles y pruebas verificables.
7. La arquitectura multiagente para construir videojuegos sigue siendo una hipótesis de diseño. El siguiente paso es un brief y un prototipo medible, no una implementación general anticipada.

**Resultado de la fase:** se obtiene una base conceptual y técnica más completa que cualquiera de las dos lecturas por separado, sin fingir que la convergencia interpretativa constituye validación empírica. La investigación queda abierta a pruebas y refutación.

## 13. Referencias y trazabilidad

### Documentos comparados
- [Investigación Auditoría — Parte I](../../audsay/res/Investigacion_Auditoria_Godot_Parte_I.md)
- [Investigación Softly — iniciativa Godot](https://github.com/gatoscientist/Auditoria/blob/main/Softlysay/res/Investigacion_Softly_Iniciativa_Godot.md)
- Agentes de Desarrollo en Godot.pdf, 26 páginas, fuente compartida.

### Referencias técnicas destacadas del PDF
- Godot NavigationAgent3D: https://docs.godotengine.org/en/stable/classes/class_navigationagent3d.html
- Godot Navigation Performance: https://docs.godotengine.org/en/4.6/tutorials/navigation/navigation_optimizing_performance.html
- LimboAI: https://github.com/limbonaut/limboai
- Beehave: https://github.com/bitbrain/beehave
- Godot State Charts: https://github.com/derkork/godot-statecharts
- Godot RL Agents: https://github.com/edbeeching/godot_rl_agents
- NobodyWho: https://github.com/nobodywho-ooo/nobodywho
- Vav Labs Flow Fields benchmark: https://vav-labs.com/blog/moving-10000-agents-in-godot/
- Ziva MCP: https://ziva.sh/blogs/godot-mcp-server-claude-code-cursor

**Nota:** las referencias anteriores se conservan como trazabilidad de las fuentes citadas por el PDF. No se declara que cada enlace haya sido revalidado individualmente en esta fase.

---
**Fin de SYN-20261114-001.** Documento de síntesis; no reemplaza ni altera las investigaciones originales.
