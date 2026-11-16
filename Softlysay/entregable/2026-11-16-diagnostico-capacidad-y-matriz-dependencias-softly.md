# Diagnóstico funcional y matriz de dependencias — SOFTLY-FUTURE-BLOCKERS-2026-001

**Fecha:** 2026-11-16  
**Estado:** diagnóstico documental independiente; no constituye prueba runtime  
**Corte de repositorio:** gatoscientist/Softly, rama main, commit preliminar a2bc038bd6bf14fa67c244b2c0e0ff1cd29c8bc9

## 1. Regla de lectura

Se distinguen cinco niveles:
1. **Definido:** existe mandato, contrato, schema o procedimiento.
2. **Ejecutable en sesión:** un modelo puede realizarlo con herramientas efectivamente disponibles y permisos.
3. **Integrado:** la capacidad está conectada al flujo y puede ser invocada por los componentes relevantes.
4. **Automatizado:** ocurre sin que una persona o sesión tenga que iniciar manualmente cada paso.
5. **Verificado:** existe evidencia de pruebas sobre el comportamiento y el entorno objetivo.

No se debe promover una capacidad de un nivel a otro por inferencia.

## 2. Diagnóstico de capacidad

| Capacidad | Definición documental | Ejecución en sesión | Integración/automatización acreditada | Diagnóstico |
|---|---|---|---|---|
| Interpretar mandatos, analizar y redactar | Sí | Sí, según modelo y contexto | No requiere runtime | Capacidad funcional actual de sesión |
| Crear/editar documentos | Sí | Sí | Depende de herramienta/destino | Prompting basta para contenido; GitHub para persistir remoto |
| Leer/escribir GitHub | Sí | Sí con conector y permisos | No despierta otras sesiones | Capacidad externa conectada, no motor de agentes |
| Crear agentes documentales | Sí, molde y checklist | Sí | Persistencia GitHub si el destino es repo | No necesita Runtime |
| Seleccionar especialistas | Reglas de taxonomía y no-herencia | Parcial: requiere evidencia y contexto | No hay registry operativo completo acreditado | Falta catálogo vivo de competencia/disponibilidad |
| Coordinar trabajo propio | Parcialmente definida | Sí por planificación y actualización documental | Sin monitor de estado autónomo acreditado | Depende de disciplina de sesión y continuidad |
| Coordinar pares | Sí, handoff y responsabilidades | Publicar/leer handoff sí | Invocación automática no acreditada | La transferencia documental no garantiza ejecución |
| Orquestar tareas task-centric | Modelo y schema presentes | Se puede planificar/documentar | No hay motor task-centric acreditado | Diseño documental, no orquestación ejecutable |
| Validar esquema JSON | Hay schemas | No se acredita validador general en el flujo | No | Schema no equivale a validación automática |
| Validar grafo de tareas | Necesidad documentada | No se acredita | No | Sin validador de referencias/ciclos |
| Integrar resultados incompatibles | Responsabilidad discutida | Sí, mediante deliberación y revisión humana/modelo | Sin árbitro semántico automático acreditado | Falta proceso explícito de integración y autoridad por ámbito |
| Auditoría documental | Contratos de auditoría existentes | Sí con acceso a repos | No es monitoreo continuo | Requiere encargo y sesión activa |
| Runtime Mini 0.2.0 | Código/manifiesto/tests en repo | No se ejecutó en esta investigación | Integración con Softly no acreditada | Artefacto experimental, no prueba de servicio disponible |
| Runtime task-centric | Objetivo discutido; no implementación acreditada | No | No | Bloqueante solo si el objetivo exige esa operación |
| Activación/recurrencia | Handoffs y eventos declarativos | Manual o por mecanismo externo | Scheduler/invocador persistente no acreditado | Capacidad faltante para autonomía sin sesión iniciadora |
| Aprendizaje/evolución persistente | Decisiones, research y commits | Sí, mediante trabajo deliberado | Auto-modificación autónoma no acreditada | Evolución documental supervisada |

## 3. Runtime Mini: alcance observado

El repositorio contiene:
- softly-runtime/manifest.json, versión 0.2.0.
- softly-runtime/runtime.py.
- softly-runtime/test_runtime.py.
- softly-runtime/events.jsonl, actualmente vacío en el árbol inspeccionado.
- softly-runtime/events.head.

El manifiesto limita la operación permitida a create_text_file. El código implementa autorización contra manifiesto, confinamiento de rutas, rechazo de symlinks, escritura de archivo nuevo, ledger JSONL encadenado por hashes y verificación de checkpoint. El código declara requisitos de primitivas POSIX/dir_fd/O_NOFOLLOW y permisos del sistema operativo.

El archivo de pruebas declara seis casos, incluidos escritura permitida, escape de rutas, operación no declarada, error de permisos, symlinks y manipulación del ledger. **No se ejecutaron estas pruebas en esta investigación.** La existencia de tests no acredita que pasen.

Por tanto:
- Es falso decir que no existe ningún código llamado Runtime.
- Es correcto decir que no se acreditó Runtime task-centric.
- Tampoco se acreditó que Runtime Mini esté desplegado, conectado al modelo o disponible en la sesión.
- Runtime Mini no implementa por sí mismo el grafo de tareas, asignaciones, estados, dependencias, recepción de handoffs ni scheduler.

