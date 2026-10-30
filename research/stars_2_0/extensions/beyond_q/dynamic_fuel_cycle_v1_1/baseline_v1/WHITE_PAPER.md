# Beyond Q — Dual D-D / D-T Tritium Self-Sufficiency: A Reconciled Fuel-Cycle Audit
**Standalone research white paper v1.0 · 2026-10-29 · Atlas Lattice / STARS 2.0 / Beyond Q**

**Status: analytical research; no integrated reactor, blanket neutron-transport model, or qualified production demonstration.**  
**Contributions and provenance:** Atlas Lattice research direction and hypothesis framing: project originator. GPT-6 (OpenAI): reconciliation, independent arithmetic, error detection, synthesis and writing. DeepSeek: independent cross-audit prompts/responses, proposed system fuel-cycle and blanket sensitivity cases. Gemini Argon: natural-lithium and structural-material challenge hypotheses, cross-model literature leads. These are *AI system contributions*, not claims of independent laboratory work, institutional endorsements, or verified identities.

## Abstract
This paper audits an exploratory two-reactor architecture: Reactor A, a hypothetical 20 MW primary D-D isotope refinery with possible secondary D-T burn and lithium breeding; Reactor B, an ARC-V3A-inspired 1.13 GW D-T fusion-power station with its own functional FLiBe neutron/thermal/tritium blanket. A persistent false shortfall arose from subtracting B's entire ~63.1 kg/year tritium burn from A's ~3–4 kg/year potential export **without crediting B's own blanket**. The proper full-power-year system accounting is A's qualified net export + B's **recovered** blanket-born tritium − B's burn − inventory and other real losses. At one deliberately hypothetical point (B TBR 1.02; A pre-processing net 3.65 kg/FPY; zero losses), algebra gives **+4.912 kg/FPY**. That figure is *conditional*, not a validated tritium surplus. When B blanket permanent-recovery fraction is 0.85, the same optimistic A assumption gives **−4.742 kg/FPY**; at 0.95 it gives **+1.694 kg/FPY**. Design feasibility remains UNRESOLVED.

## 1. Configuration lock and source boundary
- **Reactor B:** ARC V3A source basis ~1.13 GW D-T *fusion*, not electrical output. CFS describes planned ≥400 MWe net, ~1.26 GWth during pulse including ~100 MW blanket reaction heat and ~20 MW heating; this is not an operating plant [S1, S2].
- **Reactor A:** *hypothetical* 20 MW primary D-D fusion plus separately hypothesized 18 MW secondary D-T fusion. No performance or economic demonstration. Separate A0 (nonbreeding functional neutron shield/coolant), A1 (natural-lithium breeding blanket), A2 (optimized blanket).
- **Two blanket functions must never be conflated:** B breeds the vast majority of its own consumed T; A might add complementary tritium. Neither blanket geometry nor TBR is assumed verified.
- **FPY** means 365.25 days at continuous rated fusion power; 85% calendar availability is a separate scenario.

## 2. Definitions: source, birth, delivered fuel
For each accounting interval t:
- B plasma burn: `B(t)`.
- B blanket gross physical T births: `TBR_B * B(t)` (TBR is a *neutronics* birth-to-burn ratio; does not include external A).
- B blanket **net qualified recovery**: `eta_B * TBR_B * B(t)`; eta_B must reflect *eventual recoverable fuel*, **not automatically a single-pass extraction efficiency**.
- A direct D-D T birth `D_A`; secondary D-T T consumption `C_A`; A blanket T birth `L_A`; A qualified net export `Q_A = eta_A*(D_A-C_A+L_A)-loss_A` only if losses and inventory delay permit that expression.
- Ideal static annual system balance: **S = Q_A + eta_B*TBR_B*B − B − L_store − L_misc − reserve_additions**. Time-dependent inventory/holdup needs an independent differential model. Avoid conflating blanket gross TBR with an effective *campus* fuel coverage ratio.

