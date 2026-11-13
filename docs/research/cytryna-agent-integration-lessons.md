# Lecciones de integración de agentes blandos: caso Cytryna

**Fuente:** *Cytryna: fusión de agentes blandos en el agente duro y costo de limpieza* (informe entregado por el usuario, 13-11-2026).
**Naturaleza:** análisis de caso y estimaciones del informe; no es una especificación de Softly ni una auditoría independiente de este repositorio.

## Propósito

Conservar únicamente los aprendizajes transferibles al diseño de Softly Agents. Cytryna es un caso de referencia, no una arquitectura que debamos copiar, corregir o incorporar a Softly.

## Hallazgo central

El informe concluye que la fusión fue superficial en código, pero profunda en gobernanza: las dependencias directas entre motor y capas blandas eran pocas, mientras que autoridad, escritura y protección de recursos sí estaban mezcladas.

## Evidencia y lecciones del caso

1. **Código de producción alojado en workspace de agente.** El informe identifica un import desde main.py hacia AGENTGUI.workspace.gui_tkinter. Código necesario para el producto vivía dentro del espacio de trabajo de una agente; además, el empaquetado y CI no lo cubrían. Lección transferible: el workspace de una instancia no debe alojar componentes esenciales del proyecto anfitrión. Los entregables aceptados deben integrarse explícitamente en ubicaciones y bajo propiedad del proyecto.
2. **Jurisdicción inconsistente.** La política de escritura de Fran no coincidía con modificaciones atribuidas a ella en archivos del motor; los logs eran incompletos y archivos de Andy fueron editados después de su entrega sin registro correspondiente. Lección: distinguir responsabilidad declarada, permiso efectivo, autoría, propiedad y registro verificable de cambios.
3. **Protección meramente declarativa.** Contratos y carpetas de agentes no estaban cubiertos por la protección del Guardián descrita en el informe; las reglas de trabajo no eran controles técnicos. Lección: los prompts no sustituyen enforcement externo de permisos y protección.
4. **Deriva entre documentación y realidad.** El informe señala rutas incorrectas y documentación que omitía información de proveedores. Lección: verificar consistencia entre contratos, configuración, código y documentación.
5. **Contaminación entre proyectos.** Se registraron residuos y referencias de TITAN en Cytryna. Lección: aislar contextos y dependencias; no trasladar artefactos de un proyecto a otro sin necesidad y procedencia.
6. **Estado de ejecución mezclado con fuentes.** Algunos logs y registros cambiaban al ejecutar tests; la copia de análisis ensució archivos rastreados. Lección: separar estado, logs y salidas de pruebas del material fuente; los tests deben ser aislados y reproducibles.
7. **Identidad independiente.** El informe considera sano que Cytryna y los contratos de sus agentes mantuvieran identidades diferenciadas. Lección: colaboración no implica fusión de identidad.

## Estimación de limpieza reportada

El informe estima aproximadamente 10–17 horas para una persona que conozca ese repositorio. Desglosa aislamiento de tests y archivos generados, protección, mapa de propiedad, separación de capas blandas, traslado de GUI y residuos de TITAN. Presenta una opción mínima de 7–10 horas y una opción de repositorio separado con 3–4 horas adicionales.

Estas cifras son estimaciones propias del informe para Cytryna; no deben extrapolarse como costo esperado de Softly.

El informe también recomienda abordar primero tests y protección, y después los traslados de estructura. Advierte que modificar contratos protegidos por hash obliga a regenerar el manifiesto mediante el procedimiento responsable.

## Requisitos candidatos para contrastar con el modelo de Softly

- Workspace aislado por instancia/asignación y fuera del árbol de componentes esenciales del proyecto anfitrión.
- Registro de procedencia, propietario, autoría y estado de aceptación de cada recurso creado o modificado.
- Integración explícita de entregables; creación por un agente no transfiere automáticamente propiedad al proyecto.
- Permisos efectivos aplicados fuera del modelo.
- Separación de fuentes, estado de ejecución, logs y artefactos de tests.
- Contexto y memoria aislados entre proyectos por defecto.
- Retiro que revoque accesos y retire recursos temporales sin borrar entregables aceptados ni dañar el anfitrión.
- Verificación posterior al retiro: integridad del proyecto, residuos y recursos huérfanos.
- Trazabilidad suficiente para reconstruir quién hizo qué, cuándo y bajo qué asignación.

Estos son requisitos candidatos derivados del caso, no decisiones aprobadas ni funcionalidades implementadas.

## Límites del informe

El propio documento indica que no revisó en profundidad MOTOR, GUI ni TESTERS; de auditorías solo leyó títulos; la atribución por agente se apoyó en logs incompletos y las horas son estimaciones. Mantener estas limitaciones al citar sus conclusiones.

## Relación con Softly

Contrastar estos requisitos con docs/architecture/agent-model-v0.1.md y el brief existente. No reemplazar el modelo de cuatro piezas (Agent Definition, Project Brief, Project Assignment, Work Session) ni crear un molde distinto por familia sin evidencia y decisión explícita.
