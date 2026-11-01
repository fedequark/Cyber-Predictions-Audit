# De predicciones públicas a juicios auditables

## Obstáculos de operacionalización y evidencia en 120 predicciones de conferencias de ciberseguridad, 2005–2018

**Versión 1.6 — 23 de septiembre de 2026.** Reencuadre metodológico posterior al análisis y revisión focal asistida por cuatro IAs. Los registros congelados y los juicios originales de desenlace no se alteran. Este manuscrito presenta un **estudio de caso exploratorio**; no estima la habilidad predictiva de ponentes ni de conferencias.

### Resumen

**Problema.** Una predicción pública puede parecer acertada sin especificar población, fecha, magnitud o fuente capaz de resolverla. Auditarla exige decisiones de interpretación que también pueden cambiar el resultado.

**Objetivo.** Describir qué obstáculos aparecen al convertir **120 predicciones incluidas** de un corpus documental de conferencias de ciberseguridad en juicios de desenlace trazables. La pregunta original —qué proporción superaba los umbrales registrados— se conserva como análisis descriptivo; el énfasis en auditabilidad es **posterior al examen de los resultados**.

**Método.** Las 120 unidades proceden de 36 sesiones productivas entre 138 sesiones con material suficiente (S3) en un marco de 189. Antes de buscar desenlaces se registraron internamente reformulación, horizonte, indicador, umbrales y reglas de evidencia por unidad. **Codex figura como codificador inicial de las 120 extracciones y los 120 desenlaces.** Después se realizaron diagnósticos exploratorios, cuatro revisiones no humanas y una adjudicación focal del autor sobre 48 decisiones, con acceso a los votos de las IAs.

**Resultados.** Cinco unidades eran directamente puntuables (clase A); **115/120** requirieron operacionalización (clase B). La codificación original fue 54 cumplidas, 35 incumplidas y 31 indeterminadas. Entre las 89 resolubles, 54 se codificaron como cumplidas (**60,7%**; intervalo Wilson descriptivo 95%: **50,3–70,2%**). Los extremos sobre las 120 unidades son **45,0–70,8%** si las 31 indeterminadas se tratan, alternativamente, como fallos o aciertos. Clasificar como «cumplida» toda unidad resoluble también produce 60,7%, por construcción. En la revisión focal posterior, las decisiones finales del autor divergieron de la codificación original en 6/18 desenlaces seleccionados por desacuerdo entre IAs; esto **no** es una tasa de error poblacional. Persisten cinco dudas semánticas entre 22 unidades revisadas y dos juicios positivos de búsqueda sin URL aportada por el autor.

**Conclusión.** El valor más sólido del trabajo es exponer, por unidad, cómo se pasó de una cita prospectiva a un criterio comprobable y dónde ese proceso sigue siendo incierto. La tasa de cumplimiento describe el registro original, no la capacidad predictiva de los conferencistas. La revisión focal detecta discrepancias, pero no reemplaza una segunda codificación humana ciega.

## 1. Preguntas y alcance de las afirmaciones

La pregunta **original del protocolo interno** fue: «¿Qué proporción de las predicciones públicas, explícitas, observables y con horizonte vencido del corpus recuperado se cumplió dentro del plazo anunciado?». Su estimando operativo fue `cumplidas / determinables`, bajo umbrales escritos antes de buscar desenlaces. Se informa el resultado de esa pregunta sin convertir la revisión posterior en una nueva serie confirmatoria.

La pregunta que organiza **esta versión, formulada después de conocer el corpus y sus dificultades**, es: **¿Qué límites de interpretación, operacionalización, disponibilidad de evidencia y reproducción aparecen al auditar las 120 predicciones incluidas?** Tres subpreguntas la hacen comprobable:

1. ¿Cuántas unidades necesitaron reglas añadidas para volverse puntuables y qué parte del conjunto quedó sin desenlace determinable?
2. ¿Cómo afectan la indeterminación, la concentración por sesión y las referencias base triviales a la interpretación de la tasa original?
3. ¿Qué desacuerdos aparecen en una revisión focal posterior, y cuáles pueden o no cerrarse con las fuentes disponibles?

No se pregunta qué fracción de **todas** las frases prospectivas de las charlas era auditable: no existe el registro histórico fila por fila de candidatos textuales excluidos para estimarla. Tampoco se mide calibración, discriminación o habilidad predictiva de los ponentes: las intervenciones no aportaron probabilidades comparables ni alternativas exhaustivas.

