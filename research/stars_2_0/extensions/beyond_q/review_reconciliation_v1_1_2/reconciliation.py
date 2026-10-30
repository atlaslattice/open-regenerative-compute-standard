"""Explicit mass conventions and conditional screening, no physical validation."""
from fuelcycle.physics import AVOGADRO,MEV_J,FPY_S,dd_source,T_KG_PER_ATOM

def tritium_factor(q_mev=17.6,molar_kg=.00301604928,fpy_days=365.25):
    if min(q_mev,molar_kg,fpy_days)<=0:raise ValueError('positive inputs required')
    # GW J/s * seconds / (J/reaction) * kg/atom
    return 1e9*(fpy_days*86400)/(q_mev*MEV_J)*(molar_kg/AVOGADRO)

def static_balance(burn,a_plasma_net,a_blanket_gross,eta_plasma,eta_blanket,
                   tbr_b,eta_b,loss=0.,reserve_addition=0.):
    if burn<=0 or min(a_plasma_net,a_blanket_gross,loss,reserve_addition,tbr_b)<0:
        raise ValueError('invalid mass source/sink')
    if any(not 0<=x<=1 for x in (eta_plasma,eta_blanket,eta_b)) or eta_b==0:
        raise ValueError('invalid recovery')
    a=eta_plasma*a_plasma_net+eta_blanket*a_blanket_gross
    s=a+eta_b*tbr_b*burn-burn-loss-reserve_addition
    return dict(a_assumed_recovered_kg=a,surplus_kg=s,surplus_percent_B_burn=100*s/burn,
        tbr_b_break_even=(burn+loss+reserve_addition-a)/(eta_b*burn),
        qualified_usable_surplus_kg=None,evidence='POTENTIAL-DERIVED')

def source_case(f,dd_yield,dt_yield):
    if not 0<=f<=1 or min(dd_yield,dt_yield)<0:raise ValueError('invalid source case')
    d=dd_source();birth=d['t_atoms_s']*FPY_S*T_KG_PER_ATOM
    burn=birth*f
    primary_n=d['n_atoms_s']*FPY_S
    secondary_n=burn/T_KG_PER_ATOM
    blanket=dd_yield*primary_n*T_KG_PER_ATOM+dt_yield*burn
    return dict(dd_birth_kg=birth,a_secondary_burn_kg=burn,
        plasma_net_kg=birth-burn,dd_neutrons=primary_n,dt_neutrons=secondary_n,
        blanket_gross_kg=blanket)

def enrichment_plan():
    rows=[]
    for route in ['fixed_geometry','separately_optimized_geometry']:
        for alloy in ['inconel_surrogate','vanadium_4cr4ti','eurofer_surrogate']:
            for li in [.075,.20,.30,.90]:
                rows.append(dict(route=route,li6_atom_fraction=li,alloy=alloy,
                    fixed_blanket_cm=90 if route=='fixed_geometry' else None,
                    candidate_blanket_cm='85;90;100' if route!='fixed_geometry' else '90',
                    common_basis='same source spectrum and normalization, stoichiometry, temperature, ports and scoring',
                    tbr=None,optimized_geometry=None,
                    status='UNRESOLVED: no transport data; no geometry optimum selected'))
    return rows

def constant_inventory_example(old_mass=118.6,old_fraction=.9,new_fraction=.25):
    # Mass/fraction normalization example only; not a salt/geometry calculation.
    return old_mass*old_fraction/new_fraction
