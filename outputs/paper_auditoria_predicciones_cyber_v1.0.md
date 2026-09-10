# ¿Acertaron los escenarios del futuro *cyber*?

## Auditoría retrospectiva de 120 predicciones explícitas en conferencias de ciberseguridad, 2005–2018

### Resumen

Las conferencias de ciberseguridad producen afirmaciones memorables sobre el futuro, pero rara vez vuelven sobre ellas cuando vence su horizonte. Auditamos retrospectivamente 120 predicciones explícitas formuladas entre 2005 y 2018 en 36 sesiones de Black Hat USA, Chaos Communication Congress y Virus Bulletin. El corpus se seleccionó mediante un orden previamente fijado y una regla de parada de 80–120 observaciones. Antes de consultar desenlaces, cada predicción fue atomizada y recibió un indicador, un umbral de éxito, un umbral de contradicción, fuentes admisibles y una regla para evidencia faltante o conflictiva. El registro outcome-blind se congeló en 120 filas y se evaluó después contra fuentes oficiales, documentación técnica, literatura científica e informes especializados.

Encontramos 54 predicciones cumplidas, 35 incumplidas y 31 indeterminadas. Entre las 89 resolubles, la tasa descriptiva de acierto fue 60,7% (IC Wilson 95%: 50,3–70,2%). Si todos los indeterminados se tratan como fallos, cae a 45,0%; si se tratan como aciertos, sube a 70,8%. La serie recurrente *Security Nightmares* aportó 73 observaciones y obtuvo 66,0% entre resolubles, frente a 53,8% en el resto. Las predicciones de ocurrencia acertaron con más frecuencia que las de tendencia o prevalencia. Los ponentes anticiparon razonablemente bien la aparición de nuevas capacidades y controversias, pero peor su magnitud, calendario y difusión. Una cuarta parte del corpus no pudo adjudicarse: la auditabilidad futura no depende sólo de formular una predicción explícita, sino de dejar una métrica observable.

**Palabras clave:** predicción tecnológica; ciberseguridad; forecasting; auditoría retrospectiva; conferencias; calibración; análisis de escenarios.

## 1. Introducción

La industria de la ciberseguridad vive orientada al futuro. Cada año, keynotes y paneles anuncian el siguiente conflicto del cifrado, la próxima clase de malware, el fin de una arquitectura o la llegada de una plataforma insegura. Esas afirmaciones tienen efectos profesionales: ayudan a fijar agendas, justifican inversión, orientan investigación y ofrecen titulares. Sin embargo, el ecosistema premia más la novedad de la predicción que su evaluación posterior.

Preguntar si «acertaron» parece sencillo hasta intentar convertir una frase escénica en una prueba. «Habrá más ataques» exige decidir qué cuenta como ataque, qué periodo comparar, cómo deduplicar divulgaciones y qué evidencia demostraría que el aumento no ocurrió. «Todo tendrá un procesador» requiere definir producto, categoría y casi universalidad. La retrospectiva sin reglas previas invita a dos sesgos opuestos: reinterpretar caritativamente una frase célebre o exigirle una precisión que nunca tuvo.

Este estudio audita predicciones explícitas con horizontes ya vencidos y criterios fijados antes de buscar el resultado. Su pregunta principal es:

> ¿Qué proporción de las predicciones explícitas sobre el futuro de la ciberseguridad, formuladas en sesiones de 2005–2018, supera sus propios umbrales de cumplimiento una vez vencido el horizonte?

La contribución no es un ranking de gurús. Es un procedimiento reproducible para transformar retórica prospectiva en afirmaciones auditables y una primera descripción de qué clases de predicción sobreviven mejor al paso del tiempo.

## 2. Diseño y métodos

### 2.1 Universo y selección

Se construyó un marco de sesiones de tres venues profesionales con archivos suficientemente trazables: Black Hat USA, Chaos Communication Congress (CCC) y Virus Bulletin. El periodo de emisión fue 2005–2018. Se recorrió un orden S3 congelado que alternaba celdas de venue y periodo para reducir la discrecionalidad del investigador. La revisión terminó al alcanzar el límite superior preregistrado de 120 predicciones elegibles; se habían recorrido las 138 sesiones del orden.

La unidad de análisis fue una predicción atómica, atribuible y con horizonte vencido. Se excluyeron exhortaciones, amenazas sin afirmación futura, objetivos normativos, condicionales sin expectativa adoptada y frases cuyo horizonte no había vencido. Las predicciones podían ser de clase A —suficientemente específicas en el original— o B —operacionalizadas sin alterar su dirección sustantiva—. El corpus final contiene 5 A y 115 B.

