# Plan de validación independiente v1.1

## Objetivo

Completar la verificación prevista en el preregistro sin exponer al segundo codificador a los juicios originales.

## Paquetes

`python scripts/generar_paquete_doble_codificacion.py` genera en `work/doble_codificacion/`:

- `desenlaces_muestra_ciega_v1.1.csv`: muestra determinista de 30/120 predicciones. Contiene texto y reglas congeladas, pero no el juicio ni las fuentes usadas por el primer codificador.
- `atomizaciones_clase_b_ciega_v1.1.csv`: las 115 operacionalizaciones clase B para evaluar fidelidad semántica de forma conservadora.
- `MANIFIESTO.md`: semilla, regla de selección y hashes de entrada.

## Instrucciones para el segundo codificador

1. No consultar `evaluacion_desenlaces_v1.0.csv` hasta entregar la hoja.
2. Para cada desenlace, buscar evidencia de forma independiente y completar `independent_judgment`, URLs, resumen y aplicación del umbral.
3. Usar únicamente `fulfilled`, `not_fulfilled`, `indeterminate` o `mixed`.
4. Para cada atomización clase B, completar `semantic_fidelity` con `yes`, `no` o `uncertain`, añadir una reformulación alternativa cuando corresponda y justificarla.
5. Registrar nombre o identificador del codificador y fecha de evaluación.

## Cálculo

Después de recibir la hoja completa:

```text
python scripts/calcular_acuerdo.py work/doble_codificacion/desenlaces_muestra_ciega_v1.1.csv
```

El programa informa acuerdo bruto, κ de Cohen y matriz de confusión. Las discrepancias deben adjudicarse después de congelar y conservar ambos juicios originales.

## Inclusión/exclusión

El paquete actual contiene sólo predicciones incluidas. Para calcular el acuerdo preregistrado de inclusión/exclusión se necesita el registro de candidatos, incluidos los descartados y su localización en la fuente. Hasta recuperarlo, este componente debe declararse no estimable; no debe sustituirse por una segunda lectura que conozca qué frases fueron seleccionadas.

## Independencia

La autoría original y sistemas de IA que hayan participado en la primera codificación no cuentan como segundo codificador independiente. La revisión debe realizarla otra persona competente, idealmente con conocimiento de ciberseguridad y de al menos los idiomas relevantes.
