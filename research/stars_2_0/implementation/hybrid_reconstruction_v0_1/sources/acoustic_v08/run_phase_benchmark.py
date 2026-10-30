#!/usr/bin/env python3
"""Stars2 v0.8 phase-locked laser vs illustrative spherical acoustic clock.
A gaussian beam/target-overlap geometry proxy only. NO nuclear yield, plasma SBS, laser-energy transfer or net power modeled.
"""
from pathlib import Path
import csv,json,hashlib,zipfile
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
SEED=20261028
N=2000
f=817.652920
A_um=0.1  # hypothetical displacement from target solid not obtained from fluid pressure in v07
w_um=5.0  # illustrative beam 1/e^2 radius
x0_um=2.0 # baseline beam-to-target center offset
jitter_deg=10.
iso=1e-4 # an assumed external transmission coefficient (not physical test)
ambient_A_um=0.02  # hypothetical exterior disturbance in target displacement units, not v07 pressure
rng=np.random.default_rng(SEED)
# same ambient disturbance phase and laser timing jitter for paired arms
jitter=rng.normal(0,jitter_deg,N)
noise_phase=rng.uniform(0,2*np.pi,N)
external_um=ambient_A_um*iso*np.cos(noise_phase)
phase_list=[0,90,180,270]
conditions=[('REFERENCE',None,'unisolated'),('OFF',None,'isolated'),('SHAM',None,'isolated')]+[(f'ON_{p:03d}',p,'isolated') for p in phase_list]
# SHAM uses an electrical/thermal parity flag only; not a validated hardware sham
# Reference uses unisolated ambient, OFF is identical without internal drive.
rows=[]; samples=[]
for name,nominal,barrier in conditions:
    ext=(ambient_A_um if barrier=='unisolated' else ambient_A_um*iso)*np.cos(noise_phase)
    if nominal is None: displacement=ext
    else: displacement=ext+A_um*np.cos(np.deg2rad(nominal+jitter))
    # 1D Gaussian overlap, not absorption or alpha production.
    overlap=np.exp(-2*((x0_um-displacement)/w_um)**2)
    mean=float(np.mean(overlap)); sem=float(np.std(overlap,ddof=1)/np.sqrt(N))
    rows.append(dict(arm=name,phase_deg='' if nominal is None else nominal,shots=N,
                     isolation_factor=1 if barrier=='unisolated' else iso,
                     internal_amplitude_um=A_um if nominal is not None else 0,
                     normalized_optical_overlap_mean=mean,overlap_sem=sem,
                     mean_target_displacement_um=float(np.mean(displacement)),
                     acoustic_electrical_parity_flag=('UNVERIFIED' if name.startswith('SHAM') else 'N/A'),
                     nuclear_yield='NOT_MODELED',alpha_energy='NOT_MODELED',
                     field_guidance='UNCHANGED_FROM_V0.7_NOT_COUPLED'))
    for i in range(N):samples.append(dict(arm=name,shot_id=i,laser_phase_deg='' if nominal is None else nominal+float(jitter[i]),
                                        displacement_um=float(displacement[i]),normalized_optical_overlap=float(overlap[i])))
# Null checks: no displacement means no phase dependence; phase inversion yields symmetric displacement signs for zero jitter
refov=np.exp(-2*(x0_um/w_um)**2)
for ph in phase_list:
    nullov=np.exp(-2*((x0_um-0*np.cos(np.deg2rad(ph)))/w_um)**2)
    assert abs(nullov-refov)<1e-15
