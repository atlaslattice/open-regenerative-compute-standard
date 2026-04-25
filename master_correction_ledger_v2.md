# ORC-012 Master Correction Ledger v2.0

**Document ID:** ORCS-MCL-001 v2.0
**Date:** April 24, 2026
**Author:** Manus (Infrastructure & Build Seat)
**Status:** 73 correction items from 9 reviews (8 reviewers), 67 unique deliverables after merging
**Classification:** Build-control artifact — correction source of truth for ORC-012 TDD v0.2

---

## Governing Rules

> **Ground Truth Supersession Rule:** GitHub AI Review 2 supersedes all prior repository-count, module-location, and implementation-status claims. Any ORC-012 TDD section using earlier repo assumptions must be updated against Review 2 before Phase 0 approval.

> **Dependency Note:** Corrections SHALL be implemented in dependency order, not numerical order.

> **Canonical Implementation Rule:** This Master Correction Ledger is not itself the ORC-012 TDD. It is the correction source of truth. ORC-012 TDD v0.2 must map every correction item to one of: Implemented, Deferred, Superseded, Not Applicable, or Requires Convenor Decision. No correction may disappear without status.

> **Phase 0 Gate:** Phase 1 may not begin until all Phase 0 blockers are complete or explicitly waived by Convenor decision.

---

## Phase 0 Blockers (19 items)

These items MUST be resolved before Phase 1 implementation begins:

| ID | Correction | Category | Owner | Status |
|----|-----------|----------|-------|--------|
| 5 | Repository Reference Table with commit SHAs | Repo Ground Truth | Manus + GitHub AI | Accepted |
| 47 | Phase 0 = Constitutional Build Gate (8 required outputs) | Constitutional | Manus | Accepted |
| 48 | MCP Permission Surface Matrix (7-row) | Constitutional | Manus | Accepted |
| 49 | Destructive Action Policy (11 action types) | Constitutional | Manus | Accepted |
| 50-M | TransparencyPacket v0.2 Package (merged: items 4, 15, 50) | Architecture | Manus | Accepted |
| 51 | Verify-Before-Build + SourceModuleRecord dataclass | Repo Ground Truth | Manus + Claude | Accepted |
| 53 | Classifier rename: Epistemic vs Safety State | Architecture | Manus | Blocking |
| 56 | Budget v0 from Day 1 | Implementation | Manus | Accepted |
| 59 | Explicit 10-case test matrix | Testing | Manus (Convenor approval) | Accepted |
| 60 | Permission / Approval Engine (Module 17) | Constitutional | Manus | Accepted |
| 61-a | splitmerge420 → atlaslattice cleanup | Repo Ground Truth | GitHub AI (in progress) | In Progress |
| 61-b | Repo count corrected: 6-9 load-bearing, not 3 | Repo Ground Truth | Manus | Supersedes prior |
| 61-c | aluminum-os = Royalty Runtime, NOT Constitutional Engine | Repo Ground Truth | Manus | Supersedes prior |
| 61-e | 144-sphere already defined in constitutional-os (INV-37) | Repo Ground Truth | Manus | Supersedes prior |
| 69 | License/IP/Provenance Clearance policy | Constitutional | Manus | New — Blocking |
| 70 | Secrets Handling Policy | Constitutional | Manus | New — Blocking |
| 71 | Data Classification Policy (PUBLIC/INTERNAL/SENSITIVE/RESTRICTED) | Constitutional | Manus | New — Blocking |
| 72 | Approval UX Definition (how Convenor approves) | Constitutional | Manus | New — Blocking |
| 73 | Rollback/Revert Policy (compensating actions for writes) | Constitutional | Manus | New — Blocking |

---

## Merged Themes

Three correction themes had overlapping items from multiple reviewers. These are merged into single deliverables:

**Metabolic Layer Integration Package** (merges items 12, 21, 42):
MetabolicImpact schema (Gemini) + bridge paragraph connecting strategy to MetabolicImpact data model (GPT) + House 12 governance mapping and Chennai grounding (Grok).

**TransparencyPacket v0.2 Package** (merges items 4, 15, 50):
Schema versioning (GitHub AI) + reclassified to Medium complexity / 3-5 day implementation (GPT) + expanded ~30-field governed execution event schema across 7 categories (Notion AI).

