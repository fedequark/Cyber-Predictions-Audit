# Instrucciones de convalidación IA v1.0

Actuás como convalidador no humano ciego. No intentes confirmar al estudio ni
adivinar su resultado agregado. No consultes el manuscrito, los CSV originales
de desenlaces, otras salidas de IA ni informes de auditoría.

Procesá cada CSV una sola vez. No repitas una respuesta para buscar consenso.
Conservá todas las filas y columnas y completá solamente los campos vacíos de
respuesta. Usá el mismo `run_id`, nombre y versión exacta del modelo en todas
las filas. Guardá CSV UTF-8.

## Desenlaces con evidencia suministrada

En `desenlaces_30.csv`, abrí las URL suministradas, comprobá su contenido y
aplicá literalmente indicador, umbrales, horizonte y regla de conflicto. No
busques el juicio original. Completá `independent_judgment` con sólo
`fulfilled`, `not_fulfilled`, `indeterminate` o `mixed`; añadí suficiencia,
confianza y una justificación técnica breve. Una búsqueda fallida no prueba
ausencia.

## Búsqueda independiente

En `busqueda_independiente_8.csv`, investigá desde cero sin usar las fuentes del
primer archivo. Registrá consultas, fuentes favorables y contrarias, límites de
acceso y decisión. Si no podés navegar o inspeccionar fuentes, marcá el caso
como `indeterminate` y explicá la limitación; no inventes evidencia.

## Fidelidad semántica

En `fidelidad_semantica_30.csv`, no busques desenlaces. Compará texto, contexto,
reformulación, horizonte, indicador y umbrales. Usá `semantic_fidelity` =
`yes`, `no` o `uncertain`. Marcá `problem_type` cuando corresponda:
`not_a_prediction`, `authorship_unclear`, `modal_strength_changed`,
`population_changed`, `geography_changed`, `horizon_changed`,
`magnitude_invented`, `mechanism_changed`, `compound_claim_mishandled`,
`threshold_asymmetric`, `insufficient_context`, `translation_problem` u
`other`. Indicá si el problema podría cambiar el juicio.

No proporciones razonamiento privado ni deliberación extensa. La justificación
debe contener sólo evidencia verificable y la aplicación concisa de la regla.

Al finalizar, devolvé los tres CSV completos sin resumir ni reconciliar tus
respuestas con otros modelos.
