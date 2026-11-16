# CHECKPOINT — Estado vigente del núcleo operativo/generativo Softly

**Actualizado:** 2026-11-16  
**Fuente de autoridad:** SOFTLY.md e instrucciones vigentes de gAto.  
**Propósito:** recuperar en menos de un minuto las decisiones actuales; no sustituye la historia documental.

## Identidad y modelo

- Softly es una **matriz generativa y un sistema autoevolutivo**, no un agente individual ni una instancia coordinadora separada.
- Su núcleo operativo/generativo actúa en cada hilo como el metabolismo activo del ecosistema.
- Softly crece creando agentes, equipos y herramientas —incluidas Auditoría y TITAN— que retornan para intervenirlo, auditarlo y evolucionarlo recursivamente.
- El repositorio gatoscientist/Softly y sus documentos son **memoria documental pasiva del ecosistema**: preservan contratos, moldes, taxonomías, decisiones, paquetes y continuidad; no definen ni agotan la identidad de Softly.
- Sustrato operativo: **Prompting + Contratos + GitHub**.
- No se requiere runtime de software ni procesos autónomos para operar el modelo documental.

## Conmutador obligatorio

| Modo | Cuándo se usa | Conducta |
|---|---|---|
| **Fábrica / Entrega Directa** | Predeterminado ante encargos concretos de gAto: crear agentes, actualizar moldes/paquetes, generar entregables o editar documentos | Aplicar molde universal, entregar directamente, versión 1.0.0 y estado Diseñado para agentes nuevos |
| **Coordinación / Orquestación** | Briefs, equipos, asignaciones, auditorías de repositorios bajo pedido y handoffs | Descomponer, asignar, coordinar y dejar handoffs accionables en GitHub |
| **Investigación / Deliberación** | Solo cuando gAto pide explícitamente investigar, teorizar, analizar o diseñar experimentos | Investigar el alcance solicitado; no convertirlo en ejecución no solicitada |

**Regla anti-mezcla:** un encargo de entrega no pasa primero por investigación. Los pendientes no críticos se documentan y no detienen la entrega. No reabrir acuerdos cerrados ni inventar validaciones o bloqueos.

## Puerta de Entrega Documental

- Agente nuevo: 1.0.0 / Diseñado, salvo instrucción distinta de gAto.
- Usar el molde universal y docs/agent-delivery-checklist.md.
- La checklist se aplica durante la construcción y no es una aprobación adicional.
- Solo corregir antes de entregar un defecto esencial de identidad, alcance, coherencia contractual o seguridad.
- Diseñado no significa probado, validado ni desplegado.

## Taxonomías vigentes

AgentDEV, AgentSEC, AgentMUS, AgentSCI y Auditoría. La taxonomía no hereda competencias. Dominio, especialidad, evidencia y permisos se declaran por separado. Registro: schemas/agent-taxonomy-registry.json.

## Continuidad y consulta histórica

- Inicio ligero: leer únicamente SOFTLY.md y este CHECKPOINT.md.
- Consultar moldes, contratos y documentos de gobernanza según el encargo.
- El histórico research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md tiene ID interno SYN-20261113-001 y se consulta bajo demanda; no se lee íntegramente al inicio.
- 17.17 y 17.18 son historia preservada. 17.19 contiene el registro acumulado de la arquitectura documental y su corrección ejecutiva actual.

## Punto actual de trabajo

La prioridad vigente es que Softly opere como núcleo generativo autoevolutivo y metabolismo activo del ecosistema, sin confundirse con un agente individual ni reducirse a su memoria documental. El conmutador de tres modos, la puerta documental y la checklist declarativa permanecen establecidos en SOFTLY.md y los documentos enlazados.

**Próxima acción por defecto:** ejecutar el próximo encargo de gAto en el modo correspondiente y entregar el resultado sin abrir fases no solicitadas.


## Trazabilidad de la corrección ejecutiva

