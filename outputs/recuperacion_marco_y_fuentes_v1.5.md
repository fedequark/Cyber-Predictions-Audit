# Recuperación del marco original y seguimiento de fuentes v1.5

Fecha de corte de esta revisión: 15 de septiembre de 2026. Esta es una auditoría documental **posterior** a la congelación y adjudicación de las 120 predicciones. No modifica los registros, el orden S3 ni los desenlaces originales.

## Procedencia del denominador

El directorio original de trabajo en `OneDrive/PRIA/1 Projects/Research - PrediccionesConfs/work` conserva `marco_maestro_189_sesiones_v0.9.csv` (SHA-256 `A9C608FA24B54FFEE534500EBA46FEA1F9B4FB0C331B80C02EE6359762B68EDB`). Se incorporó una copia **byte por byte** al repositorio, no una lista inferida a partir del total agregado. Sus 189 `frame_id` son únicos; las 138 filas calificadas S3 coinciden exactamente por ID con `orden_seleccion_s3_v0.2.csv`. Las otras 51 son 33 Black Hat USA y 18 Virus Bulletin; CCC tiene 85/85 S3.

| Periodo | Black Hat USA no S3 | Virus Bulletin no S3 | Total |
| --- | ---: | ---: | ---: |
| 2005–2009 | 11 | 6 | 17 |
| 2010–2014 | 19 | 5 | 24 |
| 2015–2018 | 3 | 7 | 10 |
| **Total** | **33** | **18** | **51** |

La calificación **original**, al cierre del marco, era 29 `pending_archive`, 4 `pending_manual`, 17 `pending_paper` y 1 S1. «Pendiente» describe una búsqueda no cerrada; no prueba que la charla carezca para siempre de una fuente integral. Ninguna de estas 51 produjo unidades en el corpus congelado, y eso no equivale a un fracaso predictivo.

También se conservaron byte por byte los tres registros de disponibilidad originales: Black Hat 2005–2013 (SHA-256 `4D9B7B560CA715FFFA3DFBD4BC2401DBC83C725ECAB5B9B57A5264B845BAE1CB`), Black Hat 2014–2018 (`0A92DE1C5E3AD9FDC8C5803DF3419E052DF0E412A4C61F691BC1389C0A0FC8CB`) y Virus Bulletin (`38BE2A60CA85E1196CA9C8F79AF9A6E869CAD7E81596E8302B1BE7083BDEAE5B`). Las 33 filas Black Hat tienen motivo individual: 31 indican que la primera búsqueda no encontró coincidencia de título en el canal oficial, una descarta un vídeo de Black Hat Europe por exigir USA y una descarta una falsa coincidencia de título. Esto tampoco es un agotamiento de archivos. En el registro Virus Bulletin, 17 filas quedaron `pending_paper` sin motivo individual más fino; la S1, `VB-2011-P03`, sí consta como fuente primaria insuficiente.

## Revisión focal de las 17 Virus Bulletin pendientes

Se contrastaron por ID/título el programa o abstract oficial, los índices de slides de 2006–2015 donde existen, y búsquedas dirigidas de paper/diapositivas de autor. Para 2016–2018 se revisaron las fichas oficiales y los indicadores de material que pudieron verificarse. El estado siguiente es **nuevo** y se informa por separado de `source_grade` original. Enlaces a recursos, no reproducción de papers o slides de terceros.

