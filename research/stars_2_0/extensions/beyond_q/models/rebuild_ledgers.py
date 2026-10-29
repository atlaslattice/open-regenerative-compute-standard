"""Conditional accounting, not an ARC operating-point prediction. Stdlib only."""
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EV_J = 1.602176634e-19
NA = 6.02214076e23
# Rounded reaction energies; measured distributions/reactivities are not modeled.
Q_DD_HE3 = 3.27
Q_DD_T = 4.03
Q_DT = 17.6
MOLAR_MASS = {"T": 3.016, "He3": 3.016, "He4": 4.003}  # g/mol, rounded
R = 8.31446261815324  # J/(mol K)


def write_csv(path, rows):
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def mass_kg(atoms, species):
    return atoms / NA * MOLAR_MASS[species] / 1000


def dd_births(power_mw, cf, he3_branch=0.5):
    if power_mw < 0 or not 0 <= cf <= 1 or not 0 <= he3_branch <= 1:
        raise ValueError("Invalid power, availability or branch fraction")
    q = he3_branch * Q_DD_HE3 + (1-he3_branch) * Q_DD_T
    events = power_mw * 1e6 * 365*86400 * cf / (q * 1e6 * EV_J)
    return events * he3_branch, events * (1-he3_branch)


def dt_burn(power_mw, cf):
    if power_mw < 0 or not 0 <= cf <= 1:
        raise ValueError("Invalid D-T power or availability")
    return power_mw * 1e6 * 365*86400 * cf / (Q_DT * 1e6 * EV_J)


def main():
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    assumptions = json.loads((ROOT / "models/assumptions_v0_1.json").read_text())
    pdd=assumptions['DD_primary_power_MW']
    pdt=assumptions['DT_fusion_power_MW']
    cf=assumptions['capacity_factor_each']
    branch=assumptions['DD_He3_branch_fraction']
    rec=assumptions['recovery_and_qualification']
    survival=assumptions['secondary_isotope_survival_base_case']
    h_atoms, t_atoms = dd_births(pdd, cf, branch)
    dt_atoms = dt_burn(pdt, cf)
    recovered_t = mass_kg(t_atoms, "T") * rec * survival
    recovered_h = mass_kg(h_atoms, "He3") * rec * survival
    # No secondary burn credited: explicitly a primary-only accounting scenario.
    # No extra T from Li credited: transport qualification is absent.
    summary = {
        "quantity_status": "DERIVED_CONDITIONAL_PRIMARY_ONLY",
        "dd_T_born_kg_year": mass_kg(t_atoms, "T"),
        "dd_He3_born_kg_year": mass_kg(h_atoms, "He3"),
        "dd_deuterium_consumed_kg_year": (h_atoms+t_atoms)*2/NA*2.014/1000,
        "dd_T_recovered_kg_year": recovered_t,
        "dd_He3_recovered_kg_year": recovered_h,
        "dd_He3_recovered_liters_273_15K_101325Pa": h_atoms*rec*survival/NA*R*273.15/101325*1000,
        "dt_T_burn_kg_year": mass_kg(dt_atoms, "T"),
        "direct_T_fraction_of_DT_burn": recovered_t / mass_kg(dt_atoms, "T"),
        "unclosed_T_balance_kg_year_before_decay_reserves_losses": mass_kg(dt_atoms, "T")-recovered_t,
        "primary_DD_MW_for_direct_T_balance_same_cf_recovery": pdd*mass_kg(dt_atoms, "T")/recovered_t,
        "recovered_capex_ancestor_USD": 5.87e9,
        "recomputed_capex_descendant_USD": 2.8e9+2.8e9+150e6-200e6+120e6,
        "DD_on_state_primary_neutron_power_MW": pdd*branch*2.45/(branch*Q_DD_HE3+(1-branch)*Q_DD_T),
        "DD_on_state_primary_charged_power_MW": pdd-pdd*branch*2.45/(branch*Q_DD_HE3+(1-branch)*Q_DD_T),
        "energy_ledger_status": "INCOMPLETE: heating/secondary/blanket/recovery/conversion/auxiliaries UNKNOWN",
        "thermal_105MW_ancestry": "UNKNOWN",
        "net_minus40MWe_ancestry": "UNKNOWN",
        "net_campus_export_status": "NOT_REPRODUCED",
        "ROI_status": "NOT_COMPUTED: unresolved energy and cost inputs",
    }
    (out / "primary_balance_v0_1.json").write_text(json.dumps(summary, indent=2)+"\n")
    rows=[]
    for power in [10, 25, 50, 100, 250, 500]:
        for survival in [.2, .4, .6, .8, 1.0]:
            for recovery in [.2, .4, .6, .8, .95]:
                h,t = dd_births(power,cf,branch)
                rows.append({"DD_primary_MW":power,"isotope_survival_assumed":survival,
                    "recovery_qualification_assumed":recovery,
                    "T_kg_year":mass_kg(t,"T")*survival*recovery,
                    "He3_kg_year":mass_kg(h,"He3")*survival*recovery,
                    "T_offset_fraction":mass_kg(t,"T")*survival*recovery/mass_kg(dt_atoms,"T"),
                    "evidence":"PARAMETRIC_NOT_OPERATING_POINTS"})
    write_csv(out / "survival_recovery_sensitivity_v0_1.csv", rows)
    # Twenty-year PHYSICAL demand/production ledger; deficit is not a purchase.
    # No startup inventory, reserve or processing latency is imputed as available.
    rows=[]
    retained_h=0.0
    for year in range(1,21):
        new_h=recovered_h
        retained_h += new_h*assumptions['internal_He3_allocation']
        rows.append({"year":year,"DD_T_recovered_kg":recovered_t,
            "DT_T_required_kg":mass_kg(dt_atoms,"T"),
            "unclosed_T_requirement_kg":mass_kg(dt_atoms,"T")-recovered_t,
            "He3_qualified_kg_primary_only":new_h,
            "He3_internal_allocation_kg":new_h*assumptions['internal_He3_allocation'],
            "He3_external_allocation_kg":new_h*assumptions['external_He3_allocation'],
            "He3_retained_no_use_no_loss_stock_kg":retained_h,
            "external_He3_sales_kg":"UNKNOWN",
            "startup_inventory_kg":"UNKNOWN","reserve_kg":"UNKNOWN",
            "processing_latency":"UNKNOWN","tritium_decay_kg":"UNKNOWN",
            "availability_status":"annual_scenario_no_dispatch_model",
            "operational_fuel_closure":"NOT_ESTABLISHED"})
    write_csv(out / "twenty_year_primary_only_v0_1.csv",rows)
    receipt={"code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "assumptions_sha256":hashlib.sha256((ROOT / "models/assumptions_v0_1.json").read_bytes()).hexdigest(),
        "outputs":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.glob('*')) if p.name!='run_receipt_v0_1.json'},
        "scope":"arithmetic and conditional stoichiometry only; no engineering validation",
        "inputs":assumptions}
    (out / "run_receipt_v0_1.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
