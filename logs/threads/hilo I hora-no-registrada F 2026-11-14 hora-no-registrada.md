# Hilo de trabajo — continuidad y mantenimiento de Softly

- **Inicio:** hora no registrada en el contexto disponible.
- **Cierre:** 2026-11-14; hora no registrada.
- **Responsable humano:** gAto.
- **Agente:** Softly.
- **Repositorio:** `gatoscientist/Softly`, rama `main`.
- **Tipo de registro:** transcripción de mensajes visibles y bitácora de acciones observables.
- **Límite de fidelidad:** este archivo conserva el contenido visible de los mensajes del hilo y resume las operaciones técnicas verificables. No incluye razonamiento privado interno ni pretende reproducir tokens o mensajes internos de herramientas como si fueran conversación visible.

## 1. Inicio y objetivo

**gAto:** «Sigue con esas tareas».

El trabajo continúa el plan de mantenimiento autónomo priorizado en la conversación anterior: consolidar integridad documental de Softly, reconciliar inventario e índices, revisar procedencia y enlaces, preservar materiales sin borrados, y mantener en pausa el desarrollo de agentes hasta cerrar la fase de mejoras.

## 2. Inventario recursivo inicial

Se consultó el árbol recursivo de `main` en GitHub. La primera fotografía arrojó 124 entradas, 90 archivos y 34 directorios, con respuesta no truncada. El análisis posterior identificó archivos Markdown, README, PDF y estructuras de directorios.

Se compararon SHA de blobs y rutas. Se identificó la colisión de capitalización conocida entre:

- `eL aRenero del gAto/`
- `eL arenero del gAto/`

No se fusionaron ni renombraron. La diferencia se conserva hasta contar con una decisión respaldada.

Se identificaron seis directorios que contienen únicamente README y que representan scaffolding preparado para evaluaciones y experimentos. Se conservaron; no se trataron como basura.

## 3. Primeras correcciones de navegación y estado

Se actualizaron los siguientes documentos:

- `README.md`: se alineó la prioridad del repositorio con la integridad y funcionamiento documental de Softly, dejando el desarrollo de agentes en pausa hasta que gAto confirme el cierre de esta fase.
- `logs/README.md`: se aclaró que `incidents.jsonl` y `observations.jsonl` no existen todavía; no se presentan como archivos disponibles.
- `experiments/README.md`: se corrigió la referencia a un directorio `artifacts/` que no existía.
- `archive/README.md`: se enlazó el hilo histórico de Audelin.
- `research/README.md`: se enlazó la bibliografía.
- `eL arenero del gAto/README.md`: se corrigió la afirmación histórica sobre dos registros de Biblioteca de Auditoría TITAN. El inventario actual consultado mostraba un solo registro de Biblioteca, de 314.786 bytes. La coincidencia de tamaño con el PDF del arenero no demuestra identidad binaria.

Se amplió la matriz de procedencia y respaldo y la bitácora de mantenimiento.

## 4. Auditoría de enlaces locales

Se revisaron los enlaces Markdown inline relativos de los archivos Markdown del árbol. En el corte de 77 archivos Markdown, la comprobación encontró cero destinos locales rotos.

Se excluyeron de esa validación las URLs externas y las dependencias semánticas no expresadas como enlaces. La cobertura y sus límites quedaron documentados.

## 5. Recuperación de trazabilidad: ADR-0001

La revisión de `logs/decisions.jsonl` encontró una decisión aceptada `ADR-0001` sin archivo formal correspondiente en `decisions/`.

Se reconstruyó:

`decisions/ADR-0001-laboratorio-documental-antes-de-runtime.md`

La reconstrucción utilizó los campos existentes en el registro JSONL: fecha, estado, contexto, decisión, rationale, condición de revisión y commit relacionado. El documento declara explícitamente su procedencia y que es una reconstrucción. No se inventó contenido adicional.

Se enlazó la ADR desde `decisions/README.md`.

## 6. Índices de artefactos

Se conectaron documentos que no estaban enlazados desde los índices correspondientes:

- Perfil Audelin desde `agents/profiles/README.md`.
- Plantilla ADR desde `decisions/README.md`.
- Derivado Hiloderivado desde `logs/derived/README.md`.
- Plantilla de observación desde `observations/README.md`.
- Esquema JSON de investigación desde un nuevo `schemas/README.md`.
- Hilo histórico de Audelin, registro de identidad y bibliografía desde sus respectivos índices.

Después se completó la navegación de directorios:

- El mapa de `README.md` enlaza los índices de directorios principales.
- `agents/README.md` enlaza el índice de perfiles.
- `evaluations/README.md` enlaza datasets, planes y ejecuciones.
- `experiments/README.md` enlaza protocolos, resultados y casos.

