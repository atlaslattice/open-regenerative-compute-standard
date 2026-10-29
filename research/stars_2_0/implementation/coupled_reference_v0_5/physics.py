"""Bounded stopping coordinates and conditional first-reaction integration."""
import bisect,importlib.util,json,math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).parent

def load_model():
    spec=importlib.util.spec_from_file_location('forge_stopping_v04',ROOT.parent/'stopping_models_v0_4/model.py')
    model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
    return model,model.load_tables()

class Coordinate:
    """Relative atom-column coordinate, zero at a POSITIVE energy floor, not a full range."""
    def __init__(self,fn,lo,hi,steps=2048):
        if not 0<lo<hi or steps<16:raise ValueError('invalid stopping grid')
        self.e=np.geomspace(lo,hi,steps+1);self.s=np.array([fn(float(e)) for e in self.e])
        if not np.isfinite(self.s).all() or np.any(self.s<=0):raise ValueError('positive stopping required')
        self.r=np.zeros(steps+1)
        for i in range(steps):self.r[i+1]=self.r[i]+self.segment(i,self.e[i+1])
    def segment(self,i,E):
        a,b=self.e[i:i+2];sa,sb=self.s[i:i+2];slope=(sb-sa)/(b-a)
        return 1e6*((E-a)/sa if slope==0 else math.log1p(slope*(E-a)/sa)/slope)
    def coordinate(self,E):
        if not self.e[0]<=E<=self.e[-1]:raise ValueError('STOPPING_ENERGY_COVERAGE_MISSING')
        i=min(bisect.bisect_right(self.e,E)-1,len(self.e)-2)
        return self.r[i]+self.segment(i,E)
    def outgoing(self,E,column):
        if not math.isfinite(column) or column<0:raise ValueError('invalid column')
        if column==0:self.coordinate(E);return E
        r=self.coordinate(E)-column
        if r<0:return None
        i=min(bisect.bisect_right(self.r,r)-1,len(self.r)-2)
        a,b=self.e[i:i+2];sa,sb=self.s[i:i+2];slope=(sb-sa)/(b-a);d=(r-self.r[i])*1e-6
        return float(a+d*sa if slope==0 else a+sa*math.expm1(slope*d)/slope)

def sigma(rows,E):
    e=[float(r['E_lab_MeV']) for r in rows]
    if any(r['observable']!='PUBLICATION_MODEL_EXTRAPOLATED_FUSION_EVENT_CROSS_SECTION' for r in rows):raise ValueError('source observable mismatch')
    if not .22<=E<=e[-1]:raise ValueError('REACTION_ENERGY_COVERAGE_MISSING; narrow low resonance excluded')
    i=min(bisect.bisect_right(e,E)-1,len(e)-2);f=(E-e[i])/(e[i+1]-e[i])
    return rows[i]['sigma_event_b']*(1-f)+rows[i+1]['sigma_event_b']*f

def reactions(coordinate,rows,E,column,boron_fraction,steps):
    if not math.isfinite(column) or column<0 or not 0<boron_fraction<=1:raise ValueError('invalid target column')
    if not isinstance(steps,int) or steps<1:raise ValueError('invalid reaction grid')
    end=coordinate.outgoing(E,column)
    if end is None:raise ValueError('PROTON_STOPPING_COVERAGE_MISSING')
    sigma(rows,E);sigma(rows,end)
    width=column/steps;survival=1.;bins=[];tau_total=0.
    for j in range(steps):
        N=(j+.5)*width;energy=coordinate.outgoing(E,N)
        rate=sigma(rows,energy)*1e-24*boron_fraction;tau=rate*width
        probability=survival*(-math.expm1(-tau))
        bins.append(dict(start_atoms_cm2=j*width,width_atoms_cm2=width,rate_per_atom_column=rate,event_probability=probability))
        survival*=math.exp(-tau);tau_total+=tau
    probability=-math.expm1(-tau_total)
    return dict(probability=probability,optical_depth=tau_total,unreacted_exit_energy_MeV=end,bins=bins)

def sample_depth(result,rng):
    if result['probability']<=0:raise ValueError('no reaction distribution to sample')
    probabilities=np.array([b['event_probability'] for b in result['bins']]);probabilities/=probabilities.sum()
    b=result['bins'][int(rng.choice(len(probabilities),p=probabilities))]
    t=b['rate_per_atom_column']*b['width_atoms_cm2']
    offset=-math.log1p(-rng.random()*(-math.expm1(-t)))/b['rate_per_atom_column']
    return b['start_atoms_cm2']+offset
