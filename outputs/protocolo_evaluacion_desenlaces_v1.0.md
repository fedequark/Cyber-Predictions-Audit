# Protocolo operativo de evaluación de desenlaces

Este documento gobierna la fase posterior a la congelación del corpus del 8 de agosto de 2026.

## Unidad y categorías

Cada fila del registro congelado se evalúa una sola vez como `fulfilled`, `not_fulfilled`, `indeterminate` o `mixed`. `mixed` se reserva para predicciones con umbral compuesto cuyos componentes verificables apuntan en direcciones opuestas; en el análisis binario principal cuenta como no acierto. `indeterminate` se excluye del denominador binario principal y se incorpora como no acierto en el análisis conservador.

## Jerarquía de evidencia

Se priorizan registros oficiales, legislación, documentación de fabricantes, artículos científicos y análisis técnicos primarios. Los informes contemporáneos de organizaciones especializadas se admiten cuando el indicador congelado así lo permite. Las noticias sirven para localizar o corroborar evidencia, pero no sustituyen una fuente primaria disponible.

## Aplicación ciega a la redacción

El juicio debe responder literalmente al indicador, umbral de éxito, umbral de contradicción y regla de ausencia o conflicto congelados. No se rebaja el umbral por plausibilidad narrativa. Una predicción puede ser intuitivamente correcta y quedar indeterminada si la evidencia no cubre la población o magnitud exigida.

## Trazabilidad

La clave es `selection_order-session_id-candidate_order`. Cada decisión conserva URL, periodo probatorio, síntesis factual, aplicación del umbral y tratamiento de conflicto o ausencia. El registro de extracción congelado no se modifica.
