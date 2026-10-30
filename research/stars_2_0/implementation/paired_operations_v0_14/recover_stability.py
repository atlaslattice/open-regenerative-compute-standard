"""Reproduce selected published stability summaries from archived numeric data.

Do not execute the source notebook. Restrict pickle constructors to the exact
NumPy/Pandas data constructors used by the pinned source records.
"""
import argparse
import builtins
import hashlib
import importlib
import io
import json
from pathlib import Path
import pickle

import numpy as np

ALLOWED={('builtins','slice'),('numpy','dtype'),('numpy','ndarray'),
 ('numpy.core.multiarray','scalar'),('numpy.core.multiarray','_reconstruct'),
 ('numpy.core.numeric','_frombuffer'),('pandas.core.frame','DataFrame'),
 ('pandas.core.internals.managers','BlockManager'),('pandas._libs.internals','_unpickle_block'),
 ('pandas.core.indexes.base','_new_Index'),('pandas.core.indexes.base','Index'),
 ('pandas.core.indexes.multi','MultiIndex')}

class NumericUnpickler(pickle.Unpickler):
    def find_class(self,module,name):
        if (module,name) not in ALLOWED:raise ValueError('Unsupported source constructor: '+module+'.'+name)
        if module.startswith('numpy.core.'):module=module.replace('numpy.core.','numpy._core.')
        return getattr(importlib.import_module(module),name)

def checked_load(path,sha):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=sha:raise ValueError('Source member hash mismatch')
    return NumericUnpickler(io.BytesIO(raw)).load()

def recover(sources,out):
    sources=Path(sources);out=Path(out);out.mkdir(parents=True,exist_ok=True)
    meta=json.loads((sources/'ProtonSpatial_secondary.pkl.receipt.json').read_text())
    df=checked_load(sources/'ProtonSpatial_secondary.pkl',meta['sha256'])
    run='20210803/run05'
    bursts=np.unique([x[1] for x in df.index])[4:]
    window=df.loc[run].loc[bursts]
    vals=window['peak_Gy'].values
    finite=np.isfinite(vals)
    keep=finite&(vals>.1)
    dose=vals[keep][:300]
    m=json.loads((sources/'beam_fits/MEMBER_RECEIPTS.json').read_text())['members']
    rows=[]
    for burst in bursts:
        name=f'20210803_run05_burst{burst:03}_ProtonSpatial_beamprops.pkl'
        mm=next(x for x in m if Path(x['name']).name==name)
        data=checked_load(sources/'beam_fits'/name,mm['sha256'])
        for event,props in zip(data['event_list'],data['beam_props_list']):
            rows.append(dict(burst=int(burst),event=int(event),props=np.asarray(props,dtype=float).tolist()))
    selected=rows[:300];a=np.array([r['props'] for r in selected])
    minor=np.minimum(a[:,2],a[:,4]);major=np.maximum(a[:,2],a[:,4]);cx=a[:,1];cy=a[:,3]
    summary=dict(run=run,analysis_bursts=[int(x) for x in bursts],
       all_source_dataframe_rows=len(df),rows_in_selected_bursts=len(vals),
       dose_nonfinite_in_window=int(np.sum(~finite)),dose_at_or_below_threshold_in_window=int(np.sum(finite&(vals<=.1))),
       dose_retained_before_300_cap=int(np.sum(keep)),dose_entries_used=len(dose),
       beam_fit_entries_before_300_cap=len(rows),beam_fit_entries_used=len(selected),
       peak_dose_mean_Gy=float(np.mean(dose)),peak_dose_population_SD_Gy=float(np.std(dose)),
       minor_divergence_mean_mrad=float(np.mean(minor)),minor_divergence_population_SD_mrad=float(np.std(minor)),
       major_divergence_mean_mrad=float(np.mean(major)),major_divergence_population_SD_mrad=float(np.std(major)),
       centroid_x_population_SD_mrad=float(np.std(cx)),centroid_y_population_SD_mrad=float(np.std(cy)),
       centroid_convention='Population SD about constant mean, includes drift; not a measurement of laser timing jitter',
       all_preparation_attempt_success_probability=None,acoustic_effect_measured=False,
       selection='Source notebook: unique bursts[4:], dose>0.1 Gy, first300; beam fits first300 over selected bursts',
       interpretation='Published source stability benchmark; selection exclusions are not automatically physical misfires or unsuccessful preparations',
       notebook_cached_values=dict(dose_mean_Gy=40.7,dose_SD_Gy=4.6,minor_mean_mrad=23.48,minor_SD_mrad=2.35,major_mean_mrad=40.,major_SD_mrad=3.16))
    result=dict(summary=summary,peak_dose_Gy=dose.tolist(),beam_fit_rows=selected)
    (out/'STABILITY_DATA.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--sources',default='sources');p.add_argument('--out',default='receipts/run001');a=p.parse_args()
    print(json.dumps(recover(a.sources,a.out)['summary'],indent=2))
