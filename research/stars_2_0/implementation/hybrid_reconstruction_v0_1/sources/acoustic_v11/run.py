from pathlib import Path
import numpy as np, csv, json, hashlib, zipfile
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
TAU_ON=.001; BETA=500.; TAU_MEMORY=.005; GAP=.002; DT=2e-6
DURS_MS=[.1,.25,1,2,5,10,25,50,100]
# Both proposed acoustic schedules. PRE ends 2ms ahead of shot, PRE+SUSTAIN continues to shot.
def run(duration_ms, scheme):
    dur=duration_ms/1000
    end=GAP if scheme=='PRE_ONLY' else 0
    start=-dur-end
    t=np.arange(start,DT/2,DT)
    a=m=dose=0.
    for time in t:
        on=(time< -end-1e-12) if scheme=='PRE_ONLY' else time<0
        da=(1-a)/TAU_ON if on else -BETA*a
        a+=DT*da
        m+=DT*(a*a-m)/TAU_MEMORY
        if on: dose+=a*a*DT
    return a,m,dose, max(dur,0)
rows=[]
for scheme in ['PRE_ONLY','PRE_PLUS_SUSTAIN']:
    for duration in DURS_MS:
        a,m,dose,active_s=run(duration,scheme)
        rows.append({'arm':scheme,'pretreatment_ms':duration,'amplitude_envelope_at_shot':a,'slow_history_proxy_at_shot':m,'integrated_a_squared_s':dose,'actuator_on_time_ms':active_s*1000,'fusion_events':'NOT_MODELED','qualified_alpha_output_J':'NOT_MODELED','net_electric_J':'NOT_MODELED','device_damage':'NOT_MODELED'})
with (D/'duration_sweep.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
fig,ax=plt.subplots(figsize=(9,5));
for arm,style in [('PRE_ONLY','o-'),('PRE_PLUS_SUSTAIN','s--')]:
 r=[x for x in rows if x['arm']==arm];ax.plot([x['pretreatment_ms'] for x in r],[x['slow_history_proxy_at_shot'] for x in r],style,label=arm)
ax.set(xscale='log',xlabel='Actuation duration before laser (ms)',ylabel='Uncalibrated history variable at shot',title='Longer acoustic conditioning: saturating toy memory (not fusion success)');ax.grid(alpha=.3);ax.legend();fig.tight_layout();fig.savefig(D/'duration_memory.png',dpi=155);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,5));
for arm,style in [('PRE_ONLY','o-'),('PRE_PLUS_SUSTAIN','s--')]:
 r=[x for x in rows if x['arm']==arm];ax.plot([x['pretreatment_ms'] for x in r],[x['integrated_a_squared_s']*1000 for x in r],style,label=arm)
ax.set(xscale='log',yscale='log',xlabel='Actuation duration before laser (ms)',ylabel='Integrated squared envelope (ms)',title='Input-exposure proxy grows with duration (no damage law assigned)');ax.grid(alpha=.3);ax.legend();fig.tight_layout();fig.savefig(D/'duration_exposure.png',dpi=155);plt.close(fig)
checks=[]
def test(name,yes):
 assert yes,name;checks.append(name)
for arm in ['PRE_ONLY','PRE_PLUS_SUSTAIN']:
 r=[x for x in rows if x['arm']==arm]
 test(f'{arm}: long-duration history exceeds shortest',r[-1]['slow_history_proxy_at_shot']>r[0]['slow_history_proxy_at_shot'])
 test(f'{arm}: exposure rises monotonically',all(r[i+1]['integrated_a_squared_s']>r[i]['integrated_a_squared_s'] for i in range(len(r)-1)))
 test(f'{arm}: bounded envelopes',all(0<=v['amplitude_envelope_at_shot']<=1.001 for v in r))
 test(f'{arm}: bounded history',all(0<=v['slow_history_proxy_at_shot']<=1.001 for v in r))
 test(f'{arm}: no fusion success invented',all(v['fusion_events']=='NOT_MODELED' for v in r))
 test(f'{arm}: monotone time',all(r[i+1]['actuator_on_time_ms']>r[i]['actuator_on_time_ms'] for i in range(len(r)-1)))
# Verify PRE_ONLY amplitude is lower than continuous for same duration when decay gap is present
for dur in DURS_MS:
 d={r['arm']:r for r in rows if r['pretreatment_ms']==dur}
 test(f'{dur:g} ms: pre-only decays across 2ms gap',d['PRE_ONLY']['amplitude_envelope_at_shot']<d['PRE_PLUS_SUSTAIN']['amplitude_envelope_at_shot'])
