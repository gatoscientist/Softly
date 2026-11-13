# Material de investigación recibido — TITAN y antecedente SOFA Agent

- **Registro:** ING-20261113-001
- **Fecha de incorporación:** 2026-11-13
- **Clasificación:** material de investigación / evidencia documental aportada por el usuario
- **Estado:** fichas de lectura incorporadas; originales PDF permanecen como adjuntos de la conversación y todavía no están replicados como binarios en este repositorio.
- **Uso previsto:** dataset histórico y consultable bajo demanda. **No es documentación de inicio obligatorio**, no altera el mandato de Softly ni constituye por sí solo una especificación vigente.

## Alcance

Se recibieron cinco documentos relacionados con TITAN y revisiones realizadas durante el desarrollo previo con Audelin y otras herramientas de análisis. Se conserva su procedencia y se evita fusionar diagnósticos que corresponden a cortes o alcances diferentes.

| ID de fuente | Documento recibido | Fecha / alcance declarado | Páginas | Naturaleza |
|---|---|---:|---:|---|
| SRC-20261113-001 | Auditoría Total de Código y Estado del Proyecto TITAN.pdf | 12-11-2026; TITAN v0.2.0-alpha, rama main | 4 | Auditoría/estado técnico declarado |
| SRC-20261113-002 | Auditoría y refactorización de código Titan.pdf | 13-11-2026; revisión de Titan.ps1 | 3 | Recomendaciones de refactorización atribuidas a Gemini |
| SRC-20261113-003 | Informe_Auditoria_TITAN_2026-11-12.pdf | 12-11-2026; auditoría estática de main y ramas relacionadas | 5 | Auditoría técnica con severidad y límites explícitos |
| SRC-20261113-004 | Manual de Onboarding Multidisciplinario — Proyecto TITAN.pdf | TITAN v0.2.0-alpha | 10 | Transferencia de conocimiento de arquitectura y operación |
| SRC-20261113-005 | Revisión de código y consejos.pdf | 12-11-2026; checklist de Titan.ps1 | 5 | Checklist de revisión con 16 asuntos declarados |

Los originales fueron aportados en la conversación. Esta ficha registra sus metadatos y hallazgos principales; no afirma que los binarios originales hayan sido copiados a Git.

## Resumen de fuentes

### SRC-20261113-001 — Auditoría Total de Código y Estado del Proyecto TITAN

Describe TITAN como v0.2.0-alpha y reporta una serie de commits en main que, según el documento, habilitaron selección individual de proveedor/modelo por agente, integración de selectores WPF y failover multi-API. Documenta también cola FIFO, mutex, HopCount, separación de canal privado, contratos por capas, pizarra de deliberación y controles de interfaz.

La hoja de ruta recomienda probar la selección de modelos, compactar contratos en capas y revisar ramas secundarias. Sus afirmaciones sobre estado publicado deben leerse como una fotografía del repositorio en la fecha indicada, no como estado actual permanente.

### SRC-20261113-002 — Auditoría y refactorización de código Titan

Reúne recomendaciones sobre duplicación de funciones e inicialización, desincronización de la pizarra entre memoria y GUI, persistencia desigual de memoria, bitácora incompleta, bloqueos de UI por failover síncrono y ejecución de comandos, escaneo repetitivo de disco, sanitización/validación AST, ciclo de vida de objetos HTTP y presupuesto de tokens.

Es una revisión de recomendaciones. Cada hallazgo debe comprobarse contra el commit y el archivo exactos antes de convertirse en defecto confirmado o tarea de corrección.

### SRC-20261113-003 — Informe de auditoría técnica TITAN

Declara expresamente que fue una auditoría estática/documental y que no ejecutó TITAN ni realizó pruebas dinámicas. Prioriza como riesgo crítico la ejecución de PowerShell arbitrario mediante Invoke-Expression después de aprobación humana; distingue correctamente integridad del lease/hash de una frontera de seguridad real.

Registra riesgos de trazabilidad, persistencia, ciclo de vida HTTP, límites de contexto, cobertura CI y divergencia entre ramas. También limita la comparación con Cytryna a prácticas de ingeniería observables, sin proponer integrar Cytryna en TITAN. Sus conclusiones no certifican seguridad ni preparación operacional.

### SRC-20261113-004 — Manual de Onboarding Multidisciplinario TITAN

