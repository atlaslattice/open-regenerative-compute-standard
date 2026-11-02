"""Append-only convention and engineering-gap audit. Python stdlib only."""
import csv
import hashlib
import json
import math
from pathlib import Path
from routing import SPECIES,BARYONS,CHARGE,secondary_burn,route,assay_screen

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent
NA=6.02214076e23; MEV_J=1.602176634e-13; FPY_S=365.25*86400
R=8.31446261815324


def gas_volume_L(mol_nuclei,species,T_K=273.15,P_Pa=101325.,*,rounded_parent=False):
    if species not in ['He3','He4','T_atom_equivalent','T2']:raise ValueError('declare atom/molecule basis')
    if any(not math.isfinite(v) for v in [mol_nuclei,T_K,P_Pa]) or mol_nuclei<0 or T_K<=0 or P_Pa<=0:raise ValueError('invalid gas inputs')
    if rounded_parent and (T_K!=273.15 or P_Pa!=101325.):raise ValueError('parent convention is0C/1atm only')
    mol_gas=mol_nuclei/2 if species=='T2' else mol_nuclei
    vm=22.414 if rounded_parent else R*T_K/P_Pa*1000
    return mol_gas*vm


def mean_DD_MeV(T_branch):
    if not 0<=T_branch<=1:raise ValueError('branch')
    return T_branch*4.03+(1-T_branch)*3.27


