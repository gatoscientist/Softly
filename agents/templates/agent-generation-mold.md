# Molde universal de creación y evolución de agentes

**Estado:** molde operativo canónico.  
**Salida documental predeterminada:** versión 1.0.0, estado Diseñado para agentes nuevos, salvo instrucción distinta de gAto.  
**Propósito:** producir paquetes profesionales, claros, portables y utilizables sin convertir la creación en una fase académica.

## 1. Entrada y criterio de avance

La entrada es el brief de gAto, que puede ser libre e incompleto. Extraer lo conocido y distinguir supuestos. No exigir campos no esenciales para empezar. Preguntar solo si falta un dato que cambie la identidad, misión, alcance, permisos o seguridad del agente.

## 2. Dimensiones que no deben confundirse

- Identidad y misión.
- Taxonomía profesional y dominio.
- Especialidades y competencias.
- Responsabilidades y exclusiones.
- Herramientas requeridas, disponibles y conectadas.
- Permisos declarados y permisos efectivos.
- Definición portable, asignación a proyecto y contexto de sesión.

No heredar competencias, permisos o herramientas por taxonomía, jerarquía, proyecto o relación entre agentes. Toda derivación entre pares declara dominio, competencia, razón y evidencia.

## 3. Proceso de creación en Modo Fábrica

1. Interpretar el resultado solicitado.
2. Resolver nombre/ID, misión, taxonomía y dominio usando el brief; completar detalles no críticos con supuestos explícitos.
3. Definir responsabilidades, límites, exclusiones y relaciones de coordinación.
4. Declarar especialidades y competencias sin inflar capacidades; separar lo demostrado de lo requerido o pendiente.
5. Definir procedimiento, entradas, salidas, formatos de entrega y criterios de calidad.
6. Definir memoria, aislamiento de contexto, herramientas y permisos sin inventar conexiones ni autoridad.
7. Generar los documentos del paquete desde una identidad y versión coherentes.
8. Aplicar la checklist declarativa durante la generación; corregir solo defectos esenciales.
9. Entregar directamente el paquete en versión 1.0.0, estado Diseñado, salvo indicación distinta.
10. Registrar pendientes no críticos como notas; no retener el artefacto principal.

## 4. Paquete documental

Seleccionar los documentos que correspondan al alcance, evitando archivos vacíos o ceremoniales:

- AGENT.md: identidad, misión, reglas de conducta y límites.
- PROFILE.md: perfil funcional, dominio y especialidades.
- CONTRACT.md: responsabilidades, entradas, salidas, autoridad e interfaces.
- OPERATING-PROCEDURE.md: procedimiento práctico y ciclo de trabajo.
- PERMISSIONS.md: permisos requeridos, límites y aprobaciones; no concede permisos.
- instructions/system.md: instrucciones ejecutivas del agente.
- expertise/: conocimiento de dominio necesario.
- skills/: procedimientos reutilizables.
- tools/: catálogo de herramientas y estado real de disponibilidad.
- version.json y CHANGELOG.md: identidad/versionado y trazabilidad.
- README.md: entrada rápida al paquete.

El paquete debe adaptarse al agente y no copiar especialidades ni restricciones de otro.

## 5. Puerta de Entrega Documental

La entrega está lista cuando el agente tiene identidad y misión claras, taxonomía/dominio declarados, responsabilidades y límites coherentes, contrato utilizable y documentos esenciales consistentes.

**Valores predeterminados:**
- Versión 1.0.0.
- Estado Diseñado.
- Taxonomía profesional del catálogo oficial.
- Competencias no demostradas identificadas honestamente.

La entrega documental no requiere pruebas runtime, integración, despliegue ni certificación experimental. No usar Experimental ni draft como estado de madurez del paquete. Los pendientes no críticos se anotan y el paquete se entrega.

Solo detener el artefacto afectado ante un defecto esencial y concreto de identidad, alcance, contradicción contractual o seguridad. Corregir ese defecto específico, sin abrir una investigación general.

## 6. Checklist declarativa

Aplicar docs/agent-delivery-checklist.md durante la generación:
- identidad, ID, versión y estado consistentes;
- misión, responsabilidades y exclusiones claras;
- taxonomía, dominio, especialidades y competencias diferenciados;
- no-herencia por defecto y derivaciones justificadas;
- contrato, procedimiento, permisos y contexto coherentes;
- herramientas requeridas separadas de las disponibles;
- archivos esenciales y referencias internas correctos;
- supuestos no críticos anotados;
- commit y relectura desde main si se entrega en GitHub.

La checklist es una auto-revisión de producción, no una aprobación externa. Resultado: **ENTREGAR**, o **CORREGIR** un defecto esencial específico. No existe estado intermedio de espera por pruebas no solicitadas.

## 7. Evolución y cierre de decisiones

Para modificar un agente existente, conservar su identidad y versión previa; incrementar la versión según el cambio solicitado y registrar el motivo. No reabrir decisiones cerradas sin petición de gAto o evidencia nueva, concreta y pertinente.

## 8. Principio rector

Crear y entregar el agente mínimo que cumpla bien su misión. La calidad se demuestra en la claridad, coherencia y utilidad del paquete; la investigación y las pruebas posteriores son actividades separadas que se realizan cuando se solicitan.
