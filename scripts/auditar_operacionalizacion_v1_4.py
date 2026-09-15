"""Make the frozen A/B operationalization burden inspectable without recoding it."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
OUTPUTS = ROOT / "outputs"
with (WORK / "registro_extraccion_congelado_v1.0.csv").open(encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))
assert len(rows) == 120

# A lexical cue only queues contextual review; it cannot decide commitment.
modal = re.compile(r"\b(could|might|may|possible|possibly|könnte|können|podría)\b", re.IGNORECASE)
focus = {
    "31-VB-2016-P01-10": "Roadmap stage states a capability a product could have; adoption as forecast requires contextual verification.",
    "34-CCC-2013-034-14": "German 'könnte es passieren' expresses possibility; speaker commitment is not yet independently established.",
}
audit = []
for row in rows:
    key = f"{int(row['selection_order'])}-{row['session_id']}-{row['candidate_order']}"
    cue = modal.search(row["verbatim_text"])
    audit.append({
        "prediction_key": key,
        "prediction_class_frozen": row["prediction_class"],
        "horizon_source_frozen": row["horizon_source"],
        "prediction_type_frozen": row["prediction_type"],
        "authorship_frozen": row["authorship"],
        "modal_word_in_excerpt": cue.group(0) if cue else "",
        "contextual_review_priority": "P0" if key in focus else "P1" if cue else "P2" if row["prediction_class"] == "B" else "P3",
        "review_question": focus.get(key, "Check whether the literal claim supports the frozen threshold and deadline." if row["prediction_class"] == "B" else "Check direct scoreability against the original segment."),
        "source_segment_reviewed_v1_4": "no",
        "speaker_commitment_reassessment": "not_assessed",
        "threshold_translation_reassessment": "not_assessed",
        "proposed_addendum": "",
    })

fields = list(audit[0])
with (WORK / "revision_compromiso_y_operacionalizacion_v1.4.csv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(audit)

classes = Counter(row["prediction_class_frozen"] for row in audit)
horizons = Counter(row["horizon_source_frozen"] for row in audit)
cues = [row for row in audit if row["modal_word_in_excerpt"]]
text = [
    "# Auditoría de compromiso y operacionalización v1.4", "",
    "**Estado:** mapa de revisión post hoc; el corpus congelado y sus juicios no se alteran.", "",
    "## Magnitud de la traducción", "",
    f"De 120 unidades, **{classes['A']}** son clase A y **{classes['B']}** clase B. La clase B necesitó especificar población, umbral, indicador o mecanismo; no es por sí misma una afirmación inválida. La proporción global mezcla ambas clases y no mide cuánto juicio añadió cada operacionalización.", "",
    "Los horizontes tienen etiquetas originales heterogéneas. `section_inherited` aparece en **" + str(horizons["section_inherited"]) + "** filas e `individual` en **" + str(horizons["individual"]) + "**; otras etiquetas combinan o contextualizan ambas fuentes. No se colapsan sin releer el segmento original.", "",
    "## Frases modales para revisión contextual", "",
    f"Una búsqueda léxica conservadora señala **{len(cues)}** citas con palabras como *could*, *might* o *könnte*. Es un filtro de revisión, no una decisión sobre validez: una oración puede mencionar una posibilidad y luego adoptar un pronóstico firme.", "",
    "Dos casos merecen revisión primero:", "",
]
for key, reason in focus.items():
    text.append(f"- `{key}`: {reason}")
text += [
    "", "No se excluyen todavía. El texto corto y el contexto conservado no sustituyen la grabación o diapositiva íntegra. Una reauditoría debe documentar: (1) si el hablante adopta el resultado, (2) si el horizonte aplica a esa proposición, (3) qué parte del umbral se añadió, y (4) si otro umbral razonable cambiaría el juicio. Cualquier exclusión o cambio de regla será adenda exploratoria con trazabilidad y tasa recalculada por separado.",
    "", "## Instrumento", "",
    "`work/revision_compromiso_y_operacionalizacion_v1.4.csv` preserva la clave y los metadatos congelados, y deja estados `not_assessed` para una revisión real del segmento. No debe rellenarse automáticamente con inferencias del resultado ya conocido.", "",
]
(OUTPUTS / "auditoria_compromiso_y_operacionalizacion_v1.4.md").write_text("\n".join(text), encoding="utf-8", newline="\n")
print(f"Mapa v1.4: A={classes['A']}, B={classes['B']}, pistas modales={len(cues)}; sin recodificación.")
