"""Cold infinite-plane alpha transport with explicit unresolved low-energy tails."""
import math
import numpy as np

def rotation_to(axis):
 u=np.asarray(axis,float)
 if u.shape!=(3,) or not np.isfinite(u).all() or abs(float(u@u)-1)>1e-10:raise ValueError('finite unit beam axis required')
 ref=np.array([0.,0.,1.]) if abs(u[2])<.9 else np.array([1.,0.,0.])
 x=np.cross(ref,u);x/=np.linalg.norm(x);y=np.cross(u,x)
 R=np.column_stack([x,y,u])
 if abs(np.linalg.det(R)-1)>1e-12:raise ValueError('improper event rotation')
 return R

def propagate(E,mu,depth,total,coordinate):
 for x in [E,mu,depth,total]:
  if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite scalar required')
 if E<0 or abs(mu)>1+1e-12 or not 0<=depth<=total:raise ValueError('invalid energy/direction/column')
 face='REAR' if mu>=0 else 'FRONT'
 if total==0:return dict(status='VACUUM_POST_BIRTH_CONTROL',face=face,escaped_E=E,material_lower=0.,unresolved_E=0.,path_atoms_cm2=0.)
 if abs(mu)<1e-12:return dict(status='UNRESOLVED_GRAZING',face=None,escaped_E=None,material_lower=0.,unresolved_E=E,path_atoms_cm2=None)
 path=(total-depth)/mu if mu>0 else depth/abs(mu)
 floor=float(coordinate.e[0])
 if E<floor:return dict(status='BIRTH_BELOW_STOPPING_FLOOR',face=None,escaped_E=None,material_lower=0.,unresolved_E=E,path_atoms_cm2=path)
 result=coordinate.outgoing(E,path)
 if result is None:return dict(status='TAIL_BELOW_POSITIVE_STOPPING_FLOOR',face=None,escaped_E=None,material_lower=E-floor,unresolved_E=floor,path_atoms_cm2=path)
 return dict(status='MODEL_INTERVAL_ESCAPE',face=face,escaped_E=result,material_lower=E-result,unresolved_E=0.,path_atoms_cm2=path)