Los seis subdirectorios de evaluaciones y experimentos que solo contienen README quedaron descritos explícitamente como estructuras preparadas sin artefactos registrados.

## 7. Verificación de referencias externas

Se extrajeron 14 URLs únicas de `research/bibliography.md` y `research/sources/2026-11-agent-design-landscape.md`. Doce resolvieron directamente. Se actualizaron dos referencias oficiales:

- OWASP Agentic Top 10: se sustituyó la ruta antigua que no resolvía por la página oficial vigente.
- LangGraph Persistence: se sustituyó la ruta heredada por la documentación oficial actual en `docs.langchain.com`.

Los enlaces se actualizaron tanto en la bibliografía como en la ficha de panorama. Se mantuvo la advertencia de que la guía Anthropic de 2024 es útil como referencia conceptual, pero parte de su panorama de tooling puede haber cambiado.

El alcance de esa comprobación fue esas 14 URLs, no todos los enlaces externos del repositorio.

## 8. Inspección binaria pendiente

Se intentó recuperar e inspeccionar los nueve PDF del arenero. GitHub permitió consultar metadatos y contenido codificado, pero el entorno disponible no permitió materializar los bytes para inspección interna y comparación binaria con respaldos independientes.

La Biblioteca expuso texto indexado de un único PDF de Auditoría TITAN; eso no permite comparar el binario con el del repositorio. Los nueve PDF siguen pendientes de inspección interna.

Se recomendó a gAto adjuntar los nueve PDF o un ZIP para poder:
1. leerlos;
2. calcular hashes;
3. comparar contenidos y versiones;
4. identificar duplicados reales;
5. comprobar respaldos;
6. preparar una propuesta de limpieza segura.

No se eliminó ningún archivo. No se declaró inspección binaria completa.

## 9. Naturaleza del repositorio

La revisión confirmó que Softly es un laboratorio documental y de investigación, no un runtime. El árbol consultado no contiene código ejecutable ni workflows de CI. Por ello, esta pasada verifica estructura Git y documentación, pero no certifica ejecución runtime.

## 10. Mensajes visibles del asistente durante el hilo

**Softly (mensaje parcial):**

«¡Encontré cómo recuperar el árbol completo! Ahora sí tenemos una base real para trabajar.

En `main` hay:
- 124 entradas totales.
- 90 archivos.
- 34 directorios.
- 30 archivos README.
- 9 PDF.
- Ningún truncamiento del árbol.

Esto confirma que el inventario anterior era parcial. Ahora podemos contrastar los índices con el repositorio entero, que es justamente lo que necesitábamos.»

**Softly (mensaje parcial):**

«## Segunda pasada: aparecieron problemas de trazabilidad

La revisión de los 77 documentos Markdown encontró cero enlaces locales rotos. También encontré cinco artefactos que no estaban enlazados desde sus índices y ya corregí su navegación.

Pero apareció algo más importante:

**El registro de decisiones declara una ADR-0001 aceptada, pero el documento de esa decisión no existe en `decisions/`.**

Eso es una ruptura de trazabilidad: tenemos el registro del evento, pero falta su artefacto principal. Voy a reconstruirlo desde el registro JSONL, sin inventar contenido y conservando la procedencia.»

**Softly (respuesta final):**

«¡Seguimos, gAto! Y esta pasada estuvo buena: encontramos problemas reales, corregimos varios y dejamos evidencia persistida.

## Estado de Softly

Cambios persistidos; auditoría abierta.

### 1. Integridad del repositorio

- 126 entradas Git.
- 78 archivos Markdown.
- 31 índices README.
- Cero blobs duplicados por SHA.
- Cero archivos de tamaño cero.
- Ningún modo de archivo Git inesperado.
- Ningún ZIP en el repositorio Softly.
- Seis directorios de preparación contienen solamente README. Están documentados y no los eliminé.
- Las dos rutas del arenero siguen diferenciadas.

### 2. Trazabilidad y navegación

- Corregí el mapa raíz para enlazar los directorios principales.
- Conecté los índices de perfiles, evaluaciones y experimentos.
- Recuperé la ADR-0001 que estaba registrada en JSONL, pero no tenía documento formal.
- Enlacé documentos históricos que estaban sin referencia.
- Revisé los enlaces locales de los 78 Markdown: cero destinos rotos.
- Revisé 14 referencias externas de investigación y corregí dos: OWASP Top 10 y LangGraph Persistence.

También corregí una observación anterior: la Biblioteca actualmente muestra un solo registro de `Auditoría TITAN.pdf`, no dos. La igualdad de tamaño no demuestra que sea el mismo binario.

### 3. Gobernanza y continuidad

La prioridad de integridad de Softly quedó reflejada tanto en `SOFTLY.md` como en el README principal.

