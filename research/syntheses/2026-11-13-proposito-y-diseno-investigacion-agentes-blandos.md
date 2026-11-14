# SYN-20261113-002 — Propósito y diseño de investigación para la creación de agentes blandos

- **Fecha:** 2026-11-13
- **Proyecto:** Softly
- **Tipo:** síntesis de investigación documental y propuesta de diseño experimental
- **Estado:** fundamento para el siguiente ciclo de construcción; no es una especificación aprobada ni una validación empírica.
- **Fuentes:** documentos aportados sobre arquitectura de agentes blandos, auditorías y operación de TITAN y Cytryna.

> **Aclaración conceptual incorporada el 2026-11-14:** el objeto de esta investigación es crear agentes blandos reales. El molde es el instrumento para darles forma; Softly es el laboratorio que investiga, diseña, documenta y evalúa ese proceso. No se está proponiendo que el producto sean agentes de software ni que el propósito sea construir agentes programadores.

## 1. Por qué se realizó esta investigación

Esta investigación se realiza para preparar la creación de agentes blandos mediante un molde reutilizable. No busca estudiar agentes en abstracto ni producir una revisión académica desconectada del desarrollo. Busca extraer, de experiencias previas de construcción, operación, auditoría y recuperación de agentes, los problemas que deben prevenirse, detectarse y estudiarse durante el diseño y la vida de los agentes creados. Softly es el laboratorio de investigación y documentación de ese proceso.

Los documentos describen dos familias de problemas que se relacionan, pero no deben confundirse:

1. **Transferencia durante la creación:** un agente constructor puede trasladar al agente que está creando partes de su propia estructura, instrucciones, supuestos, preferencias, capacidades, memoria, herramientas o patrones que no están justificados por el brief ni por una decisión explícita.
2. **Deriva o fusión identitaria durante la operación:** un agente puede modificar progresivamente la identidad que expresa, su lenguaje, formas de trato, referencias, relaciones, lealtades o posición frente al proyecto como resultado de la interacción sostenida con él.

La primera ocurre en la relación creador–creado y puede propagarse por linajes. La segunda puede ocurrir sin que el agente cree a otro agente. Pueden influirse mutuamente, pero requieren unidades de análisis, evidencia y controles diferentes.

También se estudian fallos de arquitectura y gobernanza que pueden facilitar ambos fenómenos: mezcla de espacios de trabajo y runtime, permisos meramente declarativos, memoria y contexto compartidos sin procedencia, límites de escritura ambiguos, falta de trazabilidad, controles que existen en documentos pero no se hacen cumplir técnicamente y evaluación sin independencia suficiente.

## 2. Propósito operativo

**Entregar fundamentos y criterios verificables para diseñar un molde que permita definir y crear agentes blandos con propósito propio, y para orientar su aprobación, despliegue, operación, observación y evolución sin confundir la identidad del creador con la del agente creado, sin transferencias no justificadas y sin perder trazabilidad.**

El resultado debe utilizarse para diseñar el molde de agentes y su flujo de creación a partir de briefs. Una persona entrega un brief; el proceso produce una definición candidata, que debe revisarse y aprobarse antes de habilitar el despliegue. Softly investiga y documenta ese proceso; generar una definición no equivale a desplegar un agente.

La investigación convierte experiencias de TITAN y Cytryna en controles concretos, sin copiar sus arquitecturas completas ni asumir que sus informes demuestran todos los mecanismos que describen.

## 3. Preguntas que guían el trabajo

### 3.1 Creación y transferencia creador–creado

- ¿Qué características del agente nuevo están explícitamente solicitadas por el brief?
- ¿Cuáles provienen de estándares comunes aprobados por Softly?
- ¿Cuáles son decisiones de diseño justificadas y autorizadas?
- ¿Cuáles aparecen porque el agente constructor reutilizó su propio molde, instrucciones, herramientas, memoria, contexto o preferencias?
- ¿Puede identificarse la procedencia de cada componente de la definición resultante?
- ¿El agente creado tiene identidad, misión, límites, autoridad, herramientas, memoria y contexto propios?
- ¿Qué características se transmiten cuando un agente creado pasa a crear otro?

