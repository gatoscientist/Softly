# SOFT-RES-001 — Anatomía de un agente persistente

- **ID:** SOFT-RES-001
- **Fecha:** 2026-11-13
- **Tipo:** ficha de investigación arquitectónica
- **Estado:** exploratoria; conclusión provisional, no normativa
- **Pregunta:** ¿Qué partes debe poder describir Softly para definir un agente persistente, sin imponer que todos los agentes tengan la misma estructura interna?
- **Alcance:** estructura conceptual y límites del agente. No define capacidades, especialidad, modelo, runtime ni mecanismo de despliegue.

## 1. Contexto y criterio

Softly necesita una forma reutilizable de describir agentes que puedan incorporarse a proyectos distintos. La definición del agente debe distinguirse del brief del proyecto y de la asignación contextual de cada sesión.

Modelo de trabajo actualmente documentado:

1. **Definición del agente:** identidad, rol, instrucciones, memoria declarada y límites.
2. **Brief de proyecto:** objetivo, dominio, contexto y resultado esperado.
3. **Asignación contextual:** herramientas, permisos, fuentes, equipo y restricciones disponibles en ese proyecto.
4. **Sesión de trabajo:** ejecución concreta bajo el contexto y las autorizaciones asignadas.

Este modelo es una base de análisis, no una implementación automática ni una decisión cerrada sobre el formato final.

## 2. Perspectivas que deben contrastarse

La investigación no debe elegir de antemano entre una estructura universal rígida y agentes completamente libres. Se contrastan tres alternativas:

### A. Contrato estructural común

Todos los agentes exponen un conjunto mínimo compartido de campos y límites. La estructura interna puede variar.

**Ventaja esperada:** interoperabilidad, validación y comprensión consistente.

**Riesgo:** convertir el contrato mínimo en una plantilla demasiado rígida o confundir campos descriptivos con controles efectivos.

### B. Estructura interna específica por agente

Cada agente organiza su definición según su función y contexto.

**Ventaja esperada:** flexibilidad y menor fricción para especialidades diferentes.

**Riesgo:** heterogeneidad difícil de inspeccionar, comparar, versionar y conectar con herramientas comunes.

### C. Modelo híbrido

Un contrato común pequeño define identidad, propósito, límites, autoridad, interfaces y referencias; cada agente puede añadir módulos internos específicos.

**Ventaja esperada:** equilibrio entre interoperabilidad y libertad de diseño.

**Riesgo:** que el núcleo crezca por acumulación y termine imponiendo una arquitectura no validada.

Estas alternativas son lentes de investigación. Ninguna queda aprobada por esta ficha.

## 3. Anatomía candidata: dimensiones a investigar

La siguiente lista es un inventario de preguntas y dimensiones candidatas, no un esquema obligatorio ni una afirmación de que cada agente deba tener un archivo separado.

| Dimensión | Qué debería aclarar | Preguntas abiertas |
|---|---|---|
| Identidad y procedencia | Quién es el agente dentro del sistema, versión y origen de su definición | ¿Qué identidad es estable y qué atributos dependen del proyecto? |
| Propósito y rol | Para qué existe y qué responsabilidad acepta | ¿Cómo evitar roles vagos o solapados? |
| Instrucciones y precedencia | Qué reglas gobiernan su conducta y cómo se resuelven conflictos | ¿Qué jerarquía debe imponer el runtime y qué solo se documenta? |
| Límites y autoridad | Qué no puede hacer, qué requiere autorización y quién puede cambiar su contrato | ¿Cómo distinguir límites declarativos de enforcement real? |
| Contexto y conocimiento | Qué fuentes puede consultar, con qué alcance y procedencia | ¿Qué información es permanente, contextual o solo de sesión? |
| Memoria y continuidad | Qué estado puede persistir, para qué y bajo qué controles | ¿Cómo separar historial, estado de ejecución y conocimiento de largo plazo? |
| Interfaces y colaboración | Cómo recibe trabajo, entrega resultados y delega | ¿Qué contratos mínimos permiten interoperabilidad sin acoplar agentes? |
| Herramientas y entorno | Qué herramientas o entornos pueden asignársele | ¿Dónde se declaran y dónde se aplican los permisos efectivos? |
| Evaluación y observabilidad | Cómo se verifica su comportamiento y se registran resultados | ¿Qué trazas son útiles sin almacenar datos innecesarios? |
| Ciclo de vida y evolución | Cómo se crea, versiona, prueba, suspende y retira | ¿Qué cambios requieren revisión o migración? |

## 4. Evidencia disponible

### 4.1 Panorama técnico externo ya registrado en Softly

La síntesis exploratoria del panorama de diseño de agentes registra que las fuentes consultadas describen componentes recurrentes como instrucciones, guardrails, herramientas, estado/memoria, orquestación, entorno y trazabilidad. También destaca la separación entre configuración del agente, runtime/harness, sesión/eventos y sandbox.

La misma síntesis advierte que estas fuentes pertenecen a proveedores, frameworks y marcos de riesgo distintos; sus abstracciones orientan la investigación, pero no prueban que exista una única arquitectura correcta para Softly.

Referencia interna: [Panorama inicial de diseño de agentes](../sources/2026-11-agent-design-landscape.md).

### 4.2 Aprendizajes documentales de TITAN

El material histórico de TITAN describe contratos por capas, roles diferenciados, canales/contextos con distintos niveles de privacidad, persistencia, leases y coordinación. Las auditorías asociadas advierten que contratos, hashes, aprobaciones o separación de directorios no equivalen por sí solos a sandbox ni a aislamiento técnico.

