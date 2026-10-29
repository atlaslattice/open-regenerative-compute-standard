import argparse,hashlib,json,math,platform
from pathlib import Path
import mpmath as mp
import scipy
from literal_audit import literal_equation2,log_slope
from spectra import density,integral
ROOT=Path(__file__).resolve().parent
PACKAGE='MEASUREMENT_PACKAGE_v3.json'

def calculate():
 d=json.loads((ROOT/PACKAGE).read_text());p={x['label']:x for x in d['table1']};mp.mp.dps=40;checks=[]
 for label,row in p.items():
  for E in [.1,.2,.5,1.,2.,3.,7.5]:
   a,b,c,z=[mp.mpf(str(row[k])) for k in ['p1','p2','p3','p4']];x=mp.mpf(str(E));ref=float((a*x**(b-1)/((1+x)**(b+c)*mp.beta(b,c)))**z);value=literal_equation2(E,row)
   checks.append(dict(label=label,x=E,literal_value=value,mpmath40digit_value=ref,relative_numeric_difference=abs(value/ref-1)))
 left=literal_equation2(3.,p['C\u2009<\u20093 MeV']);right=literal_equation2(3.,p['C\u2009≥\u20093 MeV'])
 # Figure3 graphical envelope is deliberately coarse, not digitized measurements or uncertainty.
 carbon_band=[1.,1.3];Hpeak=(p['H']['p2']-1)/(p['H']['p3']+1)
 reconciliation=dict(status='FAILED_LITERAL_RECONSTRUCTION_NOT_QUALIFIED_FOR_PRODUCTION',assumed_axes='x=ion energy inMeV, y=pit diameter inum, beta=Euler beta as printed; no unreported coordinate transform supplied',
  carbon_at3_left_um=left,carbon_at3_right_um=right,carbon_piecewise_jump_um=abs(left-right),
  figure3_carbon_at3_coarse_visual_envelope_um=carbon_band,envelope_scope='Visually verified PDFpage5 broad graphical envelope; not raw data, statistical uncertainty or refitted calibration',
  literal_values_in_graphical_envelope=carbon_band[0]<=left<=carbon_band[1] and carbon_band[0]<=right<=carbon_band[1],
  He_literal_log_slopes=[log_slope(e,p['He']) for e in [.1,.5,1.,2.,7.5]],He_literal_shape='strictly decreasing for every positive x because p2<1 and p4>0; source Figure3/text show a nonmonotonic He response',
  H_literal_peak_x_MeV=Hpeak,H_peak_text_reference_MeV_approx=[.1,.2],
  resolution='Original source implementation/definitions or corrected numerical prescription required. No guessed parameter swap, fit or normalization correction applied. This is not proof the experiment is wrong.')
 spectra=[]
 for row in d['analytic_spectrum_parameters']:
  kw={k:row[k] for k in ['equation']};kw.update(N0=row['N0_per_sr_J'],kBT=row['kBT_MeV'])
  spectra.append(dict(**row,evaluation_energies_MeV=[.1,.5,1.,2.,5.],analytic_density_per_MeV_sr_J=[density(e,**kw) for e in [.1,.5,1.,2.,5.]],counts_in_explicit_0p1_to10MeV_domain_per_sr_J=integral(.1,10.,**kw),claim='Reproduction of reported analytic parametrization only; query/domain choices do not establish measured energy coverage or Stars source applicability'))
 maxdiff=max(x['relative_numeric_difference'] for x in checks)
 if maxdiff>1e-12:raise ValueError('independent arithmetic check failed')
 return dict(status='SOURCE_PACKAGE_AND_LITERAL_RECONSTRUCTION_AUDIT',numeric_formula_check=dict(points=len(checks),decimal_digits=40,max_relative_difference=maxdiff,passed_arithmetic_gate=True,rows=checks),source_reconciliation=reconciliation,analytic_spectra_replay=spectra,
  benchmark_qualification=dict(ready_for_complete_TPS_reproduction=False,raw_pit_or_image_data_recovered=False,calibrated_filter_transmission_recovered=False,filter_nominal_stack_recovered=True,filter_thickness_covariance_recovered=False,exact_TPS_field_geometry_package_recovered=False,matched_angle_source_map_recovered=False,absolute_flux_agreement_validated=False,source_response_production_approved=False),
  independent_campaign_holdout_run=False,apparatus_prediction=None,net_energy_result=None)

def main():
 a=argparse.ArgumentParser();a.add_argument('--out',type=Path,required=True);a=a.parse_args()
 if a.out.exists():raise FileExistsError('choose new audit output')
 d=calculate();a.out.mkdir(parents=True,exist_ok=False);(a.out/'AUDIT.json').write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
 rec=dict(python=platform.python_version(),scipy=scipy.__version__,mpmath=mp.__version__,package_sha256=hashlib.sha256((ROOT/PACKAGE).read_bytes()).hexdigest(),code_sha256={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['literal_audit.py','spectra.py','run_audit.py','extract_package.py']})
 (a.out/'RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(dict(arithmetic=d['numeric_formula_check']['max_relative_difference'],reconciliation=d['source_reconciliation'],TPS_qualified=False)))
if __name__=='__main__':main()
