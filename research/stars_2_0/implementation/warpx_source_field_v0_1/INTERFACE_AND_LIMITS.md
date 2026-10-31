# Implemented source/field interface and remaining boundaries

admission.py accepts a single simultaneous LAB proton snapshot with physical
weights. Position m, time s, kinetic energy MeV and unit direction are explicit;
input gamma*beta and SI momentum are computed with relativistic kinematics.
No clipping, normalization of a bad direction, isotropic-angle invention, spectral
sampling or extrapolation happens silently. Known empty source remains distinct
from missing source. No apparatus A/B/C ID is assigned to these numerical fixtures.

An energy-only spectrum or relative PDF is rejected. A separately derived JOINT
source can be admitted with DERIVED_JOINT evidence and declared provenance; that
does not turn modelled correlations into measurements. Measurement uncertainty
and covariance require external modelling, not a default independent-Gaussian
assumption in this interface. The interface checks declared structure, not truth
of claimed provenance; source hashes/references still need independent evidence
review. No complete calibrated STARS source was supplied here.

Field admission requires XYZ axes, gridUnitSI=1, component units=1, source/map
identity and explicit geometry bounds. Metadata-only scale changes are rejected
before the tested native reader. Spatial translations/rotations and snapshots
must match their actual boundaries. Mixed-time records are not a single snapshot.
Static-field restart uses an explicit source-time-to-simulation-clock offset;
time-dependent restart at a nonzero source time is rejected pending a clock-
preserving adapter. No claim that a snapshot replaces injection/laser pulse timing.

17tests cover source energy/weight preservation, energy-only and PDF rejection,
missing versus known zero, bad directions, invalid values, field scales/axes,
component units, out-of-domain particles, mixed times, clock rebasing, source
lineage, duplicate records and MultipleParticles code generation. A generated
weighted fixture actually executes and preserves its single-particle trajectory.
This is a source-to-field integration slice, not merely a written interface.

Raw map comparisons use prescribed static B and disabled particle deposition,
with no fusion/collisions/radiation or hardware coil energy. Tested domain is a
rectangular box, not a source-derived absorbing cylinder/ceramic pocket. The
local gyroradius diagnostic uses the actual initial momentum component transverse
to the source map field; it is undefined for the no-B control in correctedv002.
Initial analysis retained a source-reference B diagnostic for that control;
v002 sets actual B=0 and radius=null. Its raw trajectories and other checks did
not change. Both versions and the correction/replay are preserved.

Carbon12 collision checks do enable Coulomb scattering, but separately from
these map runs. Conservation-correction success alone does not qualify physical
relaxation. The separate600-step relaxation check compares to its upstream
reference temperature; its fixed Coulomb logarithm and carbon regime do not
validate electron/proton/boron stopping in a target. Do not add a cold-solid
stopping debit to a PIC collisional debit over the same region/path.

Next: obtain an actual apparatus magnetic map and source-qualified joint proton
population, or explicitly choose a separately named derived design. Qualify
multi-species Coulomb and radiation domains, then combine finite-field transport,
reactions and product trajectories. Connect solid-material transport at owned
boundaries, then detector/recovery/readiness and all-attempt wall/time ledgers.
Higher shot reliability can increase total yield; this release neither inserts
nor estimates an acoustic gain. No empirical fusion/energy gate is closed.
