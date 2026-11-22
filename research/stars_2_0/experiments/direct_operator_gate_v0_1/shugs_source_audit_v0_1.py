"""Execute pinned SHUGS sources; compare with Tidal's earlier reconstruction.
No source mutation. This is not the unresolved full TCSS/Path B operator.
Usage: OPENBLAS_NUM_THREADS=1 python shugs_source_audit_v0_1.py --core PATH --packaged PATH
Writes JSON stdout; preserve each receipt under a new name.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time
import numpy as np
import scipy
import sympy

PIN='42e640e8b79bdc8d58af19946d3b9ede825af042'
HASHES={'core':'05ec9fbcaec930f954b581af67d460c7105909270735292e8c5cd63c80c1bfee',
        'packaged':'731e9aa6be6be27b3d2685d755175530a6d0ab62580e555567df335fc9fbca3b'}


def load(name,path):
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=HASHES[name]:
        raise ValueError('Source bytes differ from audited snapshot: '+name)
    spec=importlib.util.spec_from_file_location('audited_'+name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def summary(H,core):
    anti=float(np.linalg.norm(H-H.T.conj(),'fro'))
    if anti>1e-11*max(1,np.linalg.norm(H,'fro')):
        raise ValueError('Hermiticity gate failed; refuse eigh')
    vals,vecs=np.linalg.eigh(H)
    off=H.copy(); np.fill_diagonal(off,0)
    b=np.zeros(len(H)); b[-1]=1
    response=np.linalg.solve(H+1j*np.eye(len(H)),b)
    return {'hermiticity_fro':anti,
        'eigensystem_relative_residual':float(np.linalg.norm(H@vecs-vecs*vals,'fro')/max(1,np.linalg.norm(H,'fro'))),
        'eigenvalue_min':float(vals[0]),'eigenvalue_max':float(vals[-1]),
        'zero_rows_at_1e_minus_12':int(np.sum(np.max(abs(H),axis=1)<1e-12)),
        'last_node_offdiagonal_l1':float(np.sum(abs(off[-1]))),
        'last_node_diagonal':float(H[-1,-1]),
        'last_node_to_others_resolvent_l2':float(np.linalg.norm(response[:-1])),
        'legacy_core_GUE_KS':core.compute_gue_ks(vals),
        'score_scope':'historical metric only; no KS p-value validity or universality claim'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--core',required=True,type=Path)
    ap.add_argument('--packaged',required=True,type=Path)
    a=ap.parse_args(); t0=time.perf_counter()
    core=load('core',a.core); packaged=load('packaged',a.packaged)
    runs={}; matrices={}
    for N in (144,145):
        for seed in (None,42):
            for name,H in [('core',core.build_hsuf_operator(N,jitter_seed=seed)),
                           ('packaged',packaged.build_hsuf(N,seed=seed))]:
                key=f'{name}:N={N}:seed={seed}'
                runs[key]=summary(H,core); matrices[key]=H
    A=matrices['core:N=145:seed=None']; B=matrices['packaged:N=145:seed=None']
    # Controlled factorization of source differences at N145: identical raw
    # diagonal; distinct coupling scale and distinct window powers.
    raw=packaged.build_hsuf(145,params=packaged.HSUFParams(use_hanning=False),seed=None)
    lam=np.array([packaged.von_mangoldt(i) for i in range(1,146)])
    scale_pack=np.std(lam[lam>0]); diag=np.diag(raw); scale_core=np.std(diag[diag>0])
    off=raw-np.diag(diag); window=np.hanning(145)
    factorial={}; oracle_matrices={}
    for scale_name,scale in [('bare_VM',scale_pack),('completed_diagonal',scale_core)]:
        for window_name,w in [('hann',window),('sqrt_hann',np.sqrt(window))]:
            H=(np.diag(diag)+off*scale/scale_pack)*np.outer(w,w)
            key=scale_name+':'+window_name
            factorial[key]=summary(H,core); oracle_matrices[key]=H
    no_window=summary(raw,core)
    reproduction_targets={'core:N=144:seed=None':.29418,'core:N=145:seed=None':.26691,
                          'packaged:N=144:seed=None':.24246,'packaged:N=145:seed=None':.18226}
    diffs={key:float(abs(runs[key]['legacy_core_GUE_KS']-v)) for key,v in reproduction_targets.items()}
    checks={
        'original_sources_loaded_only_after_hash_check':True,
        'all_eigensystem_residuals_below_1e_minus_12':all(r['eigensystem_relative_residual']<1e-12 for r in runs.values()),
        'both_sources_isolate_last_node_even_with_jitter':all(r['last_node_offdiagonal_l1']==0 for r in runs.values()),
        'both_sources_have_zero_cross_node_resolvent':all(r['last_node_to_others_resolvent_l2']==0 for r in runs.values()),
        'packaged_admin_helper_returns_twelve_zeros':bool(np.all(packaged.admin_sphere_coupling(B)==0)),
        'removing_packaged_window_restores_coupling':no_window['last_node_offdiagonal_l1']>0,
        'factorized_core_reconstructs_source':float(np.max(abs(A-oracle_matrices['completed_diagonal:hann'])))<1e-12,
        'factorized_packaged_reconstructs_source':float(np.max(abs(B-oracle_matrices['bare_VM:sqrt_hann'])))<1e-12,
        'prior_reconstruction_scores_agree_to_reported_precision':all(d<1e-5 for d in diffs.values()),
    }
    receipt={'diagnostic_status':'PASS' if all(checks.values()) else 'FAIL',
        'historical_admin_coupling_hypothesis':'FAIL_FOR_THESE_WINDOWED_MATRICES',
        'TCSS_full_operator':'BLOCKED_MISSING_FINITE_TERM_DEFINITIONS',
        'source_repository':'atlaslattice/element-145','source_revision':PIN,
        'source_paths':{'core':'shugs/shugs_core.py','packaged':'element145/shugs/operator.py'},
        'source_sha256':HASHES,'runs':runs,
        'N145_matrix_relative_frobenius_difference':float(np.linalg.norm(A-B,'fro')/np.linalg.norm(A,'fro')),
        'N145_sorted_eigenvalue_max_difference':float(np.max(abs(np.linalg.eigvalsh(A)-np.linalg.eigvalsh(B)))),
        'factorial_scale_window':factorial,'packaged_no_window_control':no_window,
        'N145_scaling_values':{'bare_VM_sd':float(scale_pack),'completed_diagonal_sd':float(scale_core)},
        'prior_probe_rounded_score_absolute_differences':diffs,
        'checks':checks,'elapsed_seconds':time.perf_counter()-t0,
        'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limits':['No full 1728 TCSS H_B reconstruction','No physical membrane or routing simulation',
          'Legacy degree-5 unfolding and spacing filtering are preserved, not statistically qualified',
          'Zeta zeros are inputs to these matrices; no independent prediction of those zeros',
          'Hann window multiplication alone establishes no physical absorption or damping',
          'Resolvent is an algebraic connectivity check at shift i, not a mechanical transfer function',
          'No full historical ensemble, KS=0.0527 claim, or N145 architectural optimum reproduced']}
    print(json.dumps(receipt,indent=2,allow_nan=False))
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__=='__main__':main()
