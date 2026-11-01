# Anexo metodológico y de trazabilidad v1.3

Este anexo complementa v1.1 y v1.2 con capas derivadas reproducibles. No modifica los CSV congelados.

## A. Estado de análisis

| Resultado | Estado | Archivo de respaldo |
|---|---|---|
| 54/35/31 y 54/89 | Confirmatorio | `evaluacion_desenlaces_v1.0.csv` |
| Wilson y extremos 45,0–70,8 | Confirmatorio/sensibilidad prevista | `metricas_robustez_v1.2.csv` |
| Bootstrap por sesión | Exploratorio | script v1.2, semilla `20260913` |
| Concentración HHI | Exploratorio | `analisis_derivado_v1.2.csv` |
| Proxies y regresión | Exploratorio | codebook, CSV derivado y script |

## B. Correspondencia de identificador

`CCC-2013-034` en siete filas del corpus corresponde a `CCC-2013-043` en el marco: mismo orden 34, título, URL y ponentes. Los CSV canónicos no se alteran; el script normaliza sólo cruces derivados.

## C. Flujo verificable

| Etapa | n |
|---|---:|
| Marco cerrado | 189 sesiones |
| Disponibilidad S3 | 138 sesiones |
| Sin S3 | 51 sesiones |
| S3 revisadas | 138 sesiones |
| Sesiones aportantes | 36 sesiones |
| Predicciones congeladas | 120 |
| Candidatos textuales excluidos | n.d. |

El template de exclusiones v1.2 es prospectivo. No se imputan candidatos retrospectivamente.

## D. Variables derivadas

`analisis_derivado_v1.2.csv` incluye ID normalizado, venue, título y año de sesión, pertenencia a *Security Nightmares*, resolución, binario de cumplimiento, clase, tipo, fuerza de evidencia, horizonte cuando es fecha ISO, proxies y localizadores.

Los campos originales siguen teniendo autoridad. Las variables derivadas pueden regenerarse con:

```text
python scripts/analizar_robustez_v1_2.py
```

## E. Control de modelo

La regresión usa 89 casos resolubles y 33 conglomerados. Matriz: intercepto, indicador *Security Nightmares*, año estandarizado, especificidad estandarizada y dificultad estandarizada. La covarianza es sándwich agrupada con corrección finita. No se seleccionaron variables por significación ni se ajustaron comparaciones múltiples.

## F. Preservación

El inventario registra 218 combinaciones rol–URL: 36 fuentes de predicción, 94 primarias de desenlace y 88 secundarias. El hash corresponde a la cápsula textual conservada, no al contenido remoto. `archive_status=pending_external_archive` evita presentar un enlace como copia preservada.

## G. Diagnósticos adicionales v1.3

- Eliminación de cada una de las 36 sesiones: tasa resoluble residual 58,5–63,5%; tabla completa en `influencia_sesiones_v1.3.csv`.
- Indeterminación por dificultad proxy: 18,2% baja, 31,8% media y 32,6% alta. Son asociaciones descriptivas post hoc.
- Sensibilidad de un fallo débil: `39-CCC-2006-011-06` como indeterminado produciría 54/88 = 61,4%, sin alterar el juicio congelado.
- Escenarios parciales `(54+u)/120` para `u` entre 0 y 31; no se imputan resultados.
- Protocolo de réplica prospectiva: probabilidades, baseline externo preregistrado y registro de candidatos.

## H. Derechos y publicación

El paquete v1.3 aplica MIT al software y CC BY 4.0 sólo a aportes originales de investigación/datos; el material literal de terceros queda excluido conforme a `RIGHTS.md`. El repositorio GitHub se publica para reproducibilidad. La publicación académica definitiva aún requiere depósito inmutable con DOI y declaraciones editoriales de financiación, conflictos y ética.