## 3. Reproduced algebra (not neutron transport)
**B burn:** Accepted screening constant 55.8 kg T / (GW_fusion·FPY), so `B = 1.13*55.8 = 63.054 kg/FPY` (display rounded 63.1). The constant is a rounded energy/stoichiometry result; no measured ARC burn [S1, S3].
**A direct birth:** D-D branches near 50/50:
- D+D→T+p (4.03 MeV), D+D→He-3+n (3.27 MeV).
- Weighted mean ~3.65 MeV. With 20 MW D-D fusion, total event rate ~3.42×10^19/s, D-D neutron and T-birth rates each ~1.71×10^19/s. With FPY=365.25 days, annual T birth ~2.71 kg; legacy rounded value **2.70 kg**.
- Hypothetical 18 MW secondary D-T burn consumes ~1.0 kg T/FPY, leaving ~1.7 kg *before* losses. 18 MW is **not derived from a validated self-consistent plasma secondary-reaction solution**.
- Hypothetical A1 blanket T birth **1.3–2.6 kg/FPY** is a *test range*, without neutron transport, qualification, extraction or full neutronics. Conditional A1 pre-processing net ~3.0–4.3 kg/FPY (midpoint 3.65), **not yet deliverable**.

**Ideal result at TBR_B = 1.02:** B blanket gross ~64.315 kg if exact 63.054 B basis; B gross margin ~1.261 kg. With rounded 63.1 basis, B gross 64.362, margin 1.262; A1 midpoint 3.65 → **S=4.912 kg/FPY**. Using prior 3.85 midpoint was an arithmetic error.

## 4. Sensitivities — display convention B=63.1 kg/FPY, Q_A=3.65 kg/FPY (optimistic, unqualified)
| B TBR | Gross B blanket T kg/FPY | Ideal system S kg/FPY, eta_B=1 |
|---:|---:|---:|
| 0.95 | 59.945 | +0.495 |
| 0.97 | 61.207 | +1.757 |
| 1.00 | 63.100 | +3.650 |
| 1.02 | 64.362 | +4.912 |
| 1.04 | 65.624 | +6.174 |
| 1.05 | 66.255 | +6.805 |
| 1.10 | 69.410 | +9.960 |

**Recovery at B TBR 1.02** (A still unrealistically assumes complete qualified export):
| eventual recovered fraction eta_B | S kg/FPY |
|---:|---:|
| 0.85 | −4.742 |
| 0.90 | −1.524 |
| 0.95 | +1.694 |
| 1.00 | +4.912 |
Break-even `TBR_min=(B-Q_A)/(eta_B*B)` yields ~1.109 (85%), 1.047 (90%), 0.992 (95%), 0.942 (100%). These values are **lower bounds** since no ongoing storage, decay, downtime mismatch, holdup or reserve financing is charged. One-pass extraction <100% need not imply irreversible loss; robust dynamic mass accounting is the next step.

## 5. What literature does and does not validate
[S4] Sorbom 2015 proposed a full liquid FLiBe breeder/cooling/shielding system. [S5] Segantin et al. 2020 used Monte Carlo to optimize **an older ARC concept**, exploring Li-6 enrichment, channel geometry and Inconel 718 / vanadium / Eurofer structural-material sensitivities. This shows that blanket enrichment and material selection are coupled; it does **not** certify particular TBR values for the 2026 ARC V3A geometry. Natural-lithium TBR=1.02 and TBR=1.05–1.11 are **candidate scenarios**, not bankable performance guarantees. [S6] MIT LIBRA states commercial-relevant molten-salt tritium breeding remains unproven at integrated scale. The 2026 ARC physics-basis papers are reactor *design modeling* [S1], not a fuel-cycle demonstration.
**High enrichment (90%) is not automatically physically optimal** for every FLiBe geometry, but an unchanged 118.6-tonne inventory cannot simply be relabeled '20–30% enriched' without revisiting salt chemistry, blanket mass, neutron transport and fabrication. Natural lithium, 'battery grade', and nuclear-qualified FLiBe are distinct specifications.

