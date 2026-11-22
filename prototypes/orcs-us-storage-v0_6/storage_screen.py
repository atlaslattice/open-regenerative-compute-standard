"""ORCS v0.6 optional storage screening. No inferred/fictional surplus.
No live dispatch or commercial authorization.
"""
def screen_charge(rec):
    required=("observed_curtailed_mwh","available_storage_headroom_mwh","authorized_charge_mw",
              "charging_hours","charge_efficiency","discharge_efficiency",
              "stored_soc_mwh","protected_emergency_reserve_mwh","authorized_discharge_mw",
              "discharge_hours","reachable_domestic_load_mwh","transfer_limit_mwh")
    if not rec.get("observed_source_id"):
        return {"status":"UNKNOWN_NO_SOURCE","input_charged_mwh":None}
    if any(rec.get(k) is None for k in required):
        return {"status":"UNKNOWN_INCOMPLETE","input_charged_mwh":None}
    values=[rec[k] for k in required]
    if any(not isinstance(x,(int,float)) or isinstance(x,bool) or x<0 for x in values):
        raise ValueError("invalid nonnegative numerical input")
    if not (0<rec["charge_efficiency"]<=1 and 0<rec["discharge_efficiency"]<=1):
        raise ValueError("invalid efficiency")
    if not rec.get("owner_and_operator_authorized",False):
        return {"status":"NOT_AUTHORIZED","input_charged_mwh":0,"release_mwh":0}
    headroom=rec["available_storage_headroom_mwh"]
    charged=min(rec["observed_curtailed_mwh"],
                headroom/rec["charge_efficiency"],
                rec["authorized_charge_mw"]*rec["charging_hours"])
    added=charged*rec["charge_efficiency"]
    ending=rec["stored_soc_mwh"]+added
    # This screening does NOT route existing SOC for release unless explicitly
    # available above protected inventory. No claim that storage is islandable.
    releasable=max(0,ending-rec["protected_emergency_reserve_mwh"])
    release=min(releasable*rec["discharge_efficiency"],
                rec["authorized_discharge_mw"]*rec["discharge_hours"],
                rec["reachable_domestic_load_mwh"],rec["transfer_limit_mwh"])
    return {"status":"SCREEN_ONLY_HUMAN_REVIEW",
            "source_id":rec["observed_source_id"],
            "input_charged_mwh":round(charged,6),
            "energy_stored_mwh":round(added,6),
            "protected_reserve_mwh":rec["protected_emergency_reserve_mwh"],
            "potential_domestic_delivery_mwh":round(release,6),
            "real_dispatch_authorized":False,
            "note":"Power, engineering, contractual and grid permissions require independent checking."}
