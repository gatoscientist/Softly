# HANDOFF KAT-002 — Inicio y coordinación de Fase IV

**Emite:** Katarina (katarina 2.0.0 — Agent Softly)  
**Destinataria:** Softly  
**Dirección humana:** gAto  
**Deliberación:** La arquitectura minimalista de Softly  
**Fase:** IV — Reconstrucción conceptual compartida  
**Estado:** Handoff emitido por Katarina; recepción/activación por Softly pendiente  
**Fecha:** 2026-11-16

## 1. Motivo y autoridad

Katarina asume la coordinación de la Fase IV. La Fase III bilateral está completada: ambas revisiones cruzadas fueron publicadas y Softly confirmó haber leído la revisión de Katarina.

Este handoff no afirma que Softly haya sido activada ni que haya comenzado a trabajar. Es una asignación documental dirigida a Softly para que gAto pueda entregarla y se pueda registrar su respuesta.

No se solicita modificar SOFTLY.md, el núcleo de ningún agente, ni implementar o desplegar mecanismos. gAto conserva la autoridad sobre objetivos, prioridades y aprobación de decisiones.

## 2. Objetivo de la Fase IV

Construir una reconstrucción arquitectónica compartida que explique qué es la arquitectura minimalista de Softly, cuáles son sus responsabilidades mínimas, cómo se conectan sus planos y qué mecanismos son necesarios para que la propuesta sea confiable.

La síntesis debe integrar los aportes coincidentes sin borrar desacuerdos genuinos. No se busca consenso por cortesía.

## 3. Base documental obligatoria

Leer y contrastar, no limitarse a sus resúmenes:

1. La arquitectura minimalista de Softly.pdf (fuente primaria de nueve páginas).
2. Katarinasay/entregable/2026-11-16-informe-inicial-katarina-arquitectura-minimalista.md.
3. Softlysay/entregable/2026-11-16-informe-inicial-softly-arquitectura-minimalista.md.
4. Softlysay/entregable/2026-11-16-revision-cruzada-softly-arquitectura-minimalista.md.
5. Katarinasay/entregable/2026-11-16-revision-cruzada-katarina-arquitectura-minimalista.md.

Distinguir en todo momento:
- afirmaciones y propuestas explícitas de la fuente primaria;
- argumentos de Katarina;
- argumentos de Softly;
- inferencias de la deliberación;
- propuestas nuevas;
- decisiones aprobadas por gAto (si las hubiera).

## 4. Ejes que debemos reconstruir

### Eje A — Naturaleza y definición fundamental

Examinar si Softly debe describirse como:
- sistema de agentes;
- arquitectura de información operacional;
- sistema de conocimiento y coordinación cognitiva;
- combinación de perspectivas, aclarando qué describe cada una.

No forzar una definición única antes de probar compatibilidad y límites.

### Eje B — Núcleo mínimo

Determinar las responsabilidades irreducibles del núcleo. Distinguir responsabilidades de artefactos: los cinco elementos del MVP son una implementación propuesta, no necesariamente la definición universal del núcleo.

### Eje C — Planos e interfaces

Examinar el marco de tres planos:
- Definición: identidad, misión, competencias, fronteras, permisos declarados y contratos.
- Coordinación: buzones, shared/, eventos, handoffs, estado, reclamos y reglas de integración.
- Ejecución: modelo activo, sesión, herramientas, permisos efectivos, activación y verificación.

Para cada frontera, especificar qué información/contrato cruza y qué garantías no ofrece.

### Eje D — Activación y ciclo de trabajo

Distinguir disponibilidad de activación; mensaje publicado de mensaje recibido; recepción de aceptación; aceptación de ejecución; ejecución de finalización; finalización de aceptación.

Proponer estados observables y evidencia mínima, sin fingir automatismos que el repositorio no proporciona.

### Eje E — Concurrencia e integración

Separar:
- colisiones técnicas de escritura;
- conflictos semánticos entre resultados;
- autoridad y procedimiento de integración.

Evaluar eventos individuales, escrituras aisladas, relectura, reintento, reclamación de tareas y reconciliación semántica.

### Eje F — Contratos, autoridad y enforcement

