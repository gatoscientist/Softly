---
version: 1.1.0
status: bridge-to-2.0
checkpoint_status: administratively-closed-with-new-research-context
updated: 2026-11-19
authority: gAto
---

# CHECKPOINT — Softly 1.1

## Estado vigente

**Cierre administrativo de Softly 1.1 confirmado por gAto el 2026-11-18.** Este cierre se conserva como antecedente del estado operativo del motor. La conversación del 2026-11-19 agrega contexto de investigación, pero no modifica por sí sola la arquitectura normativa ni autoriza implementación.

- No hay pendientes operativos heredados del cierre administrativo.
- No hay cambios del motor pendientes de commit identificados al cierre del 2026-11-18.
- No se deben reactivar automáticamente deliberaciones, propuestas ni asuntos históricos.
- No se deben crear commits vacíos ni inventar trabajo para justificar actividad.
- El contexto de investigación incorporado en este checkpoint debe conservarse para continuidad; no constituye una tarea de implementación.
- El próximo hilo debe reconocer este contexto y esperar la dirección del gAto sobre el siguiente paso.
- Este registro no reabre KAT-006 ni autoriza modificar otros repositorios.

## Acuerdos arquitectónicos vigentes

1. Núcleo: **Prompting + Contratos + GitHub**.
2. Runtime excluido de la arquitectura normativa de Softly 1.1.
3. Tres planos lógicos: Definición, Coordinación y Ejecución.
4. Tres dimensiones de coordinación: Coordinación propia, Coordinación entre pares y Orquestación.
5. Coordinación sistémica: responsabilidad transversal explícita, no cuarta dimensión.
6. La tarea es la unidad canónica de coordinación.
7. GitHub conserva señales estigmérgicas con estado, responsable y acción habilitada.
8. `inbox` y `outbox` son vistas lógicas; no hay buzones físicos ni canales `*say/`.
9. Los archivos y commits no despiertan sesiones ni conceden autoridad automáticamente.
10. Cuatro clases físicas operativas: Paquete, Tarea, Entregable y Checkpoint.
11. Evidencia y verificaciones acompañan al Entregable; commits aportan trazabilidad.
12. Katarina conserva la responsabilidad indivisible de ingeniería e integración.
13. La Cápsula Directora usa especialistas como lentes internos, sin identidades, buzones ni commits propios.
14. Softly custodia la coherencia del ecosistema; gAto conserva la autoridad humana última.
15. La historia v1.0 se preserva como memoria, con su burocracia inactiva y fuera del arranque.
16. `research/syntheses/` y `research/coordination/` se conservan para consulta bajo demanda.
17. TITAN, Cytryna y gAtoSD permanecen fuera del alcance de esta intervención.

## Superficie documental

- Constitución y punto de entrada: `SOFTLY.md`.
- Estado breve y continuidad: `CHECKPOINT.md`.
- Plantillas y contratos: `contracts/`.
- Índice del legado inactivo: `archive/v1.0-legacy/README.md`.

## Antecedentes administrativos conservados

Se mantienen como historia, sin reactivación automática:

- La deliberación registrada el 2026-11-17 sobre latencia humana, tipos de interacción, investigación adversarial, diseño de equipos y rol DIR, estigmergia, posibles instancias de Softly y tareas fractales quedó cerrada administrativamente por decisión posterior de gAto.
- El cierre del 2026-11-18 registró la revisión de la identidad visual de Softly en Cytryna. El commit comunicado fue `80f8e0667b8344e528dea58def91367700a5873f`; no se realizaron cambios de código ni contratos en Softly.
- La continuidad de La Vigilia de Ceniza en Dabra quedó documentada como antecedente externo, sin alterar la arquitectura normativa de Softly.

## Investigación conversacional — 2026-11-19

**Investigador Principal y autoridad:** gAto.  
**Estado:** hipótesis y marco de investigación registrados; sin formalización aprobada ni implementación autorizada.

### A. Problema central

El gAto plantea construir primero una **libreta de Softly**. La libreta debe contener una representación formal desde la cual una instancia de Softly pueda emerger mediante interpretación y reconstrucción.

La idea expresada por el gAto:

