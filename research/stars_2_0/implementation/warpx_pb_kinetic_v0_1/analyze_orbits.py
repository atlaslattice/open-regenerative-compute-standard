"""Independent relativistic Lorentz ODE and observable comparisons, not apparatus validation."""
import json,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.constants import c,m_p,e
ROOT=Path(__file__).resolve().parent
cases=json.loads((ROOT/'ORBIT_CASES_v002.json').read_text())
results=[]
for case in cases:
 name=case['case'];run=ROOT/'receipts'/(name+'002')
 tr=np.loadtxt(run/'diags/reducedfiles/extrema.txt');counts=np.loadtxt(run/'diags/reducedfiles/number.txt')
 # Empty-species extrema are sentinels, not positions: only use samples with positive weight.
 active=counts[:,4]>0
 tr=tr[active];ts=tr[:,1]
 g=1+case['initial_kinetic_energy_eV']*e/(m_p*c*c)
 u=c*math.sqrt((g-1)*(g+1));angle=math.radians(case['pitch_deg'])
 y0=np.array([0.,0.,0.,u*math.sin(angle),0.,u*math.cos(angle)])
 B0=case['B0_T'];a=case['quadratic_coefficient_m2']
 def rhs(t,y):
  x,ypos,z=y[:3];uv=y[3:];gamma=math.sqrt(1+np.dot(uv,uv)/c**2);v=uv/gamma
  B=np.array([-B0*a*x*z,-B0*a*ypos*z,B0*(1+a*z*z)])
  return np.r_[v,e/m_p*np.cross(v,B)]
 ref=solve_ivp(rhs,(0,float(ts[-1])),y0,method='DOP853',rtol=2e-12,atol=1e-12,dense_output=True,max_step=1e-9)
 assert ref.success
 exact=ref.sol(ts)
 pos=tr[:,[2,4,6]];mom=tr[:,[8,10,12]]
 pp=m_p*exact[3:].T
 position_error=np.linalg.norm(pos-exact[:3].T,axis=1)
 momentum_rel=np.linalg.norm(mom-pp,axis=1)/np.linalg.norm(y0[3:]*m_p)
 psq=np.sum(mom*mom,axis=1)
 # Rationalized kinetic-energy formula avoids subtracting two rest-energy-sized quantities.
 kval=psq/(np.sqrt(m_p*m_p+psq/c**2)+m_p)
 drift=float(np.max(abs(kval/kval[0]-1)))
 B=np.column_stack([-B0*a*pos[:,0]*pos[:,2],-B0*a*pos[:,1]*pos[:,2],B0*(1+a*pos[:,2]**2)])
 normB=np.linalg.norm(B,axis=1);par=np.sum(mom*B,axis=1)/normB
 mu=(psq-par*par)/(2*m_p*normB)
 reflected=bool(np.any(par<0))
 escaped=bool(counts[-1,4]==0)
 zeroz=np.where(mom[:-1,2]*mom[1:,2]<0)[0]
 turn=None
 if len(zeroz):
  i=zeroz[0];fraction=mom[i,2]/(mom[i,2]-mom[i+1,2]);turn=float(pos[i,2]+fraction*(pos[i+1,2]-pos[i,2]))
 result=dict(case=name,active_diagnostic_samples=len(ts),final_weight=float(counts[-1,4]),escaped=escaped,parallel_momentum_reversed=reflected,first_turn_z_m=turn,max_abs_z_m=float(np.max(abs(pos[:,2]))),kinetic_energy_relative_drift=drift,max_position_error_vs_independent_ODE_m=float(max(position_error)),max_relative_momentum_error_vs_independent_ODE=float(max(momentum_rel)),mu_relative_range=float(np.ptp(mu)/mu[0]),dt_s=case['dt_s'],last_active_time_s=float(ts[-1]),end_time_s=float(counts[-1,1]),reference_ODE_rtol=2e-12)
 if a==0:
  omega=e*B0/(g*m_p);theory=np.column_stack([m_p*y0[3]*np.cos(omega*ts),-m_p*y0[3]*np.sin(omega*ts),np.full(len(ts),m_p*y0[5])])
  result['max_relative_momentum_error_vs_analytic_helix']=float(max(np.linalg.norm(mom-theory,axis=1)/np.linalg.norm(y0[3:]*m_p)))
 else:
  result['adiabatic_pitch_threshold_deg']=math.degrees(math.asin(1/math.sqrt(5)))
  result['adiabatic_guide_first_turn_z_m']=None if angle<math.asin(1/math.sqrt(5)) else math.sqrt((1/math.sin(angle)**2-1)/a)
 results.append(result)
# Predeclared numerical tolerance scales, not measurement uncertainty or model accuracy.
checks=[]
for r in results:
 checks.append((r['case']+'_magnetic_no_work',r['kinetic_energy_relative_drift']<2e-10))
 checks.append((r['case']+'_lorentz_agreement',r['max_relative_momentum_error_vs_independent_ODE']<.02))
lookup={r['case']:r for r in results}
for stem in ['uniform','mirror_reflect']:
 lo,hi=(lookup['uniform_dt'],lookup['uniform_half_dt']) if stem=='uniform' else (lookup['mirror_reflect'],lookup['mirror_reflect_half_dt'])
 checks.append((stem+'_halving_dt_reduces_momentum_error',hi['max_relative_momentum_error_vs_independent_ODE']<lo['max_relative_momentum_error_vs_independent_ODE']))
checks.extend([('losscone_escapes',lookup['mirror_losscone']['escaped']),('outside_losscone_reflects',lookup['mirror_reflect']['parallel_momentum_reversed'] and not lookup['mirror_reflect']['escaped'])])
out={'status':'NUMERICAL_FIELD_FIXTURES_ONLY','results':results,'checks':[dict(name=n,passed=bool(v)) for n,v in checks]}
path=ROOT/'receipts'/'ORBIT_ANALYSIS001.json'
with path.open('x') as f:json.dump(out,f,indent=2,allow_nan=False);f.write('\n')
print(json.dumps(out,indent=2))
assert all(v for _,v in checks)