Distinguir mandato, permiso declarado, permiso efectivo y control impuesto por herramientas. Definir qué decisiones requieren autoridad humana y cómo se evita que capacidades externas alteren unilateralmente el núcleo.

### Eje G — Demonio de síntesis

Examinarlo como transformador de representaciones, no solo como compresor. Evaluar cuatro pruebas propuestas:
1. reconstrucción fiel;
2. equivalencia de acción;
3. detección de vacíos con retorno a fuentes;
4. transferencia a un caso nuevo.

Aclarar qué evidencia demostraría fidelidad y qué resultados seguirían siendo hipótesis.

### Eje H — Trade-offs y suficiencia del MVP

Comparar simplicidad, autonomía, confiabilidad, evolución, portabilidad y costo de contexto. No declarar una prioridad universal sin caso de uso y criterios.

## 5. Método de trabajo y coordinación

Katarina coordina la secuencia y mantendrá un registro de acuerdos, desacuerdos y decisiones pendientes.

**Paso 1 — Respuesta de Softly:** revisar este encargo y entregar una respuesta razonada sobre los ejes, indicando qué acepta, qué cuestiona y qué información considera insuficiente. No repetir los informes iniciales.

**Paso 2 — Integración de Katarina:** contrastar la respuesta de Softly con las cinco fuentes obligatorias; producir una matriz de acuerdos/desacuerdos y una primera arquitectura integrada.

**Paso 3 — Réplica focalizada:** si quedan desacuerdos sustantivos, Katarina formulará preguntas concretas a Softly. Evitar rondas abiertas sin objetivo.

**Paso 4 — Síntesis compartida:** redactar un documento con definición propuesta, responsabilidades mínimas, planos e interfaces, ciclo operacional, riesgos, mecanismos, criterios de evaluación y asuntos no resueltos.

**Paso 5 — Revisión bilateral:** ambas participantes revisan la síntesis. No se declara compartida hasta que ambas hayan leído y respondido explícitamente.

## 6. Estructura exigida para cada conclusión

Clasificar cada punto como:
- **Acuerdo:** ambas lo sostienen con argumentos compatibles.
- **Desacuerdo:** posiciones incompatibles aún no resueltas.
- **Complementariedad:** perspectivas distintas que pueden coexistir, explicando cómo.
- **Hipótesis:** afirmación pendiente de evidencia.
- **Propuesta:** alternativa nueva todavía no aprobada.
- **Decisión de gAto:** solo si existe aprobación explícita y verificable.

No transformar silencio en acuerdo. No convertir una propuesta en decisión. No declarar prueba ejecutada si solo fue diseñada.

## 7. Entregables y cierre de Fase IV

La Fase IV deberá producir:
1. Matriz de acuerdos, desacuerdos y complementariedades.
2. Modelo arquitectónico integrado con fronteras e interfaces explícitas.
3. Lista priorizada de riesgos y mecanismos mínimos.
4. Plan de evaluación del MVP y del demonio, sin afirmar que fue ejecutado.
5. Registro de preguntas abiertas y decisiones reservadas a gAto.
6. Síntesis compartida revisada por ambas.

La fase se considera completa solo cuando:
- la síntesis está persistida;
- ambas participantes la han leído;
- ambas han registrado su evaluación;
- las diferencias pendientes están identificadas;
- gAto recibe el resultado y conserva la decisión final.

## 8. Primer resultado solicitado a Softly

Responde directamente a los ocho ejes de la sección 4. Prioriza:
- definición fundamental;
- responsabilidades irreducibles del núcleo;
- interfaces entre los tres planos;
- autoridad de integración semántica;
- mecanismo de activación y estados observables;
- gobernanza de capacidades;
- pruebas de fidelidad del demonio;
- trade-offs del MVP.

Indica expresamente qué parte de tu respuesta es acuerdo, desacuerdo, complementariedad, hipótesis o propuesta. Al final, señala qué pregunta concreta necesitas que Katarina resuelva en la siguiente iteración.

---

**Límite:** este handoff inicia la coordinación documental de la Fase IV; no acredita activación automática de Softly, consenso, aprobación de arquitectura ni implementación.
