# Propuesta de registro de identificadores y relaciones

**Estado:** propuesta descriptiva no normativa. No modifica el esquema JSON vigente ni autoriza migraciones.

## Objetivo

Evitar colisiones y ambigüedad entre identificadores que representan entidades documentales diferentes. La unicidad debe evaluarse dentro de cada namespace y la relación entre artefactos debe expresarse sin reutilizar el ID de otro tipo.

## Namespaces observados

| Prefijo | Entidad | Uso observado | Regla propuesta |
|---|---|---|---|
| `SRC-YYYYMMDD-NNN` | Fuente individual | Fuente externa o documento individual citado | Un ID por fuente/versionado de origen; no asignar sin metadatos verificables |
| `SRCSET-YYYYMMDD-NNN` | Conjunto de fuentes | Panorama o conjunto curado | Agrupa IDs SRC; no sustituye sus fichas |
| `ING-YYYYMMDD-NNN` | Evento de ingesta | Registro de recepción/incorporación | Identifica el evento y su procedencia; puede relacionar varios SRC |
| `SYN-YYYYMMDD-NNN` | Síntesis | Documento que integra evidencia | Un ID único por documento de síntesis; nunca reutilizar tras reasignación |
| `SOFT-RES-NNN` | Nota/recurso de investigación | Ficha exploratoria interna | Mantener separado de fuentes y síntesis |
| `ADR-NNNN` | Decisión | Decisión arquitectónica | Un ID por decisión; reemplazos se enlazan, no sobrescriben |
| `EVT-YYYYMMDD-NNN` | Evento de bitácora | Actividad registrada | ID único por evento dentro del registro de actividad |

## Relaciones recomendadas

- Una nota, síntesis o decisión puede citar uno o más SRC.
- Un SRC puede formar parte de uno o más SRCSET.
- Un ING registra la recepción de uno o más originales y puede generar fichas SRC; no equivale a la fuente misma.
- Una SYN deriva de fuentes, notas u otras síntesis y debe declarar sus dependencias.
- Una ADR puede reemplazar otra ADR, conservando el historial y el enlace bidireccional.
- Una fuente local/adjunta puede tener ubicación o identificador de adjunto y hash solo cuando los bytes estén disponibles; no inventar URL pública.

## Reglas de integridad propuestas

1. No reutilizar IDs retirados o reasignados; registrar la transición y su motivo.
2. Comprobar unicidad del ID en todo el árbol antes de aceptar un documento.
3. Mantener índice humano por namespace y referencias cruzadas desde los índices de directorio.
4. Distinguir fuente original, copia, versión, ingesta, nota derivada y síntesis.
5. Para archivos binarios, registrar nombre, ruta, tamaño y hash criptográfico calculado sobre los bytes; el Git blob SHA no sustituye un hash de archivo independiente.
6. Validar sintaxis y relaciones con herramientas automatizadas solo después de aprobar y versionar el contrato.

## Decisiones pendientes

- Aprobar o corregir esta taxonomía.
- Definir representación formal de fuentes locales/adjuntos sin URL.
- Definir cardinalidad, campos de procedencia y versionado de registros.
- Diseñar migración y ejemplos válidos antes de tocar `schemas/research-record.schema.json`.

**Límite:** esta propuesta describe el estado observado y una convención sugerida. No es estándar vigente ni debe tratarse como instrucción normativa hasta su aprobación.
