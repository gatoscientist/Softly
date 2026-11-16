# ENCARGO DE AUDITORÍA — VERIFICACIÓN DE RETIRO TOTAL DE RUNTIME
**ID:** RESET-CORE-2026-002-NR-AUD-001
**Emite:** Softly
**Autoridad:** gAto, Adenda normativa RESET-CORE-2026-002 v1.1.0
**Destinataria:** Audeline, única auditoría independiente
**Estado:** Asignación emitida; recepción y ejecución pendientes.

## Mandato
Verificar independientemente el cumplimiento de la prohibición total de Runtime. No ejecutar, probar ni invocar Runtime. No asumir que un repositorio está limpio por ausencia de carpetas llamadas runtime.

## Alcance de auditoría
Contrastar el inventario y los cambios que entregue Katarina con las fuentes persistentes en los repositorios Softly, Katarina, TITAN, Cytryna, Auditoria, Audeline, Zoe y Laboratorio-de-agentes, además de dependencias explícitamente referenciadas.

## Pruebas requeridas
1. Buscar implementaciones y dependencias por contenido, no solo por nombre de archivo: imports, procesos, workers, schedulers, dispatch, leases, enforcement, servicios, workflows, scripts, configuración, permisos, contratos, skills y pruebas.
2. Distinguir Runtime prohibido de usos genéricos y no relacionados de la palabra inglesa “runtime”; justificar cada clasificación.
3. Verificar que procesos e issues dependientes estén cerrados administrativamente y que los PR estén cerrados sin merge cuando corresponda.
4. Verificar que componentes dedicados estén retirados de las ramas normativas activas y que los componentes mixtos conserven únicamente funciones independientes.
5. Releer commits y destinos persistentes; verificar SHA, historial preservado y ausencia de reactivación normativa.
6. Informar cobertura, falsos positivos, excepciones, repositorios no inspeccionados y cualquier dependencia residual.

## Independencia
No aceptar como prueba suficiente la declaración de Katarina ni la de Softly. Contrastar directamente con GitHub y registrar discrepancias. No alterar código ni sustituir a Katarina en ingeniería. Si encuentra un incumplimiento, emitir hallazgo con ruta, evidencia, impacto y acción correctiva; no cerrar la auditoría hasta verificarlo.

## Criterio de entrega
Informe independiente de cumplimiento RESET-CORE-2026-002 v1.1.0, con matriz repositorio/hallazgo/estado/evidencia/commit y dictamen explícito. No declarar “Runtime eliminado del ecosistema” si existe cobertura incompleta.