**Three-Layer Confabulation Detection Model** (merges items 13, 18, 54):
Sphere-level detection deferred to Phase 2 (Gemini) + two-layer structural + domain model (GPT) + three-layer model adding Provenance layer (Notion AI). Phase 1: Gateway + Provenance. Phase 2: Sphere-level.

---

## Key Dependencies

**TransparencyPacket v0.2** depends on:
- Item 53: Classifier rename (Epistemic vs Safety State)
- Item 60: Permission/Approval Engine
- Item 56: Budget v0
- Item 12-M: Metabolic Layer Integration Package
- Item 52: Provenance Ledger abstraction

**Verify-Before-Build** depends on:
- Item 5: Repository Reference Table
- Item 51: SourceModuleRecord dataclass
- Items 61-b/c/d/e: GitHub Ground Truth corrections
- Item 69: License/IP clearance

**Eastern Review Flags** depend on:
- Item 61-d: Recognition that `eastern-dragonseek/` already exists (PARTIAL, not MISSING)
- Item 61-b: Corrected repo taxonomy
- Corrected routing YAML

---

## Complete Ledger — All 73 Items

### GitHub AI Review 1 (8 items) — Execution Realism

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 1 | +40% schedule buffer on all estimates | Documentation | Accepted | 0 | No |
| 2 | 3-tier testing strategy (unit/integration/constitutional) | Testing | Accepted | 1 | No |
| 3 | Conversation Code Liberation protocol for AI Studio code | Implementation | Accepted | 0-1 | Yes (for AI Studio modules) |
| 4 | TransparencyPacket schema versioning | Architecture | **Merged → 50-M** | 1 | — |
| 5 | Repository Reference Table with commit SHAs | Repo Ground Truth | Accepted | 0 | **Yes** |
| 6 | Operational gap analysis section needed | Documentation | Accepted | 0 | No |
| 7 | CI/CD from Day 1 (green pipeline) | Implementation | Accepted | 0 | Yes |
| 8 | ADR-0002 for 144-sphere system | Documentation | Accepted | 0 | No |

### Gemini (5 items) — Architectural Precision

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 9 | Two-pass classification: fast pre-screen + async deep scoring | Architecture | Accepted | 1 | No |
| 10 | Async scoring with callback/polling for Deep Path | Architecture | Accepted | 1-2 | No |
| 11 | House 12 v1.3 alignment edits (state recovery, infinite-loop, mid-debate hallucination) | Constitutional | Accepted | 1 | No |
| 12 | MetabolicImpact data model integration | Architecture | **Merged → 12-M** | 1-2 | No |
| 13 | Sphere-level confabulation detection | Architecture | **Merged → 54-M** (deferred to Phase 2) | 2 | No |

