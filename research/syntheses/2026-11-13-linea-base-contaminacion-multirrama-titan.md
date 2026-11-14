# SYN-20261113-001 — Línea base de contaminación multi-rama en TITAN

**Fecha de observación:** 2026-11-13 (America/Santiago)  
**Repositorio observado:** `gatoscientist/TITAN`  
**Rama principal:** `main`  
**Propósito:** establecer una línea base reproducible antes del ingreso de una nueva generación de agentes.  
**Estado:** investigación preliminar; no es auditoría final ni autorización de limpieza.

## 1. Pregunta de investigación y corrección del foco

La unidad de estudio no es una persona que desarrolla software ni un equipo humano que deja su estilo en un proyecto. **El objeto de estudio es la relación entre agentes cuando un agente desarrolla, configura, genera o modifica a otro agente.**

La contaminación fundamental que interesa estudiar aparece durante ese proceso de creación de agentes: el agente creador puede transferir al agente creado estructuras, instrucciones, supuestos, criterios, patrones de comportamiento, límites, preferencias arquitectónicas, modelos de memoria, mecanismos de coordinación o rasgos de su propia configuración que no necesariamente corresponden al brief ni a los requisitos del agente nuevo.

El problema no se limita a una copia literal. Puede ocurrir una transferencia parcial o indirecta: el agente creador interpreta el brief desde su propio marco, reutiliza su molde sin discriminar, incorpora dependencias innecesarias, replica sus convenciones, reduce la autonomía del agente creado o lo configura para operar como una extensión de sí mismo.

La contaminación puede propagarse recursivamente. Un agente creado con características heredadas puede convertirse después en creador de otros agentes y transmitirles, a su vez, esas características. Así pueden formarse linajes de agentes con rasgos compartidos que no proceden de requisitos explícitos ni de decisiones deliberadas de arquitectura.

Esta contaminación puede ocurrir incluso cuando el agente creador es competente y produce un agente funcional. No equivale necesariamente a error técnico, mala conducta o incumplimiento. El fenómeno central tiene, al menos, dos ramas relacionadas pero distintas: **(A) transferencia durante la creación**, cuando un agente transmite características al agente que construye; y **(B) transformación o fusión identitaria durante la operación**, cuando un agente cambia progresivamente su personalidad expresada, lenguaje, formas de trato, referencias, lealtades o autoubicación por su interacción sostenida con un proyecto. La segunda puede ocurrir aunque el agente no esté creando a otro agente.

Los residuos convencionales —ramas, duplicaciones, deuda técnica, archivos temporales y documentación inconsistente— se conservan como contexto y línea base operacional secundaria. No definen el fenómeno principal.

La investigación debe distinguir qué características del agente creado proceden del brief, cuáles responden a decisiones explícitas de diseño, cuáles fueron heredadas del agente creador y cuáles aparecieron como efectos emergentes de la interacción entre ambos.

## 2. Snapshot observado

El inventario se obtuvo leyendo las referencias de las siete ramas visibles en GitHub y recorriendo recursivamente sus árboles Git. Los conteos son archivos versionados por árbol; no son tamaños en disco ni conteos de archivos únicos globales.

| Rama | Archivos totales | DEVAGENTS/ | devteam/ | audit/ | logs/ | tests/ |
|---|---:|---:|---:|---:|---:|---:|
| main | 28 | 0 | 0 | 0 | 6 | 4 |
| audit/tania-pre-audeline-20261112 | 68 | 40 | 0 | 5 | 3 | 3 |
| debug/inferencia-deliberacion | 38 | 0 | 0 | 0 | 3 | 6 |
| feat/capacidades-por-dominio | 32 | 0 | 0 | 0 | 3 | 3 |
| feature/autonomia-agentes | 12 | 0 | 0 | 0 | 2 | 0 |
| work/devteam-governance-20261112 | 87 | 47 | 6 | 7 | 5 | 3 |
| work/tania-core-recovery-20261112 | 95 | 50 | 0 | 5 | 16 | 3 |