La contribución es un **estudio de caso metodológico con datos abiertos**, no la primera evaluación de predicciones de ciberseguridad. Schatz y Bashroush (2019) ya estudiaron predicciones de seguridad mediante temas y evaluación posterior. Aquí la unidad es la afirmación localizada, con indicador y regla de desenlace por fila, y se conservan explícitamente los resultados indeterminados.

## 2. Diseño y procedencia

### 2.1 Selección documental

El marco cerrado contenía **189 sesiones** de Black Hat USA, Chaos Communication Congress (CCC) y Virus Bulletin, entre 2005 y 2018. **138** tenían disponibilidad S3 al corte original: grabación sustancialmente completa, transcripción completa, artículo íntegro o diapositivas autosuficientes. Las **51** restantes no entraron en la extracción principal; tenían identificador y título en el marco original, pero 50 requerían búsqueda documental adicional y una era S1. RSA Conference quedó fuera porque no se reconstruyó un denominador histórico reproducible.

Las 138 sesiones S3 se recorrieron en un orden fijado por estrato de conferencia y período y por huella digital dentro de cada estrato. **36** aportaron al menos una unidad. La regla de parada retuvo las primeras **120** predicciones incluidas. Se conservaron sesiones improductivas en el denominador documental. La falta de fuentes S3 y la productividad muy desigual de las sesiones limitan la extrapolación; esta muestra no representa a todas las conferencias ni a todo su discurso sobre el futuro.

### 2.2 Unidad y registro previo al desenlace

Cada unidad incluida conserva cita literal, localizador temporal o de página, hablante, contexto, reformulación atómica, horizonte, indicador, umbral de éxito y contradicción, tipos de fuente admisible y tratamiento de evidencia faltante o conflictiva. El archivo de extracción se bloqueó antes de la búsqueda de desenlaces (SHA-256 `323739E747379873D5786DB7057E7357EED0F70F0E6425AE6A3339B96AEDA32B`). La secuencia se documentó **internamente**; no hubo depósito externo con sello temporal previo. Por ello, «congelado antes de buscar desenlaces» no equivale aquí a un preregistro externo verificable.

La clase A contiene **5** afirmaciones directamente puntuables. La clase B contiene **115** afirmaciones cuyo indicador, población, magnitud o mecanismo necesitó precisión operativa. Clase B no significa afirmación falsa o inválida; significa que el juicio depende más visiblemente de decisiones del investigador. La concordancia de esas decisiones con el sentido original requiere evaluación separada.

### 2.3 Codificación original y análisis posteriores

Los CSV de extracción y de evaluación atribuyen sus **120 filas a Codex (IA)**. En la evaluación inicial, este único codificador asignó `cumplida`, `incumplida`, `indeterminada` o `mixta`; el registro original no contiene casos mixtos. La autoría humana conserva responsabilidad editorial sobre el estudio, pero no debe confundirse con una segunda codificación de esas filas. La tasa `cumplidas / determinables`, el intervalo Wilson descriptivo y los extremos para indeterminadas pertenecían al plan operativo. La concentración, los indicadores aproximados de especificidad y dificultad, el remuestreo por sesión, las referencias base, la regresión y los diagnósticos de evidencia se definieron o calcularon después y son **exploratorios**.

El protocolo interno había previsto doble codificación de inclusiones/exclusiones, atomizaciones complejas y al menos una cuarta parte de los desenlaces. Esa validación **no se completó**. Tampoco se preservó un registro de todos los candidatos textuales excluidos, por lo que el acuerdo de inclusión/exclusión no puede reconstruirse del paquete actual.

### 2.4 Revisión focal posterior asistida por IA

Cuatro sistemas de IA (Codex, Claude, DeepSeek y Gemini) examinaron, cada uno, 30 desenlaces con evidencia suministrada, 30 reformulaciones semánticas y 8 búsquedas planteadas como independientes. **Codex también figura como codificador inicial**, por lo que su brazo posterior no es una réplica independiente de origen. La posibilidad real de consultar fuentes no fue equivalente: dos modelos declararon que no podían navegar en esa fase y DeepSeek se ejecutó por API sin navegación. Sus respuestas se usaron como **señales de discrepancia**, no como votos de verdad ni como codificadores humanos independientes.

Después, el autor cerró **48 decisiones focales**: los 18 desenlaces sin unanimidad entre IAs, 22 controles semánticos con al menos un voto «no» o «incierto», y las 8 búsquedas. La selección estaba **enriquecida por desacuerdo**. El autor vio los votos antes de cerrar cada caso; por tanto, esta etapa es adjudicación del autor asistida por IA y no una réplica ciega. Se conserva el JSON exportado, las matrices y una conciliación separada. Ninguna de estas decisiones reemplazó silenciosamente el registro original de 120 desenlaces.

