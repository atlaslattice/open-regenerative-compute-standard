"""Coherent basis kernel and conditional-event categorical likelihood.
No default detector response, no experimental calibration claim.
"""
import math
import numpy as np

def validate_kernel(kernel):
    x=np.asarray(kernel,float)
    if x.ndim!=2 or x.shape[1]!=4 or not np.isfinite(x).all() or np.any(x[:,:2]<0):raise ValueError('finite positive basis kernel required')
    if np.any(x[:,2]**2+x[:,3]**2>x[:,0]*x[:,1]+1e-12*np.maximum(x[:,0]*x[:,1],1e-300)):raise ValueError('non-positive coherent Gram matrix')
    return x

def kernel_from_amplitudes(a):
    a=np.asarray(a,complex)
    if a.ndim!=3 or a.shape[1:]!=(2,5) or not np.isfinite(a).all():raise ValueError('N x2 x5 finite amplitudes required')
    b=np.sum(np.conj(a[:,0])*a[:,1],axis=1)/5
    return np.column_stack([np.sum(abs(a[:,0])**2,axis=1)/5,np.sum(abs(a[:,1])**2,axis=1)/5,b.real,b.imag])

def weights_and_derivatives(kernel,k,delta):
    x=validate_kernel(kernel)
    if isinstance(k,bool) or not math.isfinite(k) or not 0<k<1 or not math.isfinite(delta):raise ValueError('interior k and finite phase required for differentiable fit')
    t=math.sqrt(k*(1-k));u=x[:,2]*math.cos(delta)-x[:,3]*math.sin(delta)
    w=k*x[:,0]+(1-k)*x[:,1]+2*t*u
    # Tiny negative cancellation is a numerical failure, not silently clipped.
    if np.any(w<0) or not np.isfinite(w).all():raise ValueError('negative or invalid intensity')
    d=np.column_stack([x[:,0]-x[:,1]+(1-2*k)/t*u,2*t*(-x[:,2]*math.sin(delta)-x[:,3]*math.cos(delta))])
    return w,d

def distribution(kernel,k,delta):
    w,d=weights_and_derivatives(kernel,k,delta);z=float(w.sum())
    if not math.isfinite(z) or z<=0:raise ValueError('positive total required')
    p=w/z;dp=(d-p[:,None]*d.sum(axis=0))/z
    return p,dp

def fisher(kernel,k,delta):
    p,d=distribution(kernel,k,delta);ok=p>0
    if np.any(np.abs(d[~ok])>1e-13):raise ValueError('singular changing support')
    return (d[ok].T/p[ok])@d[ok]

def fold(kernel,response,*,append_missed):
    """Columns are true bins, rows observed bins. Explicitly choose missed bin.
    Response is supplied, never synthesized here. It must be parameter independent.
    """
    x=validate_kernel(kernel);R=np.asarray(response,float)
    if not isinstance(append_missed,bool) or R.ndim!=2 or R.shape[1]!=len(x) or not np.isfinite(R).all() or np.any(R<0) or np.any(R.sum(axis=0)>1):raise ValueError('substochastic response and explicit missed-bin policy required')
    if append_missed:R=np.vstack([R,1-R.sum(axis=0)])
    return validate_kernel(R@x)

def multinomial_nll(kernel,k,delta,counts):
    p,_=distribution(kernel,k,delta);n=np.asarray(counts)
    if n.shape!=p.shape or n.dtype.kind not in 'iu' or np.any(n<0):raise ValueError('nonnegative integer event counts required')
    if np.any((p==0)&(n>0)):return math.inf
    positive=n>0
    return float(-np.sum(n[positive]*np.log(p[positive])))

def basis_rescale(kernel,scales):
    s=np.asarray(scales,float)
    if s.shape!=(2,) or not np.isfinite(s).all() or np.any(s<=0):raise ValueError('positive explicit basis scales required')
    return validate_kernel(validate_kernel(kernel)*np.array([s[0]**2,s[1]**2,s.prod(),s.prod()]))

def rescaled_k(k,scales):
    a,b=scales
    if not 0<k<1 or not a>0 or not b>0:raise ValueError('positive scales and interior k required')
    x=k/a**2;y=(1-k)/b**2
    return x/(x+y)
