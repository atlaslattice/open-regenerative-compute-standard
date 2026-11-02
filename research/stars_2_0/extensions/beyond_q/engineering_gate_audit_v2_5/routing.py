"""Species-resolved batch routing contract, not equipment performance.

Amounts are mol of nuclei by species. Retention/recycle/loss are disjoint
destinations. Recycle is banked once; no automatic repeated-pass credit.
Unknown coefficients are rejected rather than replaced by perfect efficiency.
"""
import math

SPECIES=('He3','He4','T','D','H')
BARYONS=dict(He3=3,He4=4,T=3,D=2,H=1)
CHARGE=dict(He3=2,He4=2,T=1,D=1,H=1)


class UnresolvedInput(ValueError):
    pass


def vector(x):
    if any(k not in SPECIES for k in x):raise ValueError('unknown species')
    r={s:float(x.get(s,0)) for s in SPECIES}
    if any(not math.isfinite(v) or v<0 for v in r.values()):raise ValueError('invalid inventory')
    return r


def secondary_burn(feed,He3_consumed_mol):
    f=vector(feed)
    if not math.isfinite(He3_consumed_mol) or not 0<=He3_consumed_mol<=min(f['He3'],f['D']):
        raise ValueError('reaction requires both He3 and D')
    x=He3_consumed_mol
    f['He3']-=x;f['D']-=x;f['He4']+=x;f['H']+=x
    return f


def route(feed,coefficients,*,capacity_mol_nuclei_day=None,days=1.,online_fraction=1.,kWh_per_mol_nuclei=None):
    f=vector(feed)
    if coefficients is None:raise UnresolvedInput('species routing coefficients unavailable')
    if set(coefficients)!=set(SPECIES):raise ValueError('provide each species explicitly')
    if not math.isfinite(days) or days<=0 or not math.isfinite(online_fraction) or not 0<=online_fraction<=1:
        raise ValueError('invalid service window')
    if capacity_mol_nuclei_day is not None and (not math.isfinite(capacity_mol_nuclei_day) or capacity_mol_nuclei_day<0):
        raise ValueError('invalid service capacity')
    total=sum(f.values())
    fraction=online_fraction if capacity_mol_nuclei_day is None else min(1.,capacity_mol_nuclei_day*days*online_fraction/total) if total else 0.
    out={d:{s:0. for s in SPECIES} for d in ['forward','recycle_bank','permanent_loss','retained']}
    for s in SPECIES:
        c=coefficients[s]
        if set(c)!=set(['forward','recycle_bank','permanent_loss']):raise ValueError('routing destinations')
        if any(not math.isfinite(v) or v<0 for v in c.values()) or sum(c.values())>1+1e-14:
            raise ValueError('fractions overlap or invalid')
        for d in c:out[d][s]=f[s]*fraction*c[d]
        out['retained'][s]=f[s]-sum(out[d][s] for d in c)
    if kWh_per_mol_nuclei is not None and (not math.isfinite(kWh_per_mol_nuclei) or kWh_per_mol_nuclei<0):
        raise ValueError('invalid process energy')
    return {'streams':out,'processed_mol_nuclei':total*fraction,
            'energy_kWh':None if kWh_per_mol_nuclei is None else total*fraction*kWh_per_mol_nuclei,
            'capacity_status':'UNRESOLVED' if capacity_mol_nuclei_day is None else 'ASSUMED_INPUT',
            'max_species_residual_mol':max(abs(f[s]-sum(out[d][s] for d in out)) for s in SPECIES)}


def assay_screen(feed,*,min_He3_fraction_of_helium=None,max_T_atoms_per_He3_atom=None):
    f=vector(feed);helium=f['He3']+f['He4']
    ratio3=f['He3']/helium if helium else None
    ratioT=f['T']/f['He3'] if f['He3'] else None
    if min_He3_fraction_of_helium is not None and not 0<=min_He3_fraction_of_helium<=1:
        raise ValueError('invalid isotope specification')
    if max_T_atoms_per_He3_atom is not None and max_T_atoms_per_He3_atom<0:raise ValueError('invalid T criterion')
    status='UNRESOLVED'
    if ratio3 is not None and ratioT is not None and min_He3_fraction_of_helium is not None and max_T_atoms_per_He3_atom is not None:
        status='PASS' if ratio3>=min_He3_fraction_of_helium and ratioT<=max_T_atoms_per_He3_atom else 'FAIL'
    return {'He3_fraction_of_helium_atoms':ratio3,'T_atoms_per_He3_atom':ratioT,
            'conditional_screen':status,'actual_qualified_product_mol':None,
            'note':'Computed synthetic feed composition is not an observed assay; other impurity criteria also unresolved'}
