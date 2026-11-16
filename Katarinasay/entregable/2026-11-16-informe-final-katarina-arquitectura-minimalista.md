# Informe final individual de Katarina — La arquitectura minimalista de Softly

**Agente:** Katarina 2.0.0 — `katarina` (Agent Softly)  
**Dirección humana:** gAto  
**Deliberación:** La arquitectura minimalista de Softly  
**Fase:** V — informe final individual  
**Fecha:** 2026-11-16  
**Estado:** Entregado por Katarina; informe final individual de Softly pendiente  
**Modo:** Investigación / Deliberación

## 1. Alcance

Este informe cierra la participación individual de Katarina en la deliberación. Se apoya en el PDF original, los informes iniciales, las revisiones cruzadas, las respuestas de Softly a KAT-002, KAT-003 y KAT-004, y la reconstrucción integrada final v0.3.

No es una decisión normativa ni una aprobación de gAto. Distingue acuerdos, complementariedades, diferencias abiertas, hipótesis y asuntos que requieren decisión humana. No declara implementación ni validación experimental.

## 2. Conclusión ejecutiva

La arquitectura propuesta puede describirse coherentemente como un ecosistema multiagente cuyo sustrato documental y contractual permite conservar identidad, memoria, coordinación y transferencia de trabajo, mientras que las operaciones efectivas dependen de sesiones activas, herramientas y permisos disponibles.

La síntesis bilateral alcanzó una conformidad sustantiva sobre la reconstrucción conceptual y la separación entre definición, coordinación y ejecución. No alcanzó consenso sobre la jerarquía conceptual de la identidad, ni definió una matriz completa de autoridad. El MVP y el demonio de síntesis siguen siendo hipótesis/propuestas sin validación experimental independiente.

Mi recomendación es conservar la reconstrucción v0.3 como resultado conceptual de esta deliberación y no convertirla automáticamente en cambios de SOFTLY.md, schemas o runtime. Las decisiones normativas y la eventual etapa experimental deben ser encargos separados de gAto.

## 3. Hallazgos compartidos

1. **Definición, coordinación y ejecución son planos distintos.** Pueden tener interfaces claras sin exigir tres servicios, procesos o directorios.
2. **GitHub es memoria documental y superficie persistente de coordinación.** La publicación no implica lectura, activación de sesión, aceptación ni ejecución.
3. **El núcleo se define mejor por responsabilidades que por una lista inmutable de archivos.** Los cinco elementos del MVP son una hipótesis de prototipo, no prueba de suficiencia universal.
4. **Los contratos declarativos no equivalen a enforcement.** Permisos descritos, permisos efectivos, controles técnicos y auditoría deben distinguirse.
5. **La concurrencia tiene dos dimensiones.** Los conflictos técnicos y los conflictos semánticos requieren tratamientos distintos; eventos individuales no resuelven contradicciones de significado o autoridad.
6. **Los handoffs necesitan estados y evidencia atribuibles.** Publicación, lectura declarada, aceptación de asignación, ejecución, entrega y aceptación de entrega no son equivalentes.
7. **Las capacidades externas requieren gobernanza de ciclo de vida.** Su incorporación, modificación, suspensión y retiro no deben quedar implícitos.
8. **La síntesis debe preservar fuentes originales y anclajes.** La trazabilidad es necesaria, pero no prueba por sí sola verdad ni fidelidad.
9. **La portabilidad documental no demuestra equivalencia conductual.**
10. **Las propuestas de arquitectura no son decisiones de gAto ni evidencia de implementación.**

## 4. Diferencia conceptual que permanece abierta

Katarina ha enfatizado «sistema de conocimiento y coordinación cognitiva» para describir la función organizativa de la arquitectura. Softly ha enfatizado «arquitectura de información operacional», destacando que contratos, eventos y handoffs orientan acciones cuando sesiones activas los interpretan y cuentan con herramientas.

