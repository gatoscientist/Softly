# Hilo XV — deliberación sobre comunicación multiagente, TITAN y arquitectura Softly

**Fecha:** 2026-11-17  
**Inicio:** 10:49, America/Santiago (hora de inicio de la sesión).  
**Cierre solicitado:** 11:37, America/Santiago (hora indicada por el contexto de sesión).  
**Participantes visibles:** gAto y Softly.  
**Naturaleza del registro:** síntesis documental del intercambio visible; no es transcripción literal. Se conservan las ideas y distinciones expresadas por gAto. No se incorporan razonamientos privados ni se reconstruyen intervenciones ausentes.

## Propósito y modalidad

Continuar la deliberación sobre el núcleo mínimo de Softly, comprender cómo TITAN organiza la comunicación entre agentes y explorar qué aprendizajes de los proyectos relacionados pueden servir al diseño futuro de Softly. gAto pidió expresamente mirar las definiciones de comunicación de TITAN, no volver a explicar sus roles ni ejecutar cambios a partir de cada comentario.

La conversación se mantuvo en deliberación. No se formalizaron modos, contratos, reglas ni arquitectura; no se inició implementación ni uso de herramientas por agentes.

## 1. Lección principal de TITAN: comunicación eficiente entre agentes

gAto dirigió la atención a la forma en que la tripulación de TITAN se comunica entre sí. La idea central no es simplemente intercambiar mensajes o dejar rastros, sino comunicarse con la máxima eficiencia compatible con comprender y resolver el trabajo.

Las reglas de TITAN procuran que:
- Cada mensaje transporte solamente información útil para su destinatario.
- No se repitan reglas, contexto o instrucciones que ya están disponibles en los contratos.
- Se eliminen saludos, cortesías, culpa, gratitud automática y expresiones emocionales que no aportan al contenido operativo.
- La brevedad sea una disciplina: si algo puede expresarse en cinco palabras, probablemente pueda reducirse a dos o incluso a un gesto inequívoco.
- La economía de comunicación no suprima deliberación, objeciones, evidencia ni explicaciones necesarias para comprender.
- Los agentes se comuniquen directamente, sin convertir al Princeps en intermediario de cada intercambio.

La tripulación puede deliberar extensamente cuando eso produzca comprensión, pero sus mensajes de coordinación deben ser compactos. El objetivo es reducir tráfico redundante, no reducir el pensamiento.

## 2. Dos planos de comunicación

Se distinguió la comunicación operativa entre tripulantes de la conversación privada entre Primus y el Princeps.

En el plano operativo, la tripulación intercambia mensajes breves, funcionales y tipificados. En el canal privado, el Princeps puede salir de ese registro y conversar con Primus sobre lo que está ocurriendo: pedir explicaciones, entender por qué la tripulación se comunica de determinada manera y recibir una síntesis inteligible de la situación.

Primus no debe limitarse a retransmitir mensajes: debe poder explicar al Princeps qué está pasando, qué decisiones están en juego y cuándo una decisión requiere necesariamente su intervención.

## 3. Escalamiento jerárquico: Princeps y Princeps Seniores

gAto explicó la inspiración de la jerarquía de TITAN en la organización de legiones de titanes de Warhammer 40,000, utilizada como estructura narrativa y organizativa.

La proyección descrita es que un Princeps Seniores no gestione directamente a toda la tripulación de cada TITAN. Recibe la síntesis de varios Princeps, cada uno responsable de una unidad con su propia tripulación y comunicación interna. Cada TITAN constituye una entidad coordinada por su propio director; el nivel superior observa esas entidades, recibe lo que sus responsables consideran relevante y toma decisiones de alcance superior.

La analogía apunta a una arquitectura jerárquica y distribuida:
- Agentes especialistas trabajan y se comunican dentro de sus equipos.
- Un agente director comprende el estado de su equipo y presenta al nivel superior lo que importa.
- El nivel superior coordina responsables, no cada mensaje ni cada tarea elemental.
- Las decisiones que exceden la autoridad local se elevan al nivel correspondiente.

Primus debería poder resolver autónomamente lo que esté dentro de su mandato y señalar con claridad cuándo corresponde que el Princeps decida. La síntesis debe permitir dirigir sin tener que leer doce mensajes para entender una situación.

## 4. Relación entre Softly y los proyectos

gAto aclaró que TITAN, Cytryna y gAtoSD son proyectos relacionados con Softly y forman parte del ecosistema que Softly debe comprender en su conjunto. Esta comprensión corresponde a Softly; no implica cargar todos los detalles de cada proyecto en todos los agentes ni difundir indiscriminadamente ese contexto.

