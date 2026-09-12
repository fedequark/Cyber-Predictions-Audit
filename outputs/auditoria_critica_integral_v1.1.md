# Auditoría crítica integral v1.1

**Fecha:** 12 de septiembre de 2026

**Alcance:** coherencia interna, reproducibilidad, desviaciones del protocolo y publicación web.

## Dictamen

El corpus y los resultados descriptivos están cerrados y son internamente coherentes. El paquete es apto para difusión exploratoria, pero no debe declararse listo para envío académico hasta completar o resolver formalmente la validación independiente preregistrada.

## Comprobaciones superadas

| Comprobación | Resultado |
|---|---:|
| Predicciones en registro congelado | 120 |
| Filas en evaluación de desenlaces | 120 |
| Claves emparejadas y únicas | 120/120 |
| Sesiones que aportan predicciones | 36 |
| Cumplidas / incumplidas / indeterminadas | 54 / 35 / 31 |
| Acierto entre resolubles | 54/89 = 60,7% |
| Juicios binarios inconsistentes | 0 |
| Filas sin URL probatoria | 18; ningún acierto |

Los hashes publicados se reproducen sobre los bytes canónicos: el registro de extracción y el orden S3 preservan sus bytes originales; la evaluación, resultados y paper v1.0 usan UTF-8 sin BOM y LF. `.gitattributes` y el constructor del sitio fijan explícitamente esas representaciones para evitar discrepancias de checkout entre sistemas operativos.

## Desviaciones del protocolo

1. No se ejecutó la doble codificación de al menos 25% de inclusiones/exclusiones y resultados, ni la revisión de todas las atomizaciones complejas.
2. Las categorías preregistradas de cumplimiento parcial y tardío se sustituyeron por `fulfilled`, `not_fulfilled`, `indeterminate` y `mixed`. Ninguna fila terminó como `mixed`.
3. El intervalo agrupado por sesión y la media con igual peso por sesión se añadieron post hoc.
4. El preregistro fue interno y los materiales se publicaron conjuntamente después de la evaluación. El historial público no certifica por sí solo la secuencia *outcome-blind*.

## Errata de identidad

Siete predicciones usan `CCC-2013-034`, mientras el marco S3 identifica la misma sesión como `CCC-2013-043`. Coinciden orden 34, título, año y URL. Los artefactos congelados no se reescriben; los análisis derivados deben aplicar `CCC-2013-034 → CCC-2013-043`.

## Riesgos residuales

- 115/120 predicciones son clase B y dependen de operacionalización del investigador.
- *Security Nightmares* aporta 73/120 observaciones.
- No existe línea base ni probabilidades originales, por lo que no hay medida de calibración o *skill*.
- Probar ausencias históricas es asimétrico respecto de localizar eventos positivos.
- No se conservaron capturas archivísticas completas de todas las fuentes.
- El registro publicado no incluye candidatos excluidos; no puede reconstruirse el acuerdo de inclusión/exclusión sólo con estos archivos.

## Estado de publicación

La versión 1.1 preserva los CSV v1.0 y corrige la comunicación metodológica. El repositorio contiene ahora el paper, el anexo, esta auditoría, el plan de validación y la fuente del sitio. La publicación definitiva debe incluir los mismos artefactos bajo rutas estables y un release inmutable.

## Criterio de cierre académico

El estudio podrá pasar de “exploratorio cerrado” a “listo para envío” cuando:

1. una persona independiente complete el paquete ciego de desenlaces;
2. se revise la fidelidad de las operacionalizaciones clase B;
3. se recupere o reconstruya de forma auditable el universo de candidatos excluidos, o se registre formalmente que ese componente del acuerdo no puede estimarse;
4. se calculen y publiquen acuerdo porcentual, matriz de confusión y κ/α según corresponda;
5. autoría complete financiación, conflictos de interés y declaración ética;
6. el paquete se deposite en un servicio con DOI o sello temporal externo.
