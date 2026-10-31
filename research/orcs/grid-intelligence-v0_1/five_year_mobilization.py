#!/usr/bin/env python3
"""ORCS five-year national grid mobilization: transparent, illustrative arithmetic.
No deployed hardware, procurement, verified job creation, or operating utility.
Run: python five_year_mobilization.py --test or --json.
"""
from dataclasses import dataclass
from math import isclose
import argparse
import json

YEARS = 5
US_SHIPMENTS_2021_M = 1.5   # CRS R48933 / DOE reference; NOT current production
INSTALLED_UNIT_USD = 8000   # illustrative installed average, NOT a market quote
EQUIPMENT_USD = 4000        # ASSUMED split of installed cost
INSTALLATION_USD = 4000     # ASSUMED split; sum equals INSTALLED_UNIT_USD
DIGITAL_CAPEX_B = 38.76545296
PRIORITY_LINES_CAPEX_B = 158.3
TRAINING_CAPEX_B = 6.0
DIGITAL_CONSTRUCTION_JOBS = DIGITAL_CAPEX_B * 1e9 * .35 / 130000
LINES_CONSTRUCTION_JOBS = PRIORITY_LINES_CAPEX_B * 1e9 * .30 / 140000
DIGITAL_STEADY_OPEX_FTES = DIGITAL_CAPEX_B * 1e9 * .05 * .60 / 130000
EIA_RETAIL_2025_TWH = 4079.909
AVOIDED_RESOURCE_USD_KWH = .08


@dataclass(frozen=True)
class Plan:
    name: str
    replacement_million: float
    units_each_year_million: tuple

    def validate(self):
        if len(self.units_each_year_million) != YEARS:
            raise ValueError("Need five deployment cohorts")
        if not isclose(sum(self.units_each_year_million), self.replacement_million):
            raise ValueError("Annual transformer units must sum to replacement quantity")
        if any(x < 0 for x in self.units_each_year_million):
            raise ValueError("Negative production impossible")


PLANS = (
    Plan("Priority 10M", 10.0, (1.0, 1.5, 2.0, 2.5, 3.0)),
    Plan("Oldest 55pct of 70M", 38.5, (2.0, 4.0, 7.0, 10.0, 15.5)),
    Plan("Full 70M", 70.0, (3.0, 6.0, 11.0, 20.0, 30.0)),
)


def assess(p: Plan, equipment_discount=0.20, installation_discount=0.10):
    p.validate()
    if not (0 <= equipment_discount < 1 and 0 <= installation_discount < 1):
        raise ValueError("Discount assumptions invalid")
    units = p.replacement_million * 1e6
    transformer_capex_b = units * INSTALLED_UNIT_USD / 1e9
    capex_base_b = DIGITAL_CAPEX_B + PRIORITY_LINES_CAPEX_B + TRAINING_CAPEX_B + transformer_capex_b
    factory_potential_b = units * EQUIPMENT_USD * equipment_discount / 1e9
    site_potential_b = units * INSTALLATION_USD * installation_discount / 1e9
    capex_conditional_b = capex_base_b - factory_potential_b - site_potential_b

    transformer_jobs = transformer_capex_b * 1e9 * .30 / 140000
    capex_jobs = DIGITAL_CONSTRUCTION_JOBS + LINES_CONSTRUCTION_JOBS + transformer_jobs
    # Assuming constant full-build employment job-years and linearly
    # commissioned digital operations: first-five-year OPEX employment .6 of full.
    ops_jobs_average = DIGITAL_STEADY_OPEX_FTES * .60
    total_annual_average_fte = capex_jobs / YEARS + ops_jobs_average

    return {
        "plan": p.name, "timeline_years": YEARS,
        "annual_transformer_units_m": list(p.units_each_year_million),
        "average_transformer_replacements_per_year_m": round(p.replacement_million / YEARS, 3),
        "last_year_units_relative_to_2021_US_shipments": round(p.units_each_year_million[-1] / US_SHIPMENTS_2021_M, 2),
        "baseline_capital_b": round(capex_base_b, 3),
        "conditional_factory_savings_b": round(factory_potential_b, 3),
        "conditional_install_savings_b": round(site_potential_b, 3),
        "conditional_capital_b": round(capex_conditional_b, 3),
        "unpriced": ["factory construction/ramp and tool reconfiguration",
                     "additional training capacity beyond assumed allowance",
                     "physical-grid contingency; financing and permitting",
                     "line-work outage windows/crews; field-access limitations",
                     "product qualification and legal rate/contract changes"],
        "gross_capital_supported_job_years": round(capex_jobs),
        "average_capital_supported_FTE_per_year": round(capex_jobs / YEARS),
        "average_steady_and_ramping_digital_operations_FTE_first5": round(ops_jobs_average),
        "average_total_gross_supported_FTE_per_year": round(total_annual_average_fte),
        "note": "Gross supported domestic FTE; existing utility labor, normal replacement and workforce displacement NOT deducted."
    }


