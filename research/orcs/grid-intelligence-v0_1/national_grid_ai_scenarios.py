#!/usr/bin/env python3
"""ORCS Grid Intelligence v0.1: transparent illustrative US-wide benefits model.
Uses only Python standard library. All deployment/effect inputs are ASSUMED.
No operational control, network access, vendor pricing, or trained AI.
"""
from dataclasses import dataclass, asdict
from math import isclose
import argparse
import json

EIA_2025_RETAIL_TWH = 4079.909  # EIA annual 2025 total, October 2026 release
EIA_2025_LOSSES_UNACCOUNTED_TWH = 221.419  # EIA balance, NOT pure line losses
EIA_2025_ELECTRIC_METERS_MILLION = 169.808072
EIA_2025_AMI_METERS_MILLION = 147.093020
ORNL_MAJOR_OUTAGE_COST_B_USD_PER_Y = 67.0  # 2018-2024 estimated avg, extreme weather mix
TRANSMISSION_ROUTE_MILES_PROXY = 600000  # SPECULATIVE scope proxy; route vs circuit-mi differs
ENERGY_AVOIDED_USD_PER_KWH = 0.08  # Assumed incremental avoided-resource cost, not retail
REAL_DISCOUNT = 0.05
YEARS = 30
REFRESH_RATE = 0.35
REFRESH_YEARS = (10, 20)


@dataclass(frozen=True)
class Scenario:
    name: str
    distribution_increment_usd_per_account: float
    eligible_transmission_share: float
    transmission_get_usd_per_equipped_mile: float
    wildfire_instrumentation_b: float
    national_ot_security_and_integration_b: float
    vvo_served_energy_fraction: float
    vvo_reduction_of_served_energy: float
    losses_eligible_fraction: float
    losses_reduction_fraction: float
    major_outage_damage_reduction_fraction: float
    incremental_grid_ignited_fire_damage_b_per_y: float
    fire_damage_reduction_fraction: float
    annual_opex_fraction_of_initial_capital: float = 0.05

    def check(self):
        proportions = [self.eligible_transmission_share, self.vvo_served_energy_fraction,
                       self.vvo_reduction_of_served_energy, self.losses_eligible_fraction,
                       self.losses_reduction_fraction, self.major_outage_damage_reduction_fraction,
                       self.fire_damage_reduction_fraction, self.annual_opex_fraction_of_initial_capital]
        if not all(0 <= value <= 1 for value in proportions):
            raise ValueError("All scenario fractions must be between 0 and 1")
        if min(self.distribution_increment_usd_per_account, self.transmission_get_usd_per_equipped_mile,
               self.wildfire_instrumentation_b, self.national_ot_security_and_integration_b,
               self.incremental_grid_ignited_fire_damage_b_per_y) < 0:
            raise ValueError("Dollar inputs must be nonnegative")


CASES = [
    Scenario("Conservative",60,.05,10000,1,1,.60,.003,.50,.02,.01,3,.03),
    Scenario("Reference",180,.10,20000,3,4,.70,.008,.50,.04,.04,3,.10),
    Scenario("Upper sensitivity",280,.15,35000,7,8,.85,.015,.60,.08,.08,5,.20),
]


