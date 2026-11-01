# ¿Acertaron los escenarios del futuro *cyber*?

## Auditoría retrospectiva de 120 predicciones explícitas en conferencias de ciberseguridad, 2005–2018

**Versión 1.1 — 24 de agosto de 2026**

### Resumen

**Contexto.** Las conferencias de ciberseguridad influyen en agendas profesionales y mediáticas, pero pocas veces se evalúan sus afirmaciones sobre el futuro una vez vencido el plazo.

**Método.** Auditamos 120 predicciones explícitas formuladas entre 2005 y 2018 en 36 sesiones de Black Hat USA, Chaos Communication Congress y Virus Bulletin. Se recorrieron las 138 sesiones con disponibilidad documental S3 en un orden fijado previamente. Antes de buscar desenlaces, cada predicción se atomizó y recibió indicador, umbrales de éxito y contradicción, fuentes admisibles y una regla para datos ausentes o conflictivos. El corpus *outcome-blind* se congeló y sus desenlaces se evaluaron después.

**Resultados.** Hubo 54 predicciones cumplidas, 35 incumplidas y 31 indeterminadas. Entre las 89 resolubles, 54 cumplieron el umbral: 60,7% (IC Wilson descriptivo 95%: 50,3–70,2%). Los límites de sensibilidad fueron 45,0% si todos los indeterminados se tratan como fallos y 70,8% si se tratan como aciertos. *Security Nightmares* aportó 73/120 observaciones: 66,0% entre sus casos resolubles, frente a 53,8% en el resto. En un análisis post hoc sensible a la agrupación por sesión, el intervalo aproximado fue 47,7–73,7%, y la media con igual peso para cada sesión resoluble fue 52,2%.
**Interpretación.** El corpus sugiere que las conferencias funcionaron razonablemente como radar de temas, pero peor como pronóstico de mecanismo, magnitud, prevalencia o fecha. El 60,7% no es representativo de todas las keynotes ni demuestra habilidad predictiva: no hay muestra probabilística, independencia, probabilidades originales ni línea base. La principal contribución es un método trazable para someter retórica prospectiva a condiciones explícitas de error.

**Palabras clave:** predicción tecnológica; ciberseguridad; auditoría retrospectiva; conferencias; escenarios; trazabilidad; *forecasting*.

## 1. Introducción

La industria de la ciberseguridad vive orientada al futuro. Keynotes y paneles anuncian el siguiente conflicto del cifrado, la próxima clase de malware, el final de una arquitectura o la llegada de una plataforma insegura. Esas afirmaciones fijan agendas, orientan investigación, justifican inversión y producen titulares. El ecosistema, sin embargo, premia más la novedad del escenario que su evaluación posterior.

Preguntar si una keynote «acertó» exige convertir lenguaje escénico en una prueba. «Habrá más ataques» requiere una población, una serie de medición, un periodo de comparación y una regla de deduplicación. «Todo tendrá un procesador» exige decidir qué cuenta como producto y como casi universalidad. Sin reglas fijadas antes de mirar el desenlace, la retrospectiva permite reinterpretar con benevolencia una frase célebre o exigirle una precisión que nunca tuvo.

La evaluación formal de pronósticos suele partir de probabilidades y emplear reglas de puntuación que valoran conjuntamente calibración y precisión informativa. Los torneos de predicción muestran además la importancia de explicitar probabilidades, usar clases de referencia, actualizar y registrar resultados (Gneiting, Balabdaoui y Raftery, 2007; Mellers et al., 2014; Tetlock, Mellers y Scoblic, 2017). Las conferencias estudiadas rara vez ofrecieron probabilidades. Por ello, este trabajo no estima calibración en el sentido estadístico ni un *skill score*: audita si compromisos binarios o direccionales superaron umbrales previamente congelados.

La pregunta principal es:

> ¿Qué proporción de las predicciones explícitas y con horizonte vencido de este corpus supera sus propios umbrales de cumplimiento?

La contribución es doble. Primero, ofrece una auditoría empírica trazable de 120 afirmaciones. Segundo, separa cinco logros que la conversación pública suele confundir: anticipar la **aparición** de un tema, su **mecanismo**, su **magnitud**, su **prevalencia** y su **fecha**. El objetivo no es elaborar un ranking de gurús, sino establecer qué puede afirmarse —y qué no— sobre la memoria prospectiva de las conferencias.

## 2. Diseño y métodos

### 2.1 Marco, disponibilidad y selección