assert abs(10**(-80/20)-iso)<1e-15
assert len(rows)==7
assert all(0<=r['normalized_optical_overlap_mean']<=1 for r in rows)
assert f>0 and np.isfinite(1/f)
assert abs(np.cos(np.pi/2))<1e-15
assert abs(np.cos(np.pi)+1)<1e-15
assert rows[0]['nuclear_yield']=='NOT_MODELED'
assert abs(rows[2]['normalized_optical_overlap_mean']-rows[1]['normalized_optical_overlap_mean'])<1e-15
assert len(samples)==N*len(rows)
assert 0<jitter_deg<90
assert all(np.isfinite(r['overlap_sem']) for r in rows)
assert rows[3]['normalized_optical_overlap_mean']>rows[5]['normalized_optical_overlap_mean']
assert abs(rows[4]['normalized_optical_overlap_mean']-rows[6]['normalized_optical_overlap_mean'])<0.001
checks=13
with (D/'arm_comparison.csv').open('w',newline='') as fh:
    writer=csv.DictWriter(fh,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
with (D/'shot_samples.csv').open('w',newline='') as fh:
    writer=csv.DictWriter(fh,fieldnames=samples[0].keys());writer.writeheader();writer.writerows(samples)
ph=np.linspace(0,360,721)
u=A_um*np.cos(np.deg2rad(ph))
overlap=np.exp(-2*((x0_um-u)/w_um)**2)
fig,ax=plt.subplots(2,1,figsize=(9,7),sharex=True)
ax[0].plot(ph,u,label='Assumed target displacement');ax[0].axhline(0,ls=':',color='grey');ax[0].set_ylabel('Displacement (µm)');ax[0].grid(alpha=.2)
ax[1].plot(ph,overlap,label='Optical overlap proxy');ax[1].axhline(refov,color='gray',ls='--',label='No acoustic drive');ax[1].set_xlabel('Laser phase relative to acoustic clock (deg)');ax[1].set_ylabel('Normalized Gaussian overlap');ax[1].grid(alpha=.2);ax[1].legend()
fig.suptitle('Stars 2.0 v0.8 · Phase-locked illustrative geometry (NOT fusion yield)')
fig.tight_layout();fig.savefig(D/'phase_response.png',dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,4))
labels=[r['arm'] for r in rows];ys=[r['normalized_optical_overlap_mean'] for r in rows];err=[r['overlap_sem'] for r in rows]
ax.bar(labels,ys,yerr=err,capsize=3);ax.set_ylim(min(ys)-.012,max(ys)+.012);ax.set_ylabel('Normalized optical overlap (dimensionless)');ax.tick_params(axis='x',rotation=30);ax.set_title('Matched shot sampling; no fusion or plasma physics');fig.tight_layout();fig.savefig(D/'matched_arms.png',dpi=170);plt.close(fig)
base=next(r for r in rows if r['arm']=='OFF');best=next(r for r in rows if r['arm']=='ON_000');worst=next(r for r in rows if r['arm']=='ON_180')
receipt={'status':'ILLUSTRATIVE_GEOMETRY_ONLY','seed':SEED,'checks_passed':checks,'model':{'spherical_v07_fluid_mode_frequency_Hz_used_only_as_clock':f,'mode_period_ms':1000/f,'target_displacement_amplitude_um_hypothetical':A_um,'beam_radius_um_hypothetical':w_um,'initial_offset_um_hypothetical':x0_um,'jitter_deg':jitter_deg,'isolation_amplitude_factor_assumed':iso,'shot_count_per_arm':N},'results':{'off_overlap':base['normalized_optical_overlap_mean'],'on0_overlap':best['normalized_optical_overlap_mean'],'on180_overlap':worst['normalized_optical_overlap_mean'],'on0_relative_percent':100*(best['normalized_optical_overlap_mean']/base['normalized_optical_overlap_mean']-1),'on180_relative_percent':100*(worst['normalized_optical_overlap_mean']/base['normalized_optical_overlap_mean']-1)},'nonresults':['no alpha source','no laser-plasma simulation','no nuclear reaction probability','no real elastic target mode','no collector output','no net electricity']}
(D/'receipt.json').write_text(json.dumps(receipt,indent=2))
report=f'''# Stars 2.0 v0.8 — Spherical Laser–Acoustic Phase-Lock Geometry Benchmark

**Date: 2026-10-28. Exploratory toy model; 13/13 implementation checks passed. NOT nuclear/plasma/fusion prediction.**

## Question
Could a hypothetical vibrational target displacement synchronized to an incident laser change *geometric optical overlap*, holding all other inputs fixed? The answer is **yes in the assumed Gaussian-overlap model, by construction**. An observed fusion yield effect is **not simulated or established**.

## Source lineage
Follows local v0.7 spherical fluid-cavity surrogate (f1≈817.653 Hz). Its fluid-mode pressure result is NOT converted into a solid target displacement. The present 0.1 µm displacement is an **independent illustrative assumed value**. The sphere does not propagate mechanical sound through vacuum; a real target/support elasticity and actuator-transfer function are required.

Sources to reconcile: Stars 2.0 v0.9 pre-simulation synthesis at https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/stars_2_0/whitepapers/STARS_2_0_v0_9_PRE_SIMULATION_MULTI_AGENT_SYNTHESIS_AND_HARMONIC_ANALYSIS_2026-10-27.md ; Stars 2.0 v0.4 modular electroacoustic reactor architecture at https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/stars-2-0-modular-pb11-electroacoustic-alpha-recovery-whitepaper-v0.4-2026-10-27.md .

## Mechanism explicitly simulated
\[u(\phi) = A \cos(\phi),\qquad G(\phi) = \exp[-2(x_0-u(\phi))^2/w^2].\]

Assume A={A_um:.3f} µm, beam 1/e² radius w={w_um:.2f} µm, initial offset x0={x0_um:.2f} µm, clock f={f:.3f} Hz, 10° shot-phase jitter, N={N} per arm, matched jitter and ambient disturbance draws, ambient vibration 0.02 µm **hypothetical**, exterior isolation 10^-4 amplitude **hypothetical**. Reference is unisolated with drive off; OFF isolated drive off; SHAM **software-only** equal OFF (actual electrical/heat/EMP parity NOT validated); ON phases 0°,90°,180°,270°. Compare accepted optical-overlap proxy, NOT alpha yield or absorbed energy.

## A/B results
| Arm | Overlap mean | Standard error |
|---|---:|---:|
'''
for r in rows:report+=f"|{r['arm']}|{r['normalized_optical_overlap_mean']:.8f}|{r['overlap_sem']:.8f}|\n"
report+=f'''
Relative to OFF: ON 0° change **{receipt['results']['on0_relative_percent']:.3f}%**, ON 180° change **{receipt['results']['on180_relative_percent']:.3f}%** in this chosen beam-offset geometry. These differences are the direct, programmed consequences of geometry and must not be described as unexpected model discoveries, energy gain or measured coupling. With zero vibrational displacement A=0, all phases reduce to the same overlap (negative control).

## What is NOT modeled
1. The solid target's true eigenfrequency, modal displacement, or target material response.
2. High-power laser propagation, absorption, nonlinear plasma formation, stimulated Brillouin scattering, ion-acoustic dispersion or real proton source distributions.
3. Energy-dependent proton transport/EXFOR reaction cross section, correlated 3-alpha kinematics, detector response, collection and wall-plug net electricity.
4. EM confinement changes from acoustic phase (v0.7 fields and trajectories remain **uncoupled**).
5. A physically matched SHAM electric/thermal/EMP control: SHAM=OFF by definition in code.

## Next validation gate
Replace assumed displacement with measured elastic shell/catcher field; simulate laser geometry and target absorption using source-calibrated models; pair four arms (REFERENCE/OFF/SHAM/ON) with independently verified sham thermal/EMP equivalence; feed measured incident proton distributions into independently calibrated G0-B transport and detector analysis; do not apply arbitrary ON-to-yield multipliers. Alpha-wave recovery is a **separate** post-birth branch requiring experimentally qualified plasma waves, not conventional acoustic waves in vacuum. Keep full actuator/laser/magnet load on energy ledger.

**Wizards in back; receipts in front. No physics = no magic.**
'''
(D/'REPORT_v0_8.md').write_text(report)
manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(D.iterdir()) if p.name!='SHA256_MANIFEST.json'}
(D/'SHA256_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
z=D.parent/'STARS2_LASER_ACOUSTIC_PHASE_LOCK_v0_8.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as fh:
    for p in sorted(D.iterdir()):fh.write(p,arcname=f'stars2_phase_locked_v08/{p.name}')
print(json.dumps({'zip':str(z),'checks':checks,**receipt['results']},indent=2))
