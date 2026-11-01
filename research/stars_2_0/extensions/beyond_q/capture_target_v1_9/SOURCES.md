# v1.9 source register

- **Pinned research implementation:** parent commit
  `717d0e3da8b9e726b1861ef557d03a2c3d463655`, specifically v1.8's policy-capable
  fuel engine and v1.7's scenario/energy adapters. `source_manifest.json` checks
  exact Git bytes; `outputs/source_sha256.json` records consumed source hashes.
  New target logic is in `target_controller.py`; no reactor physics was fitted
  to350k output. See the neighboring v1.7/v1.8 source registers and reports for
  full underlying transport, kinetics, fuel-cycle and numerical limitations.

- **Owner-corrected ARC design lock:**
  https://github.com/atlaslattice/open-regenerative-compute-standard/blob/6fb057618d6d6ff0ce813a99d9edf9d1485561d5/research/stars_2_0/extensions/beyond_q/ARC_DUAL_REACTOR_CANONICAL_BASELINE_2026-10-31.md.
  Two proposed1100MW fusion sources; A+20MW net is owner-historical/unvalidated.
  Laser is a separate comparison variant. This is project direction, not a
  CFS-published DD retrofit or an achieved plant operating point.

- **J.C. Hillesheim et al. (2026),** *Overview of the physics basis for the ARC
  fusion power plant*, Journal of Plasma Physics92,E69.
  https://doi.org/10.1017/S0022377826101706.
  Source of the nominal900s flattop/60s interval and D-T design energy reference.
  The inspected publication states breeding above unity without the exact
  numerical ARC V3A TBR assumed in this suite. Its D-T plant figures do not
  establish DD performance or a laser electrical balance.

- **NIST Physical Measurement Laboratory**, *Atomic Weights and Isotopic
  Compositions*, helium and hydrogen tables:
  https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=He and
  https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=H.
  Neutral-isotope mass conventions are inherited consistently; Avogadro's
  constant converts atoms to mol. STP convention0C/1atm and22.414L/mol is fixed
  in the output definitions. Atom-equivalent T liters and physical T2 liters
  remain different quantities, independent of recovery or market value.

All capture, processing, duty-transfer, reserve, energy and product-acceptance
parameters are inherited candidates or assumed scenarios unless explicitly
source-traced. Actual isotope grade, demand, price, revenue and profitability
remain unresolved. Sources are not endorsers of this architecture.
