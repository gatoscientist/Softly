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
2. Usa [docs/README.md](docs/README.md) como índice de documentación transversal y consulta [docs/operating-model.md](docs/operating-model.md) para recuperar el método de trabajo.
3. Recupera el checkpoint vigente antes de continuar trabajo previo. La prioridad operativa actual es asegurar la integridad y el funcionamiento de Softly; el desarrollo de agentes descrito en la sección 17.12 está en pausa hasta que gAto confirme el cierre de las mejoras. Consulta la sección 17.14 de [la síntesis de continuidad](research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md).
4. Revisa [docs/research-method.md](docs/research-method.md): cómo investigar y conservar evidencia.
5. Consulta [research/README.md](research/README.md): fuentes, notas y estado del conocimiento.
6. Usa [agents/README.md](agents/README.md) para documentar agentes y sus versiones.
7. Usa [experiments/README.md](experiments/README.md) y [evaluations/README.md](evaluations/README.md) para convertir ideas en pruebas.
8. Para materiales aportados por gAto, consulta la [cAjita](cAjita%20del%20gAto/README.md) y el [arenero](eL%20arenero%20del%20gAto/README.md). Sus reglas de conservación son distintas.

## Mapa del repositorio

| Área | Propósito |
|---|---|
| [`docs/`](docs/README.md) | Principios, arquitectura, seguridad y método |
| [`research/`](research/README.md) | Fuentes externas, fichas de lectura, síntesis y notas de casos históricos |
| [`agents/`](agents/README.md) | Catálogo, perfiles y versiones de agentes |
| [`experiments/`](experiments/README.md) | Hipótesis, protocolos y resultados experimentales |
| [`evaluations/`](evaluations/README.md) | Datasets, criterios, métricas y regresiones |
| [`observations/`](observations/README.md) | Conductas observadas y casos que requieren explicación |
| [`decisions/`](decisions/README.md) | Decisiones arquitectónicas con contexto y consecuencias |
| [`logs/`](logs/README.md) | Bitácora estructurada, hilos cerrados, derivados y mantenimiento |
| [`schemas/`](schemas/README.md) | Esquemas para mantener registros consistentes |
| [`templates/`](templates/README.md) | Plantillas reutilizables |
| [`archive/`](archive/README.md) | Material histórico que ya no es operativo |
| [`cAjita del gAto/`](cAjita%20del%20gAto/README.md) | Material valioso que conviene consultar y conservar |
| [`eL arenero del gAto/`](eL%20arenero%20del%20gAto/README.md) | Material temporal pendiente de clasificación |

## Estado

**Fase:** fundación del laboratorio.  
**Alcance actual:** investigación y documentación; no hay runtime de agentes implementado.  
**Regla:** no declarar una capacidad implementada hasta que exista código, prueba y evidencia correspondiente.

## Contribución

Toda incorporación debe indicar qué tipo de contenido es: fuente, observación, hipótesis, experimento, resultado, decisión o recomendación. No sobrescribir evidencia histórica para hacer que una conclusión antigua parezca correcta. Crear una nueva revisión y enlazarla.
