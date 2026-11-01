# Correction: source-conversion and auxiliary loss recovery

The initial beam-boundary expression `B + Q - B/eta` did not include electrical recovery of source-conversion losses. It is a valid bound only when those losses receive no electrical credit (and the listed auxiliary/storage assumptions hold). Calling it a universal whole-facility bound would be too broad. That interpretation is withdrawn here; earlier generated files are preserved as development history.

The current entrypoints are accounting_v004.py, run_v006.py, pipeline_v004.py and PROFILE_v003.json. The current executed result is pipeline_run004. Intermediate code/receipts are not the current facility model. No actual apparatus gain was reported in those earlier records; facility inputs remained unknown.

With beam energy B, gross source efficiency eta, source remainder L = B/eta - B, and an explicitly justified electrical recovery fraction r_s, the source-only balance is:

`net = E_downstream + r_s*L - B/eta - net_auxiliary_draw`.

If downstream recovery is perfect (`E_downstream=B+Q`), auxiliary net draw is zero and storage is cyclic:

`net = Q - (1-r_s)*B*(1/eta-1)`.

The approximately99.9994% source-efficiency threshold from this control applies to r_s=0, not to every possible recovery boundary. At r_s=1 the energy-only upper limit is Q, regardless of eta. That perfect-recovery case does not establish thermal/exergy feasibility: temperatures, rejection sinks, transport, parasitic draw and electrical conversion remain unresolved. No remainder is assumed to be heat, and no thermal energy is automatically credited as electricity.

The current model also allows each auxiliary to recover only its OWN supplied wall energy, and keeps source idle/preparation draw separate from firing-dependent source input. These credits cannot re-credit energy already assigned to beam/alpha recovery. Source idle draw remains payable on nonfiring attempts. A complete cyclic facility with all input energy hypothetically returned has net at most its modeled Q; that is an energy-only envelope, not a power prediction.

Profiles and pipeline runs001/002 predate source-loss recovery; run003 adds it; run004 also explicitly separates source idle/preparation costs. They are retained, not overwritten or promoted to current results. The particle/source/target computations are unchanged by this accounting correction.
