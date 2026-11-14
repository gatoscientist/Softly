# SYN-20261113-001 — Línea base de contaminación multi-rama en TITAN

**Fecha de observación:** 2026-11-13 (America/Santiago)  
**Repositorio observado:** `gatoscientist/TITAN`  
**Rama principal:** `main`  
**Propósito:** establecer una línea base reproducible antes del ingreso de una nueva generación de agentes.  
**Estado:** investigación preliminar; no es auditoría final ni autorización de limpieza.

## 1. Pregunta de investigación y corrección del foco

La pregunta central no es cuánto desorden técnico u organizacional deja un equipo que trabaja mal. Esa clase de residuos —errores, duplicaciones, ramas, deuda técnica, archivos temporales, documentación inconsistente— puede detectarse mediante revisión y herramientas convencionales. Es información contextual útil, pero no define el fenómeno que Softly busca estudiar.

**La contaminación fundamental que interesa estudiar es la que aparece cuando desarrolladores humanos o agentes se fusionan con el proyecto que desarrollan.** Es decir, cuando su identidad, preferencias, supuestos, criterios, hábitos, modelos mentales y necesidades particulares pasan a incorporarse al proyecto, a veces sin ser reconocidos como decisiones personales ni justificados por los objetivos originales del sistema.

Esta contaminación puede producirse incluso con desarrolladores técnicamente competentes y entregables de alta calidad. No equivale necesariamente a mala conducta, código defectuoso ni incumplimiento. El objeto de estudio es la huella que deja la incorporación no examinada de la visión particular de quienes desarrollan sobre la identidad, arquitectura, lenguaje, prioridades y comportamiento futuro del proyecto.

La proliferación de ramas y los residuos convencionales observados en TITAN se conservan como contexto y como línea base operacional secundaria. No deben confundirse con el fenómeno principal ni sustituir su investigación.

La hipótesis central requiere operacionalización: identificar qué rasgos del proyecto provienen de sus requisitos y decisiones legítimas, cuáles fueron introducidos por contribuyentes concretos, cuáles se volvieron dependencias o convenciones implícitas y cuáles alteran el proyecto sin una decisión consciente de sus responsables.

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


## 9. Fenómeno central: fusión del desarrollador con el proyecto

### 9.1 Definición de trabajo

Se denomina **contaminación por fusión desarrollador–proyecto** al proceso por el cual preferencias, supuestos, hábitos, lenguaje, identidad, modelos mentales o intereses particulares de un desarrollador (humano o agente) se incorporan al proyecto y comienzan a condicionar su diseño, evolución, interpretación o funcionamiento, sin que esa incorporación haya sido necesariamente solicitada, explicitada, evaluada o adoptada conscientemente por la dirección del proyecto.

La definición no presupone mala intención ni incompetencia. Una contribución puede ser técnicamente correcta y aun así introducir una orientación ajena a la misión o convertir una preferencia local en una característica estructural.

### 9.2 Distinciones necesarias

No toda influencia del desarrollador es contaminación. Desarrollar implica tomar decisiones e introducir conocimiento. Para estudiar el fenómeno hay que distinguir:

- **Contribución legítima:** cambio solicitado o necesario, trazable a requisitos, restricciones o una decisión autorizada.
- **Decisión de diseño explícita:** alternativa elegida conscientemente, con rationale, autoridad y consecuencias conocidas.
- **Influencia no examinada:** preferencia o supuesto del desarrollador que se incorpora sin hacerse visible como decisión.
- **Fusión:** la influencia no examinada se vuelve parte de la identidad, las convenciones, los contratos, el lenguaje o las dependencias del proyecto y condiciona el trabajo posterior.
- **Contaminación acumulativa:** sucesivas fusiones o influencias no examinadas se superponen, se normalizan y hacen cada vez más difícil distinguir el diseño del proyecto de la visión de sus contribuyentes.

### 9.3 Dimensiones candidatas para observar

Estas dimensiones son hipótesis de observación, no hallazgos ya demostrados en TITAN:

1. **Conceptual:** el desarrollador redefine qué es el proyecto, qué problema resuelve o qué significa que esté terminado.
2. **Arquitectónica:** introduce patrones, capas, abstracciones, frameworks o complejidad que responden a su modelo mental más que a requisitos comprobados.
3. **Semántica y lingüística:** impone nombres, metáforas, vocabulario, taxonomías o conceptos propios que luego condicionan cómo el equipo entiende el sistema.
4. **Normativa:** transforma preferencias personales en reglas, principios o políticas del proyecto sin autorización explícita.
5. **Funcional:** agrega capacidades, comportamientos o flujos que no fueron solicitados y que desplazan prioridades originales.
6. **Operacional:** incorpora herramientas, rutinas, procesos, formatos o dependencias que hacen que el proyecto se adapte al modo de trabajo de ese contribuyente.
7. **Relacional y de autoridad:** instala dependencias respecto de una persona/agente, privilegios implícitos, canales informales de decisión o una distribución de autoridad no acordada.
8. **Memoria e histórica:** deja explicaciones, documentación o relatos que presentan sus propias decisiones como si siempre hubieran sido parte del diseño original.
9. **Estética y estilística:** convierte preferencias de presentación, interacción o estilo en convenciones estructurales sin que exista una razón de producto.
10. **Epistémica:** hace que el proyecto adopte sus criterios de evidencia, prioridades, tolerancia a la incertidumbre o formas de validar como si fueran universales.

