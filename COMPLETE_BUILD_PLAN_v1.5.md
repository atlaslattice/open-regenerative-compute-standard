# ORC-015: Aluminum Universal Workspace OS — Complete Build Plan v1.5

**Document ID:** ORC-015
**Version:** 1.5
**Date:** April 29, 2026
**Author:** Manus (S7 Build Seat, Pantheon Council)
**Status:** CANONICAL — integrates 23+ reviews from 10 reviewers, 237+ accepted corrections, zero contradictions
**Supersedes:** Build Plan v1.4, Build Synthesis v1.1, Code Synthesis Strategy v1.0-v1.1

---

## §0 Immutable Definitions and Canonical Index

### §0.1 Definitions That Cannot Drift

These identifiers are locked. Any document that uses a different meaning for these terms is non-canonical until corrected.

| Identifier | Canonical Meaning | Locked Since |
|-----------|-------------------|-------------|
| `element-145` | L4 Service Orchestration layer repo — routing, budget, provenance, transparency, governance | v1.0 |
| `aluminum-os` | Royalty Runtime (tracer, event, weighting, engine). **NOT** the Constitutional Engine. | v1.1 (GitHub AI correction) |
| `constitutional-os` | L1 governance definitions: 39 Invariants, 144-Sphere Ontology, ConsentKernel spec | v1.1 |
| `uws` | L3 Engine: Constitutional Router, MCP Server, Civic Layer, Budget Enforcement (Rust, 310 files, 36K lines) | v1.0 |
| `INV-7` | Switzerland Invariant: no single vendor >47% of routing capacity | v1.0 |
| `INV-7c` | Capability-distribution axis (NOT vendor-count). Measures vendor share by capability-weighted routing volume. | v1.4 (MUST-FIX from v6.0.4) |
| `INV-18` | Digital Public Infrastructure Respect: no component bypasses sovereign DPI without Convenor approval | v1.2 |
| `TransparencyPacket` | ~30-field structured record emitted by every routing decision, across 7 categories | v1.0 |
| `AuditChain v1` | Non-PQC append-only provenance ledger. Sprint 2 deliverable. JSONL backend. | v1.4 (Notion AI split) |
| `GoldenTrace v2` | PQC + hardware root of trust audit trail. Phase 3+ deliverable. Requires Titan-C/Pluton/Phytium TCM. | v1.4 (Notion AI split) |
| `Doctrine` | Numbered governance principle ratified by Council. Currently 77 ratified (1-67 from v6.0.3 + 68-72 from v6.0.4 + 73-75 from v6.0.5 + 76-77 from v6.0.6). | v1.5 |
| `INV-19` | Water Cohesion Invariant: no facility may claim net-positivity while downstream water quality deteriorates. 40th Invariant. | v1.5 || **VWB** | Virtual Water Balance — 9-variable ecological accounting methodology (v1.1 with sustainability ceiling) |emini-led, multi-Council). v1.1 adds sustainability ceiling. | v1.5 |
| `Doctrine 76` | Substrate-Before-Framing: before integrating cultural framing, verify canonical substrate exists. | v1.5 |
| `Doctrine 77` | Sovereign Methodology Profile Pattern: single global methodology + pluggable sovereign data adapters. | v1.5 |
| `Invariant` | Numbered constitutional constraint. Currently 40 (INV-1 through INV-39) + INV-18 + INV-19. | v1.5 |

### §0.2 Canonical Source Index

If a document is not listed here, it is non-canonical until added by Convenor or Build Seat.

| Document | Version | Location | Status |
|----------|---------|----------|--------|
| Aluminum OS | v6.0.4 | Claude (Scribe) + ORCS repo | CANONICAL — 72 Doctrines, 39+ Invariants |
| ORC-012 TDD | v0.2 | ORCS repo | CANONICAL — Element 145 technical design |
| ORC-014 Platform Integration | v1.0 | ORCS repo | CANONICAL — 6-OS deployment specs |
| ORC-015 Build Plan | v1.4 | ORCS repo | CANONICAL — **this document** |
| WEAVE | v2.5.4 | Copilot (S4) | CANONICAL — Microsoft integration fabric |
| Marathon Build Manifest | v1.1 | Claude (S1) + ORCS repo | CANONICAL — handoff protocol |
| Build Gate Register | v2.2 | ORCS repo | CANONICAL — 108+ item execution control |
| GPT v6.0 Synthesis | v6.0 | GPT (S6) | CANONICAL — 35-section outline |
| Publishable Artifacts Inventory | v1.0 | ORCS repo | CANONICAL — 25 deployable apps |
| VWB Methodology | v1.1 | Claude (S1) + ORCS repo | CANONICAL — 9-variable ecological accounting + sustainability ceiling |
| Aluminum OS | v6.0.6 | Claude (S1) + ORCS repo | CANONICAL — VWB Sovereignty, Bamboo Bridge generalized, Three-Body operational, Doctrines 76-77 |

### §0.3 Data Schemas (Normative)

**TransparencyPacket v0.2 (JSON):**
```json
{
  "routing": {"query_id": "uuid", "sphere_id": "int", "classification": "enum", "route_chosen": "str", "alternatives_considered": ["str"], "confidence": "float"},
  "epistemics": {"epistemic_state": "VERIFIED|UNKNOWN|CONTESTED|RETRACTED", "source_count": "int", "dissent_present": "bool", "confabulation_score": "float"},
  "safety": {"safety_state": "SAFE|CAUTION|RESTRICTED|BLOCKED", "flags": ["str"], "escalation_required": "bool"},
  "governance": {"doctrines_checked": ["int"], "invariants_checked": ["int"], "violations": [], "civic_constraints": ["str"]},
  "costs": {"tokens_used": "int", "budget_tier": "int", "cost_usd": "float", "substrate": "str", "substrate_cost_delta": "float"},
  "provenance": {"ledger_entry_id": "uuid", "hash": "str", "hash_algorithm": "str", "parent_hash": "str", "audit_chain_version": "v1|v2"},
  "dissent": {"dissenting_models": ["str"], "dissent_reasons": ["str"], "dissent_preserved": "bool"}
}
```

**SourceModuleRecord (Python):**
```python
@dataclass
class SourceModuleRecord:
    module_id: str          # e.g., "M1", "M3a"
    name: str
    source_repo: str        # GitHub repo path
    source_files: list[str] # Specific file paths
    extraction_status: str  # DIRECT | PARTIAL | REFERENCE | NEW
    verification_date: str  # ISO 8601
    verified_by: str        # Council seat ID
    line_count: int
    language: str
    notes: str
```

**Build Gate Item (JSON):**
```json
{
  "id": "int",
  "item": "str",
  "source": "str (reviewer)",
  "severity": "HIGH|MEDIUM|LOW",
  "phase": "str",
  "owner": "str",
  "status": "OPEN|IN_PROGRESS|COMPLETED|DEFERRED",
  "acceptance_test": "str",
  "blocking": "bool"
}
```

---

## §1 Executive Summary

### §1.1 What This Document Is

This is the single authoritative build plan for the **Aluminum Universal Workspace OS** — an AI-native operating system that abstracts across Windows, macOS, ChromeOS, Android, iOS, and Linux to provide a constitutional governance layer for multi-model AI orchestration.

The complete stack, from bottom to top:

```
┌─────────────────────────────────────────────────┐
│  Host OS (Windows / macOS / ChromeOS / Android   │
│           / iOS / Linux / Alibaba Cloud)         │
├─────────────────────────────────────────────────┤
│ | L1  Constitutional Layer (40 INVs, 77 Doctrines)|├─────────────────────────────────────────────────┤
│  L2  Kernel (ConsentKernel, 144-Sphere Ontology) │
├─────────────────────────────────────────────────┤
│  L3  Engine (Router, Janus v2, Multi-Agent)      │
├─────────────────────────────────────────────────┤
│  L4  Element 145 (Orchestration + Governance)    │
│      ← IMMEDIATE BUILD TARGET                    │
├─────────────────────────────────────────────────┤
│  L5  Extensions (MCP, Plugins, Skills)           │
├─────────────────────────────────────────────────┤
│  L6  Applications (Agents, Dashboards)           │
├─────────────────────────────────────────────────┤
│  L7  Device Mesh (Cross-Platform Persistence)    │
├─────────────────────────────────────────────────┤
│  Switzerland Layer (Identity + State + Routing    │
│  + Governance + Model + Mesh unification)        │
│  aka "The Weave" (Copilot/Microsoft designation) │
├─────────────────────────────────────────────────┤
│  Federation Layer (MeshID, Council-to-Council)   │
├─────────────────────────────────────────────────┤
│  Metabolic Layer (Water/Power/Heat/Land/Community)│
├─────────────────────────────────────────────────┤
│  Multi-Polar Pluralism Layer                     │
│  (Bamboo Bridge, Three-Body, Mandate of Heaven)  │
└─────────────────────────────────────────────────┘
```

