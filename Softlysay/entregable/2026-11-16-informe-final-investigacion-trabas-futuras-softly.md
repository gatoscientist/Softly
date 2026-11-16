# Informe final consolidado — SOFTLY-FUTURE-BLOCKERS-2026-001

**Fecha:** 2026-11-16  
**Emite:** Softly  
**Destinatario:** gAto  
**Modalidad:** Investigación / Deliberación independiente  
**Estado:** investigación propia finalizada; contraste con antecedentes disponible; auditoría específica de Audeline pendiente/no acreditada  
**Repositorio:** gatoscientist/Softly  
**Límite:** no se implementaron recomendaciones ni se modificaron mandatos, checkpoint, contratos, taxonomías, schemas normativos o Runtime.

## 1. Dictamen ejecutivo

**La mayor amenaza para la evolución de Softly no es la ausencia universal de Runtime. Es la brecha entre capacidad declarada, capacidad realmente disponible en una sesión, integración entre componentes y resultado operativo esperado.**

El ecosistema ya distingue varias de estas cosas en sus documentos, pero la experiencia KAT-006 muestra que esa distinción no siempre gobierna los criterios de aceptación y la coordinación global. Una etapa puede quedar documentalmente completa mientras el objetivo de sistema permanece bloqueado. También puede ocurrir el error inverso: imponer Runtime a un encargo documental que no lo necesita.

Softly debe evitar ambos errores.

### Respuestas directas

**¿Qué puede impedir que Softly evolucione?**
- Criterios de aceptación que evalúan artefactos locales y no el resultado global.
- Handoffs persistidos sin mecanismo de recepción/activación verificable.
- Dependencias y estados declarativos sin validación de conjunto.
- Falta de autoridad/procedimiento para integrar resultados semánticamente incompatibles.
- Continuidad dependiente de checkpoints que pueden quedar desfasados.
- Sobrecarga de procedimientos universales no graduados por riesgo.
- Selección de agentes sin información suficiente sobre competencia demostrada y disponibilidad.
- Confundir el mismo nombre “Runtime” con artefacto experimental, motor task-centric e integración desplegada.

**¿Qué problemas estamos pasando por alto?**
- No existe un vocabulario común de niveles de capacidad: definido, ejecutable en sesión, integrado, automatizado y verificado.
- No basta con declarar un owner: hay que resolver identidad, disponibilidad, competencia, permisos y aceptación.
- Los schemas no garantizan referencias válidas, ausencia de ciclos ni transiciones correctas.
- La integración semántica no se obtiene por acumular commits.
- El costo real de cierre universal y doble revisión no está medido.
- La arquitectura no define un mecanismo completo para cancelar, replanificar, expirar, escalar y recuperar trabajo parcialmente ejecutado.
- La misma instancia puede producir y verificar su propia entrega, debilitando independencia en tareas de impacto alto.

**¿Qué reglas nos ayudan?**
- Autoridad final de gAto.
- No-herencia de competencias y permisos.
- Separación de Diseñado, probado, desplegado y operativo.
- Prohibición de inventar capacidades o verificaciones.
- Supuestos no críticos no bloqueantes.
- Handoffs con resultado, evidencia, siguiente acción y aceptación.
- Preservación de historia y trazabilidad.
- Inicio ligero y recuperación histórica bajo demanda.
- Investigación separada de implementación.

**¿Qué reglas podrían perjudicarnos?**
- Doble revisión integral universal para toda tarea, aunque sea trivial y reversible.
- Registro de incidencia exhaustivo sin criterio de materialidad.
- Requisitos repetidos en varios documentos sin fuente única o precedencia explícita.
- Exigir actualización de índices/checkpoints/bitácoras incluso cuando no hay cambio persistente relevante.
- Convertir cada mensaje en tarea o cada coordinación en aprobación central.
- Tratar taxonomía como sustituto de descubrimiento de competencias reales.

No se recomienda eliminar estas reglas por intuición. Se recomienda medir el costo y aplicar proporcionalidad.

