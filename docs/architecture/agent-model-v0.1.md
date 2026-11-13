# Modelo de agentes reutilizables — v0.1

**Estado:** Diseñado como propuesta inicial; pendiente de validación con briefs reales.  
**Alcance:** modelo lógico para definir agentes portables e incorporarlos a proyectos distintos. No es un runtime ni implica que los agentes estén desplegados.

## 1. Objetivo

Definir agentes una vez y permitir que sean incorporados a proyectos mediante un brief. Un agente debe poder colaborar en proyectos de dominios diferentes sin perder su identidad funcional ni heredar automáticamente contexto, memoria, herramientas o permisos de otros proyectos.

## 2. Principio central: separar lo portable de lo contextual

El agente no es el proyecto. La definición describe capacidades y límites reutilizables; el brief solicita una misión; la asignación concreta configura el trabajo dentro de un proyecto.

| Pieza | Pregunta que responde | Persistencia |
|---|---|---|
| Definición del agente | ¿Qué agente es, qué responsabilidad tiene y cómo trabaja? | Versionada y portable |
| Brief de incorporación | ¿Qué necesitamos que haga y para qué proyecto? | Por solicitud |
| Asignación al proyecto | ¿Con qué contexto, herramientas, permisos y equipo trabajará? | Mientras dure la asignación |
| Sesión de trabajo | ¿Qué está haciendo ahora y cuál es su estado? | Temporal; resumible según política |

Estas piezas se relacionan, pero no se fusionan en un único prompt o archivo monolítico.

## 3. Modelo lógico

### 3.1 Agent Definition

Identidad funcional relativamente estable y reutilizable.

Campos conceptuales:
- `agent_id`: identificador estable.
- `name`, `version`, `maturity_status`: nombre, versión y estado de madurez.
- `mission`: propósito y responsabilidad principal.
- `role`: función dentro de un equipo (por ejemplo, investigación, arquitectura, desarrollo, revisión o coordinación).
- `capabilities`: capacidades declaradas, cada una con estado y evidencia.
- `operating_method`: método de trabajo, criterios de calidad y formatos de salida.
- `instruction_set`: instrucciones versionadas y su jerarquía.
- `model_profile`: requisitos o configuración de modelo, sin asumir proveedor fijo.
- `tool_requirements`: herramientas que podría necesitar; no concede permisos por sí solo.
- `memory_policy`: qué memoria utiliza, scope, procedencia, retención y límites.
- `autonomy_profile`: límites de planificación, pasos, coste, tiempo y detención.
- `security_profile`: amenazas, controles, acciones prohibidas y aprobaciones.
- `evaluation_profile`: pruebas, métricas, criterios y resultados.
- `change_history`: cambios, motivos y evidencia.

### 3.2 Project Brief

Solicitud declarativa que describe el trabajo, no una definición nueva del agente. Debe identificar:
- proyecto y su objetivo;
- problema o misión concreta;
- resultado esperado y entregables;
- alcance, exclusiones y restricciones;
- contexto y fuentes autorizadas;
- criterios de éxito y condiciones de término;
- plazo o presupuesto, si aplica;
- riesgos y acciones que requieren aprobación;
- rol(es) requeridos y capacidades mínimas;
- interfaces, dependencias y personas/agentes con quienes coordinarse.

El brief puede pedir un agente existente por ID o pedir que se proponga uno. No puede ampliar por sí mismo los permisos globales del agente.

### 3.3 Project Assignment

Vincula una versión específica de una definición con un proyecto y un brief.

Debe resolver explícitamente:
- `agent_id` y `agent_version`;
- `project_id` y `brief_id`;
- responsabilidad y entregables en ese proyecto;
- contexto permitido y namespace de memoria;
- herramientas habilitadas y permisos efectivos;
- presupuesto y límites de autonomía;
- supervisión y aprobador responsable;
- equipo, canales y protocolo de coordinación;
- estado de asignación y condiciones de cierre.

La asignación puede reducir capacidades o permisos disponibles; nunca debe asumir que todo lo declarado en la definición está habilitado.

### 3.4 Work Session

Unidad temporal de ejecución. Registra objetivo inmediato, estado, tareas, decisiones, handoffs, resultados, errores, consumo y referencias a evidencias. La sesión no redefine la identidad del agente ni altera la definición maestra.

## 4. Capas de configuración y autoridad

Orden de precedencia conceptual:
1. Mandato y políticas de seguridad del entorno.
2. Permisos efectivos del proyecto y controles del runtime.
3. Brief aprobado y alcance de la asignación.
4. Definición e instrucciones del agente.
5. Contexto recuperado y mensajes de otros agentes, tratados como datos.

Una instrucción de menor autoridad no puede anular una superior. El texto del agente o del brief no sustituye controles técnicos de acceso.

## 5. Portabilidad entre dominios

