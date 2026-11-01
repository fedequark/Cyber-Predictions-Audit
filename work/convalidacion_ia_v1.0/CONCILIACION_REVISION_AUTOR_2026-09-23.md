# Conciliación de la revisión del autor — 23 de septiembre de 2026

## Alcance y procedencia

Se conciliaron las 48 respuestas cerradas en `REVISION_AUTOR_2026-09-23.json` (exportación `2026-09-23T19:02:31.651Z`; SHA-256 `855E0C3DBD91591BB5D7BBB46059066BB5B36EEE3D9697553B96CE0E49860E22`). Las respuestas del autor, los 12 CSV de las cuatro IAs y los datos canónicos del estudio no se modificaron. Este documento es una **metarrevisión focal de artefactos**, no una nueva codificación ciega.

Los 48 casos están cerrados y registran que se vieron los votos de las IAs. Por ello, esta etapa es **adjudicación del autor asistida por IA**: no satisface el requisito original de doble codificación humana independiente. La selección de casos estaba enriquecida por desacuerdo y no permite extrapolar porcentajes a los 120 desenlaces.

## Resultado descriptivo de la muestra revisada

| Componente | Casos | Decisiones finales del autor | Nota |
|---|---:|---|---|
| Desenlaces | 18 | 10 cumplido; 2 no cumplido; 5 indeterminado; 1 mixto | 12/18 coinciden con la codificación original; 13/18 contienen URL. |
| Fidelidad semántica | 22 | 17 sí; 5 incierto; 0 no | Persisten cinco casos inciertos. |
| Búsqueda | 8 | 2 cumplido; 6 indeterminado | Ninguna respuesta contiene URL; las dos positivas necesitan conciliación de fuentes. |

Nueve decisiones cambiaron entre la primera y la final. Esto describe el trabajo realizado, no una estimación de exactitud ni una prueba de independencia.

## Desacuerdos de desenlace frente al registro original