def evaluate(s: Scenario) -> dict:
    s.check()
    distribution_capital_b = EIA_2025_ELECTRIC_METERS_MILLION * s.distribution_increment_usd_per_account / 1000
    transmission_capital_b = TRANSMISSION_ROUTE_MILES_PROXY * s.eligible_transmission_share * s.transmission_get_usd_per_equipped_mile / 1e9
    capex_b = (distribution_capital_b + transmission_capital_b + s.wildfire_instrumentation_b
               + s.national_ot_security_and_integration_b)

    # Energy-conservation benefit reduces service kWh, rather than generation losses.
    # Loss benefit uses a constrained subset of EIA 'losses and unaccounted for'.
    # No energy is sold twice or attributed to both categories.
    vvo_twh = EIA_2025_RETAIL_TWH * s.vvo_served_energy_fraction * s.vvo_reduction_of_served_energy
    loss_recovery_twh = (EIA_2025_LOSSES_UNACCOUNTED_TWH * s.losses_eligible_fraction
                         * s.losses_reduction_fraction)
    energy_b = (vvo_twh + loss_recovery_twh) * ENERGY_AVOIDED_USD_PER_KWH

    # Risk accounting: 'fire' is extra non-outage damage and must exclude damage
    # already in ORNL outage figures. It is an invented sensitivity input.
    outage_b = ORNL_MAJOR_OUTAGE_COST_B_USD_PER_Y * s.major_outage_damage_reduction_fraction
    fire_b = s.incremental_grid_ignited_fire_damage_b_per_y * s.fire_damage_reduction_fraction
    annual_benefit_b = energy_b + outage_b + fire_b
    annual_operating_b = capex_b * s.annual_opex_fraction_of_initial_capital

    pv_annuity = (1 - (1 + REAL_DISCOUNT)**(-YEARS)) / REAL_DISCOUNT
    pv_replacements_b = capex_b * REFRESH_RATE * sum((1 + REAL_DISCOUNT)**(-y) for y in REFRESH_YEARS)

    # OPTIMISTIC steady-state upper accounting: nationwide benefits immediately
    # from year 1, WITHOUT construction phase ramp, tax/financing wedges or
    # individualized grid constraints. This is NOT an investment-grade NPV.
    optimistic_npv_b = ((annual_benefit_b - annual_operating_b) * pv_annuity
                        - capex_b - pv_replacements_b)
    # Ten-year linear deployment: construction cohorts in years 1..10, each
    # providing proportional benefits from commissioning year onward. Every
    # cohort receives a 35% technology refresh 10 and 20 years later.
    # All annual outcomes are scenario assumptions, NOT utility forecasts.
    staged_npv_b = 0.0
    for year in range(1, YEARS + 1):
        active_share = min(year / 10, 1.0)
        construction_b = capex_b / 10 if year <= 10 else 0.0
        cohort_refresh_b = (capex_b * REFRESH_RATE / 10
                            if 11 <= year <= 30 else 0.0)
        annual_net_b = (annual_benefit_b - annual_operating_b) * active_share
        staged_npv_b += (annual_net_b - construction_b - cohort_refresh_b) / (1 + REAL_DISCOUNT)**year
    return {
        "scenario": s.name, "capital_b": round(capex_b,3),
        "capital_distribution_b": round(distribution_capital_b,3),
        "capital_transmission_get_b": round(transmission_capital_b,3),
        "vvo_saved_twh_per_year": round(vvo_twh,3),
        "delivered_loss_recovery_twh_per_year": round(loss_recovery_twh,3),
        "annual_avoided_energy_b": round(energy_b,3),
        "annual_avoided_major_outage_damage_b": round(outage_b,3),
        "annual_avoided_non_outage_fire_damage_b": round(fire_b,3),
        "annual_combined_illustrative_benefits_b": round(annual_benefit_b,3),
        "annual_operating_cost_b": round(annual_operating_b,3),
        "pv_equipment_refresh_b": round(pv_replacements_b,3),
        "optimistic_steady_state_30year_npv_b": round(optimistic_npv_b,3),
        "ten_year_linear_rollout_30year_npv_b": round(staged_npv_b,3),
        "unvalued": [
          "Dynamic line rating headroom (not incremental nationwide MWh)",
          "Dynamic transformer rating", "Topology and advanced power-flow control",
          "Interconnection and data-center capacity", "Storage and demand flexibility",
          "Worker safety, avoided deaths/illness, ecological effects",
          "Condition-directed replacement, spare inventories, routine grid CAPEX",
        ],
    }


def test_invariants() -> None:
    cases = [evaluate(s) for s in CASES]
    assert len(cases) == 3
    for x in cases:
        assert x["capital_b"] > 0
        assert x["vvo_saved_twh_per_year"] < EIA_2025_RETAIL_TWH
        assert x["delivered_loss_recovery_twh_per_year"] <= EIA_2025_LOSSES_UNACCOUNTED_TWH
        assert x["annual_combined_illustrative_benefits_b"] >= x["annual_avoided_energy_b"]
        assert x["annual_operating_cost_b"] > 0
    assert isclose(cases[1]["capital_b"], 38.765, abs_tol=.002)
    assert isclose(cases[1]["annual_combined_illustrative_benefits_b"], 5.162, abs_tol=.002)
    assert isclose(cases[1]["optimistic_steady_state_30year_npv_b"], -2.651, abs_tol=.003)
    assert isclose(cases[1]["ten_year_linear_rollout_30year_npv_b"], -2.956, abs_tol=.005)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--inputs", action="store_true", help="also print explicit scenario assumptions")
    opts = parser.parse_args()
    if opts.test:
        test_invariants()
        print("4 categories of modeled invariants PASS; NOT physical or utility validation")
    else:
        print(json.dumps({"status": "ILLUSTRATIVE ONLY; NO OPERATING UTILITY / NO AI EXECUTED",
                          "model": "ORCS US Grid Intelligence v0.1",
                          "scenarios": [evaluate(c) for c in CASES],
                          **({"assumptions": [asdict(c) for c in CASES]} if opts.inputs else {})}, indent=2))
