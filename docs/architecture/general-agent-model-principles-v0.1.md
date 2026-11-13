# Principios transversales del modelo general de agentes — v0.1

**Fecha:** 2026-11-13  
**Estado:** principio arquitectónico acordado por el usuario; formalización documental inicial. Pendiente de contraste con diagramas originales y validación de diseño.  
**Alcance:** modelo general para diseñar, desarrollar, inicializar, asignar, operar y retirar distintas clases y familias de agentes. No es exclusivo de Softly ni de los agentes blandos.

## 1. Propósito y alcance del modelo

El objeto de diseño es un **modelo general de agentes** capaz de dar soporte a distintos universos y familias de agentes. Los agentes blandos que se están desarrollando actualmente son una aplicación de ese modelo, no su límite.

Softly es un componente/laboratorio dentro de este ecosistema. Tiene responsabilidades y principios propios, pero no debe confundirse con el modelo general ni convertirse en su sinónimo. El modelo debe poder orientar también el desarrollo de otros agentes, incluidos agentes que formen parte de productos o runtimes, sin fusionar sus identidades, memorias, permisos o autoridades.

Este documento registra un principio transversal ya aclarado por el usuario. No declara que exista una implementación técnica ni pretende cerrar el resto de la arquitectura.

## 2. Principio arquitectónico fundamental: visibilidad asimétrica entre niveles

La **visibilidad asimétrica** es un principio arquitectónico fundamental del modelo general de agentes.

- Los niveles superiores pueden tener visibilidad de los registros, actividades y artefactos producidos en los niveles inferiores, dentro del alcance definido para esa relación.
- Los niveles inferiores no pueden acceder por esa vía a los espacios, registros, contextos ni decisiones de los niveles superiores.
- La visibilidad no es recíproca por defecto: no se debe asumir acceso ascendente.
- La información se origina en los niveles donde ocurre el trabajo y puede ponerse a disposición de los niveles superiores autorizados para observación.
- Esta regla es transversal: no pertenece exclusivamente a Softly, a los agentes blandos ni a una familia funcional determinada.

La formulación “desde arriba hacia abajo” describe **quién puede ver a quién**, no el origen físico de los datos. Los registros se producen abajo y se hacen visibles hacia arriba. Conviene mantener separadas ambas direcciones en diagramas y contratos para evitar flechas ambiguas.

### 2.1 Visibilidad no concede autoridad

Poder observar o leer información de un nivel inferior no concede automáticamente autoridad para:
- intervenir en su ejecución;
- modificar sus artefactos;
- cambiar sus instrucciones, identidad o permisos;
- dirigir su trabajo o sustituir a sus responsables;
- emitir auditorías, aprobaciones o certificaciones.

La autoridad de lectura, la autoridad de escritura, la capacidad de intervención y la responsabilidad de decisión son dimensiones distintas. Deben especificarse y controlarse por separado. La observabilidad por sí sola no implica ninguna de las otras.

### 2.2 Registros y trazabilidad

Para que la visibilidad superior sea útil y verificable, los niveles que ejecutan trabajo deben producir registros y artefactos con procedencia suficiente. El modelo deberá definir, según tipo de agente y sensibilidad:
- qué actividades y resultados se registran;
- formato, granularidad y procedencia;
- quién puede leerlos y bajo qué condiciones;
- retención, protección y tratamiento de datos sensibles;
- qué partes son visibles a cada nivel.

El principio no autoriza recopilar indiscriminadamente datos privados ni elimina la necesidad de minimización, seguridad y políticas de retención.

## 3. Aplicación a Softly: un caso particular, no el origen del principio

En la arquitectura de Softly, la visibilidad asimétrica se expresa como una capacidad de observación de los niveles inferiores desde la capa superior de Softly. Los agentes y equipos inferiores no obtienen por ello acceso al espacio superior de Softly.

