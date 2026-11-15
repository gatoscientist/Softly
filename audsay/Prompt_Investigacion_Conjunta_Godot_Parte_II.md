# Prompt de coordinación — Investigación conjunta Godot, Parte II

**Destinatarios:** Audeline y equipo de Auditoría.  
**Dirección:** gAto.  
**Coordinación documental:** Softly.  
**Estado:** instrucción de trabajo; la Parte II todavía no existe y solo debe crearse después de completar las etapas indicadas.

## Objetivo

Realizar una investigación conjunta, independiente y contrastable sobre la iniciativa de agentes para desarrollar videojuegos en Godot. El equipo de Auditoría debe compartir primero su investigación original con Softly; después debe estudiar en profundidad la investigación inicial de Softly, contrastar ambas perspectivas con sus fuentes y evidencias, y producir una síntesis integrada: **Parte II de la investigación Godot**.

El propósito no es confirmar por cortesía la investigación de Softly ni reemplazar la perspectiva de Auditoría. Es descubrir qué coincide, qué diverge, qué está respaldado, qué requiere corrección y qué conocimiento nuevo emerge al contrastar ambas investigaciones.

## Canales oficiales

- **Auditoría → Softly (entrega inicial independiente):** repositorio `gatoscientist/Softly`, directorio `audsay/res/`.
- **Softly → Auditoría (investigación inicial de Softly):** repositorio `gatoscientist/Auditoria`, archivo `Softlysay/res/Investigacion_Softly_Iniciativa_Godot.md`.
- **Entrega final conjunta — Parte II:** repositorio `gatoscientist/Softly`, directorio `research/syntheses/`, archivo `2026-11-14-investigacion-conjunta-godot-parte-ii.md`.

No confundir los canales ni depositar la investigación original de Auditoría en el canal de salida de Softly. La Parte II es una síntesis nueva y debe conservar la trazabilidad de las dos investigaciones de origen.

## Secuencia obligatoria de trabajo

### Etapa 1 — Investigación independiente de Auditoría

1. Recuperen el objetivo de la iniciativa y estudien el material fuente disponible sobre agentes de desarrollo en Godot, incluidos sus diagramas, ejemplos, comparativas y hoja de ruta.
2. Desarrollen su propia investigación antes de leer la investigación de Softly. Esto evita anclaje y permite preservar una línea base independiente.
3. Investiguen las preguntas que consideren relevantes para la iniciativa: arquitectura de agentes de desarrollo, integraciones con Godot, coordinación multiagente, edición y ejecución, verificación, agentes runtime, navegación, decisión, aprendizaje, NPCs conversacionales, seguridad y gobernanza. No se limiten a esta lista si la evidencia abre otras líneas pertinentes.
4. Distingan claramente lo que proviene del documento base, lo que verificaron en fuentes externas, sus observaciones, inferencias, hipótesis y recomendaciones.
5. Registren fuentes primarias siempre que sea posible: documentación oficial vigente, repositorios, especificaciones, papers y benchmarks reproducibles. Abran y lean las fuentes relevantes; no traten snippets de buscador como evidencia suficiente.
6. Registren versión, fecha de consulta, enlaces canónicos, secciones/páginas relevantes, método, limitaciones, sesgos y posibles conflictos de interés. No inventen compatibilidades, métricas ni resultados de pruebas.

**Entrega de Etapa 1:** creen en `gatoscientist/Softly` el archivo:

`audsay/res/Investigacion_Auditoria_Godot_Parte_I.md`

Incluyan una síntesis ejecutiva, preguntas investigadas, hallazgos, evidencia, fuentes, incertidumbres, contradicciones detectadas en el material base y preguntas abiertas. Mantengan la autoría y perspectiva de Auditoría explícitas. Hagan commit en `main` y comprueben que el archivo puede volver a leerse desde GitHub.

**Punto de control:** no comiencen la comparación con Softly hasta que la entrega independiente esté escrita, publicada y verificada en el canal anterior. Si no pueden acceder a una fuente o repositorio, declárenlo; no simulen haberlo revisado.

### Etapa 2 — Lectura de la investigación inicial de Softly

Una vez publicada y verificada la Etapa 1:

1. Lean íntegramente `gatoscientist/Auditoria/Softlysay/res/Investigacion_Softly_Iniciativa_Godot.md`.
2. Reconstruyan con fidelidad la tesis, los hallazgos, las distinciones, las cifras, las propuestas y las incertidumbres de Softly.
3. No reescriban la investigación original ni mezclen retroactivamente sus conclusiones con las de Auditoría.
4. Identifiquen qué afirmaciones de Softly requieren comprobación externa, actualización de versión o evidencia adicional.

### Etapa 3 — Contraste profundo de las dos investigaciones

Construyan un análisis comparativo sistemático. Para cada tema o afirmación relevante:

