# Resultados de la auditoría retrospectiva

**Fecha de cierre:** 8 de agosto de 2026  
**Corpus congelado:** 120 predicciones, 36 sesiones, 2005–2018  
**Unidad:** predicción atómica con horizonte vencido y umbral fijado antes de consultar el desenlace

## Resultado principal

| Juicio | n | % del corpus |
|---|---:|---:|
| Cumplida | 54 | 45,0% |
| Incumplida | 35 | 29,2% |
| Indeterminada | 31 | 25,8% |
| Total | 120 | 100,0% |

Entre las 89 predicciones con juicio binario, la tasa de acierto es **60,7%** (54/89; IC Wilson 95%: **50,3–70,2%**). Este cociente es descriptivo: las observaciones están agrupadas por charla y serie, por lo que el intervalo binomial no debe interpretarse como inferencia a una población aleatoria de keynotes.

## Sensibilidad a los indeterminados

- Escenario conservador, todos como fallo: **45,0%** (54/120).
- Análisis principal, exclusión del denominador: **60,7%** (54/89).
- Escenario optimista, todos como acierto: **70,8%** (85/120).

La amplitud de 25,8 puntos porcentuales es un resultado sustantivo: una cuarta parte de las afirmaciones no dejó un rastro histórico capaz de satisfacer sus propios umbrales.

## Concentración en *Security Nightmares*

| Estrato | n | Cumplidas | Incumplidas | Indeterminadas | Acierto entre resolubles |
|---|---:|---:|---:|---:|---:|
| *Security Nightmares* | 73 | 33 | 17 | 23 | 66,0% |
| Resto del corpus | 47 | 21 | 18 | 8 | 53,8% |

Excluir la serie dominante reduce la tasa resoluble en 12,2 puntos. Esto confirma que el resultado global depende de la composición del corpus, aunque fuera de la serie todavía existe una mayoría modesta de aciertos entre casos resolubles.

## Forma de la predicción

Las categorías con al menos tres observaciones muestran una separación útil:

| Tipo | n | Acierto entre resolubles | Indeterminadas |
|---|---:|---:|---:|
| Ocurrencia | 45 | 65,7% | 10 |
| Conteo | 24 | 56,3% | 8 |
| Tendencia | 7 | 0,0% | 5 |
| Prevalencia | 4 | 25,0% | 0 |
| Maduración de capacidad | 4 | 100,0% | 0 |
| Dirección | 7 | 66,7% | 4 |
| Saliencia | 3 | 100,0% | 0 |
| Categórica | 3 | 100,0% | 0 |

Los grupos pequeños no permiten rankings estables. Sí respaldan una lectura: prever que «algo ocurrirá» resultó más fácil que acertar cuánto, cuán común o si crecería respecto del año anterior.

## Fuerza probatoria

| Evidencia | n | Cumplidas | Incumplidas | Indeterminadas |
|---|---:|---:|---:|---:|
| Fuerte | 57 | 43 | 14 | 0 |
| Moderada | 43 | 11 | 20 | 12 |
| Débil | 20 | 0 | 1 | 19 |

Esta tabla no mide la calidad intrínseca de las predicciones. La fuerza se asignó después de buscar evidencia y, por diseño, se relaciona con la determinabilidad. Sirve para mostrar dónde descansa la conclusión: los aciertos suelen dejar artefactos positivos claros; las ausencias y tendencias históricas son más difíciles de probar.

## Ejemplos comunicables

**Aciertos claros:** gusanos móviles en 2006; filtración recurrente de grandes datasets en 2010; troyanos estatales alemanes en 2011; teléfonos como credenciales físicas y activación vocal continua en 2012; ciberseguridad de dispositivos médicos en 2013; vehículos V2V de producción en 2015; nuevas técnicas Rowhammer y guerra pública por el cifrado en 2016; cambio metodológico del escaneo IPv6 en 2017; operación extranjera contra la elección estadounidense de 2020; arquitectura china de crédito social fragmentada, sin puntuación ciudadana universal.

**Fallos claros:** eCall mayoritario en automóviles europeos para 2016; mayoría de lectores de huella móviles comparando en la nube en 2014; deterioro de neutralidad de red dentro de 2016; predominio de reconocimiento facial seguro equivalente a Face ID en 2019; sistema chino obligatorio con puntuación nacional para toda la población en 2020; seguro cibernético absorbiendo 25–33,3% del presupuesto de ciberseguridad en 2025.

**Indeterminados reveladores:** recuentos anuales de controversias de privacidad; crecimiento de endpoints IPv6 directamente alcanzables excluyendo servidores; taxonomía histórica propietaria de un analista; proporción de dispositivos eléctricos con procesador; vínculo causal entre temas de Black Hat y creación de startups.

## Integridad

- Registro de extracción: `work/registro_extraccion_congelado_v1.0.csv`
- SHA-256 congelado: `323739E747379873D5786DB7057E7357EED0F70F0E6425AE6A3339B96AEDA32B`
- Registro de desenlaces: `work/evaluacion_desenlaces_v1.0.csv`
- SHA-256 del registro de desenlaces: `B3CE8AD49F6555870FCF415488506717BD8D7E71F4B955ED03514F7CE9E26F1B`
- Claves presentes: 120/120
- Duplicados: 0
- Juicios inválidos: 0
- Inconsistencias juicio/binario: 0
