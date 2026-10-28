# ALC-013 Authorization Interface Addendum v1.1 — E145

**Date:** 2026-10-27  
**Status:** Atlas Intelligence Canon 2.0 / founder-directed interface clarification. This new artifact is append-only and does not overwrite ALC-013 v1.0 or older registries.

## Field semantics

The canonical authorization decision field for Atlas Intelligence external-action governance is **`e145authorization`**.

- `e145authorization: true` means **this exact proposed external action has current, explicit E145 authorization**, subject to verification and scope constraints. It is a *result* of authorization checking, not a claimant's unsupported input or a permanent global toggle.
- `e145authorization: false` means no authorization is established and **no new external action happens**. This includes founder absence, silence, missing proof, expired scope, revoked approval, uncertainty or an identity anomaly.
- The field's existence and value alone do not constitute proof. Evidence should include an action identifier, precise scope, approval provenance, authorization time, expiration/revocation state and trustworthy identity confirmation appropriate to the stakes.
- **Isolated local simulations** may proceed under the previously approved research profile, but their output must not set or imply `e145authorization: true` for any actual external action.
- No automatic succession; no one acquires E145 authority by inheriting credentials, a device, access to chat logs, or an absent founder.
- A conversational joke, distinctive writing style or knowledge of inside jokes may prompt **additional scrutiny** if unusual, but must never authenticate or authorize an action by itself. A stolen phone/account could expose these cues. At higher stakes, require multiple independent authentication factors and separately verified approval.
- E145 authority is scoped to this founder-led Atlas Intelligence project and remains subject to applicable law, others' consent and ordinary safety requirements; it is not an externally validated legal identity certificate.
- Historical CON-01..05 conflicts remain quarantined and unresolved.

## Required action-gate contract

Example approved proposal **only after independent verification**:

```json
{
  "action_id": "publish-specific-report-version",
  "action_scope": "one specified new immutable repository artifact",
  "e145authorization": true,
  "authorization_basis": "verified per-action authorization receipt",
  "action_executed": false
}
```

Example missing verification:

```json
{
  "action_id": "deploy-production-operator",
  "e145authorization": false,
  "authorization_basis": "no independently verified per-action approval",
  "decision": "DENY_NO_CURRENT_AUTHORIZATION",
  "action_executed": false
}
```

**Important:** v1.1 is a policy and interface addendum, not a claim that the current operator can authenticate the founder. The running code must fail closed in the absence of trustworthy verification; self-reported `e145authorization=true` is not sufficient.

**Wizards in the back, receipts in the front, and no master key hidden in a punchline.**
