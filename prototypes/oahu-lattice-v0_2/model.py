#!/usr/bin/env python3
"""Oahu v0.2 module extension: capacity, conserved washing ledger and break-even ceilings.

Stdlib only. Generic demonstration, not a design/quote/cleanup certification.
Run beside unchanged ../oahu-lattice-v0_1 or local ../oahu-lattice-v01.
"""
import csv
import importlib.util
import json
import math
from pathlib import Path

ROOT=Path(__file__).parent

def bounded(x):
    if not math.isfinite(x) or not 0 <= x <= 1:
        raise ValueError('fraction outside [0,1]')
    return x

def washing_ledger(dry_feed_t, initial_water_t, added_water_t,
                   product_fraction=.70, contaminant_kg_per_dry_t=1.,
                   contaminant_partition=(.04,.95,.01), cake_solids=.50,
                   quality_limit_mgkg=100., clearance=False):
    """Mass basis = carrier dry solids + water, with a separate trace-contaminant ledger.

    Trace contaminant is embedded within carrier dry mass (not added again).
    Partition order: product, cake, water. Illustrative generic contaminant,
    not a legal threshold for any named substance. No contaminant destruction.
    clearance represents ALL external permissions/offtake/non-modeled criteria.
    Filtrate is an output/liability; no implied discharge or crop-use credit.
    """
    for value in [dry_feed_t,initial_water_t,added_water_t,contaminant_kg_per_dry_t,quality_limit_mgkg]:
        if not math.isfinite(value) or value < 0: raise ValueError('invalid mass or threshold')
    if dry_feed_t <= 0: raise ValueError('empty feed')
    bounded(product_fraction); bounded(cake_solids)
    if not 0 < cake_solids <= 1 or not 0 <= product_fraction < 1:
        raise ValueError('nonzero cake and solids fraction required')
    if len(contaminant_partition)!=3: raise ValueError('three contaminant destinations required')
    for v in contaminant_partition: bounded(v)
    if not math.isclose(sum(contaminant_partition),1.,abs_tol=1e-10):
        raise ValueError('contaminant disappearing or double counted')
    product=dry_feed_t*product_fraction
    cake_dry=dry_feed_t-product
    cake_water=cake_dry*(1/cake_solids-1)
    water=initial_water_t+added_water_t
    if cake_water > water: raise ValueError('insufficient water for assumed cake moisture')
    filtrate=water-cake_water
    total_contaminant=dry_feed_t*contaminant_kg_per_dry_t
    masses=[total_contaminant*x for x in contaminant_partition]
    if masses[0] > product*1000 or masses[1] > cake_dry*1000:
        raise ValueError('contaminant mass exceeds solids carrier')
    if masses[2] and not filtrate: raise ValueError('aqueous contamination has no carrier')
    product_mgkg=masses[0]*1000/product if product else None
    passed=bool(clearance and product and product_mgkg<=quality_limit_mgkg)
    mass_error=dry_feed_t+water-product-cake_dry-cake_water-filtrate
    contaminant_error=total_contaminant-sum(masses)
    return dict(dry_feed_t=dry_feed_t,gross_water_input_t=water,
        candidate_product_dry_t=product,accepted_product_dry_t=product if passed else 0.,
        rejected_product_dry_t=0. if passed else product,
        cake_dry_t=cake_dry,cake_wet_t=cake_dry+cake_water,
        filtrate_t=filtrate,filtrate_status='must be treated/recycled with purge accounting, or disposed',
        contaminant_input_kg=total_contaminant,contaminant_product_kg=masses[0],
        contaminant_cake_kg=masses[1],contaminant_water_kg=masses[2],
        product_mgkg=product_mgkg,quality_limit_is_hypothetical=True,
        external_clearance=clearance,accepted=passed,
        mass_error_t=mass_error,contaminant_error_kg=contaminant_error)

def annualized_capital(capex,rate,years):
    if capex is None: return None
    if capex<0 or rate<0 or years<=0: raise ValueError('invalid financing assumption')
    factor=1/years if rate==0 else rate*(1+rate)**years/((1+rate)**years-1)
    return capex*factor

