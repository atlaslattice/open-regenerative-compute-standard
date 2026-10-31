#!/usr/bin/env python3
"""ORCS five-year manufacturing/fiscal benchmark, 2026-10-31.
Reproducible hypothetical costs, NOT empirical performance or a factory test.
No real transformer efficiency, safety certification, procurement or hiring.
The output is sensitive to assumptions and is not a forecast.
Python 3 stdlib only; run --test for arithmetic invariants.
"""
from dataclasses import dataclass
from math import ceil, isclose
import argparse
import json

# Primary sources: 2025 Annual US BEA trade, BLS Sept 2026 Employment
# (released Oct 2 2026), 2025 DOL UI, CBO 2026 Economic Outlook,
# USDA ERS FY2025 SNAP, SSA 2025 SSI report.
BASELINE = {
 "unemployed_sept_2026_m": 7.109,
 "not_labor_force_wants_job_m": 5.790,
 "involuntary_part_time_m": 4.5,
 "u3_rate_sept_2026": 0.042,
 "regular_ui_benefits_2025_b": 34.4,
 "regular_ui_beneficiaries_cy2025_m": 5.3,
 "snap_2025_b": 101.7,
 "ssi_2025_b": 65.0,
 "income_security_2025_b": 397.0,
 "federal_medicaid_2025_b": 668.0,
 "merchandise_imports_2025_b": 3438.4,
 "merchandise_deficit_2025_b": 1240.9,
 "goods_services_deficit_2025_b": 901.5,
}
# Does NOT add CBO income-security to constituent SNAP, UI, SSI totals.

TARGET_QUALIFIED_UNITS_PER_YEAR = 7_700_000
MACHINE_SCHEDULED_HOURS_PER_YEAR = 8760 # 3 x 8h shifts, seven days a week
OEE = .70
LABOR_RELIEF_FTES_PER_24_7_POST = 5.25
MACHINES_PER_WATCH_POST = 12

@dataclass(frozen=True)
class Factory:
    name: str
    qualified_yield: float
    purchased_materials_per_attempt: float
    additive_hours_per_attempt: float
    additive_cost_per_hour: float
    automation_per_attempt: float
    human_labor_per_attempt: float
    postprocessing_per_attempt: float
    certified_testing_per_attempt: float
    printing_machine_hours_per_unit: float
    def assess(self):
        if not 0 < self.qualified_yield <= 1:
            raise ValueError("Valid yield required")
        costs = (self.purchased_materials_per_attempt +
                 self.additive_hours_per_attempt*self.additive_cost_per_hour +
                 self.automation_per_attempt + self.human_labor_per_attempt +
                 self.postprocessing_per_attempt + self.certified_testing_per_attempt)
        qualified_unit_cost = costs / self.qualified_yield
        cells = ceil(TARGET_QUALIFIED_UNITS_PER_YEAR * self.printing_machine_hours_per_unit /
                    (MACHINE_SCHEDULED_HOURS_PER_YEAR * OEE * self.qualified_yield)) if self.printing_machine_hours_per_unit else 0
        posts = ceil(cells/MACHINES_PER_WATCH_POST)
        return {
            "factory_process":self.name,
            "status":"HYPOTHETICAL ASSUMPTION",
            "direct_factory_cost_per_accepted_unit_usd":round(qualified_unit_cost,2),
            "cost_for_7p7m_qualified_units_b":round(qualified_unit_cost*TARGET_QUALIFIED_UNITS_PER_YEAR/1e9,3),
            "illustrative_qualified_additive_print_cells":cells,
            "monitoring_FTE_at_5p25_per_post":ceil(posts*LABOR_RELIEF_FTES_PER_24_7_POST),
            "not_included":"factory-conversion CAPEX beyond assumed machine hourly charges; engineering, certification program, freight, installation, utility outage, financing, landfill handling, environmental permits; NO measured actual losses/reliability"
        }

# All three MUST ultimately pass same independent distribution transformer's
# voltage-class, kVA, BIL, dielectric, impulse, thermal, fault, loss and
# equipment-class DOE efficiency/field acceptance standards.
FACTORIES = (
 Factory("Automated conventional", .98, 1800, 0,0,260,400,180,220,0),
 Factory("Hybrid additive/robotic", .94, 1900,4,100,150,180,220,250,4),
 Factory("Maximum additive, research only",.85,2000,18,100,220,110,500,340,18)
)

def hybrid_breakeven_additive_hours():
    conv=FACTORIES[0].assess()["direct_factory_cost_per_accepted_unit_usd"]
    h=FACTORIES[1]
    cost_without_print = (h.purchased_materials_per_attempt+h.automation_per_attempt+
                          h.human_labor_per_attempt+h.postprocessing_per_attempt+h.certified_testing_per_attempt)
    threshold=(conv*h.qualified_yield-cost_without_print)/h.additive_cost_per_hour
    return {"hybrid_print_hours_to_match_conventional_cost":round(threshold,2),
            "at_usd_per_machine_hour":h.additive_cost_per_hour,
            "warning":"Below-zero threshold would mean hybrid cannot match even with zero print time; does not include differential upfront factory tooling investment."}

