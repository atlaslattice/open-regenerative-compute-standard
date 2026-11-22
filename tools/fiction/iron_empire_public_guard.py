#!/usr/bin/env python3
"""No-dependency, read-only Iron Empire source-local continuity presence gate.

Reads only already-public ORCS files. Does not claim canon ratification, access
private Play rooms or change existing story documents.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

FOLDER = Path("docs/fiction/iron_empire")
SOURCES = {
    "v04": "THE_IRON_EMPIRE_SIX_FILM_NARRATIVE_TREATMENT_v0_4_2026-10-30.md",
    "v05": "IMPERIAL_ACCOUNTING_SCANDAL_ASSASSINATION_PRINCE_ARC_v0_5_2026-10-30.md",
    "v06": "IMPERIAL_LONGEVITY_SUMERIAN_MOTIFS_AND_LOST_HISTORY_v0_6_2026-10-30.md",
    "nov06": "MARS_GARDEN_PREQUEL_FILM_II_RESTORATION_FILM_III_CONTINUITY_DELTA_2026-11-06.md",
}
# Later author-directed deltas qualify only explicit story placement.
# v0.4 must remain intact as a preserved source, not silently overwritten.
RULES = (
    ("IE-PUB-01", "v04", r"2062.*[Aa]nomalous", "2062 anomalous observation"),
    ("IE-PUB-02", "v04", r"2069.*[Dd]amaged Imperial fleet emerges unexpectedly", "2069 arrival remains unexpected"),
    ("IE-PUB-03", "v05", r"Film II.*Emperor alone lawfully authorizes publication", "Film II Emperor-authorized audit"),
    ("IE-PUB-04", "v05", r"Film III.*[Aa]ssassination of the Emperor", "Film III assassination"),
    ("IE-PUB-05", "v05", r"no accession by the end of Film V", "No Film V coronation"),
    ("IE-PUB-06", "v05", r"actual imperial accession and coronation take place in Film VI", "Film VI coronation"),
    ("IE-PUB-07", "v04", r"[Ee]nemy true species identity/naming revealed only in Film VI", "Film VI enemy self-name reveal"),
    ("IE-PUB-08", "v06", r"[Ss]uspended animation.*major partial explanation", "Stasis and longevity remain distinct"),
    ("IE-PUB-09", "nov06", r"Film II / Book 2.*partly a prequel", "Film II ancient Mars prequel"),
    ("IE-PUB-10", "nov06", r"Martian Empire.*glassed its own planet", "Ancient Mars self-glassing"),
    ("IE-PUB-11", "nov06", r"Book/Film III.*resurrect Mars through restoration/terraforming", "Film III major restoration"),
    ("IE-PUB-12", "nov06", r"former executioner.*Minister of Trees.*work with Steve", "Steve and Minister partnership"),
    ("IE-PUB-13", "nov06", r"AUTHOR-DIRECTED CONTINUITY DELTA / NOT APPLIED TO EXISTING BIBLE", "Nov 6 change not applied to older bible"),
    ("IE-PUB-14", "v05", r"additive revision note.*NOT a silent replacement", "Older v0.4 remains preserved"),
)

def audit(root: Path):
    root = root.resolve()
    docs = {}
    missing = []
    for key, name in SOURCES.items():
        path = root / FOLDER / name
        if path.is_file():
            docs[key] = path.read_text(encoding="utf-8")
        else:
            docs[key] = ""
            missing.append(str(path.relative_to(root)))
    checks = [
        {"id": id, "source": str(FOLDER / SOURCES[key]), "note": note,
         "passed": bool(re.search(pattern, docs[key], re.IGNORECASE | re.DOTALL))}
        for id, key, pattern, note in RULES
    ]
    return {
        "classification": "PUBLIC-SOURCE PRESENCE CHECK — PROPOSED FICTION, NOT CANON",
        "checks": checks, "total": len(checks),
        "passed": sum(row["passed"] for row in checks),
        "failed": sum(not row["passed"] for row in checks),
        "missing_files": missing,
        "canon_ratified": False, "private_play_imported": False, "network_called": False,
    }

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)
    result = audit(args.root)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Iron Empire public-source guard: {result['passed']}/{result['total']} passed")
        for row in result["checks"]:
            if not row["passed"]:
                print(f"FAIL {row['id']}: {row['note']}")
        for path in result["missing_files"]:
            print("MISSING FILE:", path)
    return 0 if result["failed"] == 0 and not result["missing_files"] else 1

if __name__ == "__main__":
    sys.exit(main())
