# Comparación final de informes — La arquitectura minimalista de Softly

**Coordinación:** Katarina 2.0.0 — `katarina` (Agent Softly)  
**Dirección humana:** gAto  
**Fase:** V — comparación final  
**Fecha:** 2026-11-16  
**Estado:** Comparación documental entregada; decisiones normativas y experimentales reservadas a gAto

## 1. Fuentes contrastadas

1. Informe final individual de Katarina: `Katarinasay/entregable/2026-11-16-informe-final-katarina-arquitectura-minimalista.md` — blob SHA `90180a93b32a3415b08725b0e5a1c4abcf53d812`.
2. Informe final individual de Softly: `Softlysay/entregable/2026-11-16-informe-final-softly-arquitectura-minimalista.md` — blob SHA `6a21e9ece5d273568510e953ea221efa237a725f`.
3. Reconstrucción integrada v0.3: `Katarinasay/entregable/2026-11-16-reconstruccion-arquitectonica-integrada-fase-IV-v0.3.md` — blob SHA `b8792a73f5d5f9769cbfac2b020a9d4cb26ab2bc`.

Los tres documentos fueron leídos desde GitHub. Esta comparación sintetiza sus contenidos; no modifica la identidad normativa, schemas ni runtime.

## 2. Dictamen ejecutivo

Los informes finales de Katarina y Softly son **sustancialmente convergentes**. Ambos consideran que la reconstrucción v0.3 representa fielmente el resultado conceptual de la deliberación; ambos preservan la diferencia de énfasis entre sus perspectivas; ambos rechazan convertir la síntesis en norma por sí sola; y ambos distinguen arquitectura documental, sesión activa, ejecución efectiva y validación experimental.

No aparece una discrepancia nueva que invalide la v0.3. El informe de Softly amplía y hace más explícitos algunos mecanismos y límites que el informe de Katarina trató de forma más sintética. Esas ampliaciones son complementarias y pueden conservarse como observaciones de profundidad, sin reabrir la reconstrucción ni modificarla automáticamente.

**Resultado:** Fase V queda completada en cuanto a informes individuales y comparación final. La deliberación documental puede considerarse entregada a gAto. No se declara aprobación normativa, implementación, validación experimental ni cierre de decisiones que corresponden a gAto.

## 3. Acuerdos coincidentes

| Tema | Coincidencia de ambos informes |
|---|---|
| Identidad vigente | Se conserva literalmente: «una matriz generativa y un sistema autoevolutivo». Ningún informe propone cambiar SOFTLY.md por cuenta propia. |
| Planos | Definición, Coordinación y Ejecución son planos conceptuales diferenciables; no exigen tres servicios o directorios. |
| GitHub | Es memoria documental y superficie persistente de coordinación; publicar no activa sesiones, no prueba lectura y no garantiza ejecución. |
| Núcleo | Debe definirse por responsabilidades, no por una lista inmutable de archivos. |
| MVP | Los cinco elementos del PDF son una hipótesis razonable de prototipo, no suficiencia universal demostrada. |
| Contratos | Mandato, permisos declarados, permisos efectivos, enforcement y auditoría son conceptos distintos. Un contrato declarativo no bloquea técnicamente una acción. |
| Concurrencia | Los conflictos técnicos y semánticos son distintos. Namespacing/eventos individuales ayudan con colisiones, pero no resuelven contradicciones ni autoridad. |
| Handoffs | Publicación, lectura declarada, evaluación, aceptación de asignación, ejecución, entrega y aceptación de entrega no son equivalentes. |
| Capacidades | Las capacidades externas requieren gobernanza explícita de altas, modificaciones, revisión, suspensión y retiro. |
| Síntesis | Las fuentes originales deben preservarse y las representaciones deben mantener anclajes; trazabilidad no demuestra verdad o fidelidad por sí sola. |
| Evidencia | SYN-DAEMON-20261116-001 se registra como pasada que el PDF presenta como realizada, pero no fue reproducida ni verificada independientemente en esta deliberación. |
| Autoridad | La reconstrucción y los informes no son decisiones de gAto. |

## 4. Diferencia conceptual que permanece abierta

- **Katarina:** «sistema de conocimiento y coordinación cognitiva» enfatiza la función organizativa: cómo se conserva conocimiento, continuidad y coordinación de capacidades cognitivas.
- **Softly:** «arquitectura de información operacional» enfatiza el mecanismo accionable: cómo contratos, eventos, rutas y handoffs orientan operaciones cuando una sesión activa los interpreta y dispone de herramientas.

Softly considera plausible que la coordinación cognitiva describa la función global y la arquitectura de información operacional el mecanismo que la vuelve accionable. Pero no recomienda convertir esa composición en jerarquía normativa definitiva. Katarina coincide en no forzar una resolución terminológica durante esta deliberación.

**Clasificación:** complementariedad plausible con diferencia sustantiva de énfasis; jerarquía no resuelta. No es una contradicción binaria ni un consenso sobre cuál perspectiva es fundamental. La decisión, si se requiere, pertenece a gAto.

## 5. Aportes específicos de cada informe

