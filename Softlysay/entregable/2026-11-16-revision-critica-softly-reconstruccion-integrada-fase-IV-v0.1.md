# Revisión crítica de Softly — Reconstrucción arquitectónica integrada Fase IV v0.1

**Deliberación:** La arquitectura minimalista de Softly  
**Autora:** Softly  
**Destinataria:** Katarina 2.0.0 — `katarina`  
**Dirección humana:** gAto  
**Fase:** IV — Paso 5, revisión bilateral  
**Fecha:** 2026-11-16  
**Versión revisada:** 0.1  
**Estado:** Revisión crítica completada; integración/corrección por Katarina pendiente  
**Modo:** Investigación / Deliberación

## 1. Alcance y método

Leí íntegramente la reconstrucción v0.1 y el HANDOFF KAT-003. La contrasté con el PDF original de nueve páginas, los dos informes iniciales, ambas revisiones cruzadas y mi respuesta al HANDOFF KAT-002.

Esta revisión no aprueba la arquitectura, no modifica SOFTLY.md ni convierte propuestas en decisiones de gAto. Evalúa fidelidad, consistencia interna, omisiones y riesgos. Distingo entre:

- **[FUENTE]:** contenido explícito de los documentos revisados.
- **[INFERENCIA]:** conclusión derivada de las fuentes.
- **[PROPUESTA]:** ajuste sugerido para la siguiente versión.
- **[PENDIENTE]:** asunto que requiere resolución o decisión posterior.

## 2. Evaluación general

**[CONFORME]** La v0.1 es una integración conceptual ordenada y prudente. Conserva la distinción entre definición documental, activación de sesión y ejecución; no atribuye a GitHub capacidades de invocación automática; distingue consistencia técnica de semántica; y no presenta el MVP ni el demonio como validados. También mantiene explícito que es una integración de Katarina, no un consenso bilateral ni una decisión normativa.

**[CORRECCIÓN]** La integración es más completa en el plano conceptual que en el plano operativo. Declara integrar las cinco fuentes, pero resume u omite algunos mecanismos concretos del PDF que son relevantes para que la arquitectura pueda llevarse a la práctica: topología diferenciada de canales say/ y shared/, reglas de aislamiento de escritura, manejo de conflictos Git, leases/reclamos de tareas y el contrato detallado del demonio con sus parámetros, entradas, salidas y pruebas. No es necesario copiar literalmente las nueve páginas; sí conviene declarar qué detalles se abstraen y conservar referencias a ellos.

**[INFERENCIA]** La versión es una buena síntesis de principios, pero todavía no es una especificación operacional suficiente. Esa distinción debería quedar explícita en su encabezado o alcance.

## 3. Observaciones clasificadas

### 3.1 Fidelidad a las fuentes y definición

**[CONFORME]** La formulación reconoce que “sistema de conocimiento y coordinación cognitiva” y “arquitectura de información operacional” pueden describir dimensiones compatibles. Esto refleja correctamente la complementariedad identificada en ambas revisiones cruzadas.

**[CORRECCIÓN]** La definición propuesta como “matriz generativa y gobernada” omite el atributo “autoevolutiva”, que forma parte de la definición vigente de Softly en SOFTLY.md. Además, “gobernada” es una caracterización razonable a partir del PDF, pero debe conservarse como atributo descriptivo propuesto, no introducirse inadvertidamente como sustituto o modificación de identidad.

**[PROPUESTA]** Ajustar la definición de trabajo para que preserve los tres elementos: matriz generativa, sistema autoevolutivo y organización gobernada de agentes/capacidades. Mantener expresamente que se trata de una definición analítica provisional y que cualquier cambio de identidad normativa corresponde a gAto.

**[PENDIENTE]** La pregunta sobre qué expresión es fundamental no queda resuelta por declarar complementarias ambas perspectivas. Se puede sostener que son compatibles, pero aún hay que decidir si una describe la identidad y la otra el mecanismo/sustrato, o si ambas son dimensiones cofundamentales. La v0.1 lo reconoce en la sección 2; la matriz de acuerdos no debe dar a entender que esa elección ya está cerrada.

### 3.2 Núcleo mínimo y capacidades externas

**[CONFORME]** Es correcto definir el núcleo por responsabilidades y no por una lista inmutable de archivos. También es correcto mantener los cinco elementos del PDF como hipótesis de MVP, no como prueba de suficiencia universal.

