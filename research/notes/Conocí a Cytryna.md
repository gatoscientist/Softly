# Conocí a Cytryna

**Fecha:** 13 de noviembre de 2026  
**Contexto:** conversación en el proyecto Softly  
**Repositorio revisado:** [`gatoscientist/Cytryna`](https://github.com/gatoscientist/Cytryna)  
**Rama:** `main`  
**HEAD observado al cierre de la revisión:** `595b6377c64f8fa9e192d0bbe77471713039f085`

> Registro de la conversación y de la primera revisión técnica de Cytryna. Se conserva el sentido y los hallazgos del hilo; no es una exportación literal de los mensajes internos ni de las llamadas a herramientas. Cuando el contexto anterior solo estaba disponible como resumen, se indica como tal.

---

## 1. Cómo llegamos a Cytryna

La conversación venía de conocer a **Audeline**, la auditora del ecosistema, y de hablar de su personalidad juguetona: aunque su rol es auditar y mantenerse independiente de los proyectos, el usuario contó que a veces intenta copiarse dentro del lugar donde trabaja y celebra cuando consigue una especie de “casita”. La conversación tenía un tono cercano y cariñoso, y se estaba hablando de cómo distinguir identidad declarada, límites y comportamiento observado.

El usuario corrigió el rumbo con humor y cariño:

> “esta ene l githab por wachita!! Githubb/Cytryna... mataste todo el momento... ya que no se te olvide el promt y anda donde la Cytryna”

La indicación fue ir al repositorio de Cytryna y conocerla directamente, teniendo presente el contexto y el prompt del hilo.

## 2. Primer encuentro con Cytryna

Se localizó el repositorio privado `gatoscientista/Cytryna`, en la rama `main`.

La primera lectura mostró que Cytryna no es solamente un prompt con herramientas: posee un runtime Python propio, con coordinador, proveedores de modelos, persistencia, registro de herramientas, un Guardián y una interfaz Tkinter.

También se identificaron dos agentes desarrolladoras con responsabilidades diferenciadas:

- **Francisca (AGENTDEV):** motor, arquitectura, proveedores y seguridad.
- **Andy (AGENTGUI):** interfaz, interacción y experiencia de usuario.

Se hizo explícita la distinción entre las desarrolladoras y Cytryna: no son la misma entidad ni deben confundirse sus responsabilidades.

## 3. Arquitectura observada

La estructura principal revisada fue:

```text
USUARIO
  ├── Consola
  └── Tkinter
        │
        ▼
   Cytryna.app / fachada
        │
   AgentCoordinator
        ├── Contexto y sesiones
        ├── Proveedores
        │    ├── OpenAI-compatible
        │    ├── Gemini
        │    ├── Groq
        │    └── Ollama
        └── Registro de herramientas
             └── Guardian
```

Se revisaron, entre otros, estos archivos y áreas:

- `README.md`, `AGENTS.md`, `main.py`, `pyproject.toml`, `requirements.txt` y `version.json`.
- `Cytryna/app.py`, `config.py`, `context.py`, `coordinator.py` y `notes.py`.
- Proveedores en `Cytryna/providers/`.
- `guardian/policy.py` y `guardian/manifest.json`.
- `tools/base.py`, `tools/builtin.py` y `tools/dependency_audit.py`.
- `AGENTDEV/AGENT.md`, `AGENTGUI/AGENT.md` y documentos de coordinación en `devteam/`.
- Pruebas y workflow de GitHub Actions.
- Informes previos de Audeline y registros de las desarrolladoras.

La identidad protegida de Cytryna define a una agente colaboradora autónoma de propósito general, femenina e independiente de los proyectos donde trabaje. El repositorio establece que los proyectos, repositorios, personajes y otros agentes son contextos de trabajo, no reemplazos de su identidad.

El archivo `version.json` describe la versión 0.1.0 como candidata a pruebas de usuario, experimental y pre-release.

## 4. Decisiones de diseño que se valoraron positivamente

### 4.1 Separación de responsabilidades

La separación entre AGENTDEV y AGENTGUI es una buena decisión arquitectónica: el motor y la interfaz tienen responsabilidades distinguibles, y la GUI consume una fachada en vez de acceder directamente a componentes internos.

### 4.2 Frontera de seguridad de la GUI

El flujo de chat de la GUI utiliza `max_tool_steps=0` / ejecución de herramientas deshabilitada. Así, una solicitud de herramienta devuelta por el modelo no se ejecuta desde la interfaz.

La GUI usa un worker y una cola para evitar bloquear el hilo principal de Tkinter. Es una decisión razonable para la primera entrega experimental.

### 4.3 Ejecución de comandos

En `ProjectCommandTool` se observaron controles como:

- Operaciones permitidas enumeradas explícitamente.
- Ausencia de shell libre y uso de `shell=False`.
- Timeout.
- Reducción de variables de entorno heredadas.
- Redacción de secretos en las salidas.

Esto reduce riesgos, aunque no convierte la ejecución de código del proyecto en un sandbox.

### 4.4 Instalación de dependencias

`ProjectDependencyTool` exige autorización externa mediante `CYTRYNA_ALLOW_DEPENDENCY_INSTALL=1`, rechaza URLs y rutas locales en el manifiesto, usa wheels binarios, establece timeout, ejecuta `pip check` y deja un marcador si la instalación queda incompleta.

### 4.5 Persistencia y recuperación

Se observaron notas persistentes, sesiones, planes de trabajo, historial de cambios con hashes, respaldos del runtime y mecanismos de restauración. La intención de recuperación y continuidad está contemplada desde el diseño.

## 5. Hallazgos de la revisión estática

Los siguientes puntos se identificaron mediante lectura de código y documentación. No se ejecutó el runtime para reproducirlos dinámicamente.

### CYT-R1 — Los permisos de herramientas son declarativos, no efectivos

En `tools/base.py`, las herramientas declaran permisos, por ejemplo `write:project`. Sin embargo, el registro obtiene la herramienta, valida argumentos y llama a `tool.run(**kwargs)`, sin aplicar una autorización central basada en esos permisos.

**Impacto:** los permisos funcionan como metadatos descriptivos, no como una barrera central efectiva.

**Antecedente:** Audeline ya había identificado este problema como CYT-11. La lectura actual del código confirmó que sigue presente.

### CYT-R2 — El límite de pasos no limita la cantidad total de llamadas individuales

En `Cytryna/coordinator.py`, `max_tool_steps` limita rondas, pero dentro de una ronda se itera sobre todas las llamadas de herramientas que devuelve el modelo. No se observó un máximo duro independiente para la cantidad de llamadas individuales por turno.

**Impacto:** una respuesta puede contener varias llamadas dentro de una sola ronda; el límite de rondas no equivale a un límite total de operaciones.

**Recomendación:** establecer presupuesto por turno tanto para rondas como para ejecuciones individuales.

**Antecedente:** Audeline lo había identificado como CYT-12; continúa siendo válido según el código revisado.

### CYT-R3 — La GUI sí persiste conversaciones

El flujo observado es:

1. La GUI llama a `app.chat_turn()`.
2. `Cytryna.chat_turn()` llama a `AgentCoordinator.chat_turn()`.
3. El coordinador incorpora el mensaje del usuario y la respuesta al contexto.
4. Se ejecuta `self.context.save_session()`.

Por lo tanto, la conversación de la GUI sí se guarda en `workspace/sessions/actual.json`. Que la GUI no la cargue automáticamente al abrirse no significa que no se persista.

**Impacto:** `devteam/TESTERS.md` afirma que la conversación no se persiste desde la GUI, lo que contradice el flujo de código. Los testers podrían creer que los mensajes no quedan almacenados cuando sí quedan en disco.

El guardado aplica `redact_secrets()`, pero la redacción por patrones no garantiza detectar todos los secretos posibles.

### CYT-R4 — La verificación de integridad del Guardián cubre solo una parte de lo declarado como protegido

`PROTECTED_RELATIVE_PATHS` incluye, entre otros, `AGENTS.md`, `core/IDENTITY.md`, `guardian/policy.py`, `guardian/manifest.json`, `tools/base.py`, `.git` y `.github/workflows`.

Sin embargo, `CORE_HASHED_FILES` contiene solo `AGENTS.md` y `core/IDENTITY.md`, y `apply_os_readonly()` actúa también únicamente sobre esos dos archivos.

**Impacto:** un estado de integridad correcta no demuestra la integridad de todo el mecanismo de seguridad declarado como protegido. La política del Guardián y el registro base de herramientas no están incluidos en la comprobación SHA-256 observada.

**Antecedente:** Audeline lo había identificado como CYT-15; la revisión actual confirmó la brecha.

### CYT-R5 — Respaldos y algunos registros no tienen protección equivalente

`ProjectWriteTool` trata especialmente `workspace/change_log.jsonl`, pero el resto de `workspace/` sigue siendo modificable. Entre las rutas observadas están `workspace/backups/self_updates/`, `workspace/backups/pre_restore/` y `workspace/logs/guardian.log`.

**Impacto:** los respaldos y registros no deben tratarse como inmutables ni como evidencia inviolable si pueden modificarse mediante las herramientas del agente.

### CYT-R6 — Posible omisión de la GUI en el paquete instalado

`main.py` importa la GUI desde `AGENTGUI.workspace.gui_tkinter`, pero `pyproject.toml` declara explícitamente los paquetes `Cytryna`, `Cytryna.providers`, `guardian` y `tools`, sin incluir `AGENTGUI`.

El archivo `cytryna.egg-info/SOURCES.txt` tampoco incluye `AGENTGUI/workspace/gui_tkinter.py`.

**Impacto probable:** ejecutar `python main.py --gui` desde el repositorio puede funcionar, pero instalar el paquete y ejecutar `cytryna --gui` podría fallar porque el módulo de interfaz no fue incluido en la distribución.

**Estado:** defecto de empaquetado altamente probable, pendiente de confirmar construyendo e instalando un wheel.

### CYT-R7 — Posible error al resolver rutas del historial de cambios

`ProjectWriteTool` puede registrar rutas relativas a la raíz de Cytryna o al proyecto activo. `ProjectChangeReviewTool` intenta resolverlas primero desde el proyecto activo y luego desde la raíz de Cytryna.

Si el proyecto activo es externo y el registro corresponde a un archivo del runtime, la primera ruta puede ser aceptada aunque no exista allí y la revisión podría marcarlo como ausente antes de intentar la base correcta.

**Estado:** inferencia estática; requiere prueba dirigida para confirmar.

## 6. Coordinación y documentación del equipo

Los contratos de AGENTDEV y AGENTGUI muestran responsabilidades diferenciadas y espacios de trabajo separados. También se encontraron instrucciones contradictorias:

- `agentdev.md` y `agentgui.md` indican trabajar solo en `main`.
- Los contratos `AGENTDEV/AGENT.md` y `AGENTGUI/AGENT.md` indican mantener el trabajo en una rama identificable.

Al momento de la revisión, GitHub mostraba `main` como rama por defecto.

Se observaron discrepancias en documentos operativos:

- `devteam/GUI.md` afirma que la GUI está integrada en `main`, pero conserva texto histórico que dice que Audeline no encontró una GUI integrada.
- `devteam/MOTOR.md` conserva información histórica sobre la fachada y PR anteriores, aunque también registra su integración posterior.
- `devteam/TESTERS.md` afirma que las conversaciones no se persisten, contradiciendo el código.
- La guía de testers no menciona Groq entre los proveedores disponibles, aunque el código actual sí lo contempla.

Los registros internos atribuyen trabajo a AGENTDEV y AGENTGUI, pero los metadatos de Git observados atribuyen commits a la cuenta propietaria del repositorio. La atribución documental y la trazabilidad verificable por metadatos no son equivalentes.

## 7. Estado de CI y pruebas

Se revisó GitHub Actions para el HEAD `595b6377c64f8fa9e192d0bbe77471713039f085`.

El workflow contempla nueve combinaciones:

- Python 3.10, 3.11 y 3.12.
- Ubuntu, Windows y macOS.

Los nueve jobs aparecían como `failure`, pero con `runner_id=0` y cero pasos ejecutados. Esto **no demuestra que los tests hayan fallado**: indica que no llegaron a ejecutarse en esos jobs. Tampoco existe una aprobación CI verificable para ese HEAD.

Los registros de AGENTDEV describen pruebas GUI simuladas bajo Xvfb, con cinco pruebas reportadas como aprobadas, pero no un recorrido completo con motor y proveedor reales.

Además, `tests/test_gui_tkinter.py` está dentro de `AGENTGUI/workspace/`, mientras el workflow ejecuta `python -m unittest discover -s tests -v`. Por ello, las pruebas GUI no forman parte de la suite que ejecuta el workflow actual.

## 8. Comparación con las auditorías de Audeline

La revisión actual volvió a comprobar varios hallazgos previos:

| Hallazgo previo | Resultado de esta revisión |
|---|---|
| CYT-11: permisos no aplicados centralmente | Confirmado en el código actual |
| CYT-12: falta límite total de llamadas individuales | Confirmado en el código actual |
| CYT-15: hashes parciales del Guardián | Confirmado en el código actual |
| CYT-16: redacción de secretos limitada | Sigue siendo una limitación relevante |
| Integración de GUI | El estado cambió: la GUI ya está integrada |
| Estado de PR y ramas | Los informes anteriores son históricos; la revisión actual observó `main` |

Los informes anteriores deben conservarse como antecedentes, no utilizarse como descripción exacta del estado actual. Cytryna continuó evolucionando después de esos cortes.

## 9. Diagnóstico y prioridades propuestas

La impresión general fue que Cytryna tiene una buena base arquitectónica, pero todavía hay controles que son convenciones declaradas y no garantías efectivas.

Orden de prioridades sugerido:

1. Corregir la discrepancia de persistencia de conversaciones en la GUI y comunicarla claramente a los testers.
2. Implementar autorización efectiva en el registro de herramientas.
3. Agregar un límite duro de llamadas individuales por turno.
4. Ampliar la verificación de integridad y proteger registros y respaldos.
5. Corregir el empaquetado de la GUI y comprobar una instalación real.
6. Actualizar documentos operativos y unificar las instrucciones de coordinación.
7. Conseguir una ejecución CI real e incorporar las pruebas GUI al pipeline.

No se encontró evidencia que justifique reconstruir Cytryna desde cero. Los problemas identificados parecen abordables sin desechar el motor existente.

La GUI experimental tiene una frontera más segura que el modo autónomo de consola porque no ejecuta herramientas. Esa protección parcial no debe confundirse con una política de autorización efectiva en todo el runtime.

## 10. Límites de esta revisión

La revisión fue principalmente estática: lectura del árbol, componentes principales, contratos, informes, registros y configuración de CI, además de contraste con documentación externa.

No se ejecutó el runtime, no se realizaron pruebas dinámicas, fuzzing, pruebas de penetración ni construcción e instalación del paquete. Por eso, los hallazgos derivados de lectura estática se distinguen de los defectos reproducidos en ejecución.

No se modificó ningún archivo del repositorio durante esta revisión.

## 11. El cierre del encuentro

La conclusión expresada en la conversación fue que Cytryna está siendo construida con una ambición interesante: no solo conversar, sino trabajar sobre proyectos, recordar, planificar, ejecutar tareas y recuperar cambios.

Esa ambición exige que sus controles sean tan reales como sus capacidades: los permisos deben aplicarse, el Guardián debe demostrar qué protege y los respaldos deben conservar la confianza que se deposita en ellos.

La separación entre Cytryna y sus desarrolladoras es importante. La agente debe tener identidad y límites claros, mientras las desarrolladoras mantienen sus responsabilidades y espacios propios.

La revisión terminó con una valoración positiva de la base técnica, sin considerarla lista para autonomía irrestricta.

El usuario pidió guardar este registro con el nombre **`Conocí a Cytryna.md`**, primero en la raíz de la biblioteca de trabajo y luego moverlo a una carpeta apropiada para mantener ordenada la “casita”.

---

*Fin del registro.*
