#!/usr/bin/env python3
"""Runnable A/B/C campaign planning and identity validation; no physics outputs invented."""
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parent

def validate(r):
    cfg=r['configurations'];by={c['alias']:c for c in cfg}
    if set(by)!={'A','B','C'} or len({c['id'] for c in cfg})!=3:raise ValueError('Require three unique primary identities')
    a,b,c=(by[x] for x in 'ABC');cm=set(c['research_modules']);am=set(a['research_modules'])
    if a['inherits'] or a['stars_module_inheritance'] or am & cm:raise ValueError('A must not silently inherit STARS inventory')
    if c['inherits'] or any(x.startswith('new_') or x=='enn_fast_proton_coupling' for x in cm):raise ValueError('C must preserve its reference inventory')
    inventory=ROOT/r['original_inventory']['path']
    if hashlib.sha256(inventory.read_bytes()).hexdigest()!=r['original_inventory']['sha256']:raise ValueError('Original inventory copy changed')
    original={m['id'] for m in json.loads(inventory.read_text())['retained_modules']}
    if cm!=original:raise ValueError('C lost or acquired a reference module')
    if set(b['research_modules'])!=am|cm or set(b['inherits'])!={a['id'],c['id']}:raise ValueError('B must retain A and C research inventories')
    if len(b['research_modules'])!=len(set(b['research_modules'])):raise ValueError('Duplicate module identifiers in B')
    third=r['third_finding']
    if third['selected_source_id'] is not None and not third['selection_receipt']:raise ValueError('Third finding needs a source binding receipt; no default candidate')
    if third['status']=='UNRESOLVED_SELECTION' and third['selected_source_id'] is not None:raise ValueError('Unresolved third finding cannot be selected')
    if third['status']=='PROJECT_LEAD_CONFIRMED_SELECTION' and third['selected_source_id'] is None:raise ValueError('Confirmed selection must name its source')
    binding=json.loads((ROOT/'SOURCE_BINDINGS.json').read_text())
    bound=next(x for x in binding['A_ingredients'] if x['module_id']=='enn_fast_proton_coupling')
    if third['selected_source_id']!=bound['source_id']:raise ValueError('Selection does not match the versioned source binding')
    if any(m['retag_historical_runs'] for m in r['legacy_mappings']):raise ValueError('Historical relabeling prohibited')
    if any(x['performance'] is not None for x in cfg):raise ValueError('This registry cannot promote performance without a separate qualified run')
    return by

def campaign(r):
    by=validate(r);third=r['third_finding']['selected_source_id']
    planned=[]
    for alias in 'ABC':
        c=by[alias]; blockers=[]
        if alias in ('A','B') and third is None:blockers.append('THIRD_FINDING_NOT_BOUND')
        if c['full_configuration'] is None:blockers.append('EXACT_RUN_CONFIGURATION_UNPINNED')
        if alias=='B':blockers.append('INTEGRATION_HANDOFFS_NOT_SPECIFIED')
        planned.append({'architecture_id':c['id'],'alias':alias,'retained_module_count':len(c['research_modules']),'planned_metrics':{m:None for m in r['common_metrics']},'execution_status':'PLAN_ONLY_NOT_A_PHYSICS_RUN','blockers':blockers})
    return {'schema':'stellar-forge-abc-campaign-plan/0.1','registry_sha256':hashlib.sha256((ROOT/'ABC_REGISTRY.json').read_bytes()).hexdigest(),'primary_configurations':planned,'comparisons':[{'pair':'A versus C','purpose':'Architecture-level comparison of new research hybrid and original STARS'},{'pair':'B versus A','purpose':'Increment from integrating STARS; cannot isolate a single component'},{'pair':'B versus C','purpose':'Increment from integrating A; cannot isolate a single component'}],'ablation_policy':'Matched source/budget component ablations and crossed factorial controls; A/B/C alone do not identify causal synergy.','historical_results':'Remain in PR42 under original scenario IDs, not assigned to A/B/C by module resemblance.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);a=ap.parse_args()
    r=json.loads((ROOT/'ABC_REGISTRY.json').read_text());p=campaign(r)
    out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
    (out/'CAMPAIGN_PLAN.json').write_text(json.dumps(p,indent=2)+'\n')
    print(json.dumps({'status':'A_B_C_IDENTITIES_VALIDATED','physics_simulations_run':0,'configurations':len(p['primary_configurations']),'plan':str(out/'CAMPAIGN_PLAN.json')},indent=2))
if __name__=='__main__':main()
