# Cyber Predictions Audit

Material de investigación para **“¿Acertaron los escenarios del futuro cyber? Auditoría retrospectiva de predicciones explícitas en conferencias de ciberseguridad, 2005–2018”**.

- **Sitio público:** [cpa.federicopacheco.com](https://cpa.federicopacheco.com/)
- **Alojamiento:** Cloudflare Pages (`cyber-predictions-audit`).
- **Versión editorial vigente:** 1.4 (15 de septiembre de 2026)
- **Estado académico:** resultados cerrados; validación independiente pendiente.
- **Citación:** metadatos listos en `CITATION.cff`; DOI pendiente de depósito público.
- **Licencias:** MIT para software; CC BY 4.0 para aportes originales de investigación y base de datos. Las citas literales y recursos de terceros quedan excluidos; ver `RIGHTS.md`.

## Resultados principales

- 120 predicciones con horizonte vencido.
- 54 cumplidas, 35 incumplidas y 31 indeterminadas.
- Tasa descriptiva entre los 89 casos resolubles: 60,7%.
- IC Wilson descriptivo: 50,3–70,2%; extremos con indeterminados: 45,0–70,8%.
- Bootstrap exploratorio por sesión: 47,0–72,1%.
- La familia `Security Nightmares` concentra 73/120 casos.
- Diagnóstico exploratorio al excluir una sesión: 58,5–63,5% entre resolubles.
- La indeterminación por dificultad proxy va de 18,2% (baja) a 32,6% (alta); no se imputan resultados.
- Auditoría v1.4: un incumplimiento y 17 indeterminados sin URL probatoria; 14 indeterminados con URL para revisión de suficiencia.
- Consulta de encabezados a 218 localizadores: 161 accesibles, 13 no encontrados, 23 bloqueados/limitados, 18 fallos de red y 3 otros errores. No se archivó contenido.
- Siete predicciones usan `CCC-2013-034` frente a `CCC-2013-043` en el orden S3; orden y URL coinciden. Los originales no se corrigen silenciosamente.
- Otra serie de siete casos (`CCC-2018-085`) usa una URL de predicción 404; el orden S3 contiene una alternativa oficial que responde 200. Se muestran ambos localizadores.
- El marco de 189 sesiones tiene 51 no S3 sin registro individual publicado. La ampliación queda pendiente de su reconstrucción.

## Contenido del repositorio

- `outputs/paper_auditoria_predicciones_cyber_v1.4.md`: manuscrito vigente; integra la auditoría de evidencia y selección.
- `outputs/anexo_metodologico_y_trazabilidad_v1.4.md`: trazabilidad vigente.
- `outputs/auditoria_muestra_y_evidencia_v1.4.md`: triage de 120 casos y 138 sesiones S3.
- `outputs/revision_disponibilidad_fuentes_2026-09-15.md`: foto de disponibilidad HTTP sin contenido remoto.
- `outputs/auditoria_compromiso_y_operacionalizacion_v1.4.md`: mapa de revisión A/B y pistas modales.
- `outputs/protocolo_ampliacion_estratificada_v1.4.md`: selección futura separada del corpus congelado.
- `outputs/protocolo_replica_prospectiva_operativo_v1.4.md`: tarjeta, baseline y puntuación listos, sin pronósticos reales.
- `outputs/plan_deposito_doi_y_preregistro_v1.4.md`: plan de archivo con licencias mixtas; DOI no creado.
- `outputs/nota_revision_focal_caso_p0_v1.4.md`: búsqueda inicial no exhaustiva del único fallo sin URL, sin recodificación.
- `outputs/paper_auditoria_predicciones_cyber_v1.3.md`: manuscrito anterior preservado.
- `outputs/anexo_metodologico_y_trazabilidad_v1.3.md`: anexo anterior preservado.
- `outputs/diagnosticos_adicionales_v1.3.md`: influencia por sesión, indeterminación y evidencia débil.
- `outputs/protocolo_replica_prospectiva_v1.3.md`: diseño de una réplica con probabilidades y baselines preregistrados.
- `outputs/auditoria_preapertura_repo_v1.3.md`: revisión previa de historial y logs, con límites explícitos.
- `outputs/paper_auditoria_predicciones_cyber_v1.2.md`: manuscrito anterior preservado.
- `outputs/anexo_metodologico_y_trazabilidad_v1.2.md`: anexo anterior preservado.
- `outputs/analisis_robustez_y_representatividad_v1.2.md`: incertidumbre, referencias base, concentración, proxies y modelo.
- `outputs/codebook_proxies_v1.2.md`: reglas exactas de especificidad y dificultad exploratorias.
- `outputs/protocolo_preservacion_fuentes_v1.2.md`: niveles de preservación completos y pendientes.
- `outputs/nota_publicacion_v1.2.md`: paquete listo y decisiones editoriales pendientes.
- `outputs/auditoria_critica_integral_v1.1.md`: estado de reproducibilidad y pendientes.
- `outputs/plan_validacion_independiente_v1.1.md`: procedimiento para completar la segunda codificación.
- `outputs/paper_auditoria_predicciones_cyber_v1.0.md`: manuscrito original preservado.
- `outputs/resultados_auditoria_v1.0.md`: resultados consolidados.
- `outputs/preregistracion_consolidada_v0.2.md`: criterios preregistrados.
- `outputs/congelacion_corpus_outcome_blind_v1.0.md`: documentación de la congelación del corpus.
- `outputs/protocolo_evaluacion_desenlaces_v1.0.md`: protocolo de evaluación.
- `outputs/auditoria_cierre_final_v1.0.md`: auditoría final de integridad.
- `work/registro_extraccion_congelado_v1.0.csv`: corpus outcome-blind congelado.
- `work/evaluacion_desenlaces_v1.0.csv`: evaluación de desenlaces.
- `work/orden_seleccion_s3_v0.2.csv`: orden de selección documentado.
- `work/analisis_derivado_v1.2.csv`: variables analíticas derivadas por predicción.
- `work/metricas_robustez_v1.2.csv`: resultados numéricos y estado confirmatorio/exploratorio.
- `work/inventario_fuentes_v1.2.csv`: 218 localizadores, claves y hashes de cápsulas textuales.
- `work/registro_candidatos_excluidos_template_v1.2.csv`: esquema prospectivo; no imputa exclusiones pasadas.
- `work/influencia_sesiones_v1.3.csv`: eliminación de cada sesión, una por vez.
- `work/escenarios_indeterminados_v1.3.csv`: escenarios contrafactuales explícitos.
- `work/triage_evidencia_v1.4.csv`: prioridades de revisión por caso, sin recodificación.
- `work/rendimiento_sesiones_s3_v1.4.csv`: productividad documental de las 138 sesiones S3.
- `work/reconstruccion_marco_no_s3_template_v1.4.csv`: plantilla vacía para las 51 sesiones no enumeradas.
- `work/estado_enlaces_fuentes_2026-09-15.csv`: resultado HTTP de 218 localizadores.
- `work/revision_compromiso_y_operacionalizacion_v1.4.csv`: ficha de revisión semántica aún no completada.
- `work/tarjeta_pronostico_prospectivo_template_v1.4.csv`: plantilla vacía de nuevos pronósticos.
- `work/alternativas_enlaces_fuentes_v1.4.csv`: localizador oficial alternativo para una URL de predicción rota.
- `site/`: fuente estática reproducible del sitio público, con explorador fila por fila.
- `scripts/`: construcción del sitio y herramientas de doble codificación.

## Reproducibilidad

Los hashes se calculan sobre los bytes canónicos publicados. El registro de extracción y el orden S3 conservan su BOM/final de línea original; la evaluación, resultados y manuscrito v1.0 se canonicalizan como UTF-8 sin BOM y LF. El archivo `.gitattributes` y el constructor del sitio preservan esas reglas entre sistemas operativos. Para construir el sitio completo:

```text
npm run build:site
```

Para regenerar los análisis deterministas v1.2–v1.4 y construir el sitio:

```text
npm run check:research
```

El resultado se genera en `dist/` e incluye el sitio, los documentos, los CSV canónicos y derivados, y versiones HTML legibles del paper y del anexo.

La foto HTTP del 15 de septiembre no se regenera en CI porque depende del estado mutable de sitios externos. Para crear una nueva observación fechada, ejecutar `python scripts/comprobar_enlaces_fuentes_v1_4.py` y revisar manualmente los fallos; una respuesta 200 no verifica el contenido.

Para desplegar la salida estática en Cloudflare Pages:

```text
npm run deploy:cloudflare
```

Para preparar la validación independiente:

```text
python scripts/generar_paquete_doble_codificacion.py
```

El comando genera una muestra determinista de 30 desenlaces sin los juicios originales y una hoja conservadora con las 115 operacionalizaciones clase B. No puede reconstruir candidatos excluidos porque ese registro no forma parte del paquete publicado.

El repositorio excluye deliberadamente videos, audios, dependencias descargadas,
archivos temporales y copias locales de fuentes. La capa v1.2 añade un inventario
de localizadores y hashes de las cápsulas textuales conservadas. No presenta esos
hashes como copias de los recursos remotos.

La publicación académica definitiva aún requiere depósito inmutable con DOI,
y completar declaraciones editoriales. Abrir GitHub facilita la reproducción,
pero no cambia el alojamiento: el sitio permanece en Cloudflare Pages.
