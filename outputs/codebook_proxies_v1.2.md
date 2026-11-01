# Codebook de proxies exploratorios v1.2

Los proxies se definieron después de conocer el corpus. Sirven para auditar heterogeneidad; no reemplazan una codificación humana validada.

## Especificidad proxy (0–4)

Se suma un punto por cada condición:

1. `prediction_class = A` (el original era directamente puntuable).
2. El texto original contiene detalle numérico o cuantificador explícito.
3. `horizon_literal` está informado.
4. `population` y `geography` están informadas.

Bandas: baja 0–2, media 3, alta 4. El detector numérico se publica en `scripts/analizar_robustez_v1_2.py`.

## Dificultad proxy

- **Baja:** ocurrencia simple, categoría, saliencia o maduración de capacidad.
- **Media:** dirección, adopción, diseño, no-ocurrencia, persistencia, amplitud o similitud textual.
- **Alta:** conteo, tendencia, prevalencia, proporción, cuota, récord o estados/mecanismos compuestos.

La regla usa sólo `prediction_type`. No incorpora conocimiento posterior sobre si el evento ocurrió.

## Interpretación

Las tasas por banda son descriptivas. Las bandas pueden mezclar temas, años, venues y disponibilidad de evidencia. Cualquier afirmación sustantiva sobre “dificultad” o “especificidad” exige doble codificación y validación externa del instrumento.