## 3. Resultados originales y problemas de auditabilidad observados

### 3.1 Resolución y tasa descriptiva

| Juicio original | Unidades | Porcentaje de 120 |
|---|---:|---:|
| Cumplida | 54 | 45,0% |
| Incumplida | 35 | 29,2% |
| Indeterminada | 31 | 25,8% |

Entre las **89** unidades determinables, **54/89 = 60,7%** fueron codificadas como cumplidas (Wilson descriptivo 95%: **50,3–70,2%**). Si las 31 indeterminadas fueran todas fallos o todas aciertos, los extremos serían **45,0–70,8%** sobre el corpus completo. Son límites aritméticos, no probabilidades de que los casos faltantes se distribuyan de una u otra manera.

La regla trivial «toda unidad resoluble se cumple» obtiene el mismo 60,7% de exactitud por construcción. Una moneda justa como referencia matemática daría 50%, pero tampoco reproduce un pronóstico histórico. En consecuencia, la cifra 60,7% **no mide habilidad predictiva**.

### 3.2 Dónde se agregó juicio y dónde faltó evidencia

| Obstáculo observable en el paquete | Magnitud | Qué permite concluir —y qué no |
|---|---:|---|
| Operacionalización clase B | 115/120 | La mayoría necesitó precisión añadida; no cuantifica por sí sola cuántas reformulaciones son infieles. |
| Desenlace indeterminado | 31/120 | La fuente o el umbral no permitieron un juicio original concluyente; no equivale a fracaso del pronóstico. |
| Sin URL probatoria primaria ni secundaria en el registro original | 18/120: 17 indeterminadas y 1 incumplida | Señala un déficit de localización y preservación; no prueba inexistencia del fenómeno. |
| Concentración en la familia *Security Nightmares* | 73/120 | Limita la generalización a otras sesiones o conferencias. |
| Candidatos textuales excluidos | Recuento no disponible | Impide estimar qué proporción del discurso prospectivo inicial fue descartada. |

El inventario contiene **218 localizadores** de fuentes y cápsulas textuales asociadas a las filas, no copias verificables de todos los recursos originales. Una consulta HTTP posterior encontró enlaces accesibles, rotos y bloqueados, pero una respuesta de encabezados no certifica que el contenido conservado sea el mismo. Se documentó una correspondencia de ID (`CCC-2013-034`/`CCC-2013-043`) que afecta siete predicciones; los originales se preservan y el cruce se hace de forma explícita. Ninguno de estos diagnósticos autoriza a imputar automáticamente los 31 indeterminados.

### 3.3 Dependencia y análisis exploratorios

Las 120 predicciones proceden de **36 sesiones**, pero una serie recurrente aporta **73/120 (60,8%)**. El índice de concentración de Herfindahl por sesión es **0,044**, equivalente a **22,5** sesiones de igual peso. El remuestreo exploratorio de sesiones con reemplazo (20.000 repeticiones, semilla `20260913`) produjo **47,0–72,1%** para la tasa entre resolubles. Al retirar una sesión por vez, la tasa varió entre **58,5% y 63,5%**. Estos cálculos describen sensibilidad a la composición observada; no crean una muestra probabilística de conferencias.

Un indicador aproximado de dificultad, definido después del análisis principal, separó tasas entre casos resolubles de **73,3%** en la banda baja, **60,0%** en la media y **41,4%** en la alta. En un modelo logístico exploratorio, la razón de posibilidades asociada con dificultad fue **0,47** por una desviación estándar (intervalo agrupado 95% **0,27–0,81**). El indicador incorpora juicios de diseño y los casos están agrupados: este patrón no demuestra que los ponentes sean mejores «radares temáticos» ni identifica un mecanismo causal.

### 3.4 Qué añadió —y qué no— la revisión focal

| Componente focal | Decisiones finales del autor | Lectura válida |
|---|---|---|
| 18 desenlaces seleccionados por no unanimidad de IA | 10 cumplidas, 2 incumplidas, 5 indeterminadas y 1 mixta; **6/18** difieren del registro original | Mapa de desacuerdos en una selección difícil; no estimación de error del conjunto de 120. |
| 22 controles semánticos seleccionados por duda de IA | 17 «sí», 5 «incierto», 0 «no» | Persisten cinco dudas; «sí» no equivale a validación semántica ciega. |
| 8 búsquedas focales | 2 «cumplida», 6 «indeterminada» | Ninguna decisión del autor contiene URL en la exportación; los dos positivos requieren corroboración primaria exacta. |

