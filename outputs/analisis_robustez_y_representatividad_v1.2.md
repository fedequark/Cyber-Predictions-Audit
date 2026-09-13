# Análisis de robustez y representatividad v1.2

**Fecha:** 13 de septiembre de 2026
**Estado:** capa derivada post hoc. No modifica los registros congelados v1.0.

## 1. Incertidumbre y datos indeterminados

El estimando registrado se mantiene en **54/89 = 60,7%** entre casos resolubles, con IC Wilson descriptivo de 95% **50,3%–70,2%**. Los 31 casos indeterminados abren una banda extrema de **45,0%–70,8%**. Bastaría que 7 de los 31 indeterminados fueran cumplidos para que el resultado sobre los 120 casos superase 50%; por eso la indeterminación es parte central del resultado.

El remuestreo exploratorio por sesión (20.000 muestras, semilla `20260913`) produce un intervalo percentil de **47,0%–72,1%**. No es un intervalo poblacional: cuantifica fragilidad ante la composición de las 36 sesiones observadas.

## 2. Referencias base

No existe una línea base sustantiva reconstruible: las predicciones no traen probabilidades, alternativas mutuamente excluyentes ni una clase de referencia preregistrada. Se publican tres referencias para evitar confundirlas con *skill*:

| Referencia | Valor | Qué demuestra |
|---|---:|---|
| Moneda justa sobre los 89 resolubles | 50,0% | Referencia matemática; prueba binomial bilateral post hoc, p=0,056 |
| Sorteo que reproduce la prevalencia observada | 52,3% | Exactitud esperada de etiquetas aleatorias con la misma mezcla; no es un pronóstico histórico |
| “Siempre cumplida” sobre resolubles | 60,7% | Iguala el titular por construcción y muestra que la tasa sola no mide discriminación |

La conclusión correcta sigue siendo descriptiva. Una réplica prospectiva deberá registrar probabilidades y un baseline antes de observar desenlaces.

## 3. Representatividad y concentración

Las 120 predicciones provienen de 36 sesiones. El HHI por sesión es **0,044**, equivalente a sólo **22,5 sesiones de igual peso**. La familia *Security Nightmares* aporta 73/120 (60,8%).

| Estrato | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
| Security Nightmares | 73 | 33 | 17 | 23 | 66,0% |
| Resto | 47 | 21 | 18 | 8 | 53,8% |

Esto no representa “todas las keynotes”: el marco fue documental, tres venues no son la industria completa y una serie domina la muestra.

## 4. Especificidad y dificultad: proxies auditables

Para no recodificar retrospectivamente el texto como si hubiera sido preregistrado, v1.2 publica proxies mecánicos. La especificidad suma cuatro señales: clase A directamente puntuable, detalle numérico en el original, horizonte explícito y población+geografía declaradas. La dificultad usa una tabla fija por `prediction_type`: ocurrencia/saliencia/capacidad como baja; dirección/adopción/no-ocurrencia como media; conteo/tendencia/prevalencia/proporción/mecanismo compuesto como alta. Son análisis exploratorios, no mediciones validadas.

| Especificidad proxy | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
| Baja | 59 | 22 | 17 | 20 | 56,4% |
| Media | 58 | 31 | 16 | 11 | 66,0% |
| Alta | 3 | 1 | 2 | 0 | 33,3% |

| Dificultad proxy | n | Cumplidas | Incumplidas | Indeterminadas | % resoluble |
|---|---:|---:|---:|---:|---:|
| Baja | 55 | 33 | 12 | 10 | 73,3% |
| Media | 22 | 9 | 6 | 7 | 60,0% |
| Alta | 43 | 12 | 17 | 14 | 41,4% |

## 5. Modelo explicativo exploratorio

Se ajustó una regresión logística sobre los 89 casos resolubles, con errores sándwich agrupados por sesión. Los predictores fueron pertenencia a *Security Nightmares*, año, especificidad proxy y dificultad proxy; los tres últimos continuos se estandarizaron. Con 33 sesiones resolubles, el modelo es deliberadamente pequeño.

| Predictor | Odds ratio | IC 95% agrupado |
|---|---:|---:|
| Security Nightmares | 3,33 | 0,91–12,15 |
| Año (1 DE) | 1,92 | 1,09–3,38 |
| Especificidad proxy (1 DE) | 1,48 | 0,84–2,63 |
| Dificultad proxy (1 DE) | 0,47 | 0,27–0,81 |

Los coeficientes describen asociación condicional en este corpus. No identifican causalidad ni habilidad de ponentes; el proxy de especificidad incorpora clase A/B y el de dificultad fue definido después de conocer el corpus.

## 6. Flujo de selección reconstruible

| Etapa | n | Estado de evidencia |
|---|---:|---|
| Sesiones en el marco cerrado | 189 | Documentado en protocolo/manuscrito |
| Sesiones con disponibilidad S3 | 138 | Registro fila por fila |
| Sesiones sin S3 | 51 | Diferencia documentada; no hay registro de exclusión individual en este paquete |
| Sesiones S3 revisadas | 138 | Orden de selección publicado |
| Sesiones que aportaron predicciones | 36 | Derivable del corpus |
| Predicciones incluidas | 120 | Registro congelado |
| Candidatos textuales excluidos | n.d. | No se preservó un registro; no puede reconstruirse honestamente |

El archivo `work/registro_candidatos_excluidos_template_v1.2.csv` fija el esquema para una réplica, pero no rellena retrospectivamente candidatos inexistentes.

## 7. Preservación de evidencia

El inventario contiene 218 localizadores únicos: 36 fuentes de predicción, 94 fuentes primarias de desenlace y 88 secundarias. Cada entrada enlaza las claves afectadas y un SHA-256 de la cápsula textual ya preservada en los CSV. Esto protege identificación y texto auditado, no los bytes originales del recurso remoto. El archivado WARC/PDF/captura sigue pendiente de una operación externa y se marca explícitamente como tal.

## 8. Separación confirmatoria/exploratoria

| Componente | Estado |
|---|---|
| 54/35/31; 54/89; Wilson; extremos 45,0–70,8 | Confirmatorio según protocolo operativo |
| Sensibilidad sólo clase A | Prevista, potencia insuficiente |
| Análisis por sesión, concentración, proxies, referencias base y regresión | Exploratorio/post hoc |
| Doble codificación | Prevista y pendiente; fuera de v1.2 por decisión del autor |

## Artefactos reproducibles

- `work/analisis_derivado_v1.2.csv`: una fila por predicción con variables derivadas.
- `work/metricas_robustez_v1.2.csv`: estimaciones y estado analítico.
- `work/inventario_fuentes_v1.2.csv`: inventario de localizadores y cápsulas preservadas.
- `scripts/analizar_robustez_v1_2.py`: generación determinista de esta capa.
