"""Real OpenMC runs and adverse controls; no response-table fabrication."""
import argparse,csv,json,shutil,traceback
from pathlib import Path
from transport import case,run,sha
ROOT=Path(__file__).resolve().parent

def specification():
    jobs={}
    for source in ('DD','DT'):
        for enrichment in (.075,.20,.30,.90):
            for thickness in (60.,90.,120.):
                name=f'{source}_Li{enrichment:g}_cm{thickness:g}'
                jobs[name]=case(source=source,li6=enrichment,blanket_cm=thickness,seed=119 if source=='DD' else 219)
        for material in ('eurofer_surrogate','vanadium_4cr4ti'):
            jobs[f'{source}_{material}']=case(source=source,alloy=material,seed=319 if source=='DD' else 419)
        for name,options in [('port10',{'port_fraction':.1}),('no_multiplier',{'multiplier':False}),
          ('structure_double',{'structure_scale':2}),('Li6_zero',{'li6':0}),('Li7_zero',{'li6':1}),
          ('A0_both_Li_zero',{'nonbreeder':True}),('vacuum',{'vacuum':True})]:
            jobs[f'{source}_{name}']=case(source=source,seed=519 if source=='DD' else 619,**options)
    # Independent seeds / larger history counts on the central DT case.
    jobs['DT_independent_seed']=case(source='DT',seed=917)
    jobs['DT_more_histories']=case(source='DT',seed=1219,particles=4000,batches=60)
    return jobs

def summary(name,r):
    t=r['tallies'];get=lambda key,field='mean':t.get(key,{}).get(field,0.)
    return dict(case_id=name,source=r['case']['source'],li6=r['case']['li6'],blanket_cm=r['case']['blanket_cm'],
       alloy=r['case']['alloy'],port_fraction=r['case']['port_fraction'],multiplier=r['case']['multiplier'],
       nonbreeder=r['case']['nonbreeder'],vacuum=r['case']['vacuum'],histories=r['case']['particles']*r['case']['batches'],
       T_per_source_neutron=get('salt_T_tracklength:H3-production'),T_se_bound=get('salt_T_tracklength:H3-production','se_bound'),
       Li6_T=get('Li6_T:H3-production'),Li7_T=get('Li7_T:H3-production'),global_T=get('global_T:H3-production'),
       neutron_heat_eV=get('global_heat:heating'),leakage=get('leakage:current'),
       particle_balance_residual=r['neutron_balance_residual'],particle_balance_pass=r['particle_balance_pass'],
       independent_estimators_agree=r['estimators_agree'],
       classification='ACTUAL TRANSPORT / ASSUMED SPHERICAL TESTBED; NOT ARC VALIDATION')

def main():
    p=argparse.ArgumentParser();p.add_argument('--xs',required=True);p.add_argument('--executable',required=True)
    p.add_argument('--cache',type=Path,required=True);p.add_argument('--only',nargs='*');a=p.parse_args()
    jobs=specification();ROOT.joinpath('outputs').mkdir(exist_ok=True)
    (ROOT/'outputs/campaign_plan.json').write_text(json.dumps(jobs,indent=2)+'\n')
    rows=[];failures=[]
    for name,c in jobs.items():
        if a.only and name not in a.only:continue
        directory=a.cache/name
        try:
            if (directory/'result.json').exists():
                r=json.loads((directory/'result.json').read_text())
                if r['case']!=c:raise ValueError('cached case mismatch: use a fresh cache')
            else:r=run(c,a.xs,directory,a.executable)
            dest=ROOT/'outputs/runs'/name;dest.mkdir(parents=True,exist_ok=True)
            for path in directory.iterdir():
                if path.suffix in ('.json','.xml','.txt'):shutil.copyfile(path,dest/path.name)
            rows.append(summary(name,r))
            print(name,rows[-1]['T_per_source_neutron'],flush=True)
        except Exception as e:
            failures.append(dict(case_id=name,error=str(e)))
            print('FAILED',name,str(e),flush=True)
    if rows:
        with (ROOT/'outputs/transport_summary.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (ROOT/'outputs/campaign_failures.json').write_text(json.dumps(failures,indent=2)+'\n')
    if failures:raise SystemExit('Transport campaign has failures; see campaign_failures.json')

if __name__=='__main__':main()
