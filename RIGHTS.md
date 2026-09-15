# Alcance de derechos y material de terceros

El repositorio combina software, investigación original, metadatos públicos y
citas de otras personas. La publicación de un archivo no implica que todo su
contenido tenga la misma licencia.

| Material | Licencia de los aportes propios | Excepciones |
|---|---|---|
| `scripts/`, código JS/CSS/HTML de `site/` y workflows | MIT | Bibliotecas y servicios externos conservan sus términos |
| Manuscritos, anexos, informes, codebooks y redacción propia | CC BY 4.0 | Citas y pasajes de terceros señalados o atribuibles |
| Selección, estructura, reglas, evaluaciones y variables derivadas de `work/*.csv` | CC BY 4.0 en derechos propios aplicables | Material y derechos de terceros descritos abajo |
| `CITATION.cff`, identificadores, hechos, fechas y URL | Metadatos para citar e identificar | La licencia no crea exclusividad sobre hechos no protegidos |

## Campos del corpus que requieren atención

- `verbatim_text` en `registro_extraccion_congelado_v1.0.csv` transcribe
  declaraciones de ponentes. **No está sublicenciado bajo CC BY 4.0 por este
  proyecto.** Cada fila enlaza `source_url` y localiza el fragmento en
  `source_timestamp_or_page`.
- `context_text`, títulos de sesiones y cualquier otro campo o documento que
  reproduzca palabras literales ajenas quedan excluidos respecto de esas
  palabras, aunque el comentario o la estructura original circundante sí
  pueda estar bajo CC BY 4.0.
- Las URL de evidencia identifican fuentes independientes; no licencian ni
  preservan automáticamente los recursos enlazados.
- Videos, audios, diapositivas, papers y capturas de terceros no forman parte
  de la licencia del proyecto. Su reutilización puede exigir permiso o una
  excepción legal aplicable.

La cita se conserva para auditoría y atribución contextual. Quien reutilice
el corpus completo debe distinguir el permiso para los aportes propios de
los derechos que puedan subsistir sobre las citas. Esta nota de alcance no
resuelve por sí sola la legalidad de cada reutilización en cada jurisdicción.

## Atribución recomendada

> Pacheco, Federico. *Cyber Predictions Audit*, versión utilizada, CC BY 4.0
> para aportes originales y estructura de datos; software MIT. Las citas
> literales de ponentes quedan excluidas de esa licencia.

Para una cita académica legible por gestores bibliográficos, usá
`CITATION.cff`. El DOI sigue pendiente.
