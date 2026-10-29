"""Replay explicitly reported analytic source forms; no new experimental source fit."""
import math
from scipy.special import exp1

def density(E,*,equation,N0,kBT):
 if not all(math.isfinite(x) and x>0 for x in [E,N0,kBT]):raise ValueError('positive finite energy and source parameters required')
 if equation==3:return N0/E*math.exp(-E/kBT)
 if equation==4:return N0/math.sqrt(2*E*kBT)*math.exp(-math.sqrt(2*E/kBT))
 raise ValueError('only explicit publication forms3 and4 are supported')

def integral(Emin,Emax,*,equation,N0,kBT):
 if not all(math.isfinite(x) and x>0 for x in [N0,kBT]) or not math.isfinite(Emin) or Emin<0 or math.isnan(Emax) or Emax<=Emin:raise ValueError('explicit ordered integration domain and positive parameters required')
 if equation==3:
  if Emin==0:raise ValueError('Eq3 count diverges as lower bound tends to0; explicit positive cutoff required')
  return float(N0*(exp1(Emin/kBT)-exp1(Emax/kBT)))
 if equation==4:return N0*(math.exp(-math.sqrt(2*Emin/kBT))-math.exp(-math.sqrt(2*Emax/kBT)))
 raise ValueError('only explicit publication forms3 and4 are supported')
