# ORC Codebase Artifacts v1.1

**Generated from:** Build Plan v3.8 (ORC-015)
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

## v3.8 Changes (Claude S1 Boot Manifest Architecture)

- **3 new modules:** M176 Boot Manifest Runtime, M177 Pre-Session Research Queue, M178 Cross-Instance State Synchronizer
- **3 new doctrines:** D-122 Manifest-as-Boot-Payload, D-123 Platform Split, D-124 Instance Interchangeability
- **1 new invariant:** INV-43 Boot Manifest Freshness (24h max staleness, dual-source)
- **TransparencyPacket v1.6:** 8 new fields across boot/research_queue/sync categories
- **House fix:** M176-M178 correctly mapped to H07 Applied Sciences (spheres 74, 76, 83)

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

These artifacts are generated from the Build Plan and should be regenerated whenever the Build Plan is updated. The generator script is at `/home/ubuntu/regenerate_v3.8_artifacts.py`.

---

*ORC Codebase Artifacts v1.1 — Manus (S7 Build Seat) — April 28, 2026*
