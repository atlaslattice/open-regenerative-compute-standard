#!/usr/bin/env python3
"""Validate Atlas Lattice's append-only research lineage and descendant/receipt rules.
Standard library only. Structural validator, not a cryptographic timestamp authority.
"""
import argparse, json, pathlib, sys, re
EVIDENCE = {"SOURCE-TRACED", "SOURCE-REPRODUCED", "CALIBRATED", "VALIDATED"}
OUTCOMES = {"PASS", "FAIL", "INCONCLUSIVE"}
HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")

def validate(obj, ancestor=None):
    errors = []
    nodes = obj.get("nodes", [])
    receipts = obj.get("receipts", [])
    ids = [x.get("id") for x in nodes]
    if len(ids) != len(set(ids)) or any(not x for x in ids):
        errors.append("node ids must be unique and nonempty")
    lookup = {x["id"]: x for x in nodes if x.get("id")}
    for n in nodes:
        if n.get("evidence") not in EVIDENCE:
            errors.append("invalid evidence grade: " + str(n.get("id")))
        for p in n.get("parent_ids", []):
            if p not in lookup:
                errors.append("unknown parent " + str(p))
            elif p == n["id"]:
                errors.append("self-parenting node " + str(p))
        if n.get("parent_ids") and not n.get("change_summary") and n.get("type") == "model":
            errors.append("descendant model missing change_summary: " + n["id"])
    visited, stack = set(), set()
    def dfs(node):
        if node in stack:
            errors.append("cycle at " + node)
            return
        if node in visited or node not in lookup:
            return
        stack.add(node)
        for p in lookup[node].get("parent_ids", []):
            dfs(p)
        stack.remove(node)
        visited.add(node)
    for i in ids:
        if i: dfs(i)
    rids = [r.get("receipt_id") for r in receipts]
    if len(rids) != len(set(rids)):
        errors.append("duplicate receipt id")
    for r in receipts:
        if r.get("prediction_id") not in lookup:
            errors.append("receipt target missing: " + str(r.get("receipt_id")))
        if r.get("outcome") not in OUTCOMES:
            errors.append("bad receipt outcome")
        if not HEX64.fullmatch(r.get("dataset_commit_sha256") or ""):
            errors.append("missing valid dataset checksum")
        for key in ("protocol_version", "scoring_code_ref", "decided_at_utc", "independent_signoffs"):
            if not r.get(key):
                errors.append("receipt missing " + key)
    if ancestor is not None:
        old_nodes = {x["id"]: x for x in ancestor.get("nodes", [])}
        new_nodes = {x["id"]: x for x in nodes}
        for k, val in old_nodes.items():
            if k not in new_nodes:
                errors.append("deleted ancestor node: " + k)
            elif val != new_nodes[k]:
                errors.append("mutated ancestor node: " + k)
        old_r = {x["receipt_id"]: x for x in ancestor.get("receipts", [])}
        new_r = {x["receipt_id"]: x for x in receipts}
        for k, val in old_r.items():
            if k not in new_r:
                errors.append("deleted prior receipt: " + k)
            elif val != new_r[k]:
                errors.append("mutated prior receipt: " + k)
    return sorted(set(errors))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("current", type=pathlib.Path)
    ap.add_argument("--ancestor", type=pathlib.Path, help="Prior frozen lineage snapshot")
    args = ap.parse_args()
    data = json.loads(args.current.read_text())
    prior = json.loads(args.ancestor.read_text()) if args.ancestor else None
    problems = validate(data, prior)
    for issue in problems:
        print("FAIL:", issue)
    if problems: sys.exit(1)
    print("PASS structural lineage validation; no empirical validity or independent custody implied")