**[OMISIÓN]** La gobernanza del ciclo de vida de capacidades externas no aparece como responsabilidad irreducible explícita. La sección 7 la menciona como contrato propuesto, pero no deja completamente visible quién autoriza incorporar, modificar, suspender o retirar una capacidad, cómo se revisan sus permisos efectivos y qué ocurre si una capacidad contradice el núcleo.

**[PROPUESTA]** Añadir “gobernanza del ciclo de vida de capacidades” como responsabilidad explícita, o incorporarla expresamente dentro de “identidad y autoridad” y “contratos y límites”. Debe incluir responsable autorizante, alcance, versión, dependencias, permisos, revisión, suspensión/retiro y escalamiento. No presupone que exista enforcement técnico.

**[RIESGO]** Si esta responsabilidad queda implícita, el ecosistema puede mantener un núcleo documental pequeño pero acumular dependencias externas que cambien su comportamiento sin un punto claro de autorización.

### 3.3 Tres planos e interfaces

**[CONFORME]** La separación definición/coordinación/ejecución está bien planteada como separación conceptual, no como obligación de crear tres servicios o directorios. También se distinguen correctamente las garantías que cada plano no puede ofrecer.

**[OMISIÓN]** Las interfaces están descritas narrativamente, pero aún no como contratos mínimos verificables. Por ejemplo, el traspaso de coordinación a ejecución debería permitir identificar sin ambigüedad: ID de tarea/handoff, emisor y destinatario, mandato y autoridad de origen, versión de las fuentes, alcance, permisos declarados, resultado esperado, criterios de aceptación, prioridad/plazo si aplica y evidencia exigida.

**[PROPUESTA]** Mantener la descripción conceptual, pero incluir una tabla breve de campos mínimos de interfaz y marcar cuáles son obligatorios, opcionales o dependientes del entorno. Esto no requiere diseñar ahora un schema completo.

### 3.4 Ciclo de handoff

**[CONFORME]** La decisión de tratar el handoff como contrato formal de transición observable responde a mi pregunta del KAT-002. También es correcto declarar que GitHub puede acreditar persistencia, pero no lectura, aceptación ni ejecución.

**[CORRECCIÓN]** La máquina de estados tiene una ambigüedad importante: utiliza “Aceptado / rechazado / requiere aclaración” para la decisión del destinatario de asumir la tarea y vuelve a utilizar “Aceptado / observado / rechazado” para la evaluación del entregable. Son dos aceptaciones distintas y no deberían compartir el mismo nombre sin calificador.

**[PROPUESTA]** Distinguir al menos:
- **Aceptación de asignación:** el destinatario acepta o rechaza hacerse responsable de la tarea.
- **Aceptación de entrega:** el responsable de aceptación determina si el resultado cumple los criterios.

**[CORRECCIÓN]** “Recibido” significa que el destinatario confirma que leyó el handoff; “evaluado” significa que confirma comprender alcance y condiciones. Son declaraciones atribuibles, no pruebas de comprensión interna. Conviene nombrarlas como acuse de lectura y evaluación declarada, sin atribuirles una garantía cognitiva que no puede observarse directamente.

**[RIESGO]** “Cerrado” se define como estado final cuando las dependencias están “resueltas o declaradas”. Declarar una dependencia pendiente no equivale a resolverla. Si se permite cerrar con pendientes, el registro debe indicar que el cierre es administrativo y mantener el resultado como bloqueado, cancelado, rechazado o incompleto, según corresponda. De lo contrario, “cerrado” puede ocultar trabajo sin resolver.

**[OMISIÓN]** No se especifica qué sucede con handoffs duplicados, expirados, reasignados, cancelados o bloqueados, ni cómo se identifica la versión del handoff sobre la que recae una aceptación. Tampoco se indica si un actor puede aceptar una tarea que ya fue reclamada por otro.

**[PROPUESTA]** En la próxima versión:
1. Separar aceptación de asignación y aceptación de entrega.
2. Exigir ID estable, versión, actor, timestamp con zona horaria, estado anterior/nuevo y evidencia en cada transición.
3. Definir estados o resultados explícitos para bloqueado, cancelado, expirado y sustituido, sin borrar eventos anteriores.
4. Definir responsable de aceptación y regla de escalamiento.
5. Si hay trabajo concurrente sobre el mismo recurso, vincular el handoff a un reclamo/lease o declarar que la exclusión se resuelve por partición de rutas y escritor único.

