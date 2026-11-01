# Reconcile the original roughly350k/350k benchmark with the simulator

1 November 2026. User-directed audit of the existing v1.9 result. Neither the
initial calculation nor the simulator is assumed wrong. **Physics inputs,
controller and original simulation outputs are unchanged.** Git hashes prove
that `inputs.json`, `target_controller.py` and `run.py` still match commit
`094b88fe1b1250dc87bd0dd050bb96b4c3a0edde`.

## The result already approximately agrees

| Operating year | He-3 captured, STP L | T recovered, atom-equivalent STP L |
|---|---:|---:|
|1|352,578.510|350,838.212|
|2|352,580.837|352,739.581|
|3|352,580.837|352,739.581|

Year1 is approximately0.737% above350k for He-3 and0.239% above350k for T. The
small overshoots are not evidence that the earlier rough calculation failed.
The controller intentionally pursues350k minimum targets, so this agreement is
a consistency check, not an independent prediction of an achieved reactor yield.
The exact original350k operating-input sheet remains unresolved; do not invent
its parameters or silently replace it with the later simulator's assumptions.

## Equal branch births are preserved

The model's equal D-D branch convention gives the same born atom count in
the He-3+n and T+p branches. In operating year1, each branch births approximately
**388,921.095 atom-equivalent STP liters**. Before internal reaction and extraction
paths, no discrepancy exists in the50:50 source ledger.

As a matched-path algebraic control,388,888.889 liters born in each branch,
with the same90% recovery and no differing secondary burn/latency, gives exactly
350,000 liters of each coproduct. This demonstrates the initial relationship
without asserting that those are the original historical inputs or validated
reactor recoveries.

## Trace the year1 difference instead of forcing a match

He-3 is captured through the assumed90% collection route:

`350,028.986 L from this year's births + 2,549.525 L from net startup collection-pipeline carry = 352,578.510 L captured`.

T follows its own route, with candidate secondary D-T consumption and processing:

| T route term, atom-equivalent STP L | Year1 |
|---|---:|
| Direct DD T births |+388,921.095|
| A secondary DT consumption |−20,289.447|
| Permanent A processing loss |−18,465.169|
| Decay while in A plasma/processing route |−14.222|
| Starting minus ending A route inventory |+685.955|
| Recovered T to storage |350,838.212|

The two processing paths hold different inventories at the end of A-only
startup. Material crosses into the operating year at different rates. Thus
*births during the year* and *deliveries during the year* need not have exactly
the same volume ratio, even with equal source branches. Startup stocks are
retained, not discarded or treated as fresh source production.

This explains the approximately1,740.298-liter He-3-minus-T delivery difference
in year1 under the existing assumptions. All terms are exported in
`outputs/capture_difference_bridge.csv`; no recovery coefficient was tuned.
Molecular T2 volume is a separate reporting option; **it is not the cause of
this small discrepancy**, which is calculated on the same atom-equivalent
basis for both isotopes throughout.

## Why years2/3 are even closer

The assumed eventual He-3 capture fraction is0.900000. The candidate T path's
secondary-burn survival, independent95% processing recovery and route decay
combine to an eventual fraction of approximately**0.900405208**. After the
startup pipeline difference clears, T delivery is consequently only about
**0.0450% higher** than He-3 capture. That near equality follows from the
chosen path assumptions; it is not a universal law for a plasma or extractor.

The steady-route approximation and finite dynamic ratio differ by about
2.05e-9 in absolute ratio. That tiny disagreement is retained in
`capture_benchmark.json`, not eliminated by changing the physics. The exact
route replay reproduces the archived A pipeline/recovery states within
1.12e-16kg. The yearly flow identities close to about1e-6 STP L over a roughly
390k-liter source; this is numerical accounting, not experimental precision.

## Verification and limits

`reconcile_350k.py` replays just the unchanged reference case. It reconstructs
A's plasma/process route and its decay from explicit compartment flows and
independently advances the He-3 collection account from recorded births. It
uses the same numerical compartment kernel, so this is a bookkeeping audit,
not independent nuclear-data or reactor validation.

Three new tests verify unchanged baseline hashes, equal births/route identities
and reproduction of the existing deliveries. The original12 tests also pass:
15 combined checks. An initial test incorrectly demanded equality between an
asymptotic estimate and the finite-time result at1e-10 relative tolerance;
the actual difference was~2e-9. Its failure log is retained. The revised check
verifies the exact archived replay and preserves the asymptotic disagreement
as a reported result, rather than forcing finite dynamics to equal the limit.

```bash
python reconcile_350k.py
python -m unittest discover -v
```

**Disposition:** keep roughly350k He-3 and350k T as the explicit coproduct
benchmark. Compare calculations at matched fusion power, time window, birth
versus delivery boundary, recovery and internal-use assumptions. The missing
original input sheet remains an ancestry question, not a declaration of an
arithmetic or physics error. Physical G1-G5 stay OPEN.