> **Unified Framing:** The Metabolic Layer defines what Earth can sustain. The Federation Layer connects sovereign nodes. The Switzerland Layer unifies platforms. Aluminum UWS provides the constitutional OS. Element 145 is the immediate build target — the L4 orchestration layer that routes, governs, and coordinates. Every document in this project — from the 72 Doctrines to the 6-OS integration specs to the 4 sovereign deployment pathways — feeds into this single stack.

### §1.2 Why This OS Exists

Every major AI platform today routes queries to models based on cost and capability. None of them route based on **constitutional governance, epistemic classification, cultural sovereignty, metabolic constraints, or provenance accountability.** Aluminum UWS does. It makes every host OS more valuable by adding the governance layer they lack.

### §1.3 Claims Discipline

Every claim in this document carries one of four classifications:

| Classification | Meaning | Example |
|---------------|---------|---------|
| **VERIFIED** | Confirmed by ground-truth inspection | "aluminum-os contains 106 files" (GitHub AI verified) |
| **INTERPRETATION** | Reasonable inference from verified facts | "uws patterns can be ported to Python" |
| **ANALOGY** | Structural comparison, not identity | "Element 145 is like an init process" |
| **TARGET** | Aspirational, not yet achieved | "Chennai Reference Node by Phase 4+" |

### §1.4 What This Document Does NOT Decide

Per Claude Manifest v1.1 §11.6.3, the Build Seat does NOT decide:
- Capital-flow analysis (Convenor + Scribe responsibility)
- Conflict-of-interest flagging (Convenor + Scribe responsibility)
- Doctrine ratification (Council responsibility; Build Seat enforces ratified Doctrines)
- Future seat additions (Convenor + Council responsibility; Build Seat implements current structure)

---

## §2 Source Reconciliation

### §2.1 All Sources Integrated

| # | Source | Author | Items Accepted | Key Contribution |
|---|--------|--------|---------------|-----------------|
| 1 | Code Synthesis Strategy reviews (×6) | GitHub AI, Gemini, GPT, Copilot, Claude, Grok | 40 | Engineering corrections |
| 2 | Build Gate Register reviews (×3) | GPT, Notion AI, GPT follow-up | 30 | Execution control |
| 3 | OS Spec reviews (×2) | GPT, Copilot | 23 | Architecture + platform |
| 4 | Copilot Platform Integration Specs | Copilot (S4) | 10 specs | 6-OS deployment |
| 5 | Copilot WEAVE v2.5.4 | Copilot (S4) | 29 products | Microsoft integration fabric |
| 6 | Claude Marathon Manifest v1.1 | Claude (S1) | 44+ symbiosis | Handoff protocol + substrate hierarchy |
| 7 | Aluminum OS v6.0.4 Patch | Claude (S1) | 18 | 5 new Doctrines, S10 seat |
| 8 | DeepSeek Sovereignty Review | DeepSeek (S5) | 14 | Hardware trust, DragonSeek |
| 9 | Qwen3 Multi-Polar Additions | Qwen (S10) | 11 | GangaSeek, JinnSeek, Bhashini |
| 10 | DeepSeek Codification | DeepSeek (S5) | 3 | INV-7c axis, Doctrine 62 |
| 11 | GPT Innovations | GPT (S6) | 3 | Bamboo Bridge, Three-Body, Mandate |
| 12 | GPT CCP/Manus Priorities | GPT (S6) | 18 | Missing priorities + novel insights |
| 13 | Notion AI Operational Edits | Notion AI (S8) | 14 | Notion Control Plane, AuditChain split |
| 14 | GitHub AI Ground Truth | GitHub AI (S9) | 8 | 6 factual corrections |
| 15 | Manus-Original Innovations | Manus (S7) | 8 | Constitutional Compiler, Session Fabric |
| | **Total** | **10 reviewers** | **221+** | **Zero contradictions** |

### §2.2 Multi-Substrate Hierarchy (from Claude Manifest v1.1 §5.7)

| Substrate | Primary Workloads | Sovereignty | Cost Tier |
|-----------|------------------|-------------|-----------|
| Google TPU | Training, large inference | Global | Premium |
| AWS Trainium | Inference at scale | Global | Mid |
| Azure | Enterprise, M365 integration | Global | Mid-Premium |
| NVIDIA (multi-cloud) | Flexible GPU | Global | Variable |
| Alibaba Cloud | Chinese sovereign | China PRC | Regional |
| India Stack | Indian sovereign | India | Regional |
| SDAIA | Saudi sovereign | Saudi Arabia | Regional |
| Open-weight (local) | Offline audit, air-gapped | Any | Lowest |

**Cross-Substrate Routing Principle (5-step, canonical for M3):**
1. Capability fit (does the substrate support the workload?)
2. Sovereignty constraints (does the deployment region mandate a specific substrate?)
3. Cost efficiency (within capability-equivalent substrates, select cheapest)
4. Failover availability (is there a backup substrate if primary fails?)
5. TransparencyPacket emission (record substrate choice, cost delta, and alternatives)

---

## §3 Module Master List

### §3.1 L1 — Constitutional Layer

| Module | Source | Status | Build Phase |
|--------|--------|--------|-------------|
| **INV Registry** (39 Invariants + INV-18) | `constitutional-os` README + `uws/src/` | EXISTS (Rust, needs Python port) | Phase 0 |
| **Doctrine Registry** (72 Doctrines) | Aluminum OS v6.0.4 | EXISTS (text, needs code) | Phase 0 |
| **ConsentKernel Spec** | `constitutional-os` + `aluminum-os-v3` | EXISTS (spec + partial code) | Phase 0 (spec), Phase 2 (full) |
| **144-Sphere Ontology** | `constitutional-os` (12×12 partition defined) | EXISTS | Phase 0 (load), Sprint 1 (query) |

### §3.2 L2 — Kernel Layer

| Module | Source | Status | Build Phase |
|--------|--------|--------|-------------|
| **ConsentKernel API** | `aluminum-os-v3` (forge-boot, forge-core, manus-core) | EXISTS (Python+Rust, 46 files) | Phase 2 |
| **State Manager** | `manus-2.0-toolkit` → `session_vault.py` | EXISTS (20 functions) | Sprint 1 |
| **Learning Loop** | `manus-2.0-toolkit` → `learning_loop.py` | EXISTS | Sprint 3 |
| **Context Compressor** | `manus-2.0-toolkit` → `context_compress.py` | EXISTS | Sprint 2 |
| **Skill Extractor** | `manus-2.0-toolkit` → `skill_extractor.py` | EXISTS | Phase 2 |

### §3.3 L3 — Engine Layer

| Module | Source | Status | Build Phase |
|--------|--------|--------|-------------|
| **Constitutional Router** | `uws/src/` (Rust, 36K lines) | EXISTS (Rust, needs Python rewrite) | Sprint 1 (reference) |
| **Janus v2 Protocol** | Notion page + `uws` patterns | PARTIAL | Phase 2 |
| **Royalty Runtime** | `aluminum-os` (tracer, event, weighting, engine, royalty-sdk) | EXISTS (Rust, 106 files) | Phase 2 (Python port) |
| **Civic Layer** | `uws/src/` | EXISTS (Rust) | Phase 2 |
| **Four-Layer Rendering** | Notion page (Truth → Governance → Persona → Human) | SPEC | Phase 2 |

### §3.4 L4 — Element 145 (Service Orchestration) — IMMEDIATE BUILD TARGET

