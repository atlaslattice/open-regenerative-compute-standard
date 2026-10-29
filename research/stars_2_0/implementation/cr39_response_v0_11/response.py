"""Condition-specific, digitized reference response; no universal CR39 calibration."""
import hashlib,json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
REQUIRED_CONDITIONS=dict(species='alpha',detector='TASTRAK',etchant='NaOH',concentration_mol_L=6.25,temperature_C=98.,etch_time_hours=1.)

FIXTURE_SHA256='8c5112d0c087afc96f12dd56e115f0d8a53cb0a38ea1eafbc79344930d3621d3'

class ReferenceResponse:
 def __init__(self):
  raw=(ROOT/'ZHANG2019_DIGITIZED.json').read_bytes()
  if hashlib.sha256(raw).hexdigest()!=FIXTURE_SHA256:raise ValueError('reference fixture identity mismatch')
  self.data=json.loads(raw)
  self.rows=self.data['mean_response_rows'];self.e=np.array([r['E_alpha_MeV'] for r in self.rows]);self.d=np.array([r['mean_track_diameter_um'] for r in self.rows]);self.s=np.array([r['reported_core_spread_um'] for r in self.rows])
  if len(self.e)<2 or not np.isfinite(self.e).all() or not np.isfinite(self.d).all() or np.any(np.diff(self.e)<=0):raise ValueError('invalid reference grid')
 def check(self,conditions):
  if conditions!=REQUIRED_CONDITIONS:raise ValueError('species/detector/etch conditions differ from recovered reference; transfer is unqualified')
 def mean(self,energy_MeV,*,conditions):
  self.check(conditions)
  if isinstance(energy_MeV,bool) or not isinstance(energy_MeV,(int,float)) or not math.isfinite(energy_MeV) or energy_MeV<=0:raise ValueError('positive finite alpha energy required')
  if not self.e[0]<=energy_MeV<=self.e[-1]:return dict(status='UNCOVERED',energy_MeV=energy_MeV,mean_diameter_um=None,full_response=None,coverage_MeV=[float(self.e[0]),float(self.e[-1])])
  direct=bool(np.any(np.isclose(self.e,energy_MeV,rtol=0,atol=1e-12)))
  return dict(status='DIGITIZED_REFERENCE_POINT' if direct else 'INTERPOLATED_REFERENCE_MEAN_NOT_INDEPENDENT_CALIBRATION',energy_MeV=energy_MeV,mean_diameter_um=float(np.interp(energy_MeV,self.e,self.d)),reported_or_interpolated_core_spread_um=float(np.interp(energy_MeV,self.e,self.s)),mean_digitization_allowance_um=.06,calibration_mean_uncertainty_um=None,full_response=None,spread_scope='reported core fit width, not mean uncertainty or assumed full Gaussian response')
 def energy_candidates(self,diameter_um,*,conditions):
  self.check(conditions)
  if not math.isfinite(diameter_um) or diameter_um<=0:raise ValueError('positive finite diameter required')
  candidates=[]
  for x1,x2,y1,y2 in zip(self.e[:-1],self.e[1:],self.d[:-1],self.d[1:]):
   if min(y1,y2)<=diameter_um<=max(y1,y2):
    if y1==y2:raise ValueError('flat interval gives a continuum of candidates')
    value=float(x1+(diameter_um-y1)/(y2-y1)*(x2-x1))
    if not any(abs(value-v)<1e-10 for v in candidates):candidates.append(value)
  return dict(status='MULTIPLE_ENERGY_CANDIDATES' if len(candidates)>1 else 'REFERENCE_CANDIDATE_ONLY' if candidates else 'UNCOVERED',energy_candidates_MeV=sorted(candidates),scope='piecewise-linear mean inverse only; no unique spectrum reconstruction, probability or uncertainty inferred')
 def fold_registered_display_subset(self,energy_MeV,registered_tracks,*,conditions):
  self.check(conditions)
  if isinstance(registered_tracks,bool) or not isinstance(registered_tracks,int) or registered_tracks<0:raise ValueError('known nonnegative registered-subset count required, not incident alpha count')
  if isinstance(energy_MeV,bool) or not math.isfinite(energy_MeV) or energy_MeV<=0:raise ValueError('positive finite alpha energy required')
  if not math.isclose(energy_MeV,4.42,abs_tol=1e-12,rel_tol=0):return dict(status='FULL_RESPONSE_UNAVAILABLE_AT_THIS_ENERGY',expected_display_counts=None)
  h=self.data['figure4'];p=np.array(h['conditional_display_probabilities'])
  return dict(status='CONDITIONAL_DIGITIZED_DISPLAY_REFERENCE_ONLY',edges_um=h['display_subset_edges_um'],expected_display_counts=(registered_tracks*p).tolist(),registered_display_subset_tracks=registered_tracks,absolute_efficiency=None,missed_tracks=None,scope=h['scope'])
