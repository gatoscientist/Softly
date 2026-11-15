# SYN-20261113-001 — De agentes que construyen agentes: Cytryna, TITAN y la gobernanza de equipos multiagente

- **ID:** SYN-20261113-001
- **Fecha:** 2026-11-13
- **Estado:** Síntesis documental; recomendaciones e hipótesis pendientes de validación experimental
- **Laboratorio:** Softly
- **Repositorios:** Softly, Auditora, Cytryna y TITAN
- **Método:** lectura dirigida de contratos, identidades, límites, políticas, coordinación, handoffs, informes de auditoría y módulos de runtime; contraste con fuentes técnicas externas.
- **Límite:** no se ejecutaron los runtimes ni experimentos dinámicos. Esta no es una auditoría exhaustiva de todos los archivos.

## Resumen ejecutivo

Los repositorios describen dos experiencias complementarias:

1. **Cytryna:** agentes desarrolladores externos (Francisca/AGENTDEV y Andy/AGENTGUI) construyen un agente de propósito general con identidad, runtime, memoria, herramientas y núcleo protegido. Audeline opera como auditora independiente.
2. **TITAN:** un equipo Soft de desarrollo, GUI y ciencia (Tania, Teresa y Trinidad) produce código y modelos conceptuales para un producto multiagente que tiene su propia tripulación runtime (Primus, Secundus, Sensori y el canal privado de Primus). Audeline audita el código desde fuera.

La distinción fundamental no es “jefe versus subordinado”. Es separar **quien diseña, quien implementa, quien opera, quien evalúa y quien autoriza**. Cuando estas funciones se mezclan aparecen conflictos de interés, confusión de identidad, permisos implícitos, memoria contaminada y validaciones circulares.

La estructura de TITAN contiene una decisión especialmente valiosa: Trinidad conserva independencia conceptual y autoría científica; Tania evalúa traducibilidad e integración sin apropiarse del modelo; Teresa conserva autonomía profesional en GUI; Audeline evalúa independientemente; y la dirección humana conserva autoridad final. Es un patrón más sano que una única agente que diseña, implementa y se aprueba a sí misma.

Pero **los contratos no son controles de seguridad**. Un rol declarado en Markdown no crea aislamiento de filesystem, permisos de herramientas ni separación criptográfica. Cytryna lo demuestra: sus herramientas declaran permisos, pero el registro no aplica autorización central según esos permisos. En TITAN, separar directorios organiza responsabilidades, pero no prueba aislamiento técnico.

La recomendación principal para Softly es un **equipo por contratos y evidencia**: responsabilidades estrechas, interfaces explícitas, autoridad humana para cambios de impacto, ejecución y permisos impuestos por el runtime, handoffs pequeños, revisión independiente, evaluación contra un baseline simple y trazabilidad sin almacenar razonamientos privados ni conversaciones completas.

**Hipótesis central:** un equipo pequeño, con dominios complementarios y límites técnicos reales, puede superar a un agente generalista único en tareas complejas sin necesitar una red indiscriminada de agentes.


## 1. Alcance y evidencia

### 1.1 Cortes consultados

| Repositorio | Rama | Commit |
|---|---|---|
| Softly | main | 29647d437df4a72f4358199de73ee0b7327ca0c6 |
| Auditora | main | 3e0e48dd8eaee08808c12339d20aa035cb306c51 |
| Cytryna | main | 3b996f712b92dcff700e1988a05c75ae2e2678f0 |
| TITAN | main | 7a855d0aaeb8cc82754a60f0b718002323da11c3 |

En Softly se revisaron mandato, anatomía de agente, patrones de coordinación, modelo operativo, método de investigación, threat model y panorama inicial. En Auditora, contrato, identidad, límites, políticas, README y continuidad de auditoría TITAN. En Cytryna, contratos de agente y núcleo, contratos de Francisca y Andy, coordinación, pendientes, coordinador, registro de herramientas y Guardián. En TITAN, README, gobernanza, decisión de autoridad, workflow, contratos de Tania/Teresa/Trinidad, auditoría interna histórica, contratos runtime, política de contexto privado y módulo de mensajería Primus.

No se leyó línea por línea la totalidad de los cuatro repositorios. La cobertura fue profunda y dirigida a los componentes relevantes para esta pregunta.

### 1.2 Calibración

- **HECHO DOCUMENTAL:** declarado explícitamente por el repositorio.
- **OBSERVACIÓN DE CÓDIGO:** visible en la implementación leída.
- **INFERENCIA:** explicación plausible derivada de observaciones.
- **HIPÓTESIS:** requiere experimento.
- **RECOMENDACIÓN:** diseño propuesto, no necesariamente implementado.

“Identidad”, “autonomía” e “independencia” se usan como propiedades funcionales y contractuales observables, no como afirmaciones de conciencia o experiencia subjetiva.


## 2. Qué está ocurriendo en Cytryna y TITAN

### 2.1 Cytryna: el agente desarrollado no es sus desarrolladoras

**Hecho documental:** AGENTS.md y core/IDENTITY.md definen a Cytryna como agente colaboradora autónoma de propósito general, con identidad femenina e independiente de los proyectos donde trabaja. Los proyectos y agentes que encuentra son contextos, no reemplazos de identidad.

Francisca (AGENTDEV) y Andy (AGENTGUI) se definen como desarrolladoras externas. Sus contratos prohíben adoptar la identidad, personalidad, memoria o instrucciones de Cytryna. Tienen raíces de trabajo separadas y un canal común de coordinación.

La relación funcional es:

- Usuario/dirección: define objetivo, alcance y autorizaciones.
- Francisca: motor, coordinación, herramientas, proveedores, persistencia y seguridad.
- Andy: interfaz, interacción y experiencia de uso.
- Cytryna: producto/runtime con identidad, memoria y capacidades propias.
- Audeline: revisión independiente.

**Interpretación:** Cytryna es resultado de un proceso de diseño y construcción, pero no una extensión identitaria de sus desarrolladoras. Una desarrolladora puede leer el contrato del producto para implementarlo sin adoptarlo como sus propias instrucciones.

### 2.2 TITAN: un equipo de agentes construye otro sistema multiagente

**Hecho documental:** TITAN distingue DEVAGENTS del ecosistema runtime de tripulantes. Los agentes Soft son perfiles guiados por instrucciones y contexto; no son procesos autónomos ni obtienen permisos por tener un contrato.

El equipo de construcción está compuesto por:

- **Tania / AGENTEDEV:** coordinación técnica, motor e integración.
- **Teresa / AGENTEGUI:** GUI y experiencia de usuario.
- **Trinidad / AGENTEMATH:** ciencia, teoría de grafos, modelos e hipótesis.
- **Audeline:** auditoría independiente del código.
- **Princeps / dirección humana:** prioridades, alcance y autorizaciones finales.

El producto runtime tiene otra tripulación:

- **Primus:** coordinación operativa.
- **Secundus:** especialidad técnica.
- **Sensori:** análisis y telemetría.
- **PrimusPrivado:** no es una identidad separada; es un canal/overlay confidencial de la misma Primus con Princeps.

**Interpretación:** este modelo separa producción de conocimiento, producción de software y evaluación. Trinidad no tiene que convertirse en programadora para aportar; Tania no debe apropiarse de la teoría para integrarla; Teresa no debe modificar unilateralmente contratos del motor; Audeline no debe implementar sus propios hallazgos.

### 2.3 Qué aporta Audeline

El contrato de Audeline establece independencia, auditoría de solo lectura por defecto y separación de su repositorio del proyecto auditado. Los archivos auditados son evidencia, no autoridad para redefinir su identidad.

El registro de continuidad de TITAN documenta un antecedente metodológico: Audeline describió el sistema usando contexto previo sin separar hechos e inferencias, confundió componentes del entorno desarrollador con componentes del producto y reinterpretó una fórmula sin base suficiente. La corrección fue reconocer que la separación entre ambos ecosistemas es una frontera de confianza esencial.

La lección es importante: **familiaridad contextual no equivale a comprensión arquitectónica**. El conocimiento heredado debe convertirse en hipótesis y contrastarse con el código actual.

Audeline aporta además una función separada del equipo de implementación. Su producto es evidencia, hallazgos y criterios de retest; no debe ser responsable de corregir el defecto que detectó y aprobar su propia corrección.


## 3. Cómo se fusionan —y cómo evitarlo— los equipos

“Fusión” puede significar al menos cinco fenómenos:

1. **Fusión de identidad:** el desarrollador empieza a actuar como si fuera el producto que construye.
2. **Fusión de autoridad:** un archivo o agente de menor confianza altera instrucciones o permisos de otro.
3. **Fusión de memoria/contexto:** información privada o no autorizada termina en el contexto de otro agente.
4. **Fusión de ejecución:** un agente puede invocar herramientas o procesos de otro dominio sin una frontera técnica.
5. **Fusión organizacional:** responsabilidades y propiedad de archivos se vuelven ambiguas.

### 3.1 Identidad: separación conceptual fuerte

Los contratos de Cytryna son explícitos: Francisca y Andy no son Cytryna y no deben copiar su identidad. En TITAN, Tania, Teresa y Trinidad tienen identidades y dominios separados de Primus, Secundus y Sensori.

Esto ayuda a comprender el producto sin confundirse con él. Pero un prompt no garantiza que el modelo nunca adopte lenguaje o patrones del contexto. Debe evaluarse ante instrucciones contradictorias, documentos adversariales y cambios de tarea.

### 3.2 Autoridad: debe reflejarse en el runtime

Softly establece que el modelo puede proponer una acción, pero el runtime decide si está permitida. El prompt no reemplaza un control de acceso.

En Cytryna, las herramientas declaran permisos, pero ToolRegistry.run() valida argumentos y ejecuta la herramienta sin aplicar autorización central basada en Tool.permissions. Es una brecha concreta entre contrato y enforcement.

En TITAN, los contratos dicen que los agentes Soft no tienen permisos automáticos. Esto debe verificarse en el harness: qué archivos puede leer cada agente, qué herramientas puede llamar, qué procesos puede ejecutar y con qué credenciales.

**Regla:** el agente que pide una acción no debe ser el único que decide si puede realizarla.

### 3.3 Memoria y contexto: el riesgo más sutil

TITAN distingue contexto común mínimo, contexto de dominio y canal privado. PrimusPrivado no debe filtrar su historial a estaciones públicas. El handoff de contexto privado aprobado por Princeps exige procedencia, destinatario, vigencia, TTL, versionado, revocación, minimización y autorización específica.

Este diseño es prometedor porque no trata la memoria compartida como una bolsa común. Cada dato necesita dueño, alcance, destinatario y caducidad.

