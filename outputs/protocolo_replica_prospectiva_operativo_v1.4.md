# Réplica prospectiva: protocolo operativo v1.4

**Estado:** instrumento y algoritmo preparados; **cero pronósticos recogidos, cero desenlaces puntuados y ningún registro externo aún**. Este documento no convierte retrospectivamente el corpus 2005–2018 en una prueba de habilidad.

## 1. Momento de registro

Antes de recoger nuevas afirmaciones, fijar y registrar públicamente el marco de sesiones, periodo de inclusión, máximo por conferencia, lista de fuentes, reglas de exclusión y análisis. OSF define una preregistración como un plan público, fechado y de solo lectura antes de recoger o analizar datos. Un documento en GitHub es trazable por commit, pero no se describirá como registro OSF hasta completarlo allí.

## 2. Tarjeta obligatoria

Una fila por evento binario en `work/tarjeta_pronostico_prospectivo_template_v1.4.csv`: frase atribuida, URL y localizador original, fecha de emisión, proposición atómica, población, geografía, umbral observable, fecha límite, fuente admisible de resolución y **probabilidad original del ponente** entre 0 y 1. Si el ponente no declara probabilidad, registrar el pronóstico cualitativo en otro conjunto; no convertir retrospectivamente «probable» en 0,7. No puntuar posibilidades no adoptadas, deseos o planes controlados por el hablante.

La tarjeta debe quedar cerrada antes del desenlace. Una revisión posterior será un evento nuevo, con vínculo al original y fecha propia, nunca una edición silenciosa. No registrar resultados finales en la plantilla hasta que venza el horizonte y exista evidencia admisible.

## 3. Línea base externa

Elegir antes del resultado una clase de referencia y una probabilidad base sustentada en eventos históricos comparables con denominador y periodo publicados. La referencia no se construirá con los mismos resultados que se evalúan. Cuando no exista referencia defendible, el campo base queda vacío y se informa Brier bruto sin *skill score*. Una política «siempre sí» puede informarse separadamente como contraste trivial, no como probabilidad atribuida al ponente.

## 4. Puntuación y cobertura

Para cada caso resuelto `y∈{0,1}`, Brier individual = `(p−y)^2`; menor es mejor. Comparar pronóstico y baseline **sobre exactamente los mismos eventos**, no sobre subconjuntos distintos. Informar número de tarjetas, eventos vencidos, resolubles e indeterminados, y Brier medio. El *skill score* relativo, si la base existe y su Brier es mayor que cero, es `1 − Brier_pronóstico / Brier_base`. Informar la incertidumbre por sesión y calibración descriptiva sólo con volumen suficiente; no crear bins de calibración con cinco observaciones ni imputar indeterminados.

## 5. Validaciones automáticas y revisión humana

`scripts/puntuar_replica_prospectiva_v1_4.py` verifica probabilidades, fechas y presencia de fuente probatoria antes de calcular. Rechaza una tarjeta cerrada después de la resolución, un resultado antes de la fecha límite o un resultado binario sin URL. Es un control de datos, no una certificación de que la fuente respalda el umbral. Un revisor humano debe comprobar atribución, evento, independencia de baseline y aplicación de la fuente.

## 6. Separación de resultados

Esta réplica tendrá nueva tabla de pronósticos y release propio. No se añadirá al denominador de 120 del estudio retrospectivo. Los casos con probabilidad no declarada podrán servir para análisis descriptivo de auditabilidad, pero no para Brier. La doble codificación independiente de la cohorte retrospectiva sigue pospuesta por decisión del proyecto.

## 7. Estado pendiente

Faltan un marco prospectivo cerrado, un registro externo previo a la extracción, autorización o acceso a las fuentes completas, probabilidad original en cada pronóstico y desenlaces futuros. Por eso v1.4 prepara el flujo sin publicar una puntuación ficticia.
