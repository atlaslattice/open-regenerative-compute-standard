#!/usr/bin/env python3
"""Beyond Q active dual-ARC isotope source ledger (2026-11-01).
SCREENING ONLY: fusion powers are hypothetical achieved gross nuclear outputs,
NOT validated SPARC/ARC D-D performance. No invented wall-plug output.
"""
from dataclasses import dataclass, asdict
from pathlib import Path
import json, csv, math
AVOGADRO=6.02214076e23
MEV_J=1.602176634e-13
STP_L_MOL=22.414
HE3_G_MOL=3.01603
TRITIUM_G_MOL=3.01605
SECONDS_YEAR=365.25*86400
@dataclass(frozen=True)
class Assumptions:
    reactor_a_dd_gross_fusion_mw: float=1130.0
    reactor_b_dt_gross_fusion_mw: float=1130.0
    dd_tritium_branch_fraction: float=0.5
    dd_tritium_branch_q_mev: float=4.0327  # D(d,p)T
    dd_he3_branch_q_mev: float=3.2689     # D(d,n)He3
    dt_q_mev: float=17.589
    availability: float=0.85
    recovered_he3_fraction: float=0.375 # unvalidated whole-process illustration
    recovered_tritium_fraction: float=0.375 # independently unvalidated illustration
    he3_reference_price_usd_per_stp_liter: float=18000.0 # upside quoted-price sensitivity, not durable offtake
    tritium_reference_price_usd_per_gram: float=30000.0 # upside procurement sensitivity, not sales
    he3_volume_price_usd_per_stp_liter: float=15000.0 # owner-selected aggressive market-expansion scenario
    tritium_volume_price_usd_per_gram: float=15000.0 # owner-selected scenario
    wall_plug_mw: float|None=None  # UNKNOWN; don't infer from fusion or net electricity
    electricity_price_usd_per_mwh: float=65.0
    chassis_each_usd: float=2800000000.0 # unvalidated quote
    reactor_a_modification_usd: float=300000000.0 # unvalidated gross estimate
    financing_apr: float=0.07
    financing_years: int=30
    t_b_dedicated_breeding_fraction: float|None=None # unknown
def model(a=Assumptions()):
    assert a.reactor_a_dd_gross_fusion_mw==1130 and a.reactor_b_dt_gross_fusion_mw==1130, "ACTIVE DESIGN: BOTH REACTORS 1130 MW GROSS"
    q=a.dd_tritium_branch_fraction*a.dd_tritium_branch_q_mev+(1-a.dd_tritium_branch_fraction)*a.dd_he3_branch_q_mev
    events=a.reactor_a_dd_gross_fusion_mw*1e6/(q*MEV_J)*SECONDS_YEAR*a.availability
    t_birth=events*a.dd_tritium_branch_fraction/AVOGADRO*TRITIUM_G_MOL
    he_birth=events*(1-a.dd_tritium_branch_fraction)/AVOGADRO*HE3_G_MOL
    he_l=he_birth/HE3_G_MOL*STP_L_MOL*a.recovered_he3_fraction
    t_g=t_birth*a.recovered_tritium_fraction
    b_t_burn_g=a.reactor_b_dt_gross_fusion_mw*1e6/(a.dt_q_mev*MEV_J)*SECONDS_YEAR*a.availability/AVOGADRO*TRITIUM_G_MOL
    capex=2*a.chassis_each_usd+a.reactor_a_modification_usd
    f=a.financing_apr; n=a.financing_years
    debt=capex*f/(1-(1+f)**(-n))
    return dict(reactor_a_gross_fusion_mw=a.reactor_a_dd_gross_fusion_mw,reactor_b_gross_fusion_mw=a.reactor_b_dt_gross_fusion_mw,
       calendar_availability=a.availability,dd_he3_born_g=he_birth,dd_t_born_g=t_birth,
       recovered_he3_stp_liters=he_l,recovered_t_grams=t_g,reactor_b_t_burn_gross_grams=b_t_burn_g,
       high_quote_he3_usd=he_l*a.he3_reference_price_usd_per_stp_liter,
       high_quote_t_value_usd=t_g*a.tritium_reference_price_usd_per_gram,
       volume_case_he3_usd=he_l*a.he3_volume_price_usd_per_stp_liter,
       volume_case_t_value_usd=t_g*a.tritium_volume_price_usd_per_gram,
       illustrative_annual_debt_service_usd=debt,
       wall_plug_mw=a.wall_plug_mw,
       power_purchase_usd=None if a.wall_plug_mw is None else a.wall_plug_mw*a.availability*8766*a.electricity_price_usd_per_mwh,
       net_cash_flow_usd=None, status="UNVALIDATED FUSION POINT; UNVALIDATED RECOVERIES; NO MARKET CLEARING OR NET CASH FLOW")
def main():
    a=Assumptions(); r=model(a)
    root=Path(__file__).parent
    (root/'screening_results.json').write_text(json.dumps(r,indent=2)+'\n')
    with (root/'assumptions.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['parameter','value','status'])
        for k,v in asdict(a).items():w.writerow([k,v,'ASSUMED' if k not in ['dd_tritium_branch_q_mev','dd_he3_branch_q_mev','dt_q_mev'] else 'PUBLISHED NUCLEAR CONSTANT'])
    print(json.dumps(r,indent=2))
if __name__=='__main__':main()