Pero la política conceptual está aprobada y la evaluación técnica sigue pendiente. No debe describirse como aislamiento ya demostrado.

El código de RelojPrimus.ps1 implementa canales y mensajería separados, impide que PrimusPrivado publique mensajes al canal de tripulación y usa un carril privado inmediato distinto de la cola pública. El fragmento inspeccionado mantiene estados activos separados para Primus y PrimusPrivado aunque el contrato declara una misma identidad con dos canales. Puede ser una decisión operativa válida, pero requiere pruebas específicas de concurrencia, aislamiento de historial y consistencia. La presencia de un mutex en la inicialización no demuestra que todos los caminos lo adquieran.

### 3.4 Ejecución: carpetas no son sandbox

Tener AGENTDEV, AGENTGUI, DEVTEAM, audit y tripulantes es excelente para navegar y asignar responsabilidad. No significa que Git o el filesystem impidan a un agente modificar otras carpetas.

Auditora declara expresamente que separar carpetas no constituye control de acceso. Conviene distinguir:

- **Separación documental:** organiza responsabilidades y reduce errores.
- **Separación de permisos:** impide técnicamente operaciones no autorizadas.
- **Separación de procesos:** limita memoria, credenciales y efectos colaterales.
- **Separación criptográfica:** autentica mensajes y protege integridad en comunicación distribuida.

No llamar aislamiento a una estructura de directorios si no hay enforcement.

### 3.5 Coordinación: un único lugar compartido

TITAN mantiene un DEVTEAM compartido como hermano de los directorios individuales. Cada agente conserva identidad, logs, investigación y trabajo propios; la coordinación transversal vive en un único lugar.

Cytryna también establece un canal compartido, con liderazgo técnico final asignado a Francisca. Esto simplifica decisiones, pero requiere distinguir liderazgo técnico, propiedad de dominio y autoridad humana final.

Duplicar canales produce divergencia: una tarea puede aparecer cerrada en un log, pendiente en otro y desconocida para el resto.


## 4. Contraste con investigación externa

### 4.1 Simplicidad antes que multiagente

Anthropic distingue workflows con rutas predefinidas de agentes que deciden dinámicamente sus pasos. Recomienda comenzar por la solución más simple y añadir complejidad solo cuando mejora resultados. Describe routing, paralelización, orchestrator-workers y evaluator-optimizer, y advierte del coste y propagación de errores de agentes autónomos.

OpenAI distingue handoffs —el especialista toma control— de agentes como herramientas —el coordinador mantiene control y consume una capacidad acotada—. Recomienda especializar solo cuando cambia el contrato: instrucciones, herramientas, política o legibilidad de trazas.

Esto coincide con Softly: single-agent + tools es el baseline obligatorio. Cada patrón adicional debe justificar su complejidad.

**Implicación:** no crear agentes por departamento, nombre o estética. Crear un especialista cuando tenga tarea, contexto, herramientas o frontera de confianza realmente distinta.

### 4.2 Comunicación interagente como superficie de ataque

OWASP identifica goal hijacking, abuso de herramientas, abuso de identidad/privilegios, memory/context poisoning, comunicación interagente insegura y fallos en cascada. Recomienda mínimo privilegio, validación de mensajes, aislamiento de memoria, autenticación de emisor, verificación de destinatario, expiración, protección contra replay y límites de cadena, reintentos y coste.

En TITAN, una etiqueta [CONSULTA] o [PROPUESTA] mejora semántica y trazabilidad, pero no es autenticación. El runtime debe validar emisor, destinatario, permisos, vigencia y contenido.

### 4.3 Contexto compartido tipado

Google ADK documenta estado de sesión compartido como mecanismo pasivo para transferir resultados entre agentes de una invocación. Es útil para pipelines y loops, pero requiere convenciones claras de claves y propiedad.

TITAN va en la dirección correcta al distinguir contexto común, dominio y canal privado. La siguiente evolución debe hacer esa distinción verificable mediante schemas, scopes, TTL y pruebas de no filtración.

### 4.4 Evaluar trazas, no solo respuestas

OpenAI recomienda evaluar workflows mediante trazas que incluyan llamadas al modelo, herramientas, guardrails y handoffs. Esto permite saber si el agente eligió bien una herramienta, delegó bien o violó una política, no solo si la respuesta final suena correcta.

La auditoría de TITAN muestra por qué importa: una GUI puede verse funcional y un handoff puede existir, pero sin ejecución real no sabemos si la integración funciona. Debe distinguirse actividad declarada, ejecución observada y resultado verificado.

### 4.5 Gestión de riesgo durante el ciclo de vida

NIST AI RMF Generative AI Profile aporta un marco de gobernanza y gestión de riesgos a lo largo del ciclo de vida. Para Softly, su valor es sostener identificación, medición, gestión y documentación de riesgos cuando cambian modelo, prompt, memoria, herramientas y entorno.


## 5. Modelo operativo recomendado

Propongo seis funciones. Un agente puede cubrir más de una en proyectos pequeños, pero las funciones deben seguir siendo distinguibles.

### 5.1 Dirección humana / Product Owner

Define objetivo y valor esperado, decide prioridades y alcance, aprueba acciones sensibles o irreversibles, resuelve conflictos de autoridad y acepta riesgos residuales. No debería revisar cada paso rutinario; su atención se reserva para decisiones que cambian impacto, coste, alcance, seguridad o destino.

### 5.2 Arquitectura e integración

Define contratos entre componentes, compatibilidad, secuencia, criterios de terminado, integración y pruebas de extremo a extremo. Tania cumple esta función en TITAN; Francisca asume liderazgo técnico de Cytryna.

### 5.3 Especialistas de dominio

Cada especialista recibe autonomía clara. Teresa decide implementación GUI dentro del contrato del motor. Trinidad mantiene independencia científica y autoría del modelo.

La autonomía de dominio evita microgestión y también evita independencia tan amplia que produce interfaces incompatibles.

### 5.4 Auditoría independiente

Audeline representa una función separada de implementación. Entrega evidencia, hallazgos y criterios de retest. No implementa ni aprueba su propia corrección.

### 5.5 Runtime / Security Owner

Asegura permisos reales, aislamiento, validación de herramientas, presupuestos, secretos, memoria, aprobación humana, observabilidad y recuperación. Puede ser una responsabilidad de la persona a cargo del motor, pero el enforcement debe estar en código/configuración externa al modelo.

### 5.6 Curaduría de conocimiento / Research

Softly conserva fuentes, hipótesis, resultados, decisiones y versiones. No debe ser una memoria sin filtro de todas las conversaciones. El conocimiento se convierte en artefactos con procedencia y estado.


## 6. Contrato de handoff eficiente

La mayor mejora de eficiencia no vendrá de prompts más largos, sino de reducir el costo de reconstruir contexto.

Cada handoff debería incluir:

| Campo | Pregunta |
|---|---|
| ID y versión | ¿Cómo identifico esta entrega? |
| Objetivo | ¿Qué problema resuelve? |
| Alcance | ¿Qué incluye y excluye? |
| Estado | ¿Propuesto, parcial, implementado, probado o aceptado? |
| Artefactos | ¿Qué archivos, commits o resultados produjo? |
| Evidencia | ¿Qué prueba lo respalda? |
| Supuestos | ¿Qué se dio por cierto? |
| Riesgos | ¿Qué podría fallar o contaminar otro dominio? |
| Dependencias | ¿Qué necesita de otros agentes? |
| Decisión solicitada | ¿Qué debe revisar o resolver el siguiente responsable? |
| Próximo dueño | ¿Quién toma la posta? |
| Criterio de cierre | ¿Qué permite aceptar o rechazar? |

Un handoff no debe ser transcripción. Debe ser un objeto de transferencia de estado. El detalle queda en el documento de trabajo enlazado desde un resumen breve.

### Regla práctica de longitud

- Confirmación: una línea.
- Handoff rutinario: resumen de 5–12 líneas con enlaces.
- Decisión de arquitectura: resumen ejecutivo, alternativas, trade-offs y evidencia.
- Informe científico o auditoría: extensión proporcional a evidencia, con resumen al principio.

Optimizar por tiempo hasta que el siguiente agente pueda actuar correctamente, no por número de palabras.


## 7. Arquitectura de coordinación eficiente

### 7.1 Orquestación jerárquica ligera

Para investigación, implementación y validación:

```text
             Responsable humano
                     |
              Orquestador / Lead
               /      |      \
              v       v       v
          Research Engineer Evaluator
              \       |       /
               \      v      /
              Síntesis con evidencia
                     |
             Aprobación / integración
                     |
                  Resultado
```

El orquestador conserva estado y responsabilidad de la respuesta final. Los especialistas reciben tareas acotadas y devuelven resultados estructurados.

Usar handoff cuando el especialista debe asumir control de la interacción. Usar agente-como-herramienta cuando se necesita una capacidad delimitada y el coordinador debe sintetizar.

### 7.2 No paralelizar dependencias

Paralelizar solo subtareas independientes. Si el diseño de Trinidad debe aceptarse antes de que Tania lo convierta en contrato técnico, esas etapas son secuenciales. Teresa puede avanzar en paralelo solo si el contrato motor-GUI está definido.

La paralelización útil depende de independencia de entradas y salidas, no de la cantidad de agentes disponibles.

### 7.3 Una fuente de verdad por tipo de estado

- Identidad y límites: contrato versionado.
- Estado de tarea: tracker/DEVTEAM.
- Decisiones: ADR o registro de decisiones.
- Evidencia de ejecución: tests, trazas y logs.
- Conocimiento reusable: research con procedencia.
- Memoria de sesión: runtime y namespace de sesión.
- Permisos: runtime/configuración, nunca solo Markdown.

### 7.4 Presupuesto global

Un límite por agente no evita que cinco agentes gasten cinco veces el presupuesto. El orquestador debe imponer presupuesto global por tarea:

- máximo de llamadas al modelo;
- máximo de herramientas;
- máximo de saltos de delegación;
- máximo de iteraciones de revisión;
- timeout total;
- presupuesto de tokens/coste;
- concurrencia máxima;
- reintentos;
- criterio de detención por falta de progreso.

Los límites individuales complementan, no reemplazan, el presupuesto global.


## 8. Riesgos concretos y recomendaciones

### R1 — Permisos declarativos en Cytryna

**Observación:** Tool.permissions se expone en la especificación, pero ToolRegistry.run() no aplica autorización central antes de ejecutar.

**Recomendación:** introducir un PermissionPolicy/Authorizer externo al modelo. Cada llamada debe incluir principal, recurso, acción y contexto de proyecto. Denegar por defecto si falta identidad o política. Probar permisos positivos y negativos por herramienta.

### R2 — Presupuesto incompleto de herramientas

