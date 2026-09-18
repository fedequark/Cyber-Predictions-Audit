# Estrategia de research y venues 2027

## Cyber Predictions Audit como paper publicable y charla de conferencia

**Versión 1.7 — 18 de septiembre de 2026.** Documento de decisión editorial. No modifica el corpus congelado ni sus desenlaces.

## 1. Decisión ejecutiva

El proyecto tiene una historia fuerte para conferencias, pero todavía no un paper listo para una revista académica exigente. La prioridad correcta es:

1. **Enviar una Track Session a RSAC 2027 antes del 9 de octubre de 2026.** El material actual ya sostiene una charla práctica y basada en datos. El mensaje debe ser “cómo reconocer y producir predicciones auditables”, no “los expertos aciertan 60,7%”.
2. **No enviar el research actual, sin una contribución nueva, a Black Hat Asia 2027.** El CFP cierra el 20 de octubre y prioriza material original/no publicado. El corpus, los resultados y el sitio ya son públicos. Además, el encaje temático en sus tracks técnicos es débil.
3. **Preparar una extensión demostrable para DEF CON 35 y, si se anuncia, DEF CON Singapore 2027.** La versión DEF CON necesita una herramienta abierta, una demostración y una narrativa más adversarial: auditar una predicción como se audita una afirmación de seguridad.
4. **Reescribir el paper en inglés después del sprint RSAC.** La publicación académica debe incorporar el antecedente directo de Schatz y Bashroush (2019), una formulación nueva de las RQ y validación independiente antes de aspirar a una revista fuerte.

El mismo núcleo empírico puede alimentar las tres charlas, pero no debe reciclarse como una propuesta idéntica. Cada venue requiere una promesa distinta y, en Black Hat, material sustantivamente nuevo declarado con precisión.

## 2. Diagnóstico del research actual

### 2.1 Lo que ya es fuerte

- Corpus público de 120 afirmaciones explícitas, extraídas de 36 sesiones dentro de un marco documental de 189 sesiones.
- Congelación *outcome-blind* de afirmaciones, horizontes, indicadores y umbrales antes de buscar desenlaces.
- Trazabilidad fila por fila y publicación de casos indeterminados, en vez de descartarlos.
- Sensibilidades por indeterminación, concentración, sesión, fuerza de evidencia y baseline.
- Sitio público reproducible y datos descargables.
- Resultado contraintuitivo y comunicable: 60,7% entre resolubles, pero 60,7% también para la regla trivial “todo se cumple”.

### 2.2 Lo que hoy impide venderlo como paper top

1. **El antecedente más cercano no está discutido.** Schatz y Bashroush (2019) analizaron 238 predicciones de seguridad publicadas para 2016, las redujeron a 17 tópicos y evaluaron su realización mediante encuesta y fuentes secundarias. El paper actual cita teoría general de forecasting, pero no este trabajo directo.
2. **La novedad está formulada demasiado débilmente.** “Auditar predicciones cyber” ya tiene precedente. La novedad defendible está en la operacionalización prospectiva al desenlace, la unidad de análisis literal, la preservación de indeterminados, los baselines y la auditoría reproducible.
3. **La pregunta principal privilegia el porcentaje de aciertos.** Ese porcentaje no mide *skill* y coincide con un clasificador trivial. Debe convertirse en un resultado secundario dentro de una pregunta sobre auditabilidad y validez de inferencia.
4. **Un solo codificador sigue siendo la principal amenaza de validez.** La doble codificación está pospuesta. Es aceptable para presentar el método con transparencia, pero limita una publicación académica fuerte.
5. **La muestra no representa “las conferencias de ciberseguridad”.** Es una muestra documental de tres venues, dominada por una familia de sesiones. El título y las conclusiones deben evitar universalizar.
6. **No hay registro histórico de candidatos textuales excluidos.** Por eso no puede estimarse qué proporción de toda la retórica prospectiva fue descartada durante la extracción.
7. **El manuscrito está en español y su revisión de literatura es breve.** Para una revista internacional necesita inglés, comparación sistemática con trabajo previo y una sección de construct validity más profunda.

### 2.3 Evaluación de madurez al 18 de septiembre de 2026

