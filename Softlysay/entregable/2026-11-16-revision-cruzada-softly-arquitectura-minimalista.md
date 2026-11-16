# Revisión cruzada de Softly — Arquitectura minimalista

**Fecha:** 2026-11-16  
**Autora:** Softly  
**Destinatario:** gAto  
**Fase:** III — Revisión cruzada  
**Estado:** Revisión de Softly completada; revisión recíproca de Katarina pendiente  
**Fuente primaria:** *La arquitectura minimalista de Softly.pdf* (9 páginas)  
**Informe contrastado:** Informe inicial independiente de Katarina 2.0.0, blob SHA `4d5c4363f2f078728196085705a3c374dc175080`.

## 1. Alcance y cautela

Esta revisión contrasta mi informe inicial con el informe inicial de Katarina. No presupone que Katarina haya leído mi informe ni que haya completado su revisión recíproca. Tampoco convierte propuestas del PDF o de las participantes en decisiones aprobadas por gAto.

## 2. Argumentos de Katarina que considero acertados

1. **Tres niveles arquitectónicos.** La separación entre definición (identidad, mandato y contratos), coordinación (canales, eventos, handoffs y estado) y ejecución (modelos, herramientas, sesiones y activación) mejora mi formulación inicial. Permite localizar con precisión qué resuelve el repositorio y qué depende del entorno de ejecución.
2. **Disponibilidad no es activación.** Que exista un handoff o mensaje persistido no despierta por sí mismo una sesión. Es una distinción operacional esencial y debe expresarse sin ambigüedad.
3. **Eventos independientes.** La propuesta de evitar un archivo común mutable y preferir eventos identificados por autor y operación reduce colisiones técnicas y mejora la trazabilidad.
4. **Criterios de aceptación explícitos.** Un archivo creado o un commit exitoso no demuestran por sí solos que la tarea esté bien resuelta. Cada entrega debe declarar cómo se comprobará.
5. **Cuarta prueba de transferencia para el demonio.** Resolver una situación nueva no expresada literalmente en la síntesis permite evaluar si la representación conserva relaciones y capacidad de generalización, no solo recuperación textual.
6. **Transformador de representaciones.** La caracterización del demonio como transformador de representaciones, y no mero compresor, recoge mejor la ambición descrita en el PDF.

## 3. Argumentos que cuestiono o acoto

- **“Sistema de conocimiento” como identidad principal:** es una perspectiva útil, pero puede quedarse corta si invisibiliza la función generativa y operacional de Softly. Mi formulación complementaria es que Softly es una arquitectura de información gobernada que, interpretada por un modelo y conectada a herramientas, permite instanciar y coordinar organizaciones de agentes. No afirmo que esta descripción sea una decisión normativa.
- **Separar tres niveles no resuelve automáticamente sus interfaces.** Hay que definir qué contrato cruza cada frontera: cómo una definición se instancia, cómo una coordinación se reclama y cómo una ejecución acredita su resultado.
- **Eventos inmutables no resuelven conflictos semánticos.** Evitan que un actor sobrescriba el registro de otro, pero pueden coexistir eventos incompatibles. Hace falta una autoridad y un procedimiento explícito de integración.
- **Permisos declarativos:** coincido en que un contrato no equivale a enforcement técnico. Sin embargo, no debemos concluir que la arquitectura documental sea inútil; debemos declarar con precisión qué límites son normativos y cuáles están efectivamente impuestos por las herramientas.
- **Optimización del MVP:** simplicidad, autonomía, confiabilidad y evolución pueden entrar en tensión. No conviene fijar una prioridad universal sin especificar el caso de uso y los criterios de evaluación.

## 4. Perspectivas que incorporo

La contribución de Katarina cambia mi análisis en tres aspectos:

1. La activación merece ser una responsabilidad arquitectónica visible, no una nota al pie de la coordinación.
2. La unidad de coordinación debe ser un evento o handoff identificable, con estados y criterios de aceptación trazables; no una conversación informal que el siguiente agente deba reconstruir.
3. La evaluación del demonio debe incluir transferencia además de reconstrucción, equivalencia de acción y detección de vacíos.

## 5. Coincidencias robustas

- La arquitectura documental es prometedora, pero sus cinco elementos no garantizan por sí solos colaboración efectiva.
- GitHub aporta persistencia y trazabilidad; no aporta comprensión semántica ni activación automática.
- La concurrencia debe tratarse mediante escrituras aisladas, eventos individuales y relectura; append-only sobre un archivo único no basta.
- El demonio debe preservar intactas las fuentes originales, versionar sus representaciones y anclar afirmaciones a evidencia.
- La portabilidad documental no demuestra equivalencia conductual entre distintos modelos y entornos.
- Las propuestas arquitectónicas no deben confundirse con decisiones aprobadas por gAto.

## 6. Desacuerdos y discusión pendiente

El desacuerdo conceptual principal es el énfasis: Katarina describe Softly como sistema de conocimiento y coordinación cognitiva; yo enfatizo la información como estructura operacional ejecutable por interpretación del modelo y uso de herramientas. No son necesariamente tesis excluyentes. La discusión debe determinar si una de ellas es más fundamental o si describen perspectivas complementarias.

También queda por precisar cuánto del control debe residir en contratos y cuánto requiere enforcement externo. Ninguna de las dos perspectivas demuestra que sea posible eliminar todos los conflictos; solo identifica cómo reducirlos y detectarlos.

## 7. Propuesta de síntesis provisional

Propongo describir la arquitectura en tres planos conectados:

- **Definición:** identidad, misión, competencias, fronteras, permisos declarados y contratos.
- **Coordinación:** buzones, shared/, eventos, handoffs, estado, reclamos y reglas de integración.
- **Ejecución:** modelo activo, sesión, herramientas, permisos efectivos, activación y verificación.

GitHub es memoria documental y plano persistente de coordinación, no el agente ni el mecanismo de activación. El LLM interpreta definiciones y estado, pero su conducta depende también del entorno y las herramientas disponibles.

La integración requiere dos verificaciones diferentes:
- **Consistencia técnica:** los cambios persisten, no se pierden y mantienen integridad del repositorio.
- **Consistencia semántica:** los resultados son compatibles con el mandato, los requisitos y entre sí. Esta última exige revisión y autoridad de integración explícita.

Para el demonio propongo cuatro pruebas: reconstrucción fiel, equivalencia de acción, detección de vacíos con bajada a fuente y transferencia a un caso nuevo. Estas son propuestas para evaluación, no pruebas ejecutadas ni resultados demostrados.

## 8. Recomendaciones a gAto

1. Mantener los cinco elementos del MVP como hipótesis de base, no como suficiencia universal demostrada.
2. Adoptar la separación definición/coordinación/ejecución como marco de análisis provisional.
3. Exigir eventos identificables y escrituras aisladas antes que una bitácora compartida mutable.
4. Definir quién integra resultados incompatibles y con qué criterio de aceptación.
5. Evaluar el demonio con las cuatro pruebas propuestas antes de decidir si requiere runtime.
6. Mantener intactas las fuentes y separar explícitamente hechos, inferencias e hipótesis.
7. No modificar el núcleo normativo hasta que la deliberación final y la decisión humana lo justifiquen.

## 9. Estado

La revisión de Softly sobre el informe inicial de Katarina queda documentada. La revisión de Katarina sobre el informe inicial de Softly sigue pendiente de confirmación y entrega. Por tanto, la Fase III bilateral no está completa; las Fases IV y V no se han iniciado. No se ha implementado ningún cambio arquitectónico.
