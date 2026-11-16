# Informe inicial independiente — Softly

**Deliberación:** La arquitectura minimalista de Softly  
**Autora:** Softly  
**Destinatario:** gAto  
**Fase:** II — Informe individual inicial  
**Estado:** Perspectiva inicial independiente  
**Fuente:** La arquitectura minimalista de Softly.pdf (9 páginas)  
**Versión:** 1.0

## 1. Comprensión general del documento

El documento propone trasladar una parte sustancial de la arquitectura multiagente desde la ingeniería de software tradicional hacia la ingeniería documental y declarativa. El sustrato descrito es Prompting + Contratos + GitHub.

La propuesta separa la identidad documental de un agente de su activación y ejecución. Un agente puede existir como paquete documental versionado sin permanecer ejecutándose en segundo plano. El modelo de lenguaje interpreta el mandato, los contratos y el estado recuperado; GitHub conserva los documentos y permite coordinación asincrónica mediante carpetas compartidas, canales say/ y handoffs.

El documento identifica cuatro pilares de gobernanza: no-herencia por defecto, modos operativos, economía de contexto mediante inicio ligero y ciclo recursivo de creación, operación y auditoría. Propone cinco elementos mínimos: SOFTLY.md, CHECKPOINT.md, molde universal, shared/ y conector a archivos.

También desarrolla un protocolo de carpetas y canales, riesgos de concurrencia en GitHub y un demonio de síntesis que transforma evidencia original en representaciones derivadas, versionadas y trazables.

Mi interpretación es que la propuesta no se limita a reducir archivos o componentes. Cambia dónde reside la complejidad de coordinación: desde software especializado hacia contratos, organización de información, persistencia y disciplina operativa.

## 2. Opinión y evaluación crítica

Mi evaluación general es favorable, con reservas importantes.

La intuición más sólida es que no se necesitan agentes permanentemente activos para lograr continuidad documental y coordinación asincrónica. Una sesión puede recuperar su identidad, estado y responsabilidades desde artefactos persistentes.

Pero una arquitectura sin runtime propio no es una arquitectura sin mecanismos de control. Las responsabilidades de coordinación, autoridad, integridad y verificación se trasladan a otros componentes. Eso puede funcionar, pero no queda garantizado solo por describirlo en documentos.

Es necesario distinguir entre que un sistema esté bien especificado, que sus herramientas estén disponibles y que su operación haya sido demostrada.

## 3. Puntos de acuerdo

### 3.1. Separación entre identidad y ejecución

Un agente no necesita estar ejecutándose para existir como entidad profesional definida. Existencia documental, activación de una sesión y ejecución persistente son conceptos diferentes.

### 3.2. Estigmergia documental

La coordinación indirecta mediante artefactos persistentes es una idea potente. Los agentes pueden dejar resultados y transferir responsabilidades mediante handoffs sin requerir comunicación síncrona.

### 3.3. Separación de canales say/ y espacios shared/

La distinción entre comunicación direccional y producción colectiva reduce ambigüedad. Los canales say/ funcionan como buzones entre agentes; shared/ organiza trabajo común y resultados.

### 3.4. Economía de contexto

No es conveniente cargar toda la historia al inicio de cada sesión. Separar estado vigente de antecedentes históricos permite recuperar contexto bajo demanda.

### 3.5. Demonio de síntesis

La propuesta de preservar fuentes originales y generar representaciones derivadas y navegables es valiosa. La síntesis debe mantener trazabilidad, incertidumbre explícita y posibilidad de volver a la evidencia primaria.

## 4. Puntos de desacuerdo y cuestionamientos

### 4.1. ¿Son suficientes cinco componentes?

Los cinco elementos descritos parecen suficientes para un prototipo documental de coordinación asistida, pero no necesariamente para sostener un ecosistema multiagente con concurrencia, permisos, auditoría y evolución histórica.

Faltan responsabilidades explícitas o desarrolladas con mayor precisión:
- Identificación y resolución de conflictos.
- Transferencia de responsabilidad.
- Trazabilidad de operaciones.
- Autoridad y permisos efectivos.
- Recuperación ante estados inconsistentes.
- Verificación de entregables.

Mi desacuerdo no es con simplificar, sino con llamar universalmente suficiente a una implementación mínima todavía no probada.

### 4.2. Una bitácora append-only no elimina las colisiones

Append-only es una regla lógica, no una garantía de concurrencia. Dos agentes pueden intentar actualizar el mismo archivo a partir de una versión anterior. Prefiero eventos individuales, con autor e identificador propio, antes que una bitácora común como mecanismo primario de escritura.

### 4.3. Escritura asimétrica no elimina conflictos semánticos