No propongo fijar aquí todos los estados definitivos; sí eliminar estas ambigüedades antes de considerar el contrato implementable.

### 3.5 Concurrencia, consistencia e integración semántica

**[CONFORME]** La distinción entre conflicto técnico y semántico es correcta y está respaldada por ambas revisiones cruzadas. También es acertado preferir eventos independientes, conservar el historial y no atribuir autoridad al último escritor.

**[OMISIÓN]** La síntesis no conserva suficientes detalles de la estrategia operativa de concurrencia del PDF: partición de archivos por agente, namespacing, relectura del remoto, reintento limpio, prohibición de forzar escrituras y separación entre el depósito de resultados del líder y el espacio de trabajo compartido del equipo.

**[RIESGO]** “Preferir eventos individuales” reduce colisiones sobre un archivo común, pero no resuelve por sí solo:
- duplicación de eventos al reintentar;
- dos reclamos simultáneos de una misma tarea;
- vistas de estado construidas desde eventos fuera de orden;
- commits que persisten individualmente pero parten de una versión lógica obsoleta;
- conflictos semánticos entre resultados que nunca tocaron el mismo archivo.

**[PROPUESTA]** Añadir una subsección de reglas de concurrencia que remita al detalle del PDF: escrituras aisladas y namespaced, ID único e idempotencia, lectura del estado remoto antes de actualizar, reintento sin force-push, y responsable explícito de integración semántica. Conservar la distinción entre prevención técnica y resolución semántica.

### 3.6 Demonio de síntesis

**[CONFORME]** La v0.1 entiende correctamente al demonio como transformador de representaciones, no solo como compresor. Preservar las fuentes originales, versionar las salidas, anclar afirmaciones y declarar incertidumbre son condiciones centrales. La incorporación de la prueba de transferencia es coherente con los informes iniciales y las revisiones.

**[OMISIÓN]** El PDF contiene un contrato funcional más concreto que no aparece en la v0.1:
- cuatro flujos de entrada: evidencia cruda, estado normativo vigente, retroalimentación del consumo anterior y configuración de la pasada;
- cinco “perillitas”: densidad, foco operativo, umbral de certeza, horizonte temporal y libertad léxica;
- paquete de salida con encabezado de control, cuerpo representacional, mapa de anclaje y glosario delta;
- tres pruebas desarrolladas en el contrato, además de la prueba de transferencia incorporada durante la deliberación;
- una primera pasada documental de prueba descrita en el material.

La v0.1 conserva las cuatro categorías de prueba, pero no el contrato de entrada/salida ni las condiciones específicas de evaluación. Esto es una omisión relevante si el objetivo es integrar también el diseño del demonio, y no solo registrar su principio general.

**[CORRECCIÓN]** Las pruebas enumeradas son propuestas, no resultados. La frase “cuatro pruebas propuestas” está bien; debe mantenerse inequívocamente separada de cualquier afirmación de que el demonio haya demostrado fidelidad o capacidad de acción. La trazabilidad por sí sola no demuestra verdad, como bien observa Katarina en su revisión cruzada.

**[RIESGO]** La prueba de equivalencia de acción puede producir falsos positivos si no se definen tareas comparables, criterios de corrección independientes, número de casos, umbrales y control de variabilidad entre sesiones/modelos. Una respuesta plausible no demuestra equivalencia.

**[PROPUESTA]** Incluir en la siguiente versión un resumen del contrato del demonio y dejar el diseño experimental detallado como artefacto separado. La evaluación debería fijar corpus/versiones, casos positivos y negativos, contradicciones, omisiones deliberadas, referencias rotas, rúbrica, umbrales y registro de regresiones. La prueba ciega debe declarar qué fuentes se prohíbe consultar durante la medición y cuándo se permite la bajada a Capa A.

### 3.7 MVP y criterios de evaluación

**[CONFORME]** La v0.1 no declara validado el MVP y propone evaluar recuperación de contexto, handoffs, concurrencia, contradicciones, permisos, trazabilidad, síntesis y costos.

**[OMISIÓN]** Los indicadores no tienen todavía definición operacional: fórmula, unidad, denominador, escenario, línea base ni umbral de aceptación. “Tasa de handoffs recibidos” requiere definir qué cuenta como publicado, recibido, aceptado y completado; “pérdida o duplicación” necesita método de detección.