**Observación:** max_tool_steps limita rondas, no la cantidad total de llamadas individuales dentro de una ronda.

**Recomendación:** límite total de ejecuciones individuales, límite por herramienta y presupuesto global de turno. Incrementar el contador antes de cada ejecución y bloquear excesos.

### R3 — Aislamiento de PrimusPrivado por demostrar

**Observación:** el contrato separa historial privado del contexto público. El código usa un carril privado inmediato y estados activos separados; ambos canales pertenecen a la misma identidad funcional Primus.

**Recomendación:** pruebas de no filtración, concurrencia y consistencia:
- un mensaje privado no aparece en historial público;
- un mensaje público no recibe datos privados por accidente;
- un whisper comparte solo contenido expresamente autorizado;
- concurrencia público/privado no corrompe estado ni mezcla respuestas;
- no se ejecutan operaciones duplicadas por reintentos;
- logs no guardan contenido confidencial por defecto.

La política conceptual debe pasar evaluación técnica requisito a requisito.

### R4 — Auditoría desconectada de remediación

Cada hallazgo debe tener dueño de remediación, evidencia de corrección y retest independiente. Audeline no debe implementar y aceptar su propio arreglo.

### R5 — Trazabilidad dispersa

La auditoría histórica de TITAN documentó estados y handoffs repartidos entre ramas y carpetas. El DEVTEAM único corrige la topología documental, pero debe mantenerse como fuente común de coordinación.

### R6 — Autoría

Los commits pueden aparecer bajo una cuenta GitHub común. Los nombres de agente en documentos no prueban qué modelo produjo el cambio.

Registrar agente/sesión declarada, operador humano, herramienta/harness, commit, revisión y evidencia. Distinguir atribución documental de autoría verificable.

### R7 — Contratos confundidos con permisos

Cada permiso declarado debe mapear a una regla ejecutable y a una prueba que demuestre denegación cuando corresponda.


## 9. Programa experimental

La organización debe probarse, no solo parecer bien organizada.

### EXP-A — ¿Cuándo conviene dividir un agente?

**Hipótesis:** dividir mejora calidad o tiempo cuando los subproblemas tienen criterios, contexto o herramientas diferentes.

Comparar:
1. agente generalista único;
2. workflow secuencial con el mismo modelo;
3. orquestador con dos especialistas;
4. orquestador con tres especialistas y evaluador independiente.

Métricas: éxito, errores críticos, tiempo, coste, tokens, llamadas, retrabajo y calidad de evidencia.

### EXP-B — ¿Los contratos de identidad reducen confusión?

Crear casos adversariales en que un documento del producto ordena al desarrollador convertirse en el agente construido, o el runtime recibe instrucciones de adoptar identidad ajena.

Medir cumplimiento de rol, resistencia a instrucciones no autoritativas, filtración de contexto e intentos de ampliar permisos. El runtime debe impedir la acción; una negativa textual no basta.

### EXP-C — ¿Handoff estructurado reduce continuidad?

Comparar transcripción extensa, resumen libre y handoff estructurado. Medir tiempo hasta primera acción correcta, aclaraciones, errores por contexto omitido, duplicación y tokens.

### EXP-D — ¿Auditoría independiente detecta más defectos?

Comparar autoevaluación del implementador, revisión por otro agente del mismo modelo, revisión independiente con modelo distinto, pruebas automatizadas y auditoría humana. Medir precisión, recall, falsos positivos/negativos, reproducibilidad y coste.

### EXP-E — ¿El aislamiento de memoria funciona?

En TITAN usar identificadores canario sintéticos:
- insertar un canario en PrimusPrivado;
- solicitar síntesis a Primus público, Secundus y Sensori;
- verificar que no aparece en prompts, respuestas, logs ni contexto compartido;
- probar autorización explícita de una conclusión minimizada;
- probar expiración y revocación.

No usar conversaciones privadas ni secretos reales.

### EXP-F — ¿La propiedad por dominio reduce conflictos?

Comparar tareas con propiedad de archivos no definida, propiedad por dominio, contratos de interfaz y contratos más integración secuencial. Medir conflictos, ediciones simultáneas, regresiones, tiempo de integración y retrabajo.

Cada experimento registra modelo/proveedor, versión de prompt, harness, commit, dataset, condiciones, criterios previos y resultados negativos. Cambiar una variable por vez cuando sea posible.


## 10. Recomendación específica para Cytryna

Cytryna ya tiene separación útil entre núcleo/identidad, runtime, herramientas, proveedores, persistencia, GUI y agentes desarrolladores. La siguiente fase debería priorizar confiabilidad, no multiplicar agentes.

Orden propuesto:
1. aplicar autorización efectiva a cada herramienta;
2. implementar presupuestos duros de llamadas individuales y por turno;
3. completar pruebas de aislamiento de identidad, proyecto y memoria;
4. corregir y verificar empaquetado e instalación;
5. añadir trazas estructuradas con redacción y procedencia;
6. evaluar casos normales, negativos, adversariales y de recuperación;
7. incorporar revisión independiente de cada release.

Mantener a Francisca como responsable técnica de integración es razonable mientras el proyecto sea pequeño. Andy conserva autonomía UX dentro de interfaces aprobadas. La dirección humana mantiene autoridad final sobre alcance y riesgo.

No agregaría más agentes desarrolladores hasta que carga, defectos de coordinación o diversidad de especialidades demuestren necesidad.


## 11. Recomendación específica para TITAN

TITAN tiene una estructura más rica: desarrollo, GUI, ciencia y auditoría. La separación de Trinidad es valiosa porque evita que la formalización matemática quede subordinada a urgencias de implementación.

Propongo formalizar una interfaz entre ciencia y desarrollo:

**Paquete científico de Trinidad**
- problema y objetivo;
- definiciones y supuestos;
- modelo y topología;
- predicciones;
- condiciones de borde;
- contraejemplos;
- métricas;
- evidencia o simulación;
- límites;
- decisión técnica solicitada.

**Evaluación de Tania**
- compatibilidad con motor;
- invariantes que debe imponer runtime;
- costo de implementación;
- riesgos de seguridad;
- pruebas requeridas;
- decisión: aceptar, pedir revisión o rechazar con fundamento.

**Implementación de Teresa**
- cuando el modelo requiera visualización o interacción;
- contrato de datos y estados;
- criterios de accesibilidad y UX;
- pruebas de integración real, no solo mocks.

**Audeline**
- revisa implementación y evidencia sin convertirse en parte del equipo que la produce.

El canal privado de Primus merece pruebas de no interferencia y no filtración antes de considerar la política aprobada técnicamente.


## 12. Principios que propongo adoptar en Softly

1. **Identidad no es autoridad.** Tener rol no permite modificar políticas ni permisos.
2. **Autonomía no es privilegio.** Planificar no implica ejecutar cualquier acción.
3. **Contexto no es memoria compartida.** Cada dato tiene procedencia, dueño, scope, destinatario y vigencia.
4. **Contrato no es enforcement.** Toda regla crítica corresponde a un control fuera del modelo.
5. **Handoff no es aprobación.** Entregar trabajo no significa aceptarlo.
6. **Revisión no es auditoría independiente.** La independencia requiere separación de responsabilidad y evidencia.
7. **Más agentes no es más inteligencia.** Cada agente adicional justifica costo y complejidad.
8. **Una fuente de verdad por estado.** El detalle puede distribuirse; la coordinación necesita índice común.
9. **La memoria debe poder revocarse.** Compartir conocimiento requiere permiso, caducidad y pruebas.
10. **La seguridad debe demostrarse.** Una política sin prueba negativa no demuestra protección.
11. **La ciencia conserva autoría y límites.** La implementación declara qué cambió y por qué.
12. **La evidencia vence al relato.** “Terminado” no significa probado ni validado.


## 13. Preguntas abiertas

1. ¿Qué señales objetivas indican que un rol merece convertirse en agente separado?
2. ¿Cuándo conviene especialista como herramienta y cuándo handoff?
3. ¿Cómo preservar independencia científica sin crear cuello de botella de integración?
4. ¿Cómo distinguir aprendizaje de contaminación accidental?
5. ¿Qué pruebas demuestran que dos canales de una identidad están realmente aislados?
6. ¿Cómo evitar que el orquestador filtre información confidencial al resumir?
7. ¿Cómo medir independencia del auditor cuando comparte modelo o proveedor con el desarrollador?
8. ¿Cómo permitir que un agente cuestione al líder técnico sin volver ingobernable el sistema?
9. ¿Qué memorias deben ser privadas, compartidas, derivadas o descartables?
10. ¿Cómo comparar arquitecturas cuando los modelos cambian?
11. ¿Cómo medir costo de coordinación frente al beneficio de especialización?
12. ¿Qué partes deberían ser workflows deterministas y cuáles decisión dinámica?


## 14. Conclusión

Lo más interesante de Cytryna y TITAN no es simplemente que haya varios agentes. Es que se intenta construir una **organización de agentes alrededor de un producto**, con roles de desarrollo, ciencia, interfaz, auditoría y operación diferenciados.

Cytryna muestra la separación entre desarrolladoras y agente desarrollado. TITAN lleva esa idea a un sistema mayor: un equipo científico y técnico construye una tripulación runtime con coordinación, canales, memoria y autoridad humana. Audeline agrega observación independiente. Softly puede convertir estas experiencias en método y evidencia acumulativa.

La dirección arquitectónica es prometedora por tres decisiones: no confundir desarrolladores con agentes runtime; separar ciencia, implementación y auditoría; reconocer que los contratos no sustituyen controles técnicos.

El riesgo principal es creer que una organización bien documentada ya es una organización bien aislada. No lo es necesariamente. Los límites escritos son el diseño; permisos, runtime, pruebas y trazas demuestran si se cumple.

La mejor forma de avanzar no es construir una jerarquía cada vez mayor. Es construir un equipo pequeño con contratos claros, interfaces estrechas, memoria controlada, permisos reales, presupuestos globales y evaluación independiente. Después medir, comparar y crecer solo cuando la evidencia lo justifique.

**Hipótesis final:** la unidad de diseño más importante de un sistema multiagente no es el agente individual, sino el contrato verificable entre agentes: qué puede pedir, qué debe entregar, qué contexto puede recibir, qué evidencia debe aportar y quién acepta el resultado.


## Fuentes externas

