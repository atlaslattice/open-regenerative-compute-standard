# Output schema

`A0_daily.csv`, `A1_daily.csv`, `A2_daily.csv`: one end-of-day row, with day
starting at 1; schedule.csv uses the same displayed indexing. All source,
sink and transfer columns are **cumulative from day zero**, not rates and
not new fuel available to spend. Differences between rows give interval flows.

| Columns | Units / meaning |
|---|---|
| day | elapsed calendar days |
| on_a, on_b | requested binary daily operation; B can be fuel limited |
| a_plasma, a_blanket, b_blanket, a_process, b_process, a_store, b_store | current kg-T inventory in disjoint compartments |
| dd_birth | cumulative primary D-D T birth kg |
| blanket_a_birth, blanket_b_birth | cumulative assumed blanket T birth kg, with actual source/burn |
| a_burn, b_burn | cumulative T consumed kg, never deliverable |
| decay | cumulative kg-T-equivalent decayed across stocks; He3 mass not computed |
| permeation | cumulative T kg irreversibly lost from blankets in this model |
| process_loss | cumulative T kg irreversibly lost during processing |
| a_to_b, b_to_a | cumulative storage-to-storage transfer kg; neither source nor sink globally |
| a_extracted, b_extracted | cumulative salt-to-processing transfer kg; material remains in total inventory until burned/lost/decayed |
| b_feed, b_recirculated | cumulative feed and unburned processing-return kg; b_feed=b_burn+b_recirculated |
| a_processed, b_processed | cumulative processing-to-storage kg; can include previously circulated atoms more than once; never add these as nuclear births |
| b_unserved_burn | cumulative requested minus actual B T burn kg, not negative stock |
| dd_events, dd_t_atoms | cumulative primary D-D reactions and T-branch atoms |
| total_inventory | sum of seven stocks in kg-T |
| mass_residual_kg | initial+births-consumption-losses-final, kg; must be numerically zero |

`case_ledgers.csv` and `case_summaries.json` contain cumulative source neutron
counts and energy J. Energy fields `fusion_neutron_j` and `fusion_charged_j`
partition `fusion_j`. `assumed_blanket_reaction_q_j` is additional reaction Q,
not neutron kinetic energy. `nuclear_release_j` is their nonduplicated source
sum, **not deposited heat**. `qualified_usable_surplus_kg=null` (empty in CSV)
and `self_sufficiency=UNRESOLVED` are intentional evidence limits, never zero.
Neutron fate, deposited heat and net-electric status fields remain unresolved.

`ensemble.csv` records each actual draw, schedule seed and outcome.
`scenario_bounds.json` reports sampled min/5/50/95/max quantiles only, no
measurement-based confidence claim. `sensitivity.csv` isolates each named
parameter at the same outage schedule. `timestep_refinement.csv` differences
are relative to the finest included step, not a certified exact solution.

`argon_table_audit.csv` uses the legacy 63.1 kg B display convention.
Its 0.1/pass case yields ~1.177 kg/FPY when decay is retained, vs ~1.179
when eta is rounded to .942 as in Argon's table. This small difference is
preserved; it is not evidence for a real net surplus.

`run_manifest.json` records hashes of source/input documents, baseline snapshot
and runtime. Source files in external `--input` are additionally hashed by the
invoked-input digest. `A*_input.json` records each realized case configuration.
OpenMC provenance has a separate preflight output; no transport results exist.