La distinción corrige la terminología sin disminuir la gravedad de un bloqueo operativo cuando el objetivo sí requiere un motor task-centric.

## 4. Matriz de dependencias

| Objetivo | Dependencias indispensables | Dependencias condicionales | No es requisito universal |
|---|---|---|---|
| Investigar y emitir informe | Modelo, contexto, fuentes y criterio de alcance | Conector si la fuente está en GitHub | Runtime, scheduler |
| Crear paquete documental | Prompting, molde, contrato y criterio de aceptación | GitHub si la entrega debe persistirse allí | Runtime, despliegue, pruebas de ejecución |
| Leer repositorio | Acceso GitHub y permiso de lectura | Conocimiento de rutas/árbol | Runtime |
| Persistir archivo en GitHub | Conector, permiso de escritura, ruta y SHA/branch correctos | Relectura y commit verificable | Runtime Mini |
| Handoff documental | Identificador, destinatario, resultado, evidencia, siguiente acción, aceptación y persistencia | Acuse si riesgo/plazo lo exige | Scheduler para mera publicación |
| Ejecutar handoff en otro agente | Handoff válido y sesión/receptor invocado | Canal de notificación, aceptación y seguimiento | No basta con un commit |
| Orquestar tareas automáticamente | Registro de tareas, motor de estados, resolución de dependencias, invocador, permisos y observabilidad | Scheduler, reintentos, leases, alertas | No basta con prompting si debe ocurrir sin sesión activa |
| Validar dependencias | Conjunto de tareas y validador de referencias/ciclos | Reglas de transición y datos de ownership | Runtime general si un validador por lotes basta |
| Ejecutar operación local confinada | Herramienta/runtime, permisos SO, workspace y política | Ledger y controles de integridad según riesgo | Runtime task-centric |
| Auditoría recurrente | Scheduler o disparador, acceso a repos, política de alcance y alertas | Runtime si requiere acciones locales | Runtime Mini por sí solo |
| Equivalencia funcional entre instancias | Casos de prueba, modelos/entornos identificados, criterios y repeticiones | Instrumentación de costo y trazas | Runtime universal; puede probarse en sesiones controladas |

## 5. Dependencias artificiales y dependencias indispensables

### Artificiales si se convierten en requisitos universales
- Exigir Runtime para redactar, investigar, crear un agente documental o modificar archivos autorizados en GitHub.
- Exigir scheduler para publicar un handoff que será tomado manualmente.
- Exigir una prueba de despliegue para declarar completo un paquete en estado Diseñado.
- Exigir validador automático para toda tarea documental simple cuando una revisión de alcance proporcional es suficiente.
- Exigir que cada agente tenga todos los directorios y ceremonias aunque no exista flujo que los use.

### Indispensables según el resultado
- Conector y permiso GitHub para persistir en GitHub.
- Invocación real o sesión del destinatario para ejecutar un handoff en otro agente.
- Motor/validador de tareas si se promete gestión automática de estados y dependencias.
- Permisos efectivos y controles del entorno para ejecutar operaciones externas o locales.
- Criterio de aceptación y evidencia para declarar una entrega terminada.
- Autoridad integradora cuando varios resultados son incompatibles.

## 6. Dependencias que se confunden

| Concepto confundido | Diferencia correcta |
|---|---|
| Prompt y capacidad | El prompt describe una conducta; no crea herramienta, permiso ni proceso persistente |
| GitHub y Runtime | GitHub persiste artefactos; no ejecuta agentes ni dependencias por sí mismo |
| Schema y validador | Schema describe estructura; requiere validador para enforcement |
| Handoff y activación | Handoff conserva instrucción; invocador/sesión activa al receptor |
| Asignación y disponibilidad | Owner asignado no implica sesión activa, competencia demostrada ni permiso |
| Diseñado y operativo | Documento completo no prueba despliegue ni comportamiento |
| Runtime Mini y Runtime task-centric | El primero es una operación local acotada; el segundo tendría que gestionar tareas y dependencias |
| Cierre documental y éxito global | Los artefactos pueden estar completos y el objetivo de sistema seguir bloqueado |

## 7. Criterio para declarar bloqueo

Un requisito debe bloquear una tarea solo si:
1. el resultado solicitado depende materialmente de él;
2. la dependencia está demostrada por el alcance o por evidencia;
3. no existe alternativa equivalente autorizada;
4. el bloqueo se limita al resultado afectado.

La ausencia de Runtime no bloquea una investigación documental. Sí bloquea una aceptación funcional cuyo criterio central sea ejecutar tareas, gestionar dependencias y coordinar estados mediante Runtime.

## 8. Conclusión

La capacidad faltante no es un Runtime universal para todo Softly. Las brechas concretas son:
- invocación/activación verificable de destinatarios;
- registro y validación de tareas/dependencias cuando se requiera operación task-centric;
- autoridad y procedimiento de integración semántica;
- observabilidad de recepción, ejecución y aceptación;
- continuidad sincronizada entre sesiones y artefactos.

La decisión sobre qué brechas convertir en infraestructura corresponde a gAto, según objetivos operativos y costo demostrado.