def complete_cost(feed_t,annualized_capex,fixed_om,variable_cost,energy,
                  water_reagents,testing,transport,residual_management,
                  accepted_product_netback,avoided_baseline):
    """Annual operator/project comparison; enter incremental avoidable costs only.

    Each item is an ANNUAL dollar total. Supply explicit zero when justified.
    Unknown != zero. Netback excludes costs already in this ledger.
    Tipping charges internal to a public system are transfers, not automatic savings.
    """
    vals=locals().copy(); vals.pop('feed_t')
    if feed_t<=0: raise ValueError('nonpositive throughput')
    missing=[k for k,v in vals.items() if v is None]
    if missing: return {'rankable':False,'net_cost_usd_per_t':None,'missing':missing}
    if any(not math.isfinite(v) for v in vals.values()): raise ValueError('nonfinite cost')
    costs=sum(v for k,v in vals.items() if k not in ['accepted_product_netback','avoided_baseline'])
    return {'rankable':True,'net_cost_usd_per_t':(costs-accepted_product_netback-avoided_baseline)/feed_t,'missing':[]}

def cost_ceiling(accepted_fraction,baseline_disposal,cake_disposal,netback):
    """Hypothetical $/DRY-t feed ceiling for ALL other costs of a wash train.

    Residuals not accepted remain disposed. Rates on dry-equivalent basis for
    arithmetic only. Actual quotes must use wet masses and actual waste classes.
    This is incremental to not washing an already-separated mineral stream.
    """
    bounded(accepted_fraction)
    return baseline_disposal + accepted_fraction*netback - (1-accepted_fraction)*cake_disposal

def capacity_case(screen_tph,fines_fraction,washer_tph,hours=8,availability=.8):
    bounded(fines_fraction); bounded(availability)
    if screen_tph<0 or washer_tph<0 or hours<0: raise ValueError('negative capacity')
    fine_t=screen_tph*hours*availability*fines_fraction
    washed=min(fine_t,washer_tph*hours*availability)
    return dict(screen_tph=screen_tph,assumed_fines_fraction=fines_fraction,
        washer_tph_assumed=washer_tph,fines_offered_t_per_shift=fine_t,
        washed_t_per_shift=washed,unwashed_t_per_shift=fine_t-washed,
        fraction_of_fines_washed=washed/fine_t if fine_t else 0.)

def load_v01():
    for dirname in ['oahu-lattice-v0_1','oahu-lattice-v01']:
        p=ROOT.parent/dirname
        if (p/'model.py').exists():
            spec=importlib.util.spec_from_file_location('v01',p/'model.py')
            module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
            return module,json.loads((p/'inputs.json').read_text())
    raise FileNotFoundError('unchanged sibling v0.1 required; see README')

def attach_to_v01(module,cfg,tph,washer_tph=15,clearance=False):
    # Use metals-only source: no re-counting v0.1 conditional mineral products.
    rows,_=module.simulate(cfg,'v02_adapter',tph=tph)
    a=cfg['assumptions']; total_fines=washed=unwashed=incremental=0.
    for day in rows:
        fine=day['processed_t']*a['feed_fraction']['mineral_fines']
        cap=washer_tph*a['shift_hours']*a['availability'] if day['scheduled_shift'] else 0.
        feed=min(fine,cap)
        # New moisture hypothesis: as-received fines are 65% dry carrier solids.
        # No source assays exist. v0.1 had no moisture/contaminant resolution.
        dry=feed*.65
        if dry:
            ledger=washing_ledger(dry,feed-dry,dry*2,clearance=clearance)
            # Only accepted dry product counted; no credit for evaporated/wash water.
            incremental+=ledger['accepted_product_dry_t']
        total_fines+=fine; washed+=feed; unwashed+=fine-feed
    return dict(screen_tph_case=tph,processed_t=sum(x['processed_t'] for x in rows),
        offered_fines_as_received_t=total_fines,washed_as_received_t=washed,
        unwashed_as_received_t=unwashed,incremental_accepted_dry_product_t=incremental,
        credited_to_real_world_t=0,clearance_assumption=clearance,
        incremental_net_disposal_avoidance_t=None,
        note='Gross accepted dry product is NOT net disposal avoidance: cake moisture, reagents, water purge and treatment residues must be closed. No legacy stockpile or cost forecast.')

