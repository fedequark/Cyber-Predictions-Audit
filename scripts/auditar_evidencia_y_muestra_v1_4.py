"""Derived v1.4 evidence triage and S3-session yield; canonical CSVs stay untouched."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
OUTPUTS = ROOT / "outputs"


def read_csv(name: str) -> list[dict[str, str]]:
    with (WORK / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(name: str, fields: list[str], rows: list[dict[str, object]]) -> None:
    with (WORK / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


extraction = read_csv("registro_extraccion_congelado_v1.0.csv")
outcomes = read_csv("evaluacion_desenlaces_v1.0.csv")
sessions = read_csv("orden_seleccion_s3_v0.2.csv")
assert len(extraction) == len(outcomes) == 120
assert len(sessions) == 138

by_key = {
    f"{int(row['selection_order'])}-{row['session_id']}-{row['candidate_order']}": row
    for row in extraction
}
assert len(by_key) == 120
assert set(by_key) == {row["prediction_key"] for row in outcomes}

alternatives = read_csv("alternativas_enlaces_fuentes_v1.4.csv")
assert len(alternatives) == 1
alternative = alternatives[0]
affected_source_rows = [row for row in extraction if row["session_id"] == alternative["affected_session_id"]]
alternative_frame = next(row for row in sessions if row["frame_id"] == alternative["affected_session_id"])
assert len(affected_source_rows) == int(alternative["affected_prediction_count"])
assert all(row["source_url"] == alternative["original_url"] for row in affected_source_rows)
assert alternative_frame["official_program_url"] == alternative["alternate_url"]

url_snapshot = read_csv("estado_enlaces_fuentes_2026-09-15.csv")
assert len(url_snapshot) == 218
assert any(row["source_role"] == "prediction_source" and row["url"] == alternative["original_url"]
           and row["availability"] == "http_not_found" for row in url_snapshot)

triage: list[dict[str, object]] = []
for outcome in outcomes:
    key = outcome["prediction_key"]
    prediction = by_key[key]
    urls = sum(bool(outcome[field].strip()) for field in ("primary_evidence_url", "secondary_evidence_url"))
    if outcome["judgment"] == "not_fulfilled" and urls == 0:
        priority, action = "P0", "Revisar evidencia del incumplimiento sin inferirlo de silencio"
    elif outcome["judgment"] == "indeterminate" and urls == 0:
        priority, action = "P1", "Buscar fuente admisible para el umbral congelado; documentar búsquedas negativas"
    elif outcome["judgment"] == "indeterminate":
        priority, action = "P2", "Revisar conflicto, cobertura y suficiencia de fuentes existentes"
    elif outcome["evidence_strength"] == "weak":
        priority, action = "P3", "Verificar independencia y suficiencia de la evidencia débil"
    else:
        priority, action = "P4", "Preservar y comprobar los localizadores existentes"
    triage.append({
        "prediction_key": key,
        "session_id": prediction["session_id"],
        "judgment_frozen": outcome["judgment"],
        "evidence_strength_recorded": outcome["evidence_strength"],
        "outcome_url_count": urls,
        "prediction_locator_present": int(bool(prediction["source_url"] and prediction["source_timestamp_or_page"])),
        "primary_evidence_url": outcome["primary_evidence_url"],
        "secondary_evidence_url": outcome["secondary_evidence_url"],
        "admissible_source_type_frozen": prediction["admissible_outcome_source_type"],
        "priority": priority,
        "review_action": action,
        "review_status": "initial_nonexhaustive_search" if priority == "P0" else "not_started",
        "review_note_url": "/documents/nota_revision_focal_caso_p0_v1.4.md" if priority == "P0" else "",
        "new_evidence_url": "",
        "new_evidence_accessed_at": "",
        "proposed_addendum_judgment": "",
    })

write_csv("triage_evidencia_v1.4.csv", list(triage[0]), triage)

by_session: dict[str, list[dict[str, str]]] = defaultdict(list)
session_aliases = {"CCC-2013-034": "CCC-2013-043"}
session_by_id = {row["frame_id"]: row for row in sessions}
for original_id, frame_id in session_aliases.items():
    affected = [row for row in extraction if row["session_id"] == original_id]
    frame = session_by_id[frame_id]
    assert affected and all(
        row["selection_order"] == frame["selection_order"]
        and row["source_url"] == frame["official_program_url"]
        for row in affected
    ), "Alias de sesión sin correspondencia de orden y URL"
for outcome in outcomes:
    original_id = by_key[outcome["prediction_key"]]["session_id"]
    by_session[session_aliases.get(original_id, original_id)].append(outcome)

yield_rows: list[dict[str, object]] = []
for session in sessions:
    subset = by_session[session["frame_id"]]
    counts = Counter(row["judgment"] for row in subset)
    yield_rows.append({
        "selection_order": session["selection_order"],
        "frame_id": session["frame_id"],
        "extraction_session_id": next((old for old, new in session_aliases.items() if new == session["frame_id"]), session["frame_id"]),
        "venue": session["venue"],
        "year": session["year"],
        "period": session["period"],
        "selection_stratum": session["selection_stratum"],
        "official_program_url": session["official_program_url"],
        "content_url": session["content_url"],
        "s3_in_original_order": 1,
        "included_predictions": len(subset),
        "fulfilled": counts["fulfilled"],
        "not_fulfilled": counts["not_fulfilled"],
        "indeterminate": counts["indeterminate"],
    })

assert sum(int(row["included_predictions"]) for row in yield_rows) == 120
assert sum(int(row["included_predictions"]) > 0 for row in yield_rows) == 36
write_csv("rendimiento_sesiones_s3_v1.4.csv", list(yield_rows[0]), yield_rows)

priority_counts = Counter(row["priority"] for row in triage)
venue_counts = Counter(row["venue"] for row in yield_rows)
venue_contrib = Counter(row["venue"] for row in yield_rows if row["included_predictions"])
venue_predictions = Counter()
cell_s3 = Counter()
cell_contrib = Counter()
cell_predictions = Counter()
for row in yield_rows:
    venue_predictions[row["venue"]] += int(row["included_predictions"])
    cell = (row["period"], row["venue"])
    cell_s3[cell] += 1
    cell_contrib[cell] += int(int(row["included_predictions"]) > 0)
    cell_predictions[cell] += int(row["included_predictions"])

report = [
    "# Auditoría de evidencia y rendimiento documental v1.4",
    "",
    "**Estado:** diagnóstico derivado de los registros congelados; no hay nuevas adjudicaciones.",
    "",
    "## Evidencia que merece revisión",
    "",
    "| Prioridad | Regla | Casos |",
    "|---|---|---:|",
    f"| P0 | Incumplimiento sin URL probatoria | {priority_counts['P0']} |",
    f"| P1 | Indeterminado sin URL probatoria | {priority_counts['P1']} |",
    f"| P2 | Indeterminado con al menos una URL | {priority_counts['P2']} |",
    f"| P3 | Resuelto con evidencia débil y alguna URL | {priority_counts['P3']} |",
    f"| P4 | Resto; preservar localizadores | {priority_counts['P4']} |",
    "",
    "La ausencia de URL en un registro **no prueba** ausencia de evidencia en el mundo. Tampoco convierte automáticamente un incumplimiento en indeterminado. Cada nueva fuente debe cumplir el tipo y el umbral fijados antes de buscar desenlaces. Cualquier impugnación o cambio se documentará como adenda fechada, nunca reescribiendo el juicio v1.0.",
    "",
    "El caso P0 tiene una búsqueda inicial no exhaustiva documentada en `outputs/nota_revision_focal_caso_p0_v1.4.md`. No encontró fuente calificante, pero tampoco proporciona prueba de no ocurrencia; permanece el juicio congelado y la revisión completa está pendiente.",
    "",
    "## Sesiones S3 y productividad del corpus",
    "",
    "| Conferencia | S3 revisadas | Con al menos una predicción incluida | Predicciones incluidas |",
    "|---|---:|---:|---:|",
]
for venue in ("Black Hat USA", "CCC", "Virus Bulletin"):
    report.append(f"| {venue} | {venue_counts[venue]} | {venue_contrib[venue]} | {venue_predictions[venue]} |")
report += [
    "| **Total** | **138** | **36** | **120** |",
    "",
    "### Nueve celdas de conferencia y periodo",
    "",
    "| Periodo | Conferencia | S3 | Aportantes | Predicciones |",
    "|---|---|---:|---:|---:|",
]
for period in ("2005-2009", "2010-2014", "2015-2018"):
    for venue in ("Black Hat USA", "CCC", "Virus Bulletin"):
        cell = (period, venue)
        report.append(f"| {period} | {venue} | {cell_s3[cell]} | {cell_contrib[cell]} | {cell_predictions[cell]} |")
report += [
    "",
    "Las 102 sesiones S3 restantes no aportaron **predicciones incluidas**. Eso no significa que no hablaran del futuro: no se publica un registro individual completo de candidatos excluidos que permita verificar esa interpretación.",
    "",
    "### Correspondencia de identificador detectada",
    "",
    "Siete predicciones de la sesión de orden 34 se registraron bajo `CCC-2013-034`, pero el orden S3 congelado la denomina `CCC-2013-043`. El número de orden y la URL oficial coinciden exactamente; el título es *Security Nightmares* (2013). La tabla derivada conserva ambos identificadores. No se cambia el CSV congelado ni el juicio de ninguna predicción. Un revisor debe confirmar externamente qué identificador fue el pretendido antes de corregir metadatos en una edición futura.",
    "",
    "### URL alternativa oficial para un enlace roto",
    "",
    "El URL literal `https://media.ccc.de/v/35c3-10030-security_nightmares_0x13` aparece como fuente de predicción en siete casos de `CCC-2018-085` y devolvió 404 en la foto HTTP. El orden S3 congelado ya consigna `https://media.ccc.de/v/35c3-9685-security_nightmares_0x13` como programa oficial de la misma sesión (*Security Nightmares 0x13*, 2018); esta URL devolvió 200 el 15 de septiembre de 2026. Se publica como alternativa en `work/alternativas_enlaces_fuentes_v1.4.csv`; el URL original permanece visible y el contenido del segmento no se ha preservado ni reauditable automáticamente.",
    "",
    "## Brecha del marco original",
    "",
    "El protocolo cerrado declara 189 sesiones: 138 S3 identificables en el archivo de orden y **51 no S3 sólo como agregado** (33 Black Hat USA y 18 Virus Bulletin). El repositorio no conserva la lista de identificadores, títulos y motivos de las 51. No se puede auditar su selección fila por fila ni calcular cobertura por periodo para el marco completo. Debe reconstruirse con metadatos oficiales antes de incorporar sesiones rescatadas.",
    "",
    "## Archivos y próxima acción",
    "",
    "- `work/triage_evidencia_v1.4.csv`: los 120 casos, prioridad mecánica y columnas vacías para una revisión futura; no contiene evidencia nueva.",
    "- `work/rendimiento_sesiones_s3_v1.4.csv`: las 138 sesiones S3 del orden original y su aporte congelado.",
    "- `work/reconstruccion_marco_no_s3_template_v1.4.csv`: estructura para recuperar los 51 registros ausentes, sin filas inventadas.",
    "- `work/alternativas_enlaces_fuentes_v1.4.csv`: alternativa oficial de una URL de predicción rota, sin reemplazo silencioso.",
    "- `outputs/protocolo_ampliacion_estratificada_v1.4.md`: diseño de una ampliación separada del corpus original.",
    "",
]
(OUTPUTS / "auditoria_muestra_y_evidencia_v1.4.md").write_text("\n".join(report), encoding="utf-8", newline="\n")

if not (WORK / "reconstruccion_marco_no_s3_template_v1.4.csv").exists():
    write_csv("reconstruccion_marco_no_s3_template_v1.4.csv", [
        "frame_id", "venue", "year", "period", "title", "session_type", "official_program_url",
        "available_source_url", "availability_grade", "reason_not_s3_at_freeze", "original_frame_evidence",
        "reconstruction_source_url", "reconstructed_at", "review_status", "notes",
    ], [])

print("Auditoría v1.4: 120 casos, 138 sesiones S3; juicios v1.0 sin cambios.")
