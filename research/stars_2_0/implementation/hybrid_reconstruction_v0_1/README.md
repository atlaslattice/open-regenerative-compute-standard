# Stellar Forge — hybrid reconstruction v0.1

2026-10-30 UTC. Append-only recovery and numerical audit. No scientific freeze, no merge, no promotion of a hybrid gain into the Stars reference. Three apparatus identities are retained in APPARATUS_RECOVERY_REGISTRY_v0_2.json.

## What was recovered and reproduced

Nine original Python programs executed successfully in a new environment, with unchanged source bytes. **All 11 recovered CSV outputs were byte-identical**, including 12 reduced source/mirror scenarios, eight three-module mirror scenarios, 18 industrial scaling scenarios, and acoustic/mechanical/particle proxy outputs through v0.12. This is stronger than numerical agreement, but is not a reconstruction of the original software environment or proof of physical validity. Original environment lockfiles and execution logs were not recovered.

The search recovered 13 historical ZIP packages and additional scripts, CSVs and reports: 24 original Library files in PROVENANCE.json. The ZIP inventories also preserve older v0.1–v0.5 acoustic work and other research toys; not every inventoried archive was rerun. The executable package selects v0.6, v0.7, v0.8, v0.10, v0.11 and v0.12, plus three mirror/scaling programs. No v0.9 source package was recovered in this search. Original publication-source commit IDs for the Library-only scripts are unknown; their exact hashes and file identities are recorded instead.

**The latest reported complete high-output hybrid run remains unrecovered.** The recovered programs establish that historical numerical work happened. None of the recovered programs couples the entire proposed acoustic/laser/hollow-sphere/catcher/rotating-mirror/ash/recovery/industrial apparatus. That distinction neither disproves the project lead's reported later run nor licenses calling the recovered submodels that run.

## Replay

Use Python 3.12.14 and requirements.txt for the reconstruction environment. In a clean container where `/mnt/data` does not already exist:

```bash
python replay_originals.py --out /tmp/stellar-forge-replay-001
python audit_and_ablate.py --out /tmp/stellar-forge-audit-001
```

Each output directory must be new. The replay refuses an existing `/mnt/data`; it temporarily aliases that path to its fresh output directory because several original scripts hard-code it. It never edits the original scripts. It stages the toy CSV before running the scaling script, and stages the **recovered original** v0.11 prerequisite for the v0.12 historical cross-check. Its separately saved v0.11 replay output is compared before using that original prerequisite. Commands, hashes, dependency versions, return codes and CSV comparisons are recorded in REPLAY_RECEIPT.json.

Two large original outputs (v0.8 shot_samples.csv and v0.6 numerical_receipt.json) are inventoried rather than duplicated in this compact package; unchanged programs regenerate them. All eleven original CSV SHA256 values are in GOLDEN_CSV_HASHES.json. The missing large shot CSV is verified by hash. PNGs, ZIP container timestamps and every generated report are **not** claimed byte-identical. Original figure/ZIP hashes remain in RECOVERED_FILE_INVENTORY.json.

See [RECONSTRUCTION_REPORT.md](RECONSTRUCTION_REPORT.md), [MODULE_ABLATION_MATRIX.csv](MODULE_ABLATION_MATRIX.csv), [PROVENANCE.json](PROVENANCE.json), and [UNRESOLVED_PHYSICS.md](UNRESOLVED_PHYSICS.md).
