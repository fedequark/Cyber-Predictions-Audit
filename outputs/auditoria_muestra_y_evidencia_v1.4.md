# Auditoría de evidencia y rendimiento documental v1.4

**Estado:** diagnóstico derivado de los registros congelados; no hay nuevas adjudicaciones.

## Evidencia que merece revisión

| Prioridad | Regla | Casos |
|---|---|---:|
| P0 | Incumplimiento sin URL probatoria | 1 |
| P1 | Indeterminado sin URL probatoria | 17 |
| P2 | Indeterminado con al menos una URL | 14 |
| P3 | Resuelto con evidencia débil y alguna URL | 0 |
| P4 | Resto; preservar localizadores | 88 |

La ausencia de URL en un registro **no prueba** ausencia de evidencia en el mundo. Tampoco convierte automáticamente un incumplimiento en indeterminado. Cada nueva fuente debe cumplir el tipo y el umbral fijados antes de buscar desenlaces. Cualquier impugnación o cambio se documentará como adenda fechada, nunca reescribiendo el juicio v1.0.

El caso P0 tiene una búsqueda inicial no exhaustiva documentada en `outputs/nota_revision_focal_caso_p0_v1.4.md`. No encontró fuente calificante, pero tampoco proporciona prueba de no ocurrencia; permanece el juicio congelado y la revisión completa está pendiente.

## Sesiones S3 y productividad del corpus

| Conferencia | S3 revisadas | Con al menos una predicción incluida | Predicciones incluidas |
|---|---:|---:|---:|
| Black Hat USA | 41 | 5 | 12 |
| CCC | 85 | 29 | 99 |
| Virus Bulletin | 12 | 2 | 9 |
| **Total** | **138** | **36** | **120** |

### Nueve celdas de conferencia y periodo

| Periodo | Conferencia | S3 | Aportantes | Predicciones |
|---|---|---:|---:|---:|
| 2005-2009 | Black Hat USA | 2 | 1 | 1 |
| 2005-2009 | CCC | 21 | 9 | 35 |
| 2005-2009 | Virus Bulletin | 1 | 0 | 0 |
| 2010-2014 | Black Hat USA | 16 | 2 | 9 |
| 2010-2014 | CCC | 27 | 10 | 34 |
| 2010-2014 | Virus Bulletin | 5 | 0 | 0 |
| 2015-2018 | Black Hat USA | 23 | 2 | 2 |
| 2015-2018 | CCC | 37 | 10 | 30 |
| 2015-2018 | Virus Bulletin | 6 | 2 | 9 |

Las 102 sesiones S3 restantes no aportaron **predicciones incluidas**. Eso no significa que no hablaran del futuro: no se publica un registro individual completo de candidatos excluidos que permita verificar esa interpretación.

### Correspondencia de identificador detectada

Siete predicciones de la sesión de orden 34 se registraron bajo `CCC-2013-034`, pero el orden S3 congelado la denomina `CCC-2013-043`. El número de orden y la URL oficial coinciden exactamente; el título es *Security Nightmares* (2013). La tabla derivada conserva ambos identificadores. No se cambia el CSV congelado ni el juicio de ninguna predicción. Un revisor debe confirmar externamente qué identificador fue el pretendido antes de corregir metadatos en una edición futura.

### URL alternativa oficial para un enlace roto

El URL literal `https://media.ccc.de/v/35c3-10030-security_nightmares_0x13` aparece como fuente de predicción en siete casos de `CCC-2018-085` y devolvió 404 en la foto HTTP. El orden S3 congelado ya consigna `https://media.ccc.de/v/35c3-9685-security_nightmares_0x13` como programa oficial de la misma sesión (*Security Nightmares 0x13*, 2018); esta URL devolvió 200 el 15 de septiembre de 2026. Se publica como alternativa en `work/alternativas_enlaces_fuentes_v1.4.csv`; el URL original permanece visible y el contenido del segmento no se ha preservado ni reauditable automáticamente.

## Brecha del marco original

El protocolo cerrado declara 189 sesiones: 138 S3 identificables en el archivo de orden y **51 no S3 sólo como agregado** (33 Black Hat USA y 18 Virus Bulletin). El repositorio no conserva la lista de identificadores, títulos y motivos de las 51. No se puede auditar su selección fila por fila ni calcular cobertura por periodo para el marco completo. Debe reconstruirse con metadatos oficiales antes de incorporar sesiones rescatadas.

## Archivos y próxima acción

- `work/triage_evidencia_v1.4.csv`: los 120 casos, prioridad mecánica y columnas vacías para una revisión futura; no contiene evidencia nueva.
- `work/rendimiento_sesiones_s3_v1.4.csv`: las 138 sesiones S3 del orden original y su aporte congelado.
- `work/reconstruccion_marco_no_s3_template_v1.4.csv`: estructura para recuperar los 51 registros ausentes, sin filas inventadas.
- `work/alternativas_enlaces_fuentes_v1.4.csv`: alternativa oficial de una URL de predicción rota, sin reemplazo silencioso.
- `outputs/protocolo_ampliacion_estratificada_v1.4.md`: diseño de una ampliación separada del corpus original.
