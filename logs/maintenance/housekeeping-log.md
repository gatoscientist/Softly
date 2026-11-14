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
