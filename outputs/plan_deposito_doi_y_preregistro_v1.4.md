# Depósito con DOI y preregistro externo: estado y plan

**Estado al 15 de septiembre de 2026:** no se creó DOI ni registro externo. Zenodo abrió sin sesión iniciada; el paquete usa derechos mixtos y contiene citas de terceros. El preregistro operativo prospectivo permanece sólo como archivo versionado en GitHub hasta que se registre antes de recoger datos nuevos.

## Depósito retrospectivo

Recomendación: crear un registro Zenodo de **dataset/manuscrito v1.4**, no activar a ciegas la ingestión automática de todo GitHub. Zenodo permite declarar licencias mixtas y una licencia personalizada; su valor por defecto CC BY 4.0 para un upload completo no representaría correctamente las citas literales y otros materiales de terceros. Antes de publicar, revisar el alcance campo por campo en `RIGHTS.md`, el manifiesto de archivos y la vista previa de metadatos. En particular, un CSV con `verbatim_text` necesita advertencia explícita de material no sublicenciado; una exportación sin citas puede tener condiciones distintas, pero debe mantener claves y localizadores para que la fuente siga trazable.

Archivos candidatos: paper y anexo v1.4, protocolos, CSV canónicos y capas derivadas, `LICENSE`, `LICENSE-DATA.md`, `RIGHTS.md` y un manifiesto de hashes. No adjuntar videos ni diapositivas de terceros salvo permiso propio verificable. El registro debe citar la release exacta v1.4 y mantener futuras versiones separadas. Una vez publicado, Zenodo no permite sustituir archivos de la misma versión; corregir mediante versión nueva y nota de cambio.

## Preregistro prospectivo

Registrar en OSF **antes** de seleccionar o extraer nuevos pronósticos el marco, reglas, tarjeta, probabilidades, baseline y análisis del protocolo operativo. No declarar que v1.0 o v1.4 fueron registrados externamente antes de sus datos: sólo el estudio nuevo puede recibir ese estatus. Vincular el registro OSF al DOI del depósito retrospectivo cuando exista, pero mantener ambas contribuciones conceptualmente separadas.

## Condición de ejecución

El depósito y el registro requieren una sesión del autor en Zenodo/OSF y revisión final de metadatos, alcance de licencias y archivos. Nada de esto se presume completado por un commit o una release de GitHub. El sitio permanece en Cloudflare; los DOI serían identificadores de archivo/citación, no un cambio de alojamiento.

## Referencias operativas

- [Zenodo: licencias y derechos mixtos](https://help.zenodo.org/docs/deposit/describe-records/licenses/).
- [Zenodo: publicar un depósito y límites de edición de archivos](https://help.zenodo.org/docs/get-started/quickstart/).
- [OSF: preregistros y registros públicos](https://help.osf.io/article/330-welcome-to-registrations).
