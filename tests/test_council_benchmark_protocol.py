"""Contract checks—synthetic fixtures only, no model calls or peer identity."""
from __future__ import annotations
import copy
import pytest
from tools.council_benchmark_protocol import (
    VERSION, ARMS, DEFAULT_ROLES, RUBRIC, validate_protocol, assess_scores,
)


def proto():
    return {
        "version": VERSION, "mode": "formal_adversarial",
        "arms": list(ARMS),
        "roles": {k: f"model-{n}" for n, k in enumerate(DEFAULT_ROLES)},
        "task_ids": ["case-a", "case-b"],
        "human_root_required": True, "automated_canon_promotion": False,
        "independent_first_pass": True, "blinded_review": True,
    }


def ratings():
    return [
        {"task_id": task, "arm": arm, "scores": {k: (4 if arm == "structured_council" else 3) for k in RUBRIC},
         "evidence_refs": ["synthetic:fixture/never-a-real-study"],
         "review_state": "HUMAN_RATED_UNATTESTED", "private_mode_body_imported": False}
        for task in ("case-a", "case-b") for arm in ARMS
    ]


def test_valid_protocol_is_candidate_not_authority():
    r = validate_protocol(proto())
    assert r["status"] == "CANDIDATE_PROTOCOL_VALIDATED_ONLY"
    assert r["authority_effect"] == "NONE" and r["claims_of_superiority"] == 0

@pytest.mark.parametrize("field,bad", [
    ("version", "other"), ("mode", "fictional"),
    ("arms", ["single_model", "structured_council"]),
    ("human_root_required", False), ("automated_canon_promotion", True),
    ("independent_first_pass", False), ("blinded_review", False),
    ("task_ids", ["one"]), ("task_ids", ["dup", "dup"]),
    ("roles", {x: "same" for x in DEFAULT_ROLES}),
])
def test_fail_closed_protocol_cases(field, bad):
    x = proto(); x[field] = bad
    assert validate_protocol(x)["status"] == "HOLD"


def test_non_object_protocol_held():
    assert validate_protocol(["not a dict"])["status"] == "HOLD"


def test_no_ratings_not_claimed_as_results():
    assert assess_scores(proto(), [])["status"] == "HOLD"


def test_complete_unattested_scores_are_advisory():
    r = assess_scores(proto(), ratings())
    assert r["status"] == "UNATTESTED_HUMAN_RATINGS_ADVISORY_ONLY"
    assert r["authority_effect"] == "NONE" and r["claims_of_superiority"] == 0
    assert r["paired_differences"][0]["difference_vs_single"]["structured_council"]["correctness"] == 1

@pytest.mark.parametrize("bad", [True, 3.0, float('nan'), float('inf'), 0, 6, "5"])
def test_score_requires_exact_integer_1_to_5(bad):
    r=ratings(); r[0]["scores"]["correctness"] = bad
    assert assess_scores(proto(),r)["status"] == "HOLD"


def test_duplicate_rating_is_held():
    x=ratings(); x.append(copy.deepcopy(x[0])); assert assess_scores(proto(),x)["status"] == "HOLD"


def test_unverified_model_self_grade_is_held():
    x=ratings(); x[0]["review_state"] = "MODEL_SELF_RATED"; assert assess_scores(proto(),x)["status"] == "HOLD"


def test_private_body_import_is_rejected():
    x=ratings(); x[0]["private_mode_body_imported"] = True; assert assess_scores(proto(),x)["status"] == "HOLD"


def test_no_unsupported_source_claim():
    x=ratings(); x[0]["evidence_refs"] = []; assert assess_scores(proto(),x)["status"] == "HOLD"


def test_missing_arm_held():
    assert assess_scores(proto(),ratings()[:-1])["status"] == "HOLD"
