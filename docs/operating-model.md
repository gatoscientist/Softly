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

## Conservación de hilos de conversación

El cierre de un hilo de conversación activa una obligación documental específica, independiente del cierre de una tarea técnica:

1. Crear un archivo Markdown por cada hilo cerrado en `logs/threads/`.
2. Conservar la historia del hilo: propósito, secuencia, instrucciones, decisiones, cambios, trabajo realizado, errores, pendientes y continuidad.
3. Incluir mensajes literales cuando estén disponibles y marcar claramente las partes resumidas o reconstruidas.
4. No exigir una transcripción literal del 100 %: prima la fidelidad histórica y contextual. No inventar contenido faltante ni incluir razonamiento privado oculto.
5. Registrar la fecha y hora de inicio y cierre con zona horaria America/Santiago. Si la hora exacta no está disponible, indicarlo expresamente como `hora-no-registrada`.
6. Nombrar el archivo con el patrón `hilo I YYYY-MM-DD HH-mm F YYYY-MM-DD HH-mm.md`.
7. Comprobar ruta y contenido, realizar el commit y verificar que el archivo quedó persistido antes de declarar completado el cierre.
8. Si no se puede guardar o confirmar el commit, comunicar el bloqueo y dejar el cierre documental como pendiente.
9. No leer todos los hilos archivados al iniciar una conversación. Se consultan bajo demanda o cuando un antecedente concreto sea necesario para el trabajo.

El checkpoint de continuidad y el archivo del hilo cumplen funciones distintas: el checkpoint permite retomar el trabajo rápidamente; el registro conserva la historia para consulta posterior.

---

## Evolución iterativa de modelos y diseños

Los modelos, esquemas, taxonomías y arquitecturas de Softly son hipótesis de diseño sujetas a revisión mediante evidencia. Ninguna versión debe tratarse como definitiva por el solo hecho de estar documentada o implementada.

Ciclo obligatorio de mejora:
1. **Diseñar:** declarar versión, alcance, supuestos y criterios de aceptación.
2. **Probar:** aplicar el diseño a casos representativos y registrar el protocolo.
3. **Observar:** documentar resultados, errores, fricciones, casos no cubiertos y efectos secundarios.
4. **Evaluar:** comparar el desempeño con criterios y una línea base cuando sea posible.
5. **Redefinir:** proponer cambios vinculados a observaciones y evidencia concreta.
6. **Regresar:** repetir las pruebas relevantes y comprobar que la modificación mejora el resultado sin degradaciones inaceptables.

### Reglas de evolución

- **Ninguna versión es sagrada:** se puede volver a etapas anteriores y revisar decisiones cuando el desempeño o nueva evidencia lo justifique.
- **Cambios con fundamento:** registrar el problema observado, evidencia, alternativas, impacto esperado y criterio para aceptar el cambio. Una idea nueva por sí sola no obliga a modificar el diseño.
- **Historia preservada:** no sobrescribir artefactos ni datos históricos para hacerlos coincidir con el modelo nuevo. Versionar decisiones, esquemas, pruebas y resultados.
- **Migraciones explícitas:** todo cambio que afecte datos existentes debe definir compatibilidad, transformación, validación, reversibilidad cuando sea viable y tratamiento de registros que no puedan migrarse.
- **Separar diseño de desempeño:** una versión documentada o implementada no se considera validada hasta superar pruebas representativas, negativas y de regresión.
- **Registrar regresiones:** si una nueva versión empeora una capacidad, conservar el resultado y permitir volver a una versión anterior sin perder trazabilidad.
- **No confundir estabilidad con inmovilidad:** mantener interfaces estables cuando sea útil, pero no conservar estructuras defectuosas solo para evitar cambios.

Cada iteración debe dejar enlazados el diseño probado, los casos y datos utilizados, las observaciones, los resultados, la decisión de cambio y la versión resultante.
