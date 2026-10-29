"""Common-proposal convention/mutation diagnostics, not a confidence interval."""
import argparse,json
from pathlib import Path
import numpy as np
from run_shapes import calculate,encoded

def main():
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--samples',type=int,required=True);p.add_argument('--seed',type=int,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve previous sensitivity')
    c=json.loads(a.config.read_text());base=calculate(c,samples=a.samples,seed=a.seed)
    name='COHERENT_RAW_COEFFICIENT_0p76_PHASE_0p67_2PI';ref=np.array(base['cases'][name]['alpha_CM_counts_per_conditional_event'])
    variants=[('ABSOLUTE_COULOMB_PHASE_CONVENTION_STRESS',dict(c,coulomb_phase_convention='ABSOLUTE_LOG_GAMMA')),
        ('OMITTED_91p84keV_THRESHOLD_OFFSET_MUTATION',dict(c,pair_level_above_threshold_MeV=3.037))]
    rows=[]
    for label,changed in variants:
        r=calculate(changed,samples=a.samples,seed=a.seed);x=r['cases'][name];y=np.array(x['alpha_CM_counts_per_conditional_event'])
        rows.append(dict(label=label,config=changed,preferred_coherent_case=x,
            L1_difference_of_alpha_probability_histograms=float(np.sum(np.abs(y-ref))/3),
            interpretation='conditional diagnostic; phase conventions require matching amplitude definition; omitted threshold offset is a deliberate mutation, not a physical uncertainty draw'))
    out=dict(samples=a.samples,seed=a.seed,common_proposal=True,baseline_config=c,baseline_preferred_case=base['cases'][name],
        confidence_interval=None,source_refit='NOT_RUN',variants=rows)
    a.out.mkdir(parents=True,exist_ok=False);(a.out/'SENSITIVITY.json').write_text(encoded(out))
    print(encoded({r['label']:r['L1_difference_of_alpha_probability_histograms'] for r in rows}))

if __name__=='__main__':main()
