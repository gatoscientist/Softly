# Principio de Continuidad y Preservación
**Ámbito:** RESET-CORE-2026-002  
**Autoridad:** gAto  
**Estado:** Mandato rector para cualquier operación de limpieza, consolidación o retiro de artefactos.

## 0. Principio de Continuidad y Preservación

La ejecución de este mandato queda subordinada a la continuidad de Softly y a la preservación del trabajo recuperable.

Se establecen las siguientes condiciones:

1. El núcleo de identidad, contratos, principios y conocimiento operativo de Softly no puede eliminarse ni alterarse durante esta operación.
2. El trabajo recuperado del RESET-CORE-2026-002 debe permanecer accesible, incluyendo el registro histórico 1.0.0, sus archivos archivados, la rama de migración v2, el PR #8, los handoffs, la matriz de ramas y los registros de decisiones.
3. La existencia de duplicados debe demostrarse mediante comparación de contenido y referencias. La similitud de nombres o estructuras no constituye prueba suficiente.
4. Todo elemento cuya función, procedencia o dependencia sea indeterminada queda excluido del borrado.
5. Los commits de limpieza deben generarse en ramas de trabajo, sin modificar directamente las ramas principales.
6. Antes de cerrar la operación, Softly debe verificar que los archivos protegidos permanecen intactos y que los resultados recuperables siguen disponibles.
7. Ningún resultado puede declararse `ready` sin comprobación efectiva de sus dependencias.
8. La operación no autoriza cambios de identidad, versiones, contratos ni autoridad de agentes, salvo los expresamente indicados.

La limpieza tiene como finalidad recuperar claridad operativa, no borrar historia ni ocultar desviaciones anteriores.

## Aplicación operativa

Este principio prevalece sobre cualquier instrucción de limpieza incompatible dentro del alcance de RESET-CORE-2026-002. No modifica por sí mismo identidades, versiones, contratos, permisos ni autoridad.

Antes de proponer un borrado, cada elemento debe contar con:
- identificación inequívoca del objeto y su ubicación;
- comparación de contenido (hash o diff) con cada supuesto duplicado;
- verificación de referencias entrantes, dependencias y consumidores;
- determinación documentada de procedencia y función;
- evidencia de que la copia o referencia preservada es accesible y suficiente.

Si cualquiera de esos puntos queda indeterminado, el elemento se conserva y se clasifica como **preservación obligatoria / no evaluable para borrado**.

Toda limpieza se prepara en una rama de trabajo separada. La revisión debe comprobar el diff completo, la ausencia de cambios en archivos protegidos y la persistencia de los artefactos recuperables. La integración a una rama principal requiere revisión y autorización conforme a la gobernanza vigente; este principio no concede autorización de merge.

El estado `ready` exige evidencia verificable de dependencias satisfechas, no solo documentación declarativa. Si una dependencia no puede comprobarse, el resultado permanece en estado no certificado y se informa explícitamente.

## Conjunto protegido conocido

Como mínimo, se consideran protegidos mientras dure la operación:
- núcleo de identidad, principios, contratos y conocimiento operativo de Softly;
- registro histórico 1.0.0 y sus archivos archivados;
- rama `migration/registry-v2-reset-core-002` y PR #8;
- handoffs, matriz/manifiesto de ramas e informes de auditoría;
- registros de decisiones, bitácoras y evidencia histórica vinculada al RESET.

La lista es acumulativa, no exhaustiva. La ausencia de un elemento en esta lista no implica autorización para eliminarlo.