### 9.4 Pregunta de auditoría del fenómeno

No preguntar solamente «¿qué quedó mal?». Preguntar:

- ¿Qué parte del proyecto responde a una necesidad demostrable y qué parte responde a una preferencia del contribuyente?
- ¿Qué supuestos personales se convirtieron en contratos, dependencias, convenciones o restricciones?
- ¿Qué decisiones fueron tomadas por la dirección y cuáles fueron introducidas silenciosamente durante la implementación?
- ¿El proyecto puede ser comprendido, mantenido y extendido por otro equipo sin adoptar la identidad, hábitos o marco mental de sus autores anteriores?
- ¿Qué elementos sobreviven porque son necesarios y cuáles sobreviven porque nadie cuestionó su origen?
- ¿Qué cambios alteraron la misión, el lenguaje, la arquitectura o la experiencia del proyecto sin una decisión explícita?
- ¿Qué partes del sistema hacen que los siguientes desarrolladores deban adaptarse al autor anterior, en vez de adaptarse a los requisitos del proyecto?

### 9.5 Método de investigación propuesto

Para cada contribución o conjunto de cambios, reconstruir una cadena de procedencia:

**requisito/objetivo → decisión autorizada → contribución → artefacto introducido → dependencia o convención creada → efecto sobre el trabajo posterior.**

Registrar por separado:
- origen y autoría de la influencia;
- evidencia observable en commits, código, configuración, documentación, interfaces y comportamiento;
- justificación declarada al introducirla;
- autoridad con la que se incorporó;
- persistencia y alcance dentro del proyecto;
- costo de revertirla o sustituirla;
- efecto sobre la capacidad de un nuevo equipo para trabajar sin heredar el marco mental del equipo anterior.

No inferir estados psicológicos ni atribuir intenciones. La investigación trata sobre huellas observables en el proyecto y su procedencia, no sobre juzgar personas.

### 9.6 Diseño del experimento con nuevas generaciones de agentes

La limpieza de ramas y el archivo de snapshots permiten establecer un punto de partida operacional. El experimento principal debe observar si una nueva generación de agentes introduce elementos propios que se fusionan con el proyecto.

Para cada ciclo:
1. Registrar la misión, requisitos, límites y estado inicial del proyecto.
2. Dar a los agentes una asignación acotada, evitando prescribir soluciones innecesarias.
3. Conservar trazabilidad de sus propuestas, decisiones, cambios y justificaciones.
4. Comparar el estado final con el inicial y con los requisitos autorizados.
5. Identificar elementos nuevos que no se expliquen por requisitos o decisiones explícitas.
6. Examinar si esos elementos se convierten en dependencias, convenciones o condicionantes para el siguiente ciclo.
7. Probar si un equipo distinto puede continuar el trabajo sin adoptar supuestos particulares de los agentes anteriores.
8. Clasificar cada influencia como legítima, explícitamente adoptada, no examinada o fusión confirmada con evidencia.

No se debe penalizar automáticamente la creatividad, la iniciativa ni las mejoras propuestas. El problema no es que el desarrollador influya en el proyecto; el problema investigable es que esa influencia se vuelva parte del proyecto sin visibilidad, procedencia ni decisión consciente.

### 9.7 Relación con la línea base de ramas

La proliferación de ramas, la dispersión de archivos y la duplicación son residuos convencionales y medibles. Pueden ser síntomas de un sistema de trabajo deficiente, pero no demuestran por sí solos fusión desarrollador–proyecto.

Por lo tanto:
- mantener el inventario de ramas como línea base histórica;
- no usar el número de ramas como medida principal de contaminación;
- no equiparar limpieza técnica con ausencia de fusión;
- analizar los ZIP como evidencia de procedencia y evolución, no solo como paquetes de archivos;
- evaluar la contaminación fundamental a partir de la relación entre contribuciones, decisiones, artefactos y efectos persistentes.

### 9.8 Estado epistemológico

La definición y las dimensiones anteriores son una **propuesta conceptual de investigación** derivada de la corrección de foco del director humano. No son todavía un modelo validado ni hallazgos concluyentes sobre los agentes de TITAN. Deben someterse a contraste con los archivos históricos, las auditorías disponibles y el comportamiento de nuevas generaciones de agentes.