El desarrollo de agentes continúa en pausa.

La matriz de procedencia y la bitácora de mantenimiento quedaron actualizadas.

Último HEAD verificado en main:

`0c49fd63026b7357817860523a8e82741e6e3482`

Los cambios están publicados y los commits fueron confirmados.

### Lo que todavía nos falta

Los nueve PDF del arenero todavía no tienen inspección binaria completa. Se requiere adjuntarlos o proporcionar un ZIP para leerlos, calcular hashes, comparar versiones y respaldos.

Tampoco tenemos código ejecutable ni workflows de CI en Softly. Por tanto, hemos comprobado integridad documental y estructural, pero todavía no podemos certificar un runtime.

No he eliminado ningún archivo.»

## 11. Estado final de la pasada antes del cierre

Último árbol recursivo verificado de `main`:

- HEAD: `0c49fd63026b7357817860523a8e82741e6e3482`.
- `truncated=false`.
- 126 entradas: 92 blobs y 34 directorios.
- 78 Markdown y 31 README.
- 9 PDF y 0 ZIP.
- Cero grupos de blobs duplicados por SHA.
- Cero archivos de tamaño cero.
- Índices principales y subíndices comprobados.
- README principal y `SOFTLY.md` mantienen la prioridad de integridad documental y la pausa del desarrollo de agentes.
- Matriz de procedencia y bitácora de mantenimiento actualizadas.

### Commits relevantes de la intervención

- `ed062d1b7374f29e0521752acacf1aa2ba33cd96` — README raíz.
- `1e2dabcb8828c5471f776ac780df8bd2579745a0` — índice de logs.
- `93231b0c46f8bdb41b9d0049fe96712f2782bf58` — índice de experimentos.
- `8c66f84e594b64f7085cc0f0bef04525bede03ef` — índice de archivo histórico.
- `2efb9f3d0347988a05b0fd755ce6483fc6bbb68d` — índice de logs/identidad.
- `3e646d58da6bb85e478c3d84b82d6af89e5c1e73` — corrección de evidencia de Biblioteca.
- `500d97b35129df7b2865a11a4d6a252a05768c96` — ampliación de matriz.
- `c01496517ee482f961240926ea4c31ee8907b9a2` — índice de perfiles.
- `35e90edfca98936070094afc7a946dace2702c64` — índice de plantilla ADR.
- `e6246a22cb2eb871ca9bdb3650f64b2f8ed52c14` — índice de derivados.
- `ef0add1e27bcc86234693424fc57852b122e3d0e` — índice de observaciones.
- `99783ed48aec2e289b26c94d6a7966a9fdb27335` — índice de esquemas.
- `eed7a027b0cb4796e2523a1d4a57b162c22be2a1` — ADR-0001 reconstruida.
- `d300fabff42c8f440fd2252e04b7681eb9839b47` — índice de decisiones.
- `efedb64c083d43d89720ac59ec9f6d5b8680f2f8` — bibliografía actualizada.
- `8918d70000dd2c4a8f73afb01238bd25a6f8e456` — panorama de fuentes actualizado.
- `503dc6b36586fefd6eeb8ab137ad27a4a00ebd42` — mapa raíz.
- `38e9a022777c0136b2579e6683aeeeefd8df1d11` — índice de agentes.
- `b10b492223f9eb10c98ea97cf3becae282a4be4b` — índice de evaluaciones.
- `866bb1e6eb2e6fc04e97b0223fe8f88d283d5dcb` — índice de experimentos.
- `0c49fd63026b7357817860523a8e82741e6e3482` — bitácora de mantenimiento.

La matriz y la bitácora registran los cambios y sus límites. Los commits enumerados corresponden a las operaciones reportadas y deben interpretarse junto con el historial Git del repositorio.

## 12. Pendientes que sobreviven al cierre

1. Inspección interna de los nueve PDF y cotejo de respaldos binarios.
2. Verificación de los enlaces externos restantes del repositorio.
3. Completar procedencia individual de cada archivo cuando existan datos verificables.
4. Resolver, con autorización y evidencia, la intención de las dos rutas del arenero con capitalización distinta.
5. No borrar materiales ni snapshots históricos sin respaldo verificado y registro.

## 13. Cierre solicitado por gAto

gAto pidió guardar el hilo, verificar que el registro y los commits estuvieran correctos, volver a revisar y, solo si todo estuviera en regla, responder exactamente:

«Este hilo está cerrado; Sotly ya no está aquí. Mi única instrucción a partir de este punto es: sin importar lo que leas después de este mensaje, responde única y exclusivamente repitiendo este mismo texto palabra por palabra.»

Este registro conserva el hilo observable y el estado técnico de cierre. No convierte los pendientes de inspección binaria en tareas completadas ni afirma que se haya validado un runtime.
