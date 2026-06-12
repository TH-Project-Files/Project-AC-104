"""Regenerate data/AC-104-v1.2.1.csv and docs/controls_list.md from docs/controls/*.md.

The markdown control files are the source of truth for: title, category, IG,
aggregate risk, CIS/NIST mappings, layered-with, and the long-form Details text.
Assessment tracking columns (maturity scores, Assigned To, Validation Date,
Notes/Evidence) are preserved from the existing CSV by control ID.
"""
import csv
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTROLS = ROOT / "docs" / "controls"
CSV_PATH = ROOT / "data" / "AC-104-v1.2.1.csv"
LIST_PATH = ROOT / "docs" / "controls_list.md"

# new IDs inserted after these family siblings
INSERT_AFTER = {"AI-APP-14": "AI-APP-13", "AI-NET-10": "AI-NET-09", "AI-USR-12": "AI-USR-11"}

FIELD = re.compile(r"^\*\*(.+?):\*\*\s*(.*?)\s*$", re.M)


def parse_md(p: Path) -> dict:
    text = p.read_text(encoding="utf-8-sig")
    m = re.match(r"# (AI-[A-Z]+-\d+): (.+)", text.splitlines()[0])
    fields = {k: v for k, v in FIELD.findall(text)}
    details = re.search(r"## Details\n(.*?)\n---\n\*Part of", text, re.S)
    detail_text = details.group(1).strip() if details else ""
    if fields.get("Layered with"):
        detail_text += "\n\nLayered with: " + fields["Layered with"]
    return {
        "id": m.group(1),
        "title": m.group(2).strip(),
        "category": fields["Category"],
        "ig": fields["Implementation Group"],
        "risk": fields["Aggregate Risk Level"],
        "cis": fields["CIS v8 Safeguards"],
        "nist": fields["NIST CSF Subcategories"],
        "details": detail_text,
    }


def main() -> None:
    mds = {d["id"]: d for d in (parse_md(p) for p in sorted(CONTROLS.glob("AI-*.md")))}

    old_raw = CSV_PATH.read_text(encoding="utf-8-sig")
    old_rows = list(csv.reader(io.StringIO(old_raw)))
    header, old_data = old_rows[0], old_rows[1:]
    tracking = {r[0]: r[5:12] for r in old_data if r and r[0].startswith("AI-")}
    order = [r[0] for r in old_data if r and r[0].startswith("AI-")]
    for new_id, after in INSERT_AFTER.items():
        if new_id not in order:
            order.insert(order.index(after) + 1, new_id)
    missing = set(mds) - set(order)
    assert not missing, f"md controls absent from CSV order: {missing}"

    out = io.StringIO()
    w = csv.writer(out, lineterminator="\n")
    w.writerow(header)
    for cid in order:
        d = mds[cid]
        trk = tracking.get(cid, ["0", "0", "0", "0", "", "", ""])
        w.writerow([d["id"], d["category"], d["ig"], d["risk"], d["title"],
                    *trk, d["cis"], d["nist"], d["details"]])
    CSV_PATH.write_text(out.getvalue(), encoding="utf-8", newline="\n")

    lines = ["﻿# Master Controls List", "",
             "| Recommendation ID | Category | Implementation Group | Aggregate Risk Level | Description |",
             "|---|---|---|---|---|"]
    old_list = LIST_PATH.read_text(encoding="utf-8-sig")
    list_order = re.findall(r"\[(AI-[A-Z]+-\d+)\]", old_list)
    for new_id, after in INSERT_AFTER.items():
        if new_id not in list_order:
            list_order.insert(list_order.index(after) + 1, new_id)
    for cid in list_order:
        d = mds[cid]
        lines.append(f"| **[{cid}](./controls/{cid}.md)** | {d['category']} | "
                     f"{d['ig']} | {d['risk']} | {d['title']} |")
    LIST_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"regenerated: {len(order)} controls")


if __name__ == "__main__":
    main()