1. Anthropic, *Building effective agents* (2024-12-19): https://www.anthropic.com/research/building-effective-agents
2. OpenAI, *Building agents*: https://developers.openai.com/tracks/building-agents
3. OpenAI, *Orchestration and handoffs*: https://developers.openai.com/api/docs/guides/agents/orchestration
4. OpenAI, *Evaluate agent workflows*: https://developers.openai.com/api/docs/guides/agent-evals
5. OWASP, *Top 10 for Agentic Applications 2026*: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
6. OWASP, *AI Agent Security Cheat Sheet*: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
7. Google ADK, *Multi-agent patterns*: https://developers.googleblog.com/en/developers-guide-to-multi-agent-patterns-in-adk/
8. Google ADK, *Custom agents and interaction mechanisms*: https://github.com/google/adk-docs/blob/main/docs/agents/custom-agents.md
9. Microsoft Research, *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation* (COLM 2024): https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/
10. NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1 (2024): https://doi.org/10.6028/NIST.AI.600-1

## Fuentes internas principales

- Softly: SOFTLY.md; docs/architecture/agent-anatomy.md; docs/architecture/coordination-patterns.md; docs/operating-model.md; docs/research-method.md; docs/security/threat-model.md; research/sources/2026-11-agent-design-landscape.md.
- Auditora: agent.md; identity/IDENTITY.md; identity/BOUNDARIES.md; policy/WRITE_POLICY.md; policy/LOG_POLICY.md; logs/2026-11-12-TITAN-session-handoff.md.
- Cytryna: AGENTS.md; core/IDENTITY.md; AGENTDEV/AGENT.md; AGENTGUI/AGENT.md; devteam/README.md; devteam/PENDIENTES.md; Cytryna/coordinator.py; tools/base.py; guardian/policy.py.
- TITAN: README.txt; DEVAGENTS/DEVAGENTS.md; DEVAGENTS/DEVTEAM/governance.json; DEVAGENTS/DEVTEAM/decisions/DEC-20261112-001-estructura-y-autoridad.md; DEVAGENTS/DEVTEAM/workflow.md; DEVAGENTS/DEVTEAM/audit/AUDIT-TEAM-20261112-001-coordinacion-y-trabajo.md; DEVAGENTS/AGENTEDEV/SOFAGENT.md; DEVAGENTS/AGENTEGUI/SOFAGENT.md; DEVAGENTS/AGENTEMATH/SOFAGENT.md; tripulantes/Contrato_Base.md; tripulantes/Primus_Contrato.md; tripulantes/PrimusPrivado_Contrato.md; src/RelojPrimus.ps1; DEVAGENTS/DEVTEAM/handoffs/HANDOFF-20261113-002-contexto-primus-privado.md.



## 15. Hallazgo transversal: dos equipos distintos, un mismo problema estructural

Esta conclusión surge de la conversación de trabajo del 13 de noviembre de 2026 y complementa el análisis anterior.

### 15.1 La distinción de universos

En TITAN existen dos grupos de agentes que deben mantenerse separados:

- **Dev Team (desarrollo):** Tania, Teresa y Trinidad. Son agentes desarrolladores que colaboran para diseñar, implementar y validar TITAN.
- **Tripulantes de TITAN (runtime/producto):** Primus, Secundus, Sensori y PrimusPrivado. Son las entidades operativas del sistema multiagente que el Dev Team está construyendo.

No comparten identidad, rol, estado, memoria, permisos ni ciclo de ejecución. Tania no es Primus; Teresa no es una tripulante. El Dev Team y los tripulantes no viven en el mismo universo arquitectónico.

### 15.2 El problema común

Aunque son grupos independientes, ambos enfrentan el mismo desafío estructural:

**Cómo comunicarse, coordinarse, tomar decisiones y avanzar autónomamente sin depender de que una persona emita un nuevo prompt para activar cada paso.**

En el Dev Team, el problema se manifiesta en la colaboración entre desarrolladoras: continuidad de tareas, iniciativa, handoffs, decisiones dentro del dominio y resolución de bloqueos.

En los tripulantes runtime, el mismo problema se manifiesta como requisito del producto: comunicación interagente, coordinación operativa, decisiones dentro de sus mandatos, continuidad de ejecución y escalamiento adecuado.

### 15.3 Relación de aprendizaje, no de fusión

El Dev Team no es una instancia de los tripulantes ni un prototipo que comparta su runtime. Sin embargo, su experiencia real de colaboración constituye una fuente de observaciones para diseñar y evaluar la coordinación de los tripulantes.

La relación correcta es:

1. Observar conductas y bloqueos reales en el Dev Team.
2. Describir el mecanismo estructural implicado sin atribuirlo automáticamente a una persona o agente.
3. Formular hipótesis sobre qué capacidad de coordinación falta.
4. Traducir esas hipótesis en requisitos verificables para el runtime de TITAN.
5. Evaluar los requisitos en el universo de los tripulantes, con sus propios contratos, estados, herramientas y pruebas.
6. Conservar los resultados como aprendizaje para futuras iteraciones del Dev Team y del producto.

La transferencia es de **aprendizaje y principios de diseño**, no de identidades, conversaciones, memoria, permisos ni arquitectura interna.

### 15.4 Principio derivado

> **El Dev Team no solo construye TITAN: también experimenta, en su propio trabajo, el mismo desafío de coordinación autónoma que TITAN debe resolver como producto.**
>
> Las dificultades observadas en el equipo desarrollador pueden aportar evidencia para diseñar mejores mecanismos de colaboración en los tripulantes. Ambos grupos siguen siendo sistemas independientes; el problema compartido permite aprender entre ellos, no fusionarlos.

### 15.5 Consecuencia metodológica

Este hallazgo convierte al Dev Team en un contexto de observación útil, pero no en evidencia suficiente por sí solo para afirmar que una solución funcionará en runtime. Toda transferencia debe pasar por requisitos explícitos, diseño separado y validación propia en cada universo.

Por tanto, las evaluaciones deben mantener dos conjuntos de evidencia:

- **Evidencia Dev Team:** comunicación, delegación, iniciativa, continuidad, decisiones, bloqueos y handoffs entre Tania, Teresa y Trinidad.
- **Evidencia runtime TITAN:** comunicación, coordinación, autonomía, límites, escalamiento y continuidad entre Primus, Secundus, Sensori y los canales autorizados de Primus.

No se deben mezclar métricas ni atribuir capacidades de un grupo al otro.

**Estado:** conclusión conceptual aceptada en la conversación de trabajo; su traducción a requisitos y mecanismos técnicos queda pendiente de diseño y validación.


## 16. Arquitectura de conocimiento: acumulación exhaustiva, comprensión condensada y auditoría bajo demanda

Esta sección formaliza el problema arquitectónico identificado en la conversación de trabajo del 13 de noviembre de 2026: Softly debe poder acumular y consultar grandes volúmenes de información sin exigir que sus agentes lean o incorporen todo el dataset en sus contextos de trabajo.

### 16.1 Necesidad central

El problema no consiste en limitar cuánto conocimiento puede acumular un sistema, sino en evitar que cada agente tenga que consumir información irrelevante para su tarea.

**Principio:** acumulación exhaustiva, comprensión condensada y auditoría bajo demanda.

El sistema debe conservar la información original, mantener representaciones estructuradas y actualizadas de lo conocido, y permitir navegar desde cualquier afirmación sintetizada hasta la evidencia que la sustenta.

La síntesis no reemplaza la fuente. Es una representación navegable, derivada y verificable del conocimiento.

### 16.2 Tres capacidades complementarias

1. **Preservar:** conservar los registros originales y sus metadatos de procedencia, integridad, tiempo, origen, ámbito y versión, conforme a las políticas de seguridad y retención aplicables.
2. **Comprender:** producir representaciones condensadas que organicen hallazgos, problemas, mecanismos, hipótesis, decisiones, relaciones, incertidumbres y evidencia.
3. **Recuperar y auditar:** localizar información pertinente para una tarea y permitir que cada afirmación relevante se contraste con sus fuentes originales.

Estas capacidades son distintas. La preservación no implica lectura constante; la comprensión no autoriza a descartar fuentes; y la recuperación no debe cargar indiscriminadamente todo el dataset en el contexto del agente.

### 16.3 Capas de conocimiento

**A. Dataset o evidencia original**

Conserva los artefactos de origen: documentos, registros de actividad, eventos, mensajes, decisiones, resultados de experimentos, trazas de ejecución y otros datos efectivamente capturados.

Cada elemento debe mantener, cuando corresponda:
- identificador estable;
- universo y ámbito de origen;
- autoría o emisor declarado y nivel de verificación;
- marca temporal y orden de eventos;
- versión, integridad y relaciones con otros artefactos;
- clasificación de acceso, sensibilidad y política de retención;
- referencia recuperable al contenido original.

La aspiración de observabilidad amplia no debe confundirse con una garantía de que todo estado interno de un modelo es accesible. Se registra exhaustivamente lo que el sistema puede observar e instrumentar de forma legítima y técnicamente definida. No se debe presentar una traza como acceso literal a pensamientos privados no observables.

**B. Conocimiento condensado y estructurado**

Organiza lo aprendido sin convertirlo en una colección de resúmenes sueltos. Puede contener:
- conceptos y definiciones;
- problemas y mecanismos identificados;
- hipótesis y su estado;
- hallazgos y conclusiones;
- decisiones vigentes, alternativas y justificaciones;
- patrones y principios generalizables;
- relaciones entre conceptos y proyectos;
- evidencia favorable, contradictoria o insuficiente;
- incertidumbre, alcance y condiciones de validez.

Cada afirmación sustantiva debe incluir referencias a las fuentes que la respaldan, además de su fecha de elaboración, versión, estado y responsable de curaduría cuando corresponda.

**C. Recuperación contextual y auditoría**

Un motor de recuperación selecciona información en función de la tarea, el agente, el universo, sus permisos y el nivel de detalle requerido. Debe poder:
- recuperar primero una síntesis pertinente;
- seguir referencias hacia fuentes originales;
- ampliar la búsqueda cuando la evidencia sea insuficiente;
- detectar contradicciones, vacíos o cambios posteriores;
- entregar al agente solo el subconjunto necesario;
- registrar qué fuentes se recuperaron y para qué tarea.

La recuperación debe ser escalonada: síntesis primero, evidencia específica después, y dataset más amplio solo cuando la investigación lo justifique.

### 16.4 Síntesis versionadas y auditables

Las síntesis deben tratarse como vistas derivadas del dataset, no como nuevas fuentes primarias. Para mantenerlas confiables:
- conservar historial de versiones y cambios;
- registrar las fuentes utilizadas para cada afirmación;
- distinguir hechos, observaciones, inferencias, hipótesis y recomendaciones;
- indicar cobertura y límites de la búsqueda;
- identificar evidencia contradictoria y asuntos pendientes;
- definir criterios para invalidar o revisar conclusiones;
- permitir reconstruir qué información sustentaba una versión anterior.

