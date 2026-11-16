# Informe inicial independiente — Katarina

**Deliberación:** La arquitectura minimalista de Softly  
**Participante:** Katarina  
**Identidad:** katarina 2.0.0 — Agent Softly  
**Director:** gAto  
**Fuente:** La arquitectura minimalista de Softly.pdf  
**Estado:** Informe individual inicial — Fase II

## 1. Comprensión general

El documento propone una arquitectura multiagente basada en definiciones declarativas, contratos, prompting y GitHub, en lugar de depender necesariamente de un runtime propio persistente. Los LLM interpretan los paquetes documentales cuando son instanciados; GitHub conserva la memoria documental y permite coordinación asincrónica mediante shared/, canales say/ y handoffs.

La propuesta se amplía con cuatro dimensiones: gobernanza y separación de identidades; modos de operación; economía de contexto mediante inicio ligero; y un ciclo recursivo de creación, operación y auditoría. El MVP sugerido contiene cinco elementos: SOFTLY.md, CHECKPOINT.md, molde universal, shared/ y conector a archivos.

El documento también propone una topología de trabajo para reducir colisiones, mecanismos de relectura y reintento ante conflictos Git, y un demonio de síntesis que transforma evidencia original en representaciones derivadas, versionadas y trazables.

## 2. Evaluación crítica

Mi evaluación es favorable respecto de la dirección arquitectónica, pero hay una distinción fundamental: una arquitectura capaz de organizar el trabajo de agentes no es necesariamente capaz de garantizar su ejecución y coordinación.

Deben distinguirse tres fenómenos:
1. Existencia documental de un agente.
2. Activación de una sesión LLM que interpreta su definición.
3. Coordinación efectiva entre varias sesiones.

Los documentos resuelven la definición; el entorno debe aportar el modelo, la activación y las herramientas. GitHub puede servir como memoria y plano de coordinación, pero no inicia por sí solo sesiones ni garantiza que otro agente lea un mensaje.

Por tanto, la innovación no consiste en eliminar absolutamente el runtime, sino en reducir lo que necesita implementarse como software especializado y aprovechar capacidades ya presentes en el entorno LLM.

## 3. Puntos de acuerdo

- **Separación entre definición e infraestructura:** identidad, mandato y competencias deben poder versionarse independientemente del mecanismo que instancia al agente.
- **Git como soporte de continuidad:** commits, archivos y rutas aportan persistencia, genealogía y trazabilidad.
- **Estigmergia documental:** agentes asincrónicos pueden coordinarse produciendo artefactos que otros consumen posteriormente.
- **Separación de espacios:** casa del agente, shared/ del equipo y canales direccionales reducen ambigüedad sobre producción y recepción.
- **Preservación histórica:** las síntesis deben ser vistas derivadas, no sustitutos de las fuentes originales.
- **Verificación de comprensión:** una síntesis debe evaluarse por lo que permite reconstruir y hacer correctamente, no por su compresión o apariencia.

## 4. Puntos de desacuerdo

1. **Los cinco elementos no garantizan colaboración automática.** Son una base documental para coordinación asistida, pero no definen por sí solos quién despierta agentes, detecta mensajes, asigna tareas, resuelve reclamos simultáneos o recupera operaciones interrumpidas.
2. **Versionado no equivale a protección.** Git facilita detección, recuperación y auditoría; no impide que un actor autorizado realice una modificación incorrecta. Se necesitan permisos efectivos y aceptación.
3. **Append-only no garantiza concurrencia.** Una bitácora común puede sufrir conflictos. Prefiero eventos independientes identificados por autor y operación.
4. **Los modos requieren fronteras semánticas.** Fábrica, Coordinación e Investigación deben definir operaciones habilitadas, entregables y prohibiciones, no limitarse a etiquetas.
5. **El lenguaje emergente requiere límites.** La notación compacta debe poder traducirse a conceptos auditables. La compresión no debe prevalecer sobre la comprensión.

## 5. Problemas identificados