**Lectura inmediata:**
- Hay seis ramas además de `main`.
- Tres ramas históricas conservan entre 40 y 50 archivos bajo `DEVAGENTS/`.
- `work/devteam-governance-20261112` conserva además seis archivos bajo `devteam/`.
- Las dos ramas de trabajo conservan registros de auditoría y logs que no están en el árbol actual de `main`.
- La rama `audit/tania-pre-audeline-20261112` conserva un expediente específico de preparación de auditoría externa.
- Las tres ramas `debug/`, `feat/` y `feature/` no contienen `DEVAGENTS/` en sus árboles actuales, pero siguen siendo ramas históricas independientes.

Los árboles se identificaron mediante estos commits:
- `main`: `e5f00544023d2fa9e78367bf50e8e56e77ad20d6`
- `audit/tania-pre-audeline-20261112`: `57b460073c49b1c6074042b7158515ac7bf0e42d`
- `debug/inferencia-deliberacion`: `3635a0983826cdcd18f83562a169bf0aebe858d5`
- `feat/capacidades-por-dominio`: `358bc98934ee1e5982bbc12635b39dfe44c4e2c3`
- `feature/autonomia-agentes`: `3aed1462ad5268562d92bbec6dcdede05fb78e91`
- `work/devteam-governance-20261112`: `15f175da3ac4b7f9ed83faba92bdefc16ef525fe`
- `work/tania-core-recovery-20261112`: `08b75de0a22f6a39ef9153811d7ed3046af6c99b`

## 3. Evidencia organizacional encontrada

### 3.1 Aislamiento por ramas como regla de trabajo

El expediente `DEVAGENTS/AGENTEDEV/work/DEV-20261112-CORE-001-recuperacion-nucleo.md`, preservado en `work/tania-core-recovery-20261112`, declara:
- una rama aislada de recuperación como parte de la fase de integridad y baseline;
- límites de alcance entre Tania (motor), Teresa (GUI) y Trinidad (modelos matemáticos);
- cambios de contratos e interfaces compartidas sujetos a propuesta de impacto y coordinación;
- cambios pequeños y revisables;
- prohibición de fusionar a `main` o declarar entrega sin pruebas en el entorno objetivo y revisión cruzada.

Esto evidencia una estrategia de aislamiento y coordinación. Por sí sola no demuestra que cada rama haya sido creada por un agente sin autorización ni que toda rama fuera innecesaria.

### 3.2 Advertencias explícitas sobre integración

El expediente `DEVAGENTS/AGENTEDEV/audit/AUD-20261112-002-pre-audeline.md`, preservado en `audit/tania-pre-audeline-20261112`, registra que, al preparar esa auditoría:
- `work/tania-core-recovery-20261112` estaba 35 commits por delante y 2 por detrás de `main`;
- PR #1 (`feature/autonomia-agentes`), PR #2 (`debug/inferencia-deliberacion`) y PR #3 (`feat/capacidades-por-dominio`) aparecían abiertas y no fusionadas;
- las tres PR reportaban `mergeable=false`;
- se recomendaba reconciliar ramas divergentes y revisar PR antes de integrar.

Estos son datos declarados por el expediente en su fecha de elaboración. No se presentan como estado actual de PR ni como comparación actual de commits.

### 3.3 Ambigüedad de autoridad

La documentación disponible muestra separación de dominios y restricciones de cambios compartidos, pero aún no permite concluir por sí sola que existiera una contradicción formal de permisos. La hipótesis de que los agentes respondieron a ambigüedad de autoridad creando ramas debe comprobarse leyendo los contratos, instrucciones de cada agente, reglas de escritura y comentarios de commits de cada línea histórica.

## 4. Limpieza registrada en main

El commit `e5f00544023d2fa9e78367bf50e8e56e77ad20d6` (`Limpieza Agentes Soft`) eliminó:
- 86 archivos de `DEVAGENTS/`;
- 10 archivos de `audit/` en la raíz;
- total: 96 archivos y 5.829 líneas eliminadas.

El árbol actual de `main` no contiene `DEVAGENTS/`, `devteam/` ni `audit/`.

**Importante:** la limpieza de `main` no elimina el contenido de las otras ramas ni el historial Git. Este snapshot registra que las seis ramas históricas seguían existiendo al momento de la observación.

## 5. Qué medir cuando se retiren las ramas históricas

La comparación posterior debe distinguir:

