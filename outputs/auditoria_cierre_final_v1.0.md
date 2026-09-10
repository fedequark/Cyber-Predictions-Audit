# Auditoría de cierre final

**Fecha:** 8 de agosto de 2026

| Requisito | Evidencia | Estado |
|---|---|---|
| Recorrer todas las sesiones del orden S3 | 138 filas en `orden_seleccion_s3_v0.2.csv` y 138 archivos `cierre_extraccion_sesion_*` | Cumplido |
| Resolver verificaciones lingüísticas | Cierres 005 y 023 documentan revisión directa del alemán y resolución de la retención | Cumplido |
| Aplicar regla de parada de 80–120 | Congelación en el límite superior de 120, sin sustituciones posteriores | Cumplido |
| Limitar a horizontes vencidos | 120/120 filas congeladas con `horizon_expired=yes` | Cumplido |
| Congelar outcome-blind | Registro v1.0, SHA-256 `323739E747379873D5786DB7057E7357EED0F70F0E6425AE6A3339B96AEDA32B` | Cumplido |
| Evaluar todos los desenlaces | 120/120 claves, 0 faltantes, 0 extras, 0 duplicados | Cumplido |
| Mantener coherencia de codificación | 0 juicios inválidos y 0 discordancias juicio/binario | Cumplido |
| Producir resultados y sensibilidad | `resultados_auditoria_v1.0.md`; 54/35/31 y límites 45,0–70,8% | Cumplido |
| Redactar paper final en español | `paper_auditoria_predicciones_cyber_v1.0.md`, 2.534 palabras, sin TODO/TBD | Cumplido |
| Conservar trazabilidad | Texto, reformulación, umbral y reglas en corpus; fuentes y aplicación en tabla de desenlaces | Cumplido |

## Artefactos finales

- Corpus outcome-blind: `work/registro_extraccion_congelado_v1.0.csv`
- Desenlaces: `work/evaluacion_desenlaces_v1.0.csv` — SHA-256 `B3CE8AD49F6555870FCF415488506717BD8D7E71F4B955ED03514F7CE9E26F1B`
- Resultados: `outputs/resultados_auditoria_v1.0.md` — SHA-256 `61753C4F8E187AEC9B76086BF7525973793D1AF5FE9ED2210B8473359B161272`
- Paper: `outputs/paper_auditoria_predicciones_cyber_v1.0.md` — SHA-256 `76D58C5D563CD2050AC81A1C668E33AF16F71FE47FE65665C650CE803DA1424B`

## Salvedades conservadas

El estudio es descriptivo, con un solo codificador, preregistro interno y fuerte concentración en *Security Nightmares*. Los enlaces probatorios faltan en 18 filas: 17 son indeterminadas con evidencia débil y una es un no-cumplimiento débil; ninguna se presenta como acierto. Estas limitaciones están declaradas en el manuscrito y no quedan requisitos operativos pendientes.