La extracción completa quedó congelada antes de habilitar la búsqueda de resultados. El archivo [registro_extraccion_congelado_v1.0.csv](../work/registro_extraccion_congelado_v1.0.csv) tiene SHA-256 `323739E747379873D5786DB7057E7357EED0F70F0E6425AE6A3339B96AEDA32B`. El procedimiento y la regla de parada están documentados en [preregistracion_consolidada_v0.2.md](preregistracion_consolidada_v0.2.md) y [congelacion_corpus_outcome_blind_v1.0.md](congelacion_corpus_outcome_blind_v1.0.md).

Este fue un preregistro interno y outcome-blind, no un preregistro público con sello temporal externo. La distinción es importante: el historial de archivos conserva la separación entre extracción y desenlace, pero no ofrece la misma protección institucional que OSF u otro registro independiente.

### 2.2 Operacionalización previa al desenlace

Cada fila fijó:

1. sujeto, población, geografía y resultado esperado;
2. horizonte literal o heredado y fecha límite;
3. indicador observable;
4. umbral de éxito y de contradicción;
5. tipos de fuente admisibles;
6. reglas para duplicados, conflictos y datos ausentes.

Una frase como «el escaneo remoto de rangos completos dejará de ser razonable con IPv6» se convirtió, por ejemplo, en la exigencia de tres fuentes autoritativas que declarasen inviable el barrido exhaustivo y prescribiesen descubrimiento no secuencial. «Los móviles servirán de credencial» exigió un teléfono comercial y un despliegue real de acceso físico, no una demo de laboratorio.

La operacionalización agresiva aumenta auditabilidad a costa de fidelidad semántica. Ese riesgo se aceptó deliberadamente para producir un estudio comunicable, pero se conserva el texto literal junto con la reformulación para que el lector pueda impugnar cada traducción.

### 2.3 Evaluación de desenlaces

La fase de resultados siguió una jerarquía de evidencia: registros oficiales y legislación; documentación de fabricantes y operadores; artículos científicos y divulgaciones técnicas primarias; informes contemporáneos de organizaciones especializadas; y noticias como corroboración o localizador. Cada predicción recibió uno de tres juicios finales:

- **cumplida**, si alcanzó el umbral fijado;
- **incumplida**, si no lo alcanzó o satisfizo la contradicción;
- **indeterminada**, si la evidencia no permitía aplicar el umbral sin inferencia excesiva.

El protocolo contemplaba una categoría *mixed*, pero ningún caso terminó requiriéndola: los enunciados compuestos pudieron resolverse con su conjunción congelada o quedaron indeterminados. Los resultados, fuentes y justificaciones fila por fila están en [evaluacion_desenlaces_v1.0.csv](../work/evaluacion_desenlaces_v1.0.csv).

### 2.4 Análisis

El estimando principal es la proporción cumplida entre predicciones resolubles: cumplidas / (cumplidas + incumplidas). Se informa un intervalo Wilson binomial del 95% sólo como descriptor. Las predicciones no constituyen una muestra aleatoria independiente: están agrupadas dentro de 36 sesiones y una serie aporta 60,8% del corpus.

Se añadieron dos límites de sensibilidad: todos los indeterminados como fallos y todos como aciertos. También se repitió el resumen excluyendo *Security Nightmares* y se estratificó descriptivamente por forma de predicción. No se realizaron pruebas de significación entre subgrupos; sus tamaños y dependencia harían que una lectura causal fuese engañosa.

## 3. Resultados

### 3.1 Resultado global

De 120 predicciones, 54 cumplieron su umbral, 35 no lo hicieron y 31 quedaron indeterminadas (Tabla 1).

| Resultado | n | % |
|---|---:|---:|
| Cumplida | 54 | 45,0 |
| Incumplida | 35 | 29,2 |
| Indeterminada | 31 | 25,8 |
| Total | 120 | 100,0 |

Entre las 89 resolubles, acertaron 54: **60,7%** (IC Wilson 95%: **50,3–70,2%**). La cifra responde «sí, algo más que no», pero está lejos de justificar una reputación de clarividencia. Además, depende de cómo se interprete la ausencia de evidencia. El límite conservador es 45,0%; el optimista, 70,8%.

El 25,8% indeterminado no es mero residuo estadístico. Expone una propiedad de la prospectiva profesional: incluso una frase con fecha puede ser in-auditable si predice «más», «común» o «importante» sin una serie de medición que sobreviva hasta el futuro.

### 3.2 Dependencia de la serie dominante

*Security Nightmares* aporta 73/120 observaciones. Dentro de la serie hubo 33 aciertos, 17 fallos y 23 indeterminados: 66,0% de acierto entre resolubles. En las otras sesiones hubo 21, 18 y 8, respectivamente: 53,8% entre resolubles.