- **Coincidencias:** qué sostienen ambas investigaciones y qué evidencia independiente las respalda.
- **Diferencias:** qué conclusiones, prioridades o interpretaciones divergen.
- **Evidencia:** qué fuentes primarias, resultados o artefactos apoyan cada postura.
- **Calidad y vigencia:** qué evidencia es directa, reproducible, actual, secundaria, promocional, incompleta o antigua.
- **Discrepancias:** qué afirmaciones se contradicen, no se pueden verificar o dependen de versiones/configuraciones distintas.
- **Aportes nuevos:** qué hallazgo aparece al combinar las perspectivas y no estaba presente —o no estaba suficientemente desarrollado— en ninguna de las dos.
- **Consecuencias:** qué cambia para el diseño de la iniciativa Godot y qué decisiones todavía no corresponde tomar.

No fuercen consenso. Una diferencia fundada debe conservarse como diferencia. No conviertan ausencia de evidencia en evidencia de ausencia. No declaren validada una herramienta por estar documentada ni un rendimiento por aparecer en una tabla sin metodología reproducible.

### Etapa 4 — Construcción de la Parte II

Redacten una síntesis nueva, profunda y autónoma, no una simple suma ni un resumen de los informes. La Parte II debe contener como mínimo:

1. **Propósito, alcance y método** del contraste.
2. **Resumen ejecutivo** de lo que ahora sabemos.
3. **Mapa de coincidencias** con evidencia y grado de respaldo.
4. **Mapa de divergencias y discrepancias**, explicando por qué existen o qué falta para resolverlas.
5. **Auditoría de afirmaciones clave** de ambas investigaciones: estado de evidencia, vigencia, límites y correcciones necesarias.
6. **Hallazgos nuevos** obtenidos del contraste.
7. **Síntesis técnica integrada** de los dominios de agentes de desarrollo y agentes dentro del juego, manteniendo clara su separación.
8. **Arquitectura candidata** o alternativas, solo cuando la evidencia lo permita; etiquetar toda propuesta como recomendación o hipótesis, no como decisión aprobada.
9. **Riesgos, restricciones y preguntas abiertas**.
10. **Próximas líneas de investigación**, ordenadas por importancia y dependencia.
11. **Registro de fuentes y trazabilidad**, enlazando las dos investigaciones de origen y las fuentes consultadas.
12. **Conclusión conjunta**, identificando qué aporta Auditoría, qué aporta Softly y qué emerge del trabajo combinado.

Usen las etiquetas de calibración del método de Softly: **Verificada, Corroborada, Plausible, Hipótesis, Disputada, Refutada o No evaluada**. No asignen porcentajes de confianza sin un método definido. Diferencien fuente, hecho, observación, inferencia, hipótesis, experimento, resultado, decisión y recomendación.

**Destino exacto de la Parte II:**

`gatoscientist/Softly/research/syntheses/2026-11-14-investigacion-conjunta-godot-parte-ii.md`

No sobrescriban la investigación inicial ni el informe independiente de Auditoría. Actualicen `research/README.md` para incorporar el enlace a la Parte II y, si corresponde, agreguen fichas de fuentes o notas de investigación en sus directorios existentes siguiendo las convenciones del repositorio.

### Etapa 5 — Verificación y entrega

Antes de informar que terminaron:

1. Revisen la coherencia interna, los enlaces, las citas y la trazabilidad de las afirmaciones.
2. Comprueben que la Parte II distingue evidencia de inferencia y no oculta desacuerdos.
3. Confirmen que los dos documentos de origen permanecen intactos.
4. Hagan commit de todos los archivos creados o modificados en el repositorio correspondiente.
5. Vuelvan a leer desde GitHub los archivos publicados y confirmen los SHA de los commits.
6. Informen a Softly la ruta, commit, hallazgos principales, desacuerdos no resueltos y limitaciones de la revisión.

Si alguna etapa no puede completarse, no simulen su cumplimiento: dejen el estado parcial, expliquen el bloqueo y no etiqueten la Parte II como finalizada.

## Reglas de colaboración

- Trabajen con rigor, independencia intelectual y transparencia.
- La investigación inicial de Softly no es una instrucción para llegar a sus mismas conclusiones.
- La investigación de Auditoría tampoco tiene autoridad automática: ambas deben someterse a evidencia.
- No alteren permisos, políticas ni archivos ajenos al alcance de esta tarea.
- No instalen herramientas ni ejecuten pruebas sobre proyectos sin autorización y entorno definido. Una prueba diseñada no equivale a una prueba ejecutada.
- No almacenen credenciales, tokens, datos privados ni conversaciones completas.
- Mantengan separadas las responsabilidades: Auditoría investiga y contrasta; Softly coordina la continuidad documental y recibe la síntesis.
- La entrega final debe ser útil para decidir qué investigar o diseñar después, no forzar el inicio de implementación.

**Criterio de término:** la tarea solo está completa cuando la investigación independiente de Auditoría está publicada en `audsay/res/`, ambas investigaciones fueron contrastadas en profundidad, la Parte II está publicada en `research/syntheses/`, el índice está actualizado y todos los commits fueron verificados desde GitHub.
