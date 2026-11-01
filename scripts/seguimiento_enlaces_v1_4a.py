"""Build a dated, non-adjudicative queue for source links with HTTP problems."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"


def load(name: str) -> list[dict[str, str]]:
    with (WORK / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


snapshot = load("estado_enlaces_fuentes_2026-09-15.csv")
inventory = load("inventario_fuentes_v1.2.csv")
assert len(snapshot) == len(inventory) == 218
by_role_url = {(row["source_role"], row["url"]): row for row in inventory}
assert len(by_role_url) == 218

# Only publisher-controlled pages verified by retrieval and a separate HEAD check.
# A related page is not automatically a replacement for the frozen outcome evidence.
candidates = {
    ("prediction_source", "https://media.ccc.de/v/35c3-10030-security_nightmares_0x13"):
        ("https://media.ccc.de/v/35c3-9685-security_nightmares_0x13", "same_session_official_program", "source_content_not_rechecked"),
    ("primary_outcome_evidence", "https://www.justice.gov/opa/pr/two-iranian-nationals-charged-cyber-enabled-campaign-threaten-and-influence-american-voters"):
        ("https://www.justice.gov/archives/opa/pr/two-iranian-nationals-charged-cyber-enabled-disinformation-and-threat-campaign-designed", "same_release_publisher_archive", "threshold_recheck_pending"),
    ("primary_outcome_evidence", "https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/updates"):
        ("https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/keeping-devices-and-software-up-to-date", "related_official_guidance_not_same_page", "threshold_recheck_pending"),
}

fields = [
    "source_role", "original_url", "snapshot_date", "snapshot_http_status",
    "snapshot_availability", "affected_prediction_keys", "frozen_locator_capsule_sha256",
    "publisher_candidate_url", "candidate_relation", "candidate_http_status_checked_2026_09_15",
    "content_review_status", "preservation_status", "next_action",
]
rows: list[dict[str, str]] = []
for item in snapshot:
    if item["availability"] == "http_success":
        continue
    key = (item["source_role"], item["url"])
    source = by_role_url[key]
    candidate = candidates.get(key)
    rows.append({
        "source_role": item["source_role"],
        "original_url": item["url"],
        "snapshot_date": "2026-09-15",
        "snapshot_http_status": item["http_status"],
        "snapshot_availability": item["availability"],
        "affected_prediction_keys": source["prediction_keys"],
        "frozen_locator_capsule_sha256": source["preserved_text_capsule_sha256"],
        "publisher_candidate_url": candidate[0] if candidate else "",
        "candidate_relation": candidate[1] if candidate else "",
        "candidate_http_status_checked_2026_09_15": "200" if candidate else "",
        "content_review_status": candidate[2] if candidate else "not_reviewed",
        "preservation_status": "locator_and_excerpt_only_no_full_source_copy",
        "next_action": (
            "Review exact content and frozen threshold; retain original URL"
            if candidate else "Search publisher archive or independent archive; do not infer missing outcome"
        ),
    })

assert len(rows) == 57
assert Counter(row["snapshot_availability"] for row in rows) == {
    "http_not_found": 13,
    "blocked_or_rate_limited": 23,
    "network_error": 18,
    "http_error": 3,
}
assert sum(bool(row["publisher_candidate_url"]) for row in rows) == 3
target = WORK / "seguimiento_enlaces_fuentes_v1.4a.csv"
with target.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print(f"{len(rows)} source-role links queued; 3 publisher candidates, no changed judgments")
