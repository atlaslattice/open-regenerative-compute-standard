"""Exercise the existing v1.2 compartment kernel against external kinetic sources.
No annual extrapolation: both models cover the same2ps interval.
"""
from pathlib import Path
import sys,json,csv
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'neutronics_v1_2'))
from fuelcycle.inventory import advance

def main():
    kg_atom=.00301604928/6.02214076e23;rows=[]
    for name in ('chain_on','seed_219','seed_319','half_dt','double_ppc','lower_multiplier'):
        s=json.loads((ROOT/'outputs/runs'/name/'analysis.json').read_text())
        with (ROOT/'outputs/weighted_reaction_ledger.csv').open() as f:ledger=[r for r in csv.DictReader(f) if r['case']==name]
        stock=burn=0.;previous=0.
        for r in ledger[1:]:
            born=float(r['DD_T_birth_atoms']);h=s['dt_s']/86400
            source=(born-previous)*kg_atom/h;previous=born
            stock,exits=advance(stock,source,{'burn':s['fast_T_DT_hazard_s']*86400},h)
            burn+=exits['burn']
        measured=s['DT_burn_atoms']*kg_atom
        rows.append(dict(case=name,elapsed_s=s['elapsed_s'],WarpX_T_burn_kg=measured,v1_2_kernel_T_burn_kg=burn,
            relative_difference=burn/measured-1,remaining_T_kg=stock,
            closure_kg=s['DD_T_birth_atoms']*kg_atom-burn-stock,
            scope='Existing v1.2 exact compartment kernel, actual WarpX birth history and independent final-spectrum hazard estimate; not full-campus coupling'))
    with (ROOT/'outputs/inventory_kernel_comparison.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(json.dumps(rows,indent=2))
if __name__=='__main__':main()