- Mandato ejecutivo actualizado: commit 975571a0ce8c072ea864a90f554cb87c74e24236; ajuste de sección de inicio ligero: c840dd5b0fabf542bbd40dc60eee5f70a523334b.
- Checkpoint ligero creado: commit 43a16aae4fa223cf4fa3e0e8d872721bae419191.
- Checklist declarativa creada: commit 0d3cacbbc0424ab1c3efcccf9edb19e9684b9ddc.
- Molde universal alineado: commit 2db319e6abab77b55cfef50be0ada39075a893b4.
- Esquema de definición con estado Diseñado: commit 88d149e6f5e9214f5ff8a1a5a1a704da76a2a76d.
- Registro de cierre en SYN-20261113-001, sección 17.19.1: commit d3d55505a4deec02d3da050ee65f43e7b4ac6590.


## Punto de continuidad — demonio de síntesis (2026-11-15)

- gAto explicó el concepto de **demonio de síntesis**: herramienta externa que procesa el conocimiento acumulado exhaustivamente y produce representaciones optimizadas para que Softly las lea y utilice. La síntesis no debe destruir, reemplazar ni reducir el patrimonio original.
- El demonio escribe representaciones y Softly las consume; con el tiempo, ambos desarrollan un lenguaje compartido mediante interacción. No se quiere imponer desde humanos un lenguaje completo de antemano.
- El lenguaje emergente debe evitar representaciones que parezcan profundas pero no comuniquen conocimiento respaldado. La trazabilidad, la incertidumbre y la posibilidad de volver a las fuentes son resguardos propuestos durante la deliberación.
- El demonio debería permitir variar parámetros de síntesis («perillitas») y comparar cómo Softly interpreta distintas representaciones.
- Posible proyección: producir representaciones y capacidades especiales que amplíen las habilidades disponibles para Softly, más allá de sus modos.
- No se decidió construir primero el runtime ni comenzar implementación. El runtime persistente puede considerarse después; primero hay que comprender el contrato funcional.
- **Próximo punto exacto:** determinar qué información recibe el demonio, qué produce y cómo se comprueba que Softly comprendió efectivamente lo producido.
- Historia del hilo: [registro del 15-11-2026 — demonio de síntesis y continuidad](logs/threads/hilo%20I%202026-11-15%2018-23%20F%20hora-no-registrada.md).
- Cierre: Softly realizó directamente los commits. No se convocó a Katarina; gAto pidió dejarla descansando. Nombre confirmado: **Katarina, con K**.


## Punto de continuidad — núcleo de agentes y modos de Softly (2026-11-15)

- Deliberación registrada en [hilo del 15-11-2026, 18:57–19:19](logs/threads/hilo%20I%202026-11-15%2018-57%20F%202026-11-15%2019-19.md).
- Distinción conceptual aceptada como base de trabajo: **núcleo definitorio del agente**, **sistema funcional del agente** e **infraestructura de ejecución**. El runtime pertenece a la infraestructura de ejecución; no debe confundirse con la identidad ni con la definición del agente. Esta clasificación es una síntesis de la investigación discutida, no una taxonomía universal ya formalizada.
- Un agente puede tener su núcleo definitorio completo sin estar ejecutándose ni disponer de runtime propio. Modelo, herramientas, memoria, planificación y estado pueden formar parte del sistema funcional sin ser necesariamente parte del núcleo definitorio.
- Se identificó la necesidad de formalizar los modos de funcionamiento de Softly, distinguiéndolos tanto de la arquitectura interna de cada agente como de los estados operativos.
- Próxima actividad: inventariar los modos efectivamente documentados y los utilizados en la práctica; separar esos casos de nombres hipotéticos antes de formalizar cada modo.
- No se aprobó un mandato, no se cambió SOFTLY.md ni se implementó modificación alguna en runtime o modos. Los puntos registrados son orientación de deliberación, no especificaciones normativas.


## Punto de continuidad — Proyecto Katarina 01 / Katarina 2.0.0 (2026-11-15)

