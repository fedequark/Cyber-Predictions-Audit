# ¿Acertaron los escenarios del futuro *cyber*?

## Auditoría retrospectiva de 120 predicciones explícitas en conferencias de ciberseguridad, 2005–2018

**Versión 1.3 — 15 de septiembre de 2026**

### Resumen

**Contexto.** Las conferencias de ciberseguridad influyen en agendas profesionales, pero rara vez se comprueba lo que anticiparon una vez vencido el plazo.

**Método.** Auditamos 120 predicciones explícitas de 36 sesiones de Black Hat USA, Chaos Communication Congress y Virus Bulletin. Las sesiones proceden de un marco documental de 189, de las cuales 138 tenían material S3 y fueron revisadas en orden fijado. Antes de buscar desenlaces, cada afirmación se atomizó y recibió fecha, indicador, umbrales, fuentes admisibles y regla para evidencia ausente o conflictiva. El corpus *outcome-blind* se congeló antes de adjudicar resultados.

**Resultados confirmatorios.** Hubo 54 predicciones cumplidas, 35 incumplidas y 31 indeterminadas. Entre las 89 resolubles, 54 cumplieron el umbral: 60,7% (IC Wilson descriptivo 95%: 50,3–70,2%). Si todos los indeterminados se tratan como fallos o como aciertos, la proporción sobre el corpus es 45,0–70,8%.

**Resultados exploratorios.** La familia *Security Nightmares* aportó 73/120 observaciones. El HHI por sesión fue 0,044, equivalente a 22,5 sesiones de igual peso. Un bootstrap por sesión dio 47,0–72,1%. Un proxy post hoc de dificultad separó tasas resolubles de 73,3% (baja), 60,0% (media) y 41,4% (alta). En una regresión logística agrupada por sesión, la dificultad se asoció negativamente con cumplimiento (OR por 1 DE 0,47; IC 95% 0,27–0,81), sin interpretación causal.

**Diagnósticos adicionales exploratorios.** Al excluir una sesión por vez, la tasa resoluble varía entre 58,5% y 63,5%. La indeterminación es heterogénea: 18,2% en el proxy de dificultad baja y 32,6% en alta. Reetiquetar sólo el único fallo de evidencia débil como indeterminado cambia 60,7% a 61,4%, sin modificar el juicio canónico.

**Interpretación.** El 60,7% describe este corpus, no la habilidad predictiva de expertos o conferencias. La referencia “siempre cumplida” alcanza exactamente 60,7% por construcción, por lo que el porcentaje no demuestra discriminación. La evidencia apoya una lectura más limitada: las charlas funcionaron mejor como radar de aparición de temas que como instrumento para acertar magnitud, prevalencia, mecanismo o fecha.

## 1. Pregunta y contribución

La pregunta principal es qué proporción de las predicciones explícitas y con horizonte vencido de este corpus supera sus umbrales congelados. La contribución no es un ranking de ponentes. Es un método trazable para convertir retórica prospectiva en condiciones susceptibles de error y conservar los casos que no pueden resolverse.

Sin probabilidades originales no puede medirse calibración. Sin alternativas mutuamente excluyentes ni una clase de referencia preregistrada no puede estimarse *skill*. La auditoría evalúa correspondencia retrospectiva con reglas congeladas.

## 2. Diseño y métodos

### 2.1 Marco y selección

El marco cerrado contiene 189 sesiones entre 2005 y 2018. Ciento treinta y ocho tenían disponibilidad S3: grabación sustancialmente completa, transcripción completa, paper integral o diapositivas autosuficientes. Las 51 restantes no podían aportar predicciones. RSA Conference se excluyó al no poder reconstruirse un denominador histórico reproducible.

Las 138 sesiones S3 se ordenaron antes de la extracción mediante estratos de venue y periodo, con orden interno determinado por hash, y se revisaron íntegramente. Treinta y seis aportaron al menos una predicción. El paquete publicado no conserva un registro fila por fila de candidatos textuales excluidos; ese conteo no puede reconstruirse y se declara como dato no disponible.

### 2.2 Congelación y adjudicación

Cada fila conserva texto literal, localización, contexto, hablante, reformulación atómica, población, geografía, resultado, horizonte, indicador, umbral de éxito, umbral de contradicción, fuentes admisibles y tratamiento de ausencia o conflicto. Cinco predicciones fueron clase A, directamente puntuables; 115 fueron clase B, operacionalizadas sin alterar su dirección sustantiva.

El registro se congeló antes de buscar desenlaces. Su SHA-256 es `323739E747379873D5786DB7057E7357EED0F70F0E6425AE6A3339B96AEDA32B`. La evaluación posterior clasificó cada caso como `fulfilled`, `not_fulfilled`, `indeterminate` o `mixed`; no hubo casos `mixed`. El SHA-256 del registro de desenlaces es `B3CE8AD49F6555870FCF415488506717BD8D7E71F4B955ED03514F7CE9E26F1B`.

