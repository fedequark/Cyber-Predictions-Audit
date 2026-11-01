# Congelación del corpus outcome-blind

**Fecha:** 8 de agosto de 2026  
**Versión:** 1.0

## Resultado

Se completó el recorrido íntegro de las 138 sesiones del orden S3 preregistrado. Tras resolver las dos verificaciones lingüísticas retenidas, el corpus contiene exactamente **120 predicciones con horizonte vencido**: **5 de clase A** y **115 de clase B**. No quedan sesiones abiertas y no se consultaron desenlaces durante la extracción.

La regla de parada se satisface en el límite superior preregistrado. La señal de concentración no se diluyó: la serie *Security Nightmares* aporta 73/120 predicciones (60,8%). Se continuó hasta 120 conforme a la regla prevista; no se alteraron criterios ni se sustituyeron observaciones para corregir esa concentración. La mayor contribución de una sola sesión es 9/120 (7,5%), inferior al umbral de 15% por sesión.

## Artefacto inmutable de referencia

- Registro congelado: `work/registro_extraccion_congelado_v1.0.csv`
- SHA-256: `323739E747379873D5786DB7057E7357EED0F70F0E6425AE6A3339B96AEDA32B`
- Orden S3 SHA-256: `1C3C93302C00416528409BE2B783935BD581B5E6E70F498C15D0D39F47995FB7`
- Estado de sesiones SHA-256: `2AC4C2A864F14EFC17C9BFF89B32CCB710A123900624F483D4AA7686474B3FD2`

Las reglas de indicador, éxito, contradicción, fuentes admisibles y conflicto quedaron fijadas por fila antes de habilitar la fase de desenlaces. El campo `outcome_search_allowed=no` conserva el estado histórico de cada codificación; desde esta congelación, la búsqueda de desenlaces queda habilitada sobre una tabla separada, sin modificar el registro congelado.

## Riesgo metodológico declarado

La fuerte concentración en una serie recurrente limita la generalización a «las keynotes de ciberseguridad» en conjunto. Es, no obstante, un resultado mecánico del muestreo y de la productividad predictiva de las sesiones, no una selección posterior basada en aciertos. El análisis principal deberá informar resultados globales y análisis de sensibilidad excluyendo *Security Nightmares*.
