# Anexo metodológico y de trazabilidad v1.1

Este anexo contiene tablas derivadas. No sustituye ni modifica los dos CSV v1.0.

## A. Correspondencia de identificador

| Campo congelado | Campo del marco S3 | Evidencia de identidad | Tratamiento |
|---|---|---|---|
| `CCC-2013-034`, orden 34, 7 filas | `CCC-2013-043`, orden 34 | misma charla *Security Nightmares*, año, URL y ponentes | usar correspondencia sólo en cruces derivados |

## B. Reconciliación de resultados

| Juicio | n | % de 120 |
|---|---:|---:|
| `fulfilled` | 54 | 45,0 |
| `not_fulfilled` | 35 | 29,2 |
| `indeterminate` | 31 | 25,8 |

Resultado resoluble: 54/89 = 60,7%. Wilson 95% descriptivo: 50,3–70,2%.

## C. Dependencia por sesión: análisis exploratorio post hoc

Treinta y tres de las 36 sesiones aportaron al menos una predicción resoluble. Para el estimador ponderado por predicción (54/89), un error estándar sándwich de un modelo lineal de sólo intercepto, agrupado por sesión y con corrección finita por 33 conglomerados, fue 0,0638. Usando *t* con 32 grados de libertad, el intervalo aproximado fue 47,7–73,7%.

La media de las tasas de las 33 sesiones, dando el mismo peso a cada sesión con independencia del número de predicciones, fue 52,2%. Este promedio responde a otra pregunta y es sensible a sesiones con un solo caso. Ambos análisis se añadieron después de observar los resultados y son comprobaciones de fragilidad, no estimaciones poblacionales preregistradas.

## D. Resultado por clase

| Clase | n | Cumplidas | Incumplidas | Indeterminadas | % entre resolubles |
|---|---:|---:|---:|---:|---:|
| A | 5 | 2 | 2 | 1 | 50,0 |
| B | 115 | 52 | 33 | 30 | 61,2 |

La sensibilidad «sólo A» estaba prevista, pero cinco casos son insuficientes para una conclusión estable.

## E. Resultado por venue

Después de aplicar la correspondencia de ID:

| Venue | n | Cumplidas | Incumplidas | Indeterminadas | % entre resolubles |
|---|---:|---:|---:|---:|---:|
| Black Hat USA | 12 | 4 | 4 | 4 | 50,0 |
| CCC | 99 | 44 | 30 | 25 | 59,5 |
| Virus Bulletin | 9 | 6 | 1 | 2 | 85,7 |

No deben compararse como ranking: el número de observaciones y el formato de las sesiones difieren mucho, y las predicciones dentro de una sesión no son independientes.

## F. Resultado por forma de predicción

| Tipo congelado | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
| occurrence | 45 | 23 | 12 | 10 | 65,7 |
| count | 24 | 9 | 7 | 8 | 56,3 |
| direction | 7 | 2 | 1 | 4 | 66,7 |
| trend | 7 | 0 | 2 | 5 | 0,0 |
| adoption | 4 | 0 | 2 | 2 | 0,0 |
| capability_maturation | 4 | 4 | 0 | 0 | 100,0 |
| prevalence | 4 | 1 | 3 | 0 | 25,0 |
| categorical | 3 | 3 | 0 | 0 | 100,0 |
| salience | 3 | 3 | 0 | 0 | 100,0 |
| occurrence_and_breadth | 3 | 2 | 0 | 1 | 100,0 |
| Resto de tipos (≤2 cada uno) | 16 | 7 | 7 | 2 | 50,0 |

Los tipos pequeños son descriptores del corpus, no comparaciones inferenciales.

## G. Fuerza y disponibilidad de evidencia

| Fuerza | n | Cumplidas | Incumplidas | Indeterminadas |
|---|---:|---:|---:|---:|
| Fuerte | 57 | 43 | 14 | 0 |
| Moderada | 43 | 11 | 20 | 12 |
| Débil | 20 | 0 | 1 | 19 |

Dieciocho filas carecen de URL probatoria primaria y secundaria: 17 son `indeterminate/weak` y una `not_fulfilled/weak`. Ninguna se contabilizó como acierto. La fuerza se codificó tras buscar desenlaces y no debe tratarse como predictor independiente de exactitud.

La excepción `not_fulfilled/weak` es `39-CCC-2006-011-06`. Su justificación se basa en que la búsqueda no localizó un caso verificable de dispositivo VoIP/IPTV o *set-top box* usado como infraestructura de botnet o nodo Tor en 2007, mientras las notas reconocen cobertura histórica incompleta. Se conserva el juicio congelado, pero la fila debe encabezar una réplica independiente por la dificultad de inferir ausencia desde una búsqueda incompleta.

## H. Claves de casos usados en el texto

| Caso | Clave | Juicio | Dimensión principal |
|---|---|---|---|
| Gusano móvil fuera del laboratorio | `45-CCC-2005-006-02` | Cumplida | aparición |
| Filtraciones recurrentes en 2010 | `70-CCC-2009-021-11` | Cumplida | aparición y amplitud |
| Teléfono como credencial física | `41-CCC-2011-031-03` | Cumplida | capacidad desplegada |
| Activación vocal siempre disponible | `41-CCC-2011-031-07` | Cumplida | mecanismo/capacidad |
| Seguridad de dispositivos médicos | `127-CCC-2012-037-02` | Cumplida | saliencia |
| V2V en vehículo de producción | `20-CCC-2012-033-01` | Cumplida | adopción mínima |
| Nuevas técnicas Rowhammer | `131-CCC-2015-056-01` | Cumplida | aparición |
| Confrontación pública por cifrado | `131-CCC-2015-056-05` | Cumplida | saliencia/ocurrencia |
| Enumeración no secuencial en IPv6 | `51-BHPRO-2012-03-07` | Cumplida | cambio metodológico |
| Operación contra elección de 2020 | `30-CCC-2018-076-02` | Cumplida | aparición |
| Crédito social fragmentado | `49-CCC-2018-074-01` | Cumplida | arquitectura |
| eCall mayoritario para 2016 | `92-CCC-2014-045-01` | Incumplida | prevalencia/fecha |
| Huella comparada en nube | `34-CCC-2013-034-10` | Incumplida | mecanismo |
| Neutralidad de red en 2016 | `131-CCC-2015-056-03` | Incumplida | dirección |
| Reconocimiento facial dominante en 2019 | `130-CCC-2017-061-06` | Incumplida | prevalencia |
| Seguro cyber: 25–33,3% del presupuesto | `93-BHKEY-2015-01-01` | Incumplida | magnitud |

La fuente autoritativa de texto, umbral y evidencia sigue siendo la pareja de CSV congelados.
