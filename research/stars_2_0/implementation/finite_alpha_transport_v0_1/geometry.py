"""Straight-ray convex-box transport in uniform material column coordinates.
Coordinates have units atoms/cm2 = uniform number density times physical distance.
This scaling does not supply an unknown material number density or SI geometry.
"""
import math
import numpy as np

def vector(x,name):
 a=np.asarray(x,dtype=float)
 if a.shape!=(3,) or not np.isfinite(a).all():raise ValueError('finite 3-vector required: '+name)
 return a

def exit_box(position,direction,lower,upper):
 p=vector(position,'position');u=vector(direction,'direction');lo=vector(lower,'lower');hi=vector(upper,'upper')
 if np.any(hi<=lo) or abs(float(u@u)-1)>1e-10:raise ValueError('positive box and unit direction required')
 # No clamping, entry projection or dropping out-of-target births.
 if np.any(p<lo) or np.any(p>hi):raise ValueError('birth outside target')
 candidates=[]
 for axis in range(3):
  if u[axis]>0:candidates.append(((hi[axis]-p[axis])/u[axis],axis,1))
  elif u[axis]<0:candidates.append(((lo[axis]-p[axis])/u[axis],axis,-1))
 distance=min(x[0] for x in candidates)
 # Preserve all faces at an exact/numerically indistinguishable edge or corner.
 tol=64*np.finfo(float).eps*max(float(np.max(hi-lo)),abs(distance),np.finfo(float).tiny)
 faces=[('XYZ'[axis]+('+' if sign>0 else '-')) for d,axis,sign in candidates if abs(d-distance)<=tol]
 point=p+distance*u
 if np.any(point<lo-tol) or np.any(point>hi+tol):raise ArithmeticError('exit outside box')
 return {'path_column_atoms_cm2':float(distance),'exit_column_position_atoms_cm2':point.tolist(),'faces':faces}

def energy_through_column(E,path,coordinate):
 for value in [E,path]:
  if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:raise ValueError('nonnegative finite energy/path required')
 if path==0:return dict(status='ZERO_MATERIAL_PATH',escaped_E=E,material_lower=0.,unresolved_E=0.)
 floor=float(coordinate.e[0])
 if E<floor:return dict(status='BIRTH_BELOW_MODEL_FLOOR',escaped_E=None,material_lower=0.,unresolved_E=E)
 residual=coordinate.outgoing(E,path)
 if residual is None:return dict(status='UNRESOLVED_LOW_ENERGY_TAIL',escaped_E=None,material_lower=E-floor,unresolved_E=floor)
 return dict(status='MODEL_INTERVAL_ESCAPE',escaped_E=residual,material_lower=E-residual,unresolved_E=0.)

def apparatus_gate(profile):
 required=['target_form','composition','number_density_atoms_cm3','physical_boundary_m','support_geometry_and_composition','incident_beam_position_distribution','birth_space_time_adapter']
 missing=[key for key in required if profile.get(key) is None]
 if missing:return {'status':'BLOCKED_MISSING_APPARATUS_INPUTS','missing':missing,'net_electricity_J':None}
 # Presence is insufficient: finite_box_control is the only implemented lane.
 return {'status':'REQUIRES_QUALIFIED_APPARATUS_ADAPTER','missing':[],'net_electricity_J':None}
