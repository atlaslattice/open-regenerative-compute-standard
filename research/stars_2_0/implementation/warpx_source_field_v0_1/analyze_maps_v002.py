"""Source-unit controls and physical scale checks; no calibrated capture claim."""
import json,math
from pathlib import Path
import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.constants import m_p,c,e
root=Path(__file__).resolve().parent
field=np.load(root/'maps/FIELD_ARRAYS.npz');axes=[field['offset'][j]+np.arange(47)*field['spacing'][j] for j in range(3)]
interpolators=[RegularGridInterpolator(axes,field['B'+k],bounds_error=True) for k in 'xyz']
B=np.array([float(f(np.array([[0,.2,2.5]]))[0]) for f in interpolators]);Bnorm=float(np.linalg.norm(B))
rows=[]
for case in json.loads((root/'receipts/MAP_RUNS.json').read_text()):
 run=root/'receipts'/case['case'];numbers=np.loadtxt(run/'diags/reducedfiles/number.txt');a=np.loadtxt(run/'diags/reducedfiles/extrema.txt');active=numbers[:,4]>0;a=a[active]
 mom=a[:,[8,10,12]];p2=np.sum(mom*mom,axis=1);K=p2/(np.sqrt(m_p*m_p+p2/c**2)+m_p)
 p0=m_p*c*np.array(case['normalized_u']);perp=p0-np.dot(p0,B)*B/(Bnorm*Bnorm);rho=float(np.linalg.norm(perp)/(e*Bnorm))
 firstlost=np.where(numbers[:,4]==0)[0]
 bracket=None if not len(firstlost) else [float(numbers[firstlost[0]-1,1]),float(numbers[firstlost[0],1])]
 rows.append(dict(case=case['case'],source_grade=case['source_evidence'],final_physical_weight=float(numbers[-1,4]),axial_z_momentum_reversed=bool(np.any(mom[:,2]<0)),loss_time_bracket_s=bracket,final_or_last_active_position_m=a[-1,[2,4,6]].tolist(),relative_K_drift=float(max(abs(K/K[0]-1))),initial_B_magnitude_T=Bnorm if case['map'] else 0,local_initial_gyroradius_estimate_m=rho if case['map'] else None,local_gyroradius_over_domain_halfwidth=rho/case['scale_m_per_source_length'] if case['map'] else None,classification='FINITE_TIME_NUMERICAL_MAP_CONTROL_NOT_APPARATUS_CAPTURE_FRACTION'))
lookup={r['case']:r for r in rows}
checks=[]
def add(name,value):checks.append(dict(name=name,passed=bool(value)))
a=root/'receipts/original_low/diags/reducedfiles/extrema.txt';b=root/'receipts/metadata_only_negative_control/diags/reducedfiles/extrema.txt'
add('metadata_only_control_trace_byte_identical_to_original',a.read_bytes()==b.read_bytes())
add('original_metre_scale_low_energy_reflects',lookup['original_low']['axial_z_momentum_reversed'] and lookup['original_low']['final_physical_weight']==1)
add('no_B_control_escapes',lookup['original_no_B']['final_physical_weight']==0)
for name in ['canonical_mm_low','canonical_mm_low_half_dt','original_675keV','canonical_mm_675keV']:
 add(name+'_escapes',lookup[name]['final_physical_weight']==0)
for r in rows:add(r['case']+'_magnetic_no_work',r['relative_K_drift']<1e-10)
coarse=lookup['canonical_mm_low']['loss_time_bracket_s'];fine=lookup['canonical_mm_low_half_dt']['loss_time_bracket_s']
add('low_mm_escape_time_brackets_overlap_on_halving_dt',max(coarse[0],fine[0])<=min(coarse[1],fine[1]))
out={'status':'SOURCE_DERIVED_NUMERICAL_CONTROLS','results':rows,'checks':checks,'source_unit_interpretation':'Original file gridUnitSI=1 and numbers match FEM millimetres. Millimetre branch is separately derived, not an author-confirmed correction.','loader_scope':'Inspected WarpX26.10 ExternalFieldReader uses raw gridSpacing/offset. Negative control confirms metadata-only spatial unit change is ineffective in this tested path. Canonical explicit SI coordinates required.'}
with (root/'receipts/MAP_ANALYSIS_v002.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2));assert all(x['passed'] for x in checks)
