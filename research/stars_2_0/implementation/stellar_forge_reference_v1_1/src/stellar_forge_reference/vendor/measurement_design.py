"""Synthetic thin-target log-linear design study; no calibrated nuclear prediction."""
import hashlib
import json
import platform
from pathlib import Path
import numpy as np

PARAMETERS = ['log_areal_density', 'log_proton_stopping_scale',
              'log_alpha_stopping_scale', 'log_reaction_normalization',
              'log_detector_efficiency']
# Positive observables divided by arbitrary positive reference values before logs.
ROWS = np.array([[1,1,0,0,0], [1,0,1,0,0], [1,0,0,1,1]], dtype=float)
SIGMA = np.array([.03,.05,.08])  # Synthetic log-space noise, NOT facility estimates.

def analyze(rows, sigma):
    a = np.asarray(rows, dtype=float) / np.asarray(sigma)[:,None]
    u,s,v = np.linalg.svd(a, full_matrices=True)
    rank = int(np.sum(s > s[0]*1e-12))
    out = {'rank':rank, 'singular_values':s.tolist(),
           'null_directions':v[rank:].tolist(), 'parameter_sd_log':None}
    if rank == len(PARAMETERS):
        cov = (v.T / (s*s)) @ v
        out['parameter_sd_log'] = np.sqrt(np.diag(cov)).tolist()
    return out

def designs():
    result = {}
    for label,extra,noise in [
        ('joint_observables',[],[]),
        ('same_geometry_twice',ROWS.tolist(),SIGMA.tolist()),
        ('density_calibration',[[1,0,0,0,0]],[.02]),
        ('efficiency_calibration',[[0,0,0,0,1]],[.04]),
        ('both_calibrations',[[1,0,0,0,0],[0,0,0,0,1]],[.02,.04]),
        ('both_noisy_calibrations',[[1,0,0,0,0],[0,0,0,0,1]],[.20,.40])]:
        result[label] = analyze(ROWS.tolist()+extra, SIGMA.tolist()+noise)
    return result

def verify():
    r=designs()
    assert [x['rank'] for x in r.values()] == [3,3,4,4,5,5]
    # Independent algebra: p=y_p-t; a=y_a-t; n=y_count-t-e.
    oracle=np.sqrt([.02**2,.03**2+.02**2,.05**2+.02**2,
                    .08**2+.02**2+.04**2,.04**2])
    np.testing.assert_allclose(r['both_calibrations']['parameter_sd_log'],oracle,rtol=1e-12)
    # Finite multiplicative invariance, not merely a numerical rank check.
    theta=np.array([.2,-.1,.05,.3,-.2])
    for null in ([1,-1,-1,-1,0],[0,0,0,1,-1]):
        np.testing.assert_allclose(np.exp(ROWS@theta),np.exp(ROWS@(theta+np.array(null))),rtol=1e-14)
    # A count-model discrepancy aligned with normalization is undetectable here.
    full=np.vstack([ROWS,[1,0,0,0,0],[0,0,0,0,1]])
    shifted=np.array([0,0,.1,0,0])
    fit=np.linalg.solve(full,shifted)
    np.testing.assert_allclose(fit,[0,0,0,.1,0],atol=1e-14)
    return {'checks':['design ranks','independent variance oracle','finite invariances',
                      'invisible discrepancy'], 'status':'PASS'}

if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',required=True)
    args=parser.parse_args()
    out=Path(args.out); out.mkdir(parents=True,exist_ok=False)
    receipt={'classification':'PHYSICAL_CANDIDATE_SYNTHETIC_ONLY',
             'python':platform.python_version(),'numpy':np.__version__,
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'randomness':'none','parameters':PARAMETERS,'rows':ROWS.tolist(),
             'sigma_log':SIGMA.tolist(),'tests':verify(),'designs':designs(),
             'physical_validation':'NOT_RUN','calibration_noise':'ASSUMED_FOR_SENSITIVITY_ONLY'}
    (out/'RESULTS.json').write_text(json.dumps(receipt,indent=2,allow_nan=False)+'\n')
    print(json.dumps(receipt,indent=2,allow_nan=False))
