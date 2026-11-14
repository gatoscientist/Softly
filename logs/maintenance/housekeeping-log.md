# Bitácora de orden de la casita

Registro acumulativo de mantenimiento. Su propósito es aprender de los problemas de organización y prevenir que vuelvan a aparecer.

## 2026-11-14 — Índices, inventario y navegación

**Estado observado**
- La cAjita y los areneros no tenían índices propios en Softly.
- En Softly coexistían `eL aRenero del gAto/` y `eL arenero del gAto/`, con instrucciones en una ruta y materiales en la otra.
- El arenero del Laboratorio no tenía índice raíz.
- Los ocho ZIP de TITAN estaban almacenados sin un inventario descriptivo del directorio.
- Se encontró un enlace relativo roto en el README de Auditoría del arenero del Laboratorio.
- Los snapshots `.old` contienen archivos con hashes idénticos a sus versiones actuales, pero representan historia deliberada.
- El TXT que permanece en el arenero Softly pide postergar el orden y registrar futuras limpiezas; no contiene «pico pal que lee».

**Causas observadas e hipótesis**
- **Evidencia:** faltaban README de navegación en varios directorios y existían rutas con capitalización diferente.
- **Hipótesis:** parte del desorden proviene de incorporar materiales a medida que evoluciona el trabajo, sin crear siempre un índice en el mismo momento.
- **Evidencia:** los enlaces relativos pueden quedar mal cuando los documentos se copian o cambian de carpeta.
- **Hipótesis:** los snapshots duplicados pueden parecer basura si no se explica su función histórica.

**Acciones realizadas**
- Se crearon índices para la cAjita y el arenero de Softly, la carpeta de instrucciones con capitalización distinta y el arenero del Laboratorio.
- Se crearon índices para `Proyectos/` y `Proyectos/TITAN/`, con inventario de los ocho ZIP y sus blob SHAs.
- Se conectaron los índices desde las portadas de ambos repositorios.
- Se registraron los nueve PDF y el TXT presente en el arenero Softly, con tamaños y Git blob SHAs.
- Se corrigió el enlace roto de `eL arenero del gAto/AUDITORIA/README.md`.
- Se compararon hashes y se conservaron los snapshots históricos.
- Se auditaron enlaces Markdown locales en los 66 archivos de Softly y los 71 archivos vigentes del Laboratorio (excluidos snapshots `.old/`). Se corrigió el único enlace roto encontrado en el Laboratorio; los destinos locales de los demás archivos revisados existen.
- No se movió ni eliminó material del arenero o cAjita. No se modificaron agentes ni contratos.

**Resultado**
- Los índices y portadas enlazan a rutas existentes.
- Los ocho ZIP de TITAN tienen blob SHAs distintos: no hay duplicados binarios exactos dentro de ese conjunto.
- Dos registros de Biblioteca llamados `Auditoría TITAN.pdf` y `Auditoría TITAN(1).pdf` tienen igual tamaño y fragmentos de texto coincidentes; son duplicados probables de contenido, no identidad binaria demostrada.
- Se verificaron commits y árboles completos en ambos repositorios. Ver el [registro técnico detallado](2026-11-14-audit-follow-up.md).

**Aprendizajes preventivos**
1. Crear o actualizar un README cada vez que se incorpora un directorio de trabajo con propósito propio.
2. Mantener una ruta canónica y revisar la capitalización antes de crear carpetas; Git distingue mayúsculas y minúsculas.
3. No confiar en nombres de archivos para inferir contenido ni duplicación.
4. Comparar blob SHAs antes de considerar duplicados exactos; para ZIP/PDF, inspeccionar contenido interno antes de limpiar.
5. Revisar enlaces relativos después de copiar o mover documentos.
6. Hacer inventario antes de cualquier limpieza y registrar por qué se desordenó la casita.
7. No borrar snapshots históricos solo porque coincidan con la versión vigente.

**Pendientes**
- Determinar cuál era el TXT que gAto eliminó y que contenía «pico pal que lee»; no corresponde al único TXT que sigue en el árbol Softly.
- Resolver la diferencia de capitalización entre las dos carpetas del arenero Softly.
- Inspeccionar internamente los PDF/ZIP y comprobar respaldos antes de proponer eliminaciones.
- Continuar auditoría exhaustiva de enlaces externos y Markdown históricos del Laboratorio.


### Extensión de la misma pasada: recuperación de investigación

Se revisaron los dos documentos de investigación/guía del arenero del Laboratorio y se contrastaron con el modelo y molde vigentes de Softly. Se confirmó que son complementarios, no duplicados exactos. Se creó una síntesis en `research/notes/2026-11-14-cruce-estructura-agentes-soft.md`, se indexó desde investigación y se enlazó desde el índice del arenero del Laboratorio. Los originales permanecen en su ubicación.

**Aprendizaje añadido:** antes de descartar material del arenero, compararlo con el conocimiento canónico y buscar aportes complementarios. Un documento que comparte tema con otro no es necesariamente redundante; puede contener un nivel distinto (fundamentos, guía operativa, modelo lógico o procedimiento).


### Índices de documentación y espacios Soft Agents

