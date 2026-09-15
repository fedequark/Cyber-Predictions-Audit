# Diagnósticos adicionales v1.3

**Fecha:** 15 de septiembre de 2026. **Estado:** exploratorio/post hoc.
Esta capa no sustituye la evaluación congelada ni resuelve por decreto los 31 casos indeterminados.

## 1. Influencia de cada sesión

Se eliminaron, una por una, las 36 sesiones aportantes y se recalculó la proporción entre los casos resolubles restantes. El 60,7% original queda entre **58,5%** (sin `VB-2016-P01`) y **63,5%** (sin `CCC-2017-062`). La tabla completa preserva las 36 contribuciones y el cambio en puntos porcentuales.

Esto mide dependencia de sesiones concretas dentro del corpus, no incertidumbre de muestreo poblacional. Eliminar una sesión con pocos casos casi no mueve el resultado; una sesión con varios casos resolubles puede moverlo más.

## 2. Heterogeneidad descriptiva de la indeterminación

| Dificultad proxy | n | Cumplidas | Incumplidas | Indeterminadas | % indeterminado |
|---|---:|---:|---:|---:|---:|
| Baja | 55 | 33 | 12 | 10 | 18,2% |
| Media | 22 | 9 | 6 | 7 | 31,8% |
| Alta | 43 | 12 | 17 | 14 | 32,6% |

| Familia | n | Cumplidas | Incumplidas | Indeterminadas | % indeterminado |
|---|---:|---:|---:|---:|---:|
| Security Nightmares | 73 | 33 | 17 | 23 | 31,5% |
| Resto | 47 | 21 | 18 | 8 | 17,0% |

| Periodo de sesión | n | Cumplidas | Incumplidas | Indeterminadas | % indeterminado |
|---|---:|---:|---:|---:|---:|
| 2005–2009 | 36 | 13 | 12 | 11 | 30,6% |
| 2010–2014 | 43 | 18 | 12 | 13 | 30,2% |
| 2015–2018 | 41 | 23 | 11 | 7 | 17,1% |

Los estratos muestran heterogeneidad descriptiva de la indeterminación según atributos observados. No prueban un mecanismo de ausencia de datos ni justifican imputar a los indeterminados con la tasa de los resolubles. Las categorías de dificultad son proxies post hoc y tampoco prueban causalidad.

## 3. Identificación parcial explícita

Si `u` de las 31 indeterminadas finalmente resultara cumplida, la tasa sobre el corpus sería `(54+u)/120`. Los siguientes son escenarios contrafactuales, no nuevos juicios:

| Indeterminadas como cumplidas | Como incumplidas | % de 120 |
|---:|---:|---:|
| 0 | 31 | 45,0% |
| 7 | 24 | 50,8% |
| 16 | 15 | 58,3% |
| 24 | 7 | 65,0% |
| 31 | 0 | 70,8% |

Siete cumplidas serían suficientes para superar 50% sobre los 120 casos. El corpus no permite estimar cuántas son realmente cumplidas sin nuevas fuentes.

## 4. Sensibilidad de evidencia débil

Dieciocho filas no tienen URL probatoria primaria ni secundaria: 17 indeterminadas y una incumplida. El único incumplimiento con fuerza `weak` es `39-CCC-2006-011-06`. Si **sólo para probar fragilidad** se lo tratara como indeterminado, el balance resoluble sería 54/88 = **61,4%**, frente a 54/89 = **60,7%**. El juicio canónico no se modifica.

No se calcula una tasa “sólo evidencia fuerte” como estimador principal: la fuerza de evidencia se asignó después de observar el desenlace y puede seleccionar casos fáciles de probar, tanto positivos como negativos.

## 5. Composición del marco y rendimiento documental

| Venue | Sesiones S3 | Sesiones que aportaron predicciones | Predicciones incluidas |
|---|---:|---:|---:|
| Black Hat USA | 41 | 5 | 12 |
| CCC | 85 | 29 | 99 |
| Virus Bulletin | 12 | 2 | 9 |

Una sesión que no aportó predicciones no es equivalente a una predicción fallida. La disponibilidad documental y la densidad de proposiciones cambian mucho entre venues; estas cifras no permiten una comparación de calidad predictiva entre conferencias.

## Reproducibilidad

- `work/influencia_sesiones_v1.3.csv`: eliminación de cada sesión, fila por fila.
- `work/escenarios_indeterminados_v1.3.csv`: identificación parcial de escenarios.
- `scripts/diagnosticos_adicionales_v1_3.py`: generación determinista.
- Juicios y citas originales: registros v1.0, sin cambios.
