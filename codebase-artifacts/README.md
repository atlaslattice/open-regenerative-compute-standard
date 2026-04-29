# ORC Codebase Artifacts v1.2

**Generated from:** Build Plan v3.9 (ORC-015)
**Date:** April 28, 2026
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
│   ├── module_registry.yaml           # Complete registry of all 178 modules
│   ├── doctrine_registry.yaml         # All 119 doctrines (77 ratified + 42 proposed)
│   ├── invariant_registry.yaml        # All 47 invariants (INV-0 through INV-43)
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
└── transparency-packet/
    └── schema_v1.6.yaml               # TransparencyPacket field schema
```

## Key Metrics

| Metric | Value |
|--------|-------|
| Total Modules | 176 (unique entries in registry; 178 including sub-modules in Build Plan) |
| Total Invariants | 47 (INV-0 through INV-43, including sub-variants) |
| Total Doctrines | 119 (77 ratified D-1–D-77 + 42 proposed D-83–D-124) |
| Covered Spheres | 21 of 144 (14.6%) |
| Gap Spheres | 123 (concentrated in H03, H08 Education, H10 Health) |
| TransparencyPacket | v1.6 — 76 fields across 19 categories |

## v3.9 Changes (Claude S1 Scribe Audit — 9 Edits)

- **Status:** CANONICAL → PROVISIONAL-CANONICAL (42 unratified doctrines)
- **§3.4.1 Module Count Audit Table:** 18-row breakdown of all module ranges M1-M178
- **D-78-D-82 RESERVED:** Intentional gap between ratified and proposed corpus documented
- **Invariant count:** Corrected from 45 to 44 (INV-7c/INV-19.2 are sub-specs per §0.1)
- **M16→M80 pointer fix:** Epistemic Weather correctly referenced in M173/M177
- **M178 overclaim tightened:** "instance becomes interchangeable" → "instance state symmetry"
- **Boot Protocol v2 Fallback Clause:** D-122 binding only after M176 DELIVERED
- **§0.2 rule downgrade:** "must be executable" → "target state" with current-state annotation

## How to Use

### Module Registry
Each module entry contains:
- `id`: Module identifier (M1-M178)
- `name`: Human-readable module name
- `layer`: Architecture layer (L4/L6/L7)
- `status`: SPEC | DELIVERED
- `house`: Primary house assignment (H01-H12)
- `spheres`: Mapped sphere IDs from the 12×12 matrix

### House Manifests
Each house manifest contains:
- Complete sphere listing (12 spheres per house)
- Modules mapped to that house
- Coverage analysis (covered vs gap spheres)

### 12×12 Matrix
The complete mapping of all modules to all 144 spheres, with per-house coverage statistics and gap identification.

### Invariant Registry
All system invariants with type (HARD/SOFT), scope, and description.

### Doctrine Registry
All governance doctrines with ratification status and source version.

### TransparencyPacket Schema
All field categories and individual fields for the TransparencyPacket v1.6 specification.

## Platform Split (D-123)

Per D-123, artifacts are stored according to their nature:
- **Git (this repository):** Registries (YAML), code (Rust/Python), schemas, build plans (versioned markdown)
- **Notion:** Doctrine prose, Council exchanges, session synthesis, ratification ballots
- **Drive:** Session exports, .docx deliverables, raw artifact backups

## Versioning

These artifacts are generated from the Build Plan and should be regenerated whenever the Build Plan is updated. The generator script is at `/home/ubuntu/regenerate_v3.9_artifacts.py`.

---

*ORC Codebase Artifacts v1.2 — Manus (S7 Build Seat) — April 28, 2026*
