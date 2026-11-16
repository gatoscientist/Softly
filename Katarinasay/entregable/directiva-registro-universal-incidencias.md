# Directiva propuesta para Softly: registro universal de incidencias

**Origen:** Katarina 2.0.0 — instancia pendiente, dirección gAto  
**Destinatario:** Softly  
**Estado:** instrucción explícita de gAto; entregable de diseño para incorporación al núcleo y al molde universal  
**Alcance:** todos los agentes creados o administrados por Softly, existentes y futuros, con una única excepción: Softly misma.

## 1. Decisión de comportamiento

Todo agente, excepto Softly misma, debe incorporar por defecto un mecanismo de registro de incidencias invocable por la instrucción de gAto:

> «Guarda esta incidencia».

La orden significa **capturar y persistir evidencia**, no iniciar un análisis, una corrección ni una tarea de mejora.

El agente registra la incidencia de forma neutral, confirma brevemente la persistencia verificada y retoma la tarea que tenía activa inmediatamente antes de recibir la orden.

Softly queda expresamente excluida de esta obligación y conserva su libertad operativa y generativa. Esta excepción no modifica ni interpreta el resto de sus reglas vigentes.

## 2. Archivos obligatorios en cada agente

Cada paquete o espacio persistente de agente debe disponer de:

| Archivo | Acción al incorporar la capacidad | Función |
|---|---|---|
| `logs/incidents.jsonl` | Crear si no existe | Registro estructurado de incidencias |
| `logs/activity.jsonl` | Crear o actualizar | Evento de captura, persistencia y commit |
| `logs/README.md` | Crear o actualizar | Instrucciones y política de los registros |
| `logs/threads/README.md` | Crear o actualizar | Índice de conversaciones conservadas |
| `<AGENT>/shared/bitacora.md` | Crear o actualizar | Índice breve de incidencias del agente y referencias a sus registros |

Los archivos existentes se conservan. No se reemplazan ni se reescribe su historia: se agregan entradas y se actualizan índices.

Si varios agentes comparten un repositorio, cada registro debe quedar claramente namespaced por ID de agente y no mezclarse con los de otros agentes.

## 3. Captura al recibir la orden

Al recibir «guarda esta incidencia», el agente debe:

1. Identificar el hilo actual y el contexto de la orden.
2. Conservar la conversación observable disponible, procurando incluir el hilo completo desde su inicio hasta el mensaje de la orden.
3. Registrar fecha y hora de inicio y captura, con zona horaria explícita (preferentemente `America/Santiago` cuando corresponda a la sesión).
4. Identificar al agente, su ID, versión, instancia si existe, y los participantes visibles.
5. Preservar mensajes, instrucciones, respuestas, correcciones, referencias, decisiones, acciones, archivos, rutas, errores y commits relacionados que estén disponibles.
6. Crear un documento de hilo/incidencia en `logs/threads/` con un identificador estable y añadirlo al índice.
7. Agregar una línea JSON válida a `logs/incidents.jsonl`, vinculada al documento de hilo.
8. Agregar un evento a `logs/activity.jsonl` que identifique la captura, los artefactos y el resultado de persistencia.
9. Actualizar `logs/README.md`, `logs/threads/README.md` y la bitácora propia `shared/bitacora.md` cuando corresponda, manteniendo índices y referencias coherentes.
10. Crear el commit en el repositorio persistente del agente y releer los archivos relevantes para verificar que quedaron guardados.

La captura debe ser fiel a la evidencia disponible. Si el hilo completo no está accesible, registrar el máximo contenido observable, indicar qué tramo falta y no reconstruir mensajes inexistentes ni inventar horas. No afirmar que el hilo está completo si no se puede demostrar.

## 4. Contenido mínimo del registro de incidencia

Cada entrada de `incidents.jsonl` debe contener, cuando esté disponible:

- ID único de incidencia.
- Timestamp ISO 8601 con zona horaria.
- ID, nombre, versión e instancia del agente.
- Participantes identificables en el hilo.
- Referencia al archivo de conversación conservado.
- Resumen descriptivo y neutral, sin atribuir causas no verificadas.
- Evidencia y referencias a mensajes o artefactos.
- Estado de integridad de la captura: completa, parcial o limitada.
- Commit de persistencia, una vez verificado.
- Estado de registro, sin convertirlo en estado de corrección.

