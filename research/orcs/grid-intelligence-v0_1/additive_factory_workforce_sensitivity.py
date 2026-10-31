#!/usr/bin/env python3
"""ORCS speculative additive-factory / field workforce / trade sensitivity.
Arithmetic only, no vendor quotes, no 3D-printed transformer qualified.
Run: python additive_factory_workforce_sensitivity.py --test
     python additive_factory_workforce_sensitivity.py
"""
import argparse
import json
from math import ceil, isclose

TOTAL_UNITS = 38_500_000      # Oldest 55% of assumed 70M national stock
YEARS = 5
SHIFTS_FACTORY_HOURS_YEAR = 6000  # assumed 250 24-hour factory days
FACTORY_OEE = .70              # assumed overall equipment effectiveness
PRINT_FIRST_PASS_YIELD = .90   # assumed qualified yield
HOURS_PER_QUALIFIED_CELL_YEAR = SHIFTS_FACTORY_HOURS_YEAR * FACTORY_OEE * PRINT_FIRST_PASS_YIELD
TRANFORMER_FIELD_INSTALL_SHARE_USD = 4000  # from assumed $8k installed unit split; not quote
FIELD_LABOR_SHARE_OF_INSTALL = .60
FIELD_LOADED_PAY = 120000       # loaded employer labor cost
TRAINING_LABS_B = 3.0
LABOR_SCENARIOS = {
    "1000000 distinct trained field people in 5y": {"unique":1000000,"years_per_person":.5},
    "1000000 distinct field people, 2y average work": {"unique":1000000,"years_per_person":2.0},
    "1000000 simultaneous field jobs for 5y": {"unique":1000000,"years_per_person":5.0},
}
TRAINING_STREAMS = {
    # Cohorts MUST NOT duplicate individuals across streams.
    "new long-cycle supervised field apprentices": (400000, 20000),
    "new supervised field installation and maintenance specialists": (400000, 8000),
    "incumbent grid technician reskilling": (200000, 4000),
}
BROAD_HS8504_IMPORTS_B_ANNUAL = 36.3  # Census Sep2025-Aug2026 broad class, NOT transformer-only
BROAD_HS8504_EXPORTS_B_ANNUAL = 9.2
PRICE_BUILT_BASE_B = 511.06545296 # Previous 38.5M + digital + line + $6B training

def printer_cells(print_hours_per_unit, target_annual_units=TOTAL_UNITS / YEARS):
    """One station's full-cycle processing, assuming no batch sharing."""
    if print_hours_per_unit <= 0: raise ValueError("Positive print-hours required")
    return ceil(target_annual_units * print_hours_per_unit / HOURS_PER_QUALIFIED_CELL_YEAR)

def installation():
    annual_units = TOTAL_UNITS / YEARS
    workdays = 250
    crews = annual_units / workdays / 2.0   # optimistic 2 unit removals+installs per crew-day
    people = crews * 3                      # 3-person crew, excludes scheduling etc
    total_field_labor_budget_b = TOTAL_UNITS * TRANFORMER_FIELD_INSTALL_SHARE_USD * FIELD_LABOR_SHARE_OF_INSTALL / 1e9
    concurrent_equiv = total_field_labor_budget_b * 1e9 / YEARS / FIELD_LOADED_PAY
    return {
        "annual_units_m": annual_units/1e6,
        "units_daily_250_days": annual_units / workdays,
        "assumed_crews_2_units_day": crews,
        "assumed_crew_workers_3_per_crew": people,
        "total_qualified_field_labor_budget_b": total_field_labor_budget_b,
        "field_labor_supported_FTE_per_year_at_120k": concurrent_equiv,
        "warning": "These are NOT all field workers. Substation, line, excavation, QA and grid operations are separate; $4k install split, 60% wage share, 2/day output are invented."
    }

def training():
    n=sum(t[0] for t in TRAINING_STREAMS.values())
    budget=sum(number * unit_price for number,unit_price in TRAINING_STREAMS.values())/1e9+TRAINING_LABS_B
    return {"unique_trained_people":n,"cohort_starts_per_year":n/YEARS,
            "nonwage_training_capital_b":budget,
            "extra_training_vs_prior_6b_b":budget-6,
            "former_program_38_5m_scenario_revised_budget_b":PRICE_BUILT_BASE_B+budget-6,
            "curricula": {k:{"seats":v[0], "nonwage_cost_usd_each":v[1]} for k,v in TRAINING_STREAMS.items()},
            "important": "Graduation/completion is not equal to enrollment; AI tutorship does NOT certify live high-voltage work."}

def workforce_cases():
    vals=[]
    for key,record in LABOR_SCENARIOS.items():
        job_years=record["unique"]*record["years_per_person"]
        vals.append({"name":key,"job_years":job_years,"annual_average_FTE":job_years/YEARS,
                     "five_year_loaded_wage_bill_b":job_years*FIELD_LOADED_PAY/1e9})
    return vals

def import_displacement():
    vals=[]
    for portion in [.10,.25,.50]:
        vals.append({"assumed_substituted_share":portion,
                     "gross_imports_replaced_b_per_year":round(portion*BROAD_HS8504_IMPORTS_B_ANNUAL,3)})
    return {"report_period":"Sep 2025-Aug 2026","imports_b":BROAD_HS8504_IMPORTS_B_ANNUAL,
            "exports_b":BROAD_HS8504_EXPORTS_B_ANNUAL,
            "observed_category_trade_deficit_b":round(BROAD_HS8504_IMPORTS_B_ANNUAL-BROAD_HS8504_EXPORTS_B_ANNUAL,3),
            "scenario_gross_import_substitution":vals,
            "not_net_trade_gain":"Subtract imported raw materials/machines and altered exports; tariffs, prices, substitution and capacity matter. HS8504 contains transformers, static converters, inductors, not just utility power transformers."}

def main():
    print(json.dumps({"status":"SPECULATIVE industrial capacity ledger: no production or labor commitments",
        "print_cells_annual_average_7p7m":[{"effective_print_hours_per_unit":hours,"cells":printer_cells(hours)} for hours in [1,6,24]],
        "field_work":installation(),
        "training":training(),
        "one_million_worker_interpretations":workforce_cases(),
        "trade":import_displacement()},indent=2))

def tests():
    assert printer_cells(6) == 12223
    assert training()["nonwage_training_capital_b"] == 15
    assert isclose(training()["former_program_38_5m_scenario_revised_budget_b"],520.06545296)
    assert isclose(installation()["field_labor_supported_FTE_per_year_at_120k"],154000)
    assert isclose(workforce_cases()[2]["five_year_loaded_wage_bill_b"],600)
    assert isclose(import_displacement()["observed_category_trade_deficit_b"],27.1)
    print("SPECULATIVE arithmetic invariants PASS; no hardware tests")
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--test",action="store_true")
    args=parser.parse_args()
    tests() if args.test else main()
