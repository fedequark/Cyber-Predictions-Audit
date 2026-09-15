# Auditoría previa a la apertura del repositorio

**Fecha:** 15 de septiembre de 2026. **Alcance:** ramas y tags Git presentes localmente, y logs recientes de GitHub Actions.

- Se recorrieron 200 objetos únicos del historial Git y se examinaron los blobs de hasta 1 MB con patrones de asignación de credenciales y prefijos conocidos de tokens. No hubo coincidencias candidatas.
- Un blob histórico superaba ese límite: `public/og.png` (aprox. 1,5 MB), una imagen binaria que no se interpretó como texto en el escaneo de patrones.
- Se revisaron cinco logs recientes de Actions con patrones de tokens conocidos; no hubo coincidencias.
- El historial conserva `.openai/hosting.json`, retirado del estado actual. Sus claves históricas son `project_id`, `d1` y `r2`; son referencias de proyecto, no credenciales detectadas por el chequeo.
- Los metadatos de commits incluyen dos direcciones de autor, una personal. GitHub las mostrará cuando el repositorio sea público.
- GitHub Secret Scanning estaba deshabilitado para este repositorio privado; el escaneo local no sustituye una revisión formal de seguridad ni prueba ausencia absoluta de secretos.
- El corpus incluye 120 citas literales de ponentes; `RIGHTS.md` excluye explícitamente esas palabras de la licencia CC BY 4.0 para aportes originales.

La auditoría no reescribe historial ni retira material ya publicado en el sitio de Cloudflare. Si GitHub Secret Scanning señalara una credencial tras la apertura, la respuesta correcta sería revocarla/rotarla y evaluar el historial afectado.
