"""Transport-to-inventory interface; requires real run artifacts and hashes.

No fallback to assumed yields. Same run reused by A/B shares each MC draw.
Uncertainty here is numerical tally sampling only, not nuclear-data covariance
or calibrated model discrepancy. Research geometry remains unqualified.
"""
import argparse,csv,hashlib,json,math,random
from pathlib import Path
from fuelcycle.model import simulate
from fuelcycle.physics import argon_burn_fraction
from fuelcycle.schedules import generate

ROOT=Path(__file__).resolve().parent

from functools import lru_cache
@lru_cache(maxsize=128)
def raw_salt_moments(path, digest):
    # digest is part of the cache key, so changed bytes cannot reuse old moments.
    import openmc
    with openmc.StatePoint(path,autolink=False) as sp:
        t=sp.get_tally(name='salt_T_tracklength')
        return float(t.mean.sum()),float(t.std_dev.sum())

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def response(directory):
    directory=Path(directory)
    r=json.loads((directory/'result.json').read_text());p=json.loads((directory/'provenance.json').read_text())
    if r.get('kind')!='ACTUAL_OPENMC_TRANSPORT_IN_ASSUMED_GEOMETRY':raise ValueError('NOT A TRANSPORT RESULT')
    if r['provenance_sha256']!=sha(directory/'provenance.json') or r['case']!=p['case']:
        raise ValueError('result/provenance mismatch')
    sp=directory/f"statepoint.{r['case']['batches']}.h5"
    if not sp.exists() or r['statepoint_sha256']!=sha(sp):raise ValueError('missing or changed raw statepoint')
    for name,expected in p['input_hashes'].items():
        if sha(directory/name)!=expected:raise ValueError('input-file hash mismatch')
    if not r['particle_balance_pass'] or not r['estimators_agree']:raise ValueError('failed numerical transport checks')
    y=r['tallies']['salt_T_tracklength:H3-production']
    raw_mean,raw_se=raw_salt_moments(str(sp.resolve()),r['statepoint_sha256'])
    if not math.isclose(y['mean'],raw_mean,rel_tol=1e-12,abs_tol=1e-14) or not math.isclose(y['se_bound'],raw_se,rel_tol=1e-12,abs_tol=1e-14):
        raise ValueError('processed tally does not match raw statepoint')
    if min(y['mean'],y['se_bound'])<0 or not all(math.isfinite(v) for v in y.values()):raise ValueError('invalid tally moments')
    return r,y

def apply_responses(p,dd_directory,a_dt_directory,b_dt_directory):
    configs=[];yield_data=[]
    for directory,source in [(dd_directory,'DD'),(a_dt_directory,'DT'),(b_dt_directory,'DT')]:
        r,y=response(directory)
        if r['case']['source']!=source:raise ValueError('DD/DT source normalization mismatch')
        configs.append(r['case']);yield_data.append(y)
    # DD and DT responses for A must use the same geometry/materials.
    drop={'source','seed','particles','batches'}
    if {k:v for k,v in configs[0].items() if k not in drop}!={k:v for k,v in configs[1].items() if k not in drop}:
        raise ValueError('A DD/DT response geometry mismatch')
    cfg=dict(p,a_dd_blanket_yield=yield_data[0]['mean'],a_dt_blanket_yield=yield_data[1]['mean'],tbr_b=yield_data[2]['mean'])
    if configs[0]['nonbreeder']:cfg.update(case='A0')
    cfg['a_yield_status']='Actual transport in ASSUMED spherical geometry; no ARC design validation'
    return cfg

