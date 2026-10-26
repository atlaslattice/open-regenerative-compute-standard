"""ORCS v2.1 brine flow census: source categories and status are not interchangeable.
All values are modeled from nameplate product capacity, not observed brine releases.
"""
import json
from pathlib import Path

DAYS=365
M3_PER_MGD=3785.411784

def brine_m3_per_year(product_mgd, water_recovery, utilization):
    """Reject = product * (1/recovery - 1), provided single-pass RO assumptions apply."""
    if isinstance(product_mgd,bool) or not isinstance(product_mgd,(int,float)) or product_mgd<0:
        raise ValueError("invalid freshwater nameplate")
    if not 0<water_recovery<1 or not 0<=utilization<=1:
        raise ValueError("invalid scenario recovery or utilization")
    return product_mgd*M3_PER_MGD*DAYS*utilization*(1/water_recovery-1)

def scenario():
    data=json.loads((Path(__file__).parent.parent.parent/"data/desal_gypsum/orcs_seawater_brackish_separated_network_v2_1_2026-10-14.json").read_text())
    totals={x["category"]:x for x in data["stats"]}
    sea=totals["seawater_operating"]["known_mgd"]
    proposed=totals["seawater_proposed"]["known_mgd"]
    recent=totals["brackish_operating_reported"]["known_mgd"]
    historical=totals["brackish_status_uncertain"]["known_mgd"]
    seawater=brine_m3_per_year(sea,0.5,0.9)
    brackish_qualified={f"r_{r:.1f}":round(brine_m3_per_year(recent,r,0.9)) for r in (0.7,0.8,0.9)}
    brackish_historical={f"r_{r:.1f}":round(brine_m3_per_year(recent+historical,r,0.9)) for r in (0.7,0.8,0.9)}
    return {
      "facilities_categorized":sum(t["n"] for t in totals.values()),
      "status":"SCENARIO_ONLY_NO_ACTUAL_BRINE_FLOW_TOTAL",
      "operating_documented_seawater_product_mgd":sea,
      "seawater_model_50pct_recovery_90pct_utilization_m3_y":round(seawater),
      "proposed_seawater_product_mgd_excluded_from_current":proposed,
      "proposed_seawater_model_m3_y_SEPARATE":round(brine_m3_per_year(proposed,0.5,0.9)),
      "brackish_recent_operating_reported_product_mgd":recent,
      "brackish_recent_only_m3_y_by_recovery":brackish_qualified,
      "brackish_including_historical_uncertain_product_mgd":recent+historical,
      "brackish_including_historical_uncertain_m3_y_by_recovery":brackish_historical,
      "all_91_network_measured_annual_brine_m3_y":None,
      "unquantified_and_unclassified_facility_count":totals["source_unclassified"]["n"]+totals["seawater_unquantified"]["n"],
      "warning":"No assumption about brackish mineral concentrations; current verified plant flow and mass are unknown."
    }

if __name__=="__main__":
    print(json.dumps(scenario(),indent=2))