Los cuatro modelos coincidieron en **12/30** desenlaces con evidencia suministrada y alcanzaron una mayoría de al menos tres votos en **21/30**. La discrepancia entre modelos sirvió para escoger casos de revisión, no para resolverlos por mayoría. Nueve respuestas del autor cambiaron entre la primera y la decisión final tras consultar las objeciones.

La conciliación revisó los seis desenlaces divergentes. En `39-CCC-2006-011-13`, una IA describió erróneamente [CVE-2007-1993](https://nvd.nist.gov/vuln/detail/CVE-2007-1993) como un fallo del sistema de archivos CIFS de Linux: el registro oficial lo atribuye al servicio RPC `pfs_mountd.rpc` de HP-UX. La fuente citada no prueba el disparador específico de montar o analizar un volumen elaborado exigido por la regla. En `59-CCC-2016-060-06`, el [repositorio de Anti-Adblock Killer](https://github.com/reek/anti-adblock-killer) acredita scripts y filtros, pero por sí solo no demuestra el mecanismo adaptativo o distribuido requerido. Para `23-CCC-2018-085-07`, el [índice APWG](https://apwg.org/trendsreports/) no documenta directamente la mayoría de tres series comparables y la campaña exigidas. Estas observaciones **limitan las fuentes presentadas**, no prueban que los fenómenos nunca ocurrieron.

Las dos búsquedas positivas merecen una distinción similar. La [presentación de GSM en 26C3](https://fahrplan.events.ccc.de/congress/2009/Fahrplan/events/3654.en.html) documenta una amenaza práctica y artefactos, pero el [CCC indicó](https://www.ccc.de/de/updates/2009/gsm-nicht-mehr-sicher) que el proyecto no usó datos GSM reales por motivos legales; no se acreditó aquí el umbral completo de ataque reproducible contra una red desplegada. Las [notas de Cellebrite de marzo de 2017](https://media.cellebrite.com/wp-content/uploads/2017/07/UFED6.1_ReleaseNotes_EN.pdf) y un anuncio contemporáneo reproducido por prensa apoyan la capacidad de extraer datos de iPhone bloqueados, pero la documentación primaria accesible no une inequívocamente modelo, versión y barrera de contraseña en un mismo caso. Ambos juicios siguen separados de la tasa original.

## 4. Discusión

Este estudio muestra que «evaluar predicciones» no es sólo contar aciertos. La decisión pasa por seleccionar una unidad, atribuirla, fijar su horizonte, transformar su lenguaje en un indicador, especificar umbrales y encontrar evidencia que responda exactamente a ellos. **Las 115 unidades B no demuestran un defecto en las charlas**, sino cuánto trabajo de traducción requirió el instrumento de medición. Los 31 indeterminados y los desacuerdos posteriores hacen visible el coste de esa traducción.

La evidencia permite defender un procedimiento trazable y una cifra descriptiva **condicionada a la codificación original**. No permite comparar el talento de ponentes, estimar precisión de todas las charlas, ni declarar validado el 60,7% mediante cuatro IAs y una revisión no ciega del autor. El antecedente de Schatz y Bashroush (2019) sitúa este trabajo dentro de una literatura ya existente; la diferencia propuesta es el seguimiento por afirmación localizada y el tratamiento explícito de indeterminación, no una prioridad histórica de «primer estudio».

Una réplica prospectiva podría registrar desde el inicio cada candidato descartado, emplear dos codificadores humanos antes de buscar resultados, conservar las fuentes y fijar una probabilidad y una línea base por pronóstico. Es un programa de investigación futuro, no un experimento completado en este corpus.

## 5. Limitaciones y decisiones de integridad

- **Validez de constructo:** 115/120 reglas son clase B. La revisión semántica focal posterior deja cinco casos inciertos; no valida las 115 atomizaciones.
- **Fiabilidad y uso de IA:** los 120 registros originales de extracción y los 120 juicios de desenlace atribuyen la codificación a Codex. La adjudicación humana posterior cubrió 48 decisiones focales después de ver votos de IA; no constituye validación independiente del corpus completo ni sustituye la doble codificación humana prevista.
- **Selección:** tres conferencias, disponibilidad S3 desigual y 73 unidades de una serie; no hay muestra aleatoria de predicciones públicas. La ausencia del registro de candidatos excluidos impide medir pérdidas durante la selección textual.
- **Evidencia y ausencia:** algunas fuentes permiten verificar un acontecimiento pero no el umbral preciso; la falta de hallazgo no autoriza por sí sola a codificar «incumplida». Dieciocho juicios originales carecen de URL probatoria.
- **Temporalidad del protocolo:** el registro de afirmaciones se bloqueó internamente antes de buscar desenlaces, pero el preregistro no recibió sello temporal externo previo. El reencuadre de esta versión y los diagnósticos posteriores se declaran posteriores al análisis principal.
- **Inferencia:** la tasa sobre casos resolubles depende de cuáles resultaron resolubles; Wilson es descriptivo, y el remuestreo por sesión no corrige sesgo documental. El indicador aproximado de dificultad y la regresión no establecen causalidad.
- **Trazabilidad:** se conservan citas, localizadores y cápsulas, pero no una copia inmutable completa de todos los recursos remotos. La discrepancia de ID de una sesión se conserva visible.

## 6. Conclusión

En este corpus documental, convertir predicciones explícitas en juicios auditables requirió operacionalizar **115/120** unidades y dejó **31/120** desenlaces indeterminados. La codificación original clasificó **54 de 89** casos resolubles como cumplidos, pero esa proporción es descriptiva y coincide con una regla trivial que siempre responde «cumplida». La revisión posterior asistida por cuatro IAs hizo visibles desacuerdos y problemas concretos de evidencia; no produjo una validación humana independiente ni una nueva tasa confirmada. La contribución defendible es publicar el recorrido **cita → regla → fuente → juicio**, incluidos sus puntos de incertidumbre, para que cada inferencia pueda discutirse y reproducirse sin confundir auditabilidad con habilidad predictiva.

## Datos, código y versiones

- [Protocolo interno original](preregistracion_consolidada_v0.2.md) y [registro del bloqueo previo a desenlaces](congelacion_corpus_outcome_blind_v1.0.md).
- [Corpus congelado](../work/registro_extraccion_congelado_v1.0.csv), [desenlaces originales](../work/evaluacion_desenlaces_v1.0.csv) y [capa derivada](../work/analisis_derivado_v1.2.csv).
- [Métricas de robustez](../work/metricas_robustez_v1.2.csv), [manual de indicadores aproximados](codebook_proxies_v1.2.md) y [auditoría de evidencia/muestra](auditoria_muestra_y_evidencia_v1.4.md).
- [Marco maestro de 189 sesiones](../work/marco_maestro_189_sesiones_v0.9.csv), [inventario de localizadores](../work/inventario_fuentes_v1.2.csv) y [auditoría de operacionalización](auditoria_compromiso_y_operacionalizacion_v1.4.md).
- [Resultados de las cuatro IAs](../work/convalidacion_ia_v1.0/RESULTADOS_PARCIALES.md), [revisión exportada del autor](../work/convalidacion_ia_v1.0/REVISION_AUTOR_2026-09-23.json) y [conciliación focal](../work/convalidacion_ia_v1.0/CONCILIACION_REVISION_AUTOR_2026-09-23.md).
- [Manuscrito 1.5](paper_auditoria_predicciones_cyber_v1.5.md), conservado sin reencuadrar retrospectivamente el protocolo original.

## Derechos y declaraciones

El software original se ofrece bajo MIT y los aportes originales de investigación y base de datos bajo CC BY 4.0; las citas literales de terceros no quedan sublicenciadas. El alcance por campo consta en [RIGHTS.md](../RIGHTS.md).

**Autoría de decisiones:** Codex figura como codificador de las 120 filas originales de extracción y desenlace; el autor realizó después una revisión focal de 48 decisiones con los votos de Codex, Claude, DeepSeek y Gemini a la vista. **Validación humana independiente:** no realizada. **Preregistro externo previo:** no realizado.

**Financiación:** el autor declara que este trabajo no recibió financiación. **Conflictos de interés:** el autor declara no tener conflictos de interés.

**Ética:** se analizaron materiales disponibles públicamente y no se reclutaron participantes para este estudio. No se afirma contar con una aprobación o exención ética institucional; la formulación formal de esta declaración deberá ajustarse a las exigencias del destino de envío.

## Referencias

Gneiting, T., Balabdaoui, F. y Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. *Journal of the Royal Statistical Society: Series B*, 69(2), 243–268. https://doi.org/10.1111/j.1467-9868.2007.00587.x

Mellers, B. et al. (2014). Psychological strategies for winning a geopolitical forecasting tournament. *Psychological Science*, 25(5), 1106–1115. https://doi.org/10.1177/0956797614524255

Schatz, D. y Bashroush, R. (2019). Security predictions—A way to reduce uncertainty. *Journal of Information Security and Applications*, 45, 107–116. https://doi.org/10.1016/j.jisa.2019.01.009

Tetlock, P. E., Mellers, B. A. y Scoblic, J. P. (2017). Bringing probability judgments into policy debates via forecasting tournaments. *Science*, 355(6324), 481–483. https://doi.org/10.1126/science.aal3147