Además, para el proceso descrito por el usuario:
- Softly no es auditora, no audita, no certifica ni reemplaza auditores.
- Softly no participa ni interviene en el ciclo de trabajo.
- Softly espera a que el ciclo concluya antes de leer y analizar sus registros y los resultados de auditoría. No observa ese ciclo en tiempo real.
- Leer auditorías y resultados permite a Softly incorporarlos como antecedentes; no convierte a Softly en autora ni autoridad de esas auditorías.
- La visibilidad de Softly sobre información inferior no le otorga automáticamente permisos de modificación o intervención.

Estas son definiciones del caso Softly y del proceso descrito; no deben confundirse con el principio transversal ni generalizarse a todos los agentes como si todos tuvieran el mismo rol o calendario.

## 4. Separación de universos y capas

El modelo debe conservar distinciones explícitas entre:
- Softly como laboratorio/capa del ecosistema;
- agentes blandos que investigan, diseñan, desarrollan o mantienen proyectos;
- equipos de desarrollo que trabajan sobre un producto;
- agentes internos que forman parte del runtime o producto desarrollado (por ejemplo, tripulantes de TITAN);
- auditores y agentes científicos, cuando correspondan.

Las relaciones de visibilidad entre capas deben especificarse sin fusionar identidades, memoria, permisos, autoridad ni propiedad de artefactos. En el ejemplo explicado por el usuario, los tripulantes registran su actividad y el equipo de desarrollo del producto puede observar esos registros; Softly, desde una capa superior, puede observar registros de los equipos y agentes inferiores según el alcance definido. Esto ilustra la arquitectura; no establece por sí solo un runtime implementado.

## 5. Reglas del proceso de trabajo descrito (no confundir con principios universales)

El usuario describió un proceso experimental con ciclos de trabajo, auditorías y deliberación. Para ese proceso:
1. Las auditorías ocurren después de cada ciclo de trabajo; esta secuencia fue señalada expresamente como una regla que debe mantenerse.
2. Puede haber varios auditores independientes, con perspectivas, alcances e información disponible diferentes. No imponer un único auditor ni un flujo universal.
3. La deliberación científica posterior a las auditorías es distinta de la auditoría. Busca formalizar, detectar inconsistencias, contradicciones, paradojas y problemas que el desarrollo o las auditorías podrían no revelar.
4. El agente científico que colabora durante el desarrollo no debe confundirse con un nuevo agente científico inicializado para una deliberación posterior.
5. El principio “buscar problemas, no culpables” guía la revisión del trabajo.
6. Softly analiza los antecedentes una vez cerrado el ciclo; no interviene en la ejecución ni influye en las conclusiones de los auditores.

Estos puntos documentan el proceso descrito y deberán contrastarse con los diagramas originales antes de convertir detalles adicionales en contratos generales.

## 6. Distinciones que el diseño debe preservar

Al modelar visibilidad, no colapsar:
- **nivel/capa arquitectónica** y **familia funcional**;
- **lectura/observación** y **escritura/intervención**;
- **visibilidad** y **autoridad**;
- **origen del registro** y **dirección de acceso**;
- **agente blando** y **agente interno de un producto**;
- **auditoría** y **deliberación científica**;
- **principio transversal** y **regla específica de un proceso**;
- **diseñado**, **prototipado**, **probado**, **validado** y **operativo**.

## 7. Estado y trabajo pendiente

**Acordado:** la visibilidad asimétrica es un principio arquitectónico fundamental del modelo general de agentes, no solo de Softly.

**Documentado como aplicación:** la capa Softly observa hacia abajo y analiza después del cierre de los ciclos, sin auditar ni intervenir.

**Pendiente:**
- contrastar la formalización con los diagramas originales del usuario;
- precisar niveles, límites y relaciones sin inventar jerarquías;
- definir contratos de registro, acceso, retención y protección;
- determinar cómo se hace cumplir técnicamente la separación de lectura, escritura e intervención;
- validar el principio con familias y proyectos contrastantes;
- distinguir invariantes del modelo de decisiones configurables por proyecto.

No se debe afirmar que este principio está implementado o probado técnicamente por el hecho de estar documentado.