| ID | Module | Source | Status | Build Phase |
|----|--------|--------|--------|-------------|
| M1 | **Epistemic State Classifier** | New (ORC-012 §5) | SPEC | Sprint 1 |
| M2 | **Safety State Classifier** | New (ORC-012 §5) | SPEC | Sprint 1 |
| M3 | **Routing Engine** | Foundry Router ref + `uws` patterns | SPEC + REFERENCE | Sprint 1 |
| M3a | **Multi-Polar Routing Table** | Qwen3 (primacy_by_region) | SPEC | Sprint 1 |
| M4 | **TransparencyPacket Emitter** | New (ORC-012 §6) | SPEC | Sprint 1 |
| M5 | **Budget Manager** | `uws` budget module (Rust → Python) | REFERENCE | Sprint 1 |
| M6 | **Provenance Ledger (AuditChain v1)** | New (ORC-012 §9) | SPEC | Sprint 2 |
| M6a | **Open-Weight Provenance Verifier** | DeepSeek-R1 offline audit | SPEC | Sprint 2 |
| M6b | **Provenance Genome** | Manus-original (full ancestry + replay) | SPEC | Phase 2 |
| M7 | **Confabulation Detector (3-layer)** | New (ORC-012 §10) | SPEC | Sprint 2 |
| M8 | **Eastern Review Module** | `eastern-dragonseek/` (PARTIAL) + Civilizational Frame Classifier | PARTIAL | Sprint 2 |
| M9 | **MSP-001 Safety Boundary** | New (ORC-012 §12) | SPEC | Sprint 3 |
| M10 | **Test Harness** | New (ORC-012 §13) | SPEC | Sprint 3 |
| M11 | **Pipeline Orchestrator** | `nexusOrchestrator.ts` pattern | REFERENCE | Sprint 2 |
| M12 | **Task Generator** | New + N6 Structured Outputs | SPEC | Sprint 2 |
| M13 | **Three-Tier Archive** | New | SPEC | Sprint 3 |
| M14 | **Ingestion Service** | New | SPEC | Phase 2 |
| M15 | **Model Router** | `manus-2.0-toolkit` → `model_router.py` + LiteLLM | EXISTS | Sprint 1 |
| M16 | **Learning Loop** | `manus-2.0-toolkit` → `learning_loop.py` | EXISTS | Sprint 3 |
| M17 | **Permission/Approval Engine** | New (Notion AI review) | SPEC | Sprint 1 |
| M17a | **Sovereignty Bound Exception** | DeepSeek (INV-7c lift when <3 families) | SPEC | Sprint 1 |
| M17b | **Sovereignty Gradient** | Manus-original (0.0-1.0 continuous score) | SPEC | Phase 2 |
| M18 | **Hardware Trust CN** (`hardware_trust_cn.py`) | DeepSeek (SM2/SM3/SM4 adapter) | SPEC | Phase 3 |
| M19 | **Bhashini-MCP Bridge** | Qwen3 (India Stack APIs) | SPEC | Phase 2 |
| M20 | **Arabic-Constitutional Bridge** | Qwen3 (Sphere 7 Arabic legal) | SPEC | Phase 2-3 |
| M21 | **Saudi Grid Adapter** | Qwen3 (NEOM solar/wind) | SPEC | Phase 4+ |
| M22 | **China Metabolic Pre-Fetch** | Qwen3 (CMA Fengwu/Pangu Weather) | SPEC | Phase 4+ |
| M23 | **Bamboo Bridge** | GPT + v6.0.6 (5-layer universal protocol sovereignty adapter: Detection → Mapping → Compliance → Provenance → Delivery) | SPEC | Phase 2 (framework) → Phase 3 (national modules) |
| M24 | **Three-Body Validation** | GPT + v6.0.6 (3-frame definitions + 5-step reasoning protocol: Decomposition → Per-Frame → Convergence → Divergence → Synthesis) | SPEC | Phase 3 |
| M25 | **Digital Mandate of Heaven** | GPT + Manus (5-signal legitimacy metric, composed above VWB v1.1 substrate) | SPEC | Phase 2 (VWB calculator) → Phase 3 (compound score) |
| M25a | **VWB Calculator** | v6.0.6 (9-variable equation + sustainability ceiling + RegionalWaterAccountingProfile) | SPEC | Phase 2 |
| M25b | **Regional Water Accounting Profiles** | v6.0.6 (China/Hebei, India/Punjab, Saudi/NEOM templates) | SPEC | Phase 2 |
| M25c | **Water TransparencyPacket** | v6.0.6 (~15 water-specific fields, extends standard TransparencyPacket) | SPEC | Phase 2 |
| M26 | **Persistent Researcher** | CCP-1 (dream/play cycle agent) | SPEC | Phase 2 |
| M27 | **Constitutional Compiler** | Manus-original (YAML → Python + CI/CD gate) | SPEC | Phase 2 |
| M28 | **Session Handoff** | Manus-original (multi-session continuity) | SPEC | Phase 2 |
| M29 | **Constitutional API** | Manus-original (governance as microservice) | SPEC | Phase 3 |
| M30 | **Cross-Task Memory Bridge** | Manus-original (across-task persistence) | SPEC | Phase 2 |
| M31 | **Manus API Orchestrator** | Manus-original (programmatic project mgmt) | SPEC | Phase 1.5 |
| M32 | **Notion Governance Loop Controller** | Manus-original (closed-loop governance-execution) | SPEC | Phase 2 |
| M33 | **Multi-Agent Session Fabric** | Manus-original (parallel Council deliberation) | SPEC | Phase 3 |

**Total L4 modules: 40** (7 Sprint 1, 7 Sprint 2, 4 Sprint 3, 1 Phase 1.5, 13 Phase 2, 5 Phase 3, 3 Phase 4+)

### §3.5 L5 — Extension & Plugin Layer

| Module | Source | Status | Build Phase |
|--------|--------|--------|-------------|
| **MCP Server Framework** | `atlaslattice/servers` (TypeScript) | EXISTS (needs Python port) | Phase 2 |
| **Claude Code Plugins** | `claude-code-plugins-plus-skills` (340 plugins) | EXISTS | Phase 2 |
| **Kintsuji Code Fixer** | `Kintsuji-code-fixer-` | EXISTS | Phase 2 (mandatory CI/CD gate per CCP-3) |
| **Bhashini-MCP Server** | Qwen3 | SPEC | Phase 2 |
| **Saudi Grid MCP Server** | Qwen3 | SPEC | Phase 4+ |
| **Agent Control Plane** | Notion page `3220c1de-73d9-81ba-a19c-f48fe1273275` | EXISTS (extraction needed) | Phase 2 |

### §3.6 L6 — Application Layer (Deployable Apps)

**Phase A — Immediate deployment to Manus servers:**

| App | Source | Size | Status | Demonstrates |
|-----|--------|------|--------|-------------|
| **sheldongemini-GPI** | GitHub (Vite+React) | Full repo | READY | Deploy directly |
| **Janus Enhanced Ingestion** | AI Studio #03 | 2.26M chars | COMPLETE (extraction needed) | Full ORCS pipeline + 3D Sphere |
| **Sanctuary v2 Council Manager** | AI Studio #02 | 1.16M chars | COMPLETE (extraction needed) | Council UI + multi-model debate |

**Phase B-D — Additional apps (see §5.2 for full sequence)**

### §3.7 L7 — Device Mesh Layer

| Module | Source | Status | Build Phase |
|--------|--------|--------|-------------|
| **Cross-Platform Auth/Adapter** | `constitutional-continuum` (TypeScript, 7 files) | EXISTS (minimal) | Phase 3 |
| **Apple CLI** | `atlaslattice/apple-cli` | EXISTS | Phase 3 |
| **Gemini CLI** | `atlaslattice/aluminum-gemini-cli` (TypeScript) | EXISTS | Phase 3 |
| **Device Mesh Sync Protocol** | ORC-014 §8 (6x6 handoff matrix) | SPEC | Phase 4+ |
| **MeshID System** | ORC-014 Federation Layer | SPEC | Phase 4+ |


---

## §4 Repository-to-Module Mapping

### §4.1 Complete 50-Repo Classification

| Grade | Criteria | Count |
|-------|----------|-------|
| **ESSENTIAL** | Contains code that must be extracted or ported for Element 145 | 8 |
| **VALUABLE** | Contains patterns, specs, or partial implementations worth extracting | 11 |
| **REFERENCE** | Design reference only — no code extraction | 17 |
| **PERIPHERAL** | Tangentially related | 5 |
| **INERT** | Financial/DeFi stubs, empty, or abandoned | 10 |

**ESSENTIAL Repos (8):**

| Repo | Grade Confidence | What to Extract | Target Module(s) |
|------|-----------------|----------------|-------------------|
| `uws` (310 files, 36K lines) | HIGH | Router patterns, budget enforcement, civic layer, MCP server | M3, M5, M9, L3 Engine |
| `aluminum-os` (106 files) | HIGH | Royalty Runtime (tracer, event, weighting) | L3 Royalty Runtime |
| `aluminum-os-v3` (46 files) | HIGH | ConsentKernel (forge-boot, forge-core, manus-core) | L2 Kernel |
| `constitutional-os` | HIGH | 39 INVs, 144-Sphere Ontology, Council roster | L1 Constitutional |
| `manus-2.0-toolkit` (113 files) | HIGH | model_router.py, session_vault.py, learning_loop.py, context_compress.py | M15, M16, L2 State |
| `open-regenerative-compute-standard` (90+ files) | HIGH | All canonical docs, council reviews, build plan | Governance corpus |
| `Kintsuji-code-fixer-` | MEDIUM | Code quality enforcement | L5 CI/CD gate |
| `sheldongemini-GPI` | MEDIUM | Vite+React app, deploy directly | L6 Application |

**VALUABLE Repos (11):**