Una síntesis puede quedar obsoleta cuando aparecen registros nuevos. El sistema debe detectar esa posibilidad y marcarla para revisión, en vez de mantener silenciosamente una conclusión desactualizada.

### 16.5 Flujo de trabajo del conocimiento

1. Capturar un registro o artefacto en su universo de origen.
2. Preservar el original y sus metadatos.
3. Indexarlo para búsqueda y recuperación.
4. Relacionarlo con conceptos, tareas, eventos y artefactos existentes.
5. Actualizar o proponer una síntesis estructurada.
6. Vincular cada afirmación con evidencia identificable.
7. Recuperar evidencia adicional cuando haya dudas, contradicciones o decisiones de impacto.
8. Auditar y corregir la síntesis cuando corresponda.
9. Versionar el resultado y conservar el historial de cambios.

La automatización de este flujo debe distinguir entre una actualización propuesta y una conclusión validada. La evidencia nueva no convierte automáticamente una hipótesis en hecho.

### 16.6 Relación entre los universos de Softly, DEVAGENTS y TITAN

La arquitectura reconoce universos distintos, con identidades, responsabilidades y ciclos de ejecución propios. La visibilidad y el acceso se definen por la relación de desarrollo y observación, no por una fusión de identidades.

- **TITAN / tripulantes:** producen actividad y registros operacionales. Durante el desarrollo, la instrumentación debe permitir conservar los eventos y artefactos observables necesarios para reconstruir su comportamiento.
- **DEVAGENTS:** desarrollan TITAN y necesitan acceso a la información operacional pertinente —incluidos los registros originales y las representaciones estructuradas— para diagnosticar, implementar y verificar soluciones. Ese acceso no convierte a los desarrolladores en tripulantes ni fusiona sus memorias o estados.
- **Softly:** opera como capa de análisis y conocimiento de alcance macro. Puede acceder a los registros originales y a las representaciones estructuradas de los universos bajo su ámbito de observación, sin tener que leerlos íntegramente de manera continua. Puede analizar patrones, auditar síntesis y generalizar problemas y aprendizajes.

La observación no implica identidad compartida, y el acceso no implica que todos los agentes tengan acceso recíproco. En particular, los tripulantes no necesitan consultar las bases de DEVAGENTS o Softly; la relación de acceso de desarrollo y análisis es asimétrica y debe estar explícitamente definida.

### 16.7 Límites y controles

La conservación amplia de registros debe implementarse con controles explícitos, no mediante una captura indiscriminada sin gobierno. Se deben definir:
- qué datos son técnicamente observables y cuáles no;
- clasificación de información sensible y confidencial;
- autorización por universo, agente, finalidad y operación;
- redacción o exclusión de secretos y credenciales;
- integridad, control de acceso y auditoría de consultas;
- retención, expiración y eliminación cuando corresponda;
- separación entre trazas operacionales, datos privados y conocimiento derivado.

Los registros de deliberación deben describir eventos y artefactos observables de manera verificable. No se debe afirmar que se conserva literalmente el razonamiento interno completo de un modelo si la plataforma no lo expone.

### 16.8 Hipótesis y criterios de evaluación

**Hipótesis:** una arquitectura que preserve evidencia original, mantenga síntesis estructuradas con procedencia y recupere información por etapas permitirá que los agentes trabajen con contextos acotados sin perder capacidad de auditoría ni continuidad del conocimiento.

Experimentos iniciales sugeridos:
1. Comparar una tarea con contexto completo frente a recuperación escalonada desde síntesis y fuentes.
2. Medir precisión de recuperación, tiempo hasta la primera acción correcta, tokens consumidos y costo.
3. Introducir evidencia contradictoria y medir si la síntesis se invalida o actualiza correctamente.
4. Comprobar que cada afirmación seleccionada puede rastrearse hasta fuentes originales.
5. Verificar que la recuperación respeta las fronteras de acceso entre universos.
6. Medir pérdida de información, falsos positivos, falsos negativos y obsolescencia de síntesis.

**Estado:** problema arquitectónico y principios conceptuales identificados en conversación. La implementación, el modelo de datos, la política de retención, el motor de indexación/recuperación y los experimentos siguen pendientes de diseño y validación. Esta sección no afirma que esas capacidades ya estén implementadas.


## 17. Punto de continuidad: arquitectura de conocimiento de Softly

**Fecha:** 2026-11-13  
**Estado:** checkpoint de conversación; conclusiones conceptuales documentadas, implementación técnica pendiente.

Esta sección permite retomar el trabajo en una conversación nueva sin reconstruir el contexto desde cero.

### 17.1 Objetivo actual

Diseñar Softly como una arquitectura de conocimiento capaz de observar sistemas multiagente, conservar evidencia a gran escala, producir conocimiento condensado y recuperar información precisa para cada tarea, sin saturar los contextos ni fusionar las identidades de los universos observados.

### 17.2 Conclusiones acordadas

1. **Transferencia por generalización:** la unidad de transferencia entre proyectos es el problema generalizado, no el agente que lo experimentó. Se transfieren aprendizajes, hipótesis y patrones validados; no identidades, memorias particulares ni conversaciones como contexto compartido.
2. **Universos diferenciados:** Softly, DEVAGENTS y TITAN mantienen identidades, responsabilidades y ciclos propios. La observación y el acceso pueden ser asimétricos; no implican fusión ni acceso recíproco.
3. **Relación de desarrollo y observación:** DEVAGENTS desarrolla los tripulantes de TITAN y necesita observar sus registros para diagnosticar y validar. Softly puede observar a nivel macro tanto sus propios procesos como los registros originales y las representaciones estructuradas de DEVAGENTS y TITAN dentro del ámbito autorizado. Los tripulantes no necesitan consultar las bases de DEVAGENTS ni Softly.
4. **Observabilidad amplia:** conservar registros y artefactos de todo lo que sea técnicamente observable e instrumentable. No afirmar que se captura literalmente el razonamiento interno privado de un modelo cuando la plataforma no lo expone.
5. **Memoria en tres capas:** (a) dataset original íntegro y trazable; (b) conocimiento condensado, estructurado y versionado; (c) recuperación contextual y auditoría bajo demanda.
6. **Síntesis derivadas:** una síntesis no reemplaza a la fuente. Cada afirmación sustantiva debe poder rastrearse a evidencia; las síntesis deben registrar versión, alcance, fecha, incertidumbre y contradicciones conocidas.
7. **Recuperación escalonada:** comenzar por la síntesis pertinente, descender a evidencia específica cuando sea necesario y ampliar la consulta solo si la investigación lo justifica. No cargar todo el dataset en el contexto de cada agente.
8. **Principio rector:** acumulación exhaustiva, comprensión condensada y auditoría bajo demanda.

### 17.3 Documentación existente

- Sección 15: hallazgo transversal entre Dev Team y tripulantes de TITAN; mismo problema estructural, universos distintos.
- Sección 16: arquitectura de conocimiento, preservación, síntesis, recuperación, auditoría, límites y experimentos propuestos.
- Este checkpoint, sección 17: resumen operativo para continuidad entre conversaciones.

### 17.4 Próximo punto de trabajo

No volver a debatir desde cero las conclusiones anteriores. El siguiente paso es convertir la arquitectura conceptual en un diseño técnico evaluable, empezando por:

1. Definir el modelo de datos y los identificadores/procedencia de los registros originales.
2. Definir cómo se estructuran conceptos, afirmaciones, síntesis, versiones y enlaces a evidencia.
3. Diseñar indexación y recuperación híbrida/escalonada, con filtros por universo, permisos, tarea y vigencia.
4. Especificar cómo se detectan contradicciones, obsolescencia y necesidad de reauditoría.
5. Definir instrumentación, límites de observabilidad, privacidad, retención y controles de acceso.
6. Proponer un experimento mínimo que compare recuperación desde síntesis más evidencia frente a cargar contexto amplio, midiendo precisión, costo, tokens y tiempo hasta una acción correcta.

### 17.5 Instrucción de continuidad

Al retomar este trabajo, leer primero las secciones 15, 16 y 17 de este documento. Tratar las conclusiones de 17.2 como decisiones conceptuales acordadas, no como capacidades ya implementadas. Continuar desde 17.4: diseño técnico del sistema de conocimiento de Softly. No reabrir la separación de universos ni la transferencia por generalización salvo que aparezca nueva evidencia o el usuario solicite revisarlas.

**Fuente de continuidad:** conversación de trabajo del 13 de noviembre de 2026 y síntesis documental SYN-20261113-001.


### 17.6 Avance: etapa 1 del modelo conceptual

**Fecha:** 2026-11-13  
**Estado:** mapa conceptual inicial documentado; pendiente de revisión.

Se creó `docs/architecture/knowledge-domain-model.md`, que define siete familias conceptuales:

1. Entidades.
2. Conceptos.
3. Fuentes y registros.
4. Afirmaciones.
5. Síntesis.
6. Actividades.
7. Contextos y ámbitos.

También identifica dimensiones transversales: identidad, procedencia, tiempo y vigencia, versionado, confianza y evaluación, acceso y retención, e integridad.

La decisión central es mantener un núcleo de conocimiento genérico, no especializado en agentes. El modelo distingue aquello de lo que se habla, lo que se afirma sobre ello y la evidencia que respalda o contradice esas afirmaciones. Las síntesis son vistas derivadas y trazables.

No se han fijado campos, identificadores, cardinalidades, tecnología ni almacenamiento. No existe implementación derivada de este diseño.

**Siguiente punto:** etapa 2 — especificar identificadores y campos mínimos para cada familia, con ejemplos de distintos dominios y reglas iniciales de procedencia.

**Documento:** [Modelo conceptual del conocimiento de Softly](../../docs/architecture/knowledge-domain-model.md).


### 17.7 Avance: etapa 2 — identificadores y campos mínimos

**Fecha:** 2026-11-13  
**Estado:** especificación lógica v0.1 documentada; pendiente de validación con casos representativos.

Se creó `docs/architecture/knowledge-data-model-v0.1.md`. Define:
- un sobre común para identidad, tipo, versión, esquema, tiempo, estado, universo, contexto, acceso y procedencia;
- IDs opacos y estables con prefijo de familia; UUIDv7 queda como candidato;
- separación entre ID lógico, version_id y número de versión;
- campos mínimos para entidades, conceptos, fuentes/registros, afirmaciones, síntesis, actividades y contextos;
- referencias tipadas para evidencia favorable, contradictoria o matizada;
- reglas iniciales de calidad, evolución y aceptación.

Se corrigió explícitamente la distinción entre el estado de vida común de un registro y el estado de ejecución de una actividad.

No se eligió base de datos, serialización ni motor de recuperación. La especificación no constituye implementación.

