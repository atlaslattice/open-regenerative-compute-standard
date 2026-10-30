import numpy as np, csv, json, hashlib, zipfile
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
f=817.652920; A=0.1; tau_on=0.001; beta_decay=500.; tau_memory=.005; dt=2e-6
# Envelope dynamics da/dt=(1-a)/tau_on when active, da/dt=-beta_decay*a otherwise.
# Slow memory dm/dt=(a*a-m)/tau_memory (cycle-averaged acoustic intensity proxy).
scenarios={
'OFF':lambda t:False,
'SHAM':lambda t:False,
'PRE_ONLY':lambda t:-.010<=t<-.002,
'SUSTAIN_ONLY':lambda t:-.00025<=t<=0,
'PRE_PLUS_SUSTAIN':lambda t:-.010<=t<=0,
}
t=np.arange(-.010,0+dt/2,dt)
traces={}; states={}
for name,drive in scenarios.items():
    a=0.; m=0.; aa=[]; mm=[]
    for tm in t:
        on=drive(tm)
        a += dt*((1-a)/tau_on if on else -beta_decay*a)
        m += dt*((a*a-m)/tau_memory)
        aa.append(a);mm.append(m)
    traces[name]=(np.array(aa),np.array(mm));states[name]=(float(a),float(m))
# Physically coherent phase at laser shot, with matched phase-jitter. No material-specific calibration.
rng=np.random.default_rng(20261028)
N=2000
phase_jitter=rng.normal(0,10,N)
ambient_phase=rng.uniform(0,2*np.pi,N)
laser_J=.6*np.clip(1+.04*rng.normal(size=N),.1,None)
phase_values=[0,90,180,270]
G0=np.exp(-2*(2/5)**2)
rows=[]
for name in scenarios:
    phases=phase_values if name not in ('OFF','SHAM') else [0]
    a,m=states[name]
    for phase in phases:
        u=A*a*np.cos(np.deg2rad(phase+phase_jitter))+.02e-4*np.cos(ambient_phase)
        overlap=np.exp(-2*((2-u)/5)**2)
        for geom_beta in [0.,1.]:
            for memory_chi in [0.,.5,1.]:
                # memory dependence *entirely hypothetical*: normalization designed to be dimensionless.
                eta=np.clip(.30*(1+geom_beta*(overlap/G0-1)+memory_chi*m*.05),0,1)
                dep=eta*laser_J
                rows.append(dict(arm=name,phase_deg=phase,geom_beta=geom_beta,memory_chi=memory_chi,
                  envelope_at_shot=a,memory_at_shot=m,mean_overlap=float(overlap.mean()),
                  mean_absorbed_J=float(dep.mean()),mean_absorptance=float(eta.mean()),
                  fusion_yield='NOT_MODELED',proton_spectrum='NOT_MODELED',
                  memory_status='HYPOTHETICAL_UNCALIBRATED'))