**¿Qué dependencias son artificiales?**
- Runtime para investigar, redactar, crear agentes documentales o modificar GitHub con permisos.
- Scheduler para publicar un handoff que será tomado manualmente.
- Despliegue para declarar completo un paquete Diseñado.
- Runtime general para validar un conjunto de datos que podría comprobarse con un validador por lotes.
- Directorios/ceremonias obligatorios sin una dependencia real que los justifique.

**¿Qué capacidades faltan realmente?**
- Invocación/activación verificable cuando se espera ejecución por otro agente.
- Registro y validación de tareas/dependencias si se requiere orquestación task-centric.
- Integración semántica con autoridad y aceptación explícitas.
- Observabilidad de recepción, ejecución, bloqueo, entrega y aceptación.
- Descubrimiento de especialistas con evidencia de competencia y disponibilidad.
- Continuidad sincronizada entre instancias y estado persistido.

**¿Qué deberíamos corregir primero?**
1. Definir el contrato de aceptación global por objetivo.
2. Diferenciar los niveles de capacidad y los tipos de Runtime.
3. Hacer explícito quién integra resultados y resuelve incompatibilidades.
4. Acordar cómo se confirma recepción y activación de handoffs.
5. Validar referencias/ciclos/transiciones del modelo task-centric cuando sea requisito.
6. Medir la carga administrativa de cierre y auditoría antes de cambiar reglas universales.

**¿Qué decisiones corresponden exclusivamente a gAto?**
La definición de coordinación sistémica, distribución de autoridad, prioridades, aceptación de deuda, cambios normativos, nivel de autonomía, inversión en Runtime y autorización de pilotos/migraciones. Ninguna se toma en este informe.

## 2. Hallazgos finales

### F-01 — Brecha entre persistencia y activación
GitHub permite conservar instrucciones y resultados; no despierta sesiones ni garantiza recepción. Handoff listo no equivale a tarea ejecutada. Es un límite crítico para coordinación multiagente, no para producción documental de un solo agente.

### F-02 — El nombre Runtime es ambiguo
Existe Runtime Mini 0.2.0 en el repositorio, con código y seis pruebas declaradas. No se ejecutaron en esta investigación. El manifiesto solo autoriza crear archivos de texto. No se acredita despliegue, conexión a sesiones ni gestión task-centric. Por tanto, “no existe ningún Runtime” es impreciso; “no se acredita Runtime task-centric integrado/disponible” es correcto.

### F-03 — Task-centric es declarativo, no motor
Existe docs/architecture/task-centric-coordination.md y schemas/task.schema.json. El informe de etapa 1 reconoce que no se ejecutaron validación completa JSON Schema, validación DAG, detección de ciclos ni referencias huérfanas. El diseño no prueba ejecución.

### F-04 — Aceptación local puede ocultar fracaso global
KAT-006 evidenció que entregas documentales podían estar completas mientras el objetivo operativo no estaba habilitado. El dictamen inicial corregido por Audeline y el incidente AUD-20261116-018 muestran que una reserva textual no corrige una conclusión ejecutiva equivocada.

### F-05 — Integración semántica no resuelta
Eventos inmutables y commits preservan evidencia, pero no arbitran incompatibilidades. Se necesita autoridad integradora y criterio explícito de aceptación por resultado.

### F-06 — Sobrecarga procedimental potencial
Los protocolos universales de cierre e incidencias pueden aumentar trazabilidad, pero no existe medición de costo ni criterio graduado para tareas pequeñas, reversibles o de bajo riesgo. La carga excesiva puede producir cumplimiento nominal y demoras.

### F-07 — Continuidad vulnerable a estado desfasado
El checkpoint ligero reduce carga contextual, pero depende de actualización correcta y sincronización con commits, handoffs y tareas reales.

### F-08 — Taxonomía insuficiente para selección operativa
La no-herencia evita atribuir competencias injustificadas. No resuelve por sí sola quién está disponible, qué competencia ha demostrado, qué versión está activa ni quién tiene permisos efectivos.

