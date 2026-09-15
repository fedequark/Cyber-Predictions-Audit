# Seguimiento documental v1.4a — 15 de septiembre de 2026

**Carácter:** adenda de búsqueda y disponibilidad posterior a los juicios congelados. Ningún desenlace v1.0 ni el denominador de 120 se modifica aquí.

## 1. Enlaces y preservación

El inventario contiene 218 pares `rol–URL`. La foto HTTP del 15 de septiembre de 2026 encontró 161 éxitos y 57 consultas no exitosas: 13 HTTP 404, 23 bloqueadas o limitadas, 18 errores de red y 3 errores HTTP distintos. Los 57 pares afectan a **51 claves de predicción únicas**. El CSV `work/seguimiento_enlaces_fuentes_v1.4a.csv` conserva por fila el URL original, rol, estado, claves afectadas y hash de la cápsula textual v1.2. Los hashes son de texto conservado, **no** de copias completas del recurso remoto.

Se comprobaron tres candidatos bajo control del editor, con HTTP 200 en una consulta independiente:

| URL original problemática | Candidato | Relación y cautela |
|---|---|---|
| [Grabación CCC 2018](https://media.ccc.de/v/35c3-10030-security_nightmares_0x13) | [Programa oficial CCC](https://media.ccc.de/v/35c3-9685-security_nightmares_0x13) | Misma sesión según el orden S3 congelado; siete casos. El segmento aún no se reexaminó. |
| [Comunicado DOJ original](https://www.justice.gov/opa/pr/two-iranian-nationals-charged-cyber-enabled-campaign-threaten-and-influence-american-voters) | [Archivo oficial DOJ](https://www.justice.gov/archives/opa/pr/two-iranian-nationals-charged-cyber-enabled-disinformation-and-threat-campaign-designed) | Misma acusación de 18 de noviembre de 2021; un caso. El relato describe actos de 2020, pero debe revalidarse la cronología y el umbral; una acusación no es condena. |
| [Guía NCSC original](https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/updates) | [Guía NCSC relacionada](https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/keeping-devices-and-software-up-to-date) | Página oficial de tema afín, **no** copia idéntica; un caso. No prueba por sí sola el recuento de seis de ocho familias con actualizaciones por defecto. |

No se reemplaza ningún enlace literal en los CSV canónicos. Un 404 puede ser una mudanza; un 403 puede ser una política antibot; una consulta HEAD exitosa no verifica el cuerpo ni su pertinencia. La preservación completa (WARC/PDF/audio) queda pendiente de licencia, acceso y verificación de integridad; no se redistribuyen materiales de terceros bajo la licencia del research.

## 2. Caso P0: evidencia contextual nueva, no calificante

Para `39-CCC-2006-011-06`, la [publicación primaria de Dartmouth](https://www.cs.dartmouth.edu/~sws/pubs/bbss07.pdf), presentada en WESS 2007 según el [registro bibliográfico del autor](https://www.cs.dartmouth.edu/~sws/research/pubs.shtml), documenta cajas multimedia/set-top ya desplegadas en un campus y ataques experimentales mediante ellas. El trabajo dice explícitamente que los investigadores **se detuvieron antes de crear un gusano** que propagara una botnet. Es una fuente contemporánea que estrecha la pregunta histórica, pero no documenta que una caja de consumo operara como infraestructura de botnet en producción o como nodo Tor durante 2007, tal como exige el umbral congelado. Tampoco prueba la ausencia de otros casos. El juicio `not_fulfilled` sigue intacto y el problema de evidencia negativa permanece.

La búsqueda exploratoria incluyó combinaciones de `2007`, `set-top box`, `botnet`, `IPTV`, `media player`, `Tor relay` y programas/estudios contemporáneos. Los resultados sobre Storm usaban PCs o un ejecutable Tor falso; no el tipo de caja requerido. La búsqueda no fue exhaustiva sobre avisos de fabricantes, reportes de incidentes y archivos históricos de relays.

## 3. Compromiso del hablante: dos casos prioritarios

Las [diapositivas oficiales de Virus Bulletin 2016](https://www.virusbulletin.com/uploads/pdf/conference_slides/2016/ASanabria-vb-2016-Begining-of-endpoint.pdf), página 30 del PDF (índice 29), sitúan “Data visibility” en el punto 5 de *Adrian’s Endpoint Security Roadmap*, dentro de una charla titulada “where we are now and where we’ll be in five years”. Esto confirma el marco de hoja de ruta, pero las diapositivas no contienen la oración oral “a product that could tell us…”. Para `31-VB-2016-P01-10` todavía falta revisar el audio completo y distinguir un deseo/capacidad hipotética de un pronóstico asumido. Su juicio `fulfilled` no se elimina automáticamente.

La [página oficial CCC 2013](https://media.ccc.de/v/30C3_-_5413_-_de_-_saal_1_-_201312301715_-_security_nightmares_-_frank_-_ron) confirma la grabación y ofrece subtítulos de terceros, pero el servicio de subtítulos no respondió en esta revisión. Para `34-CCC-2013-034-14`, “könnte es passieren” sigue siendo una modalidad posible; sin el tramo íntegro no se determina si el hablante la adoptó como pronóstico. La búsqueda exploratoria de investigación sobre basebands tampoco encontró un documento de 2014 que reúna a la vez explotación remota, demostración práctica y exposición de al menos un millón de dispositivos; un trabajo de 2012 o una falla de gestión de dispositivos no satisfacen esa combinación. El juicio `indeterminate` sigue intacto.

## 4. Muestra prospectiva y registro externo

El historial del repositorio conserva las 138 filas S3 y sólo el agregado de **51** no S3; no contiene un inventario original de esas filas. Los programas externos pueden producir *candidatos*, pero no demuestran que pertenecieran al marco cerrado de 189. La reconstrucción queda a la espera del registro original de selección o una cadena de procedencia equivalente; el template no se rellena con conjeturas.

La cohorte prospectiva sigue en **cero pronósticos reales**. El protocolo y puntuador pueden probarse, pero el marco, cuota, línea base y versión final deben cerrarse y registrarse antes de recoger afirmaciones. No hay DOI ni preregistro OSF en esta fecha; requieren cuenta autenticada y revisión de metadatos/derechos. No se usará un registro creado ahora para aparentar preregistro de la cohorte histórica.

## 5. Próxima tanda recomendada

1. Obtener el registro original de las 51 sesiones; si no existe, publicar una reconstrucción externa etiquetada como **nuevo marco**, no como recuperación cierta del original.
2. Revisar con audio íntegro los dos casos de compromiso modal, con nota de contexto, transcripción mínima y evaluación ciega al desenlace donde sea posible.
3. Recuperar cuerpo y fecha de los tres candidatos editoriales y priorizar las 17 predicciones P1 sin URL, sin inferir ausencia de evento de una búsqueda negativa.