with (D/'scenario_sweep.csv').open('w',newline='') as o:
    w=csv.DictWriter(o,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
R={(r['arm'],r['phase_deg'],r['geom_beta'],r['memory_chi']):r for r in rows}
checks=[]
def chk(name,condition):
    assert condition,name
    checks.append(name)
chk('off envelope zero',states['OFF'][0]==0)
chk('sham same state as off',states['SHAM']==states['OFF'])
chk('pre-only residual nonzero',0<states['PRE_ONLY'][0]<states['PRE_PLUS_SUSTAIN'][0])
chk('sustained-only smaller than full',states['SUSTAIN_ONLY'][0]<states['PRE_PLUS_SUSTAIN'][0])
chk('pre-only retains slow memory',states['PRE_ONLY'][1]>0)
chk('both retains memory more than sustain-only',states['PRE_PLUS_SUSTAIN'][1]>states['SUSTAIN_ONLY'][1])
chk('beta=chi=0 is universal null',max(abs(r['mean_absorbed_J']-R[('OFF',0,0.,0.)]['mean_absorbed_J']) for r in rows if r['geom_beta']==r['memory_chi']==0)<1e-12)
chk('off and sham identical',all(R[('OFF',0,b,c)]['mean_absorbed_J']==R[('SHAM',0,b,c)]['mean_absorbed_J'] for b in [0.,1.] for c in [0.,.5,1.]))
chk('phase sign flip with geometry coefficient',R[('PRE_PLUS_SUSTAIN',0,1.,0.)]['mean_absorbed_J']>R[('PRE_PLUS_SUSTAIN',180,1.,0.)]['mean_absorbed_J'])
chk('memory no effect when chi=0',all(abs(R[(name,phase,0.,0.)]['mean_absorbed_J']-R[('OFF',0,0.,0.)]['mean_absorbed_J'])<1e-12 for name in scenarios for phase in (phase_values if name not in ('OFF','SHAM') else [0])))
chk('absorptance bounded',all(0<=r['mean_absorptance']<=1 for r in rows))
chk('no fusion output invented',all(r['fusion_yield']=='NOT_MODELED' for r in rows))
chk('all numeric finite',all(np.isfinite(r['mean_absorbed_J']) for r in rows))
chk('paired sample size',N==len(laser_J)==len(phase_jitter))
chk('1 step dt resolves drive',dt<1/(20*f))
fig,ax=plt.subplots(figsize=(9,4.9))
for name in ['PRE_ONLY','SUSTAIN_ONLY','PRE_PLUS_SUSTAIN']:
    aa,mm=traces[name];ax.plot(1000*t,aa,label=f'{name} envelope')
ax.set(xlabel='Time relative to laser arrival (ms)',ylabel='Acoustic amplitude fraction',title='Independent pre-treatment and sustained-drive histories');ax.axvline(0,c='k',linestyle=':');ax.legend(fontsize=8);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(D/'acoustic_timing_envelopes.png',dpi=155);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,5))
labels=['OFF','PRE_ONLY','SUSTAIN_ONLY','PRE_PLUS_SUSTAIN']
for chi,style in [(0.,'o-'),(1.,'s--')]:
    vals=[R[(x,0,1.,chi)]['mean_absorbed_J'] for x in labels]
    ax.plot(labels,vals,style,label=f'geometry β=1; memory χ={chi:g}')
ax.axhline(R[('OFF',0,0.,0.)]['mean_absorbed_J'],c='gray',linestyle=':',label='β=χ=0 null')
ax.set(ylabel='Mean absorbed optical J [assumed proxy]',title='Timing-arm comparison; hypothetical geometry and slow-memory couplings');ax.grid(alpha=.2);ax.legend(fontsize=8)
fig.tight_layout();fig.savefig(D/'arm_absorption_sensitivity.png',dpi=155);plt.close(fig)
rec={'title':'Stars 2.0 pretreatment and sustained acoustic v0.10','status':'SIMULATED_UNCALIBRATED','checks':checks,'states':{k:{'envelope_at_shot':v[0],'memory_at_shot':v[1]} for k,v in states.items()},'n_scenarios':len(rows),'n_shots_paired':N,'model':{'frequency_hz':f,'amplitude_um':A,'drive_build_up_tau_ms':tau_on*1000,'off_decay_beta_s_inv':beta_decay,'memory_tau_ms':tau_memory*1000,'pre_window_ms':[-10,-2],'sustain_only_window_ms':[-.25,0],'laser_wall_energy_not_budgeted':True}}
(D/'receipt.json').write_text(json.dumps(rec,indent=2))
null=R[('OFF',0,0.,0.)]['mean_absorbed_J'];geom0=R[('OFF',0,1.,0.)]['mean_absorbed_J']
report=f'''# Stars 2.0 v0.10 — Acoustic pre-treatment vs sustained excitation at laser arrival

**2026-10-28 · Exploratory coupled timing surrogate · {len(checks)}/{len(checks)} checks · NO measured fusion increase.**

## Source context and reason for intervention
DeepSeek's Stars 2.0 review suggested acoustic target conditioning *before* the laser interaction; this v0.10 independently compares pre-treatment, late-start concurrent excitation, and combined continuously driven preparation. The prior v0.8-v0.9 phase-lock models used a single instantaneous acoustic displacement; they did not differentiate pre-shot target history.

## Physically distinct interventions
- **OFF**: no applied acoustic drive; source noise/laser jitter are paired across all scenarios.
- **SHAM**: numerically same as OFF; not a verified equal-heat/equal-EMP physical sham.
- **PRE_ONLY**: actuator ON from t=-10 to -2 ms; then OFF until t=0 laser arrival; free decay modeled.
- **SUSTAIN_ONLY**: actuator ON only from t=-0.25 ms until laser arrival; limited build-up time.
- **PRE_PLUS_SUSTAIN**: actuator ON continuously from t=-10 ms through laser arrival.
These schedules are illustrative test definitions, not a recommended experimental pulse protocol.

## Dynamical and optical model, with explicit unsupported links
Amplitude envelope a(t) obeys da/dt=(1-a)/1 ms (drive ON) or da/dt=-500 a /s (OFF). It modulates u=0.1 μm*a*cos(ωt+φ). A separate **hypothetical** slow preparation-memory proxy m(t) obeys dm/dt=(a²-m)/5 ms; it is not a measured permanent material transformation or microstructure law. Its influence χ on absorptance is explicitly optional and **unvalidated**.
Optical overlap G=exp[-2(x0-u)²/w²], x0=2 μm, w=5 μm, then hypothetical absorptance η=clip[0.30*(1+β(G/G0-1)+0.05χm),0,1] with β=0 or 1 and χ=0,0.5,1. Matched random laser-energy jitter 4%, phase jitter 10°, 2000 paired shots. No plasma model, cross section, stopping power, nuclear reaction, magnetic confinement, alpha collector or calibrated laser absorption is computed. The laser optical energy is set to 0.6 J; NO net-electric claim.

## Numerical state at laser arrival
| Arm | Acoustic envelope relative to nominal | Slow-memory proxy (dimensionless) |
|---|---:|---:|
'''
for name in scenarios:report+=f'| {name} | {states[name][0]:.6f} | {states[name][1]:.6f} |\n'
report+='''
## Optical absorbed-energy proxy at 0° phase
Compare as a sensitivity range, **not** as measured improvement. `β=0,χ=0` forces all modeled arms to the same output; `β=1,χ=0` exposes a geometry-only pathway; `β=1,χ=1` adds an imposed memory pathway.

| Arm | β=1,χ=0 mean J | β=1,χ=1 mean J | Difference vs OFF for β=1,χ=0 |
|---|---:|---:|---:|
'''
for name in ['OFF','PRE_ONLY','SUSTAIN_ONLY','PRE_PLUS_SUSTAIN']:
    q=R[(name,0,1.,0.)]['mean_absorbed_J'];z=R[(name,0,1.,1.)]['mean_absorbed_J']
    report+=f'| {name} | {q:.8f} | {z:.8f} | {(q/geom0-1)*100:+.4f}% |\n'