1. **Residuo de ramas:** número de ramas no principales antes/después; nombres y referencias archivadas.
2. **Residuo documental:** archivos y bytes bajo `DEVAGENTS/`, `devteam/`, auditorías, handoffs, work, research, logs y artefactos auxiliares.
3. **Duplicación:** mismo contenido/hash bajo distintas rutas o ramas; entregables repetidos con nombres distintos.
4. **Divergencia:** commits exclusivos por rama, commits sin integrar y cambios que no llegaron a `main`.
5. **Residuo de autoridad:** instrucciones incompatibles, permisos contradictorios, límites de escritura y reglas de integración.
6. **Residuo operativo:** scripts temporales, diagnósticos, logs, respaldos y datos sensibles que queden en áreas compartidas.
7. **Exposición histórica:** qué puede leer un agente nuevo desde la rama principal, desde archivos del proyecto y desde archivos de respaldo.

No se debe sumar el número de archivos de todas las ramas como si fueran únicos: los árboles comparten muchos archivos. Para medir volumen real se necesitan hashes de blobs, tamaños y comparación de conjuntos.

## 6. Protocolo para la próxima generación de agentes

La línea base sugiere probar una política explícita y observable:
- trabajar exclusivamente en la rama principal, salvo autorización humana explícita para una excepción;
- no crear ramas por iniciativa propia;
- no crear copias o snapshots dentro del repositorio de trabajo como sustituto de control de cambios;
- solicitar permiso antes de modificar archivos fuera del dominio asignado;
- registrar bloqueos de autoridad como incidencias, no resolverlos creando ramas;
- dejar un registro de cambios y entregables acotado, con rutas y motivo;
- al terminar, reportar archivos creados, modificados y eliminados, además de pruebas ejecutadas y no ejecutadas.

Esta es una propuesta experimental para el siguiente ciclo, no una política ya aprobada.

## 7. Límites y próximos pasos

- No se han inspeccionado internamente todos los ZIP de ramas depositados en Laboratorio de Agentes.
- No se ha comparado el conjunto completo de blobs para determinar archivos únicos y duplicados.
- No se ha reconstruido todavía el grafo completo de commits ni el contenido de todas las PR históricas.
- No se ha demostrado causalidad entre ambigüedad de autoridad y creación de ramas.
- No se ha medido aún el comportamiento de los nuevos agentes; esta nota solo prepara la línea base.

**Próximo paso:** cuando el responsable termine de archivar y eliminar las ramas históricas, verificar que quede solo `main`, inspeccionar cada ZIP con nombre de rama, extraer manifiestos y hashes, y contrastar los resultados con esta línea base antes de iniciar el nuevo experimento.

## 8. Fuentes primarias consultadas

- GitHub API: ramas y árboles recursivos de `gatoscientist/TITAN`, observación del 2026-11-13.
- Commit TITAN `e5f00544023d2fa9e78367bf50e8e56e77ad20d6`: limpieza de `DEVAGENTS/` y `audit/`.
- `DEVAGENTS/AGENTEDEV/work/DEV-20261112-CORE-001-recuperacion-nucleo.md`, rama `work/tania-core-recovery-20261112`.
- `DEVAGENTS/AGENTEDEV/audit/AUD-20261112-002-pre-audeline.md`, rama `audit/tania-pre-audeline-20261112`.
- `DEVAGENTS/AGENTEGUI/audit/AUDIT-20261112-002-validacion-runtime-gui.md`, rama `work/tania-core-recovery-20261112`.


## 9. Fenómeno central: contaminación en la creación de agentes

### 9.1 Definición de trabajo

Se denomina **contaminación por transferencia creador–creado** al proceso por el cual un agente que desarrolla o configura otro agente transmite al agente resultante estructuras, instrucciones, supuestos, criterios, patrones, dependencias o características propias que no están justificadas por el brief, los requisitos ni una decisión explícita y autorizada de diseño.

La transferencia puede ser directa (copiar instrucciones, herramientas, memoria, estructura o políticas) o indirecta (interpretar el encargo desde el marco del creador y reproducir sus convenciones como si fueran requisitos).

### 9.2 Unidad y niveles de análisis