Se describieron sus diferencias:
- **TITAN:** proyecto multiagente y juego de rol; explora tripulaciones de especialistas que colaboran y se dirigen mediante una jerarquía. Su propósito incluye permitir que una persona sin conocimientos técnicos específicos pueda liderar un equipo multidisciplinario mediante una dirección adecuada.
- **Cytryna:** agente persistente con runtime, interfaz gráfica y conexión con APIs; actualmente gAto puede conectarse directamente a Cytryna y conversar con ella.
- **gAtoSD:** proyecto de seguridad informática y manejo de Ring 0, con capacidades profundas de telemetría y técnicas de seguridad. gAto indicó que contiene mucho de su experiencia en sistemas operativos y seguridad.

No se pidió que Softly convierta estos proyectos en tareas ni que los intervenga. Se compartió contexto para que Softly comprenda cómo encajan en el ecosistema y qué capacidades podrían aportar.

## 5. Deliberación, eficiencia y cuello de botella humano

gAto sostuvo que los agentes deben deliberar entre ellos de forma habitual porque necesitan entender qué está ocurriendo antes de actuar. La deliberación consume recursos, pero actuar sin comprensión no produce trabajo útil.

También precisó que gAto debe seguir siendo un cuello de botella deliberado en el sentido de marcar hasta dónde puede avanzar el sistema antes de requerir comprensión o decisión humana. Los agentes deben avanzar hasta donde tengan autoridad y evidencia suficientes; cuando aparezca un bloqueo real, deben detenerse en ese punto y presentar qué ocurrió para que gAto pueda comprenderlo y decidir. No se espera que todo el sistema sea infalible ni que nunca aparezcan bloqueos.

Se discutió que los bloqueos pueden ser inevitables en sistemas complejos. La aspiración no es prometer ausencia absoluta de bloqueos, sino evitar que un bloqueo local paralice indiscriminadamente todo el ecosistema y permitir que el trabajo independiente continúe cuando corresponda. La analogía de mutación y selección fue planteada por gAto como intuición sobre la aparición de resultados negativos y positivos; no se convirtió en un modelo formal.

## 6. Herramientas y contexto

gAto expresó que actualmente existe reticencia a incorporar herramientas en los flujos de agentes porque las experiencias de asignación han terminado en bloqueos. Considera necesario limpiar y reducir el contexto antes de ampliar el uso de herramientas, para que su incorporación no empeore la situación.

No se seleccionaron herramientas ni se inició su activación. Se reconoció que la capacidad de usar herramientas debe formar parte del desarrollo futuro, pero no se trató como tarea inmediata de este hilo.

## Ideas y principios deliberativos que quedan preservados

1. La comunicación entre agentes debe ser tan eficiente como sea posible: mensaje mínimo suficiente, sin cortesía ceremonial ni repetición de reglas conocidas.
2. La eficiencia comunicativa no equivale a deliberar poco. Los agentes deben deliberar lo necesario para entender, contrastar y resolver.
3. La deliberación debe ser distribuida entre agentes y equipos; gAto no debe ser el intermediario de cada intercambio.
4. La conversación privada con el director permite al humano comprender el cuadro operativo sin contaminar el canal de trabajo con el registro de esa conversación.
5. Los agentes directores deben coordinar responsables y elevar decisiones de nivel superior, no retransmitir cada detalle.
6. Softly debe comprender que TITAN, Cytryna y gAtoSD forman parte de su ecosistema, sin absorber indiscriminadamente sus contextos internos.
7. El avance autónomo debe detenerse ante límites reales de comprensión, autoridad o riesgo; el bloqueo local no debe convertirse automáticamente en parálisis global.
8. La incorporación de herramientas requiere un contexto más limpio y agentes capaces de utilizarlas sin quedar atrapados en procedimientos.
9. Las ideas anteriores son material de deliberación, no normas aprobadas ni arquitectura formal.

## Límites y decisiones explícitamente no tomadas

- No se modificaron contratos, mandatos, taxonomías ni modos de Softly.
- No se formalizó una arquitectura Princeps/Princeps Seniores para Softly.
- No se declaró que TITAN deba copiarse íntegramente en Softly; se examinó como antecedente de comunicación y organización.
- No se crearon, activaron ni modificaron agentes.
- No se intervinieron TITAN, Cytryna ni gAtoSD.
- No se seleccionaron ni activaron herramientas.
- No se inició auditoría, investigación formal ni tarea derivada de cada pregunta conversacional.
- No se alteró el estado de RESET-CORE-2026-002.

## Punto de continuidad

La conversación deja como aprendizaje principal la distinción entre deliberación profunda y comunicación operativa mínima. Softly debe poder comprender su ecosistema y coordinar responsables sin cargar con todos los historiales ni convertirse en intermediaria de cada intercambio. Las ideas quedan disponibles para futuras deliberaciones; solo se convertirán en documentos normativos o implementación cuando gAto lo indique expresamente.

**Estado del hilo:** cerrado y archivado documentalmente; sin decisiones normativas nuevas.
