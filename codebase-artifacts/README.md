# ORC Codebase Artifacts — 12×12+1 Ontological Filesystem

**Version:** 3.14 (Multi-Seat Innovation Convergence)
**Generated from:** `COMPLETE_BUILD_PLAN_v3.14.md`
**Date:** April 29, 2026

---

## Structure

The codebase is organized by the **144+1 sphere ontology** — 12 Houses × 12 Spheres + Element 145.

```
codebase-artifacts/
├── houses/
│   ├── H01_philosophy_logic/
│   │   ├── S01_formal_logic_proof_theory/
│   │   │   └── manifest.yaml          ← Sphere manifest (modules, invariants, status)
│   │   ├── S02_epistemology_knowledge_systems/
│   │   │   └── manifest.yaml
│   │   ├── ... (12 spheres per house)
│   │   └── manifest.yaml              ← House-level manifest (totals, coverage)
│   ├── H02_formal_sciences/
│   ├── ... (12 houses)
│   └── H12_law_governance/
├── element-145/
│   └── manifest.yaml                  ← Unified Sovereign Kernel
├── registries/
│   ├── module_registry.yaml           ← All 182 modules with sphere assignments
│   ├── invariant_registry.yaml        ← All 51 invariant entries (45 canonical + sub-specs)
│   ├── doctrine_registry.yaml         ← All 125 doctrines (77 ratified + 48 proposed)
│   └── 12x12_matrix.yaml             ← Coverage heat map (74/144 = 51.4%)
├── toolchain/
│   ├── corrections_ledger.yaml        ← Queryable corrections log
│   └── BRIDGE_AUDIT.md                ← Known extraction limitations
└── README.md                          ← This file
```

## Canonical Counts

| Category | Count | Notes |
|----------|-------|-------|
| Houses | 12 | H01-H12 |
| Spheres | 144 (+1) | 12 per house + Element 145 |
| Populated Spheres | 74/144 (51.4%) | At least 1 module or invariant |
| Modules | 182 | Including sub-modules (M3.1, M6a/b/c, M25a/b/c, etc.) |
| Invariants | 51 entries | 45 canonical (INV-0..44) + 6 sub-specs |
| Doctrines | 125 | 77 ratified + 48 proposed (D-78-D-82 promoted from RESERVED) |

## Numbering Is Locked

From v3.14 forward, numbering is immutable. We only add, never renumber. The numbering doesn't matter as much as the actual code — what matters is the ontological placement.

## Coverage by House

| House | Populated Spheres | Modules | Invariants |
|-------|-------------------|---------|------------|
| H01 Philosophy & Logic | 2/12 | 3 | 5 |
| H02 Formal Sciences | 12/12 | 92 | 14 |
| H03 Natural Sciences | 2/12 | 2 | 2 |
| H04 Technology & Engineering | 12/12 | 26 | 9 |
| H05 Arts & Creative Expression | 10/12 | 21 | 1 |
| H06 Humanities & Culture | 2/12 | 0 | 2 |
| H07 Applied Sciences | 5/12 | 8 | 2 |
| H08 Education & Pedagogy | 2/12 | 0 | 2 |
| H09 Life Sciences | 2/12 | 2 | 1 |
| H10 Health & Medicine | 2/12 | 1 | 1 |
| H11 Social Sciences | 5/12 | 3 | 5 |
| H12 Law & Governance | 12/12 | 20 | 7 |

## Regeneration

```bash
python3 build_12x12_codebase.py
```

The generator script is the single source of truth for sphere assignments. To add a module, add it to `MODULE_ASSIGNMENTS` in the script and re-run.

---

*Codebase Artifacts v1.7 — 12×12+1 Ontological Filesystem — April 29, 2026*
