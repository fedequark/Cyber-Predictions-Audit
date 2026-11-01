# Narrativa y borrador RSAC 2027

**Versión 1.8 — 18 de septiembre de 2026.** Construido a partir de la experiencia escrita por Federico Pacheco y de los casos congelados del corpus. Debe ser revisado y reescrito finalmente por el autor antes de enviarlo.

## 1. Experiencia del autor, editada

### Inglés

I began this research after repeated conversations with CISOs who used ideas heard at major cybersecurity conferences as inputs to corporate strategy. The problem was not listening to experts. It was the way authority bias and confirmation bias could turn a memorable conference claim into a corporate decision without testing its evidence, precision, or failure conditions. I wanted a better way to advise security leaders: preserve conferences as an early-warning radar, while distinguishing signals worth investigating from forecasts strong enough to support a decision.

### Español de control

Inicié esta investigación después de conversar repetidamente con CISOs que usaban ideas escuchadas en grandes conferencias como insumos de su estrategia corporativa. El problema no era escuchar a expertos, sino cómo el sesgo de autoridad y el de confirmación podían convertir una afirmación memorable en una decisión corporativa sin examinar su evidencia, precisión o condiciones de fallo. Quería una forma mejor de asesorar a líderes: conservar las conferencias como radar temprano, distinguiendo señales para investigar de pronósticos suficientemente sólidos para respaldar decisiones.

## 2. Casos extremos defendibles

### A. El mayor fallo cuantitativo: cyber insurance

**Caso:** `93-BHKEY-2015-01-01`, Jennifer Granick, *The Lifecycle of a Revolution*.

**Predicción operacionalizada:** para el 5 de agosto de 2025, el seguro cyber consumiría entre 25% y 33,3% del presupuesto de ciberseguridad de las organizaciones que lo compraran.

**Resultado:** `not_fulfilled`, evidencia moderada. El mercado creció, pero los estudios de presupuesto localizados dejaron el gasto en seguros muy por debajo de un cuarto y no aportaron dos estimaciones centrales dentro del rango anunciado.

**Por qué sirve en escena:** es la afirmación con horizonte más largo y magnitud presupuestaria más agresiva entre los fallos de alta dificultad. Habla directamente a CISOs: acertar que una categoría crecerá no valida cuánto presupuesto absorberá.

### B. El fallo por calendario: AVX-512

**Caso:** `4-BHPRO-2014-03-03`, Quynh Nguyen Anh, *Capstone: Next Generation Disassembly Framework*.

**Predicción operacionalizada:** habría AVX-512 en hardware Intel real antes del 7 de agosto de 2015.

**Resultado:** `not_fulfilled`, evidencia fuerte. Intel identifica Knights Landing como la primera implementación y el Xeon Phi 7250 fue lanzado en Q2 de 2016.

**Por qué sirve en escena:** el mecanismo tecnológico era correcto, pero el plazo explícito no. Si se borra la fecha, parece un acierto; si se conserva, es un fallo. Ilustra por qué una predicción necesita vencimiento y por qué no debe moverse el arco después del hecho.

### C. El “acierto perfecto” que no mide forecasting: referéndum neerlandés

**Caso:** `133-CCC-2017-072-01`, *Fuck Dutch mass-surveillance: let's have a referendum!*

**Predicción operacionalizada:** el referéndum neerlandés sobre la ley de inteligencia tendría lugar el 21 de marzo de 2018.

**Resultado:** `fulfilled`, evidencia fuerte; ocurrió exactamente ese día.

**Por qué sirve en escena:** una fecha oficial programada puede producir un acierto exacto sin requerir habilidad predictiva. El caso muestra que accuracy mezcla anticipación, calendario conocido y afirmaciones triviales si no se define una clase de referencia.

### D. La afirmación más grande que no se pudo resolver: todo el email mundial

**Caso:** `11-CCC-2005-002-09`, Frank Rieger, *We lost the war*.

**Predicción operacionalizada:** para el 27 de diciembre de 2015 existiría tecnología comercial explícitamente capaz de almacenar todo el tráfico mundial de email.

**Resultado:** `indeterminate`, evidencia moderada. Había estimaciones de 205.600 millones de emails diarios y archivos comerciales de escala petabyte, pero no se localizó documentación de producto que demostrara capacidad para “todo el email mundial”, ni evidencia que permitiera contradecirla.

**Por qué sirve en escena:** audaz no significa resoluble. Sin definición de tráfico, retención, duplicación, compresión y capacidad comercial disponible, el desenlace no puede adjudicarse honestamente.

### E. El acierto de alta saliencia: elección estadounidense de 2020

**Caso:** `30-CCC-2018-076-03`, J. Alex Halderman, *Election Cybersecurity Progress Report*.

**Predicción operacionalizada:** la elección presidencial estadounidense de 2020 sería cerrada y divisiva.