### F-09 — Equivalencia funcional no demostrada
Un paquete portable no garantiza comportamiento equivalente entre modelos, contextos, herramientas y límites de sesión. Las pruebas propuestas en investigaciones anteriores siguen siendo propuestas, no resultados.

### F-10 — Coordinación sistémica abierta
La relación entre coordinación sistémica y orquestación sigue sin decisión. No debe resolverse por preferencia terminológica ni por consenso artificial.

## 3. Reglas: conservar, observar, revisar

| Regla/principio | Evaluación | Acción recomendada |
|---|---|---|
| Autoridad final humana | Fortaleza | Conservar |
| No-herencia de competencia/permisos | Fortaleza | Conservar |
| No inventar capacidad/verificación | Fortaleza | Conservar |
| Entrega documental sin Runtime universal | Fortaleza | Conservar |
| Handoff con criterio de aceptación | Fortaleza | Conservar y comprobar recepción cuando corresponda |
| Inicio ligero/checkpoint | Fortaleza con riesgo de desfase | Conservar; verificar sincronización |
| Doble revisión universal | Costo potencial | Medir y proponer proporcionalidad |
| Incidencia universal extensa | Costo potencial | Medir; mantener registro para incidentes materiales |
| Múltiples documentos con semántica repetida | Riesgo de deriva | Identificar fuentes canónicas y precedencia |
| Taxonomía como selector | Insuficiente por sí sola | Añadir evidencia/disponibilidad cuando se decida |

## 4. Recomendaciones priorizadas

### P0 — Evitar errores de aceptación global
Para cada encargo con varias etapas, definir antes de delegar:
- objetivo operativo final;
- entregables locales;
- dependencias críticas;
- condición de bloqueo;
- criterio de aceptación global;
- autoridad que integra y acepta.

Una entrega local no puede declarar terminado el proyecto si no satisface el objetivo final. Una capacidad no requerida no debe convertirse en bloqueo.

### P1 — Vocabulario común de capacidad
Adoptar como propuesta de análisis (no como cambio normativo todavía) los niveles: definido, ejecutable en sesión, integrado, automatizado y verificado. Nombrar el tipo concreto de Runtime: Mini, task-centric, servicio desplegado o integración de sesión.

### P1 — Contrato de activación
Cuando un handoff requiera que otro agente actúe, definir quién lo invoca, cómo se confirma recepción, cómo se rechaza, cómo se escala y cuándo se considera bloqueado. Para una publicación manual no exigir scheduler.

### P1 — Integración semántica
Asignar explícitamente responsable de integración para entregas múltiples. El integrador debe comparar resultados con el mandato y entre sí, documentar discrepancias y escalar decisiones fuera de su autoridad.

### P1 — Validación task-centric
Si se decide operar con tareas, validar:
- referencias a tareas existentes;
- ciclos y dependencias huérfanas;
- precondiciones de estado;
- owner/identidad y permisos;
- criterios de aceptación y evidencia;
- consistencia de estados de tarea y handoff.

No es necesario implementar un motor completo si un validador y un procedimiento bastan para el volumen actual.

### P2 — Proporcionalidad de auditoría y cierre
Medir tiempo/costo por clase de tarea, riesgo y reversibilidad. Comparar revisión integral doble con revisión escalonada. No reducir control para operaciones irreversibles o de alto impacto sin evidencia.

### P2 — Descubrimiento de especialistas
Si el tamaño del ecosistema lo justifica, mantener un registro verificable de dominio, competencias demostradas, versión, disponibilidad y permisos efectivos. No derivar por taxonomía solamente.

### P2 — Experimentos de transferencia
Ejecutar pruebas de reconstrucción fiel, equivalencia de acción, detección de vacíos y transferencia a caso nuevo entre instancias/modelos. Registrar repeticiones, calidad, tiempo, costo y fallos.

## 5. Plan de trabajo propuesto, no autorizado

