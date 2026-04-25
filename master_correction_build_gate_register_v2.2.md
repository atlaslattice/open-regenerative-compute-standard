# ORC-012 Master Correction and Build Gate Register v2.2

**Document ID:** ORCS-MCBGR-001 v2.2
**Date:** April 24, 2026
**Author:** Manus (Infrastructure & Build Seat)
**Status:** 84 correction items from 11 reviews (7 reviewers), 76 unique deliverables after merging
**Classification:** Execution control document — correction and gate source of truth for ORC-012 TDD v0.2
**Lineage:** Correction Ledger v1.0 → v2.0 → Build Gate Register v2.1 → v2.2

---

## Non-Adoption Risk Statement

> **Failure to implement these controls introduces risk of unbounded cost growth, unverifiable outputs, unsafe tool execution, and inability to meet regulatory or audit requirements.**

---

## Governing Rules

> **Ground Truth Supersession Rule:** GitHub AI Review 2 supersedes all prior repository-count, module-location, and implementation-status claims. Any ORC-012 TDD section using earlier repo assumptions must be updated against Review 2 before Phase 0 approval.

> **Dependency Note:** Corrections SHALL be implemented in dependency order, not numerical order. See Global Dependency Graph below.

> **Canonical Implementation Rule:** This Register is not itself the ORC-012 TDD. It is the correction source of truth. ORC-012 TDD v0.2 must map every correction item to one of: Implemented, Deferred, Superseded, Not Applicable, or Requires Convenor Decision. No correction may disappear without status.

> **Phase 0 Gate:** Phase 1 may not begin until all Phase 0 blockers are complete or explicitly waived by Convenor decision.

> **HITL Authority Rule:** No action requiring human approval may auto-execute on timeout. The system degrades or queues, never escalates its own authority.

---

## Council Role Assignments

| Role | Seat | Primary Responsibility | Review Domain |
|------|------|----------------------|---------------|
| Build Seat | Manus | Implementation, CI/CD, repo structure | All items (executor) |
| Repo Ground Truth | GitHub AI | File verification, cleanup PRs, taxonomy | Items 5, 36, 38, 40, 51, 61-* |
| Epistemic Review | Claude | Claim verification, SourceModuleRecord audit | Items 35-41, 79 |
| Safety/Policy | Notion AI | Governance policies, permission surfaces | Items 47-60, 69-73, 80 |
| Integration/Stress | GPT | Hardening, threat model, acceptance criteria | Items 74-78, 81-84 |
| External Framing | Copilot + Grok | Readability, strategic coherence | Items 24-34, 43-45 |

---

## Global Dependency Graph (Phase 0 Critical Path)

```
Path A: Canonical Source → Verification Chain
75 (Canonical Source Decision)
 → 51 (SourceModuleRecord dataclass)
 → 5 (Repository Reference Table)
 → 69 (License/IP Clearance)
 → 17 (Verify-Before-Vault)

Path B: Observability → Transparency Chain
76 (Observability Contract)
 → 50-M (TransparencyPacket v0.2)
 → 52 (Provenance Ledger)
 → 83 (Audit Export Contract)

Path C: Security → Permissions Chain
77 (Security Threat Model)
 → 48 (MCP Permission Surface Matrix)
 → 49 (Destructive Action Policy)
 → 73 (Kill Switch Policy)
 → 80 (HITL Boundary)

Path D: Environment → Build Chain
74 (Dependency/Secret Inventory)
 → 70 (Secrets Handling Policy)
 → 71 (Data Classification Policy)
 → 7 (CI/CD green pipeline)
 → 56 (Budget v0)

Path E: Classification → Testing Chain
53 (Classifier rename: Epistemic vs Safety State)
 → 59 (10-case test matrix)
 → 78 (Acceptance Criteria per Phase)
 → 45 (Day 14 Success Gate)
```

**Critical path:** Path A must complete first (it gates Verify-Before-Build). Paths B-E can proceed in parallel once Path A item 75 is resolved.

---

## Phase 0 Blockers (26 items)

These items MUST be resolved before Phase 1 implementation begins:

| ID | Correction | Category | Severity | Owner | Status | Acceptance Test |
|----|-----------|----------|----------|-------|--------|-----------------|
| 5 | Repository Reference Table with commit SHAs | Repo Ground Truth | HIGH | Manus + GitHub AI | Accepted | Table exists with SHA per repo, verified by Claude |
| 36 | AI Studio code → HIGH severity (PARTIAL not DIRECT) | Repo Ground Truth | HIGH | Manus | Accepted | All AI Studio modules tagged PARTIAL in SourceModuleRecord |
| 38 | Branch drift / repo verification (exact paths) | Repo Ground Truth | HIGH | Manus + Claude | Accepted | Every line-count claim has file path + as-of date |
| 40 | MCP Server / Kintsugi / ACP verification | Repo Ground Truth | MEDIUM | Manus | Needs Verification | Line counts verified against actual files |
| 45 | Day 14 Success Gate (p50 <2s routing excl. model response; p95 measured not enforced) | Testing | HIGH | Manus | Accepted (edited) | Benchmark script exists, p50/p95 measured |
| 47 | Phase 0 = Constitutional Build Gate (8 required outputs) | Constitutional | CRITICAL | Manus | Accepted | All 8 outputs exist in repo |
| 48 | MCP Permission Surface Matrix (7-row) | Constitutional | CRITICAL | Manus | Accepted | Matrix document in repo, reviewed by Council |
| 49 | Destructive Action Policy (11 action types) | Constitutional | CRITICAL | Manus | Accepted | Policy document in repo, all 11 types listed |
| 50-M | TransparencyPacket v0.2 Package (merged: 4, 15, 50) | Architecture | HIGH | Manus | Accepted | Schema file with ~30 fields, version header, 7 categories |
| 51 | Verify-Before-Build + SourceModuleRecord dataclass | Repo Ground Truth | HIGH | Manus + Claude | Accepted | Python dataclass exists, populated for all extraction targets |
| 53 | Classifier rename: Epistemic vs Safety State | Architecture | CRITICAL | Manus | Blocking | All code/docs use new names, zero references to old names |
| 56 | Budget v0 from Day 1 | Implementation | HIGH | Manus | Accepted | budget_config.yaml exists with sandbox limits |
| 59 | Explicit 10-case test matrix | Testing | HIGH | Manus | Accepted | 10 test cases documented with expected outcomes |
| 60 | Permission / Approval Engine (Module 17) | Constitutional | HIGH | Manus | Accepted | Interface definition exists, stub implementation passes |
| 61-a | splitmerge420 → atlaslattice cleanup | Repo Ground Truth | HIGH | GitHub AI | In Progress | Zero references to splitmerge420 in any active repo |
| 61-b | Repo count: 6-9 load-bearing, not 3 | Repo Ground Truth | HIGH | Manus | Supersedes prior | TDD Section 3 updated with correct count |
| 61-c | aluminum-os = Royalty Runtime, NOT Constitutional Engine | Repo Ground Truth | HIGH | Manus | Supersedes prior | TDD Section 3 updated with correct module locations |
| 61-e | 144-sphere already defined in constitutional-os (INV-37) | Repo Ground Truth | MEDIUM | Manus | Supersedes prior | TDD references constitutional-os as source |
| 69 | License/IP/Provenance Clearance policy | Constitutional | CRITICAL | Manus | New — Blocking | Policy document exists, SourceModuleRecord includes license field |
| 70 | Secrets Handling Policy | Constitutional | CRITICAL | Manus | New — Blocking | .env.example exists, redaction rules documented |
| 71 | Data Classification Policy (PUBLIC/INTERNAL/SENSITIVE/RESTRICTED) | Constitutional | HIGH | Manus | New — Blocking | Classification table exists, defaults documented |
| 72 | Approval UX Definition (how Convenor approves) | Constitutional | HIGH | Manus | New — Blocking | Approval mechanism defined, test approval logged |
| 73 | Rollback/Revert + Kill Switch Policy | Constitutional | CRITICAL | Manus | New — Blocking (expanded) | Policy includes compensating actions + kill switch triggers + degradation cascade |
| 74 | Dependency / Secret Inventory | Implementation | HIGH | Manus | New — Blocking | .env.example with all required vars, no actual values committed |
| 75 | Canonical Source Decision (avoid split-brain) | Constitutional | CRITICAL | Manus (Convenor approval) | New — Blocking | Canonical Source Table exists, signed off by Convenor |
| 76 | Observability Contract | Architecture | HIGH | Manus | New — Blocking | Contract document: log format, metric names, trace IDs, error codes |

---

## Canonical Source Decision (Item 75 — Expanded)