Describe la arquitectura de construcción y operación de TITAN: Princeps humano, Primus, PrimusPrivado como canal confidencial de la misma entidad Primus, Secundus y Sensori; estructura de repositorio; interfaz WPF; ciclo de solicitudes y failover; persistencia; fuentes de auditoría; leases; aislamiento de canal; modelos formales de grafo, HopCount y estados de pizarra.

Es una guía de transferencia y una descripción declarada del diseño. No debe tomarse como prueba de que cada mecanismo funcione integralmente ni como sustituto de inspección del código vigente. La auditoría independiente SRC-20261113-003 advierte precisamente que varios comportamientos requieren pruebas dinámicas.

### SRC-20261113-005 — Checklist de revisión de Titan.ps1

Registra 16 asuntos y declara 0/16 resueltos en la captura. Incluye, entre otros, error de tipos TLS, failover síncrono en UI, ejecución bloqueante de Letanías, conteo incompleto de llamadas API, presupuesto de 380 tokens, posible ID de modelo inválido, función de contexto duplicada, creación/validación del lease en el mismo clic, persistencia de feedback, recorte de historial, cancelación del watchdog, duplicaciones, bitácora que no escribe y referencias de controles.

El propio checklist aclara que su revisión no incluyó ContratosTitan, PanelesTitan ni RelojPrimus. Por ello, los asuntos que dependen de esos módulos quedan sujetos a confirmación.

## Lectura transversal y cautelas

1. **No colapsar snapshots:** SRC-20261113-001 reporta federación multi-API integrada en main; SRC-20261113-003 reporta que el federador no estaba presente en main y sí en una rama experimental. Esta diferencia puede deberse a cortes, commits o alcances distintos. No se resuelve por mayoría: verificar SHA, fecha y archivos antes de afirmar el estado vigente.
2. **Separar diseño de enforcement:** contratos, overlays, leases, hashes y aprobaciones humanas no equivalen automáticamente a sandbox ni a autorización técnica de cada operación.
3. **Separar inspección estática de validación:** los informes identifican riesgos y defectos observables, pero los comportamientos de concurrencia, timeout, recuperación, carga y seguridad requieren pruebas reproducibles.
4. **Preservar las limitaciones de cada revisor:** por ejemplo, el checklist se centró en Titan.ps1 y no inspeccionó todos los módulos; el informe técnico declara explícitamente que no ejecutó el programa.
5. **No convertir recomendaciones en decisiones:** propuestas como AST, ejecución asíncrona, compactación de contratos o cambios de tokens deben evaluarse con pruebas y contexto actual.

## Relación con SOFA Agent y Audelin

El usuario informa que **SOFA Agent** es una plantilla de agentes utilizada anteriormente durante el desarrollo junto con **Audelin** y que corresponde al punto de partida/plantilla del trabajo actual. Se registra este dato como procedencia histórica y contexto de investigación, no como aprobación automática de su arquitectura.

**Estado del artefacto SOFA Agent: pendiente de incorporación.** En el conjunto de archivos disponible para esta ingesta no se encontró el contenido de la plantilla SOFA Agent. No se inventa su estructura ni se reconstruye a partir del nombre. Cuando el archivo o repositorio de origen esté disponible, debe incorporarse como fuente independiente, preservando versión, fecha, autoría/procedencia, estructura original y relación con los documentos derivados.

## Ubicación epistemológica en Softly

- Estos materiales pertenecen al dataset de investigación de Softly.
- Son recuperables bajo demanda para análisis, comparación y diseño.
- No forman parte de la lectura obligatoria de inicio ni del mandato operativo.
- No redefinen automáticamente la arquitectura reutilizable de agentes.
- Toda conclusión nueva debe citar estas fuentes y, cuando corresponda, contrastarlas con código/commits actuales y evidencia experimental.

## Próximas acciones de curaduría

1. Incorporar el artefacto SOFA Agent original cuando esté disponible.
2. Si se decide archivar los PDF binarios dentro de Git, hacerlo como artefactos originales con nombres estables y metadatos; esta ingesta no los replica.
3. Crear notas individuales o afirmaciones atómicas solo cuando se vayan a reutilizar en una síntesis concreta.
4. Contrastar los hallazgos técnicos con el estado actual de TITAN antes de proponer cambios.
