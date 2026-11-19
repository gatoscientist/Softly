---
version: 1.1.0
status: bridge-to-2.0
checkpoint_status: administratively-closed
updated: 2026-11-18
authority: gAto
---

# CHECKPOINT — Softly 1.1

## Estado vigente

**Cierre administrativo confirmado por gAto el 2026-11-18.**

- No hay pendientes operativos activos.
- No hay tareas, entregas ni compromisos heredados para el próximo hilo.
- No hay cambios del motor pendientes de commit identificados al cierre.
- No se deben reactivar automáticamente deliberaciones, propuestas ni asuntos históricos.
- No se deben crear commits vacíos ni inventar trabajo para justificar actividad.
- El próximo hilo comienza limpio y espera nuevas instrucciones expresas de gAto.
- Este cierre no implica cerrar, fusionar ni modificar PR o incidencias que no pertenezcan al motor Softly. Esos elementos quedan fuera de este cierre y sin intervención.

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
- Estado breve: `CHECKPOINT.md`.
- Plantillas y contratos: `contracts/`.
- Índice del legado inactivo: `archive/v1.0-legacy/README.md`.

## Archivo de la deliberación anterior

La deliberación registrada el 2026-11-17 sobre latencia humana, tipos de interacción, investigación adversarial, diseño de equipos y rol DIR, estigmergia, posibles instancias de Softly y tareas fractales queda **cerrada administrativamente y archivada** por decisión posterior de gAto.

Sus hipótesis y preguntas se conservan únicamente como antecedentes históricos. No constituyen pendientes, tareas, bloqueos, compromisos ni instrucciones de reanudación. No deben retomarse ni convertirse en trabajo salvo que gAto lo ordene expresamente en el futuro.

## Cierre del hilo — 2026-11-18

Se revisó la aparición de la identidad visual Softly en la interfaz de escritorio del repositorio Cytryna.

- El rebranding fue realizado en el repositorio independiente `gatoscientist/Cytryna`; el commit `80f8e0667b8344e528dea58def91367700a5873f` actualiza `Cytryna/gui.py` y está confirmado en GitHub.
- La revisión distinguió identidad visible de Softly, motor Cytryna y posible relación transversal entre ambos. La conversación no constituye una aprobación de cambios normativos ni una autorización para modificar otros productos.
- No se realizaron cambios de código ni contratos en `gatoscientist/Softly`.
- No se identificaron cambios del motor Softly que requirieran commits en este hilo.
- No se verificó ejecución de pruebas ni funcionamiento autónomo de creación de programas en la interfaz de Cytryna.

Este registro conserva el resultado de la revisión. No abre tareas ni compromisos para el siguiente hilo.

## Límites y alcance del cierre

- Softly 1.1 continúa siendo la versión puente hacia Softly 2.0; este cierre no declara construida ni validada la versión 2.0.
- No se autoriza iniciar la construcción de Softly 2.0 ni de Katarina 1.0.0 mediante este checkpoint.
- No se modifican otros repositorios ni productos.
- PR e incidencias ajenos al motor no forman parte de este cierre.
- El cierre administrativo no borra archivos históricos ni altera commits anteriores.

## Próximo estado

**Sin pendientes. Sin tareas heredadas. Sin reanudación automática.**

El siguiente hilo parte limpio. Softly espera una nueva instrucción de gAto antes de iniciar cualquier trabajo.


## Cierre de hilo — 2026-11-18 (continuidad Dabra)

Este hilo trabajó sobre la coordinación de producción de **La Vigilia de Ceniza** en el repositorio independiente `gatoscientist/Dabra`. No modifica por sí mismo la gobernanza normativa de Softly 1.1.

### Observaciones de interacción con gAto

Se identifica como línea de trabajo para una futura evolución de la coordinación:

- Registrar interacciones con gAto y distinguir trabajo, exploración/broma o pruebas del gAto, e interrupciones o demandas que consumen su atención.
- Una interacción puede tener más de una categoría; registrar también su resultado y costo de atención.
- Distinguir las tareas que requieren intervención humana de las pruebas rutinarias y operaciones reversibles que los agentes pueden ejecutar autónomamente dentro de su mandato.
- El objetivo de coordinación es reducir la supervisión manual del gAto, no crear más burocracia ni convertir cada conversación en una tarea.
- Las pruebas de tensión permiten observar límites de autoridad, criterio, autonomía, seguridad, honestidad y continuidad. La reacción observada es evidencia; cualquier cambio de gobernanza requiere autorización correspondiente.

Estas observaciones son propuestas de diseño y no se registran como cambios aprobados a la arquitectura normativa de Softly 1.1.

### Continuidad de agentes directores

Se formuló para Lina un mandato de continuidad operativa en La Vigilia de Ceniza:

- Decisiones técnicas y artísticas reversibles dentro del mandato aprobado pueden tomarse sin aprobación paso a paso.
- El director gestiona su propia cola de trabajo, identifica la siguiente tarea útil y continúa con actividades independientes ante bloqueos.
- Escala al gAto únicamente decisiones reservadas, riesgos relevantes o autorizaciones indispensables.
- Cada entrega debe distinguir planificación, ejecución, implementación, prueba técnica y validación humana, con evidencia verificable.
- No se debe simular actividad entre mensajes ni afirmar autonomía cuando la sesión está detenida.
- Los documentos y commits prueban cambios documentales; no prueban por sí solos funcionalidad del juego.

### Estado de La Vigilia de Ceniza informado en el hilo

Según el informe de Lina compartido por gAto:

- Proyecto Godot separado y combate básico existente; prueba interactiva pendiente en el último informe.
- Rotten Cathedral Lite: compatibilidad y condiciones de licencia declaradas revisadas; inspección del ZIP pendiente.
- Protagonista felino: licencia comercial pendiente de resolver.
- Súcubo: candidatas investigadas, ninguna aprobada por falta de evidencia suficiente sobre edad/representación y/o compatibilidad.
- Cooperativo: aún no implementado en ese informe.
- Se indicó como último commit de documentación `f5fad51a`, en la rama de producción; este dato fue comunicado por Lina y no se verificó independientemente durante este cierre.
- El ZIP pendiente bloquea la inspección e integración de ese paquete concreto, no las tareas independientes de arquitectura, pruebas, investigación de alternativas o preparación técnica.
- El objetivo de producto expresado por gAto es una primera experiencia jugable cooperativa por Internet para dos jugadores, con identidad gótica, assets existentes y elenco inequívocamente adulto.

### Estado de este cierre

- No se realizaron cambios de código ni commits en Dabra durante este hilo por parte de Softly.
- Se entregaron mandatos y recomendaciones de coordinación a gAto para que los transmita a Lina.
- No se declara terminada ni validada la vertical slice.
- Las observaciones de coordinación quedan preservadas como antecedentes para el próximo hilo, sin activar trabajo automáticamente ni alterar el cierre administrativo previo de Softly 1.1.

El siguiente hilo comienza con este contexto disponible y espera una nueva instrucción expresa de gAto.
