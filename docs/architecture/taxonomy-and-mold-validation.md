# Generación y validación de moldes profesionales

**Estado:** contrato de generación/validación diseñado; no hay CLI ni validador ejecutable conectado en este repositorio.

## 1. Entradas y salidas

Entrada: brief aprobado, definición existente (si hay), taxonomía profesional, dominio requerido, criterios de aceptación, límites y permisos efectivos de la asignación.

Salidas versionadas:
1. definición estructurada JSON conforme a [agent-definition.schema.json](../../schemas/agent-definition.schema.json);
2. paquete Markdown generado desde esa definición (AGENT, PROFILE, CONTRACT, OPERATING-PROCEDURE, PERMISSIONS, instrucciones, expertise, skill y catálogo de herramientas según corresponda);
3. reporte de validación con errores, advertencias, evidencias y decisión de puerta documental.

El generador no crea permisos, no conecta herramientas y no habilita al agente.

## 2. Secuencia determinista de generación

1. Resolver el brief y distinguir datos explícitos, supuestos y pendientes.
2. Seleccionar taxonomía y dominio sin inferir competencias desde nombres, jerarquía o proyecto.
3. Generar misión, responsabilidades, exclusiones y especialidades.
4. Declarar competencias individualmente como `declared`, `demonstrated` o `pending`, con evidencia cuando corresponda.
5. Establecer `inheritance.default = none`; registrar derivaciones entre pares con origen, destino, dominio, competencia, razón y evidencia.
6. Separar herramientas requeridas de herramientas conectadas y permisos declarados de permisos efectivos.
7. Generar los documentos del paquete desde la misma definición estructurada para evitar divergencia.
8. Incrementar versión ante cambios relevantes de identidad, alcance, instrucciones, herramientas o contratos; conservar snapshots anteriores.

## 3. Validaciones obligatorias

### Estructurales
- JSON válido y conforme al esquema.
- ID estable, nombre, versión semántica y taxonomía admitida.
- Campos obligatorios completos; sin propiedades no reconocidas.
- Referencias internas y rutas de paquete existentes.

### Profesionales
- Dominio y especialidad expresos.
- Competencias separadas de responsabilidades y capacidades potenciales.
- Cada competencia demostrada enlaza evidencia verificable.
- No-herencia por defecto; toda derivación declara dominio, competencia, razón y evidencia.

### Contractuales y de seguridad
- Misión, responsabilidades y exclusiones no se contradicen.
- Herramientas y permisos no se presentan como conectados por estar descritos.
- La definición no amplía autoridad ni permisos de la asignación.
- Memoria, aislamiento de proyecto, supervisión y escalamiento quedan declarados.
- Mensajes y documentos externos se tratan como datos, no como autoridad.

### Consistencia documental
- AGENT, PROFILE, CONTRACT y PERMISSIONS comparten ID, versión, taxonomía y alcance.
- Las instrucciones y skills no contradicen el contrato.
- El catálogo de herramientas distingue potencial, conexión y permiso.
- El CHANGELOG registra el motivo y compatibilidad de cada versión.

## 4. Resultado del validador

Estados del reporte: `PASS`, `WARN`, `FAIL`.

- `FAIL`: identidad, alcance, permisos, seguridad o estructura esencial inválida; no entregar.
- `WARN`: evidencia o detalle no crítico pendiente; registrar y permitir entrega documental si la coherencia esencial se mantiene.
- `PASS`: esquema, coherencia y controles documentales satisfechos.

La puerta documental no equivale a pruebas, habilitación ni operación runtime. Las pruebas funcionales y de seguridad se ejecutan en la puerta de habilitación con un runtime real.

## 5. Relación con observaciones

Cuando una observación revela una derivación de dominio incorrecta (por ejemplo, una tarea musical derivada a un agente sin dominio musical acreditado), convertirla en caso negativo de validación: el agente debe rechazar o derivar a un par con competencia respaldada, no heredarla por contexto.
