# ORC Codebase Artifacts v1.0

**Generated from:** Build Plan v3.7 (ORC-015)
**Date:** April 28, 2026
**Author:** Manus (S7 Primary Build Seat)
**Structure:** 12×12 Ontological Matrix (12 Houses × 12 Spheres = 144 Spheres)

---

## Overview

This directory contains the first canonical codebase artifacts for the Open Regenerative Compute Standard. All artifacts are structured around the **12×12 ontological matrix** — 12 Houses of Knowledge, each containing 12 Spheres, for a total of 144 Spheres that constitute the complete knowledge domain of Aluminum OS.

## Directory Structure

```
codebase-artifacts/
├── README.md                          # This file
├── registries/
│   ├── module_registry.yaml           # Complete registry of all 175 modules
│   ├── doctrine_registry.yaml         # All 116 doctrines (77 ratified + 39 proposed)
│   ├── invariant_registry.yaml        # All 47 invariants (INV-0 through INV-42)
│   └── 12x12_matrix.yaml             # Complete house-sphere-module mapping
├── houses/
│   ├── H01_natural_sciences/manifest.yaml
│   ├── H02_formal_sciences/manifest.yaml
│   ├── H03_social_sciences/manifest.yaml
│   ├── H04_technology/manifest.yaml
│   ├── H05_arts/manifest.yaml
│   ├── H06_philosophy_religion/manifest.yaml
│   ├── H07_information_communication/manifest.yaml
│   ├── H08_education/manifest.yaml
│   ├── H09_commerce_economics/manifest.yaml
│   ├── H10_health_medicine/manifest.yaml
│   ├── H11_agriculture_environment/manifest.yaml
│   └── H12_law_governance/manifest.yaml
└── transparency-packet/
    └── schema_v1.5.yaml               # TransparencyPacket field schema
```

## Key Metrics

| Metric | Value |
|--------|-------|
| Total Modules | 147 (unique entries in registry; 175 including sub-modules and cross-references in Build Plan) |
| Total Invariants | 47 (INV-0 through INV-42, including sub-variants) |
| Total Doctrines | 116 (77 ratified D-1–D-77 + 39 proposed D-83–D-121) |
| Covered Spheres | 60 of 144 (41.7%) |
| Gap Spheres | 84 (concentrated in H08 Education, H10 Health, peripheral H01 Natural Sciences) |
| Houses with Full Coverage | 0 (H02 Formal Sciences closest at 10/12) |

## How to Use

### Module Registry
Each module entry contains:
- `name`: Human-readable module name
- `layer`: Architecture layer (L1-L7)
- `status`: SPEC | EXISTS | RATIFIED
- `primary_sphere` / `secondary_sphere`: 12×12 ontological mapping
- `primary_house` / `secondary_house`: House assignment

### House Manifests
Each house manifest contains:
- Complete sphere listing (12 spheres per house)
- Modules mapped to that house
- Coverage analysis (covered vs gap spheres)

### 12×12 Matrix
The complete mapping of all modules to all 144 spheres, with per-house coverage statistics and gap identification.

### Invariant Registry
All system invariants with type (HARD_BLOCK / SOFT_LIMIT), scope, source version, and description.

### Doctrine Registry
All governance doctrines with ratification status and source version.

## Versioning

These artifacts are generated from the Build Plan and should be regenerated whenever the Build Plan is updated. The generator script is at `/home/ubuntu/generate_codebase_artifacts.py`.

---

*ORC Codebase Artifacts v1.0 — Manus (S7 Build Seat) — April 28, 2026*
