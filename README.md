# Cyber Predictions Audit

Material de investigación para **“¿Acertaron los escenarios del futuro cyber? Auditoría retrospectiva de predicciones explícitas en conferencias de ciberseguridad, 2005–2018”**.

- **Sitio público:** [cpa.federicopacheco.com](https://cpa.federicopacheco.com/)
- **Versión editorial vigente:** 1.1 (24 de agosto de 2026)
- **Estado académico:** resultados cerrados; validación independiente pendiente.
- **Citación:** metadatos listos en `CITATION.cff`; DOI pendiente de depósito público.

## Resultados principales

- 120 predicciones con horizonte vencido.
- 54 cumplidas, 35 incumplidas y 31 indeterminadas.
- Tasa descriptiva entre los 89 casos resolubles: 60,7%.

## Contenido del repositorio

- `outputs/paper_auditoria_predicciones_cyber_v1.1.md`: manuscrito vigente.
- `outputs/anexo_metodologico_y_trazabilidad_v1.1.md`: tablas derivadas y correspondencia de identificadores.
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
- `site/`: fuente estática reproducible del sitio público, con explorador fila por fila.
- `scripts/`: construcción del sitio y herramientas de doble codificación.

## Reproducibilidad

Los hashes se calculan sobre los bytes canónicos publicados. El registro de extracción y el orden S3 conservan su BOM/final de línea original; la evaluación, resultados y manuscrito v1.0 se canonicalizan como UTF-8 sin BOM y LF. El archivo `.gitattributes` y el constructor del sitio preservan esas reglas entre sistemas operativos. Para construir el sitio completo:

```text
npm run build:site
```

El resultado se genera en `dist/` e incluye el sitio, los documentos, los tres CSV de trabajo y versiones HTML legibles del paper y del anexo.

Para preparar la validación independiente:

```text
python scripts/generar_paquete_doble_codificacion.py
```

El comando genera una muestra determinista de 30 desenlaces sin los juicios originales y una hoja conservadora con las 115 operacionalizaciones clase B. No puede reconstruir candidatos excluidos porque ese registro no forma parte del paquete publicado.

El repositorio excluye deliberadamente videos, audios, dependencias descargadas,
archivos temporales y copias locales de fuentes. Las tablas conservan las URL y
los metadatos necesarios para identificar la evidencia utilizada.