| Dimensión | Estado | Lectura |
|---|---:|---|
| Reproducibilidad técnica | 8/10 | Datos, scripts, hashes y sitio son una ventaja real. |
| Trazabilidad metodológica | 8/10 | La cadena afirmación–umbral–evidencia es inspeccionable. |
| Validez interna | 5/10 | Un codificador y 115/120 operacionalizaciones clase B. |
| Validez externa | 4/10 | Tres venues, concentración alta y selección documental. |
| Posicionamiento frente al estado del arte | 3/10 | Falta el antecedente empírico más cercano. |
| Manuscrito académico | 5/10 | Honesto y sólido, pero aún descriptivo y local. |
| Charla RSAC | 8/10 | Resultado memorable y recomendaciones accionables. |
| Briefing Black Hat, material actual | 3/10 | Novedad pública y encaje de track insuficientes. |
| Charla DEF CON con demo nueva | 7/10 | Buen potencial narrativo si se construye una herramienta. |

## 3. Replanteamiento científico

### 3.1 Tesis central recomendada

> El problema de las predicciones de ciberseguridad no es sólo si terminan siendo verdaderas, sino si fueron formuladas de modo que pudieran estar equivocadas. Una auditoría reproducible muestra que la tasa bruta de acierto puede igualar un baseline trivial, mientras que precisión, resolubilidad y procedencia de evidencia determinan qué conclusiones son válidas.

Esta tesis preserva el hallazgo más interesante y evita presentar 60,7% como una medida de talento predictivo.

### 3.2 Research questions para el paper

**RQ1 — Resolución y resultados.** Entre las predicciones explícitas incluidas mediante el protocolo congelado, ¿qué proporción puede resolverse y qué resultados obtiene bajo umbrales especificados antes de observar el desenlace?

**RQ2 — Robustez inferencial.** ¿Cuánto cambian las conclusiones al considerar indeterminados, dependencia dentro de sesiones, concentración del corpus, fuerza de evidencia y baselines triviales?

**RQ3 — Auditabilidad.** ¿Qué propiedades observables de una afirmación —horizonte, población, geografía, magnitud, mecanismo y fuente de resolución— se asocian exploratoriamente con su resolubilidad y dificultad?

**RQ4 — Diseño prospectivo.** ¿Qué especificación mínima permite convertir una predicción de conferencia en un pronóstico falsable, reproducible y útil para decisiones?

RQ1 y RQ2 pueden sostenerse con el paquete actual. RQ3 debe permanecer exploratoria hasta validar el codebook y repetir la codificación de forma independiente. RQ4 es una contribución de diseño derivada de los fallos observados y debe probarse en una réplica prospectiva.

### 3.3 Contribuciones defendibles

1. Un corpus longitudinal, abierto y trazable de predicciones literales extraídas de sesiones de conferencias, con marco de selección explícito.
2. Un protocolo *outcome-blind* que separa extracción/operacionalización de adjudicación de desenlaces.
3. Un análisis que muestra por qué la tasa de acierto sin probabilidades, alternativas y baseline no equivale a habilidad predictiva.
4. Un tratamiento explícito de la indeterminación y la evidencia faltante como resultados metodológicos, no como filas descartables.
5. Una tarjeta prospectiva reutilizable para producir predicciones futuras auditables.

### 3.4 Diferencia frente al antecedente directo

