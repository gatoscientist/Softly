# Registro de evidencia y contrastes — SOFTLY-FUTURE-BLOCKERS-2026-001

**Fecha:** 2026-11-16  
**Emite:** Softly  
**Estado:** evidencia propia preservada; contraste con antecedentes disponibles; auditoría específica de Audeline pendiente/no acreditada  
**Corte Softly:** main, commit a2bc038bd6bf14fa67c244b2c0e0ff1cd29c8bc9  
**Corte Auditoria:** main, commit 41070d7fc9da73f2f7559d82427045398b6810ae  
**Corte Katarina:** main, investigación comparativa existente consultada.

## 1. Procedencia y límites

La investigación preliminar de Softly fue creada y releída desde GitHub antes de abrir los dictámenes KAT-006 de Audeline y el informe comparativo de Katarina. Por tanto, los hallazgos H-01 a H-10 de la versión preliminar se conservaron sin incorporar conclusiones ajenas.

La misión actual solicitada a Audeline, identificador AUD-SOFTLY-INTEGRITY-2026-001, no aparece en el árbol recursivo de gatoscientist/Auditoria al corte. Tampoco aparece un informe con ese ID en Audeline/reports. Esto acredita ausencia de entrega persistida en el repositorio; no permite afirmar si existe trabajo no guardado en otra sesión.

La investigación de Katarina consultada sí existe, pero su alcance es coordinación universal y rediseño arquitectónico en seis repositorios. Es un antecedente directamente relacionado, no una auditoría idéntica a SOFTLY-FUTURE-BLOCKERS-2026-001.

## 2. Registro de evidencia propia

| ID | Evidencia observada | Fuente | Qué acredita | Qué no acredita |
|---|---|---|---|---|
| E-01 | Sustrato Prompting + Contratos + GitHub; Runtime no es requisito universal | SOFTLY.md, README.md | Norma vigente del sistema | Que todas las capacidades estén integradas |
| E-02 | Handoff publicado no despierta sesión sin invocador conectado | SOFTLY.md §6, agents/templates/handoff.md | Límite explícito de coordinación documental | Que nunca exista invocación externa |
| E-03 | Molde y checklist separan Diseñado de probado/desplegado | agent-generation-mold.md, agent-delivery-checklist.md | Criterio de entrega documental | Que el paquete funcione como servicio |
| E-04 | No-herencia por defecto; taxonomía no demuestra competencia | taxonomy-and-mold-validation.md | Control contra atribución indebida | Que exista un directorio vivo de disponibilidad |
| E-05 | Modelo task-centric y schema presentes | docs/architecture/task-centric-coordination.md, schemas/task.schema.json | Diseño declarativo de tareas | Motor, validador de grafo o ejecución automática |
| E-06 | Informe KAT-006 etapa 1 declara pendientes de validador DAG, referencias y runtime | Katarinasay/reports/KAT-006-ETAPA-1-IMPLEMENTACION-2026-11-16.md | Estado y límites declarados por el informe | Pruebas de funcionamiento no ejecutadas |
| E-07 | Runtime Mini 0.2.0, manifiesto, código y seis pruebas declaradas | softly-runtime/manifest.json, runtime.py, test_runtime.py | Existe artefacto experimental acotado | Despliegue, integración o ejecución de pruebas en este encargo |
| E-08 | Eventos JSONL vacío en el árbol inspeccionado | softly-runtime/events.jsonl | No hay eventos persistidos en ese archivo en el corte | Que no existan eventos en otro entorno |
| E-09 | Revisión cruzada identifica integración semántica como problema abierto | Softlysay/entregable/2026-11-16-revision-cruzada-softly-arquitectura-minimalista.md | Reconocimiento previo del problema | Que exista autoridad/procedimiento ya resuelto |
| E-10 | CHECKPOINT conserva pregunta sistémica abierta | CHECKPOINT.md, informe KAT-006 | Estado de la pregunta y tres interpretaciones | Resolución aprobada |
| E-11 | Entregable preliminar creado y releído | Softlysay/entregable/2026-11-16-investigacion-preliminar-trabas-futuras-softly.md | Preservación de hallazgos independientes | Cierre de investigación final |

## 3. Contraste con Audeline

### 3.1 Estado de la misión solicitada

La inspección recursiva del árbol de gatoscientist/Auditoria devolvió truncated=false. En Audeline/reports aparecen los informes 016, 017 y 018 de KAT-006, pero no el ID AUD-SOFTLY-INTEGRITY-2026-001. El último commit de Auditoría al corte es:

41070d7fc9da73f2f7559d82427045398b6810ae — “Audeline: registrar incidente grave de coordinación y concepción KAT-006”.

**Estado de la auditoría específica:** no terminada/no acreditada en GitHub. No se presume actividad no persistida ni se declara que Audeline esté inactiva.

### 3.2 Antecedentes KAT-006 disponibles

