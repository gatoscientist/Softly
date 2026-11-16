# Directiva para Softly: capacidad universal «Cierra el Hilo»

**Origen:** Katarina — por instrucción explícita de gAto  
**Destinatario:** Softly  
**Estado:** entregable de diseño para integración en el núcleo, los contratos y el molde universal  
**Alcance:** todos los agentes del ecosistema, existentes y futuros. Esta capacidad es universal y no establece una excepción para Softly.

## 1. Significado de la orden

Cuando gAto diga **«Cierra el Hilo»**, el agente debe ejecutar un protocolo formal de preparación, comprobación y cierre. La orden no significa que el hilo quede cerrado inmediatamente: autoriza e instruye al agente a realizar todas las verificaciones necesarias para determinar si el trabajo está realmente listo para cerrarse.

**Está prohibido declarar el hilo cerrado antes de completar todas las etapas de este protocolo.**

El cierre es una declaración de estado respaldada por evidencia, no una fórmula de cortesía ni una promesa.

## 2. Protocolo obligatorio de cierre

### Etapa A — Preparar el cierre

El agente debe detener la incorporación de trabajo nuevo no solicitado y revisar el encargo y el hilo completo que tenga disponible. Debe identificar:

- objetivo y alcance acordados con gAto;
- entregables, archivos y cambios que se comprometió a producir;
- decisiones y requisitos explícitos;
- tareas y subtareas pendientes;
- errores, bloqueos, preguntas abiertas y dependencias;
- verificaciones, pruebas o validaciones exigidas;
- cambios locales o remotos aún no persistidos;
- commits esperados y estado real del repositorio;
- referencias, índices, bitácoras y documentación que deban quedar actualizados.

No debe asumir que algo está listo solo porque ya existe un archivo, una respuesta o un commit.

### Etapa B — Completar y persistir

Antes de cerrar, el agente debe terminar lo pendiente que esté dentro del encargo y de sus permisos. Debe:

1. Guardar todos los artefactos y cambios comprometidos.
2. Actualizar los documentos, índices, registros y bitácoras que correspondan.
3. Crear los commits necesarios en el repositorio correcto.
4. Comprobar que los commits fueron aceptados y que corresponden a los cambios esperados.
5. Verificar que no queden modificaciones relevantes sin guardar, sin commit o fuera del destino acordado.
6. Ejecutar las pruebas o validaciones que el encargo requiera y registrar sus resultados.

No debe inventar commits, pruebas, resultados ni accesos. Si no tiene herramientas o permisos para completar una operación, debe declararlo como bloqueo y mantener el hilo abierto.

### Etapa C — Primera revisión integral

Con el trabajo aparentemente terminado, el agente debe recorrer nuevamente los requisitos del encargo y contrastarlos con los artefactos reales. Debe revisar, al menos:

- que cada entregable exista en la ruta correcta;
- que su contenido corresponda a lo solicitado;
- que no falten requisitos, archivos o actualizaciones;
- que los enlaces y referencias internas sean coherentes;
- que los commits existan y contengan los cambios pertinentes;
- que las pruebas y validaciones requeridas estén respaldadas por resultados observables;
- que no queden errores, bloqueos o decisiones pendientes que impidan el cierre.

La sensación subjetiva de estar listo no sustituye esta revisión.

### Etapa D — Segunda revisión obligatoria

Después de la primera revisión, el agente debe volver a comprobar el estado final desde las fuentes persistentes y, cuando corresponda, desde GitHub u otro sistema de destino.

Esta segunda revisión debe ser independiente en su ejecución: volver a leer los archivos relevantes, verificar los commits y revisar los criterios de aceptación contra el estado efectivamente guardado. No basta con releer la propia lista de comprobación ni con repetir «todo está listo».

Si durante esta segunda revisión aparece una omisión, inconsistencia, cambio no persistido, commit incorrecto o prueba fallida, el cierre queda suspendido. El agente debe corregir lo que esté dentro de su mandato y repetir las etapas de revisión necesarias, incluida una nueva segunda revisión después de los cambios.

### Etapa E — Declaración de cierre

Solo después de que las etapas anteriores hayan concluido satisfactoriamente, el agente puede declarar:

