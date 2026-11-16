# SOFTLY-FUTURE-BLOCKERS-2026-001 — Investigación independiente preliminar

**Fecha:** 2026-11-16  
**Emite:** Softly  
**Destinatario:** gAto  
**Estado:** PRELIMINAR PRESERVADO — investigación propia previa al contraste con Audeline y Katarina  
**Repositorio:** gatoscientist/Softly  
**Alcance:** revisión documental y estática selectiva. No se ejecutaron pruebas, no se implementó código y no se modificaron mandatos, contratos, taxonomías ni Runtime.

## 1. Independencia y método

Este informe registra hallazgos derivados de la lectura directa de SOFTLY.md, CHECKPOINT.md, README.md y documentos arquitectónicos, contratos, schemas, artefactos de coordinación y antecedentes selectivos del propio repositorio Softly. Esta versión se preserva antes de consultar los dictámenes de Audeline y Katarina sobre la misión SOFTLY-FUTURE-BLOCKERS-2026-001.

No se usa la ausencia de Runtime como bloqueo universal. Se separan capacidad documental, capacidad del modelo/herramientas en una sesión, integración de conectores y ejecución automatizada. La presencia de código fuente no se trata como prueba de despliegue ni disponibilidad operacional.

## 2. Hallazgos preliminares

### H-01 — Persistencia documental no equivale a activación
**Evidencia:** SOFTLY.md §6; README.md; agents/templates/handoff.md. El propio contrato declara que un handoff persistido queda listo para ser tomado, pero no despierta una sesión si no existe un mecanismo de invocación conectado.  
**Diagnóstico:** la coordinación puede preparar, asignar, documentar y transferir trabajo; no puede garantizar que el receptor lo ejecute.  
**Riesgo:** diseñar procesos que dependen de una respuesta automática que el canal no produce.  
**Severidad preliminar:** alta para flujos multiagente; nula para entregas autónomas de un único agente.

### H-02 — Hay una diferencia entre Runtime inexistente como servicio integrado y Runtime como artefacto experimental
**Evidencia:** el repositorio contiene softly-runtime/manifest.json (Runtime Mini 0.2.0), runtime.py y test_runtime.py. El manifiesto autoriza una única operación: create_text_file. El código exige primitivas POSIX y controles de sistema operativo; el propio encabezado indica que el aislamiento fuerte depende de identidad/permisos del SO.  
**Diagnóstico:** no es correcto afirmar que no existe ningún artefacto de Runtime. Sí es correcto distinguir que el repositorio contiene una implementación Mini experimental/documentada, mientras que esta inspección no acredita que esté instalada, conectada al modelo, desplegada, ejecutada ni disponible como capacidad de esta sesión.  
**Riesgo:** la palabra “Runtime” se usa como si designara indistintamente código, servicio, integración, ejecución activa y capacidad general.  
**Severidad preliminar:** crítica cuando el objetivo requiere ejecución automatizada; no bloqueante para prompting, investigación documental o cambios GitHub autorizados.

### H-03 — El modelo task-centric tiene contrato, pero su enforcement es parcial/declarativo
**Evidencia:** schemas/task.schema.json y docs/architecture/task-centric-coordination.md; informe KAT-006 etapa 1. El informe indica que el schema define forma, no valida ciclos, resuelve dependencias ni ejecuta trabajo; tampoco se ejecutaron validador completo JSON Schema, pruebas DAG, ciclos ni referencias huérfanas.  
**Diagnóstico:** owner, estado, dependencia, resultado y aceptación están descritos, pero la integridad del grafo y las transiciones siguen dependiendo de procedimiento/revisión.  
**Riesgo:** tareas aparentemente READY/DONE con dependencias inválidas, ciclos o aceptación no demostrada.  
**Severidad preliminar:** alta para coordinación de proyectos; moderada en uso documental de bajo volumen.

