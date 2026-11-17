---
version: 1.1.0
status: bridge-to-2.0
---

# CHECKPOINT — Softly 1.1

- **Estado:** Softly 1.1 activa.
- **Responsable:** Softly.
- **Autoridad:** gAto.
- **Versión:** 1.1.0.
- **Función:** puente operativo y deliberativo hacia Softly 2.0.
- **Actualizado:** 2026-11-17.

## Acuerdos base consolidados (S2-1 / S2-2 / S2-3)

1. Núcleo cerrado: **Prompting + Contratos + GitHub**.
2. Runtime excluido de la arquitectura y fuera de norma.
3. Tres planos lógicos: Definición, Coordinación y Ejecución.
4. Tres dimensiones: Coordinación propia, Coordinación entre pares y Orquestación.
5. Coordinación sistémica es responsabilidad transversal explícita, no cuarta dimensión.
6. La tarea es la unidad canónica de coordinación.
7. GitHub conserva señales estigmérgicas con estado, responsable y acción habilitada.
8. `inbox` y `outbox` son vistas lógicas; no hay buzones físicos ni canales `*say/`.
9. Los archivos y commits no despiertan sesiones ni conceden autoridad automáticamente.
10. Solo cuatro clases físicas operativas: Paquete, Tarea, Entregable y Checkpoint.
11. Evidencia y verificaciones acompañan al Entregable; commits aportan trazabilidad.
12. Katarina conserva la responsabilidad indivisible de ingeniería e integración.
13. La Cápsula Directora usa especialistas como lentes internos, sin identidades, buzones ni commits propios.
14. Softly custodia coherencia del ecosistema; gAto conserva autoridad humana última.
15. La historia v1.0 se preserva como memoria, pero su burocracia queda inactiva y fuera del arranque.
16. `research/syntheses/` y `research/coordination/` se conservan para consulta bajo demanda.
17. TITAN, Cytryna y gAtoSD permanecen intactos y fuera de alcance.

## Superficie operativa

- Constitución y punto de entrada: `SOFTLY.md`.
- Estado breve: `CHECKPOINT.md`.
- Plantillas y contratos únicos: `contracts/`.
- Índice del legado inactivo: `archive/v1.0-legacy/README.md`.

## Límites conocidos

- Softly 1.1 no es Softly 2.0.
- La equivalencia funcional completa aún debe probarse mediante tareas reales.
- No se ha creado Katarina 1.0.0 ni se ha modificado su repositorio.
- No se han modificado ResKata, TITAN, Cytryna ni gAtoSD.
- La declaración de legado inactivo no borra archivos ni altera la historia Git.

## Acción habilitada inmediata

**Deliberación en vivo para afinar Softly 2.0**, usando la experiencia de Softly 1.1 para identificar vacíos, contradicciones y decisiones pendientes.

No iniciar la construcción de Softly 2.0 ni Katarina 1.0.0 sin el mandato correspondiente.

## Deliberación en curso — 2026-11-17 (gAto / Softly / Katarina)

**Estado:** abierta; no constituye mandato de implementación ni modifica los acuerdos S2-1/S2-2/S2-3.  
**Punto de reanudación:** gAto está escuchando la deliberación de Katarina y volverá después. Al regresar, continuar desde este checkpoint sin exigirle repetir el contexto.

### Señales e hipótesis aportadas por gAto

1. **Latencia humana:** la diferencia entre los tiempos de los agentes y la disponibilidad humana puede convertir a gAto en cuello de botella. El sistema debe poder avanzar de forma segura mientras gAto escucha, piensa o está ausente, y presentar al regreso un estado breve, comprensible y accionable.
2. **Separación de interacciones:** distinguir conversación con gAto, declaración/orden de gAto, deliberación e investigación, coordinación entre agentes y comunicación agente–gAto. No asumir que todas requieren la misma extensión, estructura o formalidad.
3. **Investigación adversarial:** investigar para encontrar fallas, condiciones de choque, bloqueos y Cisnes Negros; no validar ideas por cortesía. Se menciona la posibilidad de un equipo Antiauditor. TITAN contiene material pertinente que gAto quiere considerar.
4. **Diseño no antropomórfico de equipos:** las interacciones, organigramas y formaciones de agentes no tienen por qué imitar equipos humanos. Explorar combinaciones multidisciplinarias inusuales y el rol DIR.
5. **Estigmergia y ciclo de vida de señales:** estudiar señales con tiempo de vida sin perder trazabilidad. Hipótesis del Demonio de Síntesis: retirar limpiamente señales vencidas, conservar evidencia de su expiración y archivar material histórico sin cargarlo rutinariamente. Tres capas propuestas: (a) la señal desaparece de la superficie activa; (b) queda visible por qué desapareció; (c) el material se conserva en archivo y no se consulta por defecto. Se menciona a Audeline como posible responsable de registrar la expiración.
6. **Tres instancias/modos Softly:** propuesta de una Softly para deliberar continuamente con gAto, una Softly Fábrica y una Softly Coordinadora. Compartirían el repositorio, pero no necesariamente el mismo contexto/paquete de instrucciones. Es propuesta por deliberar, no decisión aprobada.
7. **Tareas fractales:** evitar que una conversación, una corrección de ritmo o una idea se conviertan automáticamente en tareas, subtareas o reformas de gobernanza. En deliberación, no generar planes ni tareas hasta que gAto solicite construcción. Ante una orden concreta, ejecutar con profundidad 1 y no inventar pre-tareas. En Fábrica, terminar y verificar; no dejar por defecto todo como experimental. Estas reglas son propuestas de diseño para contrastar, no cambios normativos ya aplicados.

### Preguntas abiertas para la próxima deliberación

- ¿Cómo reducir el cuello de botella humano sin quitar a gAto autoridad ni saturarlo con notificaciones?
- ¿Qué tipos de interacción existen, cómo se reconocen y qué formato/longitud corresponde a cada una?
- ¿Cómo se activa una investigación adversarial y cómo se evita que se transforme en complacencia o burocracia?
- ¿Qué aporta TITAN al diseño de comunicación y equipos? ¿Qué papel concreto tendría DIR?
- ¿Cómo se implementan expiración, desaparición de señales y trazabilidad histórica sin confundir archivo con estado activo?
- ¿Las tres Softlys deben ser instancias, perfiles/paquetes o modos separados? ¿Qué comparten y qué no?
- ¿Qué mecanismo mínimo corta las tareas fractales y permite cerrar entregas?

### Instrucción de reanudación

Al volver gAto, escuchar primero el reporte de Katarina e incorporar sus observaciones a esta deliberación. Contrastar coincidencias y desacuerdos con estas hipótesis. No ejecutar cambios de arquitectura, no modificar otros repositorios y no declarar decisiones cerradas sin deliberación/mandato explícito de gAto.

**Nota de alcance:** este registro preserva el contexto para reanudar; no afirma que las propuestas estén validadas ni que se haya investigado TITAN en esta sesión.

