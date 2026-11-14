# Softly — Laboratorio de agentes inteligentes

Softly es el espacio de investigación, diseño y experimentación dedicado a comprender cómo construir agentes inteligentes útiles, confiables, coordinados y verificables.

No es, por ahora, un framework de ejecución ni una colección de prompts. Es el laboratorio donde reunimos evidencia, formulamos hipótesis, diseñamos arquitecturas, probamos comportamientos y convertimos aprendizajes en criterios reutilizables.

## Propósito

Investigar y mejorar el diseño de agentes en todo su ciclo de vida:

- identidad, propósito e instrucciones;
- contexto, memoria y continuidad;
- razonamiento, planificación y uso de herramientas;
- autonomía, permisos y supervisión humana;
- coordinación y comunicación multiagente;
- evaluación, observabilidad y aprendizaje de fallos;
- seguridad, privacidad y resiliencia;
- despliegue, mantenimiento y evolución.

## Principio central

**No confundimos una conducta convincente con una capacidad demostrada.**

Cada afirmación importante debe distinguir evidencia, observación, hipótesis, interpretación y decisión. Cada experimento debe tener una pregunta, condiciones reproducibles y un resultado registrado.

## Cómo empezar

1. Lee [SOFTLY.md](SOFTLY.md): mandato, límites y reglas obligatorias de inicio y continuidad.
2. Usa [docs/README.md](docs/README.md) como índice de documentación transversal; luego revisa [docs/operating-model.md](docs/operating-model.md) para recuperar el método de trabajo y responsabilidades.
2. Lee [docs/operating-model.md](docs/operating-model.md): método de trabajo y responsabilidades.
3. Recupera el checkpoint vigente antes de continuar trabajo previo. Para el trabajo de molde y agentes blandos, lee las secciones 15, 16 y 17 de [la síntesis de agentes que construyen agentes](research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md): la prioridad inmediata está en 17.12. La sección 17.4 conserva una línea anterior sobre el modelo técnico de conocimiento.
4. Revisa [docs/research-method.md](docs/research-method.md): cómo investigar y conservar evidencia.
5. Consulta [research/README.md](research/README.md): fuentes, notas y estado del conocimiento.
6. Usa [agents/README.md](agents/README.md) para documentar agentes y sus versiones.
7. Usa [experiments/README.md](experiments/README.md) y [evaluations/README.md](evaluations/README.md) para convertir ideas en pruebas.
8. Para materiales aportados por gAto, consulta la [cAjita](cAjita%20del%20gAto/README.md) y el [arenero](eL%20arenero%20del%20gAto/README.md). Sus reglas de conservación son distintas.

## Mapa del repositorio

| Área | Propósito |
|---|---|
| `docs/` | Principios, arquitectura, seguridad y método |
| `research/` | Fuentes externas, fichas de lectura, síntesis y notas de casos históricos |
| `agents/` | Catálogo, perfiles y versiones de agentes |
| `experiments/` | Hipótesis, protocolos y resultados experimentales |
| `evaluations/` | Datasets, criterios, métricas y regresiones |
| `observations/` | Conductas observadas y casos que requieren explicación |
| `decisions/` | Decisiones arquitectónicas con contexto y consecuencias |
| `logs/` | Bitácora estructurada, hilos cerrados, derivados y mantenimiento |
| `schemas/` | Esquemas para mantener registros consistentes |
| `templates/` | Plantillas reutilizables |
| `archive/` | Material histórico que ya no es operativo |
| `cAjita del gAto/` | Material valioso que conviene consultar y conservar |
| `eL arenero del gAto/` | Material temporal pendiente de clasificación |

## Estado

**Fase:** fundación del laboratorio.  
**Alcance actual:** investigación y documentación; no hay runtime de agentes implementado.  
**Regla:** no declarar una capacidad implementada hasta que exista código, prueba y evidencia correspondiente.

## Contribución

Toda incorporación debe indicar qué tipo de contenido es: fuente, observación, hipótesis, experimento, resultado, decisión o recomendación. No sobrescribir evidencia histórica para hacer que una conclusión antigua parezca correcta. Crear una nueva revisión y enlazarla.
