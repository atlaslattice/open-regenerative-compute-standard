"""Nonbinding domestic-first / export-candidate planning test."""
def candidate_exports(domestic_demand_bbl,available_supply_bbl,usable_reserve_bbl,target_reserve_bbl,retail_gas_usd_gallon=None,gas_target=3.0):
    x=[domestic_demand_bbl,available_supply_bbl,usable_reserve_bbl,target_reserve_bbl,gas_target]
    if any(v is None or v<0 for v in x):
        raise ValueError('Invalid physical input')
    if retail_gas_usd_gallon is not None and retail_gas_usd_gallon<0:
        raise ValueError('Invalid price')
    domestic_served=min(domestic_demand_bbl,available_supply_bbl+usable_reserve_bbl)
    supply_for_demand=min(domestic_demand_bbl,available_supply_bbl)
    used_stock=domestic_served-supply_for_demand
    stock_left=usable_reserve_bbl-used_stock
    spare_supply=available_supply_bbl-supply_for_demand
    restock=min(spare_supply,max(0,target_reserve_bbl-stock_left))
    final_stock=stock_left+restock
    price_ok=None if retail_gas_usd_gallon is None else retail_gas_usd_gallon<=gas_target
    eligible=domestic_served==domestic_demand_bbl and final_stock>=target_reserve_bbl and price_ok is True
    return {'status':'HYPOTHETICAL_POLICY_NOT_LAW','demand_served_bbl':domestic_served,
            'unmet_bbl':domestic_demand_bbl-domestic_served,'reserve_ending_bbl':final_stock,
            'reserve_target_bbl':target_reserve_bbl,'price_threshold_met':price_ok,
            'candidate_export_bbl':max(0,spare_supply-restock) if eligible else 0,
            'export_authorized':False}
