# Softly — Laboratorio de agentes inteligentes

Softly es el laboratorio de investigación, diseño y experimentación dedicado a comprender cómo construir agentes inteligentes útiles, confiables, coordinados y verificables. El ciclo de Softly Runtime Mini 0.2 quedó cerrado administrativamente en el corte `9e8bc10` de `main`, con sus limitaciones documentadas. La prioridad activa es el desarrollo de TITAN con el equipo DEVAGENTS 1.0.0 ya entregado en [Laboratorio-de-agentes](https://github.com/gatoscientist/Laboratorio-de-agentes/tree/main/Soft%20Agents/TITAN/eL%20equipo%20del%20gAto).

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
3. Recupera el checkpoint vigente antes de continuar trabajo previo y consulta la sección 17.16 de [la síntesis de continuidad](research/syntheses/2026-11-13-de-agentes-que-construyen-agentes.md) para el cierre administrativo de Mini 0.2 y la prioridad actual de TITAN.
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

**Fase:** investigación y desarrollo documental; prioridad activa: TITAN.  
**Cierre anterior:** el ciclo de Softly Runtime Mini 0.2 quedó cerrado administrativamente en el corte `9e8bc10` de `main`, con limitaciones documentadas. El cierre no declara validación ni operación de producción.  
**Equipo activo de desarrollo:** Tiffany (AgentDEV), Tara (AgentSEC), Thea (AgentMUS) y Tábata (AgentSCI), paquetes completos `1.0.0` en estado `Diseñado`, entregados en [Laboratorio-de-agentes](https://github.com/gatoscientist/Laboratorio-de-agentes/tree/main/Soft%20Agents/TITAN/eL%20equipo%20del%20gAto).  
**Regla:** no declarar una capacidad implementada, validada u operativa más allá de la evidencia correspondiente.

## Contribución

Toda incorporación debe indicar qué tipo de contenido es: fuente, observación, hipótesis, experimento, resultado, decisión o recomendación. No sobrescribir evidencia histórica para hacer que una conclusión antigua parezca correcta. Crear una nueva revisión y enlazarla.
