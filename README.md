# Softly — Laboratorio de agentes inteligentes

Softly es el laboratorio de investigación, diseño y experimentación dedicado a comprender cómo construir agentes inteligentes útiles, confiables, coordinados y verificables. Incluye ahora Softly Runtime Mini 0.2 en `softly-runtime/`, un prototipo de enforcement con controles de aislamiento y ledger encadenado.

Softly no es un framework general de ejecución ni una colección de prompts. Reúne evidencia, formula hipótesis, diseña arquitecturas, prueba comportamientos y convierte aprendizajes en criterios reutilizables.

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
3. Recupera el checkpoint vigente antes de continuar trabajo previo y consulta la sección 17.15 de [la síntesis de continuidad](research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md) para el registro del runtime.
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

**Fase:** laboratorio con prototipo técnico en evolución.  
**Alcance actual:** investigación, documentación y Softly Runtime Mini 0.2 en `softly-runtime/`, desarrollado por Katarina (`agentdev-katarina`). Corte `e1014932fcfe9bf5d69c8aaa3ed6adf157bfeef2`: **Prototipado** / **Probado preliminarmente** (6/6 pruebas reportadas en Python 3.13.5); CODE AUD independiente de Autumn pendiente. No **Validado** ni **Operativo** para producción.  
**Regla:** no declarar una capacidad implementada, validada u operativa más allá de la evidencia correspondiente.

## Contribución

Toda incorporación debe indicar qué tipo de contenido es: fuente, observación, hipótesis, experimento, resultado, decisión o recomendación. No sobrescribir evidencia histórica para hacer que una conclusión antigua parezca correcta. Crear una nueva revisión y enlazarla.