**Resultado:** `fulfilled`, evidencia fuerte. Estados decisivos quedaron por debajo de un punto porcentual y el periodo posterior incluyó litigios y esfuerzos para revertir la certificación.

**Por qué sirve en escena:** es un acierto intuitivamente potente, pero “cerrada” y “divisiva” requirieron criterios previos. Sin ellos, casi cualquier elección conflictiva podría contarse como acierto.

## 3. Selección para una charla de 50 minutos

Usar cuatro casos principales:

1. Cyber insurance — una cifra que podría afectar presupuesto.
2. AVX-512 — una tecnología correcta en el plazo equivocado.
3. Referéndum — un acierto exacto que no requiere forecasting.
4. Todo el email mundial — una predicción imposible de resolver con honestidad.

Dejar la elección de 2020 como caso de reserva o respuesta a preguntas. Esta selección cubre magnitud, tiempo, baseline y auditabilidad sin convertir la charla en una sucesión de anécdotas.

## 4. Borrador para el formulario RSAC

### Session title — máximo 75 caracteres

`We Audited 120 Cyber Predictions. Accuracy Was the Wrong Question`

### Abstract público — máximo 400 caracteres

Security leaders often turn memorable conference claims into strategy. We audited 120 explicit predictions from 36 cybersecurity sessions and found that the headline accuracy equaled a trivial baseline. Through four extreme cases, attendees will learn to separate thematic signals from decision-grade forecasts and apply a five-field test before a prediction influences budget or policy.

### Session detail privado — máximo 2.500 caracteres

I began this research after repeated conversations with CISOs who used ideas heard at major cybersecurity conferences as inputs to corporate strategy. Listening to experts was not the problem. Authority bias and confirmation bias could turn a memorable claim into a corporate decision without testing its evidence, precision, or failure conditions. I wanted a better way to advise security leaders.

I built a documentary frame of 189 sessions from Black Hat USA, Chaos Communication Congress, and Virus Bulletin. From 138 sessions with qualifying material, I extracted 120 explicit predictions from 36 sessions. Before searching for outcomes, each claim received a frozen population, outcome, horizon, indicator, success threshold, contradiction threshold, and evidence rule. The resulting dataset, code, and row-level evidence are public.

The apparent result is memorable: 54 of 89 resolvable predictions met their thresholds, or 60.7%. But the rule 'label every prediction fulfilled' also scores 60.7%. Thirty-one additional claims are indeterminate. The headline therefore measures neither calibration nor forecasting skill.

Four extreme cases make the problem concrete. A forecast that cyber insurance would consume 25% to 33% of security budgets missed despite correctly anticipating market growth. AVX-512 reached real Intel hardware, but after the explicit deadline. A Dutch referendum occurred on the exact predicted date because it was already scheduled. A ten-year claim about commercial capacity to store all worldwide email could not be honestly resolved. These are not gotchas or a ranking of speakers; they expose different ways an apparently successful prediction can fail a decision maker.

Attendees will leave with a five-field test they can apply before a forecast affects strategy: population, measurable outcome, magnitude, deadline, and resolution source. They will also learn to compare a claim with a trivial baseline, preserve indeterminate outcomes, and distinguish a useful thematic radar from a decision-grade forecast. I will close by applying the method to decisions at one week, six weeks, and six months, so CISOs can improve how conference insights enter budget, policy, and risk discussions.

### Submitter comments — máximo 400 caracteres

This independent research is already public for reproducibility. Its limits are explicit: a documentary sample of three venues, clustered observations, 31 indeterminate cases, and one coder. The contribution is not a speaker ranking but a transparent method for turning influential conference claims into testable decision inputs.

### Profiling

- Format: Individual Speaker.
- Classification: Intermediate.
- Technical designation: No. The session is evidence- and method-heavy, but its primary outcome is a management decision tool rather than code, protocol analysis, or architecture.
- Track: Breaking Research & Emerging Cyber Trends.
- Alternate track: CISO Insights & Business Strategy.

## 5. Revisión que todavía requiere el autor

- Sustituir cualquier frase que no suene natural en su voz.
- Confirmar si quiere describir algunas decisiones observadas como “caprichosas”; para el CFP se recomienda “insufficiently tested” o “weakly evidenced”, que conserva la crítica sin antagonizar a la audiencia.
- Añadir una situación concreta, anonimizada, en la que una idea de conferencia entró en una conversación de presupuesto, producto o política.
- Completar biografía de hasta 800 caracteres y enlace de video.
- Declarar cualquier presentación del mismo contenido dentro de los 45 días antes o después de RSAC.

## 6. Estado tras esta tanda

La propuesta ya tiene motivación personal, evidencia, casos, utilidad ejecutiva y un borrador dentro de la estructura oficial. El principal faltante narrativo es una anécdota anonimizada que muestre cómo una afirmación de conferencia llegó a una decisión real. El principal faltante operativo es el video corto en inglés.