def portfolio(stream_cash_usd,shared_cost_usd,avoidable_public_cost_usd=None,gates=None):
    """Annual equivalent comparison, not a financing commitment or ROI.

    Stream cash values can have either sign. Shared costs allocated ONCE.
    Avoidable public cost must be incremental, net of remaining disposal and
    alternative infrastructure; excludes transfers already in stream cash.
    Values must share period, price year, discounting and stakeholder boundary.
    """
    gates=gates or {}
    if any(v not in ['pass','unresolved','fail'] for v in gates.values()):
        raise ValueError('unknown gate status')
    status='fail' if 'fail' in gates.values() else ('unresolved' if not gates or 'unresolved' in gates.values() else 'pass')
    unknown=shared_cost_usd is None or any(v is None for v in stream_cash_usd.values())
    cash=None if unknown else sum(stream_cash_usd.values())-shared_cost_usd
    comparison=None if cash is None or avoidable_public_cost_usd is None else cash+avoidable_public_cost_usd
    return dict(stream_cash_usd=stream_cash_usd,shared_cost_usd=shared_cost_usd,
        combined_project_cash_usd=cash,avoidable_public_cost_usd=avoidable_public_cost_usd,
        public_comparison_usd=comparison,clearance_status=status,
        minimum_avoidable_cost_to_offset_cash_gap_usd=None if cash is None else max(0,-cash),
        decision_eligible=status=='pass' and comparison is not None,
        note='Cross-subsidy permitted; no financial surplus overrides an environmental veto. Public value is not automatically cash available to the operator.')

def run():
    cat=json.loads((ROOT/'catalog.json').read_text())
    out=ROOT/'results';out.mkdir(exist_ok=True)
    module,cfg=load_v01()
    batch={
      'blocked':washing_ledger(1000,1000*.35/.65,2000,clearance=False),
      'hypothetical_all_external_gates_pass':washing_ledger(1000,1000*.35/.65,2000,clearance=True),
      'hypothetical_insufficient_separation':washing_ledger(1000,1000*.35/.65,2000,contaminant_partition=(.20,.79,.01),clearance=True)}
    capacities=[capacity_case(s,f,w) for s in [50,200] for f in [.2,.4] for w in [15,20,30]]
    # Only cataloged packages / machines with all costs unresolved: no fake ranking.
    cost=complete_cost(1000,*([None]*10))
    results={'status':'UNVALIDATED SCREENING EXTENSION; ZERO REALIZED CREDIT',
      'catalog_entries':len(cat['modules']), 'washing_ledger_examples':batch,
      'capacity_sensitivities':capacities,
      'v01_current_feed_adapter':[attach_to_v01(module,cfg,t,clearance=c) for t in [50,200] for c in [False,True]],
      'complete_cost_status':cost,
      'actual_cost_rankings':None,'physical_ROI':None,
      'portfolio_actual':portfolio({'metals':None,'fines':None,'fuel':None},None,gates={'residual_outlets':'unresolved'}),
      'portfolio_HYPOTHETICAL_cross_subsidy_examples':[
        portfolio({'metals':300000,'fines':-400000},100000,value,{'all_required_clearances':status})
        for value,status in [(None,'unresolved'),(300000,'pass'),(300000,'fail')]],
      'boundary':'Only capacity and generic washing/contaminant transfer are executed. Other catalog modules have no calibrated transfer function. All financial rates below are hypothetical sensitivity axes, not vendor/site cost estimates.'}
    (out/'summary.json').write_text(json.dumps(results,indent=2)+'\n')
    sensitivity=[]
    for accepted in [0,.35,.7]:
      for baseline in [0,50,100,200]:
       for cake in [50,100,200,400]:
        for price in [0,10,30]:
         sensitivity.append({'accepted_dry_fraction':accepted,
           'baseline_disposal_usd_per_dry_equivalent_t_HYPOTHETICAL':baseline,
           'residual_disposal_usd_per_dry_equivalent_t_HYPOTHETICAL':cake,
           'accepted_product_netback_usd_per_dry_t_HYPOTHETICAL':price,
           'max_all_other_cost_usd_per_dry_feed_t':cost_ceiling(accepted,baseline,cake,price)})
    with (out/'cost_ceilings.csv').open('w') as f:
      writer=csv.DictWriter(f,fieldnames=list(sensitivity[0]));writer.writeheader();writer.writerows(sensitivity)
    print(json.dumps({'catalog_entries':len(cat['modules']),'tests_to_run':'python -m unittest -v',
       'batch_candidate_dry_t':batch['blocked']['candidate_product_dry_t'],
       'blocked_accepted_t':batch['blocked']['accepted_product_dry_t'],
       'actual_cost_ranking':None,'cost_ceiling_cases':len(sensitivity)},indent=2))

if __name__=='__main__': run()