| ID | Fuente / búsqueda verificable | Estado posterior y límite |
| --- | --- | --- |
| `VB-2006-K01` | [Índice oficial VB2006](https://www.virusbulletin.com/conference/vb2006/vb2006-slides/) enlaza [142 slides del ponente](https://www.virusbulletin.com/uploads/pdf/conference_slides/2006/MikkoHypponen_VB2006.pdf). | Diapositivas primarias recuperadas. Son extensas, pero muchas contienen sólo nombres, imágenes o palabras sueltas; no se demuestra autosuficiencia del discurso. **S2 candidato**, no S3 confirmado. |
| `VB-2006-K02` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2006/abstracts/data-exfiltration-techniques-how-attackers-steal-your-sensitive-data/) llama «paper» al trabajo; no figura en el [índice de slides](https://www.virusbulletin.com/conference/vb2006/vb2006-slides/). | Paper integral de Rob Murawski no verificado en esta pasada; pendiente. |
| `VB-2007-P01` | [Ficha oficial](https://www.virusbulletin.com/conference/vb2007/abstracts/future-threats/) y [página bibliográfica del coautor John Aycock](https://pages.cpsc.ucalgary.ca/~aycock/) identifican *Future Threats*, proceedings VB2007 pp. 275–281, con [PDF alojado por el autor](https://cspages.ucalgary.ca/~aycock/papers/vb2007future.pdf) que responde HTTP 200. | **Paper primario integral recuperado posteriormente; S3 documental posterior** bajo la vía de paper completo. No entra retroactivamente en las 138 sesiones ni en las 120 unidades. |
| `VB-2008-P01` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2008/abstracts/last-minute-presentation-vb-testing-present-status-future-plans/); el [índice oficial de slides](https://www.virusbulletin.com/conference/vb2008/vb2008-slides/) lista *Race to Zero*, no esta charla. | Sigue pendiente. El deck de la sesión siguiente no se atribuye a ésta. |
| `VB-2009-K01` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2009/abstracts/keynote-address-reforming-landscape/) e [índice VB2009](https://www.virusbulletin.com/conference/vb2009/vb2009-slides/). | La fuente integral de la keynote no se verificó; pendiente. |
| `VB-2009-P01` | [Ficha oficial](https://www.virusbulletin.com/conference/vb2009/abstracts/malice-through-looking-glass-behaviour-analysis-next-decade/) y [bibliografía publicada por David Harley, coautor](https://geekpeninsula.wordpress.com/virus-bulletin/virus-bulletin-conference-papers/) enlazan su [paper VB2009 de seis páginas](https://geekpeninsula.wordpress.com/wp-content/uploads/2013/04/harley-debrosse-vb2009.pdf), que responde HTTP 200. | **Paper primario integral recuperado posteriormente; S3 documental posterior**. No altera la muestra o puntuación congeladas. |
| `VB-2010-K01` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2010/abstracts/threats-social-web/); la keynote no figura en el [índice de slides VB2010](https://www.virusbulletin.com/conference/vb2010/vb2010-slides/). | Sin grabación/paper integral verificado; pendiente. |
| `VB-2011-K01` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2011/abstracts/keynote-address-m00p-investigation-law-enforcement-and-anti-virus-industry-working-partnership/); no figura en el [índice de slides VB2011](https://www.virusbulletin.com/conference/vb2011/vb2011-slides/). | Una crónica de VB2011 no sustituye la fuente de los ponentes; pendiente. |
| `VB-2011-P02` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2011/abstracts/security-2012-staying-ahead-game/); no figura en el [índice de slides VB2011](https://www.virusbulletin.com/conference/vb2011/vb2011-slides/). | No se identificó paper/deck de esta presentación de ESET; pendiente. |
| `VB-2014-K01` | [Programa oficial](https://www.virusbulletin.com/conference/vb2014/programme/); el [índice de slides](https://www.virusbulletin.com/conference/vb2014/vb2014-slides/) advierte explícitamente que faltan decks de algunos ponentes. | Keynote no localizada en el índice; búsqueda pendiente. |
| `VB-2015-P01` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2015/abstracts/clean-software-alliance-security-and-future-unwanted-behaviours); los papers hallados sobre CSA pertenecen a otros autores/otra sesión. | No se verificó material integral de Nav Jagpal y Barak Shein para esta charla; pendiente. |
| `VB-2016-K01` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2016/abstracts/keynote-1/) identifica a Christine Whalley; la entrevista previa no es la keynote. | Sin recurso integral de la sesión verificado; pendiente. |
| `VB-2016-K02` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2016/abstracts/keynote-2) sólo ofrece «details TBA». | Sin recurso integral de Morgan Marquis-Boire verificado; pendiente. |
| `VB-2017-K01` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2017/abstracts/keynote-address-inside-cloudbleed/) documenta la charla, no su contenido íntegro. | Sin recurso integral de la keynote verificado; pendiente. |
| `VB-2017-K02` | [Abstract oficial](https://www.virusbulletin.com/conference/vb2017/abstracts/keynote-address-failure-option/) documenta la charla. | Sin recurso integral verificado; pendiente. |
| `VB-2018-K01` | [Ficha oficial VB2018](https://www.virusbulletin.com/conference/vb2018/abstracts/keynote-address-customers-suppliers-and-adversaries-come-them/) anuncia «Download slides», pero la petición de la ficha quedó bloqueada/expiró en esta revisión y no se inspeccionó el PDF. | **Deck anunciado, integridad pendiente**. No se asigna S3 por un botón o metadato. |
| `VB-2018-K02` | [Programa oficial VB2018](https://www.virusbulletin.com/conference/vb2018/programme) y [abstract](https://www.virusbulletin.com/conference/vb2018/abstracts/keynote-address-denial-trust-new-attacks). | Sin recurso integral verificado; pendiente. |

Resultado de esta primera pasada: dos papers primarios recuperados como S3 **posterior**, un deck primario que requiere revisión de autosuficiencia, un deck anunciado cuyo PDF no se verificó y trece búsquedas aún abiertas. No se afirma que esos trece recursos no existan. Las consultas a fichas VB2018 devolvieron 403 o timeout según la ruta; esos fallos se registran como límite de acceso, no como ausencia documental.

## Implicación para el estudio

La antigua frase «51 registros sin inventario» era cierta sólo para el paquete público anterior, no para el directorio original. Con esta publicación, el denominador de 189 es auditable por ID, venue, año y calificación **a la fecha de la selección original**. La disponibilidad actual ya puede divergir del corte original. Rescatar fuentes o extraer nuevos pronósticos requiere un **estudio de ampliación prospectivamente definido**: no sumar unidades a los 120 congelados después de conocer los resultados. La doble codificación independiente sigue pospuesta por decisión del investigador.

Próximas prioridades: verificar el binario y autosuficiencia de `VB-2018-K01`, revisar visualmente el deck `VB-2006-K01`, agotar por fuente/archivo las trece búsquedas Virus Bulletin aún abiertas y las 33 Black Hat con una regla explícita de cierre antes de seleccionar una ampliación. Los dos papers recuperados no deben redistribuirse sin permiso; se publican sólo sus localizadores.
