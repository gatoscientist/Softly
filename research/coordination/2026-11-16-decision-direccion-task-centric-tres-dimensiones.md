# Decisión de dirección — coordinación task-centric y modelo de tres dimensiones

- **Fecha:** 2026-11-16
- **Dirección humana:** gAto
- **Registro:** decisión de orientación para continuar investigación y diseño
- **Estado:** dirección adoptada como base de trabajo; implementación y piloto aún no autorizados
- **Fuentes:** investigación independiente de Softly; investigación independiente y comparación final de Katarina.

## 1. Decisión de gAto

gAto decide avanzar tomando como base la **Alternativa B: coordinación centrada en tareas y dependencias** propuesta convergentemente por Softly y Katarina.

La tarea será el punto de partida del modelo de coordinación. Mensajes, eventos, entregables y espacios de trabajo se tratarán como responsabilidades conceptuales diferenciadas y vinculadas a las tareas cuando corresponda. No se impone todavía una estructura física de directorios ni se aprueba una migración.

La dirección adoptada es continuar la investigación y el diseño conceptual de esta alternativa, preservando evidencia, límites y diferencias entre ambos informes.

## 2. Preferencia por tres dimensiones

gAto manifiesta preferencia por organizar el modelo de coordinación en **tres dimensiones**, en lugar de cuatro:

1. **Coordinación propia:** el agente organiza y conduce su propio trabajo dentro de su autoridad, alcance y restricciones.
2. **Coordinación entre pares:** los participantes gestionan dependencias, interfaces, recursos e intercambios necesarios para colaborar.
3. **Orquestación:** una instancia o rol con autoridad organiza trabajo distribuido, asigna responsables, gestiona dependencias, integra resultados y conduce el avance hacia el objetivo.

Esta preferencia es una decisión de organización conceptual para la siguiente etapa de investigación. No modifica por sí sola contratos, taxonomías, moldes, schemas ni instrucciones normativas.

## 3. Pregunta abierta preservada a petición de gAto

Katarina plantea una cuestión que debe seguir explícitamente abierta:

**¿La orquestación cubre suficientemente la coordinación sistémica, o la coordinación sistémica representa una responsabilidad/capacidad diferenciada que no queda completamente expresada dentro de la orquestación?**

Katarina había propuesto cuatro dimensiones funcionales: autocoordinación, colaboración entre pares, coordinación directiva y coordinación sistémica. Softly había agrupado la dimensión directiva en orquestación y no había separado la sistémica como dimensión autónoma.

La preferencia actual de gAto es de tres dimensiones. Esto **no resuelve por anticipado** el alcance de la orquestación ni elimina la pregunta de Katarina. La siguiente investigación debe examinar si la coordinación sistémica:
- queda comprendida dentro de la orquestación;
- es una especialización o responsabilidad transversal de la orquestación;
- o requiere describirse como una capacidad distinta, sin que ello obligue a convertirla en una cuarta dimensión principal.

No se debe presentar ninguna de estas alternativas como conclusión hasta que exista análisis explícito y decisión de gAto.

## 4. Alcance de lo adoptado y límites

Queda adoptada como dirección de trabajo:
- avanzar desde la Alternativa B task-centric;
- desarrollar el modelo conceptual antes de definir directorios o schemas;
- estructurar la coordinación en tres dimensiones como hipótesis/directriz de diseño;
- investigar expresamente la relación entre orquestación y coordinación sistémica.

No queda autorizado ni declarado:
- piloto en un repositorio o equipo concreto;
- migración de directorios o datos;
- modificación de SOFTLY.md, contratos, moldes, taxonomías o schemas;
- implementación de runtime, A2A, MCP o workflow engine;
- validación experimental de la propuesta.

## 5. Próxima etapa de investigación y diseño

La continuación debe:
1. Definir el alcance observable de cada una de las tres dimensiones y sus límites de autoridad.
2. Analizar la coordinación sistémica: objeto, responsabilidades, interfaces, escala, autoridad y relación con la orquestación.
3. Contrastar el modelo con los casos de los seis repositorios ya estudiados, sin confundir evidencia documental con ejecución.
4. Proponer un modelo conceptual mínimo de tarea, mensaje, evento, artifact y workspace, sin convertir automáticamente cada entidad en un directorio.
5. Identificar qué decisiones requieren definición adicional de gAto antes de un piloto.
6. Entregar una propuesta revisada con preguntas, riesgos, criterios de aceptación y opciones concretas para decisión humana.

## 6. Fuentes preservadas

- [Investigación independiente de Softly](2026-11-16-investigacion-coordinacion-universal-y-redisenio-arquitectura.md).
- [Investigación independiente y comparación final de Katarina](https://github.com/gatoscientist/Katarina/blob/main/shared/2026-11-16-investigacion-coordinacion-katarina-comparacion-softly.md).
- [Cierre del hilo de investigación de Katarina](https://github.com/gatoscientist/Katarina/blob/main/shared/threads/2026-11-16-investigacion-coordinacion-cierre.md).

**Principio de trazabilidad:** adoptar una dirección de investigación no equivale a aprobar su implementación. La pregunta sistémica de Katarina queda preservada como asunto abierto y explícito.