report='''# Stars 2.0 v0.11 — Duration × Success Endpoint Gate

**October 28, 2026. NEW version, append-only. Toy pre-treatment model, NOT measured p–B11 performance.**

## Correct primary outcomes
The previous v0.9-v0.10 models emphasized laser geometric overlap and assumed absorbed optical energy. These are **mediators**, not the Stars success endpoint. The quantitative scientific scoreboard must report, from measured source-qualified data:

1. **Nuclear/particle success:** nuclear reaction count or rate per *measured incident proton distribution* and 11B areal inventory; transmitted proton spectrum; correlated born 3-alpha distributions; front/rear/side escaped alpha energy.
2. **Collector success:** *detector-qualified* alpha counts and energies, collector accepted alpha kinetic energy, gross measured electrical output at load, all uncertainties and detector/collector transfer functions.
3. **Operational success:** unbiased all-attempted-shot qualified yield, stability/variance, target lifetime, cost per qualified shot, throughput, and wall-electric J spent per useful collector J.
4. **Net success:** all-input, facility-boundary net electric energy (including laser, acoustic, EM coils, thermal loads, replacement, standby). Never declare net gain from optical absorption.

Success defined in the Stars 2.0 v0.9 paper as qualified collector-accepted energy per all-shot facility cost, alongside full physical and wall-plug ledgers. Comparing OFF/SHAM/ON must not condition on post-treatment mediators when estimating the total causal effect.

## Model actually executed
Sweep 0.1, 0.25, 1, 2, 5, 10, 25, 50, 100 milliseconds of acoustic actuation, separately:
- PRE_ONLY, with a fixed two-millisecond off period before the laser.
- PRE_PLUS_SUSTAIN, with continuous actuation up to the shot.

Envelope: `da/dt=(1-a)/1 ms` when driven, `da/dt=-500 a/s` when off. **Hypothetical, uncalibrated** slow-history state: `dm/dt=(a²-m)/5 ms`. Cycle-integrated `∫a² dt` is an exposure proxy, not thermal energy or damage. Compare duration, residual amplitude, modeled history and exposure. All fusion success fields remain NOT_MODELED. No optical output treated as success. This demonstrates why a duration-dependent experiment is meaningful, **not** that long preparation improves reactions.

## Interpretation and negative controls
A long treatment approaches the imposed steady-history state; the model *cannot* establish that this variable physically exists in a boron-rich catcher, whether it benefits fusion, or that more exposure is safe. Under the **zero-memory physical null**, the history variable has no effect on particle/collector outcomes. Excess input energy, heating, erosion, plasma disruption or target deformation may overwhelm any benefit. Equal-energy and equal-temperature controls are necessary in addition to identical-duration controls, and a longer ON history without a measured change in target state does not justify a yield bonus.

## Proposed preregistered multiarm experiment
OFF, hardware-matched SHAM, PRE_ONLY, SUSTAIN_ONLY, PRE_PLUS_SUSTAIN, and time/phase-scrambled controls. Block by target batch, beam energy/angle, fluence and detector run; independently measure target temperature, areal density, morphology, vibration/displacement, laser spot/shot timing, transmitted proton spectrum and alpha spectra. Predeclare primary endpoint: **collector-accepted alpha energy per attempted shot**, conditional only on preregistered detector quality criteria; include all shots in cost and wall-plug denominators. Secondary endpoint: fusion reaction estimate normalized by incident proton and 11B atom inventory. Do not infer reaction count from gamma/alpha counts without calibrated backgrounds and forward model.

## Stopping gate
A physically predictive proton–boron success simulation awaits measured energy-angle proton distributions, source-qualified reaction cross sections/branches, target stopping/straggling and stack geometry, calibrated detector acceptance and complete EM field geometry. A simulation that simply maps higher pretreatment time to higher yield would be circular. Frozen G0-B predictions remain on hold.
'''
report+='\n## Run receipts\n'+f'- {len(rows)} duration-arm rows; {len(checks)} checks passed.\n'
(D/'REPORT_v0_11.md').write_text(report)
(D/'receipt.json').write_text(json.dumps({'checks':checks,'data_rows':len(rows),'model':'uncalibrated target-memory sensitivity','success_outputs':'NOT_MODELED','parameters':{'tau_on_ms':1,'beta_off_s_inverse':500,'tau_history_ms':5,'gap_ms':2}},indent=2))
(D/'SHA256_MANIFEST.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in D.iterdir() if p.name!='SHA256_MANIFEST.json'},indent=2))
z=Path('/mnt/data/STARS2_DURATION_SUCCESS_GATE_v0_11.zip');
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as f:
 for p in D.iterdir():f.write(p,p.name)
print(json.dumps({'rows':len(rows),'checks':len(checks),'PRE_ONLY_10_ms':next(r for r in rows if r['arm']=='PRE_ONLY' and r['pretreatment_ms']==10),'PRE_PLUS_SUSTAIN_10_ms':next(r for r in rows if r['arm']=='PRE_PLUS_SUSTAIN' and r['pretreatment_ms']==10),'PRE_PLUS_SUSTAIN_100_ms':next(r for r in rows if r['arm']=='PRE_PLUS_SUSTAIN' and r['pretreatment_ms']==100),'zip':str(z)},indent=2))