- AUD-20261116-016: NO-GO ACOTADO para aceptación integral KAT-006 al corte de su auditoría.
- AUD-20261116-017 corregido: NO-GO OPERACIONAL para KAT-006, al reconocer que el objetivo operativo requería runtime task-centric.
- AUD-20261116-018: registra como GRAVE el error de coordinación y concepción que confundió completitud documental con habilitación operativa.

### 3.3 Coincidencias con Softly

1. Documentación y capacidad ejecutable son planos distintos.
2. Un schema no es un motor de ejecución ni validador.
3. Handoffs/documentos no acreditan activación.
4. La ausencia de Runtime task-centric es bloqueante cuando el objetivo es precisamente operar tareas, dependencias y estados mediante ese runtime.
5. La aceptación debe responder al objetivo global, no solo a la presencia de archivos.
6. La integración debe conservar evidencia y diferenciar deuda, bloqueo y decisión humana.

### 3.4 Diferencias y matices

**Diferencia de alcance:** los informes 016–018 evalúan KAT-006 y su objetivo operativo específico. La presente misión evalúa qué puede impedir la evolución general de Softly. Un requisito bloqueante para KAT-006 no se convierte automáticamente en requisito para toda investigación, entrega documental o actividad GitHub.

**Runtime Mini:** la auditoría 017 afirma que no existe runtime task-centric. La revisión estática de Softly confirma que el repositorio contiene Runtime Mini 0.2.0, pero no un motor task-centric acreditado. No hay contradicción si se nombran correctamente ambos objetos. La frase general “no existe ningún Runtime” sería imprecisa frente al árbol actual; “no existe Runtime task-centric integrado/disponible acreditado” es más exacta.

**Aceptación:** la lección de Audeline sobre no declarar aceptación funcional sin la capacidad central requerida es correcta. También debe evitarse el error inverso: exigir capacidad runtime para un objetivo que solo solicita un artefacto documental.

### 3.5 Evaluación de la auditoría como sistema

El incidente AUD-20261116-018 es evidencia directa de un riesgo sistémico: los entregables locales pueden estar correctos mientras el objetivo de conjunto no está habilitado. El error no fue solo de redacción; falló el criterio de aceptación global y la integración del conocimiento de una dependencia crítica.

La presente investigación añade que el sistema necesita registrar la relación entre objetivo, resultado operativo, dependencias críticas y evidencia de aceptación antes de cerrar localmente cada etapa.

## 4. Contraste con Katarina

### 4.1 Fuente y alcance

Se consultó en gatoscientist/Katarina el informe “Investigación independiente de Katarina y comparación final con Softly”, archivo:

shared/2026-11-16-investigacion-coordinacion-katarina-comparacion-softly.md

El informe declara estado entregado/archivado, análisis independiente y comparación con la investigación previa de Softly. Su alcance es coordinación universal, estructuras de colaboración y seis repositorios. No es una investigación con el mismo ID ni una auditoría específica de las futuras trabas de Softly.

### 4.2 Coincidencias

- Tarea y dependencias como unidad de coordinación.
- Separar comunicación, coordinación y persistencia.
- No confundir canal o handoff con transporte/activación.
- No interpretar publicación, lectura o silencio como aceptación.
- Evitar más agentes y mensajes cuando el trabajo no presenta dependencias reales.
- Mantener GitHub como coordinación documental mientras no se demuestre que la activación manual es cuello de botella.
- Probar alternativas antes de migrar contratos o directorios.
- Diferenciar competencia universal de autocoordinación y coordinación directiva según rol.

### 4.3 Diferencias

- Katarina conserva cuatro dimensiones funcionales: autocoordinación, pares, coordinación directiva y coordinación sistémica. Softly mantiene tres dimensiones normativas en el diseño actual y la pregunta sistémica abierta.
- Katarina favorece una transición task-centric mediante piloto medido y no una reescritura inmediata. Softly coincide, pero identifica que la aceptación de un objetivo task-centric operacional específico puede quedar bloqueada si el runtime requerido no existe.
- Katarina enfatiza la semántica compartida entre tareas, mensajes, eventos, artifacts y workspaces. Softly añade mayor foco en estados de capacidad, activación y criterios de aceptación global.
- La investigación de Katarina no demuestra mediante experimento que la Alternativa B sea superior en el ecosistema real; reconoce que no ejecutó pruebas ni mediciones.

### 4.4 Interpretación

No existe contradicción necesaria entre “postergar Runtime como inversión arquitectónica general” y “Runtime task-centric bloquea un proyecto cuyo resultado operativo exige ese motor”. La primera es una recomendación de roadmap; la segunda es una condición de aceptación para un objetivo específico.

La decisión correcta depende del resultado solicitado y del alcance autorizado, no de una regla universal pro- o anti-Runtime.

## 5. Tabla de convergencia y diferencias

| Tema | Softly actual | Audeline KAT-006 | Katarina | Resultado |
|---|---|---|---|---|
| Documentación vs operación | Distinción explícita | Bloqueo si objetivo operativo no existe | Distinción explícita | Coincidencia fuerte |
| Handoff vs activación | No despierta sesión | No equivale a ejecución | No equivale a recepción | Coincidencia fuerte |
| Runtime universal | No requerido | Runtime task-centric bloquea KAT-006 | Postergar runtime general | Complementario, no contradictorio |
| Task-centric | Schema/modelo declarativo | Faltan mecanismos operativos para KAT-006 | Alternativa B mediante piloto | Coincidencia con diferencia de fase |
| Coordinación sistémica | Abierta | Abierta | Posible responsabilidad especializada | Diferencia conceptual preservada |
| Aceptación | Criterios declarativos | Criterio global debe reflejar objetivo | Aceptación separada de entrega | Coincidencia |
| Integración semántica | Riesgo identificado | Falló integración del objetivo | Falta semántica común | Coincidencia |
| Proporcionalidad | Riesgo de burocracia | Scope gate y severidad proporcional | Evitar coordinación innecesaria | Coincidencia |
| Validación | Schemas sin enforcement general acreditado | DAG/estados pendientes | Validación y experimentos propuestos | Coincidencia |

## 6. Hallazgos adicionales de esta investigación

1. **Brecha de niveles de capacidad:** el sistema carece de un vocabulario operativo común para distinguir definido, ejecutable en sesión, integrado, automatizado y verificado.
2. **Runtime ambiguo:** se usa “Runtime” para referirse a artefacto Mini, motor task-centric, servicio desplegado o disponibilidad de una sesión. Debe nombrarse el objeto concreto.
3. **Integración semántica:** commits y archivos pueden estar correctos sin que el resultado satisfaga el objetivo completo.
4. **Cierre proporcional:** el doble control universal puede resultar costoso en tareas triviales; se necesita evidencia de costo antes de recomendar cambios.
5. **Descubrimiento de especialistas:** taxonomía y no-herencia son buenas reglas, pero no bastan para conocer competencia demostrada, disponibilidad y versión activa.
6. **Continuidad:** un checkpoint ligero reduce contexto, pero si no se sincroniza con la actividad real puede propagar un estado obsoleto.
7. **Riesgo de autocertificación:** productor y verificador pueden ser la misma instancia; la independencia debe graduarse según impacto y reversibilidad.

## 7. Qué no se puede concluir

- No se puede concluir que Audeline haya terminado la misión AUD-SOFTLY-INTEGRITY-2026-001.
- No se puede concluir que Audeline no esté trabajando en una sesión no persistida.
- No se puede concluir que Runtime Mini pase sus seis pruebas: no se ejecutaron.
- No se puede concluir que Runtime Mini esté desplegado o conectado.
- No se puede concluir que Katarina haya ejecutado una prueba task-centric.
- No se puede concluir que la Alternativa B sea superior sin piloto.
- No se puede resolver la coordinación sistémica por consenso entre informes.
- No se puede inferir que Runtime sea necesario para todas las capacidades de Softly.

## 8. Conclusión del contraste

La coincidencia central de los tres cuerpos de trabajo disponibles es que Softly necesita separar definición, coordinación, ejecución y aceptación. La principal diferencia está en el alcance y el momento: Katarina recomienda un piloto antes de inversión runtime; Audeline exige runtime para aceptar funcionalmente KAT-006 porque ese es su objetivo operativo; Softly concluye que la dependencia debe evaluarse por tarea y no universalizarse.

La auditoría específica de Audeline para esta misión permanece pendiente/no acreditada. La investigación previa de Katarina sirve como contraste parcial y relevante, no como sustituto de una auditoría nueva.

## 9. Referencias y SHAs de corte

### Softly
- SOFTLY.md blob: ed10002b6b70bc03302fcecec6e73e39ec7914ea
- CHECKPOINT.md blob: b3526db8367d1592500950e493b9c68d46c35350
- README.md blob: 8e892af15353f450b5e2c627f87c14a3eb56b925
- Investigación preliminar commit: a2bc038bd6bf14fa67c244b2c0e0ff1cd29c8bc9
- Investigación preliminar blob tras relectura: bea2c4d1c03b0177f315feca88338af178ca1c83
- Runtime Mini manifest blob: 5ccf4e2969c0c548c8b755ed31a8822987e00880
- Runtime Mini code blob: 77eac417b7a2b5a612b33803069997b13fe8bb61
- Runtime Mini tests blob: 3bc068907c7c2e5d061b90dbc9bdd35344fe7b7c

### Auditoria
- HEAD al corte: 41070d7fc9da73f2f7559d82427045398b6810ae
- AUD-20261116-016: 398f7e7c3d580107e09aa804da9ed54f30819806
- AUD-20261116-017: 393610af38227050a21b678835bfd13445ed84c9
- AUD-20261116-018: 0346f0c0bb30687b53995806782402251c68ec64

### Katarina
- Informe comparativo independiente: shared/2026-11-16-investigacion-coordinacion-katarina-comparacion-softly.md
- La investigación es antecedente relacionado, no auditoría idéntica a la presente misión.

---

**Estado:** contraste parcial completado con antecedentes persistidos. Pendiente: auditoría específica de Audeline y eventual nueva investigación específica de Katarina, si se emiten y persisten. No se fuerza consenso ni se modifica normativa.
