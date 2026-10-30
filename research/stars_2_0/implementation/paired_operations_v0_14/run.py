"""Generate the paired evidence-constrained and exploratory result package."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np

from model import attempt_accounting,overlap_probability,tail_models

def save(path,obj):Path(path).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')

def run(stability_path,out):
    out=Path(out)
    if out.exists():raise FileExistsError('Use a new immutable output directory')
    source=Path(stability_path).read_bytes();stability=json.loads(source);s=stability['summary']
    if s['run']!='20210803/run05' or s['beam_fit_entries_used']!=300:raise ValueError('Unexpected source fixture')
    rows=stability['beam_fit_rows'];cx=np.array([r['props'][1] for r in rows]);center=float(np.mean(cx));sigma=float(np.std(cx));resid=cx-center
    reference=dict(label='EVIDENCE-CONSTRAINED COMPONENT BENCHMARK',source_dose_mean_Gy=s['peak_dose_mean_Gy'],source_dose_SD_Gy=s['peak_dose_population_SD_Gy'],source_pointing_SD_mrad=s['centroid_x_population_SD_mrad'],
       component_laser_optical_J=.190,component_laser_to_proton_fraction_approx=.005,
       derived_proton_beam_energy_J_approx=.190*.005,reported_repetition_Hz=5.,
       derived_proton_beam_power_W_approx=.190*.005*5,
       boundary='Streeter2025 component experiment, not Stars, not wall-plug efficiency',
       Stars_readiness_probability=None,Stars_fire_probability_given_ready=None,
       Stars_energy_J_per_attempt=None,Stars_net_electrical_J_per_attempt=None,
       causal_acoustic_effect=None,acoustic_off_additional_credit=0,
       completeness='Component benchmarks available; full apparatus reference not determined')
    grid=np.linspace(.25,2,71);curves=[]
    for width in [.5,1.,2.]:
        records=[]
        for ratio in grid:
            empirical=float(np.mean(abs(resid*ratio)<=width*sigma))
            gaussian=overlap_probability(float(ratio),width)
            records.append(dict(jitter_sigma_ratio=float(ratio),empirical_selected_sample_overlap_fraction=empirical,
                                gaussian_overlap_fraction=gaussian))
        curves.append(dict(acceptance_halfwidth_over_reference_SD=width,records=records))
    baseline=overlap_probability(1,1);half=overlap_probability(.5,1)
    examples=[]
    for bad in [0.,.2,1.]:
        for delay in [0.,.5,1.]:
            # r=f=1 isolates jitter pathway. These are scenario choices, not
            # inferred all-attempt firing/readiness probabilities.
            b=attempt_accounting(ready_probability=1,fire_given_ready=1,physical_success_given_fired=baseline,failed_fired_energy_fraction=bad)
            h=attempt_accounting(ready_probability=1,fire_given_ready=1,physical_success_given_fired=half,failed_fired_energy_fraction=bad)
            gain=h['normalized_energy_per_attempt']/b['normalized_energy_per_attempt']
            examples.append(dict(failed_fired_energy_fraction=bad,extra_serial_preparation_over_baseline_cycle=delay,
                                 per_attempt_energy_ratio=gain,per_time_energy_ratio=gain/(1+delay),
                                 assumptions='Centered 1D Gaussian; window=reference SD; halve jitter; fixed successful-pulse energy; readiness/firing unchanged'))
    tail=[]
    for e in [2.25,3.3,3.9,4.52,5.,6.,7.5,8.]:
        nominal=tail_models(e)
        if e<=4.52:classification='DERIVED_INTERPOLATION_BETWEEN_TWO_SAME_CONDITION_ANCHORS'
        else:classification='DERIVED_EXTRAPOLATION_OUTSIDE_RECOVERED_MEASUREMENTS'
        tail.append(dict(E_MeV=e,location_um_by_model=nominal,classification=classification,
                         scenario_model_spread_um=[min(nominal.values()),max(nominal.values())],confidence_interval=None))
    corners=[tail_models(7.5,x0=x0,y0=y0,x1=x1,y1=y1) for x0,y0,x1,y1 in itertools.product([2.25-.06,2.25+.06],[.639-.0005,.639+.0005],[4.52-.11,4.52+.11],[.611-.0005,.611+.0005])]
    exploratory=dict(label='EXPLORATORY POTENTIAL SIMULATION',
       jitter_model='Analyst 1D physical overlap window; NOT diagnostic acceptance or measured acoustic transfer',
       jitter_scenarios=curves,conditional_energy_examples=examples,
       measured_centroid_source_SD_mrad=sigma,assumed_acceptance_center_mrad=center,
       narrowing_operation='Scale selected measured deviations about their mean; preserve fixed center. No causal acoustic attribution.',
       helium_location_predictions=tail,
       helium_7p5_endpoint_sensitivity_um={k:[min(c[k] for c in corners),max(c[k] for c in corners)] for k in corners[0]},
       endpoint_sensitivity_semantics='Source energy intervals used as corner sensitivities; printed locations +/-0.0005 um rounding allowance. Not statistical CI or comprehensive model uncertainty.',
       full_7p5_detector_response=None,Stars_net_electrical_output=None,
       acoustic_wall_energy=None,acoustic_CAPEX=None,
       adverse_case='Lower jitter can reduce overlap for a misaligned mean; added serial prep can reduce output per time. Stability alone need not change mean energy.')
    out.mkdir(parents=True)
    save(out/'RESULTS.json',dict(reference=reference,exploratory=exploratory))
    save(out/'RECEIPT.json',dict(stability_input_sha256=hashlib.sha256(source).hexdigest(),
        model_sha256=hashlib.sha256(Path(__file__).with_name('model.py').read_bytes()).hexdigest(),
        runner_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        deterministic=True,random_sampling=False,seed=None,scientific_freeze=False,
        energy_gain_demonstrated=False))
    return reference,exploratory

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--stability',default='receipts/stability001/STABILITY_DATA.json');p.add_argument('--out',required=True);a=p.parse_args();run(a.stability,a.out)
