# Pocket/reference causal comparison v0.1 — proposal, not prediction lock

Use six local cells: REF_OFF, REF_SHAM, REF_ON, POCKET_OFF, POCKET_SHAM,
POCKET_ON. They are nested within a specified pB apparatus and do not relabel
A=new hybrid, B=integrated hybrid or C=original STARS.

First compare transport under matched *incident proton phase space* and B11
inventory/areal density, characterizing all backing and acceptance. A later
end-to-end apparatus comparison holds the externally supplied drive conditions
fixed and lets proton source changes be measured mediators. Fixing proton output
in that later comparison would remove a possible acoustic mechanism. Report
both comparisons; neither is a substitute for the other. Equal total boron
inventory, equal line-of-sight areal density and equal geometric thickness are
not generally simultaneously achievable for unlike 3D targets; declare the
matching estimand and report the other differences explicitly.

Predeclare success threshold and measurement basis before revealing outcomes.
Report yield per attempted shot including aborts, conditional successful-shot
yield, unsuccessful-shot yield, timing bias/jitter, born/escaped/detected alphas,
useful electricity, total wall input, cycle time and target survival. A success
threshold alone must not suppress the continuous yield distribution. Log target
readiness, time-to-readiness, laser trigger and actual firing separately.

Separate target batches and entire calibration/experimental campaigns for held-out
validation. Randomize treatment within eligible blocks with recorded independent
seeds. No final holdout tuning. Tolerance/jitter distributions must be recovered
from measurements or explicitly sourced derived estimates; none are supplied in
this release. Use paired nuisance realizations for numerical contrasts when
appropriate, with distinct reproducible random streams for sampling processes;
paired numerical ensembles do not simulate independent laboratory replication.
Sham matching must specify thermal/electrical/EMP/mechanical equivalence and
which coherent target motion is suppressed; a generic drive-off condition does
not qualify automatically. If simultaneous matching is infeasible, use additional
controls and report the identifiable estimand.

Estimate geometry×acoustic interaction as
(POCKET_ON-POCKET_SHAM) - (REF_ON-REF_SHAM), with outcome units and grouped
uncertainty. OFF comparisons diagnose sham effects separately. Never multiply
component gain claims. Independent model-discrepancy/holdout checks precede
optimization. Sample size and detectable effect await calibrated variance,
clustering, missingness and scientific success criteria; no arbitrary n or
assumed 10/30/100% gain is frozen here.

Proposed falsifiers: no reproducible state change; state change but no useful
proton/alpha change; improvement only in detector acceptance; improved conditional
yield but reduced all-attempt yield; net benefit erased by preparation cost,
downtime or damage; benefit vanishing on grouped holdouts. Preserve all outcomes.
