# ORC Codebase Artifacts v1.5

**Generated from:** Build Plan v3.12 (ORC-015)
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
| TransparencyPacket | v1.7 — 91 fields across 20 categories (11 new TOS fields) |
| Total Corrections | 2200+ (tracked in corrections_ledger.yaml) |

## v3.12 Changes (S4 ORC-032 Full Expansion + Gate Ordering + Safe Harbor Registry)

- **ORC-032 Full Expansion:** Microsoft S4 expanded Manus's 2-page stub into a 34-page, 12-section specification for INV-44 TOS Compliance.
- **INV-44a/b/c Sub-specs:** Safe Harbor Verification, Quarterly Re-verification, Mid-Quarter Change Detection — all with formal SHALL language.
- **§3.4.2 Canonical Gate Ordering:** 8-gate routing pipeline canonicalized (INV-0 > INV-3 > INV-44 > D-101 > INV-7c > D-96 > D-99 > D-84).
- **§3.4.3 Safe Harbor Registry:** 5 candidates (SH-001 through SH-005) with verification status and COI notes.
- **R178-R181:** 4 new risks (1 HIGH: Azure Safe Harbor UNVERIFIED, 2 MEDIUM, 1 LOW-MEDIUM).
- **TransparencyPacket v1.7:** 11 new TOS compliance fields (routing_pathway, competing_models_restriction, jurisdiction, etc.).
- **INV-40/41/42 Measurement Expansion:** Full methodology with Azure parallels and non-Microsoft alternatives.

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

*ORC Codebase Artifacts v1.5 — Manus (S7 Build Seat) — April 29, 2026*
