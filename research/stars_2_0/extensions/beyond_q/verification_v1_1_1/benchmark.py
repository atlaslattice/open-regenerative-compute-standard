"""Independent linear implementation of pinned TMAP8 Meschini fixture.

Upstream equations/parameters: upstream/fuel_cycle.i (LGPL-2.1 source).
This reimplementation is distributed under LGPL-2.1; see upstream/LICENSE.
Not a new reactor physics model, nor independent experimental validation.
"""
from pathlib import Path
import math
import numpy as np
from scipy.linalg import expm

ROOT=Path(__file__).resolve().parent
NAMES=['T_01_BZ','T_02_TES','T_03_FW','T_04_DIV','T_05_HX','T_06_DS',
       'T_07_vacuum','T_08_FCU','T_09_ISS','T_10_storage','T_11_membrane']

def system():
    tau=np.array([4500,86400,1000,1000,1000,3600,600,585,22815,np.inf,100.])
    eps=np.array([1e-4,1e-4,0,0,1e-4,1e-4,1e-4,1e-4,1e-4,0,1e-4])
    lam=math.log(2)/388800000.
    matrix=np.diag(-(1+eps)/tau-lam)
    # Explicit directed fractions, donor outflow included once in diagonal.
    for donor,recipient,fraction in [(0,1,1),(1,4,.3),(1,10,.7),(2,0,1),
         (3,0,1),(4,0,.33),(4,2,.33),(4,3,.3399),(4,5,.0001),
         (5,8,1),(6,7,.5),(6,9,.5),(7,8,1),(8,5,.1),(8,9,.9),(10,9,1)]:
        matrix[recipient,donor]+=fraction/tau[donor]
    burn=8.99e-7;feed=burn/.025
    source=np.zeros(11);source[0]=1.067*burn
    source[2]=source[3]=.0001*feed
    source[6]=(1-.025-.0002)*feed;source[9]=-feed
    return matrix,source,lam,eps/tau

def activity(t):
    return .75 if t>17000 else float(t%1800<1350)

def reproduce():
    gold=np.genfromtxt(ROOT/'upstream/gold.csv',delimiter=',',names=True)
    m,s,_,_=system();x=np.zeros(11);x[9]=1.14;rows=[x.copy()]
    for left,right in zip(gold['time'][:-1],gold['time'][1:]):
        h=right-left
        # Upstream FunctionValuePostprocessor executes INITIAL/TIMESTEP_END:
        # source evaluated at preceding accepted time, not new endpoint.
        x=np.linalg.solve(np.eye(11)-h*m,x+h*s*activity(left));rows.append(x.copy())
    reference=np.column_stack([gold[k] for k in NAMES]);actual=np.array(rows)
    error=actual-reference
    return gold,actual,dict(max_abs_error_kg=float(np.max(abs(error))),
        rmse_kg=float(np.sqrt(np.mean(error**2))),
        per_stock_max_error_kg={k:float(np.max(abs(error[:,i]))) for i,k in enumerate(NAMES)},
        method='Backward Euler at published timestamps, lagged forcing',
        physical_validation=False)

def exact_at(times):
    """Continuous-time matrix-exponential oracle, split at every source jump."""
    m,s,_,_=system();aug=np.zeros((12,12));aug[:11,:11]=m;aug[:11,11]=s
    x=np.zeros(12);x[9]=1.14;x[11]=1
    transitions={0.,17000.}
    for t in range(0,18000,1800):transitions.update([float(t),float(t+1350)])
    events=sorted(set(map(float,times))|{t for t in transitions if t<=max(times)})
    lookup={0.:x[:11].copy()};left=0.
    cache={}
    for right in events:
        if right<=left:continue
        a=activity((left+right)/2);h=right-left
        key=(h,a)
        if key not in cache:
            mat=aug.copy();mat[:11,11]*=a;cache[key]=expm(mat*h)
        x=cache[key]@x;lookup[right]=x[:11].copy();left=right
    return np.array([lookup[float(t)] for t in times])

if __name__=='__main__':print(reproduce()[2])