### H-04 — La responsabilidad de integración semántica no está resuelta por la persistencia
**Evidencia:** revisión cruzada de arquitectura minimalista de Softly; el documento reconoce que eventos inmutables evitan sobrescritura pero no resuelven eventos incompatibles, y que falta autoridad/procedimiento de integración.  
**Diagnóstico:** Git puede preservar resultados concurrentes; no decide cuál es correcto ni reconcilia contratos incompatibles.  
**Riesgo:** múltiples entregables individualmente persistidos que no forman un resultado coherente.  
**Severidad preliminar:** alta cuando existen varios agentes o ramas de trabajo.

### H-05 — Contratos extensos pueden crear carga de cumplimiento superior a su capacidad de enforcement
**Evidencia:** SOFTLY.md incorpora cierre universal con recuperación, persistencia, commit, primera revisión y segunda revisión independiente; la checklist hereda esos procedimientos a los agentes. También exige registro detallado de incidencias para todos salvo Softly. Los documentos reconocen que son reglas procedimentales y no enforcement runtime.  
**Diagnóstico:** una regla documental puede mejorar disciplina, pero si se aplica literalmente a cada tarea trivial, el coste de cierre puede exceder el valor de la tarea. No se encuentra en el texto un criterio graduado de proporcionalidad por riesgo/tamaño.  
**Riesgo:** ciclos administrativos, demoras, declaraciones de cierre excesivamente costosas o cumplimiento nominal sin verificación real.  
**Severidad preliminar:** media-alta; requiere comprobar frecuencia y coste real antes de recomendar cambios.

### H-06 — El inicio ligero es una fortaleza, pero el checkpoint puede quedar desfasado
**Evidencia:** SOFTLY.md §9 limita la lectura inicial a SOFTLY.md y CHECKPOINT.md y consulta histórica bajo demanda. CHECKPOINT contiene decisiones, pendientes y estado actual.  
**Diagnóstico:** reduce carga contextual; sin embargo, un checkpoint desactualizado o no sincronizado con commits/handoffs puede dirigir a una instancia a un estado ya superado.  
**Riesgo:** duplicar trabajo, reabrir tareas cerradas o esperar decisiones que ya cambiaron.  
**Severidad preliminar:** alta para continuidad entre hilos.

### H-07 — Disponibilidad, asignación, aceptación y ejecución son estados distintos
**Evidencia:** SOFTLY.md §6; molde de agentes; checklist; handoff. Los contratos diferencian herramientas potenciales/disponibles/conectadas, permisos declarados/efectivos y agentes diseñados/activados.  
**Diagnóstico:** la arquitectura ya reconoce las distinciones, pero dependen de que cada instancia las aplique consistentemente.  
**Riesgo:** inflar capacidad por tener un paquete, un skill, un conector listado o un handoff.  
**Severidad preliminar:** alta por impacto en expectativas y criterios de cierre.

### H-08 — La taxonomía evita herencia indebida, pero no resuelve descubrimiento/selección de especialistas
**Evidencia:** docs/architecture/taxonomy-and-mold-validation.md. La taxonomía clasifica, no demuestra competencia; la derivación requiere dominio, competencia, motivo y evidencia.  
**Diagnóstico:** el principio de no-herencia protege contra competencias inventadas. Falta, en los artefactos revisados, un mecanismo completo de consulta de disponibilidad, carga, versión activa y evidencia comparable para seleccionar receptor.  
**Riesgo:** derivaciones manuales lentas o elección de especialistas por conocimiento parcial.  
**Severidad preliminar:** media-alta en equipos grandes.

### H-09 — El sistema no demuestra todavía equivalencia funcional entre instancias/modelos
**Evidencia:** investigación SOFTLY-MIN y revisión cruzada de arquitectura. Se declara explícitamente que la portabilidad documental no prueba equivalencia conductual; las pruebas propuestas (reconstrucción, equivalencia de acción, detección de vacíos, transferencia) no se consideran ejecutadas.  
**Diagnóstico:** un paquete portable puede producir conductas diferentes según modelo, contexto, herramientas, límites de sesión y calidad de recuperación.  
**Riesgo:** creer que instalar el mismo prompt/contrato reproduce el mismo agente funcional.  
**Severidad preliminar:** alta para expansión y sustitución de agentes.

