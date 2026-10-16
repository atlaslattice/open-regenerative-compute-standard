#!/usr/bin/env python3
"""ORCS Maui emergency-water and bottled-import capture SCREENING model v0.8.
Uses model assumptions; NOT hydraulic engineering, verified Maui demand, or dispatch.
Python standard library only. Run: python3 maui_emergency_water_wholesale_v08.py
"""
from dataclasses import dataclass

GAL_PER_M3 = 264.172052
M3_PER_MGD_DAY = 1_000_000 / GAL_PER_M3
HISTORIC_COUNTYWIDE_HOUSEHOLD_MGD = 22.5
OPERATING_FACTOR = 0.85  # Demonstrative, NOT a measured emergency service guarantee.
SEAWATER_RO_KWH_PER_M3 = 3.5  # RO-only scenario: excludes ZLD, pumping, pretreatment etc.
BOTTLED_EQUIVALENTS = 53_926_000 # extrapolated annual 500-mL equivalent single-serve PET
IMPORTED_PORTION = 0.80 # unverified and stress-tested, not measured
WHOLESALE_USD = 0.75 # scenario, not invoices
MARGIN = 0.30 # desired FULLY loaded net margin, not industry proven

@dataclass(frozen=True)
class Case:
    name: str
    west_running: float = 1.0
    north_running: float = 1.0
    central_running: float = 1.0

CASES = (
    Case("All plants available"),
    Case("West offline", west_running=0),
    Case("North offline", north_running=0),
    Case("Central at 50% capacity", central_running=0.5),
    Case("West offline + Central at 70%", west_running=0, central_running=0.7),
    Case("Central fully offline", central_running=0),
)

def output_mgd(central_nameplate, case):
    """Conservative scenario: output factor times concurrent operational derate.
    Actual 85% annual capacity utilization is not an availability guarantee."""
    return OPERATING_FACTOR * (
        6.0 * case.west_running +
        5.0 * case.north_running +
        central_nameplate * case.central_running
    )

def ro_mw(mgd):
    return (mgd * M3_PER_MGD_DAY * SEAWATER_RO_KWH_PER_M3) / 24_000

def fmt(x): return f"{x:,.2f}"

def main():
    print("MAUI ORCS EMERGENCY SCREENING 2026-10-16 (NOT verified district demand)")
    print("West 6 MGD / North 5 MGD / Central alternatives 22,25,28 MGD")
    print("Output 0.85 x nameplate x plant-operation factor; NOT measured reliability.")
    print("2026 Maui Ordinance 5929 Stage 1/2/3 reduction goals: 10/20/30%")
    print("Important: statute applies to current system demand under utility direction;")
    print("here reductions are applied to historical household baseline ONLY as test loads.")
    targets={name:HISTORIC_COUNTYWIDE_HOUSEHOLD_MGD*factor for name,factor in
             (("historical household",1),("hypothetical 10% smaller",.9),
              ("hypothetical 20% smaller",.8),("hypothetical 30% smaller",.7))}
    for central in (22,25,28):
        print(f"\nCENTRAL nameplate={central} MGD | total nameplate={11+central} MGD")
        print("Situation                                Output  RO MW  historical/20%")
        for case in CASES:
            val=output_mgd(central,case)
            statuses=["YES" if val>=targets[key] else "NO"
                      for key in ("historical household","hypothetical 20% smaller")]
            print(f"{case.name:<40} {val:>6.2f} {ro_mw(val):>6.2f}  {'/'.join(statuses)}")
    annual_equiv_imported=BOTTLED_EQUIVALENTS*IMPORTED_PORTION
    replaced=annual_equiv_imported*.75
    gross=replaced*WHOLESALE_USD
    net=gross*MARGIN
    print("\nBOTTLED WATER HYPOTHETICAL 80% import, 75% capture and $0.75 price")
    print(f"Equivalent imports: {annual_equiv_imported/1e6:.2f} million units")
    print(f"Equivalent locally supplied: {replaced/1e6:.2f} million units")
    print(f"Local manufacturer wholesale SALES replacing imports: ${gross/1e6:.2f} million/y")
    print(f"Target 30% NET: ${net/1e6:.2f} million/y (NOT verified)")
    print("Imported-product displacement value is a LOCAL REVENUE OPPORTUNITY,")
    print("not additional profit to be added to gross sales or material savings.")
    print("\nDO NOT CLAIM N-1: central outage leaves only 9.35 MGD.")
    print("Model excludes real district hydraulics, essential nonresidential demand,")
    print("peak/fire flows, ZLD electricity/brine tanks, production reliability,")
    print("off-grid PV/battery hourly dispatch, existing-source backup and finance.")

if __name__ == "__main__":
    main()
