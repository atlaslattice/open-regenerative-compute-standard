# THE IRON EMPIRE — Public Continuity Guard v0.1

**PROPOSED FICTION · source-index engineering · NOT CANON-RATIFIED · 22 November 2026**

This file is a small additive companion to the public Iron Empire story sources. It reconciles the scope of a later author-directed correction without rewriting or erasing earlier editions. No private Lore Foundry, Play/Brain messages, characters, permissions or unpublished Restoration Atlas content are copied here.

## Development chronology (not a final screenplay)

| Story component | Source precedence | Working placement |
| --- | --- | --- |
| Distant anomaly and Imperial arrival | Public six-film treatment v0.4 | Human anomaly detection in **2062**; damaged fleet unexpectedly emerges in **2069** |
| Full Imperial accounting audit | Author correction v0.5 | **Film II**, expressly published on the Emperor's authority after reconciliation |
| Ancient Mars | Author correction dated **2026-11-06** | **Film II** partly prequel: ancient gardens, bug invasion, self-glassing, exile and agricultural amnesia |
| Major restoration of Mars | Same **2026-11-06** correction | **Film III**: Steve and former executioner/Minister of Trees work with Cydonian and other partners; ecologies recover slowly |
| Emperor assassinated and heir exiled | v0.5 | **Film III**; these events can coexist with Mars restoration, exact in-film order still open |
| Prince remains uncrowned | v0.5 | **Film V**, even after the prince stops a rogue strike with independent allies |
| Coronation and adversary species' self-name | v0.4 + v0.5 + v0.6 | **Film VI only**; no premature official naming |
| Prince's age | v0.6 | Extended fictional physiology plus substantial suspended animation; exact dates not adopted |

**Specific unresolved collision:** Film III must carry both the largest Mars restoration storyline and the Emperor's assassination/coup. Neither needs to happen instantaneously. The prince's rescue, treatment of surviving Cydonian jurisdictions and restoration consent rules still need authored ordering. The newer Mars delta says **AUTHOR-DIRECTED CONTINUITY DELTA / NOT APPLIED TO EXISTING BIBLE**, so do not silently rewrite v0.4.

## Source provenance — all four files already public

All paths are inside docs/fiction/iron_empire/ in this repository.

- Six-film treatment v0.4 — Git blob **7fdaf3fbeb01b7f0d140d921ef24ba3fe8d45310**.
- Imperial accounting / assassination / prince v0.5 — Git blob **8aac5934bdc7f41c2b91524c06cc85ba774d2ad1**.
- Imperial longevity / suspended animation v0.6 — Git blob **a0b5795128ef6f3cc51d516375c5be5579b1735f**.
- Mars Garden prequel / restoration chronology delta, 2026-11-06 — Git blob **046caeec8ec5a5b8070c15b7086532af3380c07a**.

These were read from GitHub on November 22, 2026. No unpublished author material is treated as a public source.

## Reproducible local guard

Run from the repository root:

    python tools/fiction/iron_empire_public_guard.py --root . --json
    python -m unittest discover -s tests/fiction -v

The source-local command checks **14 defined source anchors**, fails closed on missing files, and prints its exact results. The tests use **synthetic fixtures** and deliberately mutate chronology. The same 14 regexes were separately checked against actual connector-read public GitHub contents and returned **14/14 matches** on November 22. This is only a presence audit, not full script continuity proof. CI, merges, publication, rights and canon ratification remain independently gated.

## Open author decisions

Decide where the Film III Mars restoration scenes occur relative to the assassination and prince's departure; specify the Cydonian and other survivor consent treaties; maintain the unpublished 14-item editorial decision register separately. A GitHub merge does **not** grant story rights, assent from contributors, or canon authority. Earlier editions remain independently attributable and reversible.
