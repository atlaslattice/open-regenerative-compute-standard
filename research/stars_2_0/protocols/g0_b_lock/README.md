# G0-B Validation Lockfile v0.1 — proposed freeze manifest

Copilot's Oct 27 round-six review recommended a compact human/machine-readable lockfile. This directory provides a **DRAFT template and basic fail-closed completeness checker**; neither constitutes actual preregistration or makes an experiment successful.

- [JSON template](G0_B_VALIDATION_LOCKFILE_TEMPLATE_v0_1.json) — identifies protocol/model versions, original nuclear/stop/detector data hashes, materials, thickness positions, primary observables, preselected thresholds, exclusions, randomization custodian, blind dataset digest, unblinding authorization and failure criteria. Empty fields remain `null`.
- [check_g0_b_lock.py](check_g0_b_lock.py) — standard-library structural lint. Run:
  ```bash
  python check_g0_b_lock.py G0_B_VALIDATION_LOCKFILE_TEMPLATE_v0_1.json
  ```
  The draft deliberately exits code 2 and prints `BLOCKED`. It checks required keys and hash *formats*, not actual remote hashes, independent custodian signatures, randomization integrity, science quality, or actual dataset secrecy.

## Recommended freeze lifecycle
1. **DRAFT:** complete instrument/model/source description and numeric acceptance criteria, with independent review. Never fabricate missing quantities.
2. **READY_FOR_FREEZE:** source/codes and model predictions are versioned, independent sign-offs documented, and blind custodian assigned. External registry/escrow or repository commit locks the complete **immutable JSON bytes** and links model/prediction hashes. The template's internal `lockfile_sha256` must not be represented as a self-contained byte hash of a file that contains its own hash; hash the artifact **outside** it (in a signed external receipt).
3. **FROZEN:** no model or scoring alterations; data-acquisition proceeds according to frozen protocol. Pre-existing public validation information must not leak into calibration/training.
4. **DATA COMMITMENT:** on acquisition, the independent data custodian computes and publishes/escrows the raw blind-dataset hash **before unblinding**. Because that hash may not exist at initial freeze, put it in a *separate signed, append-only post-acquisition receipt* rather than modifying the original locked manifest in place.
5. **UNBLINDED:** only after frozen predictions, protocol, scorer and acquired blind data are separately hashed and independently approved; append an authorization/receipt that references the frozen version.
6. **PASS/FAIL:** apply original scoring criteria and publish failures. Revision after unblinding requires a **new model generation and fresh blind experiment**.

**Caution about checker:** It has a conservative mode system, but `FROZEN` means only that required format fields are populated; the checker does not validate a time-stamped registry, actual source licenses or signatures. Gate status is determined by independent custodians using evidence, not by this script's success alone.

**Primary protocol:** [G0-B v0.1](../G0_B_BLINDED_PROTON_TRANSMISSION_AND_ALPHA_ESCAPE_PROTOCOL_v0_1_2026-10-27.md).

**Other reusable research branches:** Nuclear-data source ledger and normalization code can reuse the same lockfile/hashing pattern, but physical detector calibration and blinded validation are domain-specific.
