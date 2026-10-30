"""Stars 2.0 G1/G2 v0.6 exploratory compartmental A/B; no fusion model."""
from pathlib import Path
import numpy as np, math, json, csv, hashlib, zipfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
m_p=1.67262192595e-27; m_alpha=6.6446573357e-27; e=1.602176634e-19
# Reuse prior v0.5 damped first-mode toy, not a material-calibrated BN foil.
f0=1e4; beta=500.; sigma_areal=.01; external_pressure=1.; internal_pressure=.05
omega0=2*math.pi*f0

def response(f,p):
    omega=2*math.pi*f
    return (p/sigma_areal)/math.hypot(omega0**2-omega**2,2*beta*omega)

def boris_trace(B, energy_keV, mass, charge_e, T=0.35e-6, steps=7000, radius_m=.3):
    # Uniform static B along z, E=0, initially transverse +x, initial position at axis.
    v=np.array([math.sqrt(2*energy_keV*1e3*e/mass),0.,0.])
    x=np.zeros(3); dt=T/steps; q=charge_e*e
    omega=q*B/mass; tvec=np.array([0.,0.,omega*dt/2]); svec=2*tvec/(1+np.dot(tvec,tvec))
    energy_initial=.5*mass*np.dot(v,v); radial_peak=0.; first_exit=None
    saved=[]
    for i in range(steps):
        vm=v+np.cross(v,tvec); v=v+np.cross(vm,svec)
        x+=v*dt
        rr=float(np.linalg.norm(x[:2])); radial_peak=max(radial_peak,rr)
        if first_exit is None and rr>=radius_m: first_exit=(i+1)*dt
        if i%(steps//350)==0: saved.append([x[0],x[1]])
    energy_delta=(.5*mass*np.dot(v,v)-energy_initial)/energy_initial
    rg=(mass*np.linalg.norm(v[:2])/(q*abs(B))) if B else None
    return dict(B_T=B,E_keV=energy_keV,orbit_radius_m=rg,radial_max_m=radial_peak,first_wall_time_s=first_exit,energy_relative_error=energy_delta,analytic_radial_max_m=2*rg if rg else None,orbit=np.array(saved).tolist())

arms=[
  dict(name='A_unisolated_no_EM',iso_db=0,drive=False,B=0.),
  dict(name='B_isolated_no_EM',iso_db=-80,drive=False,B=0.),
  dict(name='C_isolated_acoustic_no_EM',iso_db=-80,drive=True,B=0.),
  dict(name='D_isolated_acoustic_3T',iso_db=-80,drive=True,B=3.),
]
rows=[]; traces={}
for arm in arms:
    transmitted=external_pressure*10**(arm['iso_db']/20)
    ext=response(f0,transmitted); internal=response(f0,internal_pressure if arm['drive'] else 0.)
    # Separate coherent signals: unknown phase means total peak envelope lies between |a-b| and a+b.
    rec={'arm':arm['name'],'isolation_db_at_10khz':arm['iso_db'],'EM_B_T':arm['B'],
      'external_pressure_at_target_Pa':transmitted,'internal_applied_pressure_Pa':internal_pressure if arm['drive'] else 0.,
      'external_displacement_nm':ext*1e9,'internal_displacement_nm':internal*1e9,
      'combined_phase_unknown_lower_nm':abs(ext-internal)*1e9,'combined_phase_unknown_upper_nm':(ext+internal)*1e9,
      'fusion_yield':'NOT MODELED','alpha_electrical_collection':'NOT MODELED'}
    for species,m,z,E in [('proton',m_p,1,675.),('alpha',m_alpha,2,2893.3)]:
        trace=boris_trace(arm['B'],E,m,z)
        traces[(arm['name'],species)]=trace
        rec[f'{species}_radial_max_m']=trace['radial_max_m']
        rec[f'{species}_first_wall_time_ns']=None if trace['first_wall_time_s'] is None else trace['first_wall_time_s']*1e9
    rows.append(rec)
with (P/'arm_comparison.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
# Two independent analytic checks of Lorentz gyro: gyroradius and first transit for B0.
checks={
 'attenuation_amplitude_is_1e_minus4': abs(10**(-80/20)-1e-4)<1e-15,
 'unisolated_vs_isolated_external_displacement': abs(rows[1]['external_displacement_nm']/rows[0]['external_displacement_nm']-1e-4)<1e-13,
 'acoustic_drive_same_with_and_without_B': abs(rows[2]['internal_displacement_nm']-rows[3]['internal_displacement_nm'])<1e-14,
 'no_drive_exactly_zero_internal':rows[0]['internal_displacement_nm']==rows[1]['internal_displacement_nm']==0,
 'uniform_magnetic_energy_conserved': max(abs(t['energy_relative_error']) for t in traces.values())<1e-10,
 'zero_B_proton_wall_time_matches_ballistic':abs(traces[('A_unisolated_no_EM','proton')]['first_wall_time_s']-.3/math.sqrt(2*675e3*e/m_p)) < 0.35e-6/7000,
 'zero_B_alpha_wall_time_matches_ballistic':abs(traces[('A_unisolated_no_EM','alpha')]['first_wall_time_s']-.3/math.sqrt(2*2893.3e3*e/m_alpha)) < 0.35e-6/7000,
 'three_T_proton_orbit_matches_analytic':abs(traces[('D_isolated_acoustic_3T','proton')]['radial_max_m'] / traces[('D_isolated_acoustic_3T','proton')]['analytic_radial_max_m']-1)<2e-4,
 'three_T_alpha_orbit_matches_analytic':abs(traces[('D_isolated_acoustic_3T','alpha')]['radial_max_m'] / traces[('D_isolated_acoustic_3T','alpha')]['analytic_radial_max_m']-1)<2e-4,
 'magnetically_guided_test_particles_do_not_touch_sidewall':all(traces[('D_isolated_acoustic_3T',s)]['first_wall_time_s'] is None for s in ['proton','alpha']),
 'no_B_test_particles_touch_sidewall':all(traces[('A_unisolated_no_EM',s)]['first_wall_time_s'] is not None for s in ['proton','alpha']),
 'phase_interval_valid':all(row['combined_phase_unknown_lower_nm'] <=row['combined_phase_unknown_upper_nm'] for row in rows),
 'zero_fusion_model_no_gain_claim':all(row['fusion_yield']=='NOT MODELED' for row in rows),
}
assert all(checks.values()),checks
# plots
fig,axs=plt.subplots(1,2,figsize=(12,4.4))
labels=['A','B','C','D']; x=np.arange(4)
axs[0].bar(x-.16,[r['external_displacement_nm'] for r in rows],width=.32,label='Transferred ambient vibration')
axs[0].bar(x+.16,[r['internal_displacement_nm'] for r in rows],width=.32,label='Intentional acoustic drive')
axs[0].set_yscale('symlog',linthresh=.005);axs[0].set_xticks(x,labels);axs[0].set_ylabel('Steady-state amplitude (nm)');axs[0].set_title('10 kHz mechanical channels (separate amplitudes)');axs[0].legend(fontsize=8)
for s in ['proton','alpha']:
  for arm in ['A_unisolated_no_EM','D_isolated_acoustic_3T']:
    z=traces[(arm,s)]; pts=np.array(z['orbit']);axs[1].plot(pts[:,0],pts[:,1],label=f'{s}, {"3 T" if z["B_T"] else "0 T"}',lw=1.4)
theta=np.linspace(0,2*np.pi,400);axs[1].plot(.3*np.cos(theta),.3*np.sin(theta),'k--',lw=1,label='Illustrative 0.3 m side wall')
axs[1].set_aspect('equal');axs[1].set_xlabel('x (m)');axs[1].set_ylabel('y (m)');axs[1].set_title('Uniform-field toy orbits, E=0');axs[1].legend(fontsize=7,loc='upper right')
fig.tight_layout();fig.savefig(P/'mechanical_and_EM_comparison.png',dpi=165);plt.close(fig)
receipt={'status':'EXECUTED_EXPLORATORY_SEPARATED_SUBSYSTEMS_NOT_SELF_CONSISTENT_FUSION',
 'assumptions':{'mechanics':'one-mode linear oscillator; f0=10kHz beta=500/s areal mass=0.01kg/m2','external_pressure_Pa':external_pressure,'active_pressure_Pa':internal_pressure,'attenuation':'ideal flat -80dB at 10kHz only; physical feasibility NOT ESTABLISHED','particle_model':'nonrelativistic uniform static B, E=0, initial perpendicular injection from center, no stopping, scattering, space charge, electric trapping, collisions or finite chamber ends','B_T':3,'cylindrical_sidewall_R_m':.3,'observation_window_s':.35e-6,'energies_keV':{'proton':675,'alpha':2893.3},'fusion_yield':'NOT MODELED','collector':'NOT MODELED','electric_energy_consumption':'NOT MODELED'},'arms':rows,'checks':checks,'orbits':{k[0]+'_'+k[1]:v for k,v in traces.items()}}
(P/'numerical_receipt.json').write_text(json.dumps(receipt,indent=2,default=lambda o: o.item() if hasattr(o,'item') else str(o)))
report=f'''# STARS 2.0 G1/G2 coupled-field benchmark v0.6\n\n**Date:** 2026-10-28. **Executed, exploratory. NOT a calibrated reactor, plasma, BN foil or fusion-energy simulation.** Append-only new local version referencing v0.1–v0.5.\n\n## Architecture and control contract\nA = unisolated/no electromagnetic (EM) guidance; B = −80 dB isolated/no EM; C = isolated + intentional 10 kHz acoustic drive/no EM; D = C + static uniform 3 T magnetic guidance. All mechanics uses the same uncalibrated 10-kHz single-mode oscillator from v0.5. Mechanical isolation suppresses only *ambient input*, not the intentionally applied *internal* actuator; attenuation is idealized and specified only at 10 kHz. Phase between background and drive is not characterized, hence report separate amplitudes and possible phase-coherent total bounds.\n\n## Numerical inputs\nExternal harmonic pressure: 1 Pa; after −80 dB: 0.0001 Pa. Internal drive: 0.05 Pa. Mass per area 0.01 kg/m²; beta=500 s⁻¹. Proton kinetic energy =675 keV LAB; alpha illustration 2893.3 keV (8.68 MeV/3), **not a sampled correlated 3-alpha reaction**. Uniform static B=3 T, E=0, fictitious cylindrical sidewall radius R=0.3 m. Particle source at axis launched perpendicular to B. Numerical Boris integrator, 7000 steps over 350 ns. Neglect axial movement, fields generated by particles, collisions, stopping, straggling, density, target, collector, and power. Field is *trajectory guidance only*, not realistic confinement or recirculation.\n\n## Results\n\n| Arm | Ambient motion (nm) | Intentional motion (nm) | Proton sidewall? | Alpha sidewall? |\n|---|---:|---:|---|---|\n'''
for row in rows:
    report+=f"| {row['arm']} | {row['external_displacement_nm']:.6g} | {row['internal_displacement_nm']:.6g} | {'yes' if row['proton_first_wall_time_ns'] is not None else 'no in 350 ns'} | {'yes' if row['alpha_first_wall_time_ns'] is not None else 'no in 350 ns'} |\n"
report+=f'''\nTests: **{sum(checks.values())}/{len(checks)} passed**. 3-T charged-particle trajectories conserve kinetic energy in static B, by construction to numerical precision. Passing toy orbits are not evidence of plasma confinement, stability, nuclear reaction rate, or electrical recovery. A static B field cannot do kinetic work on the particles.\n\n## Decision / negative controls\nNo per-event reaction probability or alpha-production rate is calculated, so all arms have *unavailable* nuclear output rather than fictitious gains. No reliable electrical energy ledger is available: the magnets, actuators, laser, cryocooling, pump and output collector have not been specified with measured loads. Replacing absent values with zeros would be scientifically improper.\n\n### Next physically meaningful integration\nSource-qualified BN foil geometry and target vibration transfer function, measured −80 dB frequency-dependent transmissibility (including real structure-borne paths and heating), Lorentz/Boris independent benchmark in finite E/B geometry and beam distributions, proton stopping with EXFOR alpha-production semantics, correlated three-alpha dynamics, detector-forward modeling, full losses. Start with independent analytic checks and negative controls; no blind fusion prediction until implementation contract signed.\n\n### Origin\nLocal previous simulation `/mnt/data/stars2_minus80db_v05/run.py`, and research specification `STARS_2_0_v0_9_PRE_SIMULATION_MULTI_AGENT_SYNTHESIS_AND_HARMONIC_ANALYSIS_2026-10-27.md`; RF v0.2 and electroacoustic v0.4 for particle architecture. No original files modified.\n'''
(P/'REPORT_v0_6.md').write_text(report)
(P/'test_receipt.json').write_text(json.dumps(checks,indent=2,default=lambda o: o.item() if hasattr(o,'item') else str(o)))
files=sorted([p for p in P.iterdir() if p.is_file() and p.name!='SHA256_MANIFEST.json'])
(P/'SHA256_MANIFEST.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2))
z=P.parent/'STARS2_G1G2_COUPLED_FIELD_BENCHMARK_v0_6.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as dest:
 for f in sorted(P.iterdir()): dest.write(f,arcname=f.name)
print(json.dumps({'tests':{k:bool(v) for k,v in checks.items()},'arms':rows,'zip':str(z),'size':z.stat().st_size},indent=2))