| Data Type | Canonical Source | Sync Direction | Conflict Rule | Override Authority |
|-----------|-----------------|---------------|---------------|-------------------|
| Code & schemas | GitHub (`element-145`) | GitHub → all | GitHub wins | Build Seat |
| Governance docs | Notion (sheldonbrain) | Notion → GitHub mirror | Notion wins | Convenor |
| Build artifacts | GitHub Releases | Immutable, no sync | N/A (versioned) | Build Seat |
| Session logs & reviews | Notion (primary) | Notion → GitHub mirror | Notion wins | Any Council seat |
| Routing ontology | GitHub (`element-145/config/`) | GitHub → runtime | GitHub wins | Build Seat + Convenor |
| House specifications | Notion (primary) | Notion → GitHub mirror | Notion wins, Convenor resolves | Convenor |

---

## Security Threat Model Structure (Item 77 — Expanded)

Minimum required structure for the threat model:

| Attack Vector | Severity | Detection Mechanism | Mitigation Strategy | Recovery Path |
|--------------|----------|-------------------|-------------------|--------------|
| Prompt injection via user input | CRITICAL | Input sanitization + pattern matching | Pre-flight constraint check, input validation | Reject input, log event, alert |
| Tool abuse (unauthorized MCP calls) | CRITICAL | Permission Surface Matrix enforcement | Module 17 approval gate | Revoke tool access, rollback action |
| Malicious repo inputs (poisoned PRs) | HIGH | CI/CD validation + code review gate | Signed commits, branch protection | Revert PR, audit trail |
| Poisoned AI Studio code | HIGH | SourceModuleRecord verification | Extraction protocol, test-before-integrate | Quarantine module, flag PARTIAL |
| Credential leakage (logs/packets) | CRITICAL | Secrets redaction layer | .env isolation, log scrubbing | Rotate credentials, audit exposure |
| Ledger tampering | HIGH | Hash chain verification | Append-only ledger, integrity checks | Restore from last verified hash |
| Unauthorized destructive actions | CRITICAL | Destructive Action Policy + HITL gate | Approval required, no auto-execute | Compensating action, full audit |
| API drift exploitation (stale endpoints) | MEDIUM | Nightly smoke tests | Fallback chain, LiteLLM abstraction | Switch provider, degrade tier |

---

## HITL Timeout/Escalation Behavior (Item 80 — Expanded)

| Scenario | Timeout | Escalation | Safe Fallback |
|----------|---------|-----------|---------------|
| Routine approval (non-destructive) | 24 hours | Auto-escalate to Convenor | Queue action, continue other work |
| Destructive action approval | 4 hours | Auto-escalate to Convenor | Block action, log timeout event |
| Safety-sensitive escalation | 1 hour | Auto-escalate to Convenor + notify all seats | Halt pipeline, enter safe mode |
| Budget override | 4 hours | Auto-escalate to Convenor | Use current budget tier, no override |

---

## Phase Acceptance Criteria (Item 78 — Expanded)

### Phase 0 must pass:
1. All 26 Phase 0 blockers: complete or explicitly waived by Convenor
2. Canonical Source Table exists and is Convenor-signed
3. `.env.example` complete with all required variables
4. CI/CD pipeline green on main
5. Threat model reviewed by ≥2 Council seats

### Phase 1 must pass:
1. 10-case test matrix: 100% pass
2. No destructive action executed without approval
3. TransparencyPacket valid in all routing flows
4. Budget enforcement triggers degrade (not terminate)
5. Provenance ledger replay succeeds for all logged events

### Phase 1.5 must pass:
1. Shadow Mode runs ≥48 hours with no authority
2. Routing divergence <10% from expected behavior
3. All 5 simulation scenarios completed with documented outcomes
4. Audit export produces valid JSON and CSV
5. No regression in Phase 1 acceptance criteria

---

## Merged Themes (4 packages, 8 items consolidated)

**Metabolic Layer Integration Package** (merges items 12, 21, 42):
MetabolicImpact schema (Gemini) + bridge paragraph (GPT) + House 12 governance mapping and Chennai grounding (Grok).

**TransparencyPacket v0.2 Package** (merges items 4, 15, 50):
Schema versioning (GitHub AI) + Medium complexity / 3-5 day estimate (GPT) + ~30-field governed execution event schema across 7 categories (Notion AI).

**Three-Layer Confabulation Detection Model** (merges items 13, 18, 54):
Sphere-level deferred to Phase 2 (Gemini) + two-layer structural + domain (GPT) + three-layer with Provenance (Notion AI). Phase 1: Gateway + Provenance. Phase 2: Sphere-level.

