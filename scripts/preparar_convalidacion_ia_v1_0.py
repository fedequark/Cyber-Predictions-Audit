#!/usr/bin/env python3
"""Prepara paquetes ciegos y reproducibles para cuatro convalidadores IA."""

from __future__ import annotations

import csv
import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
SOURCE = WORK / "doble_codificacion"
OUTPUT = WORK / "convalidacion_ia_v1.0"
MODELS = ("codex", "claude", "deepseek", "gemini")
SEED_SEARCH = "cpa-ai-search-audit-v1.0"
SEED_SEMANTIC = "cpa-ai-semantic-audit-v1.0"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def rank(seed: str, key: str) -> str:
    return hashlib.sha256(f"{seed}|{key}".encode()).hexdigest()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    outcomes = read_csv(SOURCE / "desenlaces_muestra_ciega_v1.1.csv")
    semantics = read_csv(SOURCE / "atomizaciones_clase_b_ciega_v1.1.csv")
    evaluation = {
        row["prediction_key"]: row
        for row in read_csv(WORK / "evaluacion_desenlaces_v1.0.csv")
    }
    commitment = {
        row["prediction_key"]: row
        for row in read_csv(WORK / "revision_compromiso_y_operacionalizacion_v1.4.csv")
    }
    triage = {
        row["prediction_key"]: row
        for row in read_csv(WORK / "triage_evidencia_v1.4.csv")
    }

    # La evidencia original se revela, pero no el juicio, resumen ni aplicación.
    for row in outcomes:
        evidence = evaluation[row["prediction_key"]]
        row["provided_primary_evidence_url"] = evidence["primary_evidence_url"]
        row["provided_secondary_evidence_url"] = evidence["secondary_evidence_url"]
        row["validation_mode"] = "provided_evidence"
        row["confidence"] = ""
        row["evidence_sufficiency"] = ""
        row["model_name"] = ""
        row["model_version"] = ""
        row["run_id"] = ""

    search_keys = {
        row["prediction_key"]
        for row in sorted(outcomes, key=lambda r: rank(SEED_SEARCH, r["prediction_key"]))[:8]
    }
    search_rows = []
    for source_row in outcomes:
        if source_row["prediction_key"] not in search_keys:
            continue
        row = dict(source_row)
        row["provided_primary_evidence_url"] = ""
        row["provided_secondary_evidence_url"] = ""
        row["primary_evidence_url"] = ""
        row["secondary_evidence_url"] = ""
        row["validation_mode"] = "independent_search"
        row["search_log"] = ""
        search_rows.append(row)

    modal = {
        key for key, row in commitment.items() if row.get("modal_word_in_excerpt", "").strip()
    }
    evidence_risk = {
        key for key, row in triage.items() if row.get("priority") in {"P0", "P1", "P2"}
    }
    selected: list[dict[str, str]] = []
    selected_keys: set[str] = set()
    for group in (
        [r for r in semantics if r["prediction_key"] in modal],
        sorted(
            [r for r in semantics if r["prediction_key"] in evidence_risk],
            key=lambda r: rank(SEED_SEMANTIC + "-risk", r["prediction_key"]),
        ),
        sorted(semantics, key=lambda r: rank(SEED_SEMANTIC, r["prediction_key"])),
    ):
        for row in group:
            if row["prediction_key"] not in selected_keys and len(selected) < 30:
                selected.append(dict(row))
                selected_keys.add(row["prediction_key"])
    for row in selected:
        row["problem_type"] = ""
        row["could_change_judgment"] = ""
        row["confidence"] = ""
        row["model_name"] = ""
        row["model_version"] = ""
        row["run_id"] = ""

    outcome_fields = list(outcomes[0].keys())
    search_fields = list(search_rows[0].keys())
    semantic_fields = list(selected[0].keys())
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for model in MODELS:
        model_dir = OUTPUT / model
        model_dir.mkdir(exist_ok=True)
        write_csv(model_dir / "desenlaces_30.csv", outcomes, outcome_fields)
        write_csv(model_dir / "busqueda_independiente_8.csv", search_rows, search_fields)
        write_csv(model_dir / "fidelidad_semantica_30.csv", selected, semantic_fields)
        shutil.copyfile(OUTPUT / "PROMPT.md", model_dir / "PROMPT.md")

    manifest = [
        "# Manifiesto de convalidación IA v1.0",
        "",
        f"- Modelos previstos: {', '.join(MODELS)}.",
        f"- Desenlaces con evidencia suministrada: {len(outcomes)}.",
        f"- Búsquedas independientes: {len(search_rows)}.",
        f"- Operacionalizaciones clase B: {len(selected)}.",
        f"- Semilla de búsqueda: `{SEED_SEARCH}`.",
        f"- Semilla semántica: `{SEED_SEMANTIC}`.",
        "- Las cuatro copias son idénticas al generarse; sólo debe variar la respuesta.",
        "- Esto es convalidación no humana y no satisface la doble codificación humana preregistrada.",
        "",
    ]
    for name in ("desenlaces_30.csv", "busqueda_independiente_8.csv", "fidelidad_semantica_30.csv"):
        manifest.append(f"- `{name}` (Codex): `{sha256(OUTPUT / 'codex' / name)}`")
    (OUTPUT / "MANIFIESTO.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(f"Paquetes creados en {OUTPUT}")


if __name__ == "__main__":
    main()