Por tanto, TITAN sirve como antecedente para formular preguntas sobre separación de responsabilidades, autoridad, persistencia y enforcement. No debe copiarse como arquitectura de Softly sin inspección y validación adicionales.

Referencia interna: [Material histórico TITAN y antecedente SOFA Agent](2026-11-13-material-titan-sofa-agent.md).

### 4.3 SOFA Agent y Audelin

El usuario identifica SOFA Agent como una plantilla utilizada previamente durante el desarrollo junto con Audelin. El artefacto original de SOFA Agent no está incorporado en el conjunto de fuentes registrado a la fecha de esta ficha. No se atribuye a SOFA Agent ninguna estructura concreta hasta disponer del original.

## 5. Hechos, inferencias e hipótesis

### HECHOS DOCUMENTALES

- El panorama de Softly registra modelos técnicos que separan configuración, herramientas, estado/memoria, runtime, entorno y observabilidad.
- Los antecedentes de TITAN documentan separación de roles y contratos, pero también advierten que la estructura documental no garantiza aislamiento ni autorización técnica.
- El artefacto original de SOFA Agent está pendiente de incorporación; su estructura no puede describirse con la evidencia disponible.

### INFERENCIAS

- Es útil separar la definición relativamente estable del agente de su asignación contextual a un proyecto y de la sesión concreta.
- Un contrato común podría facilitar validación e interoperabilidad, siempre que no pretenda describir exhaustivamente la estructura interna de todos los agentes.
- Los permisos deben expresarse en la definición o asignación, pero su cumplimiento debe residir en mecanismos externos al texto del agente.

### HIPÓTESIS

- Un núcleo estructural mínimo más extensiones específicas por agente podría ofrecer un equilibrio mejor que una plantilla rígida o una libertad total.
- La definición del agente debería ser portable entre proyectos, mientras que herramientas, permisos, contexto y objetivos concretos se resolverían en la asignación contextual.
- La persistencia debería modelarse por clases de información y políticas de alcance, no como una única “memoria” indiferenciada.

Estas hipótesis requieren contraste con fuentes, revisión del artefacto SOFA Agent y experimentos posteriores.

## 6. Riesgos y límites

1. **Sobrediseño temprano:** definir carpetas y archivos antes de conocer qué información necesita cada agente.
2. **Confusión entre contrato y control:** creer que declarar una prohibición impide técnicamente una acción.
3. **Acoplamiento al proveedor:** usar conceptos de un SDK como estructura universal.
4. **Memoria indiscriminada:** mezclar historial, estado operativo, preferencias, conocimiento y datos privados.
5. **Autoridad ambigua:** no distinguir quién puede modificar identidad, instrucciones, permisos o versiones.
6. **Plantilla monolítica:** convertir un formato común en una obligación de que todos los agentes tengan las mismas partes internas.
7. **Falsa continuidad:** asumir que persistir archivos equivale a mantener contexto correcto, vigente y seguro.

## 7. Conclusión provisional

La investigación favorece **explorar un contrato estructural común y pequeño, con extensiones internas específicas por agente**, sin declararlo todavía como decisión de arquitectura.

Como mínimo, el contrato candidato debería permitir identificar al agente, explicar su propósito y responsabilidades, declarar límites y autoridad, referenciar instrucciones y conocimiento, describir interfaces y señalar cómo se versiona y evalúa. No se propone aún un listado obligatorio de archivos ni directorios.

La especialidad o maestría del agente —por ejemplo, una formación avanzada en física— pertenece al brief o perfil contextual que corresponda; no es necesario fijarla en la anatomía universal. Tampoco se define aquí el nivel de capacidad: depende del modelo inicializador, herramientas, contexto y evaluación.

## 8. Decisiones

**Decisiones aprobadas por esta ficha:** ninguna.

**Criterios de trabajo ya expresados para la investigación:**
- Mantener la biblioteca de investigación como conocimiento consultable, no como instrucciones obligatorias de inicio.
- Separar investigación, arquitectura aprobada e implementación.
- Evolucionar los modelos iterativamente y conservar versiones anteriores y su procedencia.
- No inicializar ni desplegar agentes como parte de esta etapa de investigación.

## 9. Próximos pasos de investigación

1. Incorporar y analizar el archivo original de SOFA Agent, preservando su estructura y procedencia.
2. Profundizar fuentes primarias sobre anatomía, jerarquía de instrucciones, memoria, permisos, colaboración y ciclo de vida.
3. Contrastar la lista de dimensiones con agentes reales y con el modelo reutilizable v0.1 ya documentado en Softly.
4. Construir una matriz comparativa entre contrato común, estructura específica e híbrido, con criterios de interoperabilidad, seguridad, mantenibilidad, flexibilidad y coste.
5. Proponer un esquema candidato solo después de ese contraste; someterlo a revisión antes de convertirlo en especificación.

## 10. Trazabilidad

- Panorama inicial: `research/sources/2026-11-agent-design-landscape.md`.
- Material TITAN/SOFA: `research/notes/2026-11-13-material-titan-sofa-agent.md`.
- Modelo reutilizable de agentes v0.1: documentado en los commits `fd470869` y `4478e694`.
- Principio de evolución iterativa: commits `7d56d3d`, `b9dd6f0` y `edb4a0a`.

---

**Nota epistemológica:** esta ficha ordena el estado inicial de la pregunta. No constituye una investigación externa exhaustiva, una auditoría de implementaciones ni una decisión arquitectónica definitiva.
