# ORC Codebase Artifacts v1.3

**Generated from:** Build Plan v3.10 (ORC-015)
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
│   ├── invariant_registry.yaml        # 44 invariants (INV-0..43) + 3 sub-specs
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
| Total Module Entries | 178 (in registry; 179 including M3.1 which uses non-bold format) |
| Total Invariants | 44 (INV-0 through INV-43; sub-specs INV-7c/INV-11.8/INV-19.2 do NOT increment count) |
| Total Doctrines | 124 (77 ratified D-1–D-77 + 5 reserved D-78–D-82 + 42 proposed D-83–D-124) |
| TransparencyPacket | v1.6 — 80 fields across 19 categories |

## v3.10 Changes (Claude S1 Scribe Verification)

- **Module Count Audit Table:** Rewritten with dual-column (Integer Slots vs Entries) and counting rule blockquote. Total corrected to 179 entries (176 L4 + 3 L6/L7).
- **Doctrine Registry:** Full rewrite with canonical names from §14 (previously used stubs). D-78-D-82 RESERVED entries added.
- **Invariant Registry:** Count corrected to 44. INV-40/41/42 added. Sub-specs (INV-7c, INV-11.8, INV-19.2) explicitly listed as non-counting.
- **§0.1 Invariant Definition:** Rewritten to enumerate INV-0..43 = 44 total.
- **Metadata:** All version headers corrected to 3.10.
- **Counting Rule (v3.10):** Count by MODULE ENTRY — each distinct module ID = 1 entry.

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
44 invariants with type (HARD/SOFT), scope, and description. Plus 3 sub-specifications listed separately.

### Doctrine Registry
124 governance doctrines with ratification status (ratified/reserved/proposed) and source version.

### TransparencyPacket Schema
80 fields across 19 categories for the TransparencyPacket v1.6 specification.

## Platform Split (D-123)

Per D-123, artifacts are stored according to their nature:
- **Git (this repository):** Registries (YAML), code (Rust/Python), schemas, build plans (versioned markdown)
- **Notion:** Doctrine prose, Council exchanges, session synthesis, ratification ballots
- **Drive:** Session exports, .docx deliverables, raw artifact backups

## Versioning

These artifacts are generated from the Build Plan and should be regenerated whenever the Build Plan is updated. The generator script is at `/home/ubuntu/regenerate_v3.10_artifacts.py`.

---

*ORC Codebase Artifacts v1.3 — Manus (S7 Build Seat) — April 29, 2026*
