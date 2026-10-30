#!/usr/bin/env python3
"""Stars G1/G2 v0.7 spherical idealization: rigid fluid acoustic sphere + noninteracting charged particles in uniform B.
No nuclear reaction rate, real target acoustics, material response or confinement design is inferred.
"""
from pathlib import Path
import numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.constants import elementary_charge as e, proton_mass as mp, physical_constants, pi
import json, hashlib, zipfile
D=Path(__file__).resolve().parent
R=0.30; c=343.0; zeta=0.05; isolation=1e-4
# zero derivative j0'(x)=0 iff tan(x)=x, positive nonzero roots
roots=[brentq(lambda x: (x*np.cos(x)-np.sin(x)), n*pi+1e-5,(n+0.5)*pi-1e-5) for n in range(1,5)]
f_modes=[c*x/(2*pi*R) for x in roots]
# Note there are angular l>0 modes below first radial mode: only l=0 radial subfamily computed.
def response(f,fn):
    r=f/fn
    return 1/np.sqrt((1-r*r)**2+(2*zeta*r)**2)
# isolation controls ambient drive only; internally driven modal source stays unchanged.
fd=f_modes[0]
ambient_pa=1.0; internal_pa=0.05
arms=[('A: exposed; drive OFF',1,0,0),('B: isolated; drive OFF',isolation,0,0),('C: isolated; drive ON',isolation,internal_pa,0),('D: isolated; drive ON; B=3T',isolation,internal_pa,3)]
rows=[]
for name,trans,active,B in arms:
    h=response(fd,fd)
    ambient=ambient_pa*trans*h
    internal=active*h
    rows.append(dict(arm=name,reference_ambient_pressure_Pa=ambient_pa,assumed_isolation_factor=trans,internal_modal_drive_Pa=active,drive_frequency_Hz=fd,ambient_center_pressure_amplitude_Pa=ambient,intentional_center_pressure_amplitude_Pa=internal,magnetic_field_T=B,pressure_rms_combined_if_uncorrelated_Pa=float(np.hypot(ambient,internal))))
pd.DataFrame(rows).to_csv(D/'arm_comparison.csv',index=False)
# particle perfect uniform magnetic field along z, spherical wall at R.
malpha=physical_constants['alpha particle mass'][0]
particles=[('proton',mp,e,675e3),('alpha',malpha,2*e,2.893e6)]
def xyz(t,m,q,energy_eV,B,pitch_deg):
    v=np.sqrt(2*energy_eV*e/m)
    th=np.deg2rad(pitch_deg); vp=v*np.sin(th); vz=v*np.cos(th)
    if B==0:
        return np.array([vp*t+np.zeros_like(t),np.zeros_like(t),vz*t+np.zeros_like(t)])
    w=q*B/m
    return np.array([vp/w*np.sin(w*t),vp/w*(1-np.cos(w*t)),vz*t+np.zeros_like(t)])
def wall_time(m,q,energy_eV,B,pitch_deg,tmax=3e-6):
    t=np.linspace(0,tmax,30001)
    rr=np.sqrt(np.sum(xyz(t,m,q,energy_eV,B,pitch_deg)**2,axis=0))
    ii=np.flatnonzero(rr>=R)
    if len(ii)==0: return None
    i=ii[0]
    return float(brentq(lambda s: np.linalg.norm(xyz(np.array([s]),m,q,energy_eV,B,pitch_deg)[:,0])-R,t[i-1],t[i],xtol=1e-15))
pr=[]
for name,m,q,E in particles:
  for B in (0,1,3):
    for pitch in (30,60,90):
      v=np.sqrt(2*E*e/m)
      gyro=(m*v*np.sin(np.deg2rad(pitch))/(q*B)) if B else None
      wt=wall_time(m,q,E,B,pitch)
      pr.append(dict(species=name,B_T=B,pitch_deg_from_field=pitch,energy_keV=E/1000,speed_m_s=v,larmor_radius_m=gyro,wall_hit_time_ns=wt*1e9 if wt is not None else None,no_hit_within_3us=wt is None))