### 2.3 Plan confirmatorio y análisis post hoc

El estimando principal, Wilson y los extremos para indeterminados pertenecen al plan operativo. La sensibilidad sólo clase A estaba prevista, pero cinco casos son insuficientes. La agrupación por sesión, concentración, referencias base, proxies de especificidad/dificultad, regresión, eliminación de una sesión por vez y diagnósticos de indeterminación/evidencia se añadieron después de observar el corpus y se etiquetan como exploratorios.

El bootstrap remuestreó 36 sesiones con reemplazo 20.000 veces (semilla `20260913`). La regresión logística usó los 89 casos resolubles y errores sándwich agrupados por las 33 sesiones que aportaron alguno. Incluyó familia *Security Nightmares*, año, especificidad proxy y dificultad proxy. Los predictores continuos se estandarizaron.

### 2.4 Proxies exploratorios

La especificidad proxy suma cuatro señales mecánicas: clase A, detalle numérico en el texto original, horizonte explícito y población+geografía informadas. La dificultad usa una tabla fija por tipo: ocurrencia/saliencia/capacidad como baja; dirección/adopción/no-ocurrencia como media; conteo/tendencia/prevalencia/proporción/mecanismo compuesto como alta. El codebook y el script publican la regla exacta.

## 3. Resultados

### 3.1 Resultado global e incertidumbre

| Resultado | n | % de 120 |
|---|---:|---:|
| Cumplida | 54 | 45,0 |
| Incumplida | 35 | 29,2 |
| Indeterminada | 31 | 25,8 |

Entre los 89 casos resolubles, 54 cumplieron: **60,7%** (Wilson 95% **50,3–70,2%**). Los extremos sobre los 120 casos son **45,0%** si todo indeterminado falla y **70,8%** si todo indeterminado acierta. Siete aciertos entre los 31 indeterminados bastarían para superar 50% sobre el corpus completo.

El bootstrap exploratorio por sesión produjo **47,0–72,1%**. Este intervalo cuantifica sensibilidad a la composición observada; no convierte la muestra documental en una muestra aleatoria.

### 3.2 Baselines y discriminación

| Referencia post hoc | Valor |
|---|---:|
| Moneda justa sobre resolubles | 50,0% (p bilateral=0,056) |
| Etiqueta aleatoria con prevalencia observada | 52,3% de exactitud esperada |
| Clasificar todo como “cumplida” | 60,7% |

La tercera referencia iguala el titular por definición. Esto demuestra que la proporción de aciertos, sin un conjunto de alternativas o probabilidades, no mide discriminación ni valor añadido.

### 3.3 Concentración

*Security Nightmares* aporta 73 casos: 33 cumplidos, 17 incumplidos y 23 indeterminados, o 66,0% entre resolubles. El resto aporta 21, 18 y 8, respectivamente, o 53,8%. El HHI por sesión es 0,044 y el número efectivo de sesiones 22,5 frente a 36 nominales.

### 3.4 Especificidad y dificultad

| Dificultad proxy | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
| Baja | 55 | 33 | 12 | 10 | 73,3 |
| Media | 22 | 9 | 6 | 7 | 60,0 |
| Alta | 43 | 12 | 17 | 14 | 41,4 |

La especificidad proxy no mostró un gradiente estable: baja 56,4%, media 66,0% y alta 33,3%, pero la banda alta sólo contiene tres casos. No debe interpretarse como evidencia de que ser específico empeore el pronóstico.

### 3.5 Modelo exploratorio

| Predictor | Odds ratio | IC 95% agrupado |
|---|---:|---:|
| *Security Nightmares* | 3,33 | 0,91–12,15 |
| Año (1 DE) | 1,92 | 1,09–3,38 |
| Especificidad proxy (1 DE) | 1,48 | 0,84–2,63 |
| Dificultad proxy (1 DE) | 0,47 | 0,27–0,81 |

Los coeficientes son asociaciones condicionales en 89 observaciones, con pocos conglomerados y variables construidas post hoc. No identifican causalidad ni comparan talento de ponentes.

### 3.6 Diagnósticos de fragilidad y evidencia

Al excluir cada una de las 36 sesiones aportantes, la tasa entre resolubles queda entre **58,5%** (sin `VB-2016-P01`) y **63,5%** (sin `CCC-2017-062`). La influencia exacta de cada sesión se publica en un CSV derivado.

La indeterminación no es uniforme: 10/55 (18,2%) en dificultad proxy baja, 7/22 (31,8%) en media y 14/43 (32,6%) en alta. En *Security Nightmares* es 23/73 (31,5%) y en el resto 8/47 (17,0%). Estas asociaciones descriptivas no demuestran un mecanismo de datos ausentes ni justifican imputar los 31 casos.

Dieciocho filas carecen de URL probatoria primaria y secundaria: 17 indeterminadas y una incumplida. La única incumplida de fuerza débil, `39-CCC-2006-011-06`, produciría 54/88 = **61,4%** si se tratara contrafactualmente como indeterminada. El registro original permanece 54/89. No se usa la categoría “evidencia fuerte” como filtro del estimando principal, porque se adjudicó después del desenlace.

