# Revisión focal inicial del único incumplimiento sin URL probatoria

**Caso:** `39-CCC-2006-011-06`. **Fecha:** 15 de septiembre de 2026. **Estado:** búsqueda inicial no exhaustiva, sin nuevo juicio.

El umbral congelado exige un caso verificado durante 2007 de una caja de consumo VoIP, IPTV o reproductor multimedia funcionando como infraestructura de botnet o nodo Tor. La evaluación v1.0 la clasificó `not_fulfilled` con fuerza `weak`, sin URL primaria ni secundaria; su aplicación declara que no se estableció un caso calificante. Eso es una debilidad concreta de auditabilidad: la ausencia de un hallazgo en una búsqueda no demuestra por sí misma la ausencia histórica del evento.

En la revisión inicial se buscaron combinaciones de *2007*, *set-top/VoIP/IPTV/media player*, *botnet* y *Tor node*. Dos documentos cercanos no superan el umbral:

- [Análisis de Storm de Steven Murdoch, 7 septiembre 2007](https://www.lightbluetouchpaper.org/2007/09/07/analysis-of-the-storm-javascript-exploits/): describe un falso ejecutable Tor que incorpora computadoras a una botnet; no una caja de consumo funcionando como nodo o bot.
- [Informe de la UIT sobre botnets, 2008, con contexto 2007](https://www.itu.int/dms_pub/itu-s/opb/gen/S-GEN-CYBER-2008-PDF-E.pdf): caracteriza la generación Storm, pero no documenta un dispositivo del tipo requerido.

La búsqueda no cubrió de manera exhaustiva archivos de respuesta a incidentes, listas históricas de relays Tor ni catálogos de hardware. El juicio congelado no se modifica; tampoco se presenta el resultado de esta búsqueda como prueba de no ocurrencia. La sensibilidad exploratoria ya publicada muestra que tratar **sólo contrafactualmente** este caso como indeterminado movería la tasa resoluble de 54/89 = 60,7% a 54/88 = 61,4%.

Próxima revisión: buscar archivos históricos de Tor y reportes contemporáneos de malware por modelo de aparato, documentar cada consulta y aplicar literalmente el umbral antes de proponer una adenda.