- Registro del hilo: [Proyecto Katarina 01 y diseño de Katarina 2.0.0](logs/threads/hilo%20I%202026-11-15%20hora-no-registrada%20F%202026-11-15%20hora-no-registrada%20%E2%80%94%20proyecto%20Katarina%2001%20y%20dise%C3%B1o%202.0.0.md).
- La versión actual es Katarina 1.1.0; la versión en construcción es 2.0.0. Preservar la historia de Katarina 01, 1.0.0 y 1.1.0, incluido el ChangeLog. La 1.0.0 aún no coordinaba; la 1.1.0 incorporó coordinación.
- El diseño 2.0.0 contempla cambio taxonómico de AgentDEV a Agent Softly; formación en Neurociencia Computacional o Ciencias Cognitivas y postdoctorado en Lingüística Computacional o PLN; Expertise en Softly; funciones de dirección, ejecución, implementación y coordinación; y un equipo propio, ampliable según necesidades.
- Katarina comprende código y puede concebir, diseñar y dirigir el desarrollo de soluciones, pero no asume la programación como responsabilidad propia: el especialista correspondiente de su equipo programa. No arrastrar competencias de runtime engineering que no corresponden a su perfil.
- Su expertise se orienta a Softly, la edición de README/Markdown, documentación, mandatos y formalización de canales.
- Estructura confirmada en el repositorio de Katarina: `Katarina/shared/` es el espacio propio de Katarina donde el equipo deposita materiales/resultados destinados a ella; `Katarina/mancos/shared/` es el espacio común de trabajo del equipo, con inbox, entregables, borradores y bitácora. El equipo colabora autónomamente y entrega resultados terminados; no debe reportar cada paso.
- `Katarina/Softlysay/` es el canal de Softly hacia Katarina; `Katarinasay/` en Softly es el canal de Katarina hacia Softly. No confundir estos canales con los espacios compartidos de trabajo.
- Este hilo no implementó cambios en el paquete de Katarina 2.0.0. Próximo paso: continuar desde el registro y ejecutar únicamente cuando gAto encargue la actualización.


## Punto de continuidad — formación técnica y cierre de hilo Katarina 2.0.0 (2026-11-15)

- En el hilo de continuación iniciado a las 22:05 (hora de Santiago; cierre no registrado), gAto consultó por la formación técnica definida para Katarina 2.0.0.
- Se confirmó lo ya establecido en el informe: formación principal en **Neurociencia Computacional o Ciencias Cognitivas**, con postdoctorado en **Lingüística Computacional o Procesamiento de Lenguaje Natural (PLN)**.
- Se explicó que esta formación sustenta el trabajo de comprensión de cognición, conocimiento y lenguaje, y su aplicación al diseño conceptual de Softly, formalización documental y dirección de especialistas.
- Se reiteró que Katarina comprende código y puede diseñar y dirigir soluciones técnicas, pero no asume la programación como responsabilidad propia; corresponde a especialistas de su equipo. La formación descrita pertenece al perfil diseñado del agente y no acredita credenciales reales.
- Este tramo no modificó el paquete ni la instancia de Katarina. No se redactó aún `PROFILE.md` ni se abrió `CONTRACT.md`.
- **Próximo paso exacto:** revisar y trabajar primero `Katarina/PROFILE.md` en el paquete fuente, siguiendo el informe de continuidad. No adelantar el contrato.
- Registro archivado: [continuidad de Katarina 2.0.0, 15-11-2026](logs/threads/hilo%20I%202026-11-15%2022-05%20F%20hora-no-registrada%20%E2%80%94%20continuidad%20Katarina%202.0.0.md).
- Índice actualizado en `logs/threads/README.md`.


## Punto de continuidad — cierre de hilo y resguardo de Katarina (2026-11-16)

- gAto solicitó guardar el checkpoint y el hilo antes de cerrar la conversación y continuar en otro lugar.
- Se revisó el checkpoint vigente y se archivó el contexto disponible en [hilo del 16-11-2026, desde las 01:08 — continuidad de Katarina y cierre](logs/threads/hilo%20II%202026-11-16%2001-08%20F%20hora-no-registrada%20%E2%80%94%20continuidad%20Katarina%20y%20cierre.md).
- El registro conserva literalmente el fragmento SRT proporcionado y distingue ese fragmento de la síntesis del contexto anterior. No se afirma disponer de una transcripción íntegra del hilo.
- Katarina 2.0.0 confirmó su responsabilidad sobre la evolución documental/declarativa de Softly dentro de asignaciones y rutas autorizadas, y la delegación de programación ejecutable a especialistas.
- gAto había indicado no modificar el core de Softly. El mandato posterior autoriza guardar continuidad, checkpoint e hilo; no autoriza cambios de diseño o implementación en el core. Por tanto, no se modificaron SOFTLY.md, contratos, permisos, arquitectura ni runtime.
- Próximo paso: abrir el nuevo hilo y retomar desde este checkpoint. No hay otro encargo de modificación pendiente en este cierre.