La diferencia descriptiva de 12,2 puntos no demuestra superioridad de sus ponentes. La serie se diseñó precisamente para enumerar pesadillas del año siguiente, produjo muchas predicciones de ocurrencia y repitió dominios con alta tasa base. Sí muestra que un único formato editorial puede mover el titular global del estudio.

### 3.3 Qué tipo de futuro fue más predecible

Las predicciones de ocurrencia —al menos un ataque, producto, regulación o controversia— lograron 65,7% entre resolubles. Los conteos alcanzaron 56,3%. Las cuatro predicciones de maduración de capacidad y las tres de saliencia se cumplieron, aunque esos grupos son demasiado pequeños para generalizar.

En el extremo opuesto, las siete predicciones de tendencia produjeron cero aciertos confirmados, dos fallos y cinco indeterminados. En prevalencia hubo un acierto y tres fallos. El hallazgo cualitativo es más estable que los porcentajes pequeños: los ponentes reconocieron tecnologías y conflictos emergentes mejor de lo que estimaron su velocidad o penetración.

### 3.4 Aciertos emblemáticos

Varios aciertos capturaron cambios reales antes de que fueran triviales:

- En 2005 se anticipó que un gusano móvil abandonaría el laboratorio en 2006; las familias Cabir y Commwarrior documentaron propagación autónoma en dispositivos reales.
- La predicción de filtraciones recurrentes se cumplió holgadamente en 2010 con múltiples datasets institucionales publicados por WikiLeaks.
- En 2011 se pronosticaron teléfonos como credenciales físicas y activación vocal siempre disponible. En 2012 HID desplegó Galaxy S III con llaves NFC en Netflix y Good Technology, y Samsung incorporó el disparador «Hi Galaxy» en móviles de masas.
- La ciberseguridad de dispositivos médicos ganó saliencia en 2013, incluido el inicio del programa regulatorio de la FDA.
- Toyota comercializó comunicación V2V/V2I en vehículos de producción japoneses en 2015.
- Rowhammer produjo en 2016 nuevos ataques prácticos —entre ellos Flip Feng Shui y Drammer—, y el conflicto Apple–FBI convirtió el acceso excepcional al cifrado en una confrontación jurídica y mediática masiva.
- La predicción técnica de que IPv6 requeriría enumeración no secuencial quedó respaldada por RFC 7707 y trabajos de generación de hitlists.
- En 2020 se produjo una operación cibernética iraní atribuida contra el proceso electoral estadounidense.
- La lectura menos sensacionalista del crédito social chino acertó: al cierre de 2020 predominaban listas sectoriales, reglas locales e intercambio de datos, no una puntuación universal de ciudadanía.

### 3.5 Fallos informativos

Los fallos también son útiles porque revelan errores de calendario, escala o arquitectura:

- eCall no fue equipamiento estándar en la mayoría de modelos europeos para 2016; la obligación para nuevos tipos llegó en 2018.
- Los móviles con huella de 2014 tendieron a comparar plantillas localmente, no en una nube remota.
- La neutralidad de red no se deterioró materialmente dentro de 2016 según el umbral; ese año entraron en vigor protecciones europeas y reglas indias.
- En 2019, el reconocimiento facial sencillo era común, pero la autenticación segura comparable a Face ID no representaba la mitad de los envíos mundiales.
- China no desplegó para 2020 el sistema obligatorio nacional de puntuación general que describían algunas keynotes.
- No se hallaron estudios que situaran el seguro cibernético entre 25% y 33,3% del presupuesto de seguridad para agosto de 2025.

Estos casos ilustran un patrón: muchas predicciones «fallidas» acertaron el tema, pero adelantaron la fecha, exageraron el alcance o eligieron el mecanismo equivocado. Bajo reglas retrospectivas laxas podrían haberse contado como éxitos narrativos.

## 4. Discusión

### 4.1 ¿Acertaron?

La respuesta más honesta es: **acertaron con frecuencia, pero no con precisión uniforme**. El 60,7% entre resolubles sugiere que las predicciones explícitas contenían información. No obstante, muchos enunciados tenían tasas base favorables: en un ecosistema adversarial, pronosticar «habrá al menos una nueva vulnerabilidad» es más fácil que pronosticar una prevalencia o tendencia cuantificada.

El resultado no compara a los ponentes con una línea base formal. Sin una tasa base —por ejemplo, qué porcentaje de eventos cyber plausibles ocurre en cualquier año— no puede interpretarse 60,7% como habilidad de forecasting. Este paper mide correspondencia retrospectiva bajo umbrales, no *skill score*.

### 4.2 La métrica es parte de la predicción