report+=f'''

Universal no-coupling null mean absorbed energy: **{null:.8f} J**, independent of acoustic schedule. Any better result when χ or β >0 is determined by assumed coefficients and does not validate the mechanism. Unlike earlier models, pre-treatment alone can leave a nonzero mechanical ringdown and a slowly relaxing history variable; that does not imply a real boron catcher exhibits preparation memory.

## Decision gates
1. Measure actual BN/boron target wave modes, mechanical damping and phononic isolation in the relevant structure, not in the fluid sphere surrogate.
2. Measure target surface/morphology/density/temperature at laser arrival after PRE_ONLY vs SUSTAIN_ONLY vs combined actuation. Fit a memory model only with experimental data; compare to zero-memory null.
3. Calibrate laser absorption and proton spectral distributions with actual diagnostics. Fit β and χ on training shots, predict withheld phase/schedule arms.
4. Real hardware SHAM must match electrical/thermal/EMP conditions; all shots and per-shot energy expense included.
5. For Stars fusion interpretation, only after calibrated proton source and target state should EXFOR nuclear cross sections, BN proton/alpha stopping, correlated 3-alpha event kinematics, detectors and collector acceptance be applied. No invented fusion multiplier.
6. Do not claim electromagnetic confinement is modeled here; integrate it as separate measured E/B field and loss topology later.

## Preservation
This is a NEW v0.10 local artifact. No v0.9/v0.8 files overwritten; no GitHub writes. Numerical checks are consistency checks, not empirical validation.
'''
(D/'REPORT_v0_10.md').write_text(report)
files=[p for p in D.iterdir() if p.name!='SHA256_MANIFEST.json']
(D/'SHA256_MANIFEST.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2))
z=Path('/mnt/data/STARS2_PRETREAT_SUSTAIN_PHASE_v0_10.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as archive:
    for p in sorted(D.iterdir()):archive.write(p,arcname=p.name)
print(json.dumps({'states':rec['states'],'n_rows':len(rows),'checks':len(checks),'zip':str(z),'zip_bytes':z.stat().st_size,'selected':{k:R[(k,0,1.,0.)]['mean_absorbed_J'] for k in ['OFF','PRE_ONLY','SUSTAIN_ONLY','PRE_PLUS_SUSTAIN']}},indent=2))