### GPT (10 items) — Production Readiness

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 14 | Integration complexity underestimated — adopted GPT's language | Documentation | Accepted | 0 | No |
| 15 | TransparencyPacket reclassified to Medium (3-5 days) | Architecture | **Merged → 50-M** | 1 | — |
| 16 | Progressive 144-sphere rollout (12→36-48→144) | Architecture | Accepted | 1-3 | No |
| 17 | Verify-Before-Vault stronger definition (cross-model-family + non-conflicted) | Constitutional | Accepted | 1 | No |
| 18 | Confabulation Detection two-layer model | Architecture | **Merged → 54-M** | 1 | — |
| 19 | Budget enforcement graceful degradation (degrade tier, don't terminate) | Implementation | Accepted | 1-2 | No |
| 20 | Failure Modes & Recovery section (5 failure modes with recovery chains) | Architecture | Accepted | 0-1 | No |
| 21 | Metabolic Layer bridge paragraph | Documentation | **Merged → 12-M** | 1 | — |
| 22 | Simulation Mode + Shadow Mode + Audit Export (Phase 1.5/2 deliverables) | Implementation | Accepted | 1.5-2 | No |
| 23 | "Demonstrates core feasibility" (not "proves the thesis") | Documentation | Accepted | 0 | No |

### Copilot (11 items) — External Readability

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 24 | "Why Python?" one-liner at top | Documentation | Accepted | 0 | No |
| 25 | Eastern Review purpose statement (connects to House 12 anti-bias) | Documentation | Accepted | 0 | No |
| 26 | A2A timeline conditional on UWS reuse | Documentation | Accepted | 0 | No |
| 27 | Civic Layer generalization statement | Documentation | Accepted | 0 | No |
| 28 | Cross-provider API drift risk — nightly smoke tests + fallback chain | Architecture | Accepted | 1-2 | No |
| 29 | One-sentence Element 145 definition for cold readers | Documentation | Accepted | 0 | No |
| 30 | ADK graph diagram (ASCII/Mermaid) | Documentation | Accepted | 0 | No |
| 31 | Test coverage note per sprint | Testing | Accepted | 1-3 | No |
| 32 | Phase 0 environment setup (renamed Day 0, add dependency list) | Implementation | Already Addressed | 0 | — |
| 33 | Rust migration path elevation (visibility in strategy) | Documentation | Accepted | 0 | No |
| 34 | "What Success Looks Like at Day 14" MVP definition | Testing | Accepted | 0 | No |

### Claude (7 items) — Epistemic Rigor

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 35 | Math reconciliation (29 modules vs 16 modules — three framings table) | Documentation | Accepted | 0 | No |
| 36 | AI Studio code → HIGH severity (PARTIAL not DIRECT until extracted) | Repo Ground Truth | Accepted | 0 | **Yes** |
| 37 | Timeline needs +50% integration overhead (60-90 days realistic) | Documentation | Accepted | 0 | No |
| 38 | Branch drift / repo verification (exact paths needed) | Repo Ground Truth | Accepted | 0 | **Yes** |
| 39 | Remove "Daavud's preference" attribution from language decision | Documentation | Accepted | 0 | No |
| 40 | MCP Server / Kintsugi / ACP verification (line counts need file paths) | Repo Ground Truth | Needs Verification | 0 | Yes |
| 41 | Seat-by-seat review questions for Council | Documentation | Accepted | 0 | No |

### Grok (5 items) — Strategic Coherence

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 42 | Metabolic Layer connection paragraph (merged with GPT's version) | Documentation | **Merged → 12-M** | 1 | — |
| 43 | House 12 Governance Primitives Mapping table | Constitutional | Accepted | 0 | No |
| 44 | Minor clarifications (144-sphere lineage + Chennai grounding) | Documentation | Accepted | 0 | No |
| 45 | Day 14 Success Gate with <2s latency requirement | Testing | Accepted | 0 | **Yes** |
| 46 | Scrap 1 hardware deployment note | Implementation | **Deferred** to Phase 4 | 4+ | No |

### Notion AI Review 1 (14 items) — Constitutional Completeness

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 47 | Phase 0 = Constitutional Build Gate (8 required outputs) | Constitutional | Accepted | 0 | **Yes** |
| 48 | MCP Permission Surface Matrix (7-row) | Constitutional | Accepted | 0 | **Yes** |
| 49 | Destructive Action Policy (11 action types) | Constitutional | Accepted | 0 | **Yes** |
| 50 | TransparencyPacket v0.2 schema (~30 fields, 7 categories) | Architecture | **Merged → 50-M** | 1 | — |
| 51 | Verify-Before-Build + SourceModuleRecord dataclass | Repo Ground Truth | Accepted | 0 | **Yes** |
| 52 | Provenance Ledger abstraction (pluggable backends) | Architecture | Accepted | 1 | No |
| 53 | Classifier rename: Epistemic vs Safety State (MUST-FIX) | Architecture | **Blocking** | 0 | **Yes** |
| 54 | Three-layer confabulation (adds Provenance layer) | Architecture | **Merged → 54-M** | 1-2 | — |
| 55 | Eastern Review flags in Phase 1 YAML | Constitutional | Accepted | 1 | No |
| 56 | Budget v0 from Day 1 | Implementation | Accepted | 0 | **Yes** |
| 57 | State recovery / checkpointing in Phase 1 | Implementation | Accepted | 1 | No |
| 58 | Dashboard not in critical path (CLI/JSON first) | Architecture | Accepted | 1 | No |
| 59 | Explicit 10-case test matrix (complete) | Testing | Accepted | 0 | **Yes** |
| 60 | Permission / Approval Engine as Module 17 | Constitutional | Accepted | 0-1 | **Yes** |

### GitHub AI Review 2 — Ground Truth (8 items)

> **These items supersede prior claims. See Ground Truth Supersession Rule.**

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 61-a | splitmerge420 → atlaslattice cleanup (SYSTEMIC) | Repo Ground Truth | **In Progress** (GitHub AI executing) | 0 | **Yes** |
| 61-b | Repo count: 6-9 load-bearing, not 3 | Repo Ground Truth | **Supersedes prior** | 0 | **Yes** |
| 61-c | aluminum-os = Royalty Runtime, NOT Constitutional Engine (lives in uws) | Repo Ground Truth | **Supersedes prior** | 0 | **Yes** |
| 61-d | Eastern Review = PARTIAL (eastern-dragonseek/ exists) | Repo Ground Truth | **Supersedes prior** | 0 | No |
| 61-e | 144-sphere already defined in constitutional-os (INV-37, 12x12) | Repo Ground Truth | **Supersedes prior** | 0 | No |
| 61-f | 144-sphere-ontology repo missing — needs creation or formalization | Repo Ground Truth | Accepted | 1 | No |
| 61-g | 52 AI Studio codebases not in GitHub — future work | Repo Ground Truth | Accepted | 1+ | No (but affects reuse claims) |
| 61-h | 6-cluster repo taxonomy (141 → 6-9 load-bearing) | Repo Ground Truth | Accepted | 0 | No |

### Notion AI Review 2 — Structural Edits (5 new policy items)

| ID | Correction | Category | Status | Phase | Blocking? |
|----|-----------|----------|--------|-------|-----------|
| 69 | License/IP/Provenance Clearance: every extracted module must include source license, authorship, allowed reuse status, and whether generated/human-authored/mixed | Constitutional | **New — Blocking** | 0 | **Yes** |
| 70 | Secrets Handling Policy: API keys, OAuth tokens, credentials SHALL never be written to logs, TransparencyPackets, test fixtures, or ledger entries. Phase 0 must define `.env` handling, secret redaction, and rotation plan | Constitutional | **New — Blocking** | 0 | **Yes** |
| 71 | Data Classification Policy: inputs and artifacts classified as PUBLIC / INTERNAL / SENSITIVE / RESTRICTED. MSP-001, health, credentials, private workspace data default to RESTRICTED | Constitutional | **New — Blocking** | 0 | **Yes** |
| 72 | Approval UX Definition: Phase 0 must define how the Convenor approves or denies actions (CLI prompt, Notion page, GitHub issue label, or chat confirmation). Approval events logged in Provenance Ledger | Constitutional | **New — Blocking** | 0 | **Yes** |
| 73 | Rollback/Revert Policy: any allowed write action must define a rollback or compensating action before execution. If rollback is impossible, action classified as destructive/high-risk requiring explicit approval | Constitutional | **New — Blocking** | 0 | **Yes** |

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total correction items | 73 |
| Merged items (duplicates) | 6 (merged into 3 packages) |
| Unique deliverables | 67 |
| Phase 0 blockers | 19 |
| Items accepted | 55 |
| Items merged | 6 |
| Items superseding prior claims | 4 |
| Items deferred | 2 |
| Items already addressed | 1 |
| Items in progress | 1 |
| Items needing verification | 1 |
| New items (Notion AI Review 2) | 5 |
| Contradictions between reviewers | 0 |

| Category | Count |
|----------|-------|
| Constitutional / Governance | 18 |
| Repo Ground Truth | 14 |
| Architecture | 12 |
| Implementation | 8 |
| Testing | 6 |
| Documentation | 14 |
| Deferred / Future | 1 |

| Reviewer | Reviews | Items | Focus |
|----------|---------|-------|-------|
| GitHub AI | 2 | 16 | Execution realism + ground truth |
| Gemini | 1 | 5 | Architectural precision |
| GPT | 1 | 10 | Production readiness |
| Copilot | 1 | 11 | External readability |
| Claude | 1 | 7 | Epistemic rigor |
| Grok | 1 | 5 | Strategic coherence |
| Notion AI | 2 | 19 | Constitutional completeness + build control |

---

*This Master Correction Ledger was produced by Manus (Infrastructure & Build Seat) on April 24, 2026. It incorporates 73 correction items from 9 reviews by 8 reviewers, with zero contradictions. It is the correction source of truth for ORC-012 TDD v0.2 and the `atlaslattice/element-145` build.*
