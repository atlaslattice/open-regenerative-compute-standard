from pathlib import Path
import numpy as np, csv,json,hashlib,zipfile
from scipy.integrate import quad
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path('/mnt/data/stars2_duration_success_v012');D.mkdir(exist_ok=True)
tau_on=.001; beta=500.; tau_mem=.005; gap=.002
DURS_MS=[.1,.25,1,2,5,10,25,50,100,250,500,1000,2500,5000,10000]
# Analytic integration of toy amplitude dynamics, history convolution, and exposure
def state(ms,arm):
 T=ms/1000; a0=1-np.exp(-T/tau_on)
 if arm=='PRE_ONLY':
  a=a0*np.exp(-beta*gap)
  m_pre=(1-np.exp(-T/tau_mem))-2*(np.exp(-T/tau_on)-np.exp(-T/tau_mem))/(1-tau_mem/tau_on)+(np.exp(-2*T/tau_on)-np.exp(-T/tau_mem))/(1-2*tau_mem/tau_on)
  m=m_pre*np.exp(-gap/tau_mem)+a0*a0*(np.exp(-gap/tau_mem)-np.exp(-2*beta*gap))/(tau_mem*(2*beta-1/tau_mem))
 else:
  a=a0
  m=(1-np.exp(-T/tau_mem))-2*(np.exp(-T/tau_on)-np.exp(-T/tau_mem))/(1-tau_mem/tau_on)+(np.exp(-2*T/tau_on)-np.exp(-T/tau_mem))/(1-2*tau_mem/tau_on)
 dose=T-2*tau_on*(1-np.exp(-T/tau_on))+.5*tau_on*(1-np.exp(-2*T/tau_on))
 return {'arm':arm,'pretreatment_ms':ms,'amplitude_envelope_at_shot':a,'slow_history_proxy_at_shot':m,'integrated_a_squared_s':dose,'actuator_on_time_ms':ms,'fusion_probability':'NOT_MODELED','fusion_events':'NOT_MODELED','qualified_alpha_output_J':'NOT_MODELED','net_electric_J':'NOT_MODELED','device_damage':'NOT_MODELED'}
rows=[state(ms,arm) for arm in ['PRE_ONLY','PRE_PLUS_SUSTAIN'] for ms in DURS_MS]
with (D/'duration_sweep.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
old=list(csv.DictReader(open('/mnt/data/stars2_duration_success_v011/duration_sweep.csv')))
errs=[]
for r in old:
 p=next(x for x in rows if x['arm']==r['arm'] and abs(x['pretreatment_ms']-float(r['pretreatment_ms']))<1e-9)
 for key in ('amplitude_envelope_at_shot','slow_history_proxy_at_shot','integrated_a_squared_s'):
  errs.append({'arm':r['arm'],'duration_ms':p['pretreatment_ms'],'key':key,'absolute_error':abs(float(r[key])-p[key])})
checks=[]
def check(name,cond):
 assert cond,name
 checks.append(name)
for arm in ['PRE_ONLY','PRE_PLUS_SUSTAIN']:
 subset=[r for r in rows if r['arm']==arm]
 check(f'{arm} history bounded',all(0<=r['slow_history_proxy_at_shot']<=1 for r in subset))
 check(f'{arm} amplitude bounded',all(0<=r['amplitude_envelope_at_shot']<=1 for r in subset))
 check(f'{arm} duration monotonic',all(subset[j+1]['pretreatment_ms']>subset[j]['pretreatment_ms'] for j in range(len(subset)-1)))
 check(f'{arm} dose monotonic',all(subset[j+1]['integrated_a_squared_s']>subset[j]['integrated_a_squared_s'] for j in range(len(subset)-1)))
 check(f'{arm} history monotonic',all(subset[j+1]['slow_history_proxy_at_shot']>=subset[j]['slow_history_proxy_at_shot']-1e-10 for j in range(len(subset)-1)))
 check(f'{arm} null fusion untouched',all(r['fusion_probability']=='NOT_MODELED' for r in subset))
for ms in DURS_MS:
 d={r['arm']:r for r in rows if r['pretreatment_ms']==ms}
 check(f'{ms} ms pre-only smaller amplitude',d['PRE_ONLY']['amplitude_envelope_at_shot']<d['PRE_PLUS_SUSTAIN']['amplitude_envelope_at_shot'])
check('10-second case exists',sum(abs(r['pretreatment_ms']-10000)<1e-8 for r in rows)==2)
check('10-second dose formula',abs(state(10000,'PRE_ONLY')['integrated_a_squared_s']-9.9985)<1e-9)
# Original Euler was dt 2e-6, analytic diff tolerance practical
check('prior Euler matched within 0.002 absolute',max(x['absolute_error'] for x in errs)<.002)
fig,axes=plt.subplots(2,1,figsize=(10,8),sharex=True)
for arm,style in [('PRE_ONLY','o-'),('PRE_PLUS_SUSTAIN','s--')]:
 vals=[r for r in rows if r['arm']==arm]
 axes[0].plot([r['pretreatment_ms']/1000 for r in vals],[r['slow_history_proxy_at_shot'] for r in vals],style,label=arm)
 axes[1].plot([r['pretreatment_ms']/1000 for r in vals],[r['amplitude_envelope_at_shot'] for r in vals],style,label=arm)
for a in axes:
 a.set_xscale('log');a.grid(alpha=.25);a.axvline(10,color='gray',linestyle=':',label='10 seconds');a.legend(fontsize=8)
axes[0].set_ylabel('Toy history variable at laser arrival');axes[1].set_ylabel('Toy mechanical envelope at laser arrival');axes[1].set_xlabel('Acoustic pre-treatment duration (seconds)');fig.suptitle('Stars 2.0 v0.12 — 10-second pre-treatment / toy-state saturation, NOT fusion yield');fig.tight_layout();fig.savefig(D/'duration_10s_saturation.png',dpi=155);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,4.8))
for arm in ['PRE_ONLY','PRE_PLUS_SUSTAIN']:
 v=[r for r in rows if r['arm']==arm]
 ax.plot([r['pretreatment_ms']/1000 for r in v],[r['integrated_a_squared_s'] for r in v],marker='o',label=arm)