La composición documental también difiere: Black Hat USA aporta 12 predicciones de 5/41 sesiones S3; CCC, 99 de 29/85; y Virus Bulletin, 9 de 2/12. Las sesiones improductivas no son pronósticos fallidos.

## 4. Discusión

La formulación defendible es: 54 de 89 casos resolubles superaron sus umbrales. La banda 45,0–70,8%, la concentración, el bootstrap, la influencia por sesión y el baseline trivial impiden traducir esa frase como “los expertos aciertan seis de cada diez”.

El patrón por dificultad es compatible con la tesis de radar temático: anticipar que aparecerá una clase de problema parece más fácil que acertar su cantidad, penetración, mecanismo conjunto o calendario. Como el instrumento de dificultad es post hoc, la próxima réplica debe validarlo de forma ciega antes de usarlo confirmatoriamente.

La indeterminación también es un hallazgo metodológico. Se concentra en recuentos históricos sin archivo estable, poblaciones sin denominador y conceptos como “más”, “común” o “importante”. Una predicción auditable debería publicar población, resultado, magnitud, fecha, fuente de resolución y probabilidad.

## 5. Limitaciones

- La muestra es documental, no probabilística, y cubre tres venues.
- Una familia de sesiones aporta 60,8% del corpus.
- Las observaciones dentro de una sesión no son independientes.
- 115/120 operacionalizaciones son clase B.
- Hubo un solo codificador; la doble codificación prevista sigue pendiente y se excluye deliberadamente de v1.2.
- No existe registro fila por fila de candidatos textuales excluidos.
- Las fuentes remotas pueden cambiar o desaparecer; v1.2 preserva localizadores y cápsulas textuales, no todos los bytes originales.
- La errata `CCC-2013-034/043` se conserva en los CSV y se corrige sólo en cruces derivados.
- Los análisis de concentración, proxies, baseline, modelo, influencia por sesión e indeterminación por estratos son exploratorios.
- La heterogeneidad observada de la indeterminación no revela el resultado de los casos sin evidencia.

## 6. Conclusión

Las conferencias estudiadas detectaron con frecuencia temas que luego importaron, pero el corpus no demuestra habilidad predictiva. La contribución más sólida es metodológica: volver las predicciones falsables, mantener visibles los casos indeterminados y publicar suficiente trazabilidad para que otra persona pueda impugnar cada juicio.

## Datos y código

- [Corpus congelado](../work/registro_extraccion_congelado_v1.0.csv)
- [Evaluación de desenlaces](../work/evaluacion_desenlaces_v1.0.csv)
- [Capa derivada v1.2](../work/analisis_derivado_v1.2.csv)
- [Métricas de robustez](../work/metricas_robustez_v1.2.csv)
- [Inventario de fuentes](../work/inventario_fuentes_v1.2.csv)
- [Análisis detallado v1.2](analisis_robustez_y_representatividad_v1.2.md)
- [Codebook de proxies](codebook_proxies_v1.2.md)
- [Protocolo de preservación](protocolo_preservacion_fuentes_v1.2.md)
- [Diagnósticos adicionales v1.3](diagnosticos_adicionales_v1.3.md)
- [Influencia por sesión](../work/influencia_sesiones_v1.3.csv)
- [Escenarios de indeterminación](../work/escenarios_indeterminados_v1.3.csv)
- [Protocolo de réplica prospectiva](protocolo_replica_prospectiva_v1.3.md)
- [Alcance de derechos](../documents/RIGHTS.md)

## Derechos y acceso

El software se publica bajo MIT y los aportes originales de investigación y base de datos bajo CC BY 4.0. Las palabras literales de ponentes y otros materiales de terceros no están sublicenciados por este proyecto. El alcance campo por campo se documenta en `RIGHTS.md`; el sitio permanece en Cloudflare Pages y el repositorio GitHub pasa a público para facilitar reproducción.

## Declaraciones

**Codificación:** un solo codificador; la validación independiente continúa pendiente.

**Preregistro:** interno, sin sello temporal externo previo.

**Financiación y conflictos:** deben completarse por la autoría antes de un envío.
**Ética:** análisis de materiales públicos; la revista deberá determinar si requiere declaración formal.

## Referencias

Gneiting, T., Balabdaoui, F. y Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. *JRSS B*, 69(2), 243–268. https://doi.org/10.1111/j.1467-9868.2007.00587.x

Mellers, B. et al. (2014). Psychological strategies for winning a geopolitical forecasting tournament. *Psychological Science*, 25(5), 1106–1115. https://doi.org/10.1177/0956797614524255

Tetlock, P. E., Mellers, B. A. y Scoblic, J. P. (2017). Bringing probability judgments into policy debates via forecasting tournaments. *Science*, 355(6324), 481–483. https://doi.org/10.1126/science.aal3147
