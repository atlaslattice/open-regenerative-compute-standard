"""Generate diagnostic recovery ledgers; no parent-package mutation."""
import copy
import csv
import hashlib
import json
from pathlib import Path
from model import simulate, required_downstream, MOLAR_STP_L

ROOT=Path(__file__).resolve().parent


def csv_write(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def main():
    p=json.loads((ROOT/'inputs.json').read_text())
    out=ROOT/'outputs';out.mkdir(exist_ok=True)
    base=p['assumed_base_stage_parameters']
    base=base|{'birth_mol_day':p['gross_He3_STP_L_per_year_from_v2_3']/MOLAR_STP_L/p['duration_days']}
    cases={
        'illustrative_stages_70pct_plasma_escape':{},
        'no_secondary_He3_burn':{'plasma_burn_day':0.},
        'zero_He_capture':{'pump_capture_regeneration_fraction':0.},
        'pump_off_days_180_210':{'pump_off':[[180,210]]},
        'source_and_pump_off_days_180_210':{'source_off':[[180,210]],'pump_off':[[180,210]]}
    }
    summaries=[]
    for name,changes in cases.items():
        r=simulate(copy.deepcopy(base)|changes,dt=p['step_days'],days=p['duration_days'])
        csv_write(out/(name+'.csv'),r.pop('rows'))
        (out/(name+'.json')).write_text(json.dumps(r,indent=2)+'\n')
        summaries.append({'case':name,'born_STP_L':r['cumulative_mol']['born']*MOLAR_STP_L,
            'product_candidate_STP_L':r['candidate_product_STP_L'],
            'secondary_He3_consumed_STP_L':r['cumulative_mol']['secondary_burn']*MOLAR_STP_L,
            'He4_additional_born_mol':r['additional_He4_born_mol'],
            'He3_retained_in_process_mol':sum(r['stocks_mol'][k] for k in ['plasma','pump','purifier']),
            'max_abs_He3_ledger_residual_mol':r['max_abs_residual_mol'],
            'qualified_product_STP_L':None,'evidence':r['evidence']})
    csv_write(out/'summary.csv',summaries)
    targets=[]
    for survival in [.7,.8,1.]:
        for target in p['overall_baseline_recoveries_unchanged']:
            targets.append({'plasma_survival_scenario':survival,'overall_target':target,
                            **required_downstream(target,survival),'evidence':'conditional arithmetic; not universal plasma bounds'})
    csv_write(out/'required_downstream.csv',targets)
    refinement=[]
    for dt in [.25,.125,.0625]:
        r=simulate(base,dt=dt,days=p['duration_days']);refinement.append({'step_days':dt,
            'candidate_product_STP_L':r['candidate_product_STP_L'],
            'max_abs_residual_mol':r['max_abs_residual_mol']})
    (out/'refinement.json').write_text(json.dumps(refinement,indent=2)+'\n')
    transient=[]
    for dt in [.25,.125,.0625,.03125]:
        r=simulate(base,dt=dt,days=1.)
        transient.append({'step_days':dt,'first_day_candidate_STP_L':r['candidate_product_STP_L']})
    (out/'transient_refinement.json').write_text(json.dumps(transient,indent=2)+'\n')
    # Source-rounded reaction energies retained only for this precursor check.
    # They are not replacements for current nuclear constants or parent physics.
    synfuel=12.4*.6; electricity=(18.3/2)*.5
    source_audit={'report':'COO-2218-190, DOI10.2172/6712040',
        'reaction_figure_PDF_page':6,'energy_figure_PDF_page':7,
        'two_DD_plus_one_DT_source_rounded_MeV':3.2+4.0+17.6,
        'source_printed_MeV_per_primary_DD':12.4,
        'derived_synfuel_MeV_equivalent':synfuel,
        'derived_satellite_electricity_MeV_equivalent':electricity,
        'derived_fraction_synfuel_from_unrounded_outputs':synfuel/(synfuel+electricity),
        'derived_fraction_synfuel_from_printed_7_4_and_4_5':7.4/(7.4+4.5),
        'source_printed_fraction_synfuel':.74,
        'split_check':'FAIL_UNRECONCILED_AT_DISPLAYED_OUTPUT_BOUNDARY',
        'note':'Could require an unstated weighting/boundary. Preserve source; do not fit the model to74/26. This is not the1982 plasma benchmark.',
        'source_T_internal_burn_fraction_in_reaction_illustration':1.,
        'resulting_T_available_for_external_B_per_two_primary_DD_events':0.}
    (out/'precursor_arithmetic.json').write_text(json.dumps(source_audit,indent=2)+'\n')
    (out/'execution.json').write_text(json.dumps({'cases':len(cases),'GM1982_reproduced':False,
        'parent_physics_changed':False,'full_reactor_energy_closed':False,
        'hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['model.py','inputs.json','run.py']}},indent=2)+'\n')
    print(json.dumps({'cases':len(cases),'source_split_check':source_audit['split_check'],
        'max_residual_mol':max(r['max_abs_He3_ledger_residual_mol'] for r in summaries),
        'baseline_candidate_STP_L':summaries[0]['product_candidate_STP_L'],
        'refinement_fractional_difference_last_two':abs(refinement[-1]['candidate_product_STP_L']-refinement[-2]['candidate_product_STP_L'])/refinement[-1]['candidate_product_STP_L']},indent=2))


if __name__=='__main__':main()
