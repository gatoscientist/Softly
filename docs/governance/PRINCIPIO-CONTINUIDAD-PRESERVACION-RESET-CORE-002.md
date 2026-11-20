# Principio de Continuidad y Preservación — RESET-CORE-2026-002

**Emisor:** gAto, Dirección  
**Fecha:** 2026-11-16  
**Aplicación:** Toda operación de limpieza, recuperación, consolidación o reorganización documental/técnica derivada de RESET-CORE-2026-002.  
**Estado:** Mandato rector de preservación para la operación.

La ejecución de cualquier operación queda subordinada a la continuidad de Softly y a la preservación del trabajo recuperable.

## Condiciones obligatorias

1. El núcleo de identidad, contratos, principios y conocimiento operativo de Softly no puede eliminarse ni alterarse durante esta operación.
2. El trabajo recuperado del RESET-CORE-2026-002 debe permanecer accesible, incluyendo el registro histórico 1.0.0, sus archivos archivados, la rama de migración v2, el PR #8, los handoffs, la matriz de ramas y los registros de decisiones.
3. La existencia de duplicados debe demostrarse mediante comparación de contenido y referencias. La similitud de nombres o estructuras no constituye prueba suficiente.
4. Todo elemento cuya función, procedencia o dependencia sea indeterminada queda excluido del borrado.
5. Los commits de limpieza deben generarse en ramas de trabajo, sin modificar directamente las ramas principales.
6. Antes de cerrar la operación, Softly debe verificar que los archivos protegidos permanecen intactos y que los resultados recuperables siguen disponibles.
7. Ningún resultado puede declararse `ready` sin comprobación efectiva de sus dependencias.
8. La operación no autoriza cambios de identidad, versiones, contratos ni autoridad de agentes, salvo los expresamente indicados.

La limpieza tiene como finalidad recuperar claridad operativa, no borrar historia ni ocultar desviaciones anteriores.

## Aplicación y criterio de cumplimiento

- Este principio se aplica junto con RESET-CORE-2026-002 y el Dictamen de Dirección de destrabe. No reemplaza sus límites de autoridad ni reabre Runtime o KAT-006.
- La rama `migration/registry-v2-reset-core-002` y Softly PR #8 son evidencia de trabajo recuperado y deben mantenerse accesibles durante la operación. Su contenido no se considera aprobado por el solo hecho de existir.
- La preservación de los artefactos nombrados debe verificarse por ruta, referencia Git y contenido. Para afirmar identidad binaria se requiere comparar SHA de blob o contenido equivalente; nombres coincidentes no bastan.
- Las comparaciones de duplicidad deben incluir contenido y referencias entrantes/salientes conocidas. Si falta cualquiera de esos antecedentes, el elemento se conserva.
- Las operaciones de limpieza se preparan y ejecutan en ramas de trabajo. La integración a ramas principales requiere el flujo de revisión aplicable y nunca se realiza como escritura directa de limpieza.
- La condición `ready` exige que cada dependencia declarada exista, sea accesible y haya sido inspeccionada en la referencia usada por el entregable.
- La verificación final debe releer desde GitHub los artefactos protegidos y comparar sus hashes con el baseline registrado antes de la operación. También debe comprobar accesibilidad de PR #8, rama de migración, archivos históricos/archivados, handoffs, matriz de ramas y decisiones.
- Cualquier excepción, discrepancia o imposibilidad de verificar se registra como pendiente localizado. No se sustituye por una afirmación de éxito.

## Protección negativa

Este mandato no autoriza:
- eliminar, sobrescribir, renombrar ni reescribir el núcleo de Softly;
- modificar directamente `main` u otra rama principal con commits de limpieza;
- eliminar el registro histórico 1.0.0 ni los archivos archivados;
- cerrar, fusionar, reescribir o borrar PR #8 o su rama de migración como parte de la limpieza;
- deducir duplicidad por nombres, rutas o similitud estructural;
- borrar elementos de procedencia, función o dependencia indeterminada;
- cambiar identidades, versiones, contratos, permisos o autoridad fuera de una autorización expresa.