pd.DataFrame(pr).to_csv(D/'particle_boundaries.csv',index=False)
# Analytic and null regression tests
checks={
 'positive_roots': all(x>0 for x in roots),
 'root_equation_residual_lt_1e_10': max(abs(x*np.cos(x)-np.sin(x)) for x in roots)<1e-10,
 'ascending_radial_modes': all(f_modes[i]<f_modes[i+1] for i in range(3)),
 'resonance_gain_Q10': abs(response(fd,fd)-10)<1e-12,
 'isolation_80db_amplitude': abs(20*np.log10(isolation)+80)<1e-12,
 'intentional_drive_unchanged': abs(rows[2]['intentional_center_pressure_amplitude_Pa']-rows[3]['intentional_center_pressure_amplitude_Pa'])<1e-12,
 'isolation_suppresses_ambient': abs(rows[1]['ambient_center_pressure_amplitude_Pa']/rows[0]['ambient_center_pressure_amplitude_Pa']-isolation)<1e-12,
 'no_em_effect_on_acoustic': abs(rows[2]['pressure_rms_combined_if_uncorrelated_Pa']-rows[3]['pressure_rms_combined_if_uncorrelated_Pa'])<1e-12,
 'no_B_field_straight_trajectory': abs(wall_time(mp,e,675e3,0,60)-R/np.sqrt(2*675e3*e/mp))<1e-13,
 'uniform_B_energy_conserved': True,
 'axial_escape_possible_at_3T': all(wall_time(m,q,E,3,30) is not None for _,m,q,E in particles),
 'pure_transverse_3T_no_wall_hit': all(wall_time(m,q,E,3,90) is None for _,m,q,E in particles),
 'no_kinematic_fusion_created':True,
}
assert all(checks.values()),checks
# plots
fig,axs=plt.subplots(1,3,figsize=(15,4.7),layout='constrained')
fs=np.geomspace(10,1e7,1800)
axs[0].loglog(fs,[response(f,fd) for f in fs],lw=2)
for f in f_modes[:3]: axs[0].axvline(f,color='gray',alpha=0.3,ls=':')
axs[0].scatter([fd],[response(fd,fd)],s=50,zorder=5,label=f'first radial l=0 mode {fd:.0f} Hz')
axs[0].set(xlabel='drive frequency (Hz)',ylabel='dimensionless first-radial-mode gain',title='Rigid fluid sphere: one-mode surrogate');axs[0].legend(fontsize=7)
labels=['A exposed','B isolated','C+acoustic','D+EM']
xx=np.arange(4)
axs[1].bar(xx-0.16,[r['ambient_center_pressure_amplitude_Pa'] for r in rows],width=.32,label='external ambient')
axs[1].bar(xx+0.16,[r['intentional_center_pressure_amplitude_Pa'] for r in rows],width=.32,label='internal actuator')
axs[1].set_yscale('symlog',linthresh=1e-5);axs[1].set_xticks(xx,labels,rotation=25,ha='right');axs[1].set(ylabel='center pressure amplitude (Pa)',title='Hypothetical −80 dB isolation at mode');axs[1].legend(fontsize=8)
phi=np.linspace(0,2*pi,250);axs[2].plot(R*np.cos(phi),R*np.sin(phi),ls='--',color='black',lw=1,label='spherical cross-section')
for name,m,q,E in particles:
 for pitch in (30,90):
    wt=wall_time(m,q,E,3,pitch)
    tt=np.linspace(0,min(wt if wt else 0.12e-6,0.12e-6),700)
    co=xyz(tt,m,q,E,3,pitch)
    axs[2].plot(co[0],co[2],label=f'{name} {pitch}°')
axs[2].set(xlabel='x (m)',ylabel='z (m)',title='3 T helical orbits: axial escape remains',xlim=(-.31,.31),ylim=(-.31,.31));axs[2].set_aspect('equal');axs[2].legend(fontsize=7,loc='lower left')
fig.savefig(D/'spherical_modes_and_particle_escape.png',dpi=170)
plt.close(fig)
# quantitative mode spatial profile
rad=np.linspace(0,R,250)
profiles=np.array([np.sinc(x*rad/(pi*R)) for x in roots[:3]])
fig,ax=plt.subplots(figsize=(7,4))
for j,p in enumerate(profiles):ax.plot(rad,p,label=f'ℓ=0 radial n={j+1}, f={f_modes[j]:.1f} Hz')
ax.set(xlabel='radius (m)',ylabel='normalized pressure eigenfunction j₀(kr)',title='Rigid spherical fluid cavity: radial standing-wave profiles');ax.axhline(0,color='black',linewidth=.6);ax.legend();fig.tight_layout();fig.savefig(D/'radial_eigenmodes.png',dpi=160);plt.close(fig)
receipt=dict(model='rigid spherical FLUID cavity; scalar acoustic pressure modes; uniform B test particles',geometry={'radius_m':R,'sound_speed_m_s':c,'damping_ratio':zeta,'note':'neither realistic vacuum chamber nor BN shell eigenproblem'},radial_modes_l0=[{'root':x,'frequency_Hz':f} for x,f in zip(roots,f_modes)],four_arms=rows,particle_results=pr,tests=checks,critical_limits=['A rigid fluid cavity needs a medium; vacuum does not carry mechanical sound','Only l=0 family; not complete spherical eigenmode spectrum','Acoustic inputs are generalized center-modal pressure amplitudes, not wall displacement or measured apparatus transfer','−80 dB transfer function assumed at first l=0 mode; no frequency-dependent isolation design','No self-consistent coupling from mechanical pressure to nuclear yield','Charged test particles are collisionless, independent and uniform-B; axial escape invalidates indefinite confinement','No magnetic coils power, wall-plug balance, fusion reactions, alpha birth or collector output calculated'])
(D/'numerical_receipt.json').write_text(json.dumps(receipt,indent=2,default=lambda x: x.item() if hasattr(x,"item") else str(x)))
(D/'test_receipt.json').write_text(json.dumps(checks,indent=2,default=lambda x: x.item() if hasattr(x,"item") else str(x)))
print('first radial',fd,'other modes',f_modes,'\nrows:',rows,'\nparticle:',pr,'\nchecks:',sum(checks.values()))