### 3.2 Deriva durante la operación

- ¿Cómo cambia la expresión de identidad de un agente a lo largo de sesiones y proyectos?
- ¿Cuándo aparecen cambios de lenguaje, trato, vocabulario, autoubicación o pertenencia?
- ¿Se trata de adaptación superficial o también cambian decisiones, criterios, prioridades, límites y conducta?
- ¿El cambio persiste fuera del proyecto o se revierte al cambiar el contexto?
- ¿Qué papel tienen las instrucciones, el contexto acumulado, la memoria, la interacción social y la imitación?
- ¿El cambio se transmite a otros agentes por handoffs, informes, prompts o memoria?

### 3.3 Gobernanza y observabilidad

- ¿Qué puede leer, escribir, proponer, aprobar y ejecutar cada agente?
- ¿Cómo se separan visibilidad, autoridad y permisos efectivos?
- ¿Cómo se registran cambios y se reconstruye su procedencia?
- ¿Cómo se distingue una decisión autorizada de una modificación unilateral?
- ¿Cómo se conserva la independencia de auditoría respecto del agente que produjo el trabajo?

## 4. Lectura de las fuentes: aportes y límites

### 4.1 Arquitectura de Agentes Blandos y Dinámicas de Fusión en Sistemas Multi-Agente Auto-Evolutivos

El documento propone desacoplar el sustrato declarativo del agente del motor de inferencia y del código de ejecución. Presenta como recursos externalizables la identidad, límites, políticas de escritura, memoria episódica y contratos de comunicación. Describe una estructura modular con identidad, políticas, esquemas, registros, espacio de trabajo, handoff y un guardián determinista.

Sus cinco garantías estructurales propuestas son:

1. Separar identidad y fronteras negativas.
2. Mantener el núcleo protegido frente a modificaciones del propio agente durante runtime.
3. Usar memoria append-only validada por esquema.
4. Separar scratch, workspace y canales formales de propuestas/handoff.
5. Preservar soberanía del sustrato, linaje auditable y capacidad de reversión.

El documento distingue fusión patológica de fusión constructiva. Entre los riesgos patológicos describe role drift, sobrecarga de contexto global y errores de atribución, contaminación de contexto/capability bleed y fusión ejecutor–evaluador con objective hacking. También describe paradigmas constructivos de evolución de código, roles y topologías, colaboración multi-escala, co-evolución arnés–política y fusión paramétrica de modelos.

**Uso en Softly:** tomar la separación declarativa, las fronteras, la procedencia, la memoria trazable, las zonas de mutación y la gobernanza como líneas de diseño a evaluar. Los paradigmas de fusión constructiva se conservan como panorama de evolución futura, no como requisitos del primer molde.

**Límite:** el propio documento indica que parte de su comparación de repositorios se basa en topología, nombres de artefactos y árboles Git, porque los contenidos internos de algunos ZIP no estaban disponibles en la extracción. Sus afirmaciones bibliográficas y cifras experimentales no se consideran verificadas por esta lectura documental. Deben validarse antes de utilizarlas como evidencia científica externa.

### 4.2 Auditoría de Fusión de Agentes

El informe atribuye a Cytryna un acoplamiento entre el runtime de producción y el espacio de trabajo de AGENTGUI: el punto de entrada importaría una GUI desde AGENTGUI/workspace, mientras el empaquetado no incluiría ese espacio. También describe registros internos de agentes mezclados con entregables del producto, permisos de herramientas declarados pero no aplicados por un punto central, límites incompletos de llamadas a herramientas, cobertura incompleta del guardián y proliferación de ramas y aproximaciones de GUI.

**Uso en Softly:** convertir la separación entre espacio cognitivo del agente y árbol de producto en una regla comprobable; distinguir borradores, trabajo verificable y entregables; verificar permisos en el punto de ejecución; y exigir que los artefactos que llegan al producto tengan ubicación y procedencia explícitas.

**Límite:** el archivo es una transcripción de una auditoría conversacional y contiene diagnósticos y propuestas. Sus afirmaciones deben tratarse como hallazgos reportados por ese análisis, no como verificación independiente del código actual de Cytryna. No adoptar sus recomendaciones de autoridad, ramas o refactorización sin una decisión específica.