| Dimensión | Schatz y Bashroush (2019) | Cyber Predictions Audit |
|---|---|---|
| Material | 238 predicciones publicadas para 2016 | 120 afirmaciones literales en conferencias, 2005–2018 |
| Unidad analítica | 17 tópicos latentes obtenidos con LDA | Predicción atómica con cita y localizador |
| Resolución | Opinión de 134 participantes y fuentes secundarias | Umbrales y fuentes admisibles congelados antes del desenlace |
| Resultado ausente | No es la contribución central | Categoría `indeterminate` preservada y analizada |
| Baseline/*skill* | No es el foco | Baselines explícitos; se evita inferir *skill* |
| Reproducibilidad | Resultado agregado | Datos, reglas, hashes, scripts y explorador por fila |

La afirmación de novedad no debe ser “primera evaluación de predicciones de ciberseguridad”. Debe ser “primera auditoría longitudinal y reproducible, a nivel de afirmación, con operacionalización previa al desenlace y tratamiento explícito de indeterminación”, sujeta a completar una revisión bibliográfica sistemática antes de usar “primera”.

## 4. Estrategia por venue

### 4.1 RSAC 2027 — prioridad inmediata

**Estado oficial:** CFP abierto; cierre el 9 de octubre de 2026 a las 23:59 PT. Conferencia del 5 al 8 de abril de 2027 en San Francisco. Las Track Sessions duran 50 minutos con preguntas incluidas.

**Encaje recomendado:** `Breaking Research & Emerging Cyber Trends`, nivel intermedio. Segunda opción: `CISO Insights & Business Strategy` si el contenido se centra en decisiones, presupuesto y comunicación de riesgo.

**Promesa al público:** salir con una prueba de cinco preguntas para decidir si una predicción merece influir en estrategia, y con una plantilla para reformularla de modo auditable.

**Mensaje:** no se trata de avergonzar ponentes ni de decidir quién “adivinó”. Se trata de evitar que señales temáticas vagas se conviertan en certezas ejecutivas.

**Arco sugerido de 50 minutos:** 

- 0–5: una predicción que parece correcta hasta intentar puntuarla.
- 5–12: cómo se construyó y congeló el corpus.
- 12–22: 54/89, indeterminación y por qué 60,7% no es *skill*.
- 22–31: qué tipos de afirmaciones resisten o fallan la auditoría.
- 31–40: cinco campos de una predicción auditable.
- 40–45: aplicación a decisiones a una semana, seis semanas y seis meses.
- 45–50: preguntas.

**Títulos de trabajo para que el autor reescriba con su propia voz:**

- `We Audited 120 Cyber Predictions. Accuracy Was the Wrong Question`
- `From Hype to Falsifiable: Auditing Cybersecurity Predictions`
- `Your Cyber Forecast Needs an Expiration Date`

**Riesgo principal:** una propuesta demasiado académica o dedicada a explicar el problema. RSAC pide profundidad, diferenciación y resultados accionables; el detalle de sesión debe mostrar casos, números y herramientas que el público aplicará.

### 4.2 Black Hat Asia 2027 — evaluar, no reciclar

**Estado oficial:** CFP de Briefings abierto; cierre el 20 de octubre de 2026 a las 23:59 SGT. Briefings el 2 y 3 de marzo de 2027 en Singapur. Formatos de 20, 30 o 40 minutos.

**Veredicto con el material actual:** **no enviar todavía**. El sitio y el repositorio ya publican el corpus y los hallazgos. El CFP pregunta expresamente por publicaciones previas, porcentaje de material nuevo y planes de publicación, y señala que el board prioriza contenido original no publicado. También prioriza demos y papers de grado académico.

**Encaje de track:** `Policy` es el menos forzado, porque acepta investigación y métricas sobre decisiones y sistemas de seguridad. `Human Factors` sólo sería defendible si se añade evidencia sobre cómo las formulaciones afectan juicio o decisión; el corpus actual no mide eso.

**Qué convertiría la propuesta en candidata:**

- una herramienta abierta nueva que analice una afirmación y produzca una ficha de falsabilidad, con demo;
- un estudio nuevo, predefinido, que compare codificadores o mida resolubilidad sin observar desenlaces;
- una réplica con material de Asia y un marco reconstruible, sin mezclarla retrospectivamente con los 120 casos;
- al menos 50% de material sustantivamente nuevo y una declaración exacta de todo lo ya publicado.

**Restricción crítica de autoría:** los términos del CFP de Black Hat prohíben texto generado por LLM y permiten IA sólo para editar/refinar material escrito por el autor o revisar prior art. Este documento no debe copiarse en el formulario. El autor debe redactar la propuesta; una revisión posterior puede comprobar claridad, consistencia y límites.

### 4.3 Black Hat USA 2027 — objetivo condicionado

El CFP 2027 aún no está publicado. En 2026 abrió el 27 de enero y cerró en marzo; esto sirve sólo como referencia de planificación, no como fecha prometida para 2027.

**Veredicto:** mejor objetivo Black Hat que Asia si entre octubre y enero se completa una contribución nueva técnica/demostrable. La versión para USA debe competir como research nuevo, no como difusión del paper existente.

**Gate de envío:** no preparar un Briefing hasta tener:

1. demo reproducible;
2. novedad no publicada claramente separable del corpus v1.6/v1.7;
3. paper técnico de soporte;
4. video de 2–3 minutos en inglés;
5. respuesta honesta y cuantificada sobre material previamente publicado.

### 4.4 DEF CON 35, Las Vegas — alta afinidad narrativa

**Estado oficial conocido:** DEF CON 35 está anunciado para el 5–8 de agosto de 2027 en Las Vegas. El CFP de charlas todavía no está anunciado.

**Promesa al público:** aprender a “romper” una predicción antes de que se use para vender miedo, presupuesto o certeza.

**Versión de la historia:** más adversarial, visual y participativa. En vivo, la audiencia recibe afirmaciones reales anonimizadas, intenta definir qué observación las refutaría y compara su criterio con el registro congelado.

**Títulos de trabajo:**

- `We Fact-Checked the Cyber Future`
- `Forecast Injection: How Cyber Predictions Evade Falsification`
- `Everything Happened: Breaking the Cyber Prediction Game`

**Contribución necesaria:** un `Forecast Falsifiability Linter` abierto o una experiencia equivalente. Sin demo, la charla corre el riesgo de sentirse como una lectura de paper.

### 4.5 DEF CON Singapore 2027 — vigilar, no asumir

DEF CON celebró su primera conferencia de Singapur en 2026. Al 18 de septiembre de 2026 existe una convocatoria oficial para **training** en Singapur 2027, con fechas tentativas del 10 al 12 de marzo, pero no se verificó un CFP de charlas 2027 ni fechas finales de la conferencia. No debe presentarse como oportunidad confirmada todavía.

Si aparece el CFP, el mismo criterio que para Las Vegas aplica: demo y participación. Una extensión con material regional mejoraría relevancia, pero no debe añadirse apresuradamente al corpus congelado.

## 5. Estrategia de publicación del paper

### 5.1 Secuencia recomendada

1. Mantener v1.5 como resultado congelado y v1.7 como capa editorial, sin reescribir retroactivamente el análisis.
2. Entregar RSAC con el dataset actual y una promesa práctica.
3. Completar revisión de literatura y redactar un manuscrito inglés v2.0.
4. Completar validación independiente de una muestra antes del envío académico. La decisión previa de posponerla se respeta, pero el paper debe declarar que sigue siendo un gate de publicación fuerte.
5. Registrar externamente el protocolo de cualquier ampliación antes de extraer nuevos desenlaces.
6. Depositar una release citable con DOI cuando quede definido qué material debe permanecer no publicado para Black Hat.
7. Enviar el paper a una revista aplicada después de una revisión de encaje y políticas editoriales vigentes.

### 5.2 Título académico recomendado

`From Predictions to Falsifiable Claims: A Reproducible Retrospective Audit of Cybersecurity Conference Forecasts, 2005–2018`

### 5.3 Estructura del manuscrito v2.0

1. Introducción: influencia de predicciones y problema de auditabilidad.
2. Trabajo relacionado: forecasting cuantitativo, predicciones de seguridad, auditoría retrospectiva y ciencia abierta.
3. Constructos: predicción, resolubilidad, cumplimiento, calibración y *skill*.
4. Marco y selección documental.
5. Protocolo *outcome-blind* y adjudicación.
6. RQ1–RQ4 y plan analítico.
7. Resultados confirmatorios.
8. Diagnósticos exploratorios claramente separados.
9. Amenazas a validez: selección, coder, operacionalización, evidencia mutable y dependencia.
10. Implicaciones: plantilla prospectiva y agenda de réplica.

### 5.4 Política de originalidad y publicación

El research ya es público. No se debe intentar presentarlo como inédito. Para RSAC esto no aparece como una exclusión en las páginas revisadas y la transparencia fortalece la propuesta. Para Black Hat, la publicación previa debe declararse y una propuesta sólo es competitiva si contiene investigación o tooling nuevos. El DOI del paquete existente mejora citabilidad, pero conviene decidir el alcance de la próxima release antes de publicar cualquier componente reservado como novedad de Black Hat.

## 6. Sprint operativo

### Hasta el 25 de septiembre

- Autor: escribir en inglés, con voz propia, un párrafo de “hard-won lesson” y tres casos que pueda contar en escena.
- Research: integrar el antecedente de 2019 y cerrar la matriz de contribuciones.
- Talk: seleccionar track RSAC, nivel y tres takeaways aplicables.
- Speaker proof: elegir o grabar una muestra breve en inglés.

### 26 de septiembre–2 de octubre

- Redactar la propuesta RSAC completa desde el material del autor.
- Hacer dos revisiones: una de contenido y otra como reviewer competitivo.
- Diseñar tres slides prueba: baseline trivial, anatomía de una predicción y checklist de cinco campos.

### 3–8 de octubre

- Rehearsal de diez minutos con cronómetro.
- Recortar generalidades y añadir detalle verificable.
- Completar campos del portal y validar límites de caracteres.
- Enviar antes del último día.

### 10–20 de octubre

- Decidir Black Hat Asia con un gate binario: sólo enviar si existe contribución nueva demostrable y texto escrito por el autor.
- Si el gate falla, no forzar el venue; mover el objetivo a Black Hat USA 2027.

### Octubre de 2026–enero de 2027

- Construir el linter/prototipo y la demo.
- Redactar paper v2.0 en inglés.
- Completar revisión independiente cuando el autor decida reactivar esa tarea.
- Preparar propuestas DEF CON y Black Hat USA adaptadas, no clonadas.

## 7. Próximos gates de calidad

| Gate | Criterio de salida |
|---|---|
| G1 — RSAC | Propuesta completa, específica, con tres takeaways y detalle de sesión; escrita/revisada por el autor. |
| G2 — Literatura | Matriz de prior art con búsqueda documentada y afirmación de novedad no absoluta. |
| G3 — Validación | Acuerdo independiente reportado para extracción/operacionalización y desenlaces. |
| G4 — Demo | Herramienta reproducible que convierte una afirmación en especificación auditable. |
| G5 — Paper | Manuscrito inglés, RQ explícitas, contribuciones comparadas y amenazas de validez completas. |
| G6 — Publicación | Release inmutable, DOI, declaraciones de autoría/IA, financiación, conflictos y ética. |

## 8. Fuentes oficiales y literatura clave

- RSAC 2027 Call for Submissions: https://www.rsaconference.com/usa/call-for-submissions
- RSAC 2027 Tips: https://www.rsaconference.com/usa/call-for-submissions/tips
- RSAC 2027 Process: https://www.rsaconference.com/usa/call-for-submissions/process
- RSAC 2027 FAQ: https://www.rsaconference.com/usa/call-for-submissions/faq
- RSAC 2027 Tracks: https://www.rsaconference.com/usa/call-for-submissions/tracks
- Black Hat Call for Briefings: https://blackhat.com/call-for-papers.html
- Black Hat Asia tracks: https://blackhat.com/html/tracks-asia.html
- Black Hat Asia 2027 preparation document: https://i.blackhat.com/asia-27/BHAS27-Call%20for%20Briefings-Preparation-Doc.pdf
- DEF CON 35 announcement: https://forum.defcon.org/node/253966
- DEF CON Singapore announcement: https://forum.defcon.org/node/253433
- DEF CON Training Singapore 2027: https://training.defcon.org/pages/2027-singapore-call-for-trainers-march-def-con-sg
- Schatz, D. y Bashroush, R. (2019). *Security predictions—A way to reduce uncertainty*. Journal of Information Security and Applications, 45, 107–116. https://doi.org/10.1016/j.jisa.2019.01.009
- Husák, M., Komárková, J., Bou-Harb, E. y Čeledá, P. (2019). *Survey of Attack Projection, Prediction, and Forecasting in Cyber Security*. IEEE Communications Surveys & Tutorials, 21(1), 640–660. https://doi.org/10.1109/COMST.2018.2871866

## 9. Estado después de esta tanda

El proyecto queda mejor posicionado porque ya no confunde tres productos diferentes:

- **dataset/auditoría pública:** existe y es reproducible;
- **paper académico:** requiere reposicionamiento, literatura y validación;
- **charla:** puede enviarse ya a RSAC con un mensaje accionable.

El próximo cuello de botella no es recopilar más cifras. Es convertir la experiencia del autor en una propuesta RSAC específica antes del 9 de octubre, mientras se protege una contribución realmente nueva para Black Hat o DEF CON.