def hiring_case(net_additional_workers, mean_wage_usd=60000, ui_share=.25,benefit_spell_avoided_fraction=.50,
                additional_manufacturing_workers=0,manufactured_gross_output_per_worker=300000,
                gross_output_replacing_imports_fraction=.35,imported_input_share_of_substituted_output=.25):
    if not all(0<=x<=1 for x in [ui_share,benefit_spell_avoided_fraction,
                    gross_output_replacing_imports_fraction,imported_input_share_of_substituted_output]):
        raise ValueError("probability/share invalid")
    if any(x<0 for x in [net_additional_workers,additional_manufacturing_workers,mean_wage_usd]):
        raise ValueError("nonnegative workers/wages required")
    # Other income tax effects, changes in SNAP, SSI and Medicaid are ZERO until
    # measured with individual/household linked eligibility and state rules.
    # Employer+employee payroll tax 12.4% OASDI+2.9% Medicare assumed all
    # annual wages under OASDI annual limit; net increase only if jobs actually
    # come from people NOT already employed at the baseline.
    payroll_b=net_additional_workers*mean_wage_usd*.153/1e9
    annual_avg_ui_benefit=BASELINE["regular_ui_benefits_2025_b"]*1e9/(BASELINE["regular_ui_beneficiaries_cy2025_m"]*1e6)
    ui_avoided_b=(net_additional_workers*ui_share*
                  benefit_spell_avoided_fraction*annual_avg_ui_benefit)/1e9
    manufactured_output_b=additional_manufacturing_workers*manufactured_gross_output_per_worker/1e9
    imported_finished_sales_displaced_b=(manufactured_output_b*gross_output_replacing_imports_fraction)
    incremental_imported_inputs_b=imported_finished_sales_displaced_b*imported_input_share_of_substituted_output
    trade_effect_b=imported_finished_sales_displaced_b-incremental_imported_inputs_b
    return {"net_new_employed_fte":net_additional_workers,
            "of_which_manufacturing_fte":additional_manufacturing_workers,
            "gross_annual_wage_bill_b":round(net_additional_workers*mean_wage_usd/1e9,3),
            "payroll_tax_receipts_combined_employer_worker_b":round(payroll_b,3),
            "ui_savings_if_counterfactual_claims_b":round(ui_avoided_b,3),
            "no_model_credit_snap_ssi_medicaid_or_income_tax":True,
            "new_manufacturing_gross_output_b":round(manufactured_output_b,3),
            "displaced_finished_goods_imports_b":round(imported_finished_sales_displaced_b,3),
            "additional_imported_inputs_b":round(incremental_imported_inputs_b,3),
            "conditional_direct_goods_balance_improvement_b":round(trade_effect_b,3),
            "warning":"Payroll tax is a transfer, not social net output. Factory output is not manufacturing value added. Trade-balance scenario is static; exchange rates, intermediate imports, exports/price responses omitted."}

def sample():
    cases=[hiring_case(300000,additional_manufacturing_workers=100000),
           hiring_case(1000000,additional_manufacturing_workers=300000),
           hiring_case(2000000,additional_manufacturing_workers=800000)]
    return {"status":"COUNTERFACTUAL SCENARIOS ONLY",
            "baselines":BASELINE,
            "factory_cells":[f.assess() for f in FACTORIES],
            "factory_equivalent_cost_gate":hybrid_breakeven_additive_hours(),
            "new_jobs_and_trade":[c for c in cases],
            "public_accounting_warning":"Do not add the $397B CBO income security amount to SNAP, UI, SSI. Medicaid not a cash benefit. Don't count wages as both cost savings and GDP, and don't count factory output as GDP.",
            "validation_gates":["Identical certified electrical performance (not inferred from manufacturing cost)",
                                "Same genuine maintenance/service life and warranty",
                                "Per-unit itemized bills verified independently for n=100/1000/10000",
                                "Local qualified workforce versus reallocated existing employment",
                                "Regional wage, UI and benefit eligibility counterfactual",
                                "Domestic parts tier 1-n, gross output, imported intermediates and export response"]}

def tests():
    f=[a.assess() for a in FACTORIES]
    assert f[0]["illustrative_qualified_additive_print_cells"]==0
    assert f[1]["illustrative_qualified_additive_print_cells"]==ceil(7.7e6*4/(8760*.7*.94))
    assert f[2]["direct_factory_cost_per_accepted_unit_usd"]>f[0]["direct_factory_cost_per_accepted_unit_usd"]
    a=hiring_case(1000000,additional_manufacturing_workers=300000)
    assert isclose(a["gross_annual_wage_bill_b"],60)
    assert isclose(a["payroll_tax_receipts_combined_employer_worker_b"],9.18)
    assert isclose(a["conditional_direct_goods_balance_improvement_b"],23.625)
    assert isclose(a["ui_savings_if_counterfactual_claims_b"],.811,abs_tol=.002)
    print("Arithmetic-only assertions PASS; physical factory and macro causal effects UNVALIDATED")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--test",action="store_true")
    args=p.parse_args()
    if args.test: tests()
    else: print(json.dumps(sample(),indent=2))
