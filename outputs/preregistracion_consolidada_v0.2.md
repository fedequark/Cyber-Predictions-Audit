# Preregistración consolidada v0.2

## ¿Acertaron los escenarios del futuro cyber?

### Auditoría retrospectiva de predicciones explícitas en conferencias de ciberseguridad, 2005–2018

**Fecha de cierre del protocolo:** 7 de agosto de 2026  
**Fecha límite para resultados:** 6 de agosto de 2026  
**Estado:** protocolo consolidado previo a la extracción sistemática y a la búsqueda de resultados  
**Prioridad:** impacto mediático y profesional, aceptando menor representatividad y mayor heterogeneidad documental a cambio de una pregunta clara y comunicable.

## 1. Pregunta principal

¿Qué proporción de las predicciones públicas, explícitas, observables y con horizonte vencido formuladas en keynotes, plenarias y sesiones oficialmente prospectivas de grandes conferencias de ciberseguridad entre 2005 y 2018 se cumplió dentro del plazo anunciado?

La inferencia descriptiva se limita al corpus recuperado. No se afirmará que las sesiones representan todas las conferencias, toda la industria ni todos los pronósticos de cada ponente.

## 2. Universo fuente cerrado

El marco contiene 189 sesiones únicas:

| Venue | Sesiones | S3 | Otras |
|---|---:|---:|---:|
| Black Hat USA | 74 | 41 | 33 pendientes |
| Chaos Communication Congress | 85 | 85 | 0 |
| Virus Bulletin | 30 | 12 | 17 pendientes y 1 S1 |
| **Total** | **189** | **138** | **51** |

RSA Conference queda fuera del análisis principal porque no pudo reconstruirse un denominador histórico reproducible. El *Cryptographers’ Panel* de 2018 sólo podrá aparecer como sensibilidad explícitamente externa al marco principal.

Una sesión entra al universo cuando es keynote/plenaria o cuando sus metadatos oficiales contemporáneos activan la regla prospectiva congelada. No se incorporarán nuevas sesiones después de conocer su contenido o sus resultados.

## 3. Disponibilidad documental

- **S3:** grabación sustancialmente completa, transcripción completa, paper integral del ponente o diapositivas autosuficientes.
- **S2:** fuente primaria parcial o insuficiente para recuperar todos los compromisos predictivos.
- **S1:** sólo metadatos, abstract o recapitulación.
- **S0:** fuente no recuperada.

Sólo las 138 sesiones S3 pueden contribuir predicciones al análisis principal. Las demás permanecen en el denominador documental y se informarán como pérdida de fuente.

## 4. Orden de revisión congelado

Las sesiones S3 se separan en nueve celdas: tres venues por tres periodos (2005–2009, 2010–2014 y 2015–2018).

Dentro de cada celda se ordenan ascendentemente mediante:

`SHA-256("CYBERFUTURES-2026-08-07-v1|" + frame_id)`

Las celdas se recorren por rondas en este orden:

1. 2005–2009: Black Hat, CCC, Virus Bulletin;
2. 2010–2014: Black Hat, CCC, Virus Bulletin;
3. 2015–2018: Black Hat, CCC, Virus Bulletin.

El orden resultante contiene 138 sesiones y 37 rondas. Su archivo operativo es `work/orden_seleccion_s3_v0.2.csv`, con SHA-256 `1C3C93302C00416528409BE2B783935BD581B5E6E70F498C15D0D39F47995FB7`.

## 5. Unidad analítica

La unidad es una proposición predictiva atómica. Se conservarán el fragmento literal, marca temporal o página, contexto mínimo, hablante, reformulación atómica, fenómeno, población, resultado, horizonte literal y fecha límite.

Una oración con resultados separables se divide. Los componentes que sólo tengan sentido conjuntamente permanecen unidos. Reformulaciones repetidas del mismo compromiso dentro de una sesión se consolidan y se conservan sus distintas localizaciones.

## 6. Compromiso predictivo

