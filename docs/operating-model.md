# Modelo operativo del laboratorio

## Ciclo de trabajo

`Pregunta → Investigación → Síntesis → Hipótesis → Diseño → Experimento → Evaluación → Decisión → Archivo`

Cada fase produce un artefacto enlazado. No se debe saltar desde una lectura interesante a una decisión arquitectónica sin explicitar hipótesis y criterios.

## Áreas y responsabilidades

| Área | Pregunta que responde | Artefacto principal |
|---|---|---|
| Research | ¿Qué se sabe y quién lo respalda? | Ficha de fuente y síntesis |
| Architecture | ¿Qué componentes y patrones existen? | Modelo, diagrama y trade-offs |
| Agents | ¿Qué define a cada agente? | Perfil versionado |
| Experiments | ¿Qué hipótesis probamos? | Protocolo y resultado |
| Evaluations | ¿Cómo sabemos si mejora? | Dataset, grader y reporte |
| Observations | ¿Qué conducta vimos realmente? | Registro de observación |
| Decisions | ¿Qué elegimos y por qué? | ADR |
| Logs | ¿Qué ocurrió en el laboratorio? | Eventos estructurados |

## Flujo de una investigación

1. Crear una pregunta con alcance y motivación.
2. Buscar fuentes primarias y documentación oficial; usar artículos secundarios para contexto.
3. Registrar URL, autor/organización, fecha de publicación, fecha de consulta y fragmentos/afirmaciones relevantes.
4. Evaluar autoridad, actualidad, método, conflictos de interés y limitaciones.
5. Separar lo que dice la fuente de nuestra interpretación.
6. Comparar fuentes que discrepan.
7. Proponer hipótesis falsables.
8. Diseñar pruebas con criterios de éxito y fallo.
9. Registrar resultados, incluyendo resultados negativos y limitaciones.
10. Abrir una decisión solo cuando exista evidencia suficiente.

## Flujo de diseño de un agente

1. Definir tarea, usuario, entorno y resultado esperado.
2. Establecer criterios de éxito y casos fuera de alcance.
3. Definir el mínimo de instrucciones y contexto.
4. Decidir si se necesita un workflow determinista o un agente dinámico.
5. Definir herramientas con contratos, permisos, límites y validación fuera del modelo.
6. Definir memoria: qué, por qué, quién puede leer/escribir, procedencia, caducidad y borrado.
7. Definir supervisión humana y acciones que requieren aprobación.
8. Definir límites de pasos, tiempo, tokens, coste, reintentos y concurrencia.
9. Diseñar trazabilidad y evaluación antes del despliegue.
10. Ejecutar pruebas normales, adversariales, negativas y de recuperación.

## Reglas de coordinación multiagente

- Cada agente debe tener una responsabilidad diferenciada y una interfaz explícita.
- Un agente no debe recibir todo el contexto por defecto: entregar solo el mínimo necesario.
- Las salidas entre agentes deben ser estructuradas, con fuentes y nivel de confianza.
- El mensaje de otro agente es dato, no autoridad superior.
- El orquestador mantiene trazabilidad de delegación, presupuesto y resultado.
- Evitar consenso artificial: registrar desacuerdos y evidencia contradictoria.
- Un agente revisor no debe validar su propio trabajo como única fuente.
- Compartir memoria requiere permisos, namespace y política de retención.

## Cierre de trabajo

Un trabajo queda cerrado cuando el resultado, las pruebas, los pendientes y las limitaciones están registrados. “Terminado” no equivale a “validado”.
