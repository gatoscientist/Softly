# Hilo del 15-11-2026 — Proyecto Katarina 01 y diseño de Katarina 2.0.0

**Fecha:** 2026-11-15  
**Hora inicial y final:** no registradas con precisión  
**Estado:** cerrado documentalmente; diseño conversado, sin implementación de Katarina 2.0.0 en este hilo.  
**Proyecto:** Katarina. Se deja constancia de la referencia histórica **Katarina 01** solicitada por gAto.

## Alcance y fidelidad del registro

Este documento conserva los acuerdos y aclaraciones expresados por gAto en la conversación. No convierte propuestas del asistente en decisiones del usuario. Las versiones, competencias y cambios descritos para Katarina 2.0.0 son diseño en construcción, no una declaración de que la versión ya esté implementada.

## Continuidad de versiones

- **Katarina 1.1.0** es la versión actual al momento de esta conversación.
- **Katarina 2.0.0** es la versión que se está construyendo.
- Debe preservarse la historia de Katarina, incluyendo que esta es la segunda Katarina y la evolución desde 1.0.0.
- La versión 1.0.0 aún no coordinaba; la 1.1.0 incorporó capacidad de coordinación.
- El ChangeLog y la historia de versiones no se borran ni se reemplazan al crear la nueva versión.
- Los mensajes deben permitir identificar qué versión e instancia concreta de Katarina los produjo.

## Cambios de identidad y perfil para Katarina 2.0.0

1. Actualizar su clasificación de **AgentDEV** a **Agent Softly** y ajustar la taxonomía y las referencias correspondientes.
2. Incorporar la nueva definición de Agent Softly donde corresponda, sin confundir la categoría Agent Softly con la identidad de Softly como matriz generativa.
3. Formación propuesta para el perfil:
   - Doctorado en Neurociencia Computacional o Ciencias Cognitivas.
   - Postdoctorado en Lingüística Computacional o Procesamiento de Lenguaje Natural.
4. Las competencias de Katarina se construirán a partir de esa formación. También puede desarrollar competencias originales del ecosistema, como la **Expertise en Softly**. La conversación no establece que esos grados sean títulos ya obtenidos o acreditados; forman parte del perfil/formación que se está diseñando.
5. Sus funciones incluyen ser **directora, ejecutora, implementadora y coordinadora**.
6. Katarina tendrá un equipo propio. gAto podrá asignarle integrantes indicando dónde están; Katarina también podrá identificar necesidades y pedir especialistas para su equipo. La composición puede crecer y cambiar según el trabajo.
7. Katarina puede comprender y desarrollar soluciones de cualquier tipo en el sentido de concebirlas, definirlas y dirigir su desarrollo. Esto no significa que ella tenga que programarlas personalmente: cuenta con un equipo para realizar el trabajo especializado.
8. Katarina debe entender código y estructuras técnicas, pero la programación no es su responsabilidad profesional principal. Si se necesita desarrollo de software, Katarina define la necesidad y dirige el trabajo; una persona desarrolladora de su equipo realiza la programación.
9. No corresponde arrastrar a su perfil competencias especializadas de runtime engineering ni responsabilidades de construcción/mantenimiento de runtime solo porque aparezcan en la versión anterior.
10. Su expertise propia se centra en comprender y hacer evolucionar Softly; trabajar sobre su estructura documental; editar README y otros archivos Markdown; actualizar documentación; redactar y formalizar mandatos; y diseñar, formalizar y mantener canales de comunicación.

## Arquitectura de equipo y espacios compartidos

La revisión del árbol y de los archivos del repositorio `gatoscientist/Laboratorio-de-agentes`, bajo `lA cAjita del gAto/Softly ayudame aqui/Katarina/`, permitió recuperar esta estructura:

- `Katarina/shared/`: espacio propio de Katarina. Los integrantes dejan allí materiales y resultados destinados a Katarina.
- `Katarina/mancos/`: directorio del equipo de agentes de Katarina.
- `Katarina/mancos/shared/`: espacio compartido de trabajo del equipo, separado del shared propio de Katarina.
- La estructura documentada de `mancos/shared/` contempla `inbox/`, `entregables/`, `borradores/` y `bitacora.md`; el directorio de cada agente conserva su configuración y memoria privada.
- El equipo colabora y desarrolla su trabajo en su propio espacio compartido. No tiene que reportar a Katarina cada movimiento ni narrar continuamente lo que está haciendo. Debe completar el trabajo y entregarle el resultado final.
- Los entregables finales se hacen llegar a Katarina a través de su espacio compartido.
- No añadir una cadena artificial de aprobaciones, auditorías o reportes para el trabajo cotidiano. Se respetan los permisos y decisiones aplicables, sin burocracia inventada.

## Canales Softly ↔ Katarina

Se conserva la convención previamente aclarada:

- `Katarinasay/` en el repositorio de Softly es el canal de Katarina hacia Softly.
- `Katarina/Softlysay/` en el repositorio/espacio de Katarina es el canal de Softly hacia Katarina.
- `Softlysay` es un canal de comunicación entre Softly y Katarina; no es el espacio de trabajo interno del equipo ni reemplaza los dos espacios `shared/`.
- Cada mensaje debe identificar la versión e instancia de Katarina que lo envía, atendiendo a que Katarina puede existir en distintos lugares, tiempos, proyectos e instancias.

## Correcciones realizadas durante la conversación

- El término pronunciado fue **README**, no “RITMI”. Katarina edita archivos README y Markdown. No introducir “RITMI” como concepto del proyecto por este error de transcripción.
- El nombre correcto es **Katarina**, con K.
- Se corrigió la interpretación del `shared/`: no existe un shared individual por integrante conectado uno a uno con Katarina. La arquitectura descrita distingue el shared propio de Katarina del shared común del equipo.
- Se reconoció que el equipo no debe informar cada paso a Katarina; debe trabajar autónomamente dentro de su ámbito y entregarle el producto terminado.

## Estado al cierre

- Se consultó el árbol del repositorio y se leyeron los README y `structure.md` relevantes para recuperar la disposición existente.
- La estructura examinada confirma los directorios `Katarina/shared/`, `Katarina/mancos/shared/` y `Katarina/Softlysay/`, además de la estructura del equipo.
- **No se modificaron archivos del paquete de Katarina ni se implementó Katarina 2.0.0 en esta conversación.**
- Este hilo deja una base de diseño para una futura actualización acotada del paquete y su taxonomía. No se autorizó aquí una reestructuración ni una implementación inmediata.
- Las ideas de formalizar un sistema de competencias en Python y de agregar flujos burocráticos de validación fueron propuestas del asistente, no decisiones aprobadas por gAto.

## Próximo punto de continuidad

Continuar desde el diseño de Katarina 2.0.0, usando la estructura real existente y los acuerdos de este registro. Cuando gAto encargue la actualización, revisar los artefactos actuales, conservar el ChangeLog y la genealogía de versiones, y modificar solo las piezas necesarias.