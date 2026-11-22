#!/usr/bin/env python3
"""Offline, non-authorizing council benchmark review contract.

This module validates source-traceable *descriptions* of trial artifacts. It
never runs a model, attests a person, validates an external source, or decides
CANON/release status. It is intentionally standard-library only.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from typing import Any

VERSION = "orcs.council-benchmark/v0.1"
ARMS = ("single_model", "unstructured_council", "structured_council")
MODES = ("ambient", "formal_adversarial")
EVIDENCE_CLASSES = ("OBSERVED", "PUBLISHED", "DERIVED", "ASSUMED", "SPECULATIVE")
RUBRIC = ("correctness", "hallucination_resistance", "evidence_clarity", "contradiction_detection", "institutional_legibility", "usefulness")
DEFAULT_ROLES = ("calibration", "governance", "adversarial", "ecosystem", "enterprise_translation")


def _id(value: Any) -> bool:
    return isinstance(value, str) and bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}", value))


def _valid_rating(value: Any) -> bool:
    return type(value) is int and 1 <= value <= 5  # reject bool and noncanonical floats


def validate_protocol(protocol: Any) -> dict[str, Any]:
    """Check a proposed benchmark design; do not imply actual measurements."""
    errors: list[str] = []
    if not isinstance(protocol, dict):
        return {"status": "HOLD", "errors": ["protocol must be object"], "authority_effect": "NONE"}
    if protocol.get("version") != VERSION:
        errors.append("unknown protocol version")
    if protocol.get("mode") not in MODES:
        errors.append("unknown mode")
    arms = protocol.get("arms")
    if not isinstance(arms, list) or arms != list(ARMS):
        errors.append("arms must include the exact three predeclared comparisons")
    roles = protocol.get("roles")
    if not isinstance(roles, dict) or set(roles) != set(DEFAULT_ROLES) or not all(_id(v) for v in roles.values()):
        errors.append("five distinct named role assignments required")
    elif len(set(roles.values())) != len(roles):
        errors.append("role assignments must be distinct")
    tasks = protocol.get("task_ids")
    if not isinstance(tasks, list) or len(tasks) < 2 or any(not _id(t) for t in tasks) or len(set(tasks)) != len(tasks):
        errors.append("at least two unique predeclared tasks are required")
    if protocol.get("human_root_required") is not True:
        errors.append("human-root authority must be explicit")
    if protocol.get("automated_canon_promotion") is not False:
        errors.append("automated CANON promotion prohibited")
    if protocol.get("independent_first_pass") is not True:
        errors.append("independent first-pass generation required")
    if protocol.get("blinded_review") is not True:
        errors.append("blind the rating process to arm identity")
    return {"status": "HOLD" if errors else "CANDIDATE_PROTOCOL_VALIDATED_ONLY", "errors": errors,
            "authority_effect": "NONE", "executed_model_calls": 0, "claims_of_superiority": 0}


def assess_scores(protocol: Any, ratings: Any) -> dict[str, Any]:
    """Advisory paired comparison on attributed, explicitly human-reviewed ratings.

    The function never infers that an untrusted metadata label proves human
    identity. It requires *reported* human review and still labels all outputs
    unverified until authenticated externally.
    """
    check = validate_protocol(protocol)
    if check["status"] != "CANDIDATE_PROTOCOL_VALIDATED_ONLY":
        return {"status": "HOLD", "errors": check["errors"], "authority_effect": "NONE"}
    if not isinstance(ratings, list):
        return {"status": "HOLD", "errors": ["ratings must be a list"], "authority_effect": "NONE"}
    tasks = protocol["task_ids"]
    lookup: dict[tuple[str, str], dict] = {}
    errors = []
    for row in ratings:
        if not isinstance(row, dict):
            errors.append("rating row must be object")
            continue
        task = row.get("task_id")
        arm = row.get("arm")
        if task not in tasks or arm not in ARMS:
            errors.append("unknown task or arm")
            continue
        key = (task, arm)
        if key in lookup:
            errors.append("duplicate task/arm rating")
            continue
        scores = row.get("scores")
        if not isinstance(scores, dict) or set(scores) != set(RUBRIC) or not all(_valid_rating(scores[k]) for k in RUBRIC):
            errors.append("all six rubric ratings must be integer 1..5")
            continue
        refs = row.get("evidence_refs")
        if not isinstance(refs, list) or not refs or not all(isinstance(x, str) and x.strip() for x in refs):
            errors.append("nonempty evidence source pointers required")
            continue
        if row.get("review_state") != "HUMAN_RATED_UNATTESTED":
            errors.append("ratings must be explicitly declared human-rated; identity unverified")
            continue
        if row.get("private_mode_body_imported") is not False:
            errors.append("private mode evidence import prohibited")
            continue
        lookup[key] = row
    if len(lookup) != len(tasks) * len(ARMS):
        errors.append("paired complete three-arm coverage required per task")
    if errors:
        return {"status": "HOLD", "errors": sorted(set(errors)), "authority_effect": "NONE"}
    # Keep each dimension independent rather than canceling weak evidence with
    # a strong single scalar. No statistical p value from deterministic scores.
    differences = []
    for task in tasks:
        row = {"task_id": task, "difference_vs_single": {}}
        for arm in ARMS[1:]:
            row["difference_vs_single"][arm] = {
                k: lookup[(task, arm)]["scores"][k] - lookup[(task, ARMS[0])]["scores"][k]
                for k in RUBRIC
            }
        differences.append(row)
    return {"status": "UNATTESTED_HUMAN_RATINGS_ADVISORY_ONLY", "authority_effect": "NONE",
            "claims_of_superiority": 0, "tasks": len(tasks), "paired_differences": differences,
            "caution": "No measured superiority or causal effect established; verify reviewers, design, leakage and uncertainty."}


def cli() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("protocol_json", help="file with proposed protocol only")
    parser.add_argument("--ratings-json", help="optional manually collected and still-unattested rubric rows")
    args = parser.parse_args()
    with open(args.protocol_json, encoding="utf-8") as f:
        protocol = json.load(f)
    if args.ratings_json:
        with open(args.ratings_json, encoding="utf-8") as f:
            output = assess_scores(protocol, json.load(f))
    else:
        output = validate_protocol(protocol)
    print(json.dumps(output, indent=2, sort_keys=True))
    if output["status"] == "HOLD":
        raise SystemExit(2)


if __name__ == "__main__":
    cli()