Una afirmación debe comprometer al hablante con que un estado futuro ocurrirá o será más probable que su alternativa. No bastan:

- posibilidades, escenarios hipotéticos o listas de riesgos;
- preguntas, bromas o hipérboles;
- deseos, recomendaciones, objetivos o planes bajo control del hablante;
- advertencias condicionales cuyo antecedente no sea observable;
- descripciones del presente o del pasado;
- citas de terceros no adoptadas inequívocamente por el ponente.

La confianza puede ser probabilística, pero debe permitir una condición de error. “Podría suceder” queda fuera; “es más probable que suceda que que no suceda” puede entrar.

## 7. Autoría

Cada candidato se clasifica como:

- `propia`;
- `colectiva_panel`;
- `tercero`;
- `ambigua`.

Sólo `propia` y `colectiva_panel` pueden entrar al conjunto A+B. Una proyección de un tercero mostrada como contexto no se atribuye al ponente salvo adopción explícita. En paneles, una afirmación sólo se asignará colectivamente cuando exista asentimiento inequívoco; de lo contrario se asignará al hablante identificable.

## 8. Horizonte

Se aceptan únicamente:

1. **individual:** fecha, plazo o intervalo contenido en la afirmación;
2. **heredado:** la moderación, introducción o encabezado fija inequívocamente un límite para el bloque y no se ha anunciado un cambio de horizonte.

El plazo se calcula desde la fecha de la sesión salvo que el hablante indique otro punto de partida. Para “en N años”, la fecha límite será el mismo día y mes N años después; para “para 20XX”, el 31 de diciembre de ese año; para “durante la próxima década”, diez años después de la sesión.

“Pronto”, “algún día”, “en el futuro”, “eventualmente”, “en los próximos años” y equivalentes sin límite superior se registran como horizonte abierto y no cuentan. No se inventará un horizonte usando conocimiento posterior. Sólo entran predicciones cuya fecha límite sea igual o anterior al 6 de agosto de 2026.

## 9. Clases congeladas antes de buscar resultados

### Clase A — directamente puntuable

Predicción de acontecimiento, estado o cantidad con indicador y umbral naturales o expresos.

### Clase B — direccional puntuable

Predicción de aumento, descenso, predominio o sustitución para la cual pueden fijarse, sin consultar el resultado, población, línea base, serie o indicador y regla de decisión.

### Clase C — no puntuable

Lenguaje prospectivo que carece de compromiso, observabilidad, horizonte válido, autoría admisible o condición de error. Se conserva con motivo de exclusión, pero no cuenta para la parada ni para la tasa principal.

## 10. Ficha ex ante obligatoria

Antes de cualquier búsqueda de resultados se congelarán para cada unidad A o B:

- cita y reformulación atómica;
- autoría;
- población, ámbito geográfico y unidad;
- horizonte literal y fecha límite;
- tipo de predicción;
- indicador o acontecimiento observable;
- fuente de resultados admisible por tipo, no por conclusión;
- umbral de cumplimiento y de contradicción;
- tratamiento de datos faltantes o conflictivos.

Las decisiones se incorporarán a una tabla bloqueada con fecha y hash. Hasta ese bloqueo, `outcome_search_allowed` permanecerá en `no`.

## 11. Regla de parada

Las sesiones se codifican completas siguiendo el orden congelado y se retienen aunque produzcan cero unidades.

- No se detiene antes de alcanzar 100 predicciones A+B.
- Se termina la sesión que alcanza o supera 100.
- Si el total queda entre 100 y 120, se detiene.
- Si supera 120, se conservan las primeras 120 según su orden de aparición en la fuente; las restantes se registran como `overflow_terminal_session`.
- Si se agotan las 138 sesiones con 80–99 unidades, se publican todas y se declara que no se alcanzó el objetivo central.
- Si se agotan con menos de 80, el trabajo se presenta como estudio de viabilidad o de falsabilidad, no como la estimación principal planificada.

No habrá reemplazo de sesiones improductivas, cuota posterior por venue ni máximo posterior por ponente.

## 12. Concentración y dependencia