def conditioning():
    # Existing 10-year Grid Intelligence reference program includes CVR/VVO:
    served_share, cvr = .70, .008
    vvo_saved_twh = EIA_RETAIL_2025_TWH * served_share * cvr
    vvo_value_b = vvo_saved_twh * AVOIDED_RESOURCE_USD_KWH
    # Possible additional active-conditioning and phase-balance effect,
    # only after independent meter verification of NO OVERLAP with CVR,
    # loss optimization, and power-electronics own conversion losses.
    extra_candidate_twh = EIA_RETAIL_2025_TWH * .001
    # Stage example: 99.15% passive, two 97% converters vs
    # 97% SST plus 98% DC converter; excludes essential UPS parity.
    existing_chain = .9915 * .97 * .97
    proposed_chain = .97 * .98
    full_load_mw = 1000
    avoided_input_mw = full_load_mw * (1 / existing_chain - 1 / proposed_chain)
    return {
        "embedded_reference_VVO_energy_TWh_y": round(vvo_saved_twh, 3),
        "embedded_reference_VVO_resource_value_B_y": round(vvo_value_b, 3),
        "optional_separately_tested_0p1pct_TWh_y": round(extra_candidate_twh, 3),
        "optional_separately_tested_0p1pct_resource_value_B_y": round(extra_candidate_twh * AVOIDED_RESOURCE_USD_KWH, 3),
        "example_legacy_three_stage_efficiency": round(existing_chain, 5),
        "example_proposed_two_stage_efficiency": round(proposed_chain, 5),
        "example_mw_input_avoided_if_equal_functionality": round(avoided_input_mw, 2),
        "warning": "Power factor correction and harmonic filtering do NOT create energy; stage example is NOT validated or a complete UPS-reliability design. No additional credit in base model."
    }


def training():
    # Tuition, curriculum, instructor and lab costs ONLY; wages of
    # working apprentices already exist within job-years, do NOT double count.
    starts_per_year = 40000
    incumbent_refresh_per_year = 50000
    newcomers_training_usd = 20000
    incumbents_training_usd = 4000
    standards_lab_b = 1.0
    return {
        "five_year_new_apprenticeship_starts": starts_per_year * YEARS,
        "five_year_incumbent_retraining_seats": incumbent_refresh_per_year * YEARS,
        "training_program_b": round((starts_per_year * YEARS * newcomers_training_usd +
                incumbent_refresh_per_year * YEARS * incumbents_training_usd) / 1e9 + standards_lab_b,3),
        "not": "200,000 journey-level graduates; many electrical/line apprenticeships take 3–4 years under qualified trainers",
        "rules": ["AI tutors and simulation are NON-credentialing support",
                  "Human/registered program verified practical exams",
                  "State/CDL/OSHA and utility qualifications remain applicable",
                  "NERC qualified role training and cybersecurity as relevant",
                  "Apprentice pay already within project labor, not training tuition"]
    }


def tests():
    x = [assess(p) for p in PLANS]
    assert isclose(x[0]["baseline_capital_b"], 283.065, abs_tol=.005)
    assert isclose(x[1]["baseline_capital_b"], 511.065, abs_tol=.005)
    assert isclose(x[2]["baseline_capital_b"], 763.065, abs_tol=.005)
    assert isclose(x[1]["conditional_capital_b"], 464.865, abs_tol=.005)
    assert isclose(x[1]["average_total_gross_supported_FTE_per_year"], 226000, abs_tol=500)
    assert training()["training_program_b"] == 6.0
    assert conditioning()["embedded_reference_VVO_energy_TWh_y"] == 22.847
    assert all(sum(p.units_each_year_million)==p.replacement_million for p in PLANS)
    print("Five-year unit/cost/jobs/training/conditioning invariant tests PASS (arithmetic only)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        tests()
    else:
        print(json.dumps({"status": "SCENARIO ONLY; NO DEPLOYED TECHNOLOGY, JOB CREATION OR GUARANTEED COST REDUCTIONS",
                          "manufacturing": [assess(p) for p in PLANS],
                          "training": training(), "power_conditioning": conditioning()}, indent=2))