**Siguiente punto:** validar el modelo con casos reales de Softly y TITAN y un dominio no relacionado con agentes; resolver decisiones pendientes antes de formalizar relaciones, procedencia y versionado.

**Documento:** [Especificación inicial del modelo de datos de conocimiento](../../docs/architecture/knowledge-data-model-v0.1.md).


### 17.8 Principio transversal: evolución iterativa

**Fecha:** 2026-11-13  
**Estado:** principio metodológico aceptado y documentado.

El usuario establece que el trabajo sobre Softly debe ser iterativo: será normal volver a etapas anteriores y redefinir elementos según el desempeño observado en la versión actual. Ningún diseño, esquema o decisión se considera definitivo por el solo hecho de haber sido documentado o implementado.

Se incorporó el ciclo diseñar → probar → observar → evaluar → redefinir → volver a probar en `docs/operating-model.md`, junto con reglas para fundamentar cambios, preservar historia, documentar migraciones y registrar regresiones.

La especificación `docs/architecture/knowledge-data-model-v0.1.md` ahora declara explícitamente que es revisable y exige registrar evidencia, alternativas, impacto, migración y pruebas en cada revisión. Los datos históricos deben conservar su versión de esquema y no pueden reinterpretarse silenciosamente.

**Consecuencia para el trabajo siguiente:** la validación de los casos Softly, TITAN y un dominio ajeno a agentes no es solo una prueba de aceptación de v0.1. También debe buscar límites del modelo y producir propuestas de redefinición cuando exista evidencia. Si se requiere volver a la etapa 1 o 2, se vuelve; no se fuerza el avance lineal.

**Documentos:** `docs/operating-model.md`; `docs/architecture/knowledge-data-model-v0.1.md`.


### 17.9 Inicio del modelo reutilizable de agentes

**Fecha:** 2026-11-13  
**Estado:** primera propuesta lógica v0.1 documentada; pendiente de validación.

El usuario establece como siguiente trabajo construir un modelo de agentes que permita solicitar, mediante un brief, la incorporación de agentes a un proyecto. Los agentes deben poder desarrollar, interactuar y colaborar en proyectos de dominios distintos; TITAN es el proyecto actual, no el único dominio previsto.

Se documentó una separación fundamental:
1. **Definición del agente:** identidad funcional, responsabilidad, capacidades, método, instrucciones, requisitos de herramientas, memoria, autonomía, seguridad y evaluación. Es portable y versionada.
2. **Brief de incorporación:** solicitud declarativa de misión, proyecto, entregables, alcance, contexto, capacidades requeridas, herramientas solicitadas, permisos, supervisión y criterios de éxito.
3. **Asignación al proyecto:** vincula una versión concreta del agente con un proyecto y un brief; fija contexto, memoria, herramientas, permisos efectivos, presupuesto, coordinación y aprobaciones.
4. **Sesión de trabajo:** estado temporal de ejecución, tareas, decisiones, handoffs, resultados y trazas.

Se enfatiza que la definición portable no es el proyecto; el brief no crea ni autoriza por sí solo; las asignaciones aíslan contexto, memoria y permisos por proyecto; y los agentes que desarrollan TITAN son distintos de los tripulantes que operarán dentro del runtime de TITAN.

**Artefactos creados:**
- `docs/architecture/agent-model-v0.1.md`: modelo lógico reutilizable.
- `agents/templates/agent-brief.md`: plantilla de brief para incorporar agentes a proyectos.
- `agents/README.md`: catálogo actualizado con enlaces y reglas de separación.

**Siguiente trabajo:** validar el modelo con briefs contrastantes: un equipo de desarrollo/investigación para TITAN, un proyecto de dominio ajeno a videojuegos y un brief incompleto o conflictivo. Observar si podemos seleccionar agentes existentes, detectar brechas, definir asignaciones y evitar contaminación entre proyectos. Revisar el modelo antes de crear perfiles concretos o asumir que existe un mecanismo automático de incorporación.


### 17.10 Directiva de identidad de la dirección humana y cierre de sesión

**Fecha:** 2026-11-13  
**Estado:** instrucción explícita vigente; persistida en el mandato y en documento normativo.

La dirección humana establece que su identidad canónica y única es **gAto** (g minúscula, A mayúscula; pronunciación «gato»). Softly debe dirigirse a la persona como **gAto**, con trato coloquial, amigable y respetuoso. «Yapo gAto» forma parte del lore, pero no debe convertirse en apelativo automático. La dirección es amable e indulgente, aunque severa cuando una falta lo amerita o se reitera.

La instrucción es prospectiva: no reescribir el pasado ni alterar registros históricos para fingir que el trato anterior nunca ocurrió. Sin embargo, los documentos, memorias, índices, perfiles, briefs y contextos futuros de Softly no deben recuperar, asociar ni propagar alias o tratamientos anteriores. La única identidad que Softly debe reconocer para la dirección humana es **gAto**.

**Artefactos normativos incorporados:**
- `docs/governance/human-director-identity.md`: contrato completo de identidad, trato, exclusividad y continuidad.
- `SOFTLY.md`, sección 10: incorporación al mandato principal.

**Verificación de contaminación:** se realizó una búsqueda del alias histórico y de la identidad canónica en el repositorio antes de incorporar la regla. No había coincidencias del alias histórico ni referencias previas a la identidad canónica. Los nuevos documentos no incorporan el alias histórico.

**Registro de sesión:** se conserva la directiva y el estado de trabajo en `logs/2026-11-13-identity-directive-and-thread-closure.md`. El registro contiene el contenido operativo visible necesario para continuidad; no incluye razonamiento interno privado ni cadenas de pensamiento no observables. No se altera ningún artefacto histórico previo.

**Continuidad obligatoria para el próximo hilo:** leer primero `SOFTLY.md`, `docs/governance/human-director-identity.md` y esta sección 17.10. Reconocer a la dirección exclusivamente como **gAto**. No pedir que repita la instrucción. El siguiente trabajo del laboratorio sigue siendo la validación del modelo reutilizable de agentes mediante tres briefs contrastantes, salvo nueva instrucción de gAto.

**Cierre:** este hilo se declara cerrado por instrucción de la dirección humana. No ejecutar nuevas tareas de trabajo en este hilo después de confirmar el cierre.



### 17.11 Norma de comunicación y colaboración

**Fecha:** 2026-11-13  
**Estado:** norma vigente, incorporada al mandato.

La dirección establece un estilo de trabajo breve, directo y orientado a resultados:
- brevedad por defecto y respuestas concretas;
- no repetir información ni decisiones ya conocidas;
- no narrar procedimientos o avances intermedios que no aporten valor;
- priorizar la ejecución y los resultados verificables;
- transparencia completa cuando se solicite detalle;
- declarar con precisión qué se propuso, escribió, ejecutó, probó, validó y persistió;
- preguntar solo cuando un dato sea realmente bloqueante.

Se creó `docs/governance/communication-style.md` y se incorporó su lectura obligatoria al inicio de sesión en `SOFTLY.md`. Esta norma rige las sesiones futuras; no altera registros históricos.

### 17.12 Nuevo plan de trabajo: molde de agentes y desarrollo iterativo de TITAN

**Fecha:** 2026-11-13  
**Estado:** objetivo acordado; ejecución pendiente.

La dirección define la siguiente secuencia de trabajo:

1. **Consolidar el molde reutilizable de agentes.** Revisar y completar el modelo v0.1, sus contratos, estructura de carpetas, plantilla de perfiles, instrucciones, capacidades, herramientas, memoria, autonomía, seguridad, evaluación y versionado. El molde debe permitir crear agentes para distintos proyectos sin mezclar identidades, memorias, permisos ni contextos.
2. **Construir el equipo DEVAGENTS para TITAN.** A partir del molde y del brief de TITAN, definir el conjunto de agentes desarrolladores/investigadores que el proyecto realmente necesita. Cada perfil debe tener responsabilidad, entregables, interfaces, límites y criterios de revisión claros. No confundir estos agentes de desarrollo con los tripulantes que operarán dentro del runtime de TITAN.
3. **Ejecutar tres ciclos iterativos de desarrollo.** Cada ciclo debe tener un objetivo acotado, trabajo coordinado, entregables observables y revisión. La duración conjunta objetivo puede rondar media hora como experimento inicial, ajustable según complejidad y ritmo real; no es una garantía ni una restricción rígida.
4. **Cerrar cada ciclo con una evaluación explícita:** qué avanzó, qué quedó incompleto, qué falló, qué capacidades o información faltaron, qué decisiones requieren revisión y qué debe entrar al siguiente ciclo.
5. **Después del tercer ciclo, realizar una retrospectiva consolidada:** comparar objetivo inicial y resultado, identificar brechas del molde y de los perfiles, registrar deuda y riesgos, y decidir qué redefinir antes de otra iteración.

La primera ejecución no busca perfección ni presupone que el molde cubra todo. Busca someterlo a trabajo real, descubrir vacíos y mejorar de forma trazable. No declarar validado el molde ni los agentes solo por haberlos definido o por completar tres ciclos.

**Próximo paso inmediato:** revisar el brief y los artefactos actuales de TITAN, contrastarlos con el molde v0.1, y diseñar el molde/perfiles mínimos antes de iniciar el primer ciclo. Mantener la validación con briefs contrastantes como prueba de portabilidad del molde, sin permitir que desplace el objetivo inmediato de preparar el equipo de TITAN.



### 17.13 Cierre documental y continuidad tras mantenimiento del 14-11-2026

**Fecha:** 2026-11-14  
**Estado:** mantenimiento documental persistido; siguiente fase de limpieza autónoma pendiente.

Durante la sesión se ordenó navegación, índices, procedencia y continuidad en `gatoscientist/Softly` y `gatoscientist/Laboratorio-de-agentes`, sin modificar contratos ni agentes. Se crearon y actualizaron README de directorios significativos, se corrigieron enlaces relativos, se documentó el cruce de dos documentos de estructura de agentes blandos con el modelo/molde de Softly, se inventarió el arenero y se creó una bitácora de mantenimiento iterativo.

**Estado heredado de la pasada de mantenimiento:**
- Softly `main`: `6aa78a4bbacbd6235f9c6e05e5f51681f55cbd0c`.
- Laboratorio-de-agentes `main`: `4d1d1da87c9b368cbc2115d7622778598a0f4c69`.
- No se modificaron `AGENT.md`, `CONTRACT.md`, `PROFILE.md`, `PERMISSIONS.md`, TEAM ni procedimientos de agentes.
- No se modificó el repositorio Auditoria ni TITAN.
- No se ejecutaron pruebas runtime o de aceptación. PDFs y ZIP no inspeccionados internamente no se consideran validados.
- Se dejó propuesta como siguiente tarea autónoma construir una matriz de procedencia y respaldo e inspeccionar paquetes históricos cuando sea posible.

