#!/usr/bin/env python3
"""Texas manure methane pre-feasibility SCREEN: USDA inventory + explicit hypotheses.

No claim of actual collected feedstock, LNG delivery, RNG credits, or profit.
Stdlib-only. Example: python tools/texas_manure_rng_screen.py --self-test
                  python tools/texas_manure_rng_screen.py --json
Change/validate inputs ONLY with verified local field data before use.
"""
from __future__ import annotations
import argparse
import json

FT3_PER_M3 = 35.3147
LHV_MMBTU_PER_M3 = 0.03393
DAYS_PER_YEAR = 365

# The headcounts are USDA/Texas state inventories as of Jan 1 2026 (cattle)
# / Dec 1 2025 (swine); all other fields are unverified screening assumptions.
COHORTS = {
    "dairy": dict(head=705_000, kg_day=55.0, collection=0.75, methane_m3_per_wet_t=18.0),
    "feedlot": dict(head=2_540_000, kg_day=25.0, collection=0.55, methane_m3_per_wet_t=13.0),
    "hogs": dict(head=1_130_000, kg_day=5.0, collection=0.65, methane_m3_per_wet_t=12.0),
}

def calculate(cohorts=COHORTS, recovery=0.95, uptime=0.95, price_per_mmbtu=6.0):
    if not (0 <= recovery <= 1 and 0 <= uptime <= 1 and price_per_mmbtu >= 0):
        raise ValueError("Invalid recovery, uptime or gas value")
    outputs = {}
    for name, values in cohorts.items():
        head = values["head"]
        kg = values["kg_day"]
        share = values["collection"]
        yield_per_t = values["methane_m3_per_wet_t"]
        if head < 0 or kg < 0 or yield_per_t < 0 or not (0 <= share <= 1):
            raise ValueError(f"Invalid cohort assumptions: {name}")
        wet_t = head * kg * DAYS_PER_YEAR / 1000
        collected_t = wet_t * share
        gross_m3 = collected_t * yield_per_t
        outputs[name] = {
            "wet_t_per_year": wet_t,
            "collected_t_per_year": collected_t,
            "gross_ch4_m3_per_year": gross_m3,
            "gross_bcf_per_year": gross_m3 * FT3_PER_M3 / 1e9,
        }
    sum_gross = sum(x["gross_ch4_m3_per_year"] for x in outputs.values())
    cleaned = sum_gross * recovery * uptime
    return {
        "model_status": "SCENARIO, NOT MEASURED OR BANKABLE",
        "sources": {
            "headcount": "https://www.nass.usda.gov/Quick_Stats/Ag_Overview/stateOverview.php?state=texas",
            "methane_params": "Unverified screen: require volatile-solids and BMP sampling",
            "pipeline": "https://www.rrc.texas.gov/resource-center/research/gis-viewer",
        },
        "cohorts": outputs,
        "total_wet_t_per_year": sum(x["wet_t_per_year"] for x in outputs.values()),
        "total_collected_t_per_year": sum(x["collected_t_per_year"] for x in outputs.values()),
        "gross_ch4_m3_per_year": sum_gross,
        "gross_bcf_per_year": sum_gross * FT3_PER_M3 / 1e9,
        "cleaned_ch4_m3_per_year": cleaned,
        "cleaned_bcf_per_year": cleaned * FT3_PER_M3 / 1e9,
        "cleaned_lhv_mmbtu_per_year": cleaned * LHV_MMBTU_PER_M3,
        "synthetic_gross_commodity_value_usd": cleaned * LHV_MMBTU_PER_M3 * price_per_mmbtu,
        "gas_value_usd_per_mmbtu_lhv_assumed": price_per_mmbtu,
    }

def dairy_module(head=5000, kg_day=55, collection=.75, methane_per_t=18,
                 recovery=.95, uptime=.95, price=6):
    d = calculate({"dairy_site":dict(head=head,kg_day=kg_day,
                   collection=collection,methane_m3_per_wet_t=methane_per_t)},
                  recovery=recovery, uptime=uptime,price_per_mmbtu=price)
    d["wet_collected_t_per_day"] = head * kg_day / 1000 * collection
    d["gross_ch4_m3_per_day"] = d["gross_ch4_m3_per_year"] / 365
    return d

def self_test():
    d=calculate()
    assert abs(d["gross_ch4_m3_per_year"]-372_868_487.5)<1
    assert abs(d["gross_bcf_per_year"]-13.1677387755)<.000001
    assert abs(d["cohorts"]["dairy"]["gross_bcf_per_year"]-6.747)<.01
    assert abs(d["cohorts"]["feedlot"]["gross_bcf_per_year"]-5.852)<.01
    assert abs(d["cohorts"]["hogs"]["gross_bcf_per_year"]-.568)<.01
    site=dairy_module()
    assert abs(site["gross_ch4_m3_per_day"]-3712.5)<.01
    assert abs(site["cleaned_lhv_mmbtu_per_year"]-41494.49)<.1
    assert abs(site["synthetic_gross_commodity_value_usd"]-248966.92)<1
    assert calculate(recovery=0)["cleaned_ch4_m3_per_year"]==0
    try:
        calculate(recovery=1.1)
    except ValueError: pass
    else: raise AssertionError("recovery >100% must fail")
    return True

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test",action="store_true")
    parser.add_argument("--json",action="store_true")
    parser.add_argument("--dairy-site",action="store_true",help="5,000-head hypothetical dairy module")
    parser.add_argument("--gas-price",type=float,default=6.0,
                        help="Purely illustrative $/MMBtu LHV commodity value")
    args=parser.parse_args()
    if args.self_test:
        self_test()
        print("PASS: eleven numerical/boundary checks")
    else:
        output=(dairy_module(price=args.gas_price) if args.dairy_site
                else calculate(price_per_mmbtu=args.gas_price))
        print(json.dumps(output, indent=2, sort_keys=True))

if __name__=="__main__":
    main()
