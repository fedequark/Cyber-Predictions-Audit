"""Verify recovered source snapshots against the frozen S3 selection."""

import csv
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
EXPECTED_HASHES = {
    "marco_maestro_189_sesiones_v0.9.csv": "A9C608FA24B54FFEE534500EBA46FEA1F9B4FB0C331B80C02EE6359762B68EDB",
    "disponibilidad_blackhat_2005_2013_v0.2.csv": "4D9B7B560CA715FFFA3DFBD4BC2401DBC83C725ECAB5B9B57A5264B845BAE1CB",
    "disponibilidad_blackhat_2014_2018_v0.2.csv": "0A92DE1C5E3AD9FDC8C5803DF3419E052DF0E412A4C61F691BC1389C0A0FC8CB",
    "disponibilidad_vb_30_v0.5.csv": "38BE2A60CA85E1196CA9C8F79AF9A6E869CAD7E81596E8302B1BE7083BDEAE5B",
}


def rows(name):
    with (WORK / name).open("r", encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


for name, expected in EXPECTED_HASHES.items():
    actual = hashlib.sha256((WORK / name).read_bytes()).hexdigest().upper()
    assert actual == expected, f"{name}: source bytes changed"

frame = rows("marco_maestro_189_sesiones_v0.9.csv")
s3_order = rows("orden_seleccion_s3_v0.2.csv")
assert len(frame) == 189
assert len({row["frame_id"] for row in frame}) == 189
assert len(s3_order) == 138
assert {row["frame_id"] for row in frame if row["source_grade"] == "S3"} == {
    row["frame_id"] for row in s3_order
}
non_s3 = [row for row in frame if row["source_grade"] != "S3"]
assert len(non_s3) == 51
assert Counter(row["venue"] for row in non_s3) == {"Black Hat USA": 33, "Virus Bulletin": 18}
assert Counter(row["source_grade"] for row in non_s3) == {
    "pending_archive": 29,
    "pending_manual": 4,
    "pending_paper": 17,
    "S1": 1,
}
assert all(row["title"] and row["year"] and row["official_program_url"] for row in frame)

availability = (
    rows("disponibilidad_blackhat_2005_2013_v0.2.csv")
    + rows("disponibilidad_blackhat_2014_2018_v0.2.csv")
    + rows("disponibilidad_vb_30_v0.5.csv")
)
by_id = {row["frame_id"]: row for row in availability}
assert all(row["frame_id"] in by_id for row in non_s3)
assert all(by_id[row["frame_id"]]["source_grade"] == row["source_grade"] for row in non_s3)

note = (ROOT / "outputs" / "recuperacion_marco_y_fuentes_v1.5.md").read_text(encoding="utf-8")
assert all(f"`{row['frame_id']}`" in note for row in non_s3 if row["source_grade"] == "pending_paper")
print("Marco v1.5 verificado: 189 IDs; 138 S3 coinciden; 51 no S3 con auditoría fuente.")
