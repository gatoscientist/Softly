# Bitácora del laboratorio

La bitácora conserva eventos de trabajo, no conclusiones implícitas.

## Archivos

- `activity.jsonl`: acciones y eventos relevantes.
- `decisions.jsonl`: referencias a decisiones formales.
- [Registro de directiva de identidad y cierre de sesión (2026-11-13)](2026-11-13-identity-directive-and-thread-closure.md): antecedente de gobernanza; consultar junto con los documentos normativos vigentes.
- `incidents.jsonl`: registro de incidencias, evidencias, causas y acciones correctivas. Distingue hechos verificados de reportes aún no auditados.
- [INC-20261116-002 — uso de apelativo distinto de la identidad directiva](2026-11-16-incidencia-uso-de-apelativo-wachito.md): Softly se dirigió a gAto como «Wachito»; hecho registrado a petición explícita de gAto.
- `observations.jsonl`: registro estructurado de observaciones aún no clasificadas como incidencias.
- [OBS-20261116-004](../observations/OBS-20261116-004-confusion-repositorio-rutas-creacion-katarina-titan.md): confusión de repositorio durante la creación de Katarina para TITAN.
- [INC-20261116-003](2026-11-16-incidencia-creacion-katarina-repositorio-equivocado.md): creación inicial en repositorio equivocado; ubicación corregida y verificada, prevención pendiente.
- `threads/`: historia documental de cada hilo de conversación cerrado ([índice de hilos](threads/README.md)).
- `derived/`: notas intermedias o derivados de análisis que no sustituyen transcripciones ni cierres de hilo ([índice de derivados](derived/README.md)).
- `maintenance/`: registros de mantenimiento documental, seguimiento de hallazgos y verificación de cambios. Ver el [índice de mantenimiento](maintenance/README.md), la [bitácora de orden de la casita](maintenance/housekeeping-log.md) y el [seguimiento de auditorías 2026-11-14](maintenance/2026-11-14-audit-follow-up.md).

## Conservación obligatoria de hilos

Cada hilo que gAto dé por cerrado debe guardarse como un archivo Markdown independiente dentro de `logs/threads/`. No se archivan solo los hilos que produjeron código o decisiones: se conserva cada hilo cerrado para que su historia pueda consultarse más adelante.

El objetivo es preservar la historia, no garantizar una transcripción literal perfecta. El registro debe incluir el propósito, los temas tratados, la secuencia y evolución de la conversación, instrucciones relevantes, decisiones, correcciones, acciones realizadas, archivos y commits, errores, pendientes y punto de continuidad. Se incorporan citas literales cuando estén disponibles y se identifican explícitamente los resúmenes o reconstrucciones.

No es requisito recuperar el 100 % de los mensajes. Sí es obligatorio no inventar intervenciones, hechos, fechas, resultados ni razonamientos privados. Se deben señalar los vacíos y las limitaciones de recuperación. No incluir cadena de pensamiento privada; conservar el proceso observable y las razones comunicadas.

### Convención de nombres

Usar:

`hilo I YYYY-MM-DD HH-mm F YYYY-MM-DD HH-mm.md`

Las horas corresponden a America/Santiago. Si no se conoce una hora exacta, usar `hora-no-registrada` en ese segmento del nombre y declararlo dentro del archivo. No estimar horas.

### Verificación antes de cerrar

- Crear el archivo en `logs/threads/`.
- Comprobar que el contenido y la ruta son correctos.
- Realizar el commit en Git.
- Verificar que el commit se completó y que el archivo quedó persistido.
- Solo entonces declarar que el hilo está archivado. Si algo falla, informar que sigue pendiente.

### Consulta

Los archivos se conservan para consulta bajo demanda. No existe obligación de leer todos los hilos al iniciar una nueva conversación. Al abrir un hilo nuevo se recupera el mandato y el checkpoint vigente; el historial conversacional se consulta cuando gAto lo solicita o cuando un antecedente específico lo hace necesario.

El archivo del hilo es historia documental; el checkpoint es una síntesis operativa para retomar el trabajo. Uno no reemplaza al otro.

## Reglas generales de la bitácora

- Una línea JSON por evento en los archivos JSONL.
- Fecha ISO 8601 con zona horaria.
- ID único y tipo de evento.
- Enlaces a artefactos, no duplicados extensos.
- Nunca registrar secretos ni conversaciones completas que contengan datos privados innecesarios.
- Corregir mediante evento nuevo; no reescribir historia sin dejar rastro.

La bitácora es trazabilidad documental. No es un sistema inmutable ni una garantía criptográfica.


## «Guarda esta incidencia» y «Cierra el Hilo»

Para cada agente persistente, salvo Softly misma para el registro de incidencias, la captura debe conservar hilo observable, JSONL, hilo, bitácora, índices, commit verificado y relectura. Softly está excluida de este comando para su propio registro; los demás agentes deben disponer de logs y bitácora propios. «Cierra el Hilo» aplica también a Softly: recuperar compromisos, completar y persistir, verificar commits/pruebas y realizar dos revisiones finales independientes antes de declarar el cierre. La orden de incidencia no crea una tarea correctiva ni reemplaza el cierre; cerrar un hilo no borra registros.

La documentación no significa que el runtime implemente estas operaciones. Registrar evidencia observable sin secretos, cadena de pensamiento privada ni datos personales innecesarios. Si persistencia o verificación no pueden demostrarse, informar el bloqueo.
