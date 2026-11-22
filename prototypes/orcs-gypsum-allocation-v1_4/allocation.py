"""Exclusive gypsum allocation. No invented agronomic outcomes or materials."""
import json
from pathlib import Path

CATEGORIES=("agriculture","sulfuric_acid","industrial","resilience_reserve")

def assess(record):
    """Estimate eligibility only from a real, qualified, source-stamped batch.

    Annual gross model/chemical-equivalent ceilings are intentionally rejected
    for allocation until independently assayed and product qualified.
    """
    if not record.get("batch_source_url") or not record.get("site_id") or not record.get("observation_date"):
        return {"status":"UNKNOWN_SOURCE","allocatable_t":None}
    if record.get("status")!="MEASURED_QUALIFIED" or not record.get("certificate_reference"):
        return {"status":"UNKNOWN_UNQUALIFIED_GYPSUM","allocatable_t":None}
    tonnes=record.get("qualified_tonnes")
    if tonnes is None or isinstance(tonnes,bool) or not isinstance(tonnes,(int,float)) or tonnes<0:
        return {"status":"UNKNOWN_MASS","allocatable_t":None}
    alloc=record.get("allocation_tonnes")
    if not isinstance(alloc,dict) or any(k not in alloc for k in CATEGORIES) or any(k not in CATEGORIES for k in alloc):
        return {"status":"UNKNOWN_ALLOCATION","allocatable_t":tonnes}
    if any(not isinstance(alloc[k],(float,int)) or isinstance(alloc[k],bool) or alloc[k]<0 for k in CATEGORIES):
        raise ValueError("Allocation must be finite nonnegative quantities")
    import math
    if not math.isfinite(float(tonnes)) or any(not math.isfinite(float(alloc[k])) for k in CATEGORIES):
        raise ValueError("Nonfinite mass")
    total=sum(alloc.values())
    if total>tonnes+1e-8:
        return {"status":"REJECTED_DOUBLE_COUNT","allocatable_t":tonnes,"requested_t":total}
    if alloc["agriculture"]>0 and not record.get("soil_product_approved"):
        return {"status":"UNKNOWN_AGRONOMIC_SAFETY","allocatable_t":tonnes}
    if alloc["sulfuric_acid"]>0 and not record.get("acid_process_verified"):
        return {"status":"UNKNOWN_ACID_PROCESS","allocatable_t":tonnes}
    return {"status":"MASS_BALANCE_ONLY","allocatable_t":tonnes,
            "allocated_t":{k:alloc[k] for k in CATEGORIES},
            "unallocated_t":round(tonnes-total,6),
            "real_world_delivery_verified":False,"export_authorized":False}

def source_inventory():
    return json.loads((Path(__file__).parent/"registry.json").read_text())

if __name__=="__main__":
    r=source_inventory()
    print(json.dumps({"status":"NO_QUALIFIED_REAL_WORLD_BATCHES_INGESTED",
      "official_sources":len(r["sources"]),"model_ceilings":len(r["prior_model_ceiling"])},indent=2))