El marco cerrado contiene 189 sesiones de Black Hat USA, Chaos Communication Congress (CCC) y Virus Bulletin entre 2005 y 2018. Se consideraron elegibles para extracción las 138 sesiones con disponibilidad S3: grabación sustancialmente completa, transcripción completa, paper integral o diapositivas autosuficientes. Las 51 restantes permanecieron en el denominador documental, pero no podían aportar predicciones. RSA Conference se excluyó porque no fue posible reconstruir un denominador histórico reproducible.

Las 138 sesiones S3 se ordenaron antes de la extracción mediante un procedimiento estratificado por venue y periodo, con orden interno determinado por hash. Se revisaron íntegramente. La regla de parada exigía alcanzar al menos 100 predicciones A+B, terminar la sesión terminal y detenerse si el total quedaba entre 100 y 120; sólo si se agotaban las 138 sesiones se admitía publicar 80–99. El recorrido se agotó y el corpus quedó en el límite superior de 120, sin reemplazar sesiones improductivas ni imponer cuotas posteriores.

Treinta y seis sesiones aportaron al menos una predicción. La unidad analítica fue la proposición predictiva atómica, atribuible, observable y con horizonte vencido al 6 de agosto de 2026. Se excluyeron exhortaciones, objetivos normativos, posibilidades sin expectativa adoptada, afirmaciones de terceros no adoptadas, horizontes abiertos y frases cuyo plazo no había vencido.

Las predicciones se clasificaron como A cuando el original era directamente puntuable y como B cuando se podía fijar ex ante una regla direccional u operativa sin alterar su dirección sustantiva. El corpus contiene 5 A y 115 B.

### 2.2 Congelación *outcome-blind*

Para cada fila se conservaron texto literal, localización, contexto, hablante, reformulación atómica, población, geografía, resultado, horizonte, fecha límite, indicador, umbral de éxito, umbral de contradicción, tipos de fuente admisibles y tratamiento de ausencia o conflicto.

La operacionalización de clase B fue deliberadamente exigente. Por ejemplo, que el escaneo remoto exhaustivo de IPv6 dejase de ser razonable se tradujo en evidencia autoritativa que prescribiera descubrimiento no secuencial; que los móviles sirvieran de credencial exigió un teléfono comercial y un despliegue físico real, no una demostración. Esta estrategia aumenta auditabilidad, pero introduce juicio del investigador y puede alejar la regla del significado pragmático original. El texto y la reformulación permanecen juntos para permitir impugnación.

El registro se congeló antes de habilitar la búsqueda de desenlaces. Su SHA-256 es `323739E747379873D5786DB7057E7357EED0F70F0E6425AE6A3339B96AEDA32B`.

### 2.3 Evaluación de desenlaces

La jerarquía de evidencia priorizó legislación y registros oficiales; documentación de fabricantes y operadores; artículos científicos y divulgaciones técnicas primarias; informes contemporáneos con método; y prensa como corroboración o localizador. Cada fila recibió un juicio:

- **cumplida**, si alcanzó el umbral congelado dentro del plazo;
- **incumplida**, si no lo alcanzó o satisfizo la contradicción;
- **indeterminada**, si la evidencia no permitía aplicar el umbral sin inferencia excesiva;
- **mixed**, reservada para componentes verificables en conflicto; ninguna fila terminó en esta categoría.

El registro de desenlaces conserva URL, periodo probatorio, síntesis factual, aplicación del umbral y tratamiento de conflicto o ausencia. Su SHA-256 es `B3CE8AD49F6555870FCF415488506717BD8D7E71F4B955ED03514F7CE9E26F1B`.

### 2.4 Desviaciones y errata de identificación

El preregistro preveía doble codificación de al menos 25% de inclusiones, atomizaciones y resultados. Esa verificación no se ejecutó: extracción y adjudicación fueron realizadas por un solo codificador. Es una desviación del protocolo y la principal tarea pendiente antes de un envío académico. Además, el preregistro enumeraba categorías separadas para cumplimiento parcial y tardío; el protocolo operativo posterior las sustituyó por cuatro juicios (`fulfilled`, `not_fulfilled`, `indeterminate`, `mixed`). El registro final no contiene casos `mixed` ni conserva parciales o tardíos como categorías separadas. Esta simplificación debe considerarse una segunda desviación, aunque las reglas binarias congeladas por fila siguieron gobernando la adjudicación.

Siete filas congeladas usan `CCC-2013-034`, mientras el marco S3 asigna a la misma sesión, en el mismo orden 34 y con la misma URL, `CCC-2013-043`. Los CSV no se modificaron. En cruces derivados se empleó la correspondencia documentada `CCC-2013-034 → CCC-2013-043`. La errata no afecta texto, juicio ni totales; sin la correspondencia, subcuenta *Security Nightmares* en siete observaciones.

