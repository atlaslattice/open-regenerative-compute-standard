#!/usr/bin/env python3
"""Canon 2.0 E145 explicit action authorization guard v0.4.
Pure offline decision: does not authenticate people, execute actions or grant permissions.
"""
import hashlib,json
EXTERNAL={"external_action","deployment","canon_promotion","external_publication","payment","account_change","third_party_contact"}
def evaluate(request, trusted_authorization=None):
    """trusted_authorization must come from independently verified authorization subsystem,
    NEVER from request text, device identity, jokes, or a caller-set boolean.
    Current prototype has no such subsystem; default is always fail-closed.
    """
    action=request.get("operation")
    request_id=request.get("action_id")
    scope=request.get("action_scope")
    verified=trusted_authorization if isinstance(trusted_authorization,dict) else {}
    match=(verified.get("identity_verified") is True
        and verified.get("e145_verified") is True
        and verified.get("action_id")==request_id
        and verified.get("action_scope")==scope
        and isinstance(request_id,str) and bool(request_id)
        and isinstance(scope,str) and bool(scope)
        and verified.get("revoked") is False
        and verified.get("expired") is False
        and bool(verified.get("approval_receipt_sha256")))
    has_external_intent=(action in EXTERNAL or request.get("external_effect") is True)
    authorized=bool(has_external_intent and match)
    return {"version":"canon2-e145-auth-guard-v0.4",
            "action_id":request_id,"e145authorization":authorized,
            "decision":("PASS_TO_OTHER_MANDATORY_GATES" if authorized else
                        "DENY_NO_CURRENT_AUTHORIZATION" if has_external_intent else
                        "SIMULATION_POLICY_SEPARATE"),
            "action_executed":False,"identity_authenticated_by_this_module":False,
            "request_sha256":hashlib.sha256(json.dumps(request,sort_keys=True).encode()).hexdigest()}