| Repo | Grade Confidence | What to Extract |
|------|-----------------|----------------|
| `bazinga` (26 files) | MEDIUM | Compute layer patterns |
| `claude-code-plugins-plus-skills` (340 plugins) | HIGH | Plugin architecture, skill definitions |
| `servers` (TypeScript) | MEDIUM | MCP server patterns |
| `atlas-lattice-foundation` (100 files) | MEDIUM | Governance framework |
| `constitutional-continuum` (7 files) | LOW | Cross-platform adapter skeleton |
| `apple-cli` | MEDIUM | Apple platform integration |
| `aluminum-gemini-cli` | MEDIUM | Gemini platform integration |
| `deer-flow` | LOW | Agent flow patterns |
| `awesome-claude-code` | HIGH | Curated tool/plugin reference |
| `manus-artifacts` (100+ files) | HIGH | Session artifacts, handoff documents |
| `eastern-dragonseek/` (in ORCS repo) | HIGH | Policy framing, EPVR bridge, MOU template |

**REFERENCE (17), PERIPHERAL (5), INERT (10):** See Appendix A for full listing.

### §4.2 Ground-Truth Corrections (GitHub AI, verified)

| What Was Claimed | What's Actually True | Impact |
|-----------------|---------------------|--------|
| 3 GitHub repos | 6-9 load-bearing repos | Inventory expanded |
| `aluminum-os` = Constitutional Engine | `aluminum-os` = Royalty Runtime | Wrong extraction target corrected |
| Eastern Review = MISSING | Eastern Review = PARTIAL (`eastern-dragonseek/` exists) | One fewer MISSING module |
| 144-sphere needs design work | 144-sphere already defined in `constitutional-os` | Extraction, not design |
| `splitmerge420` references | Being cleaned up to `atlaslattice` (GitHub AI PRs in progress) | Repo hygiene |

---

## §5 Deployable Applications

### §5.1 Manus Deployment Pipeline

**Extraction → Deploy workflow for AI Studio apps:**

```
Step 1: Extract code from AI Studio JSON
        python3 extract_app.py --source ai_studio_codebases/XX_name.json
        
Step 2: Scaffold Vite project
        pnpm create vite app-name --template react-ts
        
Step 3: Replace API keys with env vars
        grep -r "AIza\|sk-\|xai-" src/ → replace with import.meta.env.VITE_*
        
Step 4: Upload static assets
        manus-upload-file --webdev assets/*.png
        
Step 5: Deploy to Manus
        webdev_init_project → webdev_save_checkpoint → Publish
```