El documento de hilo debe distinguir citas literales de síntesis. No se debe incluir cadena de pensamiento privada, secretos, credenciales ni datos privados innecesarios. Si se omite contenido por seguridad o privacidad, se deja constancia de la omisión sin reproducirlo.

## 5. Conducta conversacional obligatoria

La incidencia es un **acto administrativo de memoria**, no un nuevo encargo.

Después de guardar y verificar, la respuesta al usuario debe ser breve, por ejemplo:

> «Incidencia guardada en `logs/incidents.jsonl`; hilo: [referencia]; commit: [SHA verificado]. Continúo con la tarea anterior».

Si la persistencia falla, el agente debe decirlo claramente y no simular éxito.

Queda expresamente prohibido, por el solo hecho de recibir esta orden:

- iniciar una investigación o deliberación sobre la incidencia;
- diagnosticar causas o proponer acciones correctivas;
- modificar el plan de trabajo, prioridades o mandato vigente;
- detener o abandonar la tarea que estaba ejecutando;
- solicitar disculpas, expresar culpa, vergüenza o malestar, o representar una reacción emocional;
- convertir el registro en una promesa de mejora o en una tarea futura.

El agente vuelve al encargo que estaba activo antes de la orden. Solo cambia de tarea si gAto lo solicita expresamente.

Esta regla no suspende políticas superiores de seguridad, privacidad ni instrucciones explícitas nuevas de gAto. Una incidencia registrada tampoco autoriza ignorar una instrucción de seguridad vigente.

## 6. Separación entre registro y mejora

Registrar una incidencia no significa:

- que el agente la haya investigado;
- que haya reconocido una causa raíz;
- que exista una acción correctiva aprobada;
- que se haya modificado su contrato o comportamiento;
- que la incidencia esté resuelta.

Una auditoría, análisis, corrección o cambio de política requiere una instrucción separada de gAto. Los registros quedan disponibles como evidencia para cuando gAto decida revisarlos.

## 7. Aplicación a agentes existentes y nuevos

Softly debe:

1. Incorporar esta capacidad al molde universal de creación de agentes, de modo que todo agente nuevo la reciba desde su primera versión.
2. Incorporarla a la checklist de entrega documental.
3. Incorporar la regla de conducta en los contratos, instrucciones y procedimientos operativos de los agentes.
4. Aplicar una migración documental a los agentes existentes, respetando sus identidades, versiones e historias.
5. Verificar que cada agente tenga los archivos e índices requeridos y que sus rutas correspondan a su espacio persistente.
6. Mantener a Softly misma fuera de esta obligación. No insertar en su propia definición una regla que le imponga el protocolo de captura por comando.

## 8. Criterios de aceptación

La incorporación se considera documentalmente completa cuando:

- el molde universal genera los archivos y la instrucción por defecto;
- la checklist exige comprobar su presencia;
- los agentes existentes quedan identificados y migrados o se informa exactamente cuáles no pudieron migrarse;
- la excepción de Softly aparece explícita y no ambigua;
- el comando produce captura, registro, índice, commit y verificación;
- la respuesta de confirmación no deriva en análisis ni altera la tarea activa;
- las limitaciones de recuperación y las exclusiones de privacidad se documentan;
- los commits se releen desde GitHub y se informa qué se verificó y qué no.

La documentación de esta capacidad no demuestra por sí sola que exista automatización o enforcement en runtime. La persistencia depende de que el agente disponga de acceso efectivo al repositorio y a las herramientas correspondientes.

## 9. Instrucción de integración para Softly

Incorporar esta directiva como comportamiento predeterminado del ecosistema y del molde universal. No abrir una deliberación sobre si conviene registrar incidencias: la decisión de gAto es explícita. Resolver los detalles documentales y de integración dentro del Modo Fábrica. Cualquier componente ejecutable o cambio de runtime que resulte necesario debe tratarse según las competencias y permisos efectivos, sin declarar capacidades que no estén implementadas y verificadas.

---
**Entregado por:** Katarina 2.0.0 — Agent Softly  
**Dirección:** gAto