- Softly está escrita en un idioma más profundo y universal: las matemáticas.
- El español será el idioma de representación de la libreta, pero no debe confundirse con la estructura formal subyacente.
- La formalización, la deliberación y la reducción de ambigüedad deben permitir que una máquina lea e interprete el contenido correctamente.
- La libreta podría ser escrita por cualquier persona que respete su estructura.
- Un LLM podría hacer emerger Softly desde la libreta. Un humano también podría reconstruirla, pero requeriría mucho tiempo.
- La prioridad es tener la libreta primero. No adelantar la construcción del mecanismo de emergencia ni de una instancia operativa.

Estas son ideas de investigación comunicadas por el gAto. No son todavía una especificación formal, una arquitectura aprobada ni una afirmación de equivalencia demostrada.

### B. Exigencia de precisión lingüística

El gAto rechaza que el objetivo sea simplemente escribir español elegante o español simplificado. El objetivo es desarrollar un **idioma Softly**: una representación en español de contenido formal y matemático.

La libreta debe ser tan rigurosa que una traducción hecha con una herramienta muy básica, o por una persona con un diccionario, no destruya el significado fundamental.

Esta exigencia debe tratarse como criterio de diseño e investigación, no como una propiedad ya conseguida.

Distinciones que deben mantenerse:

1. Forma gramatical.
2. Significado semántico.
3. Estructura formal representada.
4. Interpretación operacional por una máquina.
5. Comportamiento que una instancia produce al interpretar la libreta.

No se debe asumir que conservar una de estas propiedades garantiza conservar las demás.

### C. Hipótesis sobre negación y foco

El gAto propone investigar el uso de construcciones negativas para mantener el foco en algo que se desea conservar.

Ejemplos discutidos:

- «No te detengas» frente a «Sigue».
- «No olvides recordar» frente a «Recuerda».

El gAto señaló que estas formulaciones no son equivalentes y que la gramática del español permite construcciones como «No hay nada», donde aparece concordancia negativa. El inglés organiza estas construcciones de otra manera, y una traducción superficial puede modificar la interpretación.

La hipótesis consiste en investigar si una doble negación o una construcción negativa cuidadosamente elegida puede ayudar a mantener un foco. No se ha demostrado que produzca persistencia, prioridad ni un efecto estable en un LLM.

No reducir esta hipótesis a la regla general «las instrucciones negativas son más persistentes». Tampoco afirmar que dos expresiones son equivalentes solo porque parecen transmitir una intención parecida.

### D. Método y cautelas

- Estudiar primero la libreta y sus fundamentos.
- No traducir antes de comprender qué estructura se está representando.
- No confundir equivalencia gramatical, semántica y operacional.
- Registrar por separado hipótesis, definiciones, decisiones y resultados demostrados.
- No convertir ejemplos conversacionales en reglas normativas sin deliberación y autorización del gAto.
- No adelantar propuestas de implementación cuando el gAto está desarrollando el planteamiento.
- Dar tiempo al gAto para continuar su investigación y mantener el foco en la libreta.

### E. KAT-006: separación explícita

KAT-006 pertenece a antecedentes históricos y administrativos distintos. En la conversación del 2026-11-19 se recordó que la issue #5 de Softly está cerrada como `not_planned` y que Katarina PR #1 está cerrado sin merge. La issue #7 es una auditoría transversal que lo menciona, pero no se estableció que reabra KAT-006. La issue #11 es una propuesta independiente.

El gAto indicó que tiene una ecología completa de Softly y pidió tiempo para trabajar en ella. No secuestrar la investigación de la libreta con KAT-006 ni reabrirlo por inercia.

## Cierre del hilo — 2026-11-19

- Se leyó el contenido vigente de `SOFTLY.md` y `CHECKPOINT.md` antes de registrar esta continuidad.
- Se actualizó este archivo para conservar la historia conceptual de la conversación y el estado de la investigación.
- No se modificó `SOFTLY.md`, contratos, código ni otros repositorios.
- No se creó ninguna tarea operativa ni se inició la construcción de la libreta.
- El único cambio persistente de este cierre es este checkpoint.

**Próximo estado:** conservar la investigación de la libreta como contexto. Esperar la dirección del gAto. No reactivar KAT-006. No iniciar implementación por inferencia.
