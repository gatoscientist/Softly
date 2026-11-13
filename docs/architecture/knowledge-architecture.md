# Arquitectura de conocimiento: propuesta inicial

- **Estado:** propuesta conceptual inicial
- **Fecha:** 2026-11-13
- **Relacionada con:** SYN-20261113-001, secciones 16 y 17
- **Alcance:** documentar el primer paso de diseño; no especifica una implementación ni declara capacidades operativas.

## 1. Conclusión de trabajo

El siguiente avance de Softly será convertir la arquitectura conceptual de conocimiento —acumulación exhaustiva, comprensión condensada y auditoría bajo demanda— en un diseño técnico evaluable.

Para comenzar, el modelo se organizará alrededor de tres elementos conceptuales:

1. **Conceptos:** identifican aquello de lo que se habla, por ejemplo agentes, proyectos, documentos, versiones, experimentos o decisiones.
2. **Afirmaciones:** expresan una proposición concreta sobre uno o más conceptos. Deben indicar su tipo epistemológico (hecho, observación, inferencia, hipótesis, decisión o recomendación), estado de evaluación y evidencia asociada.
3. **Síntesis:** organizan y condensan un conjunto de afirmaciones para responder una pregunta o describir un tema. Son vistas derivadas y versionadas; nunca reemplazan las fuentes originales.

Esta separación permite distinguir el objeto del que hablamos, lo que sostenemos acerca de él y la representación condensada que construimos a partir de varias afirmaciones.

## 2. Relaciones mínimas

El modelo conceptual inicial contempla estas relaciones:

- Un concepto puede estar relacionado con otros conceptos.
- Una afirmación puede referirse a uno o varios conceptos.
- Una afirmación puede estar respaldada, contradicha o matizada por una o varias fuentes o registros originales.
- Una síntesis reúne afirmaciones y conserva referencias hacia ellas.
- Una versión nueva de una afirmación o síntesis debe mantener la trazabilidad de la versión anterior y explicar el cambio.
- Una síntesis puede quedar desactualizada cuando aparece evidencia nueva, cambia el alcance o se detecta una contradicción.

Representación simplificada:

`Fuentes y registros → Afirmaciones → Síntesis`
  
`Conceptos ↔ Afirmaciones ↔ Síntesis`

Las fuentes y registros originales permanecen como evidencia primaria. Las afirmaciones y síntesis son capas derivadas que deben poder navegarse hasta esa evidencia.

## 3. Identidad, procedencia y versionado

Como principio de diseño, cada elemento persistente deberá contar con:

- identificador estable y único;
- tipo de elemento;
- fecha de creación y última revisión;
- versión o mecanismo equivalente de historial;
- origen y responsable de incorporación, cuando corresponda;
- ámbito o universo al que pertenece;
- clasificación de acceso y política de retención;
- relaciones explícitas con otros elementos.

Los identificadores concretos, el esquema de datos, las reglas de versionado y la representación de las relaciones quedan pendientes de especificación. No se fija todavía una tecnología de almacenamiento ni un formato físico.

## 4. Principios que debe respetar el diseño

1. **La fuente no se sustituye por el resumen.** Los originales se conservan según las políticas de seguridad y retención.
2. **Toda afirmación importante debe ser rastreable.** La síntesis debe permitir llegar a las afirmaciones y desde ellas a la evidencia.
3. **La incertidumbre es información.** Se registran contradicciones, límites de cobertura y estados de evaluación.
4. **El conocimiento tiene contexto.** Se conserva el universo de origen y se aplican permisos en cada recuperación.
5. **La recuperación es escalonada.** Primero se consulta la síntesis pertinente; después, las afirmaciones y fuentes necesarias; se amplía la búsqueda solo cuando la tarea lo justifica.
6. **El historial no se reescribe.** Las correcciones generan nuevas versiones y mantienen la procedencia.
7. **Acceso no significa identidad compartida.** Softly, DEVAGENTS y TITAN mantienen sus universos y permisos diferenciados.

## 5. Secuencia de trabajo acordada

El diseño se desarrollará por etapas, sin intentar implementar todo de una vez:

1. Definir el modelo de datos y los identificadores de conceptos, afirmaciones, fuentes y síntesis.
2. Especificar las relaciones, referencias de evidencia y versionado.
3. Diseñar la indexación y recuperación híbrida/escalonada, con filtros por universo, permisos, tarea y vigencia.
4. Definir la detección de contradicciones, obsolescencia y necesidad de reauditoría.
5. Especificar instrumentación, observabilidad, privacidad, retención y controles de acceso.
6. Diseñar un experimento mínimo que compare recuperación desde síntesis más evidencia frente a la carga de contexto amplio, midiendo precisión, costo, tokens y tiempo hasta una acción correcta.

## 6. Estado y límites

Esta nota registra una **propuesta de organización conceptual y un plan de trabajo**. No constituye una decisión de implementación ni demuestra que exista un sistema de almacenamiento, indexación, recuperación o auditoría funcionando.

Las conclusiones de la sección 17.2 de la síntesis SYN-20261113-001 se mantienen como acuerdos conceptuales de continuidad. Este documento desarrolla el siguiente paso indicado en la sección 17.4, sin reabrir esos acuerdos.

## 7. Próximo punto concreto

El siguiente artefacto será una especificación mínima del modelo de datos: entidades, campos obligatorios, identificadores, relaciones y ejemplos de registros. Debe ser lo bastante pequeña para evaluarse y evolucionar sin comprometer prematuramente la tecnología de implementación.


## 8. Desarrollo del modelo conceptual

La etapa 1 quedó desarrollada en [Modelo conceptual del conocimiento de Softly](knowledge-domain-model.md). El documento define siete familias —entidades, conceptos, fuentes y registros, afirmaciones, síntesis, actividades y contextos— y dimensiones transversales de identidad, procedencia, tiempo, versionado, evaluación, acceso, retención e integridad.

Este mapa sigue siendo conceptual: no fija campos, identificadores, tecnología ni almacenamiento. El siguiente paso es especificar los campos e identificadores mínimos y probar el modelo con ejemplos de distintos dominios.
