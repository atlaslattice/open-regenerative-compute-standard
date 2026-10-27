# Atlas Lattice Research Lineage v0.1 — INV0-WIZ research alias

**Status:** working GitHub-hosted research prototype. **Not an amendment to the Aluminum OS Canon.**

**User-approved subtext:** *Reality may defeat a wizard, but it cannot delete their commit history.* 🧙

## Canon reconciliation / old source drift

The actual Aluminum OS website invariant registry in [Invariants.tsx](https://github.com/atlaslattice/aluminum-os/blob/main/website/client/src/pages/Invariants.tsx) names **INV-0: System Integrity** (governing amendment of the 12-House/144-Sphere ontology). The canonical audit also identifies **INV-17: Zero Erasure** and **INV-19: Audit Immutability** in [CANON_AUDIT.md](https://github.com/atlaslattice/aluminum-os/blob/main/docs/canon/CANON_AUDIT.md). However, older ORCS codebase syntheses call a quantum dual-use screening field `inv0_cleared` and describe an **INV-0 Do No Harm** gate. These are **inconsistent historical uses** across project records. The origin of the conflict (including whether a particular model introduced it) has not been proved. Never overwrite the existing numbered Canon based on this project-specific nickname.

**INV0-WIZ** is therefore a *project-specific alias* to the existing Zero Erasure/Audit Immutability principles, **not** an official `INV-0` replacement. Governance records requiring formal amendment should be reconciled with the actual signed canonical registry independently.

## Real outputs in this directory

1. [atlas_research_lineage_v0_1.json](atlas_research_lineage_v0_1.json) — a seed ancestry data graph containing six actual STARS documents/tools, explicit parent IDs and zero fictional PASS or FAIL receipts. It is **not** a complete registry of all Atlas Lattice historical experiments.
2. [validate_lineage.py](validate_lineage.py) — basic standard-library structural lint checking parent existence, cycles, unique IDs, receipt prerequisites and **ancestor immutability** if an old JSON snapshot is supplied.
3. [lineage_viewer.html](lineage_viewer.html) — a self-contained, small mobile-readable interactive HTML snapshot with search, type filter, ancestor/descendant detail and archive links. **This is a static embedded snapshot**, not an automated GitHub Pages deployment or GitHub API client. GitHub's code viewer may display its HTML source rather than run it; download the HTML and open locally, or host it on a normal static web host to use the interactions.

## Reproducible validation commands

```bash
python research/lineage/validate_lineage.py research/lineage/atlas_research_lineage_v0_1.json

# Freeze prior JSON separately. On next generation, compare against snapshot:
python research/lineage/validate_lineage.py research/lineage/atlas_research_lineage_v0_2.json \
  --ancestor research/lineage/atlas_research_lineage_v0_1.json
```

Structural lint **does not** prove timestamps, independent signatures, clinical/security safety, accuracy of linked content or experimental success. Commit hashes (and, for high-assurance use, independently signed/timestamped snapshots) should anchor immutable records. For stronger append-only enforcement use CI with a signed prior snapshot and a policy protecting the main branch; a locally supplied `--ancestor` file is not an adversarial trust boundary.

## Proposed event lifecycle (implementing the Copilot tree)

```text
prediction_v1
   |
   +-- frozen-prediction receipt (protocol hash + code/source/data versions)
   |        |
   |        +-- PASS -> separate validation receipt
   |        +-- FAIL -> separate failure receipt
   |        +-- INCONCLUSIVE -> separate inconclusive receipt
   |
   +-- prediction_v2
            |-- parent_id = prediction_v1
            |-- change summary
            |-- previous receipts never altered
            |-- evidence credentials reset unless independently earned
            +-- fresh experiment + fresh commitment required
```

The graph currently has **no actual experimental receipts**. Later results must never be entered just because a model asserts success.

## Sensitive data / retractions

Keep *public* immutable references where appropriate, but when a historical artifact exposes secrets or poses a serious risk, restrict access and append a dated reason/redaction/tombstone record. **Do not claim public Git history can always preserve both complete secrecy and full bytes forever.** Sensitive raw datasets may require an access-controlled vault or a safer redacted derivative, with a cryptographic provenance reference. Scientific failure should not be confused with a safety or privacy exception.

## What it would take to be production-ready

- Freeze a typed JSON schema and immutable ID conventions; retain separately signed data and validation receipts.
- Test schema against malformed inputs, cycles, duplicated receipts, mutation and missing required proof.
- Add GitHub Actions CI checks that compare current graph with protected historical snapshot.
- Render automatically from committed JSON rather than manually embedding six initial nodes.
- Add actual public experimental data only when the G0-B protocol has passed formal freeze, detector qualification, acquisition and independent unblinding.
- Reconcile central Aluminum OS Canon names/status via authenticated governance procedure.

**History immutable. Confidence revisable. Hats under peer review.**