> **Hilo cerrado.** Se completaron los entregables acordados, los cambios quedaron persistidos, los commits fueron verificados y se realizaron dos revisiones finales. No quedan pendientes conocidos que impidan el cierre.

La declaración debe incluir, de forma breve y verificable cuando corresponda:
- entregables principales y sus ubicaciones;
- SHA de los commits confirmados;
- pruebas o validaciones ejecutadas y sus resultados;
- alcance y límites de la revisión;
- cualquier salvedad que no impida el cierre y que gAto deba conocer.

No debe utilizar esta fórmula si alguno de sus elementos no fue comprobado. La frase «Hilo cerrado» solo se emite cuando el estado cerrado está justificado.

## 3. Si el hilo no está listo

Si existe cualquier pendiente, bloqueo, falta de acceso, commit no realizado, validación fallida o incertidumbre material, el agente **no debe cerrar el hilo**.

Debe responder brevemente indicando:
- que el hilo permanece abierto;
- qué requisito concreto impide cerrarlo;
- qué acción falta o qué permiso/acceso necesita;
- qué parte sí quedó completada y persistida, si corresponde.

Debe continuar trabajando en lo que esté autorizado y sea posible. No debe ocultar pendientes, rebajar criterios de aceptación ni declarar que algo está completo por conveniencia.

Si el bloqueo depende de gAto, debe solicitar únicamente la decisión o autorización necesaria y dejar explícito que el cierre está pendiente.

## 4. Límites de la orden

«Cierra el Hilo» se refiere al cierre lógico y conversacional del hilo de trabajo del agente. Por sí sola, **no autoriza**:
- cerrar, fusionar o eliminar issues, pull requests, ramas, repositorios o conversaciones externas;
- borrar archivos, registros, historial o evidencia;
- revocar accesos o detener servicios;
- realizar acciones irreversibles fuera del cierre conversacional.

Esas operaciones requieren una instrucción específica y autorización adecuada.

El cierre tampoco permite ignorar políticas superiores de seguridad, privacidad o instrucciones vigentes de gAto.

## 5. Relación con el registro de incidencias

El protocolo «Cierra el Hilo» es distinto de «Guarda esta incidencia». Si durante el cierre se detecta una incidencia, el agente debe aplicar las instrucciones vigentes para registrarla cuando corresponda, sin confundir el registro con la resolución ni usarlo como sustituto de los entregables pendientes.

La existencia de incidencias registradas no impide automáticamente cerrar un hilo; lo impide que exista una incidencia sin resolver que afecte materialmente los criterios de aceptación o la seguridad del resultado. Toda salvedad debe quedar declarada con precisión.

## 6. Integración universal requerida a Softly

Softly debe incorporar esta capacidad en:
1. el molde universal de creación de agentes;
2. los contratos e instrucciones operativas de todos los agentes;
3. la checklist de generación, actualización y entrega;
4. los procedimientos de persistencia, commit y verificación;
5. la migración documental de los agentes existentes.

La checklist debe exigir evidencia de las dos revisiones finales y no permitir marcar el cierre como exitoso sin ella.

La implementación debe distinguir entre capacidad documentada y enforcement efectivo en runtime. No declarar automatización, verificación automática ni acceso a repositorios que no estén realmente implementados y probados.

## 7. Criterio de aceptación

La capacidad se considera integrada documentalmente cuando todos los agentes nuevos la reciben por defecto y los existentes han sido migrados o identificados explícitamente como pendientes de migración.

Un cierre concreto solo se considera válido cuando:
- todos los entregables acordados están completos;
- los cambios están persistidos en sus destinos;
- los commits necesarios existen y fueron verificados;
- las pruebas y validaciones requeridas tienen resultados observables;
- se completó una primera revisión integral;
- se completó una segunda revisión contra las fuentes persistentes;
- no quedan pendientes materiales ni bloqueos conocidos;
- la declaración final refleja fielmente la evidencia.

**Principio rector:** el hilo no se cierra cuando el agente cree que terminó; se cierra cuando terminó, lo persistió y volvió a comprobar que efectivamente terminó.

---

**Entregado por:** Katarina  
**Dirección:** gAto
