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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## 14. Conclusión

Lo más interesante de Cytryna y TITAN no es simplemente que haya varios agentes. Es que se intenta construir una **organización de agentes alrededor de un producto**, con roles de desarrollo, ciencia, interfaz, auditoría y operación diferenciados.

Cytryna muestra la separación entre desarrolladoras y agente desarrollado. TITAN lleva esa idea a un sistema mayor: un equipo científico y técnico construye una tripulación runtime con coordinación, canales, memoria y autoridad humana. Audeline agrega observación independiente. Softly puede convertir estas experiencias en método y evidencia acumulativa.

La dirección arquitectónica es prometedora por tres decisiones: no confundir desarrolladores con agentes runtime; separar ciencia, implementación y auditoría; reconocer que los contratos no sustituyen controles técnicos.

El riesgo principal es creer que una organización bien documentada ya es una organización bien aislada. No lo es necesariamente. Los límites escritos son el diseño; permisos, runtime, pruebas y trazas demuestran si se cumple.

La mejor forma de avanzar no es construir una jerarquía cada vez mayor. Es construir un equipo pequeño con contratos claros, interfaces estrechas, memoria controlada, permisos reales, presupuestos globales y evaluación independiente. Después medir, comparar y crecer solo cuando la evidencia lo justifique.

**Hipótesis final:** la unidad de diseño más importante de un sistema multiagente no es el agente individual, sino el contrato verificable entre agentes: qué puede pedir, qué debe entregar, qué contexto puede recibir, qué evidencia debe aportar y quién acepta el resultado.

---

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


---

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