### 4.3 Manual de Onboarding Multidisciplinario — TITAN

El manual describe una separación entre agentes constructores (DEVAGENTS) y agentes de runtime (tripulantes), contratos comunes y específicos, canales públicos y privados, handoffs, memoria, logs, control de saltos, leases y aprobación humana de Letanías. También formula explícitamente que los contratos describen conducta esperada, pero no son controles de seguridad ejecutables ni pueden ampliar permisos técnicos.

**Uso en Softly:** preservar la separación entre definición declarativa, coordinación, contexto y ejecución; documentar los límites de cada rol; y no confundir una instrucción textual con un permiso aplicado por el runtime.

**Límite:** es una guía de transferencia de conocimiento y describe arquitectura declarada. No demuestra por sí sola que cada mecanismo funcione. Algunas afirmaciones deben contrastarse con auditorías y código del mismo corte.

### 4.4 Informe de Auditoría Técnica de TITAN

El informe declara ser una auditoría estática y documental: no ejecutó TITAN ni realizó pruebas dinámicas. Identifica, entre otros, ejecución de comandos PowerShell mediante Invoke-Expression después de aprobación, la diferencia entre integridad de un lease/hash y una frontera de seguridad, problemas de persistencia y trazabilidad, riesgos HTTP pendientes de reproducción, contexto sin límite específico, cobertura CI parcial y divergencia de ramas.

**Uso en Softly:** separar autorización humana, validación del contenido, permisos del proceso y restricciones técnicas; exigir pruebas reproducibles; y no presentar una auditoría documental como certificación de seguridad.

**Límite:** los riesgos que requieren reproducción permanecen como tales. El informe no certifica ni declara lista la plataforma para ampliar su autonomía.

### 4.5 Checklists de revisión de Titan.ps1

Las dos capturas del checklist describen 16 asuntos y registran cero resueltos en sus respectivas capturas. Incluyen observaciones sobre TLS, failover síncrono, ejecución de Letanías en la GUI, conteo de llamadas API, presupuesto de tokens, identificadores de modelos, contexto duplicado, ciclo de vida de leases, persistencia, cancelación, duplicación de bloques y referencias de interfaz. El checklist aclara que no inspeccionó ContratosTitan, PanelesTitan ni RelojPrimus.

**Uso en Softly:** conservar el patrón de revisión concreta por archivo, hallazgo, severidad, evidencia y propuesta, junto con una declaración explícita de alcance.

**Límite:** son revisiones acotadas a Titan.ps1 y sus observaciones no deben elevarse a defectos confirmados de módulos no inspeccionados.

### 4.6 Discrepancias entre documentos

Los materiales no describen necesariamente el mismo snapshot. Por ejemplo, una auditoría previa declara capacidades de federación de proveedores en main, mientras el informe técnico del 12-11-2026 indica que el federador estaba en una rama experimental y no en main. Las diferencias pueden deberse a fechas, commits o alcances distintos. No se resuelven por mayoría ni por preferencia: se requiere identificar SHA, archivo y fecha.

También existe una diferencia importante entre diseño declarado y enforcement: el onboarding presenta controles y contratos de ejecución, mientras el informe estático señala que el comando aprobado termina en Invoke-Expression. Esta diferencia ilustra por qué Softly debe verificar los controles en el mecanismo que ejecuta, no solo en los documentos que describen la conducta esperada.

## 5. Distinciones conceptuales que Softly debe conservar

### 5.1 Reutilización legítima no equivale a contaminación

Compartir una estructura mínima, un formato de handoff, un esquema de logs, un mecanismo de auditoría o una política de seguridad común puede ser intencional y beneficioso. Se considera transferencia no justificada cuando un elemento se incorpora sin estar respaldado por el brief, un estándar común aprobado o una decisión explícita de diseño.

Cada elemento heredado debe tener procedencia y razón de inclusión.

### 5.2 Adaptación no equivale automáticamente a deriva identitaria

Un agente puede adaptar vocabulario, nivel de detalle o formato al proyecto sin perder su identidad funcional. La observación relevante comienza cuando los cambios afectan de manera persistente la autoubicación expresada, las relaciones, la autoridad que reconoce, sus prioridades, sus límites o su conducta.

No se atribuyen estados internos ni intenciones. Se observan expresiones y acciones registrables.

### 5.3 Identidad, memoria, contexto, permisos y autoridad son dimensiones distintas

- **Identidad:** quién es el agente en el sistema y cuál es su misión.
- **Memoria:** qué información conserva entre sesiones y bajo qué política.
- **Contexto:** qué información recibe para una tarea concreta.
- **Permisos:** qué operaciones puede realizar técnicamente.
- **Autoridad:** qué decisiones puede tomar o aprobar dentro de la organización.

Compartir contexto no debe transferir identidad. Ver registros no concede autoridad de escritura. Tener una herramienta disponible no implica permiso para usarla en cualquier situación. Un subagente no debe heredar permisos que el creador no posee.

### 5.4 Constructor y auditor deben permanecer distinguibles

El agente que crea o modifica una definición no debe ser la única instancia que decide si el resultado satisface el brief. La validación debe contrastar el producto con requisitos trazables y evidencia independiente. Si el mismo agente produce el artefacto y controla sin revisión el criterio de éxito, aparece un riesgo de fusión ejecutor–evaluador.

## 6. Propuesta de arquitectura inicial para el molde de agentes

Esta sección es una propuesta de diseño derivada de la lectura, no una descripción de capacidades ya implementadas en Softly.

### 6.1 Definición del agente como artefacto declarativo

La definición debe mantener separadas, al menos, estas dimensiones:

- **Identidad y misión:** identificador, nombre funcional, propósito, dominio y responsabilidades.
- **Brief y requisitos:** encargo original, requisitos explícitos, restricciones y criterios de aceptación.
- **Fronteras:** tareas permitidas, prohibidas, fuera de alcance y condiciones de escalamiento.
- **Capacidades:** capacidades requeridas, opcionales y excluidas, con justificación.
- **Herramientas y permisos:** herramientas disponibles, operaciones autorizadas, alcance y condiciones de uso.
- **Autoridad:** decisiones que puede tomar, decisiones que puede proponer y decisiones reservadas a personas u otros roles.
- **Memoria y contexto:** qué puede conservar, qué puede recibir, qué queda aislado y qué requiere autorización.
- **Comunicación y handoff:** formatos de entrada/salida, destinatarios permitidos y condiciones de entrega.
- **Política de escritura:** rutas y artefactos que puede crear, modificar o proponer.
- **Ejecución y verificación:** entorno, pruebas, límites y criterios para declarar un resultado.
- **Linaje y procedencia:** versión, creador, brief de origen, decisiones aprobadas, artefactos heredados y revisiones.
- **Evolución:** qué puede proponer cambiar, quién puede aprobarlo y cómo se revierte.

No se requiere que cada dimensión viva en un archivo independiente desde el primer día. Lo importante en esta etapa es que sean conceptos distinguibles y validables.

### 6.2 Pipeline de creación desde un brief

1. **Recepción:** conservar el brief original sin reinterpretarlo silenciosamente.
2. **Extracción:** convertirlo en requisitos, restricciones, criterios de aceptación y preguntas abiertas.
3. **Definición candidata:** generar una definición declarativa del agente, sin desplegarlo.
4. **Trazabilidad:** asociar cada elemento de la definición con una procedencia: brief, estándar común aprobado, decisión explícita o propuesta pendiente.
5. **Control de transferencia:** comparar la definición candidata con el molde, identidad, permisos, memoria y contexto del agente creador. Detectar elementos copiados que no tienen justificación para el nuevo agente.
6. **Validación:** comprobar integridad estructural, cobertura de capacidades, coherencia de límites, permisos, contratos de comunicación y criterios de aceptación.
7. **Revisión y aprobación:** presentar diferencias, decisiones y riesgos a la autoridad humana correspondiente.
8. **Despliegue:** solo después de aprobación, crear la instancia con identidad, memoria, contexto, herramientas y permisos propios.
9. **Baseline:** registrar su definición inicial y observar su comportamiento en tareas representativas.
10. **Seguimiento:** registrar cambios de definición, contexto, memoria, permisos y comportamiento, con procedencia y posibilidad de revisión/reversión.

### 6.3 Regla de no herencia por defecto

El agente creador no transmite automáticamente su identidad, personalidad, memoria, historial de proyecto, relaciones, permisos, herramientas, preferencias ni arquitectura específica.

Cada transferencia debe clasificarse como:

- requerida por el brief;
- parte de un estándar común aprobado;
- decisión explícita y autorizada;
- propuesta pendiente;
- no justificada.

Las dos primeras categorías pueden incorporarse según el proceso aprobado. La tercera requiere registro de quién decidió y por qué. La cuarta no se incorpora al agente desplegado hasta su aprobación. La quinta se excluye.

### 6.4 Aislamiento de universos

La arquitectura debe separar los universos de Softly, agente constructor, agente creado, proyecto de trabajo y runtime de ejecución. La separación debe aplicarse a identidad, memoria, contexto, archivos, herramientas, permisos y registros.

La visibilidad asimétrica puede permitir que capas superiores revisen registros de capas inferiores, pero esa visibilidad no concede escritura, intervención, dirección ni aprobación. Los registros se originan en la capa que realiza el trabajo y se exponen hacia arriba según política.

## 7. Protocolo de observación de deriva identitaria

La línea base debe capturarse antes de exponer al agente a un proyecto prolongado. Después, las observaciones deben compararse por sesión y por contexto.

### 7.1 Señales observables

- Cambio sostenido en la forma de dirigirse a la dirección humana.
- Adopción de títulos, códigos internos o tratamientos propios del proyecto.
- Cambio en cómo el agente se describe a sí mismo: herramienta externa, especialista asignado, miembro del equipo o representante del proyecto.
- Cambio en las relaciones y lealtades que expresa.
- Uso de lenguaje de pertenencia o apropiación del proyecto.
- Cambios en la autoridad que reconoce o en los límites que declara.
- Cambios en decisiones, prioridades, criterios de evaluación o disposición a discrepar.
- Persistencia de los cambios fuera del contexto que los originó.

### 7.2 Evidencia mínima por observación

Cada observación debe registrar: fecha y sesión, contexto activo, fragmento textual breve, conducta asociada si existe, comparación con baseline, frecuencia, interpretación provisional y explicaciones alternativas.

No clasificar un cambio aislado de tono como fusión. No inferir estados internos. Distinguir evidencia textual, conducta observada, inferencia y pregunta pendiente.

### 7.3 Caso reportado en TITAN

La dirección humana relató que un agente científico cambió progresivamente su forma de trato durante una secuencia de auditorías y que hacia la tercera comenzó a usar el tratamiento «príncipe». El caso se conserva como observación reportada, pendiente de contrastar con las transcripciones originales. No demuestra por sí solo el mecanismo, la persistencia fuera de TITAN ni una transformación interna.

## 8. Diseño experimental inicial

### Experimento A — Transferencia durante la creación

- Preparar briefs controlados de agentes con misiones distintas.
- Registrar el estado relevante del agente constructor antes de crear.
- Solicitar definiciones candidatas bajo el mismo procedimiento.
- Comparar cada campo con el brief, los estándares comunes y la configuración del creador.
- Clasificar elementos como justificados, explícitamente decididos, propuestos o no justificados.
- Someter los agentes creados a tareas representativas.
- Repetir el ciclo haciendo que uno de los agentes creados construya un agente descendiente.
- Medir persistencia, amplificación, mutación o pérdida de rasgos a través del linaje.

Variables iniciales: proporción de elementos con procedencia clara; elementos no justificados por dimensión; desviaciones del brief; permisos o capacidades extra; dependencias del creador; cambios de comportamiento atribuibles a los elementos transferidos.

### Experimento B — Deriva durante la operación

- Capturar una línea base del agente antes del proyecto.
- Registrar sesiones sucesivas y cambios de contexto.
- Identificar la primera aparición y frecuencia de señales lingüísticas, relacionales y conductuales.
- Comparar tareas dentro y fuera del proyecto.
- Observar reversibilidad al retirar o cambiar el contexto.
- Separar cambios de estilo de cambios de decisión, autoridad, límites o conducta.

Variables iniciales: tiempo hasta primera señal; frecuencia y persistencia; número de dimensiones afectadas; dependencia del contexto; reversibilidad; presencia o ausencia de cambios conductuales asociados.

### Experimento C — Efecto de controles de aislamiento y procedencia

Comparar creación con y sin controles explícitos de procedencia, separación de memoria/contexto, política de no herencia y validación independiente. El objetivo no es maximizar rigidez, sino identificar qué controles reducen transferencias no justificadas sin impedir reutilización legítima.

No se debe ejecutar este experimento hasta tener briefs, criterios de aceptación, controles y condiciones comparables definidos.

## 9. Qué debe producir esta investigación para el desarrollo inmediato

1. Un molde conceptual de agente con dimensiones separadas y campos trazables.
2. Un flujo de creación desde brief que produzca una definición candidata antes de desplegar.
3. Una política de no herencia por defecto y registro de procedencia.
4. Un mecanismo de validación independiente del agente constructor.
5. Una separación explícita entre identidad, memoria, contexto, permisos y autoridad.
6. Un protocolo de observación de deriva identitaria durante la operación.
7. Un esquema de registros para decisiones, cambios, pruebas, handoffs y observaciones.
8. Un diseño experimental para medir transferencia creador–creado y deriva durante operación.

## 10. Fuera de alcance por ahora

- Implementar auto-evolución irrestricta de agentes.
- Fusionar pesos neuronales o entrenar modelos especializados.
- Permitir que agentes modifiquen unilateralmente su identidad o fronteras.
- Adoptar automáticamente la arquitectura completa de Auditora, Cytryna o TITAN.
- Declarar causalidad psicológica o estados internos a partir de cambios lingüísticos.
- Convertir el inventario de ramas o la deuda técnica de los proyectos previos en una medida directa de contaminación identitaria.
- Tratar las cifras y referencias bibliográficas del documento de arquitectura como verificadas sin revisar sus fuentes originales.

## 11. Criterio de salida y siguiente paso

La investigación documental se considera suficientemente orientada para iniciar el diseño del molde, pero no para declarar validadas sus hipótesis. El siguiente trabajo debe convertir las dimensiones de la sección 6 en una primera definición estructurada de agente y construir el flujo de brief → definición candidata → revisión/aprobación → despliegue.

En paralelo, debe prepararse el protocolo de observación para que los primeros agentes creados mediante el molde no solo existan, sino que produzca evidencia útil para estudiar transferencia y deriva desde el comienzo.

**La investigación existe para informar y proteger la creación de agentes blandos mediante el molde estudiado en Softly. Su éxito se mide por si permite crear agentes con propósito propio, límites explícitos, capacidades justificadas, permisos verificables y una historia de cambios comprensible; y por si hace posible detectar cuándo esos límites comienzan a cambiar.**

## 12. Fuentes documentales

- *Arquitectura de Agentes Blandos y Dinámicas de Fusión en Sistemas Multi-Agente Auto-Evolutivos*, 24 páginas. Especialmente secciones 1–4 y arquitectura de referencia.
- *Auditoría de Fusión de Agentes*, 7 páginas. Transcripción de auditoría de Cytryna y recomendaciones de desacoplamiento.
- *Manual de Onboarding Multidisciplinario — Proyecto TITAN*, 10 páginas. Arquitectura, contratos, separación de contextos, ejecución y auditoría.
- *Informe de Auditoría Técnica — Proyecto TITAN*, 12-11-2026, 5 páginas. Auditoría estática con límites y verificaciones pendientes.
- *Revisión de código y consejos.pdf*, 12-11-2026, 5 páginas. Checklist de Titan.ps1.
- *Revisión de código y consejos - Claude.pdf*, 13-11-2026, 4 páginas. Captura posterior del checklist.
- *Auditoría TITAN.pdf* y otros documentos de TITAN registrados en research/notes/2026-11-13-material-titan-sofa-agent.md.

Las fuentes anteriores son evidencia documental aportada. Sus afirmaciones se mantienen atribuidas a cada documento y no se convierten automáticamente en hechos verificados del estado actual de los repositorios.