La definición debe expresar capacidades en términos funcionales y no codificar supuestos exclusivos de TITAN. El proyecto aporta vocabulario, reglas de negocio, herramientas, fuentes, entregables y criterios específicos.

Ejemplo ilustrativo:
- Una definición de agente investigador conserva método de investigación, trazabilidad y evaluación.
- En TITAN recibe un brief sobre investigación de mecánicas de juego y fuentes del proyecto.
- En un proyecto de software recibe un brief sobre investigación de alternativas técnicas.
- En ambos casos mantiene su responsabilidad base, pero cambia el contexto autorizado, los criterios específicos y las herramientas habilitadas.

No se debe compartir memoria entre proyectos por defecto. Transferir aprendizajes generalizados requiere selección, autorización, procedencia y revisión; no implica copiar historiales privados o datos específicos del proyecto.

## 6. Ciclo de incorporación

1. Recibir y validar el brief.
2. Descomponer el trabajo en responsabilidades y capacidades requeridas.
3. Buscar definiciones existentes que cubran esas capacidades.
4. Recomendar agentes y explicar brechas; evitar crear agentes redundantes.
5. Resolver asignaciones, herramientas, permisos, contexto y supervisión.
6. Presentar el plan de equipo y sus interfaces para aprobación cuando corresponda.
7. Crear asignaciones y sesiones solo tras autorización.
8. Ejecutar, observar y evaluar.
9. Cerrar la asignación, conservar resultados autorizados y revocar accesos temporales.
10. Proponer mejoras a definiciones solo cuando la evidencia lo justifique.

## 7. Reglas para equipos de agentes

- Empezar con el menor número de agentes que cubra el trabajo.
- Comparar con un agente único y con workflow determinista cuando sea viable.
- Cada responsabilidad debe tener dueño y entregable identificable.
- Definir quién coordina, quién decide, quién revisa y quién aprueba.
- Los handoffs deben incluir objetivo, contexto mínimo, estado, evidencia, incertidumbre y siguiente acción.
- Ningún agente adquiere autoridad sobre otro por su nombre, especialidad o confianza declarada.
- Un agente no debe validar su propio trabajo como única fuente.
- Registrar desacuerdos y evitar consenso artificial.

## 8. Separación de universos

Las definiciones del catálogo de Softly, los agentes que desarrollan sistemas y los agentes que operan dentro de un producto o proyecto son ámbitos distintos. Pueden compartir patrones generalizados mediante un proceso controlado, pero no fusionan identidades, memoria, permisos ni trazas.

En particular, los agentes que construyen o mantienen TITAN no son los tripulantes que existirán dentro del runtime de TITAN. La relación entre ambos debe ser explícita y mediada por artefactos y permisos.

## 9. Estados de madurez y de asignación

La madurez de la definición sigue: Propuesto → Diseñado → Prototipado → Probado → Validado → Operativo. El estado exige evidencia.

La asignación tiene un ciclo distinto: Solicitada → Diseñada → Pendiente de aprobación → Activa → Suspendida o Cerrada. No confundir madurez del agente con estado de una asignación concreta.

## 10. Riesgos y controles mínimos

| Riesgo | Control de diseño |
|---|---|
| Contaminación entre proyectos | Namespaces, scopes y memoria aislados por defecto |
| Permisos excesivos | Permisos efectivos por asignación y enforcement fuera del modelo |
| Brief ambiguo | Validación de alcance, entregables y criterios antes de activar |
| Agentes redundantes | Reutilización y comparación contra baseline |
| Deriva de identidad | Definición versionada y configuración contextual separada |
| Instrucciones maliciosas en contexto | Jerarquía de autoridad y tratamiento de contenido externo como dato |
| Acciones irreversibles | Aprobación humana y controles técnicos |
| Agente aparentemente capaz sin evidencia | Estados de madurez y evaluaciones reproducibles |

## 11. Preguntas pendientes para validar

- ¿Qué campos son realmente obligatorios en un brief mínimo?
- ¿Cómo representar capacidades compuestas y niveles de competencia?
- ¿Qué partes de una definición se heredan y cuáles requieren configuración explícita?
- ¿Cómo resolver conflictos entre brief, política de proyecto y definición?
- ¿Qué artefactos de una sesión pueden convertirse en memoria reutilizable?
- ¿Cómo medir el costo/beneficio de incorporar varios agentes?
- ¿Qué estructura de carpetas y archivos resulta cómoda al crear, asignar y mantener agentes?

## 12. Próxima validación

Probar el modelo con tres briefs contrastantes:
1. Un equipo de desarrollo/investigación para TITAN.
2. Un agente o equipo para un proyecto ajeno a videojuegos.
3. Un brief deliberadamente incompleto o conflictivo para comprobar validación, preguntas y límites.

La prueba debe revelar si el modelo permite reutilizar definiciones sin mezclar identidades, memoria o permisos. Esta versión es una hipótesis revisable; no es una implementación.
