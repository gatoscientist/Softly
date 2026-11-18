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
