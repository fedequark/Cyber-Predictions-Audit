# Contraste RSAC y otros venues

**Versión 1.9 — 18 de septiembre de 2026.** Revisión exploratoria posterior al cierre del corpus. No modifica las 120 predicciones, sus juicios ni el estimador principal.

## 1. Qué puede afirmarse

RSAC contiene predicciones que resultaron acertadas. Sin embargo, el archivo histórico disponible no permite estimar una tasa de acierto de RSAC ni compararla con Black Hat, CCC o Virus Bulletin: no existe un denominador anual completo y reproducible para RSAC entre 2005 y 2018. La comparación defendible es entre **tipos de acierto y valor para una decisión**, no entre porcentajes por venue.

También deben distinguirse dos procedencias:

- **En el escenario de RSAC:** el *Cryptographers’ Panel* de 2018, preservado como sensibilidad fuera del marco principal.
- **En el ecosistema editorial de RSAC:** predicciones anuales publicadas por su Advisory Board. Son útiles para la narrativa, pero no deben describirse como frases pronunciadas en una sesión si sólo están documentadas en el sitio.

## 2. Casos RSAC acertados —y cuánto enseñan realmente

### A. GDPR: acierto verificable y relevante para una decisión

El 20 de diciembre de 2018, el Advisory Board de RSAC publicó que 2019 se concentraría fuertemente en las implicaciones y el *enforcement* del GDPR, y anticipó grandes actuaciones de las autoridades. El 21 de enero de 2019, la CNIL impuso a Google una sanción de **50 millones de euros** por infracciones del GDPR. La propia lista oficial de sanciones de la CNIL registra además otras seis multas durante 2019.

**Juicio exploratorio:** `fulfilled` para la proposición “2019 será un año de enforcement relevante del GDPR”. La evidencia es positiva, oficial y dentro del plazo.

**Valor informativo:** medio–alto. No fue sólo una coincidencia temática: ocurrió una actuación grande, fechada y cuantificada. Su dificultad debe moderarse porque el GDPR ya había entrado en aplicación y el debate sobre enforcement estaba abierto.