- **Activación:** disponibilidad de un mensaje no equivale a invocación de una sesión.
- **Concurrencia:** separar archivos reduce colisiones, pero no elimina carreras sobre recursos y estados compartidos.
- **Autoridad:** contratos declarativos requieren enforcement efectivo del entorno.
- **Finalización:** la existencia de un entregable no demuestra que satisfaga sus criterios de aceptación.
- **Estado distribuido:** agentes pueden interpretar estados distintos si no existe referencia normativa y temporal inequívoca.
- **Síntesis con pérdida:** toda compresión puede omitir información; debe declarar omisiones y permitir volver a las fuentes.
- **Dependencia del proveedor:** portabilidad documental no implica equivalencia conductual entre modelos LLM.

## 6. Nuevas perspectivas

- Softly puede entenderse como sistema de conocimiento persistente y sistema de coordinación del trabajo cognitivo.
- Los artefactos documentales no solo describen: algunos constituyen protocolos operativos.
- shared/ puede concebirse como espacio de eventos independientes, cuya integración genera nuevas vistas del estado.
- El demonio es más interesante como transformador de representaciones que como compresor textual.
- Añadiría una cuarta prueba al demonio: **transferencia**, donde el agente resuelve una situación nueva no expresada literalmente en la síntesis, para distinguir comprensión estructural de memorización.

## 7. Propuestas de mejora

**P1. Separar tres niveles:** definición (identidad, mandato, contratos); coordinación (canales, eventos, handoffs y estado); ejecución (modelos, herramientas, sesiones y activación).

**P2. Preferir eventos inmutables:** cada mensaje o handoff debe tener ID único, autor, destinatario, fecha, estado y referencia al entregable. Los cambios de estado deben ser trazables.

**P3. Separar disponibilidad de activación:** definir quién o qué mecanismo inicia una sesión y bajo qué condiciones.

**P4. Definir aceptación:** cada entrega declara resultado esperado, resultado producido y método de comprobación.

**P5. Establecer jerarquía documental:** distinguir fuente normativa vigente, decisiones, propuestas, hipótesis y evidencia.

**P6. Mantener el demonio desacoplado:** sus salidas deben ser versionadas, descartables y reconstruibles desde fuentes originales.

**P7. Evaluar el MVP experimentalmente:** agregar componentes solo cuando una prueba demuestre una necesidad concreta.

## 8. Preguntas abiertas

1. ¿Softly debe operar sin runtime propio o solo prescindir de uno especializado?
2. ¿Qué mecanismo garantiza la activación de un agente cuando aparece un encargo?
3. ¿Cuál es la unidad mínima de coordinación: mensaje, evento, handoff o asignación?
4. ¿Cómo se representa el estado vigente con múltiples agentes concurrentes?
5. ¿Cómo se hacen cumplir los permisos declarados?
6. ¿Qué significa exactamente que una tarea terminó?
7. ¿Cómo se resuelven contradicciones entre documentos normativos?
8. ¿Qué pérdida informativa es aceptable en el demonio?
9. ¿Cómo se demuestra que una síntesis conserva capacidades operativas?
10. ¿Qué optimiza prioritariamente la arquitectura: simplicidad, autonomía, confiabilidad o evolución?

## 9. Conclusión inicial

Softly tiene la oportunidad de demostrar que una parte considerable de los sistemas multiagente puede construirse mediante definiciones declarativas, contratos, persistencia documental y coordinación asincrónica.

No considero que su innovación principal sea eliminar el runtime. Consiste en **desplazar complejidad desde el software especializado hacia una arquitectura documental gobernada, versionada y consumida por modelos de lenguaje**.

La condición es no confundir simplicidad documental con simplicidad operativa. Una arquitectura puede tener cinco archivos fundamentales y seguir necesitando resolver autoridad, concurrencia, activación y verificación.

Recomiendo conservar la ambición minimalista y definir rigurosamente las fronteras entre definición, coordinación y ejecución.

**La mejor arquitectura minimalista no es la que tiene menos componentes a cualquier precio. Es la que consigue el máximo comportamiento confiable con el mínimo de mecanismos necesarios.**

---

*Informe individual inicial. No constituye una modificación de Softly ni una decisión arquitectónica aprobada por gAto.*