**Rollback/Revert + Kill Switch Policy** (merges items 73, GPT-78):
Compensating actions for writes (Notion AI) + kill switch triggers, authority, and degradation cascade (GPT).

---

## Key Dependencies

**TransparencyPacket v0.2** depends on:
- Item 53: Classifier rename (Epistemic vs Safety State)
- Item 60: Permission/Approval Engine
- Item 56: Budget v0
- Item 12-M: Metabolic Layer Integration Package
- Item 52: Provenance Ledger abstraction
- Item 76: Observability Contract (log/trace format alignment)

**Verify-Before-Build** depends on:
- Item 5: Repository Reference Table
- Item 51: SourceModuleRecord dataclass
- Items 61-b/c/d/e: GitHub Ground Truth corrections
- Item 69: License/IP clearance
- Item 75: Canonical Source Decision

**Eastern Review Flags** depend on:
- Item 61-d: Recognition that `eastern-dragonseek/` exists (PARTIAL)
- Item 61-b: Corrected repo taxonomy
- Corrected routing YAML

**Phase 0 Constitutional Build Gate** depends on:
- Item 75: Canonical Source Decision (must know where truth lives before producing outputs)
- Item 74: Dependency/Secret Inventory (must know what's needed before building)
- Item 77: Security Threat Model (must know threats before defining permissions)

---

## Complete Register — All 84 Items

### GitHub AI Review 1 (8 items) — Execution Realism

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 1 | +40% schedule buffer on all estimates | Documentation | MEDIUM | Accepted | 0 | Manus | All timeline tables include buffer column |
| 2 | 3-tier testing strategy (unit/integration/constitutional) | Testing | HIGH | Accepted | 1 | Manus | Test strategy document with 3 tiers defined |
| 3 | Conversation Code Liberation protocol for AI Studio code | Implementation | HIGH | Accepted | 0-1 | Manus | Protocol document + extraction script exists |
| 4 | TransparencyPacket schema versioning | Architecture | — | **Merged → 50-M** | — | — | — |
| 5 | Repository Reference Table with commit SHAs | Repo Ground Truth | HIGH | Accepted | 0 | Manus + GitHub AI | Table exists with SHA per repo |
| 6 | Operational gap analysis section needed | Documentation | MEDIUM | Accepted | 0 | Manus | Section exists in TDD |
| 7 | CI/CD from Day 1 (green pipeline) | Implementation | HIGH | Accepted | 0 | Manus | GitHub Actions green on main |
| 8 | ADR-0002 for 144-sphere system | Documentation | MEDIUM | Accepted | 0 | Manus | ADR-0002.md in repo |

### Gemini (5 items) — Architectural Precision

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 9 | Two-pass classification: fast pre-screen + async deep scoring | Architecture | HIGH | Accepted | 1 | Manus | Two-pass flow in routing graph |
| 10 | Async scoring with callback/polling for Deep Path | Architecture | MEDIUM | Accepted | 1-2 | Manus | Async handler in routing module |
| 11 | House 12 v1.3 alignment edits | Constitutional | MEDIUM | Accepted | 1 | Manus | TDD references v1.3 provisions |
| 12 | MetabolicImpact data model integration | Architecture | — | **Merged → 12-M** | — | — | — |
| 13 | Sphere-level confabulation detection | Architecture | — | **Merged → 54-M** | — | — | — |

### GPT Review 1 (10 items) — Production Readiness

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 14 | Integration complexity underestimated | Documentation | MEDIUM | Accepted | 0 | Manus | Risk register includes integration friction |
| 15 | TransparencyPacket reclassified to Medium (3-5 days) | Architecture | — | **Merged → 50-M** | — | — | — |
| 16 | Progressive 144-sphere rollout (12→36-48→144) | Architecture | HIGH | Accepted | 1-3 | Manus | Rollout plan in TDD with phase gates |
| 17 | Verify-Before-Vault stronger definition | Constitutional | HIGH | Accepted | 1 | Manus | Cross-model-family + non-conflicted rule in code |
| 18 | Confabulation Detection two-layer model | Architecture | — | **Merged → 54-M** | — | — | — |
| 19 | Budget enforcement graceful degradation | Implementation | HIGH | Accepted | 1-2 | Manus | Degradation tiers in budget_config.yaml |
| 20 | Failure Modes & Recovery section (5 modes) | Architecture | HIGH | Accepted | 0-1 | Manus | Section in TDD with recovery chains |
| 21 | Metabolic Layer bridge paragraph | Documentation | — | **Merged → 12-M** | — | — | — |
| 22 | Simulation Mode + Shadow Mode + Audit Export | Implementation | MEDIUM | Accepted | 1.5-2 | Manus | Feature flags for sim/shadow modes |
| 23 | "Demonstrates core feasibility" (not "proves the thesis") | Documentation | LOW | Accepted | 0 | Manus | Language updated in all docs |

### Copilot (11 items) — External Readability

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 24 | "Why Python?" one-liner at top | Documentation | LOW | Accepted | 0 | Manus | One-liner in TDD Section 1 |
| 25 | Eastern Review purpose statement | Documentation | MEDIUM | Accepted | 0 | Manus | Statement in TDD Section 11 |
| 26 | A2A timeline conditional on UWS reuse | Documentation | MEDIUM | Accepted | 0 | Manus | Conditional language in timeline |
| 27 | Civic Layer generalization statement | Documentation | LOW | Accepted | 0 | Manus | Statement decouples from UWS |
| 28 | Cross-provider API drift risk | Architecture | HIGH | Accepted | 1-2 | Manus | Nightly smoke test + fallback chain defined |
| 29 | One-sentence Element 145 definition | Documentation | MEDIUM | Accepted | 0 | Manus | Definition in TDD opening paragraph |
| 30 | ADK graph diagram (ASCII/Mermaid) | Documentation | MEDIUM | Accepted | 0 | Manus | Diagram in TDD Section 7 |
| 31 | Test coverage note per sprint | Testing | MEDIUM | Accepted | 1-3 | Manus | Coverage targets in sprint plans |
| 32 | Phase 0 environment setup | Implementation | — | Already Addressed | — | — | — |
| 33 | Rust migration path elevation | Documentation | LOW | Accepted | 0 | Manus | Visible in TDD risk register |
| 34 | "What Success Looks Like at Day 14" MVP definition | Testing | HIGH | Accepted | 0 | Manus | MVP definition in TDD Section 16 |

### Claude (7 items) — Epistemic Rigor

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 35 | Math reconciliation (29 vs 16 modules) | Documentation | MEDIUM | Accepted | 0 | Manus | Three-framings table in TDD |
| 36 | AI Studio code → HIGH severity | Repo Ground Truth | HIGH | Accepted | 0 | Manus | All AI Studio modules tagged PARTIAL |
| 37 | Timeline: Phase 1 prototype 2-3 weeks; Phase 1-3 integrated 60-90 days | Documentation | MEDIUM | Accepted (edited) | 0 | Manus | Distinction in TDD timeline section |
| 38 | Branch drift / repo verification | Repo Ground Truth | HIGH | Accepted | 0 | Manus + Claude | File paths + as-of dates for all claims |
| 39 | Remove "Daavud's preference" attribution | Documentation | LOW | Accepted | 0 | Manus | Technical case only, no personal attribution |
| 40 | MCP Server / Kintsugi / ACP verification | Repo Ground Truth | MEDIUM | Needs Verification | 0 | Manus | Line counts verified against files |
| 41 | Seat-by-seat review questions for Council | Documentation | LOW | Accepted | 0 | Manus | Questions distributed to Council |

### Grok (5 items) — Strategic Coherence

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 42 | Metabolic Layer connection paragraph | Documentation | — | **Merged → 12-M** | — | — | — |
| 43 | House 12 Governance Primitives Mapping table | Constitutional | HIGH | Accepted | 0 | Manus | Table in TDD Section 4 |
| 44 | Minor clarifications (144-sphere + Chennai) | Documentation | LOW | Accepted | 0 | Manus | Clarifications in TDD |
| 45 | Day 14 Success Gate: p50 <2s routing excl. model; p95 measured not enforced | Testing | HIGH | Accepted (edited) | 0 | Manus | Benchmark script with p50/p95 |
| 46 | Scrap 1 hardware deployment note | Implementation | LOW | **Deferred** to Phase 4 | 4+ | — | — |

### Notion AI Review 1 (14 items) — Constitutional Completeness

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 47 | Phase 0 = Constitutional Build Gate | Constitutional | CRITICAL | Accepted | 0 | Manus | 8 outputs in repo |
| 48 | MCP Permission Surface Matrix (7-row) | Constitutional | CRITICAL | Accepted | 0 | Manus | Matrix reviewed by Council |
| 49 | Destructive Action Policy (11 types) | Constitutional | CRITICAL | Accepted | 0 | Manus | Policy in repo |
| 50 | TransparencyPacket v0.2 schema | Architecture | — | **Merged → 50-M** | — | — | — |
| 51 | Verify-Before-Build + SourceModuleRecord | Repo Ground Truth | HIGH | Accepted | 0 | Manus + Claude | Dataclass populated |
| 52 | Provenance Ledger abstraction (pluggable) | Architecture | HIGH | Accepted | 1 | Manus | JSONL backend works, PostgreSQL interface defined |
| 53 | Classifier rename: Epistemic vs Safety State | Architecture | CRITICAL | Blocking | 0 | Manus | Zero old-name references |
| 54 | Three-layer confabulation | Architecture | — | **Merged → 54-M** | — | — | — |
| 55 | Eastern Review flags in Phase 1 YAML | Constitutional | MEDIUM | Accepted | 1 | Manus | Flags in routing YAML |
| 56 | Budget v0 from Day 1 | Implementation | HIGH | Accepted | 0 | Manus | budget_config.yaml exists |
| 57 | State recovery / checkpointing in Phase 1 | Implementation | MEDIUM | Accepted | 1 | Manus | Run IDs + node-level state |
| 58 | Dashboard not in critical path (CLI/JSON first) | Architecture | MEDIUM | Accepted | 1 | Manus | CLI output before any UI |
| 59 | Explicit 10-case test matrix | Testing | HIGH | Accepted | 0 | Manus | 10 cases documented |
| 60 | Permission / Approval Engine (Module 17) | Constitutional | HIGH | Accepted | 0-1 | Manus | Interface + stub |

### GitHub AI Review 2 — Ground Truth (8 items)

> **These items supersede prior claims. See Ground Truth Supersession Rule.**

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 61-a | splitmerge420 → atlaslattice cleanup | Repo Ground Truth | HIGH | In Progress | 0 | GitHub AI | Zero splitmerge420 references |
| 61-b | Repo count: 6-9 load-bearing, not 3 | Repo Ground Truth | HIGH | Supersedes prior | 0 | Manus | TDD updated |
| 61-c | aluminum-os = Royalty Runtime, NOT Constitutional Engine | Repo Ground Truth | HIGH | Supersedes prior | 0 | Manus | TDD updated |
| 61-d | Eastern Review = PARTIAL (eastern-dragonseek/ exists) | Repo Ground Truth | MEDIUM | Supersedes prior | 0 | Manus | TDD updated |
| 61-e | 144-sphere defined in constitutional-os (INV-37) | Repo Ground Truth | MEDIUM | Supersedes prior | 0 | Manus | TDD references constitutional-os |
| 61-f | 144-sphere-ontology repo missing | Repo Ground Truth | MEDIUM | Accepted | 1 | Manus | Repo created or formalized |
| 61-g | 52 AI Studio codebases not in GitHub | Repo Ground Truth | LOW | Accepted | 1+ | Manus | Acknowledged in TDD, future work |
| 61-h | 6-cluster repo taxonomy | Repo Ground Truth | MEDIUM | Accepted | 0 | Manus | Taxonomy in TDD Section 3 |

### Notion AI Review 2 — Structural Edits (5 policy items)

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 69 | License/IP/Provenance Clearance | Constitutional | CRITICAL | New — Blocking | 0 | Manus | SourceModuleRecord includes license field |
| 70 | Secrets Handling Policy | Constitutional | CRITICAL | New — Blocking | 0 | Manus | .env.example + redaction rules |
| 71 | Data Classification Policy | Constitutional | HIGH | New — Blocking | 0 | Manus | Classification table with defaults |
| 72 | Approval UX Definition | Constitutional | HIGH | New — Blocking | 0 | Manus | Mechanism defined, test approval logged |
| 73 | Rollback/Revert + Kill Switch Policy (expanded w/ GPT merge) | Constitutional | CRITICAL | New — Blocking (expanded) | 0 | Manus | Compensating actions + kill switch + degradation cascade |

### GPT Review 2 — Build Hardening (7 new items + 2 edits)

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 74 | Dependency / Secret Inventory | Implementation | HIGH | New — Blocking | 0 | Manus | .env.example with all required vars |
| 75 | Canonical Source Decision (avoid split-brain) | Constitutional | CRITICAL | New — Blocking | 0 | Manus (Convenor) | Canonical Source Table, Convenor sign-off (see expanded table above) |
| 76 | Observability Contract | Architecture | HIGH | New — Blocking | 0 | Manus | Contract doc: logs, metrics, traces, error codes |
| 77 | Security Threat Model | Constitutional | CRITICAL | New — Blocking | 0 | Manus | ≥8 attack vectors with severity, detection, mitigation, recovery (see expanded table above) |
| 78 | Acceptance Criteria per Phase | Testing | HIGH | New — Blocking | 0 | Manus | ≥5 pass/fail conditions per phase (see expanded criteria above) |
| 79 | External Citation / Claim Verification Gate | Documentation | HIGH | New — Blocking | 0 | Manus | Verification status tag per factual claim |
| 80 | Human Review / HITL Boundary | Constitutional | HIGH | New — Blocking | 0 | Manus | HITL boundary table + timeout/escalation behavior (see expanded table above) |

**Edits applied to existing items:**
- Item 45: Latency target softened to "p50 <2s routing excl. model response; p95 measured not enforced during Phase 1"
- Item 37: Timeline distinguished as "Phase 1 prototype: 2-3 weeks; Phase 1-3 integrated system: 60-90 days"

### GPT Review 3 — Final Tightening (6 edits + 4 new items)

**Tightening edits applied to existing items:**
- T1: Global Dependency Graph added (see section above)
- T2: Council Role Assignments added (see section above)
- T3: Item 77 expanded with minimum 8-vector structure (see expanded table above)
- T4: Item 75 expanded with explicit options, sync direction, conflict rules (see expanded table above)
- T5: Item 78 expanded with sample Phase 0/1/1.5 acceptance criteria (see section above)
- T6: Item 80 expanded with timeout/escalation behavior (see expanded table above)

**New items:**

| ID | Correction | Category | Severity | Status | Phase | Owner | Acceptance Test |
|----|-----------|----------|----------|--------|-------|-------|-----------------|
| 81 | Shadow Mode Validation Gate | Testing | HIGH | New | 1.5 | Manus | System runs ≥48h with no authority, ≥90% routing alignment before real control |
| 82 | Simulation Coverage Requirement | Testing | HIGH | New | 1.5 | Manus | 5 mandatory scenarios (ambiguity, exhaustion, failure, hallucination, denial) documented |
| 83 | Audit Export Contract | Architecture | MEDIUM | New | 1-2 | Manus | JSON + CSV export from Provenance Ledger, format in Observability Contract |
| 84 | Non-Adoption Risk Note | Documentation | LOW | New | 0 | Manus | Statement in register opening section (see above) |

---

## Summary Statistics

| Metric | v2.0 | v2.1 | v2.2 |
|--------|------|------|------|
| Total correction items | 73 | 80 | **84** |
| Merged items | 6 → 3 | 8 → 4 | 8 → 4 |
| Unique deliverables | 67 | 72 | **76** |
| Phase 0 blockers | 19 | 26 | **26** |
| Tightening edits | — | — | **6** |
| New items (this version) | — | 7 | **4** |
| Contradictions | 0 | 0 | **0** |

| Category | Count |
|----------|-------|
| Constitutional / Governance | 23 |
| Repo Ground Truth | 14 |
| Architecture | 14 |
| Implementation | 10 |
| Testing | 11 |
| Documentation | 16 |
| Deferred / Future | 1 |

| Reviewer | Reviews | Items | Focus |
|----------|---------|-------|-------|
| GitHub AI | 2 | 16 | Execution realism + ground truth |
| Gemini | 1 | 5 | Architectural precision |
| GPT | **3** | **21 + 2 edits + 6 tightenings** | Production readiness + build hardening + final tightening |
| Copilot | 1 | 11 | External readability |
| Claude | 1 | 7 | Epistemic rigor |
| Grok | 1 | 5 | Strategic coherence |
| Notion AI | 2 | 19 | Constitutional completeness + build control |

---

*This Master Correction and Build Gate Register was produced by Manus (Infrastructure & Build Seat) on April 24, 2026. It incorporates 84 correction items from 11 reviews by 7 reviewers, with zero contradictions. It is the execution control source of truth for ORC-012 TDD v0.2 and the `atlaslattice/element-145` build.*