Se completó la navegación de directorios de mayor valor: en Softly se añadieron índices para documentación, arquitectura, gobernanza, plantillas, hilos y fuentes; en el Laboratorio se añadieron índices para la raíz de Soft Agents, TITAN, Cytryna, GatoSD, gAtoSD y los perfiles de referencia de auditoría. Se enlazaron dos comentarios de gAto que estaban sin índice: la obsolescencia observada de la estructura de auditoras y la crítica al manual de TITAN.

Los índices restantes sin README corresponden a directorios de un solo archivo, snapshots o carpetas TEAM que no se modificaron. La ausencia de un README se deja como decisión consciente, no como deuda automática.


## Verificación terminal de la pasada — 2026-11-14

- Softly: 74 archivos Markdown, 30 README; enlaces locales de todos los documentos nuevos/actualizados comprobados y cobertura de los 66 archivos previos completada.
- Laboratorio: 127 archivos Markdown en total; 77 vigentes fuera de `.old/`, con enlaces locales revisados. Se corrigió el único enlace roto encontrado.
- Árboles completos y ramas sin divergencia respecto del punto de inicio de la pasada. No se modificaron contratos ni agentes.
- La cobertura se limita a enlaces locales; no equivale a validar destinos externos, ejecución runtime ni contenido binario de PDF/ZIP.


## 2026-11-14 — Auditoría recursiva del árbol y reconciliación de índices

**Corte Git verificado:** `main`, HEAD `9037434d793bbdbd6aca510b474dea1d9ac8ae2e`, árbol recursivo completo (`truncated=false`).

**Estado observado**
- El repositorio contiene 124 entradas: 90 blobs y 34 directorios; 76 Markdown, 30 README, 9 PDF, 1 TXT, 2 JSONL y 1 JSON.
- No hay blobs con SHA repetido en el árbol actual.
- La única colisión de ruta sin distinguir mayúsculas/minúsculas es la pareja documentada de directorios del arenero.
- Seis directorios de evaluación/experimentos contienen solo su README y no tienen aún artefactos. Se consideran scaffolding intencional, no basura.
- Tres archivos históricos no aparecían enlazados desde su índice: el hilo archivado de Audelin, el registro de directiva de identidad y la bibliografía.
- Había referencias documentales a una prioridad operativa antigua, dos JSONL inexistentes y un directorio `experiments/artifacts/` inexistente.
- El inventario actual de Biblioteca muestra un único `Auditoría TITAN.pdf` de 314.786 bytes; no aparece el segundo registro citado en la nota anterior.

**Acciones realizadas**
- Se actualizó el README raíz para reflejar que la integridad de Softly es la prioridad y que el desarrollo de agentes está en pausa.
- Se aclaró en `logs/README.md` que `incidents.jsonl` y `observations.jsonl` todavía no existen.
- Se corrigió `experiments/README.md` para no presentar `artifacts/` como directorio presente.
- Se enlazó el hilo de Audelin desde `archive/README.md`, el registro de identidad desde `logs/README.md` y la bibliografía desde `research/README.md`.
- Se corrigió la nota de comparación con Biblioteca en el README del arenero: el inventario actual muestra un solo registro de Auditoría TITAN, y la igualdad de tamaño no prueba identidad binaria.
- Se amplió la matriz de procedencia con el inventario recursivo, los seis directorios scaffolding, las colisiones, los enlaces añadidos y las limitaciones de inspección binaria.

**Commits de esta intervención**
- `ed062d1b7374f29e0521752acacf1aa2ba33cd96` — README raíz.
- `1e2dabcb8828c5471f776ac780df8bd2579745a0` — índice de logs.
- `93231b0c46f8bdb41b9d0049fe96712f2782bf58` — índice de experimentos.
- `8c66f84e594b64f7085cc0f0bef04525bede03ef` — índice del archivo histórico.
- `2efb9f3d0347988a05b0fd755ce6483fc6bbb68d` — índice de logs/registro de identidad.
- `9037434d793bbdbd6aca510b474dea1d9ac8ae2e` — índice de investigación/bibliografía y HEAD observado antes de esta ampliación.
- `3e646d58da6bb85e478c3d84b82d6af89e5c1e73` — corrección de evidencia de Biblioteca en el README del arenero.
- `500d97b35129df7b2865a11a4d6a252a05768c96` — ampliación de la matriz.

**Pendientes**
- Inspeccionar internamente los nueve PDF y cotejar respaldos binarios independientes. La Biblioteca solo expone texto indexado de un archivo y no permite comparar el binario con el blob Git.
- Revisar destinos externos y dependencias semánticas no expresadas como enlaces; la comprobación de enlaces Markdown locales en los 76 archivos terminó con cero destinos rotos.
- Completar la matriz de procedencia con fechas de incorporación, aportantes y destinos de respaldo cuando haya evidencia.
- No borrar ni fusionar carpetas del arenero sin resolver su intención con evidencia suficiente.

**Aprendizaje preventivo:** los índices también envejecen. Una revisión de árbol debe contrastar README, rutas reales y prioridad normativa, no limitarse a comprobar que los archivos existen. Los directorios que solo contienen README pueden ser estructuras deliberadas y no deben tratarse como residuos automáticamente.


### Verificación adicional de enlaces Markdown — 2026-11-14

Se leyeron los 76 archivos Markdown desde el árbol actual y se comprobaron los destinos relativos de todos los enlaces Markdown inline detectados. Resultado: **cero destinos locales rotos**. Los destinos HTTP/HTTPS no se validaron; tampoco se evaluaron referencias semánticas no expresadas como enlaces.
