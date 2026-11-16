# Análisis de consistencia — tipos, taxonomías e identidades

**ID:** REG-MODEL-REVIEW-2026-001  
**Fecha:** 2026-11-16  
**Emite:** Softly  
**Alcance:** contraste documental entre los diagramas de referencia de taxonomía/tipos y el registro JSON vigente.  
**Estado:** análisis y recomendación; no modifica ni aprueba el modelo normativo.

## 1. Dictamen

El registro actual mezcla conceptos que los diagramas de referencia muestran separados. La brecha no se resuelve agregando o quitando nombres del arreglo `taxonomies`: primero hay que definir qué representa cada campo.

Los diagramas distinguen, al menos visualmente:
- **Tipo/familia de agente:** DEV, AUD, UX y SEC; SCI aparece como categoría especializada.
- **Dominio profesional o taxonomía:** UX, AUD, SCI, SEC y DEV.
- **Disciplina/especialidad:** GUI aparece subordinada a UX; TeamWork y Code aparecen como especialidades de AUD.
- **Identidad:** el sujeto concreto que tiene mandato y responsabilidad.
- **Capacidad:** lo que ese sujeto puede hacer con evidencia y límites.

El JSON vigente, en cambio, usa `taxonomy` con valores `AgentDEV`, `AgentSEC`, `AgentMUS`, `AgentSCI` y `Auditoría`, y registra sujetos concretos en `agents[]`. No contiene campos separados para tipo de agente, especialidad, rol institucional o capacidad. Por eso una entrada puede leerse simultáneamente como identidad, familia profesional y disponibilidad.

## 2. Diferencias verificables

| Elemento | Diagramas de referencia | Registro vigente | Observación |
|---|---|---|---|
| DEV | Tipo y dominio profesional | `AgentDEV` | Coincidencia conceptual parcial; nomenclatura distinta |
| AUD | Tipo/dominio, con TeamWork y Code | `Auditoría` | Las especialidades no están modeladas como tales |
| UX | Tipo/dominio profesional | Ausente | Brecha |
| GUI | Disciplina especializada bajo UX | Ausente | No debería agregarse como identidad por defecto |
| SEC | Tipo/dominio de seguridad | `AgentSEC` | Coincidencia parcial |
| SCI | Dominio de ciencias formales | `AgentSCI` | Coincidencia parcial |
| MUS | No aparece en los diagramas entregados | `AgentMUS` | Puede ser evolución posterior o extensión; falta declarar procedencia |

El punto principal no es que MUS esté mal ni que UX/GUI deban incorporarse automáticamente. Es que no existe una regla documental que explique la relación entre las dos representaciones.

## 3. Modelo conceptual mínimo candidato

Como alternativa de diseño para deliberación, recomiendo mantener tres dimensiones conceptuales:

1. **Identidad:** quién es el sujeto, cuál es su casa canónica, versión y mandato.
2. **Dominio/taxonomía profesional:** en qué campo trabaja; puede contener disciplinas o especialidades jerárquicas.
3. **Capacidades:** qué operaciones y competencias concretas tiene autorizadas, con evidencia, límites y nivel de confianza.

Los repositorios, paquetes, versiones y commits son **procedencia y trazabilidad**, no una cuarta dimensión de identidad. El rol institucional (coordinación, ingeniería, auditoría) debe quedar como atributo de responsabilidad del mandato, no confundirse con dominio profesional. Las asignaciones temporales deben ser registros de vigencia y alcance, no identidades permanentes.

Este modelo es una recomendación técnica, no una decisión de Dirección. No se debe migrar el JSON hasta que gAto apruebe las definiciones y sus relaciones.

## 4. Coordinación sistémica: pregunta abierta de Katarina

Se conserva expresamente la pregunta: **¿la orquestación cubre por sí sola la coordinación sistémica transversal?**

Mi lectura provisional:
- La orquestación suele ordenar tareas, responsables, dependencias y secuencias.
- La coordinación sistémica observa además coherencia entre repositorios, contratos, gobernanza, estados, retroalimentación, efectos emergentes y continuidad temporal.
- Ambas pueden ser una sola capacidad si el contrato de orquestación incluye explícitamente esas responsabilidades y criterios de observación.
- Si el contrato solo coordina tareas locales, la cobertura sistémica no está demostrada.

No recomiendo crear una cuarta dimensión ni una identidad nueva para resolverlo. Primero hay que comprobar si el contrato de Softly incluye la observación y regulación transversal del sistema, y qué señales/evidencias permiten demostrarlo. Si ya está cubierto, se documenta como alcance de orquestación; si no, se define como capacidad transversal, sin convertirla automáticamente en nueva taxonomía o agente.

## 5. Riesgos de migrar antes de decidir

1. Convertir disciplinas (GUI) en identidades invocables.
2. Confundir el dominio profesional con el tipo institucional de agente.
3. Perder la procedencia de taxonomías históricas o extensiones como MUS.
4. Tratar disponibilidad documental como estado operativo.
5. Asignar competencias por pertenencia a una taxonomía, pese a la regla de no herencia por defecto.
6. Codificar como arquitectura una decisión todavía abierta sobre coordinación sistémica.

## 6. Recomendación

**NO-GO para modificar el registro vigente. GO para cerrar el diseño conceptual mediante una decisión explícita de Dirección.**

Antes de preparar schema 2.0, deben quedar aprobadas estas definiciones:
- qué significa “tipo de agente”;
- qué significa “taxonomía/dominio”;
- cómo se representan disciplinas y especialidades;
- cómo se separan identidad, mandato y capacidad;
- cómo se registran asignaciones temporales;
- cómo se demuestra que la orquestación cubre la coordinación sistémica.

Hasta entonces, preservar el JSON 1.0.0 y su historial, no cambiar disponibilidad ni versiones, y no añadir/eliminar categorías por inferencia. Este análisis no altera identidades, permisos, contratos ni estados operativos.
