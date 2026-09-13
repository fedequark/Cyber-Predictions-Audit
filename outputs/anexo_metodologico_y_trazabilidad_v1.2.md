# Anexo metodológico y de trazabilidad v1.2

Este anexo complementa v1.1 con la capa derivada reproducible. No modifica los CSV congelados.

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

## G. Publicación pendiente

El paquete v1.2 está listo para versionado técnico. La publicación académica definitiva requiere dos decisiones del autor que no deben inferirse: licencia del repositorio/datos y depósito público con DOI. El estado privado del repositorio también debe cambiarse explícitamente si se desea acceso público al código.
