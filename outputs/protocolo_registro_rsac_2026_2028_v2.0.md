# Protocolo del registro RSAC 2026–2028

**Versión 2.0 — congelación pre-adjudicación del 18 de septiembre de 2026.**

**Estado:** extensión separada del corpus histórico de 120 casos.

## 1. Propósito

Aplicar prospectivamente el método de auditabilidad a las predicciones que RSAC publicó en *RSAC’s Predictions: What CISOs Should Expect, 2026–2028*. El registro permite mostrar en RSAC 2027 cómo transformar pronósticos institucionales vivos en pruebas reproducibles.

No se sumará ninguna fila a los 120 casos históricos ni se utilizará para recalcular el 60,7%. Esta extensión tiene fuente, unidad, periodo y mecanismo de selección propios.

## 2. Calificación temporal honesta

Este no es un preregistro anterior a la publicación de las predicciones ni al inicio de 2026. Es un **registro pre-adjudicación** realizado el 18 de septiembre de 2026:

- algunas afirmaciones de 2026 ya estaban en curso y una —DORA antes de abril de 2026— ya había vencido;
- no se buscó evidencia de desenlace para puntuar las filas durante esta congelación;
- el conocimiento contemporáneo del investigador no puede considerarse ciego al periodo;
- las afirmaciones con vencimiento 2027–2028 constituyen el componente temporalmente más fuerte.

El caso DORA se conserva como `expired_at_freeze` y nunca se presentará como prueba prospectiva.

## 3. Fuente y marco

**Fuente oficial única:** *RSAC Cybersecurity Insights & Futures, Volume 2: RSAC’s Predictions: What CISOs Should Expect, 2026–2028*.

URL: https://www.rsaconference.com/-/media/project/rsac/rsac-website/reports/rsaccybersecurityinsightsfuturesvol2--complete.pdf?rev=b4b49398cd6b48cba00498c4cffcdfec

Fecha de recuperación para el registro: 18 de septiembre de 2026. La URL contiene un identificador de revisión, pero el servidor rechazó la descarga automatizada usada para calcular un SHA-256 local. No se afirma preservación del PDF. El texto y las páginas se registran como localizadores verificables.

El marco es exhaustivo respecto de las proposiciones explícitas y cuantificables o fechables identificadas en las páginas 3–7 del informe. Las recomendaciones de la página 8 no son desenlaces adicionales: son acciones derivadas de las predicciones.

## 4. Unidad y atomización

Una fila contiene una combinación única de población, resultado, magnitud y vencimiento. Las frases compuestas se separan cuando pueden tener desenlaces distintos. Los comentarios causales —por ejemplo, que ransomware impulsa primas— no se puntúan como predicción independiente salvo que el informe les asigne un resultado observable y una fecha.

## 5. Reglas de evaluación

- Categorías: `fulfilled`, `not_fulfilled`, `indeterminate` y `mixed` sólo para umbrales genuinamente inseparables.
- El vencimiento anual por defecto es el 31 de diciembre del año indicado.
- Para cifras internas de RSAC se priorizará una publicación oficial de RSAC con numerador, denominador y taxonomía comparables.
- Si RSAC cambia categorías o no publica el denominador, la fila será `indeterminate`; no se sustituirá con volumen de prensa.
- Para primas se requiere una serie que compare cobertura equivalente y metodología estable. Un promedio de precios sin equivalencia de cobertura no alcanza.
- Para DORA se requiere una actuación oficial de un regulador competente, no una advertencia, investigación o comentario jurídico.
- Las afirmaciones de “más de la mitad” y porcentajes exactos se puntúan por su propio umbral, no por la mera presencia del tema.
- No se consultarán desenlaces de 2027 o 2028 antes de su vencimiento salvo para registrar cambios de fuente sin adjudicar.

## 6. Análisis previsto

El análisis primario será descriptivo fila por fila. No se calculará una tasa agregada si menos de ocho filas son resolubles o si más de la mitad depende de métricas internas de RSAC no publicadas. Si se calcula, se mostrarán simultáneamente:

- cumplidas / resolubles;
- extremos tratando todos los indeterminados como fallos o aciertos;
- resultado frente al baseline “todo se cumple”;
- separación entre predicciones cuantitativas externas, métricas internas de RSAC y afirmaciones laborales cualitativas.

No habrá ranking de personas ni comparación causal con Black Hat, CCC o Virus Bulletin.

## 7. Riesgos previstos

1. RSAC controla varias métricas de resolución: propuestas, asistencia e Innovation Sandbox.
2. Las taxonomías internas pueden cambiar entre años.
3. Algunas cifras del informe son proyecciones de series ya modeladas, no apuestas independientes.
4. La congelación ocurre durante 2026 y no elimina conocimiento contemporáneo.
5. Las afirmaciones laborales sobre salidas “costosas” carecen de población y umbral suficientes; pueden permanecer indeterminadas.
6. La misma organización formula, mide y puede publicar algunos desenlaces; se requiere declarar ese conflicto de procedencia.

## 8. Gate para RSAC 2027

Antes de usar resultados nuevos en la charla:

1. cerrar el 31 de diciembre de 2026;
2. realizar una adjudicación independiente de las filas 2026;
3. conservar toda ausencia de datos como `indeterminate`;
4. publicar fuentes y notas antes de actualizar slides;
5. describir 2027–2028 únicamente como registro vivo, no como resultados.

## 9. Estado después de esta tanda

Queda congelado un puente prospectivo directamente conectado con RSAC. Es más valioso para la aceptación que añadir retrospectivamente casos favorables: demuestra que el método puede aplicarse antes de conocer el resultado y produce un compromiso público verificable.

El próximo paso metodológico es conseguir una copia preservable del informe, validar la atomización con un segundo codificador y fijar qué publicaciones oficiales de RSAC resolverán sus métricas internas.