**Fuentes:** [predicción del RSAC Advisory Board](https://www.rsaconference.com/library/blog/2019-and-beyond-the-expanded-rsac-advisory-board-weighs-in-on-whats-next); [decisión oficial de la CNIL](https://www.cnil.fr/sites/default/files/atoms/files/san-2019-001.pdf); [registro oficial de sanciones de 2019](https://www.cnil.fr/fr/node/446).

### B. AES-256: acierto binario, pero con baseline muy alto

En el *Cryptographers’ Panel* de RSAC 2018 se estimó casi despreciable la posibilidad de una ruptura práctica de AES-256 durante el año siguiente. El candidato preservado fijó el vencimiento en el 17 de abril de 2019. No se documentó una ruptura práctica durante ese intervalo; AES-256 continuó dentro del estándar FIPS 197 de NIST.

**Juicio exploratorio:** `fulfilled`, con cautela: la continuidad del estándar es evidencia compatible, no una prueba exhaustiva de ausencia mundial.

**Valor informativo:** bajo–medio. Es un pronóstico técnicamente sensato, pero una regla base “los primitivas maduras no sufrirán una ruptura práctica el próximo año” ya tendría una probabilidad alta de acertar. El caso enseña que exactitud y *skill* no son sinónimos.

**Fuentes:** [página oficial del panel](https://www.rsaconference.com/Library/presentation/USA/2018/the-cryptographers-panel-2); [FIPS 197 de NIST](https://csrc.nist.gov/pubs/fips/197/final-%281%29).

### C. Ransomware y extorsión en 2016: radar temático correcto, mecanismo no demostrado

En diciembre de 2015, el Advisory Board de RSAC anticipó un 2016 de “extortapalooza”: más extorsión, industrialización del ransomware y especial vulnerabilidad del sector salud. Durante 2016, HHS informó un promedio de **4.000 ataques diarios de ransomware**, 300% por encima de 2015. El FBI/IC3 registró **2.673 denuncias de ransomware** con más de 2,4 millones de dólares en pérdidas y **17.146 denuncias relacionadas con extorsión** con más de 15 millones de dólares en pérdidas.

**Juicio exploratorio:** `fulfilled` para el componente amplio “la extorsión/ransomware aumentará y afectará al sector salud”.

**Reserva esencial:** la predicción también habló de equipos diagnósticos, terapéuticos o de soporte vital bloqueados hasta pagar. Las fuentes revisadas prueban el auge organizacional del ransomware, no ese mecanismo específico. La frase compuesta debe separarse; no es válido usar el acierto del tema para dar por acertado el detalle más extremo.

**Valor informativo:** alto como radar temático; menor como pronóstico de mecanismo. La retrospectiva de RSAC de noviembre de 2016 corrobora la relevancia del tema, pero no se usa como evidencia independiente porque RSAC evalúa aquí su propia predicción.

**Fuentes:** [predicciones RSAC para 2016](https://www.rsaconference.com/library/blog/security-in-2016-the-rsac-advisory-boards-industry-predictions); [HHS, *Ransomware and HIPAA*](https://www.hhs.gov/hipaa/for-professionals/security/guidance/cybersecurity/ransomware-fact-sheet/index.html); [FBI/IC3, *2016 Internet Crime Report*](https://www.ic3.gov/AnnualReport/Reports/2016_IC3Report.pdf); [retrospectiva editorial de RSAC](https://www.rsaconference.com/library/blog/rsac-2017-speaker-submissions-parallel-industry-predictions-and-real-world-events).

## 3. El control negativo dentro de RSAC: correcto en dirección, tarde

El mismo panel de 2018 incluyó la conjetura de que NIST elegiría al menos un esquema de firma basado en hashes dentro del ciclo descrito como de tres años. El registro piloto congeló el 17 de abril de 2021 como fecha límite. NIST seleccionó SPHINCS+, basado en funciones hash, el 5 de julio de 2022.

**Juicio bajo la regla congelada:** `not_fulfilled`. La dirección fue correcta y el calendario no. Si se elimina el vencimiento después del resultado, el fallo se convierte artificialmente en acierto.

**Fuente de desenlace:** [anuncio oficial de NIST](https://www.nist.gov/news-events/news/2022/07/nist-announces-first-four-quantum-resistant-cryptographic-algorithms).

Este caso evita una selección promocional de éxitos y conecta directamente con el caso AVX-512 de Black Hat: en ambos, la tecnología llegó, pero después de la fecha anunciada.

## 4. Contraste útil para la charla

| Caso | Procedencia | Resultado estricto | Qué parecía medir | Qué mide al auditarlo |
|---|---|---|---|---|
| GDPR enforcement en 2019 | RSAC Advisory Board | Cumplida | Visión regulatoria | Evento grande, positivo y fechado; dificultad moderada |
| AES-256 sin ruptura práctica en un año | RSAC 2018 | Cumplida | Confianza criptográfica | Acierto con baseline muy alto y prueba de ausencia asimétrica |
| Ransomware/extorsión en 2016 | RSAC Advisory Board | Cumplida en lo amplio | Anticipación de amenaza | Buen radar temático; el mecanismo de dispositivos médicos no queda probado |
| NIST elegiría firma hash en tres años | RSAC 2018 | Incumplida | Dirección tecnológica | Dirección correcta, plazo fallido |
| AVX-512 en hardware Intel antes de agosto de 2015 | Black Hat 2014 | Incumplida | Dirección tecnológica | Dirección correcta, plazo fallido; llegó en 2016 |
| Referéndum neerlandés el 21 de marzo de 2018 | CCC 2017 | Cumplida | Precisión extrema | Calendario ya programado; casi no requiere forecasting |
| Elección estadounidense 2020 cerrada y divisiva | CCC 2018 | Cumplida | Anticipación política | Acierto relevante, pero dependiente de criterios previos para ambos adjetivos |

La conclusión no es “RSAC predice mejor”. Es más valiosa: **todos los venues producen una mezcla de señal útil, calendario conocido, afirmaciones de alta probabilidad, aciertos temáticos y errores de plazo**. El método permite distinguirlos sin atacar a los ponentes.

## 5. Cómo usarlo para aumentar la probabilidad de aceptación

La propuesta debe reconocer un acierto asociado a RSAC antes de presentar los límites. Esto evita que la charla parezca una crítica externa diseñada para desacreditar a la conferencia.

Arco recomendado:

1. Abrir con GDPR: una predicción RSAC que sí produjo señal accionable.
2. Mostrar ransomware: el tema fue correcto, pero una frase compuesta permite apropiarse de demasiado crédito.
3. Contrastar AES-256 con el referéndum: ambos “aciertan”, aunque por razones y con valor informativo muy distintos.
4. Emparejar NIST/SPHINCS+ con AVX-512: dos direcciones correctas que fallan el plazo, una en RSAC y otra en Black Hat.
5. Entregar la prueba de cinco campos para que CISOs separen radar temático de pronóstico apto para decisiones.

Frase de transición sugerida en inglés:

> RSAC forecasts did identify consequential shifts, including GDPR enforcement and the ransomware wave. But the audit shows why being directionally right is not yet enough for a budget or policy decision: leaders still need a magnitude, a deadline, a baseline, and a resolution source.

## 6. Texto corregido de motivación

La experiencia del autor no debe presentarse como una colección histórica de casos trazables. Es un patrón observado en años recientes:

> In recent years, repeated conversations with CISOs showed me how ideas heard at major cybersecurity conferences could become inputs to corporate strategy. I did not preserve those conversations as a retrospective dataset, so they motivate this research but are not evidence for its empirical claims. The recurring concern was that authority bias and confirmation bias could turn a memorable claim into a decision without testing its precision, evidence, or failure conditions.

## 7. Estado y siguientes pasos

Esta tanda añade un contraste favorable a RSAC sin sesgo de selección manifiesto: tres aciertos de distinta calidad y un fallo por vencimiento. Fortalece la propuesta porque demuestra que la charla no busca ridiculizar a la conferencia y porque transforma “acertó/no acertó” en una taxonomía útil para CISOs.

El siguiente salto de calidad sería una **mini-auditoría RSAC registrada**, con un marco reciente y completo (por ejemplo, todas las publicaciones anuales del Advisory Board en un intervalo fijado antes de resolver resultados). Hasta hacerla, estos casos deben seguir etiquetados como exploratorios y no pueden sostener una tasa comparativa entre venues.
