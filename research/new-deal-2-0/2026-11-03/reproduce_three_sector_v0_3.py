#!/usr/bin/env python3
"""ORCS New Deal 2.0 v0.3 three-sector scenario reproducibility script.
Reads CSV inputs published alongside this script; standard library only.
This is deterministic scenario arithmetic, NOT an empirical national jobs forecast.
"""
from __future__ import annotations
import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent

def read_inputs():
    with (HERE / "three_sector_assumptions_v0_3.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {row["Assumption"]: {s: float(row[s]) for s in ("Conservative","Central","Accelerated")} for row in rows}

def get(inp, name, scenario):
    return inp[name][scenario]

def calc(inp, s):
    g = lambda n: get(inp, n, s)
    t = g("Materials annual inbound") * 1e6
    n = math.ceil(t / (g("Materials module annual nameplate") * g("Materials module utilization")))
    materials_fte = t * g("Materials labor intensity") / g("Productive hours per FTE")
    qualified = t * g("Materials qualified yield")
    material_revenue = qualified * g("Qualified sale price") + t * g("Tipping fee eligible share") * g("Realized tipping fee")
    waste_opex = t * g("Materials nonlabor opex") + materials_fte * g("Annual fully loaded labor cost")
    r = g("Materials debt rate")
    years = g("Materials debt term")
    annuity = r / (1 - (1 + r)**(-years)) if r else 1 / years
    charge = n * g("Materials module CAPEX") * 1e6 * annuity
    waste_after_capital = material_revenue - waste_opex - charge
    water_construction = g("Water annual executed capex") * 1000 * g("Water construction direct jobs")
    water_om = g("Water added permanent O&M")
    grid_construction = g("Grid annual executed capex") * 1000 * g("Grid direct field construction")
    grid_om = g("Grid added permanent O&M")
    return {
        "materials_modules":n,
        "materials_direct_fte":materials_fte,
        "water_gross":water_construction + water_om,
        "grid_gross":grid_construction + grid_om,
        "total_gross":materials_fte+water_construction+water_om+grid_construction+grid_om,
        "potential_net_new":materials_fte*g("Materials newly hired share")
          + water_construction*g("Water net-new construction fraction") + water_om
          + grid_construction*g("Grid net-new construction fraction") + grid_om,
        "waste_after_capital_usd":waste_after_capital,
    }

if __name__ == "__main__":
    i=read_inputs()
    for scenario in ("Conservative","Central","Accelerated"):
        result=calc(i,scenario)
        print(scenario)
        for k,v in result.items():
            print(f"  {k}: {v:,.2f}" if isinstance(v,float) else f"  {k}: {v:,}")
    print("\nNOTE: labor coefficients, new-hire percentages, revenues and capital terms are ASSUMED.")
