#!/usr/bin/env python3
"""Genera hojas ciegas para la validación independiente preregistrada."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTRACTION = ROOT / "work" / "registro_extraccion_congelado_v1.0.csv"
EVALUATION = ROOT / "work" / "evaluacion_desenlaces_v1.0.csv"
OUTPUT = ROOT / "work" / "doble_codificacion"
SEED = "cyber-predictions-audit-double-code-v1.1"
SAMPLE_SIZE = 30


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def prediction_key(row: dict[str, str]) -> str:
    return f"{int(row['selection_order'])}-{row['session_id']}-{row['candidate_order']}"


def sha256(path: Path) -> str:
    if path == EXTRACTION:
        payload = path.read_bytes()
    else:
        payload = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    extraction = read_csv(EXTRACTION)
    evaluation = read_csv(EVALUATION)
    eval_keys = {row["prediction_key"] for row in evaluation}
    if len(extraction) != 120 or len(evaluation) != 120:
        raise SystemExit("Se esperaban exactamente 120 filas en cada registro.")

    for row in extraction:
        row["prediction_key"] = prediction_key(row)
    extraction_keys = {row["prediction_key"] for row in extraction}
    if extraction_keys != eval_keys:
        raise SystemExit("Las claves de extracción y desenlaces no coinciden.")

    ranked = sorted(
        extraction,
        key=lambda row: hashlib.sha256(
            f"{SEED}|{row['prediction_key']}".encode("utf-8")
        ).hexdigest(),
    )
    sample = ranked[:SAMPLE_SIZE]
    for row in sample:
        row.update(
            independent_judgment="",
            primary_evidence_url="",
            secondary_evidence_url="",
            evidence_date_or_period="",
            evidence_summary="",
            threshold_application="",
            conflict_or_missing_application="",
            independent_coder="",
            evaluated_at="",
        )

    outcome_fields = [
        "prediction_key", "selection_order", "session_id", "candidate_order",
        "source_url", "source_timestamp_or_page", "speaker", "verbatim_text",
        "context_text", "atomic_restatement", "subject", "population",
        "geography", "outcome", "horizon_start", "deadline", "prediction_class",
        "prediction_type", "indicator_frozen", "threshold_success_frozen",
        "threshold_contradiction_frozen", "admissible_outcome_source_type",
        "missing_conflict_rule", "independent_judgment", "primary_evidence_url",
        "secondary_evidence_url", "evidence_date_or_period", "evidence_summary",
        "threshold_application", "conflict_or_missing_application",
        "independent_coder", "evaluated_at",
    ]

    class_b = [dict(row) for row in extraction if row["prediction_class"] == "B"]
    for row in class_b:
        row.update(
            semantic_fidelity="",
            alternative_restatement="",
            rationale="",
            independent_coder="",
            evaluated_at="",
        )
    atomization_fields = [
        "prediction_key", "selection_order", "session_id", "candidate_order",
        "source_url", "source_timestamp_or_page", "speaker", "verbatim_text",
        "context_text", "atomic_restatement", "horizon_literal", "deadline",
        "indicator_frozen", "threshold_success_frozen",
        "threshold_contradiction_frozen", "semantic_fidelity",
        "alternative_restatement", "rationale", "independent_coder", "evaluated_at",
    ]

    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_csv(OUTPUT / "desenlaces_muestra_ciega_v1.1.csv", sample, outcome_fields)
    write_csv(
        OUTPUT / "atomizaciones_clase_b_ciega_v1.1.csv",
        class_b,
        atomization_fields,
    )

    manifest = (
        "# Manifiesto de doble codificación v1.1\n\n"
        f"- Semilla: `{SEED}`\n"
        f"- Regla: ordenar las 120 claves por SHA-256 de `semilla|prediction_key` y tomar las primeras {SAMPLE_SIZE}.\n"
        f"- Registro de extracción: `{sha256(EXTRACTION)}`\n"
        f"- Registro de desenlaces: `{sha256(EVALUATION)}`\n"
        f"- Muestra de desenlaces: {len(sample)} filas.\n"
        f"- Revisión conservadora de clase B: {len(class_b)} filas.\n"
        "- Los juicios y enlaces originales no se incluyen en las hojas ciegas.\n"
    )
    (OUTPUT / "MANIFIESTO.md").write_text(manifest, encoding="utf-8", newline="\n")
    print(f"Paquete generado en {OUTPUT}")


if __name__ == "__main__":
    main()