### 2.5 Análisis

El estimando principal fue la proporción cumplida entre resolubles: cumplidas / (cumplidas + incumplidas). Se calculó un intervalo Wilson binomial de 95% como descriptor, no como inferencia a una población aleatoria. Los indeterminados se incorporaron mediante límites: todos como fallos y todos como aciertos.

Se repitió el resumen excluyendo *Security Nightmares* y por forma congelada de predicción. No se realizaron pruebas de significación ni rankings. Como comprobación post hoc de dependencia, se calculó un error estándar sándwich de un modelo lineal de sólo intercepto agrupado por sesión, con corrección finita, y la media de las tasas dando igual peso a cada sesión con al menos un caso resoluble. Estos análisis no estaban preregistrados y responden a estimandos distintos.

## 3. Resultados

### 3.1 Flujo y resultado global

De las 189 sesiones del marco, 138 tenían disponibilidad S3 y fueron revisadas. Treinta y seis aportaron las 120 predicciones congeladas; las demás no aportaron unidades elegibles. Cinco predicciones fueron clase A y 115 clase B.

| Resultado | n | % del corpus |
|---|---:|---:|
| Cumplida | 54 | 45,0 |
| Incumplida | 35 | 29,2 |
| Indeterminada | 31 | 25,8 |
| Total | 120 | 100,0 |

Entre las 89 resolubles, 54 cumplieron: **60,7%** (IC Wilson descriptivo 95%: **50,3–70,2%**). Los límites fueron **45,0%** si las 31 indeterminadas se cuentan como fallos y **70,8%** si se cuentan como aciertos. La amplitud de 25,8 puntos es un resultado sustantivo: la conclusión depende de la posibilidad de documentar históricamente la afirmación.

Dieciocho filas carecen de URL probatoria: 17 son indeterminadas con evidencia débil y una es un incumplimiento débil. Ningún acierto carece de enlace. Esto protege el numerador frente a aciertos basados sólo en intuición, pero no elimina la asimetría entre demostrar presencia y ausencia.

### 3.2 Concentración y agrupación

*Security Nightmares* aporta 73/120 observaciones: 33 cumplidas, 17 incumplidas y 23 indeterminadas, o 66,0% entre resolubles. El resto aporta 21, 18 y 8, respectivamente: 53,8% entre resolubles. La diferencia de 12,2 puntos no demuestra superioridad de la serie; mezcla formato, temas, tasas base y composición.

Treinta y tres sesiones aportaron casos resolubles. El análisis post hoc agrupado dio un intervalo aproximado de **47,7–73,7%**, más ancho que Wilson. La media de tasas con igual peso por sesión fue **52,2%**. Esta última cifra no reemplaza el 60,7%: cambia la unidad de ponderación y concede el mismo peso a una sesión con uno y a otra con varios pronósticos. En conjunto, ambas comprobaciones muestran que la estructura por sesión importa.

### 3.3 Forma del compromiso

| Forma | n | Cumplidas | Incumplidas | Indeterminadas | % entre resolubles |
|---|---:|---:|---:|---:|---:|
| Ocurrencia | 45 | 23 | 12 | 10 | 65,7 |
| Conteo | 24 | 9 | 7 | 8 | 56,3 |
| Dirección | 7 | 2 | 1 | 4 | 66,7 |
| Tendencia | 7 | 0 | 2 | 5 | 0,0 |
| Prevalencia | 4 | 1 | 3 | 0 | 25,0 |
| Maduración de capacidad | 4 | 4 | 0 | 0 | 100,0 |
| Saliencia | 3 | 3 | 0 | 0 | 100,0 |

Los grupos pequeños no admiten comparación estable. El patrón descriptivo sí es coherente con la tesis principal: detectar que aparecerá un ataque, producto o controversia fue más fácil que acertar su crecimiento o penetración. Las categorías no son equivalentes a las cinco dimensiones conceptuales —aparición, mecanismo, magnitud, prevalencia y fecha—, pero ayudan a mostrar dónde se acumula la incertidumbre.

### 3.4 Casos trazables

Algunos aciertos satisfacen una condición mínima de aparición: un gusano móvil fuera del laboratorio en 2006 (`45-CCC-2005-006-02`), filtraciones recurrentes en 2010 (`70-CCC-2009-021-11`), nuevas técnicas Rowhammer en 2016 (`131-CCC-2015-056-01`) y una operación extranjera contra el proceso electoral estadounidense de 2020 (`30-CCC-2018-076-02`). Son aciertos de **aparición**, no necesariamente de prevalencia o daño.

