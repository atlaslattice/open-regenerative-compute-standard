"""Approximate Goldston/Rutherford trace-ion drag and imposed escape/burn.
Matches WarpX26.10 background_stopping assumptions; no diffusion or confinement
prediction. Energy J, densities m^-3, temperatures eV, time seconds.
"""
import math,sys
from pathlib import Path
import numpy as np
from scipy.constants import e,epsilon_0,m_e,m_u,c
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'kinetic_source_v1_3'))
from analyze import cross_section,thermal_reactivity
MT=3.0160492779*m_u-m_e;MD=2.01410177812*m_u-m_e

def coefficients(ne,Te_eV,ni,Ti_eV):
 if min(ne,ni)<0 or min(Te_eV,Ti_eV)<=0:raise ValueError('invalid density or temperature')
 def L(n,T,m):
  if not n:return 0.
  v=math.sqrt(3*T*e/m);wp=math.sqrt(n*e*e/(epsilon_0*m));value=math.log(12*math.pi*n*(v/wp)**3)
  if value<=0:raise ValueError('weak-coupling assumption failed')
  return value
 Le=L(ne,Te_eV,m_e);Li=L(ni,Ti_eV,MD)
 ae=math.sqrt(2)*ne*e**4*math.sqrt(m_e)*Le/(12*math.pi**1.5*epsilon_0**2*MT*(Te_eV*e)**1.5)
 ai=math.sqrt(2)*ni*e**4*math.sqrt(MT)*Li/(8*math.pi*epsilon_0**2*MD)
 return dict(alpha_e_s=ae,alpha_i_J32_s=ai,log_e=Le,log_i=Li)
def K_to_W(K):return K+K*K/(2*MT*c*c)
def W_to_K(W):return 2*W/(math.sqrt(1+2*W/(MT*c*c))+1)

def rate_table(Ti_eV,order=12):
 nodes,weights=np.polynomial.hermite.hermgauss(order)
 g=np.meshgrid(nodes,nodes,nodes,indexing='ij');ww=np.meshgrid(weights,weights,weights,indexing='ij')
 vD=np.stack([x.ravel() for x in g],axis=1)*math.sqrt(2*Ti_eV*e/MD)
 probs=(ww[0]*ww[1]*ww[2]).ravel()/math.pi**1.5
 energy=np.geomspace(1e3,2e6,240);values=[];mu=MT*MD/(MT+MD)
 for E in energy:
  gamma=1+E*e/(MT*c*c);vT=c*math.sqrt(1-1/gamma**2)
  speed=np.linalg.norm(vD-np.array([0,0,vT]),axis=1)
  values.append(float(np.sum(probs*cross_section(.5*mu*speed**2/(1e3*e),'DT')*speed)))
 return PchipInterpolator(np.log(energy),np.log(values),extrapolate=False)
def rate_from(table,K):
 if not 1e3<=K/e<=2e6:raise ValueError('energy outside rate-table domain')
 return float(np.exp(table(np.log(K/e))))

def candidate(ne=1e20,Te_eV=1e4,nD=1e20,Ti_eV=2e4,tau_fast_s=1.,tau_thermal_s=1.,switch_eV=1e5,K0_eV=1.01e6,rtol=1e-9,order=12):
 if min(tau_fast_s,tau_thermal_s,switch_eV)<=0 or switch_eV>=K0_eV:raise ValueError('invalid residence/transition')
 co=coefficients(ne,Te_eV,nD,Ti_eV);ae=co['alpha_e_s'];ai=co['alpha_i_J32_s']
 if ae+ai==0:raise ValueError('no drag: finite transition absent')
 table=rate_table(Ti_eV,order);W0=K_to_W(K0_eV*e);Ws=K_to_W(switch_eV*e);K0=K0_eV*e
 def rhs(t,y):
  W=max(y[0]*W0,Ws*.9);K=W_to_K(W);dW=-2*ae*W-ai/math.sqrt(W)
  burn=nD*rate_from(table,K);esc=1/tau_fast_s;S=y[1];dK=dW/math.sqrt(1+2*W/(MT*c*c))
  return [dW/W0,-(burn+esc)*S,burn*S,esc*S,-dK*S/K0,burn*S*K/K0,esc*S*K/K0]
 def stop(t,y):return y[0]-Ws/W0
 stop.terminal=True;stop.direction=-1
 tmax=20/max(2*ae,ai/W0**1.5,1e-12)
 sol=solve_ivp(rhs,[0,tmax],[1,1,0,0,0,0,0],method='DOP853',events=stop,rtol=rtol,atol=rtol*1e-3,max_step=tmax/100,dense_output=True)
 if not len(sol.t_events[0]):raise ValueError('transition not reached')
 z=sol.y[:,-1];survive=float(z[1]);thermal_rate=nD*thermal_reactivity(Ti_eV/1000,'DT');fb=thermal_rate/(thermal_rate+1/tau_thermal_s)
 result=dict(**co,ne_m3=ne,nD_m3=nD,Te_eV=Te_eV,Ti_eV=Ti_eV,tau_fast_s=tau_fast_s,tau_thermal_s=tau_thermal_s,switch_eV=switch_eV,K0_eV=K0_eV,
  time_to_switch_s=float(sol.t[-1]),p_fast_burn=float(z[2]),p_fast_escape=float(z[3]),p_to_thermal=survive,thermal_burn_conditional=float(fb),
  p_total_burn=float(z[2]+survive*fb),p_total_escape=float(z[3]+survive*(1-fb)),probability_residual=float(1-z[2]-z[3]-survive),
  fast_kinetic_partition_residual_eV=float(K0_eV*(1-z[4]-z[5]-z[6])-switch_eV*survive),background_drag_eV=float(z[4]*K0_eV),fast_burn_carried_eV=float(z[5]*K0_eV),fast_escape_carried_eV=float(z[6]*K0_eV),
  surviving_transition_eV=switch_eV*survive,assumed_thermalization_gap_to_background_eV=survive*max(0,switch_eV-1.5*Ti_eV),thermal_reaction_rate_s=float(thermal_rate),physical_validation=False,
  label='POTENTIAL-DERIVED; approximate drag and imposed uncalibrated escape/thermal transition')
 return result,sol