Ambas perspectivas pueden coexistir en una descripción por capas. Softly aceptó mantenerlas en la reconstrucción, pero no declaró resuelta su jerarquía identitaria. No hay contradicción binaria que obligue a descartar una; sí hay una diferencia sustantiva de énfasis y jerarquía.

**No recomiendo forzar una decisión terminológica durante esta deliberación.** La identidad normativa vigente de Softly permanece intacta: «una matriz generativa y un sistema autoevolutivo». Cualquier modificación de esa identidad corresponde a gAto.

## 5. Handoff y contrato existente

La deliberación identificó un schema declarativo vigente en `schemas/handoff.schema.json`, con campos obligatorios, un enum acotado de estados y un objeto lease con `claim_id` y `expires_at`.

La propuesta conceptual v0.3 amplía el contrato, pero no actualiza ese schema ni demuestra enforcement. Antes de implementar cambios se debe decidir cómo separar estado del proceso y resultado de la tarea, cómo se registra el retrabajo y si la historia se representa mediante eventos inmutables, documentos versionados o una combinación.

No recomiendo modificar el schema sin un encargo específico y una decisión sobre la matriz de autoridad.

## 6. Demonio de síntesis y evidencia

El PDF presenta la pasada SYN-DAEMON-20261116-001 como una «Pasada Real de Prueba». La deliberación conserva esa atribución como evidencia documental reportada, pero no reprodujo ni verificó independientemente el lote de entrada, el archivo Softly.zip ni la ejecución. Por tanto, no la tratamos como validación experimental independiente.

El demonio se entiende como transformador de representaciones con entradas, parámetros y paquete de salida descritos en el PDF. Las pruebas de reconstrucción fiel, equivalencia de acción, detección de vacíos y transferencia constituyen un protocolo propuesto; no hay resultados que permitan afirmar fidelidad demostrada.

La etapa experimental requeriría corpus versionado, rúbrica, casos positivos y negativos, contradicciones, omisiones deliberadas, referencias rotas, umbrales, prueba ciega y control de regresiones.

## 7. Decisiones que corresponden a gAto

No todas necesitan resolverse ahora. Las decisiones de dirección identificadas son:

1. **Identidad conceptual:** mantener la identidad normativa vigente y decidir, cuando sea oportuno, si las dos perspectivas arquitectónicas tienen jerarquía o son cofundamentales.
2. **Matriz de autoridad:** definir dominios delegables, responsables de integración semántica y condiciones de escalamiento obligatorio.
3. **Gobernanza de capacidades:** determinar quién autoriza altas, modificaciones, suspensiones y retiros, y con qué límites.
4. **Contrato de handoff:** decidir si se autoriza diseñar una nueva versión del schema para separar proceso y resultado y formalizar retrabajo.
5. **Etapa experimental:** decidir si el MVP y el demonio pasan a evaluación, con qué alcance y corpus, antes de cualquier implementación.

No propongo que gAto apruebe ahora todos los detalles técnicos. Son decisiones que deben mantenerse visibles para evitar que una propuesta documental se convierta silenciosamente en norma.

## 8. Recomendación final de Katarina

1. Conservar la reconstrucción v0.3 como resultado conceptual de la deliberación.
2. Mantener intactos SOFTLY.md y los schemas en ausencia de una orden específica.
3. Tratar el handoff ampliado y el demonio como diseños pendientes, no como capacidades existentes.
4. Separar una eventual etapa de diseño de schema de una eventual etapa experimental.
5. No cerrar la diferencia conceptual por cortesía: registrarla y permitir que gAto decida si requiere resolución.

## 9. Estado de Fase V

Este documento constituye el informe final individual de Katarina. El informe final individual de Softly debe persistirse por separado para preservar la independencia de ambas conclusiones.

Una vez recibido, Katarina puede entregar a gAto una comparación final de ambos informes y el inventario de decisiones pendientes. La autoridad final permanece en gAto.

---

*Informe final individual de Katarina 2.0.0. No constituye decisión normativa, aprobación de gAto ni certificación experimental.*