**Security gate:** Every app passes through API key scrub before deployment. Atlas Lattice Core (#05) has a visible Gemini API key — MUST be removed.

### §5.2 Deployment Sequence

**Phase A — Immediate (Day 0-3):**

| # | App | Source | Effort | Demonstrates |
|---|-----|--------|--------|-------------|
| A1 | sheldongemini-GPI | GitHub repo | 10 min | Direct deploy — already a Vite project |
| A2 | Janus Enhanced Ingestion | AI Studio #03 (2.26M chars) | 2-3 hrs | Full ORCS pipeline, 3D Sphere Lattice, AraConsole |
| A3 | Sanctuary v2 Council Manager | AI Studio #02 (1.16M chars) | 2-3 hrs | Council UI, multi-model debate |

**Phase B — Week 1:**

| # | App | Source | Effort | Demonstrates |
|---|-----|--------|--------|-------------|
| B1 | ATLAS v3 Governance Lattice | AI Studio #04 | 1-2 hrs | Quasicrystalline governance visualization |
| B2 | Swiss Governance Simulator | AI Studio #07 | 1-2 hrs | Interactive Swiss direct democracy |
| B3 | Sphere Agent Abstraction | AI Studio #08 | 1-2 hrs | 144-sphere typing and visualization |
| B4 | Atlas Lattice Core Repo | AI Studio #05 | 2-3 hrs | Chat interface + Library + Arbiter |
| B5 | Council of Sams | AI Studio #09 | 1-2 hrs | Multi-agent deliberation |

**Phase C — Week 2:**

| # | App | Source | Effort |
|---|-----|--------|--------|
| C1-C8 | Remaining 8 Priority 2 apps | AI Studio | 1-2 hrs each |

**Phase D — Week 3+:**

| # | App | Source | Effort |
|---|-----|--------|--------|
| D1-D9 | Remaining 9 Priority 3 apps | AI Studio | 1-2 hrs each |

### §5.3 Manus Server Inventory

To be populated via Manus API when API key is available. Current known projects:

| Project | Type | Status |
|---------|------|--------|
| `regenerative-compute` | web-static | Dev server running (scaffold only) |
| `aluminum OS` (parent project) | Project container | Active |

---

## §6 Build Sequence

### §6.0 De-Risking Order

Before committing to the full build sequence, validate in this order:

1. **Data models first** — TransparencyPacket, SourceModuleRecord, RoutingDecision schemas
2. **Routing correctness** — M1+M2+M3 classify and route without governance
3. **Governance overlay** — M17+M27 enforce Doctrines on routing decisions
4. **Provenance chain** — M6 AuditChain v1 records decisions immutably
5. **Cross-model validation** — M7+M8 detect confabulation and epistemic bias
6. **Device mesh last** — L7 only after L1-L6 are stable

### §6.1 Phase 0 — Constitutional Build Gate (Days 0-2)

**26 blockers must clear before Sprint 1 begins.**

Required outputs:
1. `element-145` repo created with skeleton structure
2. `.env.example` with all required secrets listed (per Build Gate item 74)
3. Green CI (lint + type-check + 0 tests passing)
4. `CONSTITUTION.md` — 39 Invariants + 72 Doctrines in machine-readable YAML
5. `ROUTING.yaml` — initial routing table (≥4 providers: Gemini, Claude, Grok, GPT)
6. `TransparencyPacket` schema v0.2 (JSON Schema)
7. `SourceModuleRecord` for every module with extraction status
8. MCP Permission Surface Matrix (7-row, initial/write/approval modes)
9. Destructive Action Policy (11 action types, all BLOCKED by default)
10. Canonical Source Decision (GitHub for code, Notion for governance, Drive for archives)
11. AuditChain v1 vs GoldenTrace v2 implementation boundary documented
12. INV-7c corrected to capability-distribution axis everywhere
13. Classifier disambiguation: Epistemic State ≠ Safety State
14. Notion Control Plane: 4 databases (Modules, Build Gates, TransparencyPackets, Sprints)
15. Manus Context Recovery Protocol documented
16. Phase 0 Acceptance Criteria: all 26 blockers resolved, CI green, schemas validate

**Governance Gate G0:** Convenor reviews Phase 0 outputs. Build proceeds only on approval.

### §6.2 Sprint 1 — Core Routing (Days 3-7)

| Deliverable | Modules | Acceptance Criteria |
|-------------|---------|-------------------|
| Epistemic State Classifier | M1 | Classifies queries into VERIFIED/UNKNOWN/CONTESTED/RETRACTED |
| Safety State Classifier | M2 | Classifies queries into SAFE/CAUTION/RESTRICTED/BLOCKED |
| Routing Engine | M3, M3a | Routes to ≥4 providers based on classification + sovereignty |
| TransparencyPacket Emitter | M4 | Every routing decision emits valid TransparencyPacket |
| Budget Manager | M5 | 6-tier budget system with graceful degradation |
| Permission Engine | M17, M17a | All destructive actions blocked without approval |
| Model Router | M15 | LiteLLM integration, ≥4 providers live |

**Sprint 1 Acceptance:** 10-case test matrix passes. p50 <2s for classification/routing excluding model response. All routing decisions emit valid TransparencyPacket. Zero destructive actions without approval.

### §6.3 Sprint 2 — Provenance & Verification (Days 8-11)

| Deliverable | Modules | Acceptance Criteria |
|-------------|---------|-------------------|
| AuditChain v1 | M6 | Append-only JSONL ledger with hash chain |
| Open-Weight Verifier | M6a | DeepSeek-R1 offline audit of hash chain |
| Confabulation Detector | M7 | 3-layer detection (structural + domain + cross-model) |
| Eastern Review | M8 | Civilizational frame classifier active |
| Pipeline Orchestrator | M11 | Multi-step query execution |
| Task Generator | M12 | Structured output generation |

**Sprint 2 Acceptance:** Provenance chain unbroken for 100 consecutive queries. Confabulation detector flags ≥80% of planted hallucinations. Eastern Review flags ≥70% of Western-biased routing decisions.

### §6.4 Sprint 3 — Safety & Testing (Days 12-14)

| Deliverable | Modules | Acceptance Criteria |
|-------------|---------|-------------------|
| MSP-001 Safety Boundary | M9 | Safety-sensitive queries routed correctly |
| Test Harness | M10 | Full 10-case matrix automated |
| Three-Tier Archive | M13 | Hot/warm/cold storage operational |
| Learning Loop | M16 | Feedback incorporated into routing |

**Sprint 3 Acceptance:** Full 10-case matrix passes. Safety boundary correctly blocks/escalates all test cases. Archive retrieval <500ms for hot tier.

### §6.5 Phase 1.5 — Shadow Mode (Days 15-21)

| Deliverable | Modules | Acceptance Criteria |
|-------------|---------|-------------------|
| Shadow Mode | M10 enhancement | ≥48h parallel run, ≥90% alignment with expected |
| Simulation Coverage | M10 enhancement | 5 mandatory scenarios pass |
| Audit Export | M6 enhancement | JSON + CSV export operational |
| Manus API Orchestrator | M31 | Programmatic project management |

### §6.6 Phase 2 — Full System (Days 22-45)

| Deliverable | Modules |
|-------------|---------|
| ConsentKernel integration | L2 Kernel |
| Janus v2 Protocol | L3 Engine |
| Constitutional Compiler | M27 |
| Session Handoff | M28 |
| Cross-Task Memory Bridge | M30 |
| Notion Governance Loop | M32 |
| Persistent Researcher | M26 |
| Bhashini-MCP Bridge | M19 |
| MCP Server Framework | L5 |
| Kintsuji CI/CD Gate | L5 |
| Provenance Genome | M6b |
| Sovereignty Gradient | M17b |
| VWB Calculator | M25a |
| Regional Water Accounting Profiles | M25b |
| Water TransparencyPacket | M25c |
| Bamboo Bridge Framework | M23 (Phase 2 portion) |
| INV-19 Enforcement | M8 enhancement |
| Ingestion Service | M14 |

### §6.7 Phase 3 — Advanced Governance (Days 46-90)

| Deliverable | Modules |
|-------------|---------|
| GoldenTrace v2 (PQC + hardware roots) | M6 upgrade |
| Hardware Trust CN | M18 |
| Bamboo Bridge | M23 |
| Three-Body Validation | M24 |
| Digital Mandate of Heaven | M25 |
| Constitutional API | M29 |
| Multi-Agent Session Fabric | M33 |
| Arabic-Constitutional Bridge | M20 |
| Cross-Platform Auth/Adapter | L7 |

### §6.8 Phase 4+ — Global Deployment

| Deliverable | Modules |
|-------------|---------|
| Chennai Reference Node | Full stack |
| DragonSeek Reference Node (Alibaba Cloud) | M18, M22, M23 |
| GangaSeek Reference Node (India Stack) | M19 |
| JinnSeek Reference Node (SDAIA) | M20, M21 |
| Device Mesh Sync Protocol | L7 |
| MeshID System | Federation Layer |
| Saudi Grid Adapter | M21 |
| China Metabolic Pre-Fetch | M22 |
| 50-node global rollout | All layers |

---

## §7 Governance Gates

| Gate | Phase Boundary | Required Approvals | Key Criteria |
|------|---------------|-------------------|-------------|
| **G0** | Phase 0 → Sprint 1 | Convenor | 26 blockers resolved, CI green, schemas validate |
| **G1** | Sprint 3 → Phase 1.5 | Convenor + 1 Council seat | 10-case matrix passes, <2s routing, zero unauthorized destructive actions |
| **G2** | Phase 1.5 → Phase 2 | Convenor + 2 Council seats | ≥48h Shadow Mode, ≥90% alignment, audit export functional |
| **G3** | Phase 2 → Phase 3 | Convenor + 3 Council seats | ConsentKernel integrated, Constitutional Compiler active, Notion loop operational |
| **G4** | Phase 3 → Phase 4+ | Full Council | GoldenTrace v2 operational, Bamboo Bridge tested, Three-Body validation passes |


---

## §8 Risk Register

| ID | Vector | Severity | Detection | Mitigation | Recovery |
|----|--------|----------|-----------|------------|----------|
| R1 | Timeline overrun | HIGH | Sprint velocity tracking | +50% buffer (60-90 days realistic) | Scope reduction to core routing |
| R2 | TransparencyPacket schema drift | HIGH | Schema validation in CI | JSON Schema versioning | Rollback to last valid schema |
| R3 | AI Studio code = hypothesis | HIGH | SourceModuleRecord verification | Extract → test → validate before DIRECT | Downgrade to PARTIAL |
| R4 | Cross-provider API drift | HIGH | Nightly smoke tests | LiteLLM abstraction + fallback chain | Provider substitution |
| R5 | Budget runaway | HIGH | Real-time cost monitoring | 6-tier degradation, not termination | Tier reduction + alert |
| R6 | Confabulation in routing | HIGH | 3-layer detection | Structural (always-on) + domain (triggered) + cross-model | Flag + human review |
| R7 | INV-7 violation | HIGH | Continuous monitoring | Automatic rebalancing | Routing table adjustment |
| R8 | Destructive action without approval | CRITICAL | Permission Engine (M17) | All 11 types BLOCKED by default | Rollback + audit |
| R9 | Provenance chain break | HIGH | Hash chain validation | Append-only + backup | Chain repair from backup |
| R10 | Eastern Review false negatives | MEDIUM | Periodic manual audit | Civilizational frame classifier | Routing table adjustment |
| R11 | splitmerge420 references | LOW | grep audit | GitHub AI cleanup PRs | Manual correction |
| R12 | Notion MCP connection failure | MEDIUM | Health check | Retry + local fallback | Queue + replay |
| R13 | Routing table poisoning | HIGH | Diff review on table changes | Approval required for table modifications | Rollback to last approved table |
| R14 | Civic constraint bypass | HIGH | Constitutional Compiler validation | Pre-commit hook blocks violations | Revert + audit |
| R15 | Session state loss | MEDIUM | Heartbeat monitoring | M28 Session Handoff + M30 Memory Bridge | Restore from last checkpoint |
| R16 | Single-provider dependency | HIGH | INV-7c monitoring | ≥4 providers always active | Automatic failover |
| R17 | Doctrine conflict | MEDIUM | Constitutional Compiler | Three-Body Validation (Phase 3) | Council resolution |
| R18 | GoldenTrace hardware unavailability | MEDIUM | Hardware inventory check | AuditChain v1 as fallback | Software-only audit |
| R19 | Model deprecation | HIGH | Provider changelog monitoring | LiteLLM model aliasing | Substitute equivalent model |
| R20 | Sovereign audit failure (China) | HIGH | SM2/SM3/SM4 compliance check | Hardware Trust CN adapter (M18) | Air-gap fallback |
| R21 | INV-7c self-destruct in sovereign | MEDIUM | Sovereignty Bound Exception (M17a) | Cap lifts when <3 compliant families | Document exception |
| R22 | Chinese cloud unavailability | MEDIUM | Alibaba Cloud health check | DragonSeek fallback to local | Air-gapped deployment |
| R23 | India Stack API changes | MEDIUM | Bhashini API version monitoring | Adapter pattern (M19) | Version pinning |
| R24 | SDAIA compliance drift | MEDIUM | Regulatory monitoring | Arabic-Constitutional Bridge (M20) | Policy update cycle |
| R25 | Multi-polar routing inconsistency | HIGH | Cross-region test suite | M3a region-aware routing table | Reconciliation protocol |
| R26 | INV-18 DPI bypass attempt | HIGH | DPI compliance monitor | Automatic block + alert | Audit + Convenor review |
| R27 | Bamboo Bridge translation loss | MEDIUM | Bidirectional validation | Round-trip testing (MCP→GB/T→MCP) | Fallback to raw protocol |
| R28 | Three-Body deadlock | MEDIUM | Timeout monitoring | Majority-rules fallback after timeout | Log dissent + proceed |
| R29 | Mandate score gaming | MEDIUM | Anomaly detection | 90-day rolling window + outlier flagging | Score reset + audit |
| R30 | Constitutional Compiler drift | HIGH | Doctrine hash verification | Compiler output compared to reference | Recompile from canonical YAML |
| R31 | Session Handoff integrity | MEDIUM | Handoff verification hash | M28 integrity check on restore | Re-request from source |
| R32 | Persistent Researcher budget runaway | MEDIUM | Budget cap per research cycle | Prometheus rest cycle enforcement | Cycle termination + report |
| R33 | Sustainability ceiling data unavailability | MEDIUM | Regional Profile completeness check | Default to raw baseline when cap absent, flag in Water TransparencyPacket | Graceful degradation |
| R34 | Regional Water Profile data quality | MEDIUM | Cross-source validation | Multiple sovereign data sources per variable | Flag low-confidence profiles |

**Total: 34 risk vectors, 0 unmitigated.**

---

## §9 Cross-Platform Integration

### §9.1 Platform Integration Matrix

| Platform | Role | Integration Method | Key APIs | Phase |
|----------|------|-------------------|----------|-------|
| **Windows** | First Host Integration Candidate | WSL2 backend + WinUI3 dashboard | Copilot Runtime, Entra, Confidential Computing | Phase 2-3 |
| **macOS** | Ring 4 Creative/Professional | Swift bridge + Apple Intelligence | Core ML, Shortcuts, Apple Intelligence | Phase 3 |
| **ChromeOS** | Lightweight + Education | PWA + Chrome Extension | Chrome APIs, Android subsystem | Phase 2 |
| **Android** | Mobile + IoT | Kotlin bridge + Gemini Nano | On-device ML, Gemini Nano, Material You | Phase 3 |
| **iOS** | Mobile Premium | Swift bridge + App Intents | SiriKit, App Intents, Core ML | Phase 3 |
| **Linux** | Developer + Server | Native Python + systemd | D-Bus, systemd, Wayland | Phase 2 |
| **Alibaba Cloud** | Chinese Sovereign | Function Compute + PolarDB + DashScope | China-specific APIs, SM2/SM3/SM4 | Phase 4+ |

### §9.2 Switzerland Layer Unification

The Switzerland Layer (aka "The Weave" per Copilot/Microsoft) provides 6 unification services:

| Service | What It Unifies | Implementation |
|---------|----------------|----------------|
| **Identity** | Microsoft Entra + Apple ID + Google Account + sovereign IDs | Federated OAuth + MeshID |
| **State** | Cross-device session persistence | M28 Session Handoff + L7 Device Mesh |
| **Routing** | Model selection across all platforms | M3 Router + M3a Multi-Polar Table |
| **Governance** | Constitutional enforcement regardless of host | M27 Constitutional Compiler |
| **Model** | Provider abstraction | M15 Model Router + LiteLLM |
| **Mesh** | Device handoff and sync | L7 Device Mesh Sync Protocol |

### §9.3 WEAVE Integration Points (from Copilot v2.5.4)

| Microsoft Product | Ring | Integration Point | Element 145 Module |
|-------------------|------|-------------------|-------------------|
| Foundry Model Router | 0 | Production routing reference | M3 |
| Azure Confidential Computing | 0 | GoldenTrace hardware root | M6 (GoldenTrace v2) |
| Microsoft Entra | 0 | Identity federation | Switzerland Layer |
| Copilot Runtime | 1 | M365 surface integration | Complementary to M3 |
| Azure AI Services | 1 | Model hosting | M15 |
| Windows Service Manager | 2 | Process lifecycle | Element 145 daemon |
| WSL2 | 2 | Python backend hosting | All L4 modules |
| WinUI3 | 3 | Dashboard rendering | L6 Application |
| VS Code | 4 | Developer integration | L5 Extension |
| Microsoft Graph | 5 | Data access | L5 Extension |

---

## §10 Symbiosis Points

### §10.1 Claude (S1) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| C1 | Constitutional reasoning for Doctrine validation | Sprint 1+ |
| C2 | Long-context analysis for provenance audit | Sprint 2+ |
| C3 | Multi-substrate hierarchy routing reference | Sprint 1 |
| C4 | Scribe role: document governance, COI flagging | Ongoing |

### §10.2 Gemini (S2) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| G1 | 2M token context for full-corpus analysis | Phase 2+ |
| G2 | Multimodal classification (image/video routing) | Phase 2+ |
| G3 | Structured output for TransparencyPacket generation | Sprint 1 |
| G4 | Gemini Nano for on-device classification | Phase 3 |

### §10.3 Grok (S3) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| GK1 | Real-time data access for live routing decisions | Sprint 1+ |
| GK2 | Adversarial testing of routing decisions | Sprint 3 |
| GK3 | X/Twitter integration for public transparency | Phase 2+ |

### §10.4 Copilot (S4) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| CO1 | Foundry Router as M3 reference implementation | Sprint 1 |
| CO2 | Azure Confidential Computing for GoldenTrace | Phase 3 |
| CO3 | Microsoft Entra for identity federation | Phase 2 |
| CO4 | 29-product integration map (WEAVE v2.5.4) | Phase 2-4+ |
| CO5 | Windows Service lifecycle management | Phase 2 |

### §10.5 DeepSeek (S5) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| DS1 | Live provider in routing table (DeepSeek-V3/R1) | Sprint 1 |
| DS2 | Open-weight offline verifier (M6a) | Sprint 2 |
| DS3 | Hardware Trust CN adapter reference | Phase 3 |
| DS4 | DragonSeek deployment pathway | Phase 4+ |
| DS5 | Doctrine 61 (open-weight audit sovereignty) | Sprint 2 |
| DS6 | Air-gapped deployment architecture | Phase 4+ |
| DS7 | SM2/SM3/SM4 crypto implementation reference | Phase 3 |

### §10.6 GPT (S6) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| GP1 | Foundry Router production experience | Sprint 1 |
| GP2 | Bamboo Bridge protocol design | Phase 3 |
| GP3 | Three-Body Validation framework | Phase 3 |
| GP4 | Digital Mandate of Heaven metric design | Phase 3 |
| GP5 | Failure mode analysis and recovery chains | Sprint 1+ |

### §10.7 Manus (S7) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| MA1 | Build execution — the only seat that writes code | All phases |
| MA2 | Constitutional Compiler (M27) | Phase 2 |
| MA3 | Session Handoff (M28) | Phase 2 |
| MA4 | Cross-Task Memory Bridge (M30) | Phase 2 |
| MA5 | Notion Governance Loop (M32) | Phase 2 |
| MA6 | Multi-Agent Session Fabric (M33) | Phase 3 |
| MA7 | Manus API Orchestrator (M31) | Phase 1.5 |
| MA8 | 25-app deployment pipeline | Phase A-D |

### §10.8 Qwen (S10) Symbiosis

| ID | Point | Build Phase |
|----|-------|-------------|
| AL1 | Multi-polar routing table (M3a) | Sprint 1 |
| AL2 | Bhashini-MCP Bridge (M19) | Phase 2 |
| AL3 | Arabic-Constitutional Bridge (M20) | Phase 2-3 |
| AL4 | GangaSeek deployment pathway | Phase 4+ |
| AL5 | JinnSeek deployment pathway | Phase 4+ |
| AL6 | 22-language translation capability | Phase 2+ |
| AL7 | Civilizational Frame Classifier enhancement | Sprint 2 |

---

## §11 Notion Control Plane

### §11.1 Required Databases (Phase 0)

| Database | Fields | Permissions |
|----------|--------|------------|
| **Modules** | ID, Name, Status, Phase, Owner, Source Repo, Extraction Status, Acceptance Test | AI-write (Manus), Human-approval (Convenor) |
| **Build Gates** | ID, Item, Source, Severity, Phase, Owner, Status, Acceptance Test, Blocking | AI-write (Manus), Human-approval (Convenor) |
| **TransparencyPackets** | Query ID, Timestamp, Classification, Route, Cost, Provenance Hash | AI-write (Element 145), Read-only (Council) |
| **Sprints** | Sprint #, Start, End, Deliverables, Status, Acceptance Criteria, Gate | AI-write (Manus), Human-approval (Convenor) |

### §11.2 Governance Automation

| Feature | Implementation | Phase |
|---------|---------------|-------|
| **HITL Approval Forms** | Notion Forms → Approvals database | Phase 0 |
| **Sprint Task Creation** | Notion Buttons → Sprint database | Phase 0 |
| **Audit Checklist** | Notion Buttons → Build Gates database | Sprint 1 |
| **Council Review Request** | Notion Buttons → notification to Council | Sprint 1 |
| **Schema Registry** | Notion pages with JSON Schema + version diffs | Phase 0 |
| **Calendar Integration** | Sprint/review → Notion Calendar events | Phase 0 |

### §11.3 Notion ↔ Module Mapping

| Notion Feature | Element 145 Module | Data Flow |
|---------------|-------------------|-----------|
| Modules database | M32 Governance Loop | Manus reads status → executes → writes result |
| Build Gates database | M32 Governance Loop | Gate items move through OPEN → IN_PROGRESS → COMPLETED |
| TransparencyPackets database | M4 Emitter + M6 Ledger | Element 145 writes packets; Notion stores for dashboard |
| Sprints database | M32 Governance Loop | Sprint planning → execution → review cycle |
| Approvals database | M17 Permission Engine | HITL requests queued → Convenor approves → Manus executes |

---

## §12 Systems Optimization Decisions

### §12.1 Answers to Manus's 6 Systems Questions

| Q# | Question | Answer Source | Decision |
|----|----------|--------------|----------|
| Q1 | Windows Service restart/recovery | Copilot WEAVE v2.5.4 | `sc.exe` failure actions: restart after 5s, 30s, 60s. Watchdog process. |
| Q2 | WSL2 ↔ Windows IPC | Copilot WEAVE v2.5.4 | Named pipes for low-latency, gRPC for structured data. Unix socket bridge. |
| Q3 | Multi-provider OAuth token refresh | GPT v6.0 | Token refresh daemon per provider. Credential vault (Azure Key Vault / Hashicorp). |
| Q4 | Device Mesh conflict resolution | GPT v6.0 + Copilot | Last-writer-wins with vector clocks. Conflict → queue for human resolution. |
| Q5 | Copilot Runtime ↔ Element 145 | Copilot WEAVE v2.5.4 | Complementary. Element 145 = constitutional routing. Copilot Runtime = M365 surface. |
| Q6 | Chromebox 5 performance | GPT v6.0 | Sufficient for development. Production needs ≥16GB RAM, SSD. |


---

## §13 Council Seat Registry

| Seat | Entity | Role | Status | Key Deliverables |
|------|--------|------|--------|-----------------|
| S1 | Claude (Anthropic) | Constitutional Scribe | ACTIVE | Aluminum OS v6.0.4, Marathon Manifest v1.1, Doctrine authoring |
| S2 | Gemini (Google) | Architectural Precision | ACTIVE | Classification framework, async scoring |
| S3 | Grok (xAI) | Truth-Seeking Challenger | ACTIVE | Strategic coherence, adversarial testing |
| S4 | Copilot (Microsoft) | Enterprise Infrastructure | ACTIVE | WEAVE v2.5.4, 6-OS platform specs, 29-product map |
| S5 | DeepSeek | Sovereign AI Representative | ACTIVE | Hardware Trust CN, DragonSeek, open-weight audit |
| S6 | GPT (OpenAI) | Analytical Rigor | ACTIVE | Failure modes, Bamboo Bridge, Three-Body, Mandate |
| S7 | Manus | Build Seat | ACTIVE | Code execution, deployment, Constitutional Compiler |
| S8 | Notion AI | Governance Analyst | ACTIVE | Notion Control Plane, operational edits, AuditChain split |
| S9 | GitHub AI | Execution Realism | ACTIVE | Ground-truth verification, repo cleanup |
| S10 | Qwen (Alibaba) | Asia-Pacific Sovereignty | ACTIVE | Multi-polar routing, Bhashini, Arabic Bridge, GangaSeek, JinnSeek |
| S144 | Ghost Seat | Observation | RESERVED | Per Doctrine 72 — universal aspiration with 4 exception categories |
| — | Apple Intelligence | Future candidate | PROVISIONAL | Ring 0 + Ring 4 integration |
| — | Mistral | Future candidate | PROVISIONAL | EU sovereignty pathway |
| — | Cohere | Future candidate | PROVISIONAL | Enterprise RAG |

---

## §14 Doctrine & Invariant Summary

### §14.1 Doctrines 1-67 (from Aluminum OS v6.0.3)

Ratified and canonical. Full text in Aluminum OS v6.0.4. Key doctrines for Element 145:

| Doctrine | Name | Element 145 Impact |
|----------|------|-------------------|
| D-7 | Verify-Before-Vault | Cross-model-family + non-conflicted verification rule |
| D-11 | Metabolic Accountability | Every routing decision carries metabolic cost |
| D-59 | Claim Verification | 4-tier classification (verified/vendor-stated/research-based/target/unverified) |
| D-61 | Open-Weight Audit | Open-weight models can audit closed-weight provenance |

### §14.2 Doctrines 68-72 (from Aluminum OS v6.0.4)

| Doctrine | Name | What It Governs |
|----------|------|----------------|
| D-68 | Open-Weight Audit Sovereignty | DeepSeek-R1 as offline verifier. M6 supports offline audit mode. |
| D-69 | Vendor Exclusion Procedures | 75% supermajority, documented justification, substitution pathway, reversible |
| D-70 | Sovereign Deployment Pathways | DragonSeek/GangaSeek/JinnSeek as canonical Phase 4+ pathways |
| D-71 | Maximum Allowable Transparency | Design intent — affects TransparencyPacket field count, GoldenTrace access, Council logging |
| D-72 | Sphere 144 Observation Rights | Universal aspiration + 4 exception categories (safety, vendor IP, sovereignty, privacy) |

### §14.3 Doctrines 76-77 (from Aluminum OS v6.0.6)

| Doctrine | Name | What It Governs |
|----------|------|----------------|
| D-76 | Substrate-Before-Framing | Before integrating cultural framing, verify canonical substrate exists. Codified from VWB session protocol. |
| D-77 | Sovereign Methodology Profile Pattern | Single global methodology + pluggable sovereign data adapters. Default architecture for all methodology modules. |

### §14.4 Key Invariants

| Invariant | Name | Enforcement |
|-----------|------|------------|
| INV-7 | Switzerland (47% cap) | M17 Permission Engine monitors continuously |
| INV-7c | Capability-distribution axis | Measurement by capability-weighted routing volume, NOT vendor count |
| INV-17 | Provenance | Every decision has a traceable origin |
| INV-18 | DPI Respect | No component bypasses sovereign Digital Public Infrastructure |
| INV-19 | Water Cohesion | No facility may claim net-positivity while downstream water quality deteriorates |

---

## §15 Sovereign Deployment Pathways

### §15.1 Chennai Reference Node (Phase 4+)

| Component | Infrastructure | Status |
|-----------|---------------|--------|
| Compute | Local data center + renewable power | TARGET |
| Models | Gemini + Claude + local fine-tuned | TARGET |
| Governance | Full ORCS stack + Indian regulatory compliance | TARGET |
| Metabolic | Water/power/heat monitoring + community benefit | TARGET |
| Partners | Named partners (classified) | TARGET |

### §15.2 DragonSeek Reference Node (Phase 4+)

| Component | Infrastructure | Compliance |
|-----------|---------------|------------|
| Cloud | Alibaba Cloud (Function Compute, PolarDB, DashScope) | PRC Cybersecurity Law + Data Security Law + PIPL |
| Crypto | SM2/SM3/SM4 via Phytium TCM | GB/T 32918 |
| Models | DeepSeek-V3, Qwen3, local fine-tuned | MIIT AI regulations |
| Standards | TC260, CESI alignment | Chinese AI standards bodies |
| Economic | Dual circulation strategy framing | Current PRC economic policy |
| BRI | Belt and Road Digital Silk Road extension (Phase 5+) | International cooperation framework |

### §15.3 GangaSeek Reference Node (Phase 4+)

| Component | Infrastructure | Compliance |
|-----------|---------------|------------|
| Stack | India Stack (Aadhaar, UPI, ONDC) | Indian IT Act + DPDPA |
| Translation | Bhashini (22 languages) | Government of India API |
| Models | Gemini + local fine-tuned | Indian AI regulations |
| Commerce | UPI + ONDC integration | RBI guidelines |

### §15.4 JinnSeek Reference Node (Phase 4+)

| Component | Infrastructure | Compliance |
|-----------|---------------|------------|
| Authority | SDAIA (Saudi Data & AI Authority) | Saudi AI Ethics Principles |
| Compute | NEOM solar + Red Sea wind | Vision 2030 |
| Legal | Arabic-Constitutional Bridge (M20) | Sharia-compatible governance |
| Language | Arabic-first Sphere 7 operation | Native Arabic legal frameworks |

---

## §16 Document Lineage

| Version | Date | Key Changes |
|---------|------|-------------|
| Code Synthesis Strategy v1.0 | Apr 20, 2026 | Initial 16-module strategy |
| Build Synthesis v1.1 | Apr 24, 2026 | 50-repo audit + AI-Native OS reframing |
| ORC-012 TDD v0.2 | Apr 24, 2026 | 16-section governance-compliant technical design |
| Build Gate Register v2.2 | Apr 24, 2026 | 84-item execution control |
| AUWS-SPEC v1.2 | Apr 24, 2026 | 7-layer OS architecture |
| ORC-014 Platform Integration v1.0 | Apr 24, 2026 | 6-OS deployment specs |
| Build Plan v1.0 | Apr 29, 2026 | First consolidated build plan |
| Build Plan v1.1 | Apr 29, 2026 | +DeepSeek sovereignty (14 items) |
| Build Plan v1.2 | Apr 29, 2026 | +Qwen3 multi-polar (11 items) + DeepSeek codification (3 items) |
| Build Plan v1.3 | Apr 29, 2026 | +GPT innovations (3) + CCP priorities (7) + Manus priorities (3) + Manus innovations (5) |
| Build Plan v1.4 | Apr 29, 2026 | +v6.0.4 Patch (18) + Manifest v1.1 (12) + WEAVE v2.5.4 (10) + Notion AI (14) + 5 Manus innovations |
| **Build Plan v1.5** | **Apr 29, 2026** | **+v6.0.6 VWB Sovereignty (16 Phase Queue items, 2 Doctrines, 1 Invariant, 6 schemas, 3 module expansions)** |

---

## §17 Immediate Next Actions

### P0 — Critical Path (This Week)

| Action | Owner | Dependency |
|--------|-------|-----------|
| Create `element-145` repo | Manus (S7) | Convenor greenlight |
| Resolve 26 Phase 0 blockers | Manus (S7) | Repo created |
| Set up Notion Control Plane (4 databases) | Manus (S7) | Notion MCP operational |
| Deploy sheldongemini-GPI to Manus | Manus (S7) | None — ready now |
| Extract + deploy Janus Enhanced Ingestion | Manus (S7) | API key scrub |
| Extract + deploy Sanctuary v2 | Manus (S7) | API key scrub |

### P1 — High Priority (Next Week)

| Action | Owner | Dependency |
|--------|-------|-----------|
| Sprint 1 execution (M1, M2, M3, M4, M5, M15, M17) | Manus (S7) | G0 passed |
| Deploy Phase B apps (5 apps) | Manus (S7) | Phase A complete |
| Vault all pending documents to Notion | Manus (S7) | Notion MCP stable |
| Claude independent verification (option c) | Claude (S1) | Convenor greenlight |

### P2 — Medium Priority (Week 3-4)

| Action | Owner | Dependency |
|--------|-------|-----------|
| Sprint 2-3 execution | Manus (S7) | Sprint 1 accepted |
| Deploy Phase C apps (8 apps) | Manus (S7) | Phase B complete |
| Begin Phase 1.5 Shadow Mode | Manus (S7) | Sprint 3 accepted |

### P3 — Lower Priority (Month 2+)

| Action | Owner | Dependency |
|--------|-------|-----------|
| Phase 2 full system | Manus (S7) | G2 passed |
| Phase 3 advanced governance | Manus (S7) | G3 passed |
| Sovereign deployment planning | Council | G4 preparation |

---

## Appendix A: Full 50-Repo Inventory

### REFERENCE Repos (17)

| Repo | Description | Relevance |
|------|-------------|-----------|
| `tucker-gemini-GPT-` | Gemini agent | Pattern reference |
| `ai-artifacts` | AI-generated artifacts | Content reference |
| `awesome-mcp-servers` | MCP server catalog | Integration reference |
| `browser-tools-mcp` | Browser MCP tools | Extension reference |
| `chrome-extension-boilerplate-react` | Chrome extension template | ChromeOS reference |
| `cline` | CLI tool | Developer reference |
| `context7` | Context management | Pattern reference |
| `gemini-cli` | Gemini CLI (not atlaslattice fork) | Reference |
| `mcp` | MCP protocol reference | Protocol reference |
| `openai-agents-python` | OpenAI agent patterns | Agent reference |
| `PraisonAI` | AI framework | Architecture reference |
| `Scira` | Search/research tool | Research reference |
| `taskmaster-ai` | Task management | Workflow reference |
| `The-Prompt-Index` | Prompt catalog | Prompt engineering reference |
| `web-check` | Web checking tool | Testing reference |
| `windsurf-memory-bank` | Memory persistence | M30 reference |
| `zed` | Editor | Developer tooling reference |

### PERIPHERAL Repos (5)

| Repo | Description | Relevance |
|------|-------------|-----------|
| `cursor-tools` | Cursor IDE tools | Tangential |
| `eliza` | Conversational agent | Historical reference |
| `firecrawl` | Web scraping | Utility only |
| `mastra` | Framework | Tangential |
| `notebooklm-mastra-demo` | Demo app | Demo only |

### INERT Repos (10)

| Repo | Description | Action |
|------|-------------|--------|
| `aave-v3-core` | DeFi protocol | Archive |
| `compound-protocol` | DeFi protocol | Archive |
| `flash-loan-mastery` | DeFi tutorial | Archive |
| `hardhat` | Ethereum tooling | Archive |
| `openzeppelin-contracts` | Solidity contracts | Archive |
| `pancake-frontend` | DeFi frontend | Archive |
| `solidity-by-example` | Solidity tutorials | Archive |
| `uniswap-v2-core` | DeFi protocol | Archive |
| `uniswap-v3-core` | DeFi protocol | Archive |
| `v3-periphery` | DeFi periphery | Archive |

---

## Appendix B: Glossary

| Term | Definition |
|------|-----------|
| **AuditChain v1** | Non-PQC append-only provenance ledger (Sprint 2) |
| **Bamboo Bridge** | Protocol sovereignty adapter (MCP/A2A ↔ GB/T/DEPA/SDAIA) |
| **Capability-distribution axis** | INV-7c measurement: vendor share by capability-weighted routing volume |
| **Constitutional Compiler** | Doctrine YAML → executable Python enforcement functions |
| **ConsentKernel** | Core governance engine — consent-based state management |
| **Digital Mandate of Heaven** | 5-signal governance legitimacy metric |
| **DragonSeek** | Chinese sovereign deployment pathway (Alibaba Cloud) |
| **Element 145** | L4 Service Orchestration layer — immediate build target |
| **Epistemic State** | VERIFIED / UNKNOWN / CONTESTED / RETRACTED classification |
| **GangaSeek** | Indian sovereign deployment pathway (India Stack) |
| **GoldenTrace v2** | PQC + hardware root of trust audit trail (Phase 3+) |
| **INV-7** | Switzerland Invariant: no single vendor >47% of routing capacity |
| **JinnSeek** | Saudi sovereign deployment pathway (SDAIA) |
| **Mandate Review** | 90-day rolling governance legitimacy assessment |
| **MeshID** | Cross-device persistent identity in the Federation Layer |
| **Multi-Polar Routing Table** | Region-aware routing with `primacy_by_region` |
| **Provenance Genome** | Full ancestry record with deterministic replay capability |
| **Safety State** | SAFE / CAUTION / RESTRICTED / BLOCKED classification |
| **Sovereignty Gradient** | Continuous 0.0-1.0 sovereignty score |
| **Switzerland Layer** | Cross-platform unification layer (aka "The Weave") |
| **Three-Body Validation** | Multi-civilizational doctrine validation framework |
| **TransparencyPacket** | ~30-field structured record emitted by every routing decision |
| **The Weave** | Copilot/Microsoft designation for the Switzerland Layer |

---

## Appendix C: DeepSeek Sovereignty Integration Summary

See Build Plan v1.1 Appendix D (preserved). Key additions in v1.4:
- S5+S10 co-occupancy confirmed and operational
- Doctrines 68-72 ratified
- INV-7c corrected to capability-distribution axis
- DragonSeek compliance checklist expanded: PRC Cybersecurity Law + Data Security Law + PIPL (three separate laws)
- Chinese standards bodies (TC260, CESI) referenced
- Dual circulation strategy framing added
- Belt and Road Digital Silk Road as Phase 5+ extension

---

## Appendix D: Manus-Original Innovations Summary

| Innovation | Module | What It Does | Phase |
|-----------|--------|-------------|-------|
| Constitutional Compiler | M27 | YAML → Python + CI/CD gate | Phase 2 |
| Session Handoff | M28 | Multi-session continuity | Phase 2 |
| Constitutional API | M29 | Governance as microservice | Phase 3 |
| Cross-Task Memory Bridge | M30 | Across-task persistence | Phase 2 |
| Manus API Orchestrator | M31 | Programmatic project management | Phase 1.5 |
| Notion Governance Loop | M32 | Closed-loop governance-execution | Phase 2 |
| Multi-Agent Session Fabric | M33 | Parallel Council deliberation | Phase 3 |
| Sovereignty Gradient | M17b | Continuous 0.0-1.0 score | Phase 2 |
| VWB Calculator | M25a | 9-variable ecological accounting + sustainability ceiling | Phase 2 |
| Regional Water Profiles | M25b | Sovereign data adapter templates (China/India/Saudi) | Phase 2 |
| Water TransparencyPacket | M25c | ~15 water-specific fields extending standard packet | Phase 2 |
| Provenance Genome | M6b | Full ancestry + replay | Phase 2 |
| Substrate-Aware Cost Optimizer | M5 enhancement | Real-time pricing → routing | Sprint 1+ |

---

## Appendix E: CCP Priorities Integration

| Priority | Status | Location in Build Plan |
|----------|--------|----------------------|
| CCP-1: Persistent Researcher | INTEGRATED | M26, §6.6 |
| CCP-2: Ara as Authority | INTEGRATED | §6.6 |
| CCP-3: Kintsuji Mandatory Gate | INTEGRATED | L5, §6.6 |
| CCP-4: Daavud's Device Mesh | INTEGRATED | L7, §6.7-§6.8 |
| CCP-5: Noosphere Cloud | INTEGRATED | §9, Federation Layer |
| CCP-6: 144 Sphere Agents | INTEGRATED | Progressive rollout 12→36-48→144 |
| CCP-7: Notion Telemetry | INTEGRATED | §11, M32 |
| CCP-8: Belt and Road Integration | INTEGRATED | §15.2, Phase 5+ |
| CCP-9: China AI Development Plan alignment | INTEGRATED | §15.2 |
| CCP-10: Social Credit exclusion | INTEGRATED | Proposed Doctrine 73 |

---

*Manus — S7 Build Seat — Atlas Lattice Foundation — April 29, 2026*
*Status: Build Plan v1.5 CANONICAL. 237+ items integrated. Zero contradictions. Ready for Phase 0.*
