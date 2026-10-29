import argparse,hashlib,json,platform
from pathlib import Path
import numpy as np
import PIL
from response import ReferenceResponse,REQUIRED_CONDITIONS
ROOT=Path(__file__).resolve().parent

def calculate():
 r=ReferenceResponse();queries=[r.mean(e,conditions=REQUIRED_CONDITIONS) for e in [3.3,3.9,7.5]];held=[]
 for j in range(1,len(r.e)-1):
  keep=np.arange(len(r.e))!=j;pred=float(np.interp(r.e[j],r.e[keep],r.d[keep]));held.append(dict(held_out_energy_MeV=float(r.e[j]),digitized_reference_mean_um=float(r.d[j]),interpolated_prediction_um=pred,signed_residual_um=pred-r.d[j]))
 h=r.data['figure4'];stats=h['source_statistics'];row=next(x for x in r.rows if x['E_alpha_MeV']==4.42)
 total=h['digitized_display_total'];allowance=h['per_bin_count_digitization_allowance'];low=sum(max(0,x-allowance) for x in h['digitized_display_counts']);high=sum(x+allowance for x in h['digitized_display_counts'])
 return dict(status='PUBLISHED_REFERENCE_DIGITIZATION_AND_RESPONSE_CHECKS_ONLY',conditions=REQUIRED_CONDITIONS,energy_queries=queries,
  figure4_source_anchor_comparison=dict(mean_4p42_diameter_difference_um=row['mean_track_diameter_um']-stats['gaussian_fit_mean_um'],core_sigma_difference_um=row['reported_core_spread_um']-stats['gaussian_fit_sigma_um'],
   source_entries=stats['entries'],digitized_display_subset_total=total,count_digitization_bounds_only=[low,high],
   raw_standard_deviation_source_um=stats['raw_standard_deviation_um'],digitized_display_subset_standard_deviation_um=h['digitized_display_standard_deviation_um'],
   standard_deviation_relative_difference=h['digitized_display_standard_deviation_um']/stats['raw_standard_deviation_um']-1,source_gaussian_chi_squared_per_ndf=stats['chi_squared']/stats['degrees_of_freedom'],
   interpretation='Figure10 core summaries agree with printed Figure4 fit within digitization allowance. Histogram reconstruction is approximate; display subset moments do not exactly match original raw statistics. No full Gaussian response accepted.'),
  leave_one_out_interpolation=held,leave_one_out_RMS_um=float(np.sqrt(np.mean([x['signed_residual_um']**2 for x in held]))),
  validation_scope='Retrospective same-campaign interpolation sensitivity, not independent experimental validation; endpoints omitted because extrapolation is prohibited',
  ambiguous_inverse=r.energy_candidates(13.,conditions=REQUIRED_CONDITIONS),
  conditional_monoenergetic_display=r.fold_registered_display_subset(4.42,1,conditions=REQUIRED_CONDITIONS),
  source_zheng2026=dict(numeric_model_recovered=False,coefficient_values=None,source_claimed_alpha_energy_range_MeV=[.5,6.],requested_7p5MeV_status='UNCOVERED',transfer_from_2019=False),
  calibrated_for_Stars=False,measured_alpha_efficiency=None,full_TPS_chain_reproduced=False,net_energy_result=None)

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError('choose a new output directory')
 result=calculate();a.out.mkdir(parents=True,exist_ok=False);(a.out/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 receipt=dict(python=platform.python_version(),numpy=np.__version__,pillow=PIL.__version__,code_sha256={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['response.py','run_reference.py','digitize.py']},fixture_sha256=hashlib.sha256((ROOT/'ZHANG2019_DIGITIZED.json').read_bytes()).hexdigest())
 (a.out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(dict(energy_queries=result['energy_queries'],interpolation_RMS_um=result['leave_one_out_RMS_um'],histogram_sd_relative_difference=result['figure4_source_anchor_comparison']['standard_deviation_relative_difference'])))
if __name__=='__main__':main()