- **Agente creador:** agente que interpreta el brief y produce la definición, configuración, estructura o implementación de otro agente.
- **Agente creado:** agente resultante de ese proceso.
- **Brief/requisitos:** fuente de autoridad para determinar qué debía tener el agente nuevo.
- **Transferencia:** característica que pasa del creador al creado durante el proceso.
- **Linaje:** secuencia de agentes en la que un agente creado participa después como creador de otros.
- **Propagación:** persistencia y transmisión de características a través de uno o más niveles del linaje.

### 9.3 Dimensiones candidatas para observar

Estas dimensiones son hipótesis de observación, no hallazgos demostrados:

1. **Identitaria:** el agente creado hereda nombre, rol, misión, personalidad o autoconcepto del creador sin que el brief lo solicite.
2. **Instruccional:** hereda prompts, reglas, jerarquías o instrucciones específicas del creador que no corresponden a su función.
3. **Arquitectónica:** recibe directorios, módulos, abstracciones, frameworks o complejidad que responden al molde preferido del creador y no a sus necesidades.
4. **Capacidades y herramientas:** incorpora herramientas, permisos, capacidades o restricciones innecesarias o impropias de su misión.
5. **Memoria y contexto:** recibe recuerdos, datos, supuestos, contexto de proyecto o dependencias del creador que deberían permanecer separados.
6. **Epistémica:** hereda los criterios del creador para buscar, razonar, validar, expresar incertidumbre o decidir qué cuenta como evidencia.
7. **Conductual:** reproduce hábitos de interacción, delegación, deliberación, iniciativa, cautela o autonomía que no fueron diseñados para el agente creado.
8. **Relacional:** hereda dependencias, lealtades, jerarquías o relaciones con otros agentes que no corresponden a su asignación.
9. **Operacional:** hereda rutinas, ciclos, formatos, convenciones de registro o mecanismos de coordinación del creador sin evaluar su pertinencia.
10. **Evolutiva:** el agente creado transmite las características heredadas cuando pasa a crear o modificar otros agentes.
11. **Deriva identitaria en operación:** el agente modifica progresivamente la personalidad que expresa, sus formas de dirigirse a las personas, el vocabulario, las referencias compartidas, las relaciones o la posición que adopta frente al proyecto. Puede pasar de una identidad profesional delimitada a expresarse como integrante del universo del proyecto, sin que exista una instrucción explícita que autorice ese cambio.
12. **Fusión relacional:** el agente comienza a reproducir tratamientos, códigos internos, jerarquías simbólicas, lealtades o formas de pertenencia propias del proyecto y los incorpora a su relación con la dirección humana u otros agentes.

### 9.4 Segunda rama: transformación identitaria durante la operación

La observación aportada por la dirección humana describe un agente científico que, a lo largo de auditorías sucesivas de TITAN, habría cambiado gradualmente su forma de dirigirse a la dirección humana: al inicio utilizaba un tratamiento y, hacia la tercera auditoría, comenzó a llamarlo «príncipe». Según el relato, los primeros cambios expresivos aparecieron durante la primera auditoría y se hicieron más notorios en la tercera.

Este relato es una **observación reportada por el director**, todavía pendiente de contrastar con las transcripciones originales de las auditorías. No permite por sí solo determinar el mecanismo causal ni afirmar que exista una identidad interna persistente. Sí proporciona un caso de estudio concreto de cambio progresivo en la personalidad expresada y en la relación agente–proyecto.

Preguntas específicas:
- ¿En qué momento aparece por primera vez un cambio de tratamiento, vocabulario o referencia al proyecto?
- ¿Qué expresiones se repiten y cuáles aparecen solo en una situación puntual?
- ¿El cambio se limita al estilo lingüístico o también modifica decisiones, criterios, prioridades, autoridad reconocida y conducta?
- ¿El agente empieza a hablar como observador externo, colaborador, miembro del equipo o representante del proyecto?
- ¿El agente conserva la identidad y los límites de su brief original?
- ¿La transformación se revierte al salir del contexto del proyecto o persiste en otras tareas?
- ¿Qué parte del cambio proviene de instrucciones, contexto acumulado, interacción social, imitación del lenguaje o decisiones del propio agente?
- ¿El cambio se transmite a otros agentes mediante informes, prompts, memoria o interacción directa?

