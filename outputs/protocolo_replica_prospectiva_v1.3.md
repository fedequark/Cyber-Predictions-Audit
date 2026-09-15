# Protocolo para una réplica prospectiva

Este documento no afirma que la auditoría 2005–2018 haya seguido estas reglas. Es un diseño nuevo para superar límites detectados en la retrospectiva.

## 1. Registro antes del desenlace

Publicar con sello temporal externo el marco de sesiones, reglas de inclusión, denominador de candidatos, orden de extracción y regla de parada. Conservar por cada candidato incluido o excluido: localizador, cita breve o paráfrasis, motivo y fecha de decisión. La fila excluida no debe confundirse con una predicción fallida.

## 2. Tarjeta de pronóstico

Solicitar al ponente una proposición atómica, población, geografía, evento, magnitud o umbral, fecha límite, fuente de resolución y probabilidad entre 0 y 1. Separar escenario posible de pronóstico adoptado. No permitir cambiar umbral tras el desenlace; toda actualización de probabilidad debe quedar fechada como pronóstico nuevo o revisión explícita.

## 3. Línea base preregistrada

Para cada clase de evento, registrar antes del plazo al menos dos referencias:

- **Tasa histórica de referencia:** casos previos comparables con denominador, periodo y fuente.
- **Pronóstico ingenuo transparente:** extrapolación o persistencia definida antes de evaluar, con la misma fecha y población.

Si no existe clase de referencia defendible, marcar el baseline como no disponible. No construirlo a partir de los mismos desenlaces que se pretende explicar.

## 4. Puntuación

Usar Brier score por evento resuelto, `(probabilidad − desenlace_binario)^2`, junto con la diferencia frente a la línea base fijada sobre **los mismos eventos resolubles**. Informar por separado cobertura de resolución, eventos indeterminados, calibración descriptiva y precisión. No asignar retrospectivamente 0 o 1 a indeterminados para mejorar la puntuación. La simple proporción de afirmaciones cumplidas no es un *skill score*.

## 5. Fuentes y preservación

Antes del cierre de cada evento, registrar fuentes primarias admisibles, política de conflicto y copia archivada cuando sea legal. Guardar hash del recurso preservado y fecha de acceso. Las URL por sí solas no preservan el contenido.

## 6. Análisis y límites

Preregistrar unidad de análisis, tratamiento por sesión, subgrupos, horizonte temporal y sensibilidad para indeterminados. Publicar resultados positivos, negativos y no resolubles. Una comparación por venue requiere que la muestra y las clases de eventos sean comparables; de lo contrario, limitarla a descripción.

La revisión humana independiente sigue siendo una tarea separada y no se ejecuta en esta actualización.
