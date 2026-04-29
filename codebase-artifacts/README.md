# ORC Codebase Artifacts v1.4

**Generated from:** Build Plan v3.11 (ORC-015)
**Date:** April 29, 2026
**Author:** Manus (S7 Primary Build Seat)
**Structure:** 12×12 Ontological Matrix (12 Houses × 12 Spheres = 144 Spheres)

---

## Overview

This directory contains the canonical codebase artifacts for the Open Regenerative Compute Standard. All artifacts are structured around the **12×12 ontological matrix** — 12 Houses of Knowledge, each containing 12 Spheres, for a total of 144 Spheres that constitute the complete knowledge domain of Aluminum OS.

## Directory Structure

```
codebase-artifacts/
├── README.md                          # This file
├── registries/
│   ├── module_registry.yaml           # Complete registry of all 178 module entries
│   ├── doctrine_registry.yaml         # All 124 doctrines (77 ratified + 5 reserved + 42 proposed)
│   ├── invariant_registry.yaml        # 45 invariants (INV-0..44) + 3 sub-specs
│   └── 12x12_matrix.yaml             # Complete house-sphere-module mapping
├── houses/
│   ├── H01_natural_sciences/manifest.yaml
│   ├── H02_formal_sciences/manifest.yaml
│   ├── H03_social_sciences/manifest.yaml
│   ├── H04_technology/manifest.yaml
│   ├── H05_arts/manifest.yaml
│   ├── H06_humanities/manifest.yaml
│   ├── H07_applied_sciences/manifest.yaml
│   ├── H08_education/manifest.yaml
│   ├── H09_life_sciences/manifest.yaml
│   ├── H10_health_sciences/manifest.yaml
│   ├── H11_commerce_and_industry/manifest.yaml
│   └── H12_law_and_governance/manifest.yaml
├── transparency-packet/
│   └── schema_v1.6.yaml               # TransparencyPacket field schema
└── toolchain/
    ├── regenerate_artifacts.py         # Deterministic artifact generator (committed for Scribe audit)
    ├── corrections_ledger.yaml         # 2100+ corrections tracked with version/source/category
    └── BRIDGE_AUDIT.md                 # Known extraction limitations and edge cases
```

## Key Metrics

| Metric | Value |
|--------|-------|
| Total Module Entries | 178 (in registry; 179 including M3.1 which uses non-bold format) |
| Total Invariants | 45 (INV-0 through INV-44; sub-specs INV-7c/INV-11.8/INV-19.2 do NOT increment count) |
| Total Doctrines | 124 (77 ratified D-1–D-77 + 5 reserved D-78–D-82 + 42 proposed D-83–D-124) |
| TransparencyPacket | v1.6 — 80 fields across 19 categories |
| Total Corrections | 2100+ (tracked in corrections_ledger.yaml) |

## v3.11 Changes (S4 Clarifications + INV-44 + Manus MSG Corrections)

- **INV-44 TOS Compliance:** New invariant added per Microsoft S4 proposal. All routed workloads must pass M142 TOS check. Quarterly re-verification per D-102. Safe Harbor Rule 1 (Azure EA).
- **INV-40/41/42 Measurement Specs:** Formalized with Azure parallels (Continuous Improvement, Knowledge Preservation, Stakeholder Notification).
- **Toolchain Committed:** `regenerate_artifacts.py` now in-repo for Scribe audit and CI gate.
- **Corrections Ledger:** Initialized with version-level tracking of all 2100+ corrections.
- **BRIDGE_AUDIT.md:** Documents known extraction limitations and proposed CI gate.
- **Invariant Count:** 44 → 45 (INV-44 added).

## How to Use

### Module Registry
Each module entry contains:
- `id`: Module identifier (M1-M178, including sub-modules like M3.1, M3a, M6a, etc.)
- `name`: Human-readable module name (canonical from Build Plan)
- `layer`: Architecture layer (L4/L6/L7)
- `status`: SPEC | DELIVERED
- `house`: Primary house assignment (H01-H12)
- `is_sub_module`: Whether this is a sub-module entry

### House Manifests
Each house manifest contains:
- Complete sphere listing (12 spheres per house)
- Modules mapped to that house
- Module count

### 12×12 Matrix
The complete mapping of all modules to all 144 spheres, organized by house.

### Invariant Registry
45 invariants with type (HARD/SOFT), scope, and description. Plus 3 sub-specifications listed separately.

### Doctrine Registry
124 governance doctrines with ratification status (ratified/reserved/proposed) and source version.

### TransparencyPacket Schema
80 fields across 19 categories for the TransparencyPacket v1.6 specification.

### Toolchain
- `regenerate_artifacts.py` — Run to regenerate all artifacts from the Build Plan. Deterministic output.
- `corrections_ledger.yaml` — Machine-readable log of all accepted corrections.
- `BRIDGE_AUDIT.md` — Documents known extraction limitations and edge cases.

## Platform Split (D-123)

Per D-123, artifacts are stored according to their nature:
- **Git (this repository):** Registries (YAML), code (Rust/Python), schemas, build plans (versioned markdown)
- **Notion:** Doctrine prose, Council exchanges, session synthesis, ratification ballots
- **Drive:** Session exports, .docx deliverables, raw artifact backups

## Versioning

These artifacts are generated from the Build Plan and should be regenerated whenever the Build Plan is updated. The generator script is at `toolchain/regenerate_artifacts.py`.

### Propagation Completeness Rule (v3.10+)
Any Build Plan edit is not "applied" until it propagates to ALL downstream artifacts. The proposed CI gate (`toolchain/BRIDGE_AUDIT.md §3`) validates this automatically.

---

*ORC Codebase Artifacts v1.4 — Manus (S7 Build Seat) — April 29, 2026*