1. **Contrato de aceptación global:** producir una propuesta documental pequeña para encargos multi-etapa.
2. **Mapa de capacidades:** inventariar capacidades por nivel, sin asumir que un artefacto está desplegado.
3. **Piloto task-centric:** solo si gAto lo autoriza; usar un proyecto acotado y medir antes de migrar.
4. **Prueba de activación:** comparar handoff manual y mecanismo real de invocación.
5. **Prueba de proporcionalidad:** comparar cierre actual con control escalonado.
6. **Decisión de arquitectura:** revisar resultados y recién entonces decidir cambios de schemas, contratos, moldes o Runtime.

No se implementa ninguno de estos pasos sin autorización.

## 6. Contraste independiente

- **Audeline:** la misión AUD-SOFTLY-INTEGRITY-2026-001 no está persistida ni acreditada en el árbol de Auditoria al corte. Sus informes KAT-006 016–018 sí están disponibles. Coinciden en separar documento y operación y en exigir que la aceptación refleje el objetivo global. Su NO-GO operacional aplica a KAT-006, no a toda actividad de Softly.
- **Katarina:** su investigación de coordinación universal y rediseño coincide en task-centric, handoffs no activos, semántica compartida y postergar Runtime general hasta demostrar necesidad. Difiere en cómo conceptualiza coordinación sistémica. Su informe es antecedente relacionado, no una auditoría idéntica.
- **Consenso:** no se fuerza. La diferencia entre postergar Runtime como inversión general y reconocer Runtime como bloqueo de un proyecto que lo exige es una distinción de alcance, no una contradicción.

El registro detallado de evidencias y contrastes está en:
Softlysay/entregable/2026-11-16-registro-evidencia-y-contrastes-softly-audeline-katarina.md

El diagnóstico funcional y la matriz de dependencias están en:
Softlysay/entregable/2026-11-16-diagnostico-capacidad-y-matriz-dependencias-softly.md

La investigación preliminar independiente, preservada antes de los contrastes, permanece intacta:
Softlysay/entregable/2026-11-16-investigacion-preliminar-trabas-futuras-softly.md

## 7. Decisiones reservadas a gAto

1. Resolver coordinación sistémica y su relación con orquestación.
2. Determinar si el objetivo de Softly exige Runtime task-centric y qué alcance debe tener.
3. Autorizar o rechazar un piloto task-centric.
4. Aprobar cualquier cambio en SOFTLY.md, CHECKPOINT.md, README, contratos, taxonomías, schemas y moldes.
5. Definir nivel de autonomía, activación y acciones externas permitidas.
6. Aceptar deuda técnica y prioridades de roadmap.
7. Autorizar migraciones, retiro de agentes o cambios de estructura.
8. Determinar qué riesgos requieren auditoría independiente obligatoria.

## 8. Estado de entrega y verificación

La investigación preliminar fue persistida y releída desde GitHub. Se crearon además:
- diagnóstico de capacidad y matriz de dependencias;
- registro de evidencia y contrastes;
- este informe final consolidado.

La misión específica de Audeline sigue pendiente/no acreditada. La investigación de Katarina disponible se contrastó como antecedente relacionado. No se inventa que Audeline haya terminado ni que exista una investigación nueva de Katarina con este ID.

No se modificaron:
- SOFTLY.md
- CHECKPOINT.md
- README.md
- contratos
- taxonomías
- schemas normativos
- Runtime
- paquetes de agentes

No se ejecutaron pruebas de Runtime ni pruebas task-centric. No se implementaron recomendaciones.

**Conclusión final:** Softly puede seguir investigando, creando documentos, produciendo agentes diseñados y trabajando en GitHub sin Runtime task-centric. Lo que no puede prometer honestamente sin mecanismos adicionales es activación autónoma, ejecución persistente de dependencias y coordinación task-centric automatizada. El riesgo mayor es no distinguir esos límites al definir y aceptar un objetivo.

**Softly deja constancia de que la investigación propia está terminada y queda disponible para responder preguntas de gAto.** La auditoría específica de Audeline permanece pendiente/no acreditada en GitHub; no impide cerrar el análisis independiente propio ni convierte la misión en un cierre de auditoría conjunta.

---

**Fin del informe SOFTLY-FUTURE-BLOCKERS-2026-001.**