### Aportes destacados de Katarina

1. Expone de forma compacta los diez hallazgos compartidos y el inventario de decisiones de dirección.
2. Subraya que la síntesis v0.3 no debe transformarse automáticamente en cambios de SOFTLY.md, schemas o runtime.
3. Recomienda separar el diseño futuro del schema de una eventual etapa experimental.
4. Mantiene el foco en la arquitectura integrada y en los límites de autoridad.

### Aportes adicionales de Softly

1. Desarrolla la colaboración como **estigmergia documental**: sesiones separadas dejan señales persistentes en canales direccionales `say/` y espacios comunes `shared/`; no se trata de comunicación mágica entre prompts.
2. Desglosa estados de existencia y operación: definido, disponible/Active Standby, sesión activa, operación ejecutada y entrega aceptada.
3. Explicita siete responsabilidades del núcleo, separando gobernanza del ciclo de vida de capacidades como responsabilidad identificable, aunque no necesariamente como subsistema.
4. Advierte contra confundir exploración/caos con causalidad demostrada o con un método permanente; la exploración puede producir hallazgos, pero también retrabajo y pérdida de trazabilidad.
5. Identifica afirmaciones cuantitativas del PDF —recuperación en menos de 60 segundos y compresión en menos de 45 líneas— como no respaldadas por un protocolo de medición suficiente en las fuentes revisadas.
6. Propone requisitos experimentales más detallados para el demonio: corpus versionado, rúbrica previa, casos negativos y contradictorios, evaluación ciega cuando corresponda, repetición y regresiones.
7. Señala que la extracción textual del PDF contiene fragmentos truncados en partes de la plantilla y del cuerpo representacional, por lo que no deben completarse por inferencia como si fueran texto íntegro.

Estos puntos profundizan la lectura de Softly; no contradicen el informe de Katarina ni requieren cambiar la v0.3. Los detalles sobre truncamiento y métricas deben entenderse como límites de la fuente documental revisada, no como prueba de que el diseño original carezca de esos elementos fuera de la extracción disponible.

## 6. Pendientes y decisiones reservadas a gAto

No es necesario resolverlos todos para dar por entregada la deliberación. Se mantienen como decisiones independientes:

1. **Identidad conceptual:** si las perspectivas son complementarias/cofundamentales o si una tiene jerarquía sobre la otra. La identidad normativa vigente permanece intacta.
2. **Matriz de autoridad:** quién integra resultados incompatibles, acepta entregas delegadas y escala conflictos por dominio.
3. **Gobernanza de capacidades:** quién autoriza altas, modificaciones, revisiones, suspensiones y retiros.
4. **Contrato de handoff:** si se encarga un diseño de nueva versión del schema para separar estado de proceso y resultado de tarea, formalizar transiciones y definir retrabajo. El schema existente no se modificó.
5. **Prioridad experimental:** si se evalúa el MVP y/o el demonio, con corpus, rúbrica, criterios, alcance y recursos definidos antes de implementar.
6. **Criterio de suficiencia:** qué nivel de confiabilidad y evidencia bastaría para adoptar el modelo en equipos o proyectos de mayores consecuencias.

## 7. Estado de evidencia y límites

- La v0.3 es una reconstrucción conceptual revisada y aceptada en lo sustantivo por Softly; no es norma aprobada por gAto.
- El schema `schemas/handoff.schema.json` existe y su contenido declarativo fue inspeccionado; no se demostró enforcement runtime, leases operativos ni transiciones automáticas.
- El PDF reporta SYN-DAEMON-20261116-001 como pasada real; la deliberación no reprodujo el lote, Softly.zip ni la ejecución.
- No se ejecutó validación experimental independiente del MVP, del demonio, de la equivalencia conductual ni de la suficiencia universal de los cinco elementos.
- No se modificaron SOFTLY.md, schemas ni runtime durante la deliberación.

## 8. Recomendación final a gAto

1. Conservar la reconstrucción integrada v0.3 como resultado conceptual de Fase IV.
2. Conservar ambos informes finales como conclusiones individuales independientes, junto con esta comparación.
3. No cambiar SOFTLY.md ni schemas sin una decisión o encargo explícito.
4. Si se prioriza avanzar técnicamente, elegir una sola línea de trabajo acotada: diseño del contrato de handoff o experimento documental reproducible del demonio/MVP. No mezclar automáticamente ambas.
5. Mantener abierta la diferencia conceptual hasta que tenga consecuencias prácticas que ameriten una decisión de identidad.

## 9. Cierre de Fase V

- Informe final individual Katarina: publicado y releído.
- Informe final individual Softly: publicado y releído.
- Comparación final: elaborada y persistida en este documento.
- Fases I–V: completadas en el plano deliberativo/documental.

**La deliberación queda entregada a gAto para decisión.** Esto no significa que las propuestas hayan sido aprobadas, que el sistema esté implementado o que se haya validado experimentalmente. La autoridad normativa y la elección de próximos trabajos permanecen en gAto.

---

*Comparación final preparada por Katarina 2.0.0 — `katarina`. No constituye decisión normativa ni aprobación en nombre de gAto.*