No se eliminan predicciones válidas para equilibrar el corpus. Se vigilarán como señales de fragilidad:

- más de 15% de unidades procedentes de una sesión;
- más de 20% procedentes de un ponente o serie recurrente.

Si se supera una señal al alcanzar 100, continuará la extracción en el orden fijado hasta diluirla o llegar a 120. Si persiste, se informará y se aplicarán análisis agrupados y sensibilidades excluyendo la fuente dominante.

## 13. Evaluación posterior

Después del bloqueo, cada predicción recibirá una categoría:

- cumplida dentro del plazo;
- parcialmente cumplida dentro del plazo;
- cumplida fuera del plazo;
- no cumplida al cierre;
- contradicha;
- indeterminable.

La tasa principal será:

`cumplidas dentro del plazo / predicciones determinables`

“Indeterminable” no se contará como fracaso. Los parciales y tardíos se mostrarán separadamente y se recodificarán en análisis de sensibilidad.

Para valores puntuales sin tolerancia natural, el error porcentual absoluto será `|observado − predicho| / |predicho|`: cumplimiento hasta 10%, parcial por encima de 10% y hasta 25%, y no cumplimiento por encima de 25%. Se informarán sensibilidades 5%/20% y 15%/30%.

## 14. Jerarquía de evidencia

1. estadísticas oficiales o regulatorias;
2. repositorios técnicos primarios;
3. estudios revisados por pares;
4. informes con método y datos transparentes;
5. informes empresariales;
6. prensa reputada para acontecimientos discretos.

Una predicción comercial no se evaluará únicamente con datos de la organización del ponente. Conflictos entre fuentes se resolverán mediante una regla escrita antes de asignar el resultado; si no pueden resolverse, la unidad será indeterminable.

## 15. Análisis

- proporciones e intervalos binomiales;
- distribución completa de resultados;
- tablas por clase, tipo, horizonte, tema, especificidad, venue y rol;
- sensibilidad excluyendo Clase B;
- sensibilidad tratando parciales como éxito y como fracaso;
- sensibilidad excluyendo fuentes dominantes;
- errores estándar o remuestreo agrupado por sesión;
- modelos parsimoniosos sólo si el número efectivo de eventos lo permite.

No se publicará un ranking de personas salvo que cada persona comparada tenga al menos cinco predicciones determinables y se muestren intervalos de incertidumbre.

## 16. Fiabilidad y lenguas

- doble codificación de al menos 25% de inclusiones/exclusiones;
- doble codificación de todas las atomizaciones complejas;
- doble evaluación de al menos 25% de resultados;
- objetivo κ/α ≥0,80 para inclusión;
- referencia exploratoria ≥0,67 para resultado, seguida de adjudicación.

Las transcripciones automáticas sólo ayudan a localizar. Toda cita decisiva se verifica contra audio, vídeo, paper o diapositiva. Para material no dominado por los codificadores se conserva original y traducción, y la decisión exige verificación humana competente.

## 17. Transparencia sobre descarte

Se publicarán sesiones examinadas, horas revisadas, sesiones con cero unidades, candidatos C, horizontes abiertos, atribuciones a terceros y motivos de exclusión. Esto permitirá estimar qué parte del discurso presentado como “futuro” admite realmente condiciones verificables de error.

## 18. Cambios respecto del borrador v0.1

Esta versión sustituye íntegramente al borrador v0.1. Los cambios se tomaron antes de evaluar resultados:

- RSAC sale del universo principal;
- el universo se fija en 189 sesiones y sólo S3 permite extracción;
- el orden cronológico se sustituye por el orden estratificado con hash;
- el sorteo terminal se sustituye por orden de aparición;
- desaparecen los máximos rígidos por sesión o ponente;
- no se aceptan horizontes vagos inferidos;
- se explicitan autoría, pérdida documental y regla de concentración.

Los materiales del piloto deberán recodificarse si aparecen en el orden definitivo. Sus decisiones previas no se trasladan automáticamente y no modifican la secuencia.
