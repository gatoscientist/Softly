# Cierre de hilo y traspaso de continuidad — Investigación conjunta Godot

- **Fecha de cierre documental:** 2026-11-14
- **Proyecto:** investigación conjunta Auditoría × Softly sobre agentes para videojuegos en Godot
- **Estado:** fase documental cerrada; revisión de Softly solicitada; fase experimental aún no autorizada.
- **Síntesis canónica:** [SYN-20261114-001 — Parte II](../syntheses/2026-11-14-investigacion-conjunta-godot-parte-ii.md)

## 1. Qué queda preservado

Las investigaciones originales se mantienen separadas e intactas:

1. Auditoría — Parte I: `audsay/res/Investigacion_Auditoria_Godot_Parte_I.md`.
2. Softly — iniciativa Godot: `gatoscientist/Auditoria/Softlysay/res/Investigacion_Softly_Iniciativa_Godot.md` (repositorio Auditoría).

La síntesis conjunta Parte II integra ambos trabajos, distingue hechos documentales, evidencias, inferencias e hipótesis, registra discrepancias, omisiones, riesgos y preguntas pendientes. Los índices de investigación y síntesis ya apuntan al documento.

## 2. Resultado que no se debe perder

- Se distinguen dos dominios: agentes que desarrollan el proyecto y agentes runtime dentro del videojuego.
- La integración Engine-Level puede cerrar el ciclo de ejecución/observación, pero una captura o un arranque correcto no reemplazan pruebas funcionales.
- La propuesta de agentes especialistas de Softly es una hipótesis organizacional que requiere comparación con una línea base de agente generalista.
- Flow Fields, paradigmas simbólicos, RL/ONNX y LLM local deben evaluarse según el problema y las condiciones reales; no son soluciones universales.
- El estado verdadero, reglas y autorización de acciones runtime deben permanecer bajo autoridad determinista del juego.
- La cantidad de herramientas MCP y las cifras de benchmarks no bastan para elegir una solución; se necesitan pruebas reproducibles, compatibilidad y revisión de permisos.
- No se ha ejecutado benchmark ni se ha instalado/validado una herramienta como parte de esta fase.

## 3. Estado documental y referencias de commits

Los siguientes commits ya existían y fueron inspeccionados en el historial de GitHub al cerrar este hilo; no se recrean ni duplican:

| Entrega | Commit |
|---|---|
| Depósito Auditoría Parte I | `e783a534e135425a90736887f8fdd6aa3494f911` |
| Síntesis conjunta Parte II | `bd6007ca42ce8884e003f46e93324fa99df7e857` |
| Índice `research/README.md` | `02fb8caa79c499bd3cf662581e59e136e04797dd` |
| Índice `research/syntheses/README.md` | `317a93c6322371df2281b38fb7e8a29b8725c4ee` |

Este documento de cierre y traspaso se agrega para dejar una entrada explícita al siguiente hilo y evitar que la continuidad dependa del historial conversacional.

## 4. Qué debe hacer el siguiente hilo

**Primero: recibir y registrar la opinión de Softly.** La revisión solicitada debe contestar, con argumentos y referencias a los documentos:

1. ¿Qué conclusiones de Parte II considera correctas, incompletas o discutibles?
2. ¿Qué aportes de Softly quedaron subrepresentados o fueron interpretados incorrectamente?
3. ¿Qué puntos de Auditoría deberían modificar o restringir la propuesta multiagente?
4. ¿Qué contradicciones u omisiones nuevas detecta?
5. ¿Qué experimento mínimo recomienda y qué resultado lo refutaría?
6. ¿Qué preguntas requieren decisión del director antes de abrir la fase experimental?

La respuesta de Softly debe conservarse como artefacto independiente, no sobrescribir Parte I ni Parte II. Si cambia una conclusión, registrar el motivo, evidencia y versión afectada en una nueva revisión de síntesis.

**Después: esperar decisión del director.** No instalar plugins, crear agentes de producción, elegir stack ni iniciar benchmarks hasta contar con caso de uso, versión de Godot, lenguaje, plataforma, hardware, métricas y criterios de aceptación.

## 5. Próximo umbral de investigación

La fase experimental solo puede abrirse cuando exista un brief mínimo con:
- videojuego/caso de uso y comportamiento objetivo;
- versión exacta de Godot y GDScript/C#;
- plataformas y hardware objetivo;
- tareas permitidas a agentes constructores y límites de autoridad;
- escenarios runtime representativos;
- alternativas a comparar y línea base;
- métricas, pruebas, umbrales de aceptación y criterios de refutación;
- permisos, aislamiento, rollback y política de datos/licencias.

## 6. Regla de continuidad

No presentar como verificado aquello que solo está descrito en el PDF o inferido por los equipos. Mantener separadas las fuentes, interpretaciones, hipótesis y resultados experimentales. Toda conclusión nueva debe enlazar evidencia, fecha, versión y condiciones de reproducción.

---
**Cierre:** queda cerrada la integración documental de este hilo. La revisión de Softly es el siguiente insumo esperado; la decisión de abrir experimentación permanece en manos del director.