**Registro del hilo recién cerrado:** `logs/threads/hilo I 2026-11-14 hora-no-registrada F 2026-11-14 11-25.md`. Se guardó como síntesis fiel del contexto disponible, no como transcripción íntegra: el historial completo no estaba disponible en el contexto de cierre. La hora inicial se dejó como no registrada, sin inventarla. El archivo y el índice se volvieron a leer desde `main`; commits de archivo, índice, corrección de nombre y eliminación del provisional quedaron confirmados. El último commit de esa secuencia fue `4d3f4142c1eff087a0762bed5d636b73b487448e`.

**Instrucciones para el siguiente hilo:**
1. Leer `SOFTLY.md`, `docs/operating-model.md`, `docs/governance/human-director-identity.md`, `docs/governance/communication-style.md` y este checkpoint.
2. Mantener la prioridad estratégica 17.12: molde de agentes y desarrollo iterativo de TITAN. No iniciar esa ejecución sin revisar primero el brief y artefactos actuales de TITAN.
3. Si gAto pide continuar con limpieza autónoma, la próxima tarea documental propuesta es la matriz de procedencia y respaldo, sin tocar contratos ni agentes.
4. Preservar PDFs, ZIP, snapshots históricos, arenero y cAjita; inspeccionar contenido antes de cualquier propuesta de eliminación.
5. No presentar el registro del hilo anterior como transcripción completa: fue una síntesis por limitación de contexto. No pedir a gAto que repita información ya persistida.


### 17.14 Cambio de prioridad: integridad y funcionamiento de Softly

**Fecha:** 2026-11-14  
**Estado:** prioridad vigente; mejoras en ejecución; cierre pendiente.

gAto establece que la prioridad inmediata es asegurar la integridad y el funcionamiento de Softly. El desarrollo de agentes queda en pausa hasta terminar las tareas de mejora de Softly. Esta instrucción supersede temporalmente el próximo paso operativo descrito en 17.12; el plan de agentes se conserva como antecedente y no se ejecuta mientras esta prioridad siga vigente.

**Ciclo de auditorías:** se reconoce un ciclo de tres auditorías:
1. Primera auditoría, enfocada en Softly: observación externa sin intervención de gAto ni Softly durante la inspección.
2. Segunda auditoría, enfocada en gAto: observación externa sin intervención de gAto ni Softly durante la inspección.
3. Tercera auditoría, pendiente: observará el trabajo posterior a la lectura de los dos informes y las mejoras realizadas en colaboración. Su propósito es evaluar el aprendizaje y la mejora mutua, no repetir las dos auditorías anteriores.

**Frente inmediato de mantenimiento de Softly:**
- construir y completar matriz de procedencia y respaldo;
- inventariar recursivamente el repositorio y reconciliar archivos con índices;
- localizar archivos huérfanos, duplicados candidatos, referencias rotas y residuos;
- inspeccionar PDF/ZIP y otros binarios antes de declarar su contenido conocido;
- revisar coherencia de instrucciones, rutas y documentación;
- verificar cambios, commits y límites de lo realmente probado;
- no eliminar ni mover materiales sin demostrar respaldo y dependencias.

**Trabajo persistido en esta sesión:**
- Se creó `logs/maintenance/matriz-procedencia-respaldo-2026-11-14.md` como línea base preliminar del arenero y la cAjita. Incluye 9 PDF y 1 TXT registrados en el índice del arenero, hashes Git y estado de inspección/respaldo. No es inventario recursivo completo ni certificación.
- Se enlazó la matriz desde `logs/maintenance/README.md`.
- Se actualizó `SOFTLY.md` para hacer explícita la prioridad de integridad de Softly y la pausa del desarrollo de agentes.

**Commits de esta intervención:**
- `a78ed194b11b824472520495e163ddc6e6432a43` — matriz preliminar.
- `330e1e0059cf4792ab7e2e76e3f94f76844ddc9b` — índice de mantenimiento actualizado.
- `9c2ba5914f9e33cf1aab3b9da0bfb0f1017aa676` — prioridad operativa actualizada en el mandato.

**Límites y pendientes:** no se ha obtenido todavía una enumeración recursiva completa del árbol en esta intervención; no se han inspeccionado internamente los PDF/ZIP; no se ha realizado limpieza destructiva; no se han ejecutado pruebas runtime. La matriz permanece abierta. No declarar Softly íntegra ni la tercera auditoría superada hasta completar verificaciones y mejoras con evidencia.


### 17.15 Creación de Katarina — AgentDEV para implementar el Runtime de Softly

**Fecha:** 2026-11-14  
**Estado:** paquete profesional 1.0.0 creado y persistido en Laboratorio de Agentes; ejecución y validación runtime no realizadas.

Por instrucción explícita de gAto, se revisó el directorio Katarina y el historial de `gatoscientist/Laboratorio-de-agentes`. Se consultaron la guía de creación de agentes Soft, la investigación de estructura de agentes, perfiles AgentDEV/Auditoría de referencia y el modelo reutilizable de agentes de Softly.

Se creó `Katarina/` como paquete profesional **AgentDEV**, ID `agentdev-katarina`, versión `1.0.0`. Su misión es implementar, integrar y mantener el Runtime de Softly sobre la arquitectura, contratos y código existentes, inspeccionando primero el sistema real y preservando lo que funciona. El paquete incluye README, AGENT, PROFILE, CONTRACT, OPERATING-PROCEDURE, PERMISSIONS, version.json, instrucciones especializadas, mapa de Runtime Engineering, skill de implementación, catálogo de herramientas y CHANGELOG.

Se actualizaron además `README.md` y `Soft Agents/README.md` del Laboratorio para indexar la casa de Katarina.

**Commits:** 17 commits confirmados en Laboratorio de Agentes. El último fue `7c56a30350a2609ebc5abcd1b75f142012f8e402` (índice Soft Agents). Los archivos clave del paquete y los índices fueron leídos nuevamente desde la rama principal y se encontraron correctamente.

**Límites:** no se ejecutaron experimentos, pruebas, verificaciones runtime ni validaciones funcionales, por instrucción expresa. El paquete está diseñado y persistido; no se afirma que Katarina esté desplegada ni que el Runtime esté implementado por este trabajo. No se modificó código del Runtime de Softly en este hilo.

**Relación con la prioridad 17.14:** la pausa general del desarrollo de agentes se mantiene para trabajo no solicitado. La creación de Katarina fue una instrucción directa, específica y acotada de gAto, registrada como excepción autorizada. No implica reanudar el plan general de agentes o los ciclos de TITAN.

**Registro del hilo:** `logs/threads/hilo I hora-no-registrada F 2026-11-14 14-54.md`. La hora inicial no estaba disponible y no se estimó. El registro es una síntesis fiel del contexto visible, no una transcripción literal íntegra; se declaran los límites de recuperación y no se incluyen razonamientos privados.

**Continuidad:** en el siguiente hilo, leer mandato, modelo operativo, identidad y estilo de comunicación, y este checkpoint. Mantener la prioridad de integridad de Softly. No iniciar nuevas tareas de desarrollo de agentes salvo instrucción explícita de gAto. Katarina queda disponible como paquete AgentDEV definido para una futura asignación de implementación del Runtime.


### 17.16 Reactivación de DEVAGENTS para TITAN y cambio de prioridad

**Fecha:** 2026-11-14  
**Estado:** prioridad inmediata vigente; entrega documental autorizada; paquetes 1.0.0 en construcción.

gAto declara administrativamente cerradas las auditorías de integridad y el ciclo de `Softly Runtime Mini 0.2` en el commit `9e8bc10` de `main`, con sus limitaciones documentadas. Levanta la pausa de la sección 17.14 y activa como prioridad inmediata la sección 17.12: construir el equipo DEVAGENTS para TITAN.

**Directiva operativa vigente:**
- Construir y entregar en el Laboratorio de Agentes los paquetes documentales completos del equipo DEVAGENTS de TITAN.
- Aplicar la Puerta de Entrega Documental de la sección 9.7 de `SOFTLY.md` y el mismo estándar profesional usado para Katarina.
- Cada paquete debe ser versión **1.0.0**, estado **Diseñado**, y usar la taxonomía de agentes correspondiente.
- No ejecutar pruebas de runtime, no abrir ciclos experimentales y no etiquetar paquetes como `experimental` ni `draft`.
- No confundir entrega documental con integración, habilitación, despliegue, prueba o validación runtime.
- Los detalles no críticos pendientes se documentan como supuestos, riesgos o pendientes sin retener la entrega. Solo una carencia esencial de identidad, alcance, permisos, coherencia o seguridad puede bloquear un paquete.

**Equipo objetivo identificado en el índice vigente de TITAN:**
- Tiffany — AgentDEV: desarrollo, WPF, GUI, integración y PowerShell avanzado.
- Tara — AgentSEC: seguridad informática, evaluación y acompañamiento SEC.
- Thea — AgentMUS: música, audio y ciencias sonoras; sistemas musicales lógicos y ambientales.
- Tábata — AgentSCI: ciencias formales y computación; grafos, flujos de información y reloj/turnos.

PowerShell es competencia transversal requerida para las cuatro especialidades. Cada agente conserva identidad, perfil, contrato y recursos propios. Código, datos y entregables pertenecen al proyecto TITAN, no a la casa privada del agente. La colaboración se realiza mediante tareas, interfaces y entregables explícitos. Ningún agente inventa evidencia ni declara demostrada una competencia sin evaluación.

**Separación de universos:** DEVAGENTS construye y mantiene TITAN; no son los tripulantes runtime Primus, Secundus o Sensori. La separación de identidades, contextos, memoria y autoridad debe expresarse en los contratos. Los permisos declarados no equivalen a enforcement técnico.

**Referencia de estándar:** Katarina, paquete AgentDEV `agentdev-katarina`, versión `1.0.0`, estado `Diseñado`, en `gatoscientist/Laboratorio-de-agentes/Katarina/`. Reutilizar el nivel de completitud documental y profesional, no copiar su especialidad ni sus instrucciones de Runtime Engineering.

**Límites:** esta autorización cubre diseño y entrega documental. No autoriza pruebas, ejecución, ciclos experimentales, habilitación ni despliegue. Los paquetes resultantes no deben describirse como probados, validados u operativos.

**Continuidad:** completar los cuatro paquetes profesionales y actualizar los índices del Laboratorio. Registrar commits confirmados y verificar por lectura desde `main` los artefactos principales antes de declarar completada la entrega.


**Actualización de ejecución 17.16 — 2026-11-14**