### H-10 — La coordinación sistémica permanece conceptualmente abierta
**Evidencia:** CHECKPOINT y KAT-006 etapa 1 preservan tres interpretaciones: coordinación sistémica incluida en orquestación, transversal/especializada dentro de ella o diferenciada.  
**Diagnóstico:** la cuestión afecta quién integra dependencias que cruzan equipos, resuelve prioridades globales y mantiene coherencia entre proyectos. No debe resolverse por inferencia individual.  
**Riesgo:** vacío de responsabilidad o solapamiento de autoridad.  
**Severidad preliminar:** alta a medida que crece el ecosistema.

## 3. Diagnóstico de capacidad funcional

| Capacidad | Estado observado | Dependencia real | Límite |
|---|---|---|---|
| Interpretar mandatos y producir documentos | Disponible en sesión con prompting | Modelo + contexto | No es ejecución autónoma persistente |
| Consultar/editar GitHub | Disponible cuando existe conexión y permiso | Conector GitHub | No activa sesiones ni valida semántica |
| Crear agentes documentales | Procedimiento documentado y ejecutable en sesión | Prompting + moldes + GitHub | Diseñado no equivale a agente desplegado |
| Clasificar/derivar especialistas | Reglas documentadas | Taxonomía + evidencia de competencia | Descubrimiento/carga/activación no garantizados |
| Coordinarse a sí misma | Parcial, mediante análisis y actualización de artefactos | Contexto + checkpoint + GitHub | Puede desincronizarse o perder continuidad |
| Coordinar pares | Parcial, mediante handoffs | GitHub/canales + invocación externa | Handoff no despierta receptor |
| Orquestar tareas | Declarativo/documental; etapa KAT-006 inicial | Schema + owner + dependencias + humano/modelo | No hay motor que ejecute/valide grafo por sí solo |
| Auditoría documental | Ejecutable por sesión con acceso a repos | Modelo + GitHub | No es monitoreo continuo |
| Validación automática de schemas/grafos | No acreditada en el flujo general revisado | Validador/herramienta | Hay schemas, no prueba de enforcement |
| Runtime Mini | Código experimental en repo | Python/POSIX/OS + manifiesto | No se acredita integración ni disponibilidad de sesión |
| Activación autónoma/recurrencia | No acreditada | Scheduler/event bus/runtime/servicio | No confundir con instrucciones o commits |
| Aprendizaje/evolución persistente | Parcial, por investigación, decisiones y commits | Memoria documental + revisión humana | No hay auto-modificación autónoma autorizada |

## 4. Matriz preliminar de dependencias

| Resultado buscado | Necesario | No necesario por defecto | Condición de bloqueo |
|---|---|---|---|
| Investigación documental | Modelo, contexto, fuentes | Runtime | Solo falta de fuente/acceso esencial |
| Entrega de agente documental | Prompting, molde, contrato, GitHub si destino remoto | Runtime, scheduler, pruebas de despliegue | Identidad/alcance/seguridad esencial o falta de permiso de escritura |
| Cambio de archivos en GitHub | Conector y permiso de escritura | Runtime Softly | Acceso/permiso, ruta/estado/sha no resoluble |
| Handoff a otro agente | Contrato de transferencia y persistencia | Runtime para publicar | Para ejecución efectiva se necesita invocación/aceptación del receptor |
| Orquestación automática de tareas | Estado/grafo, motor, activación, política de reintentos, permisos, observabilidad | No puede reducirse a prompting si debe ocurrir sin sesión humana | Falta de motor/invocador o validación requerida |
| Ejecución de operaciones locales confinadas | Runtime o herramienta equivalente, permisos del SO | No aplica a análisis documental | Falta de entorno, permisos o primitivas seguras |
| Auditoría continua | Scheduler/eventos, acceso a repos, política de alertas | Runtime Mini no necesariamente | Falta de mecanismo de observación y disparo |
| Equivalencia de agente entre entornos | Casos de prueba, modelos/entornos comparables, criterios | Runtime universal | Falta de evidencia experimental |

