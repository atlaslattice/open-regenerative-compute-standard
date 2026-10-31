# Beyond Q v1.4.1 — A-first startup and one-year fuel planning

Conditional arithmetic extension of v1.4, parent PR #51. The power basis is the
current repository design input: A=1.1GW gross DD, B=1.1GW gross DT. No laser
operating point, qualified recovery, net electricity or operational self-sufficiency
is established. All physical gates remain open.

Run with the v1.4 environment from this directory:

```bash
python calculate.py
python no_breeding_control.py
python -m unittest test_startup -v
```

The module imports the unchanged neighboring v1.4 engine. One FPY is365.25 days
or8766 hours. Initial inventories are zero in the staged A-first runs. A operates
alone until the selected B-start time, then A and B operate for one FPY with
all stocks carried continuously across the transition. There is no restart
that silently discards processing inventory.

## Two distinct startup policies

1. **Bank the whole year:** isolate B, credit neither future A delivery nor B
   breeding, and calculate initial B storage required to burn for a full FPY.
   Separately model A-only charging of that bank. Other A inventory is not
   claimed destroyed or included in the isolated B-bank requirement.
2. **A replenishes while B runs:** find a whole-hour B-start time at1h steps,
   refine the operating year at15min steps, and search back to the preceding
   failed whole-hour start. These are conditional fuel-availability boundaries,
   not physical safety limits or regulatory reserves.

The staged scenarios retain v1.4's hypothetical A0/A1/A2 and B blanket responses.
An additional A0+B-TBR0 adverse control credits **no breeding in either reactor**.
All recovery, escape, extraction, processing and reserve assumptions remain
uncalibrated; no forced positive fuel balance or experimental validation follows.

## Numerical results

B's full-power burn is **61.65398kg T/FPY**. An isolated B bank of approximately
**64.46kg** supplies that year under the stated5% pass burn,4/day processing,
0.9999 permanent processing recovery and radioactive-decay assumptions. The
hourly bank requirement comprises61.654kg burned,1.817kg decay,0.117kg processing
loss and0.871kg left in mobile stocks. The selected bank also serves the year
at15min refinement. This includes no regulatory or outage reserve and no
purity qualification. It is not a promise of continued operation after that year.

A-only charging to the same B-storage target takes approximately:

| A case | A-only charging time |
|---|---:|
| A0, no A blanket breeding |180days|
| A1, inherited natural-Li testbed response |98days|
| A2, inherited exploratory enriched-grid response |91days|

A1/A2 speedups depend on unqualified spherical-testbed neutron yields and
assumed route recovery. They are not demonstrated laser blanket performance.

If A keeps operating, the bank need not hold a full year's fuel before B
starts. With **both blankets credited zero breeding**, the tested A0 control
starts B after **76h (~3.17days)** of A-only operation, with~0.637kg in B storage
plus other A/processing stocks. It then serves one full B FPY, with no material
unserved burn and~70.0kg growth in total mobile T inventory during that year.
The initial reserve is very small and assumption-sensitive; no outage reserve
or engineering startup qualification is implied. Broader inventory growth is
not qualified export.

The separate inherited-breeding-credit cases allow tested B starts around3days
(A0),2days(A1) and approximately2days(A2); full outputs and boundary tests are
in startup_policies.csv and startup_boundary_check.csv. They are not needed to
make the zero-breeding-control arithmetic positive.

## Why annual arithmetic can be positive

At the prescribed1.1GW DD gross power and equal branches, gross direct T birth
is148.645kg/FPY. The v1.4 candidate5.21685% secondary burn consumes7.755kg,
leaving140.891kg before recovery. Assumed95% A plasma-derived recovery screens
at133.846kg/FPY, before inventory decay and delays. This is~2.17times B's burn
requirement without either blanket. The zero-breeding dynamic control includes
processing/decay and still has a positive conditional one-year stock change.

These are consequences of assumed gross fusion power and recovery. Changing
internal T burn, achieved DD power, availability, purity, permanent recovery or
losses can erase the balance. There were no laser-driven reactor simulations
in v1.4; its actual WarpX runs were bounded collision/drag tests.

A finite bank can supply one year even if future production is insufficient.
Indefinite operation requires a sustainable qualified supply rate, reserves
for credible outages, replacements and a viable electrical/thermal boundary.
Positive isotope arithmetic does not establish those requirements. Gross He3
coproduction is a separate nuclear source calculation; recoverable/purity-
qualified He3 is not modeled by these T stocks and is not asserted as surplus.

## Evidence and provenance

POTENTIAL-DERIVED: all reactor-power and startup results. VERIFIED-DERIVED:
conditional reaction bookkeeping, clock conversion and regression identities.
SOURCE-TRACED: [v1.4 report](../multiscale_v1_4/REPORT.md), its inputs/code and
[parent power correction](../DUAL_LASER_POWER_BASIS_LOCK_2026-10-30.md).
UNRESOLVED: actual reactor/laser operation, extraction qualification and all
physical gates. No external experimental evidence is generated here.

Eight numerical regressions pass. CSVs, assumptions, bank/refinement and raw
staged-stock trajectories are retained. The15min search corrected an initial
coarse start boundary: an earlier hour also served the year, so the search now
continues backward until the preceding tested hour fails. The refinement is
not hidden by calling the first passing coarse result a precise minimum.

Dave Sheldon/Atlas Lattice research direction; inherited GPT-6/Tidal Lantern,
DeepSeek and Gemini Argon analytical contributions are credited according to
the existing source register. No institutional or experimental endorsement.