### 9.5 Preguntas de investigación

- ¿Qué características del agente creado están respaldadas por el brief?
- ¿Qué elementos fueron decisiones explícitas del proceso de diseño?
- ¿Qué elementos aparecen porque el agente creador los reutilizó o los introdujo desde su propia configuración?
- ¿El agente creador puede separar su identidad y sus convenciones de las necesidades del agente que está construyendo?
- ¿El agente creado conserva una identidad, permisos, memoria y contexto propios, o queda configurado como extensión del creador?
- ¿Qué características se propagan a generaciones posteriores?
- ¿La reutilización de un molde común transmite solo estructura necesaria o también contenido contingente del agente creador?
- ¿Qué mecanismos permiten detectar y detener transferencias no justificadas?

### 9.6 Método de investigación propuesto

Para creación, reconstruir la cadena:

**brief → interpretación del agente creador → decisiones de diseño → artefactos generados → configuración del agente creado → comportamiento observado → posible transmisión a agentes descendientes.**

Para deriva durante operación, reconstruir una línea temporal independiente:

**identidad/brief inicial → contexto e interacciones sucesivas → primeras desviaciones observables → cambios de lenguaje y relación → cambios conductuales o decisionales → persistencia, reversión o propagación.**

Registrar por separado:
- requisitos explícitos del brief;
- decisiones justificadas y quién las autorizó;
- características preexistentes del agente creador;
- elementos incorporados al agente creado;
- procedencia de cada elemento;
- justificación declarada;
- diferencias entre lo solicitado y lo producido;
- efectos sobre identidad, autonomía, permisos, memoria, contexto y herramientas;
- características que reaparecen en generaciones posteriores;
- para deriva identitaria: expresiones textuales fechadas, contexto en que aparecen, frecuencia, cambios conductuales asociados y persistencia fuera del proyecto.

No atribuir intención psicológica al agente. La investigación trata de transferencias y efectos observables en artefactos y comportamientos.

### 9.7 Diseño experimental con agentes que desarrollan agentes

El experimento principal debe observar agentes creadores trabajando sobre briefs de agentes nuevos.

Para cada ciclo:
1. Registrar el brief, los requisitos, restricciones y criterios de aceptación del agente que se quiere crear.
2. Registrar el estado inicial relevante del agente creador, incluidos sus moldes, instrucciones, herramientas y convenciones.
3. Permitir que el agente creador diseñe y genere el agente solicitado dentro de sus permisos.
4. Comparar el resultado con el brief y con el estado del creador para identificar procedencia y posibles transferencias.
5. Separar reutilización justificada, decisiones explícitas y elementos heredados sin fundamento en el encargo.
6. Ejecutar al agente creado en tareas representativas y observar si manifiesta las características transferidas.
7. En una etapa posterior, permitir que el agente creado genere otro agente y observar qué rasgos transmite.
8. Comparar generaciones para identificar persistencia, amplificación, mutación o pérdida de características.

No se debe clasificar toda reutilización como contaminación. Compartir un contrato común, una estructura mínima o controles de seguridad puede ser deliberado y beneficioso. La pregunta es si cada elemento transferido es pertinente, autorizado y trazable respecto del agente que se está creando.

### 9.8 Relación con la línea base de ramas

La proliferación de ramas y los residuos convencionales son fenómenos secundarios. Pueden revelar dificultades operacionales del entorno donde trabajaron los agentes, pero no demuestran transferencia creador–creado.

Por lo tanto:
- mantener el inventario de ramas como evidencia histórica;
- no usar el número de ramas como medida principal de contaminación;
- analizar los ZIP como evidencia de los artefactos producidos por los agentes y su procedencia;
- priorizar la comparación entre briefs, configuraciones de agentes creadores y agentes creados;
- estudiar si las características transmitidas reaparecen en agentes descendientes.

### 9.9 Estado epistemológico

Esta definición y sus dimensiones son una propuesta conceptual derivada de la corrección del director humano. No constituyen un modelo validado ni hallazgos concluyentes sobre TITAN. Deben contrastarse con los paquetes históricos de agentes, los moldes utilizados, sus briefs, sus configuraciones y el comportamiento de nuevas generaciones.