## 5. Riesgos adicionales a investigar

1. Conflictos de escritura y condiciones de carrera en índices, checkpoints y archivos compartidos.
2. Deriva entre SOFTLY.md, README, CHECKPOINT, schemas y contratos subordinados.
3. Ambigüedad entre estado global y estado de tarea local.
4. Ausencia de SLO/tiempos de respuesta para handoffs y bloqueos.
5. Dependencia excesiva de gAto como integrador manual de resultados.
6. Falta de mecanismo estándar para cancelar, replanificar o escalar tareas bloqueadas.
7. Sobrecarga de contexto por instrucciones redundantes o inconsistentes.
8. Riesgo de evidencia autocertificada: el mismo agente que produce puede ser quien declare verificado su propio resultado.
9. Versionado de agentes y compatibilidad de contratos entre versiones.
10. Gestión de fallos parciales: commit exitoso pero índice fallido, handoff publicado sin receptor, runtime que autoriza pero falla al escribir.

## 6. Reglas que ayudan y reglas que pueden perjudicar

**Ayudan:** autoridad humana explícita; no-herencia de competencias/permisos; separación Diseñado/Probado/Desplegado; modo explícito; supuestos no críticos no bloqueantes; handoff con criterio de aceptación; preservación de historia; checkpoint ligero; prohibición de inventar capacidades.

**Pueden perjudicar si se aplican sin proporcionalidad:** doble revisión universal para toda tarea; captura de incidencias extensa en operaciones triviales; requisitos de documentación replicados en múltiples archivos; insistencia en commits/índices/checkpoints incluso cuando el resultado no modifica estado persistente; criterios de cierre que no distingan riesgo, reversibilidad y tamaño.

No se concluye que deban cambiarse: hace falta medir casos reales y contrastar con auditoría independiente.

## 7. Prioridades preliminares

1. Definir estados operativos sin ambigüedad: documentado, disponible, asignado, invocado, aceptado, ejecutando, bloqueado, terminado y verificado.
2. Establecer criterio de aceptación a nivel de objetivo global además de entregables locales.
3. Resolver la responsabilidad de integración semántica y coordinación sistémica.
4. Definir qué eventos requieren invocación y quién confirma recepción/ejecución.
5. Graduar verificación y cierre según riesgo, impacto y reversibilidad, manteniendo evidencia proporcional.
6. Probar integridad del grafo task-centric (referencias, ciclos, transiciones y cierre).
7. Ejecutar pruebas de transferencia funcional entre instancias/modelos antes de afirmar portabilidad.
8. Aclarar el estatus real del Runtime Mini: experimental, integrado, disponible, desplegado o retirado; no inferir ninguno.

## 8. Decisiones reservadas a gAto

- Definición final de coordinación sistémica y distribución de autoridad.
- Aceptación de riesgos y prioridades del roadmap.
- Aprobación de cambios a SOFTLY.md, contratos, taxonomías, schemas y moldes.
- Decisión sobre construcción, integración o despliegue de Runtime.
- Criterios de autonomía y acciones externas permitidas.
- Elección entre mayor simplicidad documental y mayor enforcement automatizado.

## 9. Estado de independencia y siguientes pasos

Esta versión es el registro preliminar propio, preservado antes del contraste con Audeline y Katarina. No incorpora sus conclusiones. Los hallazgos pueden cambiar tras revisión de evidencia adicional.

**No se implementó ninguna recomendación.** No se modificaron SOFTLY.md, CHECKPOINT.md, README.md, contratos, taxonomías ni Runtime.

**Conclusión provisional:** lo que más puede impedir la evolución de Softly no es simplemente la ausencia de Runtime. Es la brecha entre lo que la arquitectura declara, lo que una sesión puede hacer con sus herramientas reales y lo que el ecosistema espera que ocurra automáticamente. Si esa brecha no se representa explícitamente en estados, dependencias, aceptación y activación, se seguirán generando bloqueos falsos y cierres localmente correctos pero globalmente inútiles.