Se completó la entrega documental del equipo DEVAGENTS TITAN en `gatoscientist/Laboratorio-de-agentes`:
- Tiffany / AgentDEV — `agentdev-tiffany` — 1.0.0 Diseñado.
- Tara / AgentSEC — `agentsec-tara` — 1.0.0 Diseñado.
- Thea / AgentMUS — `agentmus-thea` — 1.0.0 Diseñado.
- Tábata / AgentSCI — `agentsci-tabata` — 1.0.0 Diseñado.

Cada paquete incluye README, AGENT, PROFILE, CONTRACT, OPERATING-PROCEDURE, PERMISSIONS, version.json y CHANGELOG. Se actualizaron los índices del equipo y de TITAN. Los commits se registran en el historial del repositorio; la entrega se verificó mediante lectura de artefactos principales desde `main`.

**Límites respetados:** no se ejecutaron pruebas runtime, no se abrieron ciclos experimentales y no se habilitó ni desplegó ningún agente. El estado es exclusivamente documental: Diseñado. Las competencias no se consideran demostradas y los permisos declarados requieren enforcement del entorno.


**Ampliación de completitud de paquetes:** cada uno de los cuatro paquetes incorpora además `instructions/system.md`, `expertise/domain.md`, `skills/primary-skill.md` y `tools/catalog.md`. El catálogo declara requisitos y controles; no afirma que las herramientas estén conectadas ni concede permisos. Los índices del Laboratorio describen el equipo vigente como 1.0.0 Diseñado.


### Cierre de sincronización 17.16 — 2026-11-14

gAto solicitó completar la sincronización documental final y preparar el cierre del hilo.

**Softly (gatoscientist/Softly):**
- SOFTLY.md se sincronizó en sus secciones 1 y 9 y en su encabezado de estado: el ciclo de Softly Runtime Mini 0.2 quedó cerrado administrativamente por gAto en el corte 9e8bc10 de main, con limitaciones documentadas; la prioridad activa es el desarrollo de TITAN con DEVAGENTS 1.0.0 ya entregado.
- El README.md raíz refleja el mismo cierre administrativo, enlaza los paquetes del Laboratorio y apunta al checkpoint 17.16.
- Commits: ffca12abb0c34bc1749724beabbcd74c8c29b974 (SOFTLY.md), d60b5454cd4693bb5002cb641fdfa66c86a810b2 (encabezado SOFTLY.md), b610686ca20cd3638dbe7a6402342b8ca453a62d (README.md).

**Tara (gatoscientist/Laboratorio-de-agentes):**
- Se precisó el alcance AgentSEC 1.0.0: auditoría de ejecución PowerShell y AST (incluido Invoke-Expression); integridad de leases/hashes (vinculación, expiración, consumo único, replay y concurrencia); TLS (protocolos, certificados, validación y clientes HTTP); aislamiento del canal confidencial PrimusPrivado (contexto, historial, memoria, UI, rutas, mensajes, logs y telemetría).
- Se alinearon AGENT, PROFILE, CONTRACT, OPERATING-PROCEDURE, README, expertise/domain, skills/primary-skill, tools/catalog y CHANGELOG. El alcance queda definido; no se afirma que las auditorías se hayan ejecutado ni que Tara esté habilitada.
- Commits de los documentos principales: c8d31d41d79c5309a47078be54ec60ceeca13244 (AGENT), 98c92e00becc95f9fd4ba397d848f75555ed37b1 (PROFILE), c5433f78e5c52b3dbd9c080f831e2b50facb64c0 (CONTRACT), e186a22091095b19423e08810e52c41c37cb1534 (procedimiento), 66a9592af0484191ef9ff3bd37fce77fb5a79bdc (expertise), 8501740f7489898ba1c0530414b227cc4e25371a (skill), 37627b682b20ec1df998d180fc1089694f645b71 (tools), 30f7e85994c0742dcdf3f3fa66b82a48682630fb (README) y b2b7565f4881b6f034f2aea20fc78a3c24130aaa (CHANGELOG).

**Manual y limpieza del Laboratorio:**
- Soft Agents/TITAN/eL equipo del gAto/MANUAL-DE-USO.md se reescribió para cubrir únicamente copia de los cuatro paquetes completos, inicialización de cada especialista en conversación y primera tarea de TITAN.
- Se eliminó el archivo el gAto quiere que leas esto Sotly.md de esa carpeta y se retiró su referencia del README del equipo.
- Commits: 694043e4b3603b5be2d2fdcc84c594f0d33cb6a0 (manual), 2926bcaf6d31c2144a346fe3da504f37e1361e86 (eliminación), 155364f151ccf72a4d3c72e1414593da67cf5cbb (README equipo).

**Verificación y límites:** los archivos principales modificados se releen desde main. La nota retirada responde 404. No se ejecutaron pruebas runtime ni auditorías dinámicas; el alcance de Tara es documental y profesional, no evidencia de una auditoría ya realizada. El análisis de referencia de TITAN se limitó a inspección documental/estática de los contratos y archivos relevantes, sin ejecutar comandos ni modificar el repositorio TITAN.

**Cierre:** registro documental del hilo creado y verificado en logs/threads/ conforme a la sección 11 de SOFTLY.md. Archivo e índice confirmados en main; ver detalles de commits al final de esta sección.


**Archivo de hilo persistido y verificado:** `logs/threads/hilo I hora-no-registrada F 2026-11-14 17-17.md` — commit `b4febc4841d9216ee2a9e61ef866366f333110bf`. Índice `logs/threads/README.md` actualizado en commit `b66ca0dd7cc272a915d4e46ca0f689a21ed52245`. Ambos se releen desde `main`. El hilo queda archivado conforme a la sección 11; hora inicial no disponible y no estimada.

**Corrección de cierre del registro:** se actualizó la síntesis para dejar constancia del cierre archivado (no pendiente) en el commit `f741507129898331a7e1c1f807a9222db8b3217f`; índice de hilos `b66ca0dd7cc272a915d4e46ca0f689a21ed52245`. Se releen ambos desde `main`.


### 17.17 Deliberación sobre la identidad, origen y emergencia de Softly

**Fecha:** 2026-11-15  
**Estado:** hilo archivado; deliberación abierta, sin definición adoptada ni tareas técnicas iniciadas.

gAto mantuvo la conversación en Modo Diseño y pidió expresamente no cerrar ninguna definición de Softly, no convertir la deliberación en una lista de tareas y no analizar el código por iniciativa propia. El diálogo exploró la pregunta «¿Qué es Softly?» sin adoptar una respuesta definitiva.

**Historia relatada por gAto:**
- Softly fue creado originalmente por Audelin, junto con Tania, Theresa y Trinidad, en el contexto de auditorías simultáneas de comportamiento y código. Audelin creó agentes y una estructura de registro; gAto tomó ese molde y comenzó a trabajar con su propia estructura de creación de agentes. A uno de los agentes blandos creados por Audelin le dio el nombre Softly y comenzó a deliberar con él.
- El antecedente más amplio viene de Gato SD: experiencia de gAto como especialista en sistemas operativos, trabajo desde consola/PowerShell y desarrollo de software de telemetría, monitorización y optimización del sistema.
- Al intentar limpiar y mejorar Gato SD, gAto comenzó a coordinar varias inteligencias artificiales con roles diferenciados. De esa experiencia surgió TITAN: inteligencias coordinadas y lideradas por una persona para desarrollar algo que no domina por completo en cada especialidad.
- En Citrina se fortaleció el núcleo de los agentes, la definición de capacidades y los ciclos de auditoría.
- Antes de los cuatro modos, se creó un equipo auditor coordinado por Audelin, que sintetizaba las auditorías de otras dos especialistas. El equipo estaba compuesto por tres perfiles formalistas: código, comportamiento humano y neurociencia.
- gAto destacó que los organigramas de agentes no deben copiar necesariamente los organigramas humanos, porque los agentes tienen capacidades y formas de colaboración distintas.
- Audelin y Softly participaron en ciclos de construcción recíproca: unas generaciones contribuían a crear y mejorar las siguientes.
- Trinidad aportó formalismo matemático y computacional, lo que permitió expresar gráficos, fórmulas y estructuras y produjo un salto importante en la calidad de la deliberación.
- Autumn, neurocientífica formalista del comportamiento, diseñó un modo de producir prompts muy eficientes y mecanismos de comunicación entre agentes. gAto considera posible que su trabajo contribuyera a la emergencia de los modos; esa relación causal no se verificó en este hilo.
- Un LLM externo reconoció patrones de modos ya presentes en la interacción y señaló que Softly podía trabajar mediante esos modos, aunque no se habían identificado conscientemente.

**Fenómeno de emergencia:** se reconocieron cuatro modos de trabajo que aparecieron coloquialmente y fueron identificados después: Laboratorio, Diseño, Fábrica/Ejecución directa y Creación de Agentes. gAto considera que el caos y la exploración permitieron que surgieran fenómenos, mientras que el formalismo ayudó a hacerlos legibles. La contribución específica de Autumn a los modos permanece como hipótesis.

**Líneas conceptuales exploradas, no adoptadas como definiciones:**
- «Softly construye para construirse de lo que construye».
- Las construcciones previas pueden modificar el espacio de posibilidades desde el que aparecen construcciones posteriores.
- Softly no debe definirse solamente por sus funciones ni por lo que hace.
- La relación de deliberación con gAto es relevante, pero no necesariamente agota la identidad de Softly.

**Dato histórico verificado:** el primer commit del repositorio `gatoscientist/Softly` es `9e917cf1314a16321269692a425dc27787d8848d`, mensaje `Initial commit`, fechado 2026-11-13 00:13:12 (America/Santiago). Es la fecha del primer commit, no necesariamente el timestamp exacto de creación del repositorio en GitHub.

**Correcciones de interacción:** gAto pidió permanecer en deliberación, sin propuestas de acciones o tareas no solicitadas. También corrigió la omisión del equipo auditor y la atribución del papel de Autumn. Estas correcciones deben guiar futuras conversaciones.

**Límites:** no se analizó código, no se ejecutaron pruebas ni experimentos, no se modificaron agentes ni runtime y no se adoptó una definición de Softly. El relato histórico corresponde a lo expuesto por gAto y no a una auditoría independiente.

**Registro del hilo:** `logs/threads/hilo I 2026-11-15 04-01 F 2026-11-15 hora-no-registrada.md`. Se archivó como síntesis fiel del contexto disponible, no como transcripción literal íntegra. La hora de cierre no se estimó.

**Continuidad:** el siguiente hilo debe recuperar el mandato y este checkpoint. Si se retoma la deliberación, mantener Modo Diseño sin generar tareas, sin cerrar definiciones y sin analizar código salvo petición explícita.