ax.set(xscale='log',yscale='log',xlabel='Actuation time (seconds)',ylabel='Integrated squared toy envelope (seconds)',title='10-second actuation adds exposure without specified fusion benefit');ax.grid(alpha=.25);ax.legend();fig.tight_layout();fig.savefig(D/'duration_10s_exposure.png',dpi=155);plt.close(fig)
case10=[r for r in rows if r['pretreatment_ms']==10000]
case100=[r for r in rows if r['pretreatment_ms']==100]
report='''# Stars 2.0 v0.12 — 10-second acoustic pre-treatment extension
**2026-10-28 · APPEND-ONLY · NO fusion gain claim**

This re-evaluates the v0.11 *uncalibrated* duration-history oscillator at **10 seconds (10,000 milliseconds)**, in both schedules: PRE_ONLY (drive ends 2 ms before laser) and PRE_PLUS_SUSTAIN (drive continues until the laser shot). The entire earlier sweep is retained, with new logarithmically spaced durations from 0.25 to 10 seconds.

## Actual computation
Original illustrative equations: ON `da/dt=(1-a)/(0.001 s)`; OFF `da/dt=-500a/s`. Toy memory `dm/dt=(a²-m)/(0.005 s)`; accumulated exposure `∫a²dt`. This version uses analytic amplitude/exposure and accurate quadrature for memory, avoiding millions of small numerical timesteps at 10 seconds. The assumed memory has an artificial **5 ms** time constant; therefore it is expected to saturate far earlier than 10 seconds. No real BN memory or material saturation measurement is implied.

## Ten-second numerical results
'''
for r in case10:
 report+=f"- {r['arm']}: envelope at laser {r['amplitude_envelope_at_shot']:.9f}; history proxy {r['slow_history_proxy_at_shot']:.9f}; exposure {r['integrated_a_squared_s']:.7f} s.\n"
report+='''
## How to interpret
- A target exposed for 10 seconds has much more **modeled cumulative acoustic exposure** than one exposed for 100 milliseconds, but does not show a corresponding increase in the saturated history variable under the fixed 5-ms-memory assumption.
- The exposure integral is not a watt-hour, absorbed energy, thermal dose or damage estimate. No actuator power, acoustic coupling efficiency, heat transport, fatigue or materials data were provided.
- This does **not** prove that long treatment has no physical benefit; a real target may possess much slower processes (thermal diffusion, microstructure, flow, relaxation), but none is calibrated here. Longer treatment could instead damage or heat the target.
- **Fusion reaction probability, alpha yield and net power are intentionally NOT MODELED.** The success endpoint remains reactions per incident proton (with source distribution and boron areal inventory), with qualified alpha output and all-attempted-shot operations tracked separately. No arbitrary positive effect of 10 s has been inserted.
- No ability to distinguish 'acoustic memory' from ordinary vibration ringdown from these equations. Test against a zero-memory null and real target-state measurements.

## Scientific follow-up
Model target state using actual relevant time constants, elastic/thermal modes, measured density/porosity, support boundary conditions and laser timing; then pass measured effects through source-qualified proton stopping, energy-dependent p–B11 cross sections and detector-forward models. Include 0/0.1/1/10 s treatment, both pre-only and sustained plus OFF/SHAM, under equal-temperature/equal-energy controls.

## Reproduction and provenance
New v0.12 only. Prior v0.11 outputs untouched; reference rows were cross-checked against the original numerical Euler scheme. Source code + CSV + plots + SHA-256 manifest included.
'''
(D/'REPORT_v0_12.md').write_text(report)
(D/'run_v012.py').write_text(Path(__file__).read_text())
(D/'receipt.json').write_text(json.dumps({'checks':len(checks),'names':checks,'old_crosscheck_max_abs_difference':max(x['absolute_error'] for x in errs),'ten_second_cases':case10,'comparability':'toy model only; no predicted nuclear yield'},indent=2))
(D/'SHA256_MANIFEST.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in D.iterdir() if p.name!='SHA256_MANIFEST.json'},indent=2))
Z=Path('/mnt/data/STARS2_10_SECOND_PRETREAT_v0_12.zip')
with zipfile.ZipFile(Z,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(D.iterdir()):z.write(p,p.name)
print(json.dumps({'checks':len(checks),'max_previous_difference':max(x['absolute_error'] for x in errs),'cases10':case10,'cases100ms':case100,'zip':str(Z),'files':[str(p) for p in D.iterdir()]},indent=2))