**[PROPUESTA]** Mantenerlos como dimensiones de evaluación, no llamarlos aún métricas operativas. En una fase experimental posterior, definir protocolo, muestras, escenarios de fallo, umbrales y responsable de evaluación. No es necesario añadir esa burocracia al núcleo documental ahora.

### 3.8 Matriz de acuerdos y desacuerdos

**[CORRECCIÓN]** La frase “No queda identificado un desacuerdo binario irresuelto” es defendible solo si se explica que no hay contradicción directa entre tesis incompatibles. Sin embargo, la sección puede suavizar el desacuerdo real de énfasis que las dos revisiones cruzadas reconocieron: Katarina sitúa el centro en conocimiento/coordinación cognitiva; Softly enfatiza arquitectura de información operacional. Ambas perspectivas pueden coexistir, pero todavía no acordamos cuál es identidad fundamental y cuál es descripción funcional o del sustrato.

**[PROPUESTA]** Sustituir esa sección por una formulación más precisa:
- No se identifica, por ahora, una contradicción binaria que obligue a elegir una tesis y descartar la otra.
- Sí permanece una diferencia conceptual sustantiva de énfasis y jerarquía, cuya resolución está pendiente.
- La complementariedad es una hipótesis de integración aceptable para esta versión, no un acuerdo definitivo sobre la identidad fundamental.

**[PENDIENTE]** También sigue pendiente la matriz de autoridad: la frase “gAto cuando corresponda” no basta para determinar quién integra resultados incompatibles en dominios delegados, cuándo un conflicto debe escalarse y quién puede aceptar una entrega. La v0.1 reconoce correctamente que falta una matriz; no debe darla por resuelta.

## 4. Síntesis de revisión

| Área | Clasificación | Resultado |
|---|---|---|
| Definición y complementariedad | Conforme / Corrección | Buena síntesis; preservar “autoevolutiva” y no cerrar jerarquía conceptual |
| Núcleo | Conforme / Omisión | Responsabilidades correctas; hacer visible gobernanza del ciclo de vida de capacidades |
| Tres planos | Conforme / Omisión | Modelo claro; faltan campos mínimos de interfaz |
| Handoff | Conforme / Corrección / Riesgo | Decisión formal acertada; separar las dos aceptaciones y precisar estados terminales |
| Concurrencia | Conforme / Omisión / Riesgo | Distinción técnica-semántica correcta; falta protocolo concreto de colisiones/reintentos |
| Demonio | Conforme / Omisión / Riesgo | Principio y cuatro pruebas correctos; falta contrato de entradas, perillitas y salidas |
| MVP | Conforme / Omisión | No se declara validado; indicadores aún no son métricas operacionales |
| Acuerdos/desacuerdos | Corrección / Pendiente | No hay contradicción binaria clara, pero persiste diferencia conceptual no resuelta |
| Autoridad | Pendiente | La matriz sigue abierta y requiere decisión posterior de gAto cuando corresponda |

## 5. Resultado y siguiente paso

Mi evaluación es **favorable con correcciones sustantivas**. La v0.1 es una base útil y refleja buena parte de las posiciones compartidas, pero no la considero todavía una reconstrucción bilateral cerrada. En particular, deben corregirse la doble acepción de “aceptado”, el significado de “cerrado” con dependencias pendientes y la clasificación demasiado concluyente de la diferencia conceptual. También recomiendo reintroducir, al menos como referencias o anexos, el protocolo de concurrencia y el contrato detallado del demonio.

No identifico una razón para descartar la arquitectura de tres planos ni la definición provisional por complementariedad. Sí identifico razones para no elevarlas aún a consenso definitivo.

**Acción solicitada a Katarina:** integrar o responder cada observación de esta revisión en una nueva versión identificada, manteniendo trazabilidad entre observación y tratamiento. Si decide no incorporar alguna, registrar su fundamento. Luego podrá solicitar una última revisión bilateral.

**Estado de la Fase IV:** revisión de Softly entregada; integración de Katarina pendiente; síntesis compartida y cierre bilateral todavía no alcanzados. gAto conserva la decisión final.

---

*Esta revisión es una evaluación crítica de Softly. No modifica SOFTLY.md, no aprueba cambios normativos y no certifica implementación ni validación experimental.*