Otros acertaron capacidad o arquitectura: teléfonos desplegados como credenciales físicas (`41-CCC-2011-031-03`), activación vocal siempre disponible (`41-CCC-2011-031-07`), V2V instalado en un vehículo de producción (`20-CCC-2012-033-01`), enumeración no secuencial para evaluar IPv6 (`51-BHPRO-2012-03-07`) y un crédito social chino fragmentado en vez de una puntuación ciudadana universal (`49-CCC-2018-074-01`).

Los fallos muestran dimensiones diferentes. eCall no fue mayoritario en modelos europeos para 2016 (`92-CCC-2014-045-01`): fallo de **prevalencia y fecha**. La mayoría de teléfonos con huella de 2014 no comparó plantillas en la nube (`34-CCC-2013-034-10`): fallo de **mecanismo**. La protección de neutralidad de red no se deterioró materialmente dentro de 2016 según el umbral (`131-CCC-2015-056-03`): fallo de **dirección y fecha**. El reconocimiento facial seguro comparable a Face ID no dominó los envíos de 2019 (`130-CCC-2017-061-06`): fallo de **prevalencia**. No se documentó que el seguro cyber absorbiera 25–33,3% del presupuesto de seguridad para agosto de 2025 (`93-BHKEY-2015-01-01`): fallo de **magnitud**, con evidencia débil que merece réplica independiente.

## 4. Discusión

### 4.1 Qué significa el 60,7%

La formulación correcta es: **54 de 89 predicciones resolubles de este corpus superaron sus umbrales congelados**. No significa que «los expertos cyber acierten seis de cada diez», porque el estudio no muestreó expertos ni keynotes al azar, una serie domina el corpus y las observaciones están agrupadas. Tampoco significa habilidad predictiva: pronosticar al menos una vulnerabilidad o controversia en un ecosistema adversarial puede tener una tasa base alta.

Sin probabilidades originales no puede medirse calibración; sin una línea base no puede calcularse valor añadido; sin alternativas fallidas no puede evaluarse discriminación. La correspondencia retrospectiva es una condición necesaria para hablar de acierto, pero no suficiente para hablar de *skill*.

### 4.2 Radar de temas, instrumento de medición

El resultado más defendible no es un porcentaje aislado, sino una diferencia conceptual. Las conferencias identificaron con frecuencia **qué clase de problema** iba a importar: malware móvil, filtraciones, dispositivos médicos, Rowhammer, cifrado, IPv6 y operaciones electorales. Fueron menos fiables cuando añadieron un mecanismo específico, una cuota de mercado, una magnitud o una fecha estrecha.

Esta distinción evita conceder crédito retrospectivo parcial. Si una predicción anuncia el mecanismo equivocado, no debe rescatarse porque el tema general se volvió importante. Si fija 2016 y el despliegue llega en 2018, acertó la dirección narrativa pero falló el plazo congelado. El corpus permite conservar ambas descripciones sin cambiar el juicio.

### 4.3 La indeterminación como hallazgo

El 25,8% indeterminado no es mero residuo. Se concentra en recuentos históricos sin archivo estable, poblaciones sin denominador, taxonomías propietarias y conceptos como «más», «común» o «importante». Además, probar que algo no ocurrió es normalmente más difícil que localizar un acontecimiento positivo.

Una predicción profesional auditable debería declarar al menos población, resultado observable, magnitud, fecha y fuente de resolución. Idealmente debería añadir una probabilidad, una clase de referencia y un mecanismo de actualización. Esa disciplina reduce margen retórico, pero permite aprender de manera acumulativa.

### 4.4 Implicaciones prácticas

Los organizadores podrían pedir a las sesiones prospectivas una «tarjeta de resolución» publicada junto al vídeo: enunciado atómico, probabilidad, fecha límite, métrica y fuente. Los ponentes podrían separar escenario —exploración de posibilidades— de pronóstico —compromiso susceptible de error—. Los periodistas deberían informar denominador e indeterminados, no sólo rescatar ejemplos memorables. Una réplica prospectiva permitiría, por primera vez, comparar conferencias con una línea base y puntuar probabilidades.

## 5. Limitaciones y amenazas a la validez

