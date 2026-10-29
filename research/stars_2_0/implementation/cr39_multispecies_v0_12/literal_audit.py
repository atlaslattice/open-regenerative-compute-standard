"""Quarantined literal publication formula. Never a production detector response."""
import math

def literal_equation2(x,p):
 if isinstance(x,bool) or not math.isfinite(x) or x<=0:raise ValueError('positive finite literal x required')
 a,b,c,d=[p[k] for k in ['p1','p2','p3','p4']]
 if min(a,b,c,d)<=0:raise ValueError('positive publication coefficients required')
 return math.exp(d*(math.log(a)+(b-1)*math.log(x)-(b+c)*math.log1p(x)-math.lgamma(b)-math.lgamma(c)+math.lgamma(b+c)))

def log_slope(x,p):return p['p4']*((p['p2']-1)-(p['p2']+p['p3'])*x/(1+x))

def apparatus_response(*args,**kwargs):raise ValueError('UNQUALIFIED: literal equation/table does not reproduce source curve; production response blocked')
