import csv
import json
import os
import time
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "work" / "convalidacion_ia_v1.0" / "deepseek"
URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"
RUN_ID = "deepseek-api-2026-09-22"


JOBS = {
    "desenlaces_30.csv": {
        "fields": [
            "independent_judgment", "primary_evidence_url", "secondary_evidence_url",
            "evidence_date_or_period", "evidence_summary", "threshold_application",
            "conflict_or_missing_application", "independent_coder", "evaluated_at",
            "confidence", "evidence_sufficiency", "model_name", "model_version", "run_id",
        ],
        "rules": "independent_judgment must be fulfilled, not_fulfilled, indeterminate, or mixed.",
    },
    "busqueda_independiente_8.csv": {
        "fields": [
            "independent_judgment", "primary_evidence_url", "secondary_evidence_url",
            "evidence_date_or_period", "evidence_summary", "threshold_application",
            "conflict_or_missing_application", "independent_coder", "evaluated_at",
            "confidence", "evidence_sufficiency", "model_name", "model_version", "run_id",
            "search_log",
        ],
        "rules": (
            "independent_judgment must be fulfilled, not_fulfilled, indeterminate, or mixed. "
            "You have no web-search tool in this API call: do not claim live browsing. If the supplied record and reliable knowledge are insufficient, use indeterminate and record that limitation in search_log."
        ),
    },
    "fidelidad_semantica_30.csv": {
        "fields": [
            "semantic_fidelity", "alternative_restatement", "rationale", "independent_coder",
            "evaluated_at", "problem_type", "could_change_judgment", "confidence",
            "model_name", "model_version", "run_id",
        ],
        "rules": "semantic_fidelity must be yes, no, or uncertain. could_change_judgment must be yes or no.",
    },
}


def call_api(api_key, rows, job):
    fields = job["fields"]
    system = (
        "You are a blind non-human research validator. Apply the frozen indicators and thresholds literally. "
        "Do not infer the study aggregate or compare with other coders. Do not invent having opened URLs. "
        "Return JSON only as an object with key results containing one object per input row. "
        "Each result must contain prediction_key plus every requested response field. "
        + job["rules"]
    )
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps({"requested_fields": fields, "rows": rows}, ensure_ascii=False)},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0,
        "max_tokens": 12000,
    }
    for attempt in range(5):
        response = requests.post(
            URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=300,
        )
        if response.status_code == 200:
            body = response.json()
            content = body["choices"][0]["message"]["content"]
            parsed = json.loads(content)
            return parsed["results"], body.get("model", MODEL)
        if response.status_code not in {429, 500, 502, 503, 504}:
            raise RuntimeError(f"DeepSeek API error {response.status_code}: {response.text[:500]}")
        time.sleep(2 ** attempt)
    raise RuntimeError("DeepSeek API failed after retries")


def main():
    api_key = os.environ["DEEPSEEK_API_KEY"]
    for filename, job in JOBS.items():
        path = BASE / filename
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fieldnames = reader.fieldnames
            rows = list(reader)
        output = []
        model_version = MODEL
        for start in range(0, len(rows), 5):
            batch = rows[start:start + 5]
            results, model_version = call_api(api_key, batch, job)
            by_key = {item["prediction_key"]: item for item in results}
            if set(by_key) != {row["prediction_key"] for row in batch}:
                raise RuntimeError(f"Key mismatch in {filename} batch {start // 5 + 1}")
            for row in batch:
                result = by_key[row["prediction_key"]]
                for field in job["fields"]:
                    row[field] = str(result.get(field, ""))
                row["independent_coder"] = "DeepSeek (AI)"
                row["evaluated_at"] = "2026-09-22"
                row["model_name"] = "DeepSeek"
                row["model_version"] = model_version
                row["run_id"] = RUN_ID
                output.append(row)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output)
        print(f"{filename}: {len(output)} rows; model={model_version}")


if __name__ == "__main__":
    main()
