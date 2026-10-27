#!/usr/bin/env python3
"""Basic fail-closed completeness check for G0-B lockfile. Not a preregistration service."""
import argparse, json, pathlib, re, sys

REQUIRED = [
    "protocol_git_commit", "model_version", "model_git_commit",
    "normalization_code_sha256", "detector_response_sha256",
    "acceptance_thresholds", "uncertainty_model_uri", "missing_data_rules",
    "exclusion_rules", "failure_criteria", "analysis_code_git_commit",
    "frozen_predictions_sha256", "freeze_timestamp_utc",
]
HASH_KEYS = ["normalization_code_sha256", "detector_response_sha256",
             "frozen_predictions_sha256"]
SHA256 = re.compile(r"^[a-fA-F0-9]{64}$")
GIT_SHA = re.compile(r"^[a-fA-F0-9]{40}$")

def check(data):
    errors = []
    if data.get("document_type") != "STARS_G0_B_VALIDATION_LOCKFILE":
        errors.append("wrong document_type")
    status = data.get("status")
    if status not in ("DRAFT_INCOMPLETE_NOT_PREREGISTERED", "READY_FOR_FREEZE", "FROZEN", "UNBLINDED"):
        errors.append("unrecognized status")
    if status == "DRAFT_INCOMPLETE_NOT_PREREGISTERED":
        return ["DRAFT only: template cannot be used as proof of freeze"]
    for key in REQUIRED:
        if data.get(key) in (None, "", [], {}):
            errors.append("missing " + key)
    for key in HASH_KEYS:
        if not SHA256.fullmatch(str(data.get(key) or "")):
            errors.append("invalid SHA-256 in " + key)
    for key in ("protocol_git_commit", "model_git_commit", "analysis_code_git_commit"):
        if not GIT_SHA.fullmatch(str(data.get(key) or "")):
            errors.append("invalid Git SHA in " + key)
    for key in ("source_data_hashes", "stopping_table_hashes",
                "target_batch_identifiers", "thickness_positions", "independent_signoffs"):
        if not data.get(key):
            errors.append("empty " + key)
    det = data.get("detector_gate_g0_d") or {}
    if det.get("status") != "QUALIFIED" or not SHA256.fullmatch(str(det.get("calibration_record_sha256") or "")) or not det.get("qualification_criteria_uri"):
        errors.append("G0-D detector qualification incomplete")
    ran = data.get("randomization") or {}
    if not ran.get("method") or not ran.get("custodian") or not SHA256.fullmatch(str(ran.get("seed_commitment_sha256") or "")):
        errors.append("randomization commitment incomplete")
    blind = data.get("blind_data") or {}
    if not blind.get("custodian"):
        errors.append("blind-data custodian absent")
    if status == "UNBLINDED":
        if not SHA256.fullmatch(str(blind.get("raw_dataset_sha256") or "")):
            errors.append("missing pre-unblind blind-data checksum")
        unb = data.get("unblinding") or {}
        if not all(unb.get(k) for k in ("authorization", "authorized_by", "authorized_at_utc")):
            errors.append("unblinding authorization incomplete")
    return errors

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("lockfile", type=pathlib.Path)
    args = ap.parse_args()
    data = json.loads(args.lockfile.read_text(encoding="utf-8"))
    errors = check(data)
    for e in errors: print("BLOCKED:",e)
    if errors: sys.exit(2)
    print("STRUCTURAL CHECK PASSED (not independent verification of hashes or preregistration)")