def write(name,rows):
    with (ROOT/'outputs'/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,required=True);a=ap.parse_args()
    p=json.loads((ROOT/'inputs/fuel_cycle.json').read_text());p['days']=365
    f=argon_burn_fraction(p['a_fast_fraction'],p['a_density_m3'],p['a_reactivity_m3_s'],p['a_residence_s'])
    table=list(csv.DictReader((ROOT/'outputs/transport_summary.csv').read_text().splitlines()))
    fixed=[];optimized=[]
    for x in (.075,.20,.30,.90):
        candidates=[]
        for cm in (60.,90.,120.):
            dd=f'DD_Li{x:g}_cm{cm:g}';dt=f'DT_Li{x:g}_cm{cm:g}'
            _,yd=response(a.cache/dd);_,yt=response(a.cache/dt)
            score=yd['mean']+f*yt['mean']
            candidate=dict(li6=x,blanket_cm=cm,dd_case=dd,dt_case=dt,
                A_weighted_T_per_primary_DD_neutron=score,A_se_bound=yd['se_bound']+f*yt['se_bound'],
                B_T_per_DT_neutron=yt['mean'],B_se_bound=yt['se_bound'],
                evidence='POTENTIAL-DERIVED use of actual transport in assumed geometry')
            candidates.append(candidate)
            if cm==90:fixed.append(candidate)
        best_A=max(candidates,key=lambda c:c['A_weighted_T_per_primary_DD_neutron'])
        best_B=max(candidates,key=lambda c:c['B_T_per_DT_neutron'])
        optimized.append(dict(li6=x,A_grid_max_cm=best_A['blanket_cm'],B_grid_max_cm=best_B['blanket_cm'],
            A_grid_max_mean=best_A['A_weighted_T_per_primary_DD_neutron'],A_se_bound=best_A['A_se_bound'],
            B_grid_max_mean=best_B['B_T_per_DT_neutron'],B_se_bound=best_B['B_se_bound'],
            engineering_optimum=None,status='Exploratory point-estimate maxima; MC selection bias and engineering constraints unresolved'))
    write('fixed_geometry_comparison.csv',fixed);write('independent_geometry_grid_maxima.csv',optimized)
    # A2 is an exploratory grid selection, not qualified optimization.
    best_x=max(optimized,key=lambda c:c['A_grid_max_mean'])
    a2_dd=f"DD_Li{best_x['li6']:g}_cm{best_x['A_grid_max_cm']:g}"
    a2_dt=a2_dd.replace('DD_','DT_',1)
    definitions={'A0':('DD_A0_both_Li_zero','DT_A0_both_Li_zero'),
                 'A1':('DD_Li0.075_cm90','DT_Li0.075_cm90'),'A2_grid_candidate':(a2_dd,a2_dt)}
    rows=[];draws=[];rng=random.Random(6119)
    for label,(dd,dt) in definitions.items():
      for secondary in (False,True):
        for condition in ('reference','poor_recovery','independent_outages','common_outage','cold_start','processor_7d','extractor_7d','B_port10'):
            base=dict(p)
            if not secondary:base.update(a_reaction_day=0,a_fast_fraction=0)
            if condition=='poor_recovery':base.update(a_plasma_recovery=.7,a_blanket_recovery=.6,process_recovery=.99)
            if condition=='cold_start':base.update(initial_b_kg=0,initial_a_kg=0)
            schedule=[(1,1)]*365
            if condition=='independent_outages':schedule=generate(365,119,.85,.90,0)
            if condition=='common_outage':schedule=generate(365,119,.9,.9,.15)
            b_case='DT_port10' if condition=='B_port10' else 'DT_Li0.075_cm90'
            cfg=apply_responses(base,a.cache/dd,a.cache/dt,a.cache/b_case)
            if label=='A2_grid_candidate':cfg['case']='A2'
            components=[(1,1,1,1)]*365
            if condition in ('processor_7d','extractor_7d'):
                for day in range(30,37):components[day]=(1,1,1,0) if condition=='processor_7d' else (1,0,1,1)
            trajectory,s=simulate(cfg,schedule,components)
            last=trajectory[-1]
            rd,_=response(a.cache/dd);ra,_=response(a.cache/dt);rb,_=response(a.cache/b_case)
            nonfuel=lambda r:max(0.,r['tallies']['global_T:H3-production']['mean']-r['tallies']['salt_T_tracklength:H3-production']['mean'])
            from fuelcycle.physics import T_KG_PER_ATOM
            # Source estimate outside mobile-fuel boundary, never delivered or
            # folded into fuel inventory; wall retention/release remains open.
            nonfuel_birth=nonfuel(rd)*s['dd_neutrons']*T_KG_PER_ATOM+nonfuel(ra)*last['a_burn']+nonfuel(rb)*last['b_burn']
            rows.append(dict(case=label,secondary_dt=secondary,condition=condition,
                A_DD_response=cfg['a_dd_blanket_yield'],A_DT_response=cfg['a_dt_blanket_yield'],B_TBR=cfg['tbr_b'],
                gross_A_blanket_T_kg=last['blanket_a_birth'],gross_B_blanket_T_kg=last['blanket_b_birth'],
                recovered_A_plasma_T_kg=last['a_plasma_processed'],recovered_A_blanket_T_kg=last['a_blanket_processed'],
                B_extracted_to_processing_kg=last['b_extracted'],B_processing_to_storage_kg=last['b_processed'],
                processing_loss_kg=last['process_loss'],permeation_kg=last['permeation'],decay_kg=last['decay'],
                A_to_B_kg=last['a_to_b'],B_burn_kg=last['b_burn'],initial_kg=s['initial_kg'],final_kg=s['final_kg'],
                inventory_change_kg=s['inventory_change_kg'],unserved_burn_kg=s['b_unserved_burn_kg'],
                mass_residual_kg=s['maximum_mass_residual_kg'],qualified_usable_surplus_kg=None,
                nonfuel_boundary_T_birth_estimate_kg=nonfuel_birth,
                evidence='POTENTIAL-DERIVED integrated spherical testbed; operational self-sufficiency UNRESOLVED'))
            if secondary and condition=='reference':
                write(f'{label}_daily.csv',trajectory)
                # One value per unique response directory preserves reuse correlation.
                unique={name:response(a.cache/name)[1] for name in {dd,dt,'DT_Li0.075_cm90'}}
                for draw in range(32):
                    y={name:max(0,rng.gauss(v['mean'],v['se_bound'])) for name,v in unique.items()}
                    sample=dict(cfg,a_dd_blanket_yield=y[dd],a_dt_blanket_yield=y[dt],tbr_b=y['DT_Li0.075_cm90'])
                    _,out=simulate(sample,schedule)
                    draws.append(dict(case=label,draw=draw,A_DD=y[dd],A_DT=y[dt],B_DT=y['DT_Li0.075_cm90'],
                        final_kg=out['final_kg'],unserved_burn_kg=out['b_unserved_burn_kg'],
                        uncertainty='Approximate tally-statistical-only draws with conservative marginal SE; no physical/cross-section covariance'))
    write('integrated_cases.csv',rows);write('transport_statistical_draws.csv',draws)
    reserve=[]
    for label,(dd,dt) in definitions.items():
      for condition in ('reference','processor_7d','B_port10'):
        cfg=apply_responses(p,a.cache/dd,a.cache/dt,a.cache/('DT_port10' if condition=='B_port10' else 'DT_Li0.075_cm90'))
        schedule=[(1,1)]*365;components=[(1,1,1,1)]*365
        if condition=='processor_7d':
            for day in range(30,37):components[day]=(1,1,1,0)
        lo,hi=0.,200.
        for _ in range(20):
            mid=(lo+hi)/2
            _,s=simulate(dict(cfg,initial_b_kg=mid),schedule,components)
            if s['b_unserved_burn_kg']>1e-8:lo=mid
            else:hi=mid
        reserve.append(dict(case=label,condition=condition,startup_B_lower_kg=lo,startup_B_upper_kg=hi,
            horizon_days=365,step_days=cfg['step_days'],criterion='Cumulative unserved B burn <=1e-8 kg; zero regulatory reserve floor',
            classification='POTENTIAL-DERIVED finite-horizon fuel-availability bracket; not qualified startup reserve'))
    write('startup_reserve_brackets.csv',reserve)
    (ROOT/'outputs/integration_status.json').write_text(json.dumps(dict(
        selected_A2_grid_case=a2_dd,geometry_scope='ASSUMED spherical testbed, not ARC V3A',
        qualified_usable_surplus_kg=None,G2_physical_validation=False,
        uncertainty='MC statistical approximation only; source model, nuclear data, temperature, material and geometry uncertainties not quantified'),indent=2)+'\n')

if __name__=='__main__':main()