def write(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def demonstrate():
    # SYNTHETIC molar packet, unrelated to a specified reactor exhaust.
    born={'He3':100.,'T':100.,'D':1000.,'He4':0.,'H':0.}
    current=secondary_burn(born,30.)
    after_reaction=current.copy(); rows=[]; banks={d:{s:0. for s in SPECIES} for d in ['recycle_bank','permanent_loss','retained']}
    for name in ['plasma_exhaust','divertor_capture','vacuum_pumping','hydrogen_helium_separation','He3_He4_separation','purification']:
        coefficients={s:dict(forward=.9,recycle_bank=.05,permanent_loss=.02) for s in SPECIES}
        if name=='hydrogen_helium_separation':
            for s in ['T','D','H']:coefficients[s]=dict(forward=.001,recycle_bank=.998,permanent_loss=0.)
        if name=='He3_He4_separation':coefficients['He4']=dict(forward=.01,recycle_bank=.98,permanent_loss=0.)
        result=route(current,coefficients)
        for s in SPECIES:
            rows.append(dict(stage=name,species=s,input_mol_nuclei=current[s],
                **{d+'_mol_nuclei':result['streams'][d][s] for d in result['streams']},
                evidence='SYNTHETIC ROUTING TEST; NOT REACTOR PERFORMANCE'))
            for d in banks:banks[d][s]+=result['streams'][d][s]
        current=result['streams']['forward']
    purified_candidate=current.copy()
    for s in SPECIES:
        banks['retained'][s]+=current[s]
        rows.append(dict(stage='qualified_storage_hold',species=s,input_mol_nuclei=current[s],
            forward_mol_nuclei=0.,recycle_bank_mol_nuclei=0.,permanent_loss_mol_nuclei=0.,retained_mol_nuclei=current[s],
            evidence='HELD: no observed assay or buyer specification'))
    final={s:sum(banks[d][s] for d in banks) for s in SPECIES}
    residual=max(abs(after_reaction[s]-final[s]) for s in SPECIES)
    sums=lambda v,w:sum(v[s]*w[s] for s in SPECIES)
    return rows,dict(initial_mol_nuclei=born,post_secondary_reaction_mol_nuclei=after_reaction,
        secondary_He3_consumed_mol=30.,additional_He4_born_mol=30.,purified_candidate_mol_nuclei=purified_candidate,
        destinations=banks,max_species_residual_mol=residual,
        reaction_baryon_residual_mol=sums(born,BARYONS)-sums(after_reaction,BARYONS),
        reaction_charge_residual_mol=sums(born,CHARGE)-sums(after_reaction,CHARGE),
        assay=assay_screen(purified_candidate),complete_process_energy_kWh=None,
        scope='Single synthetic batch routing. Banked recycle is not automatically re-fed; no hardware or continuous-plant calibration.')


def main():
    p=json.loads((ROOT/'engineering_inputs.json').read_text());out=ROOT/'outputs';out.mkdir(exist_ok=True)
    rows,demo=demonstrate();write(out/'synthetic_stage_ledger.csv',rows)
    (out/'synthetic_account.json').write_text(json.dumps(demo,indent=2)+'\n')
    vm=22.414
    gross=1100e6/(3.65*MEV_J)*.5*FPY_S*.85/NA*vm
    scenarios=[]
    for r in p['overall_He3_potential_recovery_cases']:
        potential=gross*r
        scenarios.append(dict(A_primary_DD_MW=1100,B_DT_reference_MW=1130,effective_exposure=.85,
            gross_He3_STP_L=gross,overall_assumed_recovery=r,recovered_potential_STP_L=potential,
            measured_recovered_STP_L=None,purified_product_candidate_STP_L=potential,qualified_saleable_STP_L=None,
            internal_He3_allocation_STP_L=0.,secondary_He3_consumption_STP_L=None,internal_scope='Zero mandatory internal allocation; secondary burn remains unresolved inside assumed overall recovery',
            assumed_USD_per_STP_L=p['assumed_He3_price_USD_per_STP_L'],
            conditional_value_USD=potential*p['assumed_He3_price_USD_per_STP_L'],actual_revenue_USD=None,
            actual_profit_USD=None,complete_CAPEX_USD=None,complete_OPEX_USD=None,
            evidence='POTENTIAL-DERIVED steady-throughput illustration, NOT year1 finance'))
    write(out/'product_finance_boundaries.csv',scenarios)
    volumes=[]
    for label,temp,pressure in [('STP_0C_1atm',273.15,101325.),('STP_0C_1bar_comparator',273.15,100000.)]:
        mol=350000/vm
        volumes.append(dict(reference=label,T_K=temp,P_Pa=pressure,molar_volume_ideal_L=gas_volume_L(1.,'He3',temp,pressure),
            parent_rounded_molar_volume_L=vm,He3_for_parent_350kL_amount_L=gas_volume_L(mol,'He3',temp,pressure),
            T_atom_equivalent_for_equal_nuclei_L=gas_volume_L(mol,'T_atom_equivalent',temp,pressure),
            T2_for_equal_nuclei_L=gas_volume_L(mol,'T2',temp,pressure),
            He3_mass_kg=mol*.0030160293201,T_equal_nuclei_mass_kg=mol*.00301604928,
            T_mass_if_350k_molecular_T2_L_parent_basis_kg=2*mol*.00301604928))
    write(out/'volume_conventions.csv',volumes)
    b_rows=[]
    factor=1e9/(17.6*MEV_J)*FPY_S*.00301604928/NA
    for power in [1100,1130]:
        burn=factor*power/1000
        b_rows.append(dict(B_DT_fusion_MW=power,Q_DT_MeV=17.6,derived_T_kg_per_GW_FPY=factor,
            uninterrupted_T_burn_kg_FPY=burn,historical_55_8_convention_T_kg_FPY=55.8*power/1000,
            illustrative_one_FPY_plus_10kg_startup_floor_kg=burn+10.,gross_B_TBR_assumed=1.,
            gross_blanket_birth_kg_FPY_if_TBR1=burn,qualified_recovered_blanket_kg_FPY=None,
            operational_self_sufficiency='UNRESOLVED'))
    write(out/'B_reference_comparison.csv',b_rows)
    branches=[]
    for f in [.5,.48096]:
        q=mean_DD_MeV(f);wrong=f*3.27+(1-f)*4.03
        branches.append(dict(T_branch_fraction=f,correct_mean_Q_MeV=q,swapped_label_mean_Q_MeV=wrong,
            swapped_label_source_rate_fractional_bias=q/wrong-1,
            neutron_births_per_primary_event=1-f,He3_births_per_primary_event=1-f,T_births_per_primary_event=f,
            meaning='Equal-branch convention' if f==.5 else 'Archived short kinetic sample used only as arithmetic sensitivity'))
    write(out/'branch_energy_audit.csv',branches)
    states=[dict(stage=s['name'],status='UNRESOLVED',reason='Missing measured routing/operating data or product assay',
        energy_kWh=None,capacity_qualified=False,replacement_interval_days=None) for s in p['stages']]
    write(out/'engineering_stage_status.csv',states)
    hashes={}
    for rel in ['fuel_cascade_v2_2/inputs.json','fuel_cascade_v2_2/kernel.py','isotope_value_v1_6/account.py',
                'multiscale_v1_4/fuelcycle/physics.py','capture_target_v1_9/inputs.json']:
        hashes[rel]=hashlib.sha256((PARENT/rel).read_bytes()).hexdigest()
    (out/'parent_audit_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print(json.dumps(dict(stage_ledger_rows=len(rows),max_species_residual_mol=demo['max_species_residual_mol'],
        physical_calibration=False,B_reference_MW=1130,prior_parent_B_MW=json.loads((PARENT/'fuel_cascade_v2_2/inputs.json').read_text())['B_fusion_MW']),indent=2))


if __name__=='__main__':main()