Las indeterminadas se concentraron donde el lenguaje dependía de recuentos retrospectivos inexistentes, poblaciones sin denominador o archivos propietarios. «Más controversias de privacidad» podría ser verificable si el ponente definiera un archivo de medios y una regla de deduplicación. «Común en empresas» requeriría una encuesta o medición repetida. Sin ello, el futuro puede llegar y aun así no ser auditable.

Para la práctica profesional, una buena predicción debería declarar cinco elementos: población, resultado observable, magnitud, fecha y fuente de resolución. Esa disciplina probablemente reduciría el dramatismo escénico, pero aumentaría el valor acumulativo de las conferencias.

### 4.3 El riesgo mediático y metodológico

El titular «los expertos acertaron seis de cada diez» es defendible sólo si se añade «entre los casos resolubles de este corpus». Omitir esa cláusula escondería 31 indeterminados, la concentración de 73 observaciones en una serie y la ausencia de muestreo probabilístico.

La lectura profesional más interesante es otra: **la industria anticipó mejor la dirección del cambio que su escala**. Esa formulación está respaldada por la diferencia entre ocurrencias/capacidades y tendencias/prevalencias, evita premiar predicciones vagas y conserva interés periodístico.

## 5. Limitaciones

Primero, el corpus no representa todas las keynotes de ciberseguridad. Depende de disponibilidad documental, idiomas revisables y venues con archivos recuperables. Segundo, *Security Nightmares* domina las observaciones y las predicciones dentro de una charla no son independientes. Tercero, 115/120 filas son clase B: el investigador tuvo que convertir lenguaje natural en umbrales, lo que introduce juicio aun antes de observar resultados.

Cuarto, la evaluación fue realizada por un solo codificador. La transparencia fila por fila permite auditoría externa, pero no sustituye una segunda codificación ciega ni una medida de acuerdo. Quinto, probar una ausencia histórica es mucho más difícil que localizar un evento positivo. Sexto, enlaces y páginas web pueden cambiar; se conservaron URL y síntesis, pero no una captura archivística completa de todas las fuentes. Séptimo, el preregistro fue interno: la separación outcome-blind está documentada mediante archivos y hashes, no certificada por un registro público independiente.

Finalmente, no existe una línea base de dificultad. Una extensión debería emparejar cada predicción con un pronóstico ingenuo, obtener probabilidades de los ponentes o comparar keynotes con analistas externos.

## 6. Conclusión

Esta auditoría convierte 120 frases sobre el futuro cyber en pruebas explícitas. Cincuenta y cuatro cumplieron, treinta y cinco no y treinta y una no pudieron resolverse. Entre las resolubles, el balance favorece a los ponentes por 60,7% a 39,3%, pero el resultado oscila entre 45,0% y 70,8% según el tratamiento de la incertidumbre.

Las conferencias detectaron con bastante éxito qué problemas emergerían: gusanos móviles, filtraciones, Rowhammer, cifrado, dispositivos médicos, IPv6 y operaciones electorales. Fueron menos fiables al anticipar cuánto crecerían, cuándo dominarían o qué arquitectura concreta adoptarían. El veredicto, por tanto, no es que las keynotes adivinen el futuro. Es que funcionan razonablemente como radar de temas y mucho peor como instrumento de medición.

La recomendación práctica es simple: toda keynote que quiera ser recordada por una predicción debería publicar también su criterio de resolución. Sin esa segunda mitad, el escenario puede ser brillante y aun así quedar fuera del alcance de la historia.

## Disponibilidad de datos y trazabilidad

- [Corpus congelado](../work/registro_extraccion_congelado_v1.0.csv)
- [Evaluación de los 120 desenlaces](../work/evaluacion_desenlaces_v1.0.csv)
- [Preregistro consolidado](preregistracion_consolidada_v0.2.md)
- [Informe de congelación](congelacion_corpus_outcome_blind_v1.0.md)
- [Protocolo de evaluación](protocolo_evaluacion_desenlaces_v1.0.md)
- [Resultados tabulados](resultados_auditoria_v1.0.md)

## Referencias seleccionadas

Las referencias probatorias completas se conservan por predicción en el registro de desenlaces. Fuentes transversales citadas en el texto incluyen [RFC 7707](https://www.rfc-editor.org/rfc/rfc7707), la documentación del [programa de ciberseguridad de dispositivos médicos de FDA](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity), la evaluación oficial estadounidense de [interferencia electoral de 2020](https://www.dni.gov/files/ODNI/documents/assessments/ICA-declass-16MAR21.pdf), el análisis de MERICS sobre el [sistema de crédito social chino](https://merics.org/en/report/chinas-social-credit-system-2021-fragmentation-towards-integration), las pruebas de endpoint de [AV-Comparatives](https://av-comparatives.org/tests/endpoint-prevention-response-epr-test-2021/) y el registro legislativo de [Congress.gov](https://www.congress.gov/).
