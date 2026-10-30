# Atlas Lattice — Physical, Economic & Evidence Provenance Protocol
**v0.1 · 2026-10-30 · PROPOSED research design; no deployed chain, stablecoin accounts, external parties or implemented settlement**
**Origin:** Author proposal of blockchain-anchored USD stablecoin settlements and AI review of both campus-internal and external monetary flows; Copilot's three-boundary provenance graph and examples; primary-source regulatory/NIST review. Companion: [third-party JV 50-year economics](BQ_50_YEAR_THIRD_PARTY_JV_COMMUNITY_PHYSICS_ECONOMICS_WHITE_PAPER_v0_1_2026-10-30.md), [modular contracts](../atlas_lattice_modular_testbed_v0_1/MODULE_CONTRACTS_AND_JV_GOVERNANCE.md).

## Three auditable boundaries
1. **Physical:** matter, species, water, heat quality, electricity, goods, component lifecycle; conservation laws.
2. **Economic:** external revenues/costs, internal transfer pricing, settlement fees, taxes, capital, cash, reserves and liabilities; cancel intra-campus payments on consolidation.
3. **Epistemic:** evidence that the input, transformation and output measurements are genuine and fit the required quality/uncertainty. Source-graded parameters NEVER automatically inherit a stronger grade from a downstream reproduced computation.

## Digital receipt / physical digital twin interface
Required fields: `event_id, parent_event_ids, contract_id, operator_from, operator_to, location_zone, species_or_sku, quantity, unit, purity_or_specification, measurement_method, sensor_id, calibration_version, uncertainty, capture_timestamp_utc, signed_at_utc, evidence_type, evidence_gate, source_reference, custody_marker, independent_qc, corrective_revision_id, bill_id, fiat_amount, tax_currency, settlement_mode, tx_hash_optional, confirmation_state, disclosure_class`.
Sign each receipt through authenticated operator and, where critical, separate metrology/witness keys. Hash-chain versioned **off-chain source records**; on-chain only selected timestamps, digests and permitted settlement proofs. Design for corrections: append a reversing/replacement event linked to original rather than deleting; never promise an error-free or invulnerable immutable ledger.
**NIST context:** NISTIR 8419 (2022) https://doi.org/10.6028/NIST.IR.8419 and NISTIR 8536 (Sep 2026) https://csrc.nist.gov/pubs/ir/8536/final discuss physical-digital anchors and common traceability data across manufacturing ecosystems. A valid hash cannot prove an inaccurate physical sensor measurement was true.

## Stablecoin payment option; compliance gate
The US GENIUS Act became law July 18 2025. OCC **final rule Oct 21 2026, effective Jan 18 2027**, https://occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-50.html ; the rule concerns authorized stablecoin issuance and related custody/supervision. It **does not require** settlement in stablecoins, validate every token, or remove accounting, sanctions, custody, fraud, data privacy, issuer, redemption or bank-availability risk. Where used, choose legal issuer and permitted arrangement only after legal compliance review; fiat bank, tokenized deposits and off-chain payments remain viable alternate settlement modes. No Atlas token assumed or issued.
Track stablecoin network, chain ID, issuing entity, reserve/redemption status and fees; don't infer physical movement from a coin movement, and don't infer identity/beneficial ownership solely from public wallet traces.
Avoid publishing private business data, employee financial information, dangerous industrial control parameters or precise residential records to irreversible public chains. Use role-based access, minimal hashes, confidential proofs or permissioned ledger where justified, while preserving audit rights.

## Example (entirely hypothetical, not actual deliveries)
Water provider reports **100 m3** filtered process water at **$1.50/m3** ($150 internal invoice), lab QC confirms specified water quality, recipient flow meter agrees within stated uncertainty; receipt hash gets anchored. Payment could be bank transfer or eligible stablecoin with transaction ID linked to invoice after separate confirmation. Partner A's +$150 internal sale and partner B's -$150 purchase cancel at consolidated campus boundary. Water mass does not cancel as a waste/loss if it remains within campus; transfer bookkeeping net cancels.
If independent calibration later finds actual delivery **96 m3**, append correction and refund/credit under contract; original signature remains visible but superseded for current truth.

## AI analysis: roles, controls, audit
AI may compare imports/exports, detect price anomalies, circular transfer inflation, double-counted heat or avoided purchases, mismatched units, understated chemical residuals, missing lot provenance, sudden sensor drift, operator self-dealing, and abnormal inflow/outflow of funds. Treat anomaly flags as **triage**, not allegations of crime or conclusive fraud. A qualified human and separate reviewer determine accounting dispositions.
Nightmare Lab attacks: (i) signed erroneous sensor reading, (ii) identity spoofing, (iii) nonexistent water sold, (iv) false high-grade heat delivery, (v) asset double counting, (vi) stale chain/finality/reorg, (vii) failed redemption, (viii) omitted offchain settlement, (ix) privacy leakage, (x) corrupt evidence upgrade.
**Rule:** Do not make blockchain the industrial-control system or AI the sole certifier of safety, identity, funds compliance or physical conservation.

## Experimental comparison cases
P0 signed central database + independent audit; P1 distributed tamper-evident audit anchoring; P2 legal stablecoin settlement plus P1 evidence; P3 hybrid confidential data and public commitments. Compare throughput, audit latency, error/reversal resolution, costs, cybersecurity, interoperability and the actual improvement in detected discrepancies. **A blockchain is an option whose benefits must pass comparative tests, not an assumed necessity.**

## Concrete next deliverables
1. CSV/JSON synthetic ledger with calibration and settlement revisions.
2. Reproducible campus consolidation eliminating all internal transfers.
3. Constraint checks for physical conservation, correct evidence inheritance, exact units and double-entry reconciliation.
4. Stablecoin versus fiat sensitivity: fees, custody loss, interest opportunity cost, operational continuity, regulations and reconciliation.
5. Joint sign-off from independent operator/accountant/safety reviewer before SYSTEM-INTEGRATED status.

**Epistemic invariant:** Permanent evidence of a statement ≠ permanent evidence that the statement was true.
