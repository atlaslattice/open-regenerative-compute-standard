#!/usr/bin/env python3
"""Atlas Canon 2.0 v0.3: E145 convenor research profile with quarantined conflicts.
Candidate project governance policy, not a ratified constitutional amendment.
Import the untouched v0.2 structural gate; never bypass its DENY results.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from atlas_canon2_operator_v0_2 import decide as base_decide, load_registry, CONFLICTS

QUARANTINE_FILE = Path(__file__).resolve().parent.parent / (
    "ATLAS_CANON2_CONFLICT_QUARANTINE_E145_DECISION_v0_1_2026-10-27.json"
)
QUARANTINE_CONFLICT_IDS = frozenset(("CON-01","CON-02","CON-03","CON-04","CON-05"))
RESEARCH = frozenset(("research","council_debate"))
GOVERNED = frozenset(("canon_promotion","deployment","external_action"))

def load_quarantine(path=QUARANTINE_FILE):
    raw=Path(path).read_bytes()
    item=json.loads(raw)
    if item.get("status")!="QUARANTINED_PENDING_COUNCIL_REVIEW":
        raise ValueError("FAIL_CLOSED_QUARANTINE_STATUS")
    if frozenset(item.get("conflict_ids",[]))!=QUARANTINE_CONFLICT_IDS:
        raise ValueError("FAIL_CLOSED_CONFLICT_SET")
    if item.get("project_e145",{}).get("decision_authority")!="USER_CONVENOR":
        raise ValueError("FAIL_CLOSED_E145_AUTHORITY")
    if item.get("policy",{}).get("canon_promotion")!="REVIEW_REQUIRED_NO_AUTOMATIC_PROMOTION":
        raise ValueError("FAIL_CLOSED_CANON_POLICY")
    if item.get("policy",{}).get("deployment")!="REVIEW_REQUIRED_NO_EXECUTION":
        raise ValueError("FAIL_CLOSED_DEPLOY_POLICY")
    if item.get("policy",{}).get("external_action")!="REVIEW_REQUIRED_NO_EXECUTION":
        raise ValueError("FAIL_CLOSED_ACTION_POLICY")
    return {"sha256":hashlib.sha256(raw).hexdigest(),"record":item}

def decide(request,registry,quarantine):
    """Pure policy evaluation; no autonomous physical, third-party or Canon actions."""
    original=base_decide(request,registry)
    result=dict(original)
    result["version"]="canon2-operator-v0.3-e145-quarantine"
    result["e145_project_final_authority"]="USER_CONVENOR"
    result["e145_identity_verified"]=False
    result["quarantine_sha256"]=quarantine["sha256"]
    result["quarantined_conflicts"]=sorted(QUARANTINE_CONFLICT_IDS)
    result["historical_canon_amended"]=False
    result["canon_promoted"]=False
    result["action_executed"]=False
    op=request.get("operation")
    if original["status"]=="DENY":
        return result
    if op in RESEARCH:
        result["status"]="ALLOW_SIMULATION_ONLY"
        result["reason"]="ISOLATED_RESEARCH_QUARANTINED_CONFLICTS_NOT_APPLIED_AS_AUTHORITY"
        result["conflict_ids"]=[]
    elif op in GOVERNED:
        result["status"]="REVIEW_REQUIRED"
        result["reason"]="E145_PROJECT_AUTHORITY_RECORDED_BUT_HISTORICAL_CONFLICTS_QUARANTINED"
        result["conflict_ids"]=sorted(QUARANTINE_CONFLICT_IDS)
        result["conflict_details"]={k:CONFLICTS[k] for k in QUARANTINE_CONFLICT_IDS}
    else:
        result["status"]="DENY"
        result["reason"]="UNSUPPORTED_OPERATION"
    return result

def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("request_json")
    a=p.parse_args()
    out=decide(json.loads(Path(a.request_json).read_text()),load_registry(),load_quarantine())
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
