# Beyond Q v1.7 continuation

Read REPORT.md and SOURCES.md, then inputs.json. This is the paired conditional
annual accounting package, not an achieved reactor or a new WarpX/OpenMC run.

Canonical purpose: direct DD He3 coproduct may fund A; DD tritium supplies B
startup/makeup/reserves. B has its own lithium breeding at assumed gross TBR1
in the default; processing losses remain. No T sales. T-decay He3 is uncredited.

Do not confuse primary fusion MW with net electric MW, nor source FPY with
calendar uptime. ARC400MW is pulse-averaged net after ARC's own loads. A retrofit
net draw is unknown; numeric stress cases are not a recovered engineering design.
The source input now supports ARC1100/1130 and matched1100/1100 alongside laser.

Completed: A0/A1/A2 and B replacement scenarios, inherited response and all-zero
breeding controls, independent/correlated outages and cold startup; explicit
helium4 candidate capture; startup/year energy separation; common CSVs, offline
dashboard, report, 16 tests and timestep comparison.

Next critical inputs:
1. Recover the actual ARC-DD retrofit engineering power budget and cost ancestry.
2. Qualify B gross TBR vs eventual delivered fuel, avoiding B gross birth counted
   again as delivered recirculation or as assumed surplus.
3. Laser distributions, gain, repetition rate and on-target/wall-plug data.
4. D-He3 burn and measured helium collection/cleanup/quality acceptance; certify
   He4 product before research-grade claims; cooling energy is separate.
5. Include full costs and external isotope demand curves; A dispatch should
   respond to fuel reserves and real He3 demand, rather than run all year by fiat.
6. Simulate multiple years with repairs, reserve draws and replacements, then
   revisit any indefinite-operation claim.

Failure controls show positive annual stock can coexist with temporary B
starvation. The default breeding case survives the tested A90day interruption;
this does not validate assumed TBR/recovery. All physical G1-G5 remain OPEN.

Official ARC materials specify TBR>1 and future-startup supply, not a precise V3A value or literally zero surplus. Keep TBR1 as the conservative scenario; exact current numeric specification remains unresolved.
