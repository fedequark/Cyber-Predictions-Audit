# Protocolo de preservación de fuentes v1.2

Este protocolo mejora la trazabilidad sin afirmar que ya existe una copia íntegra de cada recurso remoto.

## Nivel preservado en v1.2

1. Cada predicción conserva URL, localizador temporal o página, cita literal y contexto.
2. Cada desenlace conserva URL primaria/secundaria, periodo, síntesis factual y aplicación del umbral.
3. `inventario_fuentes_v1.2.csv` reúne los localizadores únicos, las claves afectadas y el SHA-256 de la cápsula textual conservada.
4. Los registros congelados permanecen inalterados; el inventario es derivado y regenerable.

## Nivel pendiente

Para cada fuente se debe guardar, cuando licencia y acceso lo permitan:

- una captura WARC o PDF con fecha de acceso;
- una captura de la página o diapositiva exacta usada;
- transcripción local del segmento citado;
- hash SHA-256 de cada archivo;
- URL de una copia archivada independiente;
- motivo documentado cuando la preservación no sea legal o técnicamente posible.

Los archivos binarios no deben mezclarse con los CSV canónicos. Un depósito de preservación debe usar almacenamiento versionado, un manifiesto de hashes y una política explícita sobre material con copyright. La existencia de una URL en el inventario no equivale a preservación del contenido remoto.
