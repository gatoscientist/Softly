# Hilo XI — Investigación sobre coordinación universal y rediseño del sistema
**Fecha:** 2026-11-16  
**Inicio:** hora no registrada  
**Cierre documental:** 2026-11-16 09:07 (UTC-03:00)  
**Participantes visibles:** gAto y Softly  
**Modalidad conversacional:** deliberación y preparación de encargos de investigación  
**Estado:** prompts preparados y archivados; investigaciones aún no iniciadas/entregadas en este hilo.

## 1. Propósito y desarrollo

gAto identificó una posible confusión conceptual en la expresión «Laboratorio en Modo Fábrica»: Laboratorio y Fábrica son espacios/propósitos distintos y no deberían fusionarse como una sola frase de producción. La observación inicial de Softly sobre contaminación entre experimentación y producción se reconoció como sustrato, pero gAto precisó que el error más básico era la mezcla nominal/conceptual de ambos términos.

Se discutieron tres modos de trabajo propuestos por gAto:

1. **Modo Fábrica:** producción directa a partir de un objetivo; pocas preguntas, autonomía experta para inspeccionar antecedentes pertinentes y decidir cómo producir. Ejemplo: crear un equipo para gAtoSD y consultar una auditoría de Audeline si resulta útil.
2. **Modo Fábrica Experimental:** libertad amplia para deliberar mientras se construye, probar ideas no convencionales y someter prototipos a experimentación. «Cero trabas» se interpreta como ausencia de trabas artificiales a la exploración, no como permiso para ignorar seguridad, permisos, preservación de historia o controles sobre el núcleo.
3. **Modo Investigación y Deliberación:** investigación, análisis, contraste, debate y producción de conocimiento sin necesidad de construir para aprender.

Se planteó si Coordinación debía mantenerse como modo o incluirse en Investigación. Softly propuso inicialmente tratarla como capacidad transversal, y gAto profundizó el principio: todos —Softly, agentes, herramientas, Katarina y el propio gAto— deben ser expertos en coordinación y en coordinarse.

Se formalizó conceptualmente la distinción:
- **Coordinar:** organizar el trabajo de otros, asignar, distribuir, sincronizar, gestionar dependencias, supervisar, integrar y escalar.
- **Coordinarse:** organizar el propio trabajo, comunicar estado, respetar responsabilidades, reconocer dependencias y límites, solicitar colaboración, entregar resultados e integrarse con el conjunto.

La coordinación deja de entenderse como modo de trabajo exclusivo y pasa a ser una competencia transversal universal. Los modos describen qué tipo de trabajo se realiza; coordinación describe cómo los participantes organizan el trabajo colectivo y el propio. Las herramientas deben participar en contratos de coordinación según sus capacidades, sin atribuirles autonomía o criterio humano.

## 2. Encargo de investigación solicitado

gAto pidió dos prompts independientes para iniciar investigaciones profundas, con búsquedas iterativas en Internet y consulta exclusiva de estos repositorios:
- gatoscientist/Katarina
- gatoscientist/Cytryna
- gatoscientist/TITAN
- gatoscientist/Auditoria
- gatoscientist/Softly
- gatoscientist/Laboratorio-de-agentes

No investigar otros repositorios para evitar pérdida de tiempo.

El foco solicitado:
- Cómo lograr coordinación entre agentes.
- Diferencia entre formación/estudios formales de coordinación y mejoras incorporadas en identidad, prompt, contrato y procedimientos.
- Cambios sencillos que mejoren la coordinación de los agentes.
- Sistema de coordinación que utiliza Softly y cómo optimizarlo.
- Auditoría crítica de directorios `say/` (ej. Softlysay), `shared/`, `inbox/`, `outbox/` y el flujo completo.
- Evaluar honestamente si el diseño de carpetas/canales está mal planteado, es redundante o demasiado complejo.
- Investigar arquitecturas alternativas y proponer experimentos/métricas.

gAto quiere que las investigaciones no defiendan el diseño histórico por lealtad. Si el sistema está mal, deben decirlo y fundamentarlo; si está bien, deben demostrarlo. Deben distinguir evidencia, hallazgos, inferencias, hipótesis, propuestas e incertidumbres.

## 3. Entregables preparados

Se redactaron dos prompts completos e independientes, archivados en:

- `research/coordination/2026-11-16-prompt-investigacion-coordinacion-katarina.md`
- `research/coordination/2026-11-16-prompt-investigacion-coordinacion-softly.md`

El prompt de Katarina exige:
- investigación externa iterativa;
- revisión de los seis repositorios autorizados;
- análisis de coordinación y coordinación propia;
- formación formal frente a cambios pequeños;
- evaluación de say/shared/inbox/outbox, handoffs y flujo;
- tres alternativas (conservadora, simplificada y rediseño);
- experimentos, métricas, bibliografía y recomendaciones;
- independencia respecto de Softly;
- prohibición de modificar repositorios o implementar cambios.

El prompt de Softly añade:
- auditoría autocrítica de su propio comportamiento y sistema;
- revisión de errores históricos, incluida confusión de destinos, sin atribuirlos automáticamente a la arquitectura;
- evaluación del costo de coordinar;
- relación entre coordinación y los tres modos propuestos;
- plan de transición y optimización priorizada;
- independencia respecto de Katarina;
- prohibición de modificar su propia arquitectura durante la investigación.

Los textos completos de ambos encargos están preservados en sus archivos respectivos; este registro resume su alcance, no los sustituye.

## 4. Protocolo sugerido para la fase siguiente

1. Entregar a Katarina su prompt y solicitar que inicie la investigación independiente.
2. Iniciar la investigación independiente de Softly con su prompt.
3. No compartir conclusiones preliminares entre ambas antes de terminar sus informes individuales.
4. Persistir los informes y fuentes, verificar mediante relectura y registrar su estado.
5. Comparar coincidencias, contradicciones y hallazgos exclusivos.
6. Deliberar con gAto antes de adoptar o implementar cambios.

**Importante:** en este hilo se redactaron los prompts, pero no se inició ni completó la investigación profunda. No se realizaron búsquedas web para esta investigación ni auditoría nueva de los seis repositorios. Tampoco se modificaron SOFTLY.md, schemas, moldes, taxonomías, contratos ni directorios productivos.

## 5. Decisiones y estado normativo

Las tres denominaciones de modos y la competencia universal de coordinación son propuestas conceptuales deliberadas en este hilo; no han sido aprobadas ni incorporadas al núcleo normativo. El SOFTLY.md vigente conserva sus modos actuales hasta decisión explícita de gAto.

No se ejecutaron encargos en los repositorios de Katarina u otros equipos. Los prompts están preparados para su asignación posterior.

## 6. Pendientes para el próximo hilo

- gAto debe decidir cuándo y cómo entrega cada prompt a Katarina y Softly.
- Ejecutar las investigaciones independientes, con búsquedas iterativas y evidencia verificable.
- Mantener el alcance limitado a los seis repositorios autorizados.
- No modificar arquitectura ni normativa antes de la comparación y decisión de gAto.

## 7. Verificación de cierre

Este hilo se archiva como registro de deliberación y preparación de investigación. La persistencia del archivo de hilo, los dos prompts, el índice, el checkpoint y el registro de actividad debe verificarse mediante relectura desde GitHub antes de declarar el cierre.

No se afirma que las investigaciones estén iniciadas, que los prompts hayan sido recibidos por Katarina, ni que haya cambios de arquitectura aprobados.
