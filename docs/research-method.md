# Método de investigación y trazabilidad

## Registro de fuentes

Cada fuente tiene ID estable `SRC-YYYYMMDD-NNN` y una ficha en `research/sources/`. Registrar:
- título, autor/organización y URL canónica;
- fecha de publicación/actualización y fecha de consulta;
- tipo: especificación, documentación oficial, paper, benchmark, incidente, artículo o repositorio;
- afirmaciones que respalda, con sección/página cuando sea posible;
- método y evidencia presentados por el autor;
- limitaciones, sesgos y conflictos de interés conocidos;
- estado: vigente, reemplazada, retirada o pendiente de revisión.

No tratar snippets de buscadores como lectura completa. Abrir la fuente primaria cuando la afirmación sea importante.

## Jerarquía orientativa

1. Especificaciones, estándares, código y documentación oficial vigente.
2. Papers revisados por pares y reportes técnicos con método reproducible.
3. Informes de incidentes y análisis forense con evidencia.
4. Benchmarks con datasets y metodología públicos.
5. Experiencia técnica y artículos especializados.
6. Opinión, redes sociales y contenido promocional.

La jerarquía no es absoluta: una fuente primaria puede estar incompleta o tener interés comercial. Registrar la limitación.

## Calibración de afirmaciones

Etiquetas:
- **Verificada:** directamente respaldada por evidencia reproducible o fuente primaria clara.
- **Corroborada:** varias fuentes independientes coinciden.
- **Plausible:** evidencia parcial; faltan pruebas.
- **Hipótesis:** explicación que aún debe probarse.
- **Disputada:** fuentes o experimentos se contradicen.
- **Refutada:** evidencia suficiente contradice la afirmación.
- **No evaluada:** no se ha buscado o probado adecuadamente.

No asignar porcentajes de confianza sin método definido.

## Síntesis

Una síntesis debe incluir:
1. pregunta investigada;
2. respuesta provisional;
3. evidencia a favor;
4. evidencia en contra;
5. qué no sabemos;
6. implicaciones para diseño;
7. hipótesis siguientes;
8. fuentes enlazadas.

## Experimentos

Todo experimento debe tener ID `EXP-YYYYMMDD-NNN`, versión de agente/configuración, modelo y proveedor, dataset/casos, condiciones, variables controladas, criterios, resultados brutos o referencias seguras, análisis y limitaciones.

Registrar modelo exacto, versión del prompt, herramientas, temperatura/parámetros disponibles, contexto y fecha. Si una variable no puede conocerse, indicarlo.

## Protección de información

No almacenar tokens, API keys, credenciales, información privada ni dumps de conversaciones completas. Usar ejemplos sintéticos o anonimizados. Los datos reales requieren autorización, minimización y política de retención explícita.