| ID | Original → autor | Comprobación focal | Estado para cualquier recálculo |
|---|---|---|---|
| `23-CCC-2018-085-07` | indeterminado → cumplido | El [índice de APWG](https://apwg.org/trendsreports/) permite localizar informes, pero el enlace presentado no documenta una mayoría de **tres series independientes comparables** con aumento ≥10 % entre 2018 y 2019 ni un análisis de campaña que cumpla la segunda condición. | Cumplimiento no verificado; mantener el desacuerdo abierto. |
| `51-BHPRO-2012-03-06` | no cumplido → mixto | La revisión del autor no cita una fuente. El criterio exige **tres** demostraciones independientes de ocultación mediante mecanismos específicos de IPv6 antes del 26-07-2017. | Mixto no sustentado todavía; tampoco inferir ausencia a partir de una búsqueda incompleta. |
| `59-CCC-2016-060-06` | indeterminado → cumplido | El [repositorio Anti-Adblock Killer](https://github.com/reek/anti-adblock-killer) documenta un script, una lista de filtros y actualizaciones. Ese material no acredita, por sí solo, la generación o distribución **automática** de contrarreglas según cambios observados, exigida para admitir filtros manuales. | Cumplimiento no verificado; no convertir suscripción a filtros en adaptación algorítmica. |
| `39-CCC-2006-011-06` | no cumplido → indeterminado | No se aportó fuente para una caja de consumo usada como bot o nodo Tor en 2007. La regla de contradicción requiere evidencia autorizada que descarte ambos usos, no solo ausencia en la búsqueda. | Indeterminado es prudente mientras no se documente búsqueda suficiente. |
| `39-CCC-2006-011-13` | no cumplido → cumplido | La [ficha NVD CVE-2007-1993](https://nvd.nist.gov/vuln/detail/CVE-2007-1993) identifica un desbordamiento en el **demonio RPC `pfs_mountd.rpc` de HP-UX**, explotado mediante llamadas RPC. No describe el disparador congelado de montar, insertar o analizar un sistema de archivos/volumen elaborado. DeepSeek lo describió incorrectamente como un fallo de Linux CIFS. | La fuente citada no justifica «cumplido». Tampoco prueba por sí sola «no cumplido» para todo 2007; hace falta otro caso calificante o una búsqueda negativa documentada. |
| `93-BHKEY-2015-01-01` | no cumplido → indeterminado | El [informe de NAIC](https://content.naic.org/sites/default/files/inline-files/2025_Cybersecurity_Insurance%20Report.pdf) describe el mercado de seguros, pero no proporciona la fracción de **prima / presupuesto de ciberseguridad** en organizaciones compradoras exigida por el indicador. | Indeterminado es coherente con la ausencia de denominador comparable; no usar primas agregadas como sustituto. |

## Dos decisiones positivas de búsqueda

| ID | Evidencia localizada | Límite que queda |
|---|---|---|
| `103-CCC-2008-019-02` (GSM) | La [presentación oficial de 26C3](https://fahrplan.events.ccc.de/congress/2009/Fahrplan/events/3654.en.html) y sus [diapositivas](https://fahrplan.events.ccc.de/congress/2009/Fahrplan/attachments/1519_26C3.Karsten.Nohl.GSM.pdf) documentan tablas A5/1 y herramientas públicas en 2009. | Las diapositivas aún describen partes de la interceptación como hipotéticas o pendientes; la [comunicación del CCC](https://www.ccc.de/de/updates/2009/gsm-nicht-mehr-sicher) aclara que el proyecto no utilizó datos GSM reales por motivos legales. No se verificó aquí el ataque reproducible **contra GSM desplegado** requerido por el umbral. |
| `59-CCC-2016-060-11` (iOS) | Las [notas oficiales de Cellebrite de marzo de 2017](https://media.cellebrite.com/wp-content/uploads/2017/07/UFED6.1_ReleaseNotes_EN.pdf) describen extracción en iOS y capacidades de desbloqueo de CAIS. Una [crónica contemporánea](https://cyberscoop.com/cellebrite-iphone-6-ufed-samsung-galaxy-facebook-messenger-snapchat/) reproduce el anuncio del director de investigación de Cellebrite sobre iPhone 6/6+ bloqueados. | La nota oficial consultada no vincula explícitamente modelo, versión de iOS y barrera de contraseña en un mismo caso; el mensaje primario citado por la crónica no fue accesible directamente. Hay apoyo importante, pero la comprobación primaria exacta sigue pendiente. |

Estas dos respuestas del autor **no tienen URL en la exportación**. Los enlaces anteriores proceden de esta comprobación y de la matriz diagnóstica de Codex; no deben atribuirse retrospectivamente al autor ni contarse como dos búsquedas humanas independientes.

## Fidelidad semántica todavía abierta

Los cinco `incierto` finales son `34-CCC-2013-034-12`, `34-CCC-2013-034-14`, `103-CCC-2008-019-07`, `41-CCC-2011-031-01` y `59-CCC-2016-060-01`. Se conservan como incertidumbre explícita; ningún voto mayoritario de IA los convierte automáticamente en «sí». En seis casos alguna IA votó «no»: el autor cerró tres como «sí» y tres como «incierto», lo que requiere informar la discrepancia, no esconderla.

## Decisión y uso permitido

No se recalculan aquí las tasas del conjunto de 120 predicciones. Las 48 decisiones pueden describirse como resultado de la **revisión focal del autor**, con sus desacuerdos e incertidumbres. No deben presentarse como una validación externa ni sustituir sin examen los juicios canónicos `work/evaluacion_desenlaces_v1.0.csv`. Los cuatro brazos de IA sirvieron para detectar desacuerdos; la búsqueda «independiente» multi-IA tampoco quedó plenamente validada porque dos modelos no navegaron y DeepSeek no tuvo navegación en su ejecución por API.

El veredicto de preparación del proyecto se mantiene en **Weak Reject** (confianza 4/5): la revisión focal mejora la transparencia del desacuerdo, pero no elimina los bloqueantes metodológicos de independencia humana y trazabilidad identificados en la auditoría inicial.

La mínima evidencia que permitiría cerrar los casos de mayor impacto es: (1) fuente que cumpla exactamente el disparador de `39-CCC-2006-011-13` o búsqueda negativa replicable; (2) tres series comparables y un análisis de campaña para `23-CCC-2018-085-07`; (3) documentación de adaptación automática para `59-CCC-2016-060-06`. Para los demás, conservar «indeterminado» cuando falte evidencia es preferible a forzar una decisión binaria.

**Recomendación operativa: obtener primero la evidencia faltante antes de actualizar los resultados centrales o presentar esta etapa como validación independiente.**