| Amenaza | Consecuencia | Mitigación disponible |
|---|---|---|
| Muestra no probabilística y filtrada por disponibilidad | No representa todas las keynotes | Limitar inferencia al corpus y publicar marco |
| 73/120 de una serie | Resultado sensible al formato dominante | Sensibilidad excluyendo la serie |
| Agrupación por 36 sesiones | Wilson demasiado estrecho si se lee inferencialmente | Etiquetarlo descriptivo; análisis agrupado post hoc |
| 115 predicciones clase B | Riesgo de reinterpretación al operacionalizar | Texto, reformulación y umbral por fila |
| Un solo codificador y doble codificación no realizada | Error y sesgo no cuantificados | Declarar desviación; réplica ciega pendiente |
| Preregistro interno | Sin sello temporal externo | Hashes e historial; depósito posterior no retroactivo |
| Sin línea base ni probabilidades | No hay *skill score* ni calibración | Evitar lenguaje de habilidad; diseñar réplica prospectiva |
| Ausencia más difícil de demostrar | Indeterminación y posible asimetría | Tres categorías y límites de sensibilidad |
| Pérdida o cambio de fuentes web | Replicabilidad futura frágil | URL y síntesis; archivado pendiente |
| Errata `034/043` | Cruces automáticos incompletos | Correspondencia derivada documentada |

El estudio tampoco estima causalidad entre conferencias y adopción posterior: una keynote puede detectar, amplificar o simplemente reflejar señales ya visibles. Las comparaciones por venue o tipo son descriptivas, con grupos pequeños y composiciones distintas.

## 6. Conclusión

Esta auditoría convirtió 120 frases sobre el futuro cyber en pruebas explícitas: 54 cumplieron, 35 no y 31 no pudieron resolverse. Entre las resolubles, el balance fue 60,7%, pero la conclusión completa incluye la banda 45,0–70,8%, la concentración de una serie, la dependencia por sesión y la ausencia de línea base.

El veredicto no es que las keynotes adivinen el futuro. Es más preciso y más útil: **funcionaron razonablemente como radar de temas y mucho peor como instrumento para medir mecanismo, magnitud, prevalencia y calendario**. La lección práctica es que una predicción sólo queda completa cuando publica también cómo y cuándo podrá demostrarse que estaba equivocada.

## Disponibilidad de datos, protocolo y trazabilidad

- [Corpus congelado](../work/registro_extraccion_congelado_v1.0.csv)
- [Evaluación de desenlaces](../work/evaluacion_desenlaces_v1.0.csv)
- [Preregistro consolidado](preregistracion_consolidada_v0.2.md)
- [Informe de congelación](congelacion_corpus_outcome_blind_v1.0.md)
- [Protocolo de evaluación](protocolo_evaluacion_desenlaces_v1.0.md)
- [Resultados v1.0](resultados_auditoria_v1.0.md)
- [Auditoría crítica v1.1](auditoria_critica_integral_v1.1.md)
- [Anexo metodológico v1.1](anexo_metodologico_y_trazabilidad_v1.1.md)

## Declaraciones

**Codificación:** un solo codificador; la doble codificación prevista no se realizó.

**Preregistro:** interno, no depositado externamente antes del estudio.

**Conflictos de interés y financiación:** no constan en los artefactos auditados; deben completarse por la autoría antes del envío.
**Ética:** análisis de materiales públicos; la revista deberá determinar si requiere declaración formal.

## Referencias

Gneiting, T., Balabdaoui, F. y Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. *Journal of the Royal Statistical Society: Series B*, 69(2), 243–268. https://doi.org/10.1111/j.1467-9868.2007.00587.x

Mellers, B. et al. (2014). Psychological strategies for winning a geopolitical forecasting tournament. *Psychological Science*, 25(5), 1106–1115. https://doi.org/10.1177/0956797614524255

Tetlock, P. E., Mellers, B. A. y Scoblic, J. P. (2017). Bringing probability judgments into policy debates via forecasting tournaments. *Science*, 355(6324), 481–483. https://doi.org/10.1126/science.aal3147

Las referencias probatorias de cada desenlace se conservan en `evaluacion_desenlaces_v1.0.csv`; no se duplican aquí para evitar desvincularlas de su umbral y aplicación.

## Cambios respecto de v1.0

Se conservó v1.0 sin alteraciones. Esta versión precisa la regla de parada; declara como desviación la ausencia de doble codificación; documenta la correspondencia `CCC-2013-034/043`; añade análisis agrupado post hoc, resultado por clase y claves de fila; distingue aparición, mecanismo, magnitud, prevalencia y fecha; amplía amenazas a la validez; y añade un marco bibliográfico mínimo sin convertir el estudio en evaluación formal de calibración.