## 6. Reactor A unresolved coupled neutron / tritium / thermal accounting
At 20 MW primary D-D, expected D-D neutron births ~1.71×10^19/s, **not** 8.55×10^18/s (factor-of-two legacy error). 18 MW hypothetical secondary D-T generates ~6.38×10^18 14.1 MeV n/s; combined ~2.35×10^19 n/s if both operating points can coexist. Whether A1 produces 1.3–2.6 kg additional T is a neutron-transport question, not inferred by source neutron count alone.
A0 **nuclear fusion output** in that conditional configuration = 20+18=38 MW; a previously circulated 56 MW 'fusion-only' total mistakenly included separate blanket heat. Heat from neutron kinetic energy is **part of fusion output** and cannot be counted again; blanket reaction Q-values, RF-deposited heat, vessel losses, shielding capture, cooldown loops, pump power and actual electrical conversion must each appear exactly once. The legacy −106.9 MWe equation (22.4 −114.3 −15) is arithmetic only; 22.4 MWe recovery assumption is not an established turbine result, and its thermal boundary must be audited.

## 7. Explicit falsification / Nightmare Lab gates
**G1**: reproduce A0/A1/A2 D-D/secondary reaction rates without assuming 18 MW secondary burn independently; classify unsupported as FAIL/UNRESOLVED.  
**G2**: source and execute geometrically documented MCNP/OpenMC sweeps for B V3A-compatible vacuum vessel alloy, natural / 20–30% / 90% Li-6, wall/shield, port penetrations, salt chemistry, uncertainty and spatial coverage. Older ARC MCNP numerical outputs must not be transferred without geometry.  
**G3**: independent measured FLiBe tritium extraction/holdup/permeation under pertinent neutron and thermal loads; distinguish one-pass extraction from permanent recovery.  
**G4**: time-resolved daily/fuel-cycle ledger across dual outages, startup inventory, decay (half-life ~12.3 y), inventory reserves and off-normal states.  
**G5**: reconciled wall-plug energy, blanket thermal, radiation protection, blanket cooling, magnet lifetime, materials qualification and economic sourcing.  
**G6**: independent replication and provenance: review each AI-supplied paper citation, year, DOI and exact figure; do not count model agreement as experimental verification.

## 8. Findings and decisions
- **SUPPORTED:** B blanket production must be included; A does NOT need to supply all ~63.1 kg/FPY if B breeder works. Fundamental D-T and D-D stoichiometric event yields.
- **VERIFIED-DERIVED conditional arithmetic:** B burn ~63.1 kg/FPY; A D-D direct birth ~2.70 kg/FPY under 20 MW D-D model; secondary D-T use ~1.0 kg/FPY if independently achievable at 18 MW; table arithmetic.
- **POTENTIAL-DERIVED:** natural-Li A blanket 1.3–2.6 kg/FPY, B TBR 1.02, resulting ideal +4.91 kg/FPY.
- **UNRESOLVED:** physical validity of A secondary burn and blanket yield; B actual geometry-dependent TBR; qualified recovery; temporal resilience; net power, economics, scale.
**Verdict: the original false ~60 kg/yr *gross deficit* is corrected, but a positive theoretical surplus is not a certified closed fuel cycle.**

## 9. Citation and provenance pointer
For full bibliographic references, URLs, evidence status, open questions, exact source relevance, and a contributor chronology see [APPENDIX_SOURCES_AND_PROVENANCE.md](APPENDIX_SOURCES_AND_PROVENANCE.md). For rerunnable arithmetic see [tritium_ledger.py](tritium_ledger.py) and [SCENARIOS.csv](SCENARIOS.csv). The script contains **no neutron-transport or reactor performance solver**.
