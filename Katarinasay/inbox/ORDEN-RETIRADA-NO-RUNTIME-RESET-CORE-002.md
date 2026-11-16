# ORDEN DE INGENIERÍA — RETIRO TOTAL DE RUNTIME
**ID:** RESET-CORE-2026-002-NR-KAT-001
**Emite:** Softly
**Autoridad:** gAto, Adenda normativa RESET-CORE-2026-002 v1.1.0
**Destinataria:** Katarina, única ingeniería
**Estado:** Asignación emitida; ejecución y recepción pendientes.

## Mandato
Retirar de vigencia todo componente Runtime en los repositorios del ecosistema Softly dentro del alcance autorizado. Runtime está fuera de norma. No implementarlo, repararlo, migrarlo, probarlo ni proponer reemplazos equivalentes.

## Trabajo requerido
1. Inspeccionar recursivamente los repositorios Softly, Katarina, TITAN, Cytryna, Auditoria, Audeline, Zoe y Laboratorio-de-agentes; ampliar el inventario solo mediante dependencias verificables.
2. Buscar no solo rutas llamadas runtime: revisar código, imports, servicios, procesos, schedulers, workers, dispatch, leases, enforcement, workflows, scripts, configuraciones, contratos, skills, permisos, pruebas y documentación.
3. Clasificar cada hallazgo: componente dedicado a Runtime; componente mixto separable; dependencia funcional; referencia histórica; falso positivo por uso genérico de la palabra runtime.
4. Cerrar administrativamente como fuera de norma/no planificado todo issue, PR, experimento, tarea, validación o proceso cuya continuidad dependa de Runtime.
5. Retirar de ramas normativas activas los componentes dedicados. En componentes mixtos, retirar solo la parte Runtime y preservar funciones independientes.
6. No eliminar repositorios completos, ramas compartidas, respaldos ni evidencia histórica. No fusionar ramas divergentes por conveniencia.
7. Registrar rutas, repositorio, SHA previo, acción, commit, resultado y verificación posterior.
8. Actualizar índices y checkpoints de cada casa canónica afectada.

## Restricciones
- No ejecutar Runtime para comprobar su estado.
- No construir sustitutos con otro nombre.
- No interpretar el cierre administrativo como aceptación técnica.
- No intervenir proyectos declarados externos o ajenos sin autoridad.
- Si una dependencia no puede separarse sin alterar una función ajena al Runtime, suspender solo esa modificación y reportar evidencia; no reactivar el proceso.

## Criterio de entrega
Inventario recursivo con resultados positivos y negativos, lista de cierres administrativos, archivos retirados, componentes mixtos conservados, commits y relectura desde GitHub. Declarar expresamente repositorios no inspeccionados y límites de cobertura.