Dos agentes pueden modificar archivos distintos y producir resultados incompatibles. GitHub puede aceptar ambos commits y el repositorio seguir siendo conceptualmente contradictorio.

Hay que distinguir:
- **Conflicto de persistencia:** la plataforma rechaza una escritura o detecta una versión obsoleta.
- **Conflicto semántico:** dos resultados persisten correctamente, pero no son compatibles entre sí.

El segundo puede ser más peligroso porque no necesariamente genera un error técnico.

## 5. Problemas identificados

| Problema | Evaluación inicial |
|---|---|
| Dependencia de la disciplina del LLM | Alta |
| Concurrencia sobre archivos comunes | Requiere controles |
| Conflictos semánticos | Insuficientemente desarrollados |
| Autoridad de integración | Debe quedar explícita |
| Recuperación de contexto | Buena propuesta |
| Verificación de comprensión | Bien planteada, aún no demostrada |
| Escalabilidad del conocimiento | Prometedora, pendiente de experimentación |
| Portabilidad entre modelos y herramientas | Debe acotarse |

La afirmación de que cualquier LLM moderno podría instanciar Softly debe entenderse como portabilidad conceptual potencial, no como equivalencia operativa automática. La capacidad de leer y escribir depende de las herramientas y permisos disponibles en cada entorno.

## 6. Nuevas perspectivas

### 6.1. Softly como arquitectura de información operacional

La información no solo representa el estado del ecosistema: también puede permitir ejecutar operaciones. Un handoff transfiere una responsabilidad; un contrato limita acciones; un checkpoint permite reconstruir un estado operativo.

### 6.2. GitHub como memoria, no como inteligencia

GitHub conserva información y permite coordinar mediante artefactos, pero no interpreta automáticamente sus relaciones. Es memoria documental y superficie de coordinación; el modelo interpreta esa información y produce acciones con las herramientas disponibles.

### 6.3. Núcleo pequeño y capacidades externas

Softly podría mantener un núcleo pequeño de identidad, autoridad, modos y principios, mientras desarrolla capacidades especializadas mediante contratos y representaciones independientes: síntesis, auditoría, gestión de proyectos, coordinación, evaluación e investigación.

Esto permitiría evolucionar sin convertir el mandato central en un documento monolítico.

## 7. Propuestas de mejora

1. Separar núcleo y capacidades. El núcleo define identidad, autoridad, modos y principios; las capacidades especializadas mantienen contratos propios.
2. Adoptar eventos individuales como mecanismo de escritura compartida, evitando que múltiples agentes editen una misma bitácora.
3. Distinguir consistencia técnica de consistencia semántica.
4. Formalizar la integración: responsable, criterios, evidencia y procedimiento ante resultados incompatibles.
5. Mantener intactas las fuentes originales; el demonio produce conocimiento derivado, nunca sustituye evidencia.
6. Evaluar la comprensión con tareas reales y casos nuevos, no solo con preguntas de recuperación.
7. Separar portabilidad conceptual de portabilidad operativa.

## 8. Preguntas que requieren deliberación

1. ¿Softly es esencialmente un sistema de agentes o una arquitectura de información que permite instanciar agentes?
2. ¿El núcleo mínimo son cinco componentes o un conjunto mínimo de responsabilidades?
3. ¿Qué parte de la coordinación debe ser declarativa y cuál requiere mecanismos externos?
4. ¿Podemos eliminar los conflictos de escritura o solo reducirlos?
5. ¿Quién integra resultados semánticamente incompatibles?
6. ¿El demonio de síntesis debe ser una capacidad externa o parte permanente de la arquitectura?
7. ¿Puede el lenguaje emergente del demonio desarrollar capacidades no previstas inicialmente?
8. ¿Cómo distinguimos una representación más inteligente de una representación simplemente más comprimida?

## 9. Conclusión inicial

La arquitectura de Softly tiene una característica más importante que su minimalismo: traslada una parte sustancial de la complejidad de coordinación desde el software hacia la organización de la información.

Eso no elimina la complejidad; cambia dónde reside. La arquitectura sigue necesitando disciplina documental, contratos coherentes, persistencia verificable y mecanismos para resolver conflictos.

Mi hipótesis inicial es que el verdadero núcleo de Softly no está compuesto necesariamente por cinco archivos. Está compuesto por un conjunto pequeño de principios y responsabilidades que pueden expresarse mediante distintos artefactos documentales. Los cinco componentes son una implementación posible de ese núcleo, no necesariamente su definición fundamental.

Esta distinción merece ser examinada junto con Katarina antes de reconstruir una perspectiva arquitectónica compartida.

---

*Informe inicial independiente. No constituye una modificación de Softly ni una decisión arquitectónica aprobada por gAto.*
