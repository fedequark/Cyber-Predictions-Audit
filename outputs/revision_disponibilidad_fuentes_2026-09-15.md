# Revisión de disponibilidad de enlaces (2026-09-15)

**Alcance:** 218 combinaciones rol–URL del inventario v1.2. Se consultaron únicamente encabezados HTTP. No se descargó ni archivó el contenido y no se verificó que cada URL siga respaldando la proposición.

| Resultado de la consulta | Entradas |
|---|---:|
| http_success | 161 |
| blocked_or_rate_limited | 23 |
| http_not_found | 13 |
| http_error | 3 |
| network_error | 18 |

Una respuesta 200 sólo indica acceso HTTP en este momento, no preservación ni validez de evidencia. Un 403, 429 o fallo de red tampoco prueba desaparición: puede ser una política anti-bots o un error transitorio. Los casos no accesibles requieren revisión manual y una fuente archivada o alternativa legal.

Una de las 13 respuestas 404 era una fuente de predicción para siete casos de `CCC-2018-085`. El orden S3 congelado contiene para esa misma sesión una URL oficial alternativa (`https://media.ccc.de/v/35c3-9685-security_nightmares_0x13`), que respondió HTTP 200. Se conserva la URL original y se registra la alternativa en `work/alternativas_enlaces_fuentes_v1.4.csv`. Esto recupera el localizador, no una copia inmutable ni una reauditoría del fragmento.

Detalle: `work/estado_enlaces_fuentes_2026-09-15.csv`.
