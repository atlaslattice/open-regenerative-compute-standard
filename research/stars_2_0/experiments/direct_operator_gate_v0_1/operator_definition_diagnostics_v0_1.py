"""Algebraic definition-gate diagnostics, NOT a reconstruction of TCSS/Path B.
Explicit illustrative matrices test proposed gates without inventing historical terms.
Run: OPENBLAS_NUM_THREADS=1 python operator_definition_diagnostics_v0_1.py
JSON stdout; caller should save to a new receipt filename. No input files modified.
"""
import hashlib
import json
from pathlib import Path
import platform
import time
import numpy as np
import scipy
from scipy import sparse

START = time.perf_counter()
N = 12
TOL = 1e-11  # Small deterministic float64 fixture bound, not a physical tolerance.

def dense_hermitian(H):
    H = np.asarray(H, complex)
    if H.ndim != 2 or H.shape[0] != H.shape[1] or not np.isfinite(H).all():
        raise ValueError('Finite square matrix required')
    residual = np.linalg.norm(H-H.conj().T, 'fro') / max(1.,np.linalg.norm(H,'fro'))
    if residual > TOL:
        raise ValueError('Not Hermitian: refuse eigh; no silent symmetrization')
    return np.linalg.eigh(H)


def maxabs(A):
    return float(abs(A).max())

# Explicitly NEW illustrative central-difference convention: S[i,i+1 mod N]=1,
# spacing=1, hbar=1, branch coordinates 0,...,N-1. Not recovered source code.
S = sparse.csr_matrix((np.ones(N),(np.arange(N),(np.arange(N)+1)%N)),shape=(N,N))
I = sparse.eye(N,format='csr')
X = sparse.diags(np.arange(N,dtype=float),format='csr')
P = -0.5j*(S-S.T)
L1 = 2*I-S-S.T
kron = lambda A,B: sparse.kron(A,B,format='csr')
Lxy = kron(X,P)-kron(P,X)
Lz = kron(Lxy,I)
Xz = kron(kron(I,I),X)
XL = Xz@Lz
comm = Xz@Lz-Lz@Xz

# Noncommuting Hermitian toy: product has eigenvalues +/-i.
a = np.diag([1.,-1.]); b = np.array([[0.,1.],[1.,0.]])
bad = a@b
rejected = False
try: dense_hermitian(bad)
except ValueError: rejected = True

# Trace obstruction: no finite matrices obey [X,P]=iI exactly.
comm1 = (X@P-P@X).toarray()
ccr_residual = float(np.linalg.norm(comm1-1j*np.eye(N),'fro'))
# Central P has two zero modes on an even periodic grid; P^2 != graph Laplacian.
pvals = np.linalg.eigvalsh(P.toarray())
lvals = np.linalg.eigvalsh(L1.toarray())
# Moving a coordinate seam alone vs consistently relabeling every operator.
Sd = S.toarray(); Xd = X.toarray(); Pd = P.toarray()
hxp = (Xd@Pd+Pd@Xd)/2
seam_only = ((Sd@Xd@Sd.T)@Pd + Pd@(Sd@Xd@Sd.T))/2
# Here P is circulant, so this particular seam move IS a consistent translation
# for Hxp alone. A fixed actuator/sensor must transform too to preserve response.
seam_equivariance = float(np.max(np.abs(seam_only-Sd@hxp@Sd.T)))

# Degenerate eigenspaces do not select a parity-adapted eigenbasis.
H = np.eye(2); parity=a; odd=b
R = np.array([[1.,-1.],[1.,1.]])/np.sqrt(2)
parity_basis_expectation = np.diag(odd)
rotated_expectation = np.diag(R.T@odd@R)

# delta_c as written: a bounded cancellation ratio, not automatically chirality.
def delta(H):
    vals, vecs = dense_hermitian(H)
    denom = (np.abs(vecs)**2)@np.abs(vals)
    numerator = np.abs(np.diag(H))
    return [{'value':None,'reason':'zero_denominator'} if d <= TOL else
            {'value':float(n/d),'reason':None} for n,d in zip(numerator,denom)]
cancellation = delta(b)
zero_case = delta(np.diag([0.,1.]))

metrics = {
    'tensor_commutator_max_abs':maxabs(comm),
    'tensor_product_hermiticity_max_abs':maxabs(XL-XL.getH()),
    'noncommuting_product_hermiticity_max_abs':float(np.max(np.abs(bad-bad.conj().T))),
    'noncommuting_product_eigenvalues_imag':np.linalg.eigvals(bad).imag.tolist(),
    'finite_commutator_trace_abs':float(abs(np.trace(comm1))),
    'canonical_commutator_residual_fro':ccr_residual,
    'canonical_commutator_universal_lower_bound_fro':float(np.sqrt(N)),
    'central_momentum_zero_modes':int(np.sum(np.abs(pvals)<TOL)),
    'graph_laplacian_zero_modes':int(np.sum(np.abs(lvals)<TOL)),
    'P_squared_minus_graph_L_max_abs':maxabs(P@P-L1),
    'consistent_seam_translation_max_abs':seam_equivariance,
    'degenerate_parity_basis_odd_expectations':parity_basis_expectation.tolist(),
    'degenerate_rotated_basis_odd_expectations':rotated_expectation.tolist(),
    'delta_cancellation_example':cancellation,
    'delta_zero_denominator_example':zero_case,
}
checks = {
    'tensor_factors_commute':metrics['tensor_commutator_max_abs']<TOL,
    'commuting_hermitian_product_is_hermitian':metrics['tensor_product_hermiticity_max_abs']<TOL,
    'noncommuting_product_rejected_before_eigh':rejected,
    'commutator_trace_zero':metrics['finite_commutator_trace_abs']<TOL,
    'canonical_commutator_cannot_equal_iI':ccr_residual >= np.sqrt(N)-TOL,
    'even_central_difference_has_extra_null_mode':metrics['central_momentum_zero_modes']==2 and metrics['graph_laplacian_zero_modes']==1,
    'momentum_square_not_graph_laplacian':metrics['P_squared_minus_graph_L_max_abs']>1,
    'consistent_coordinate_relabeling_preserved':seam_equivariance<TOL,
    'degenerate_eigenbasis_changes_odd_expectations':np.max(np.abs(parity_basis_expectation))<TOL and np.min(np.abs(rotated_expectation))>1-TOL,
    'delta_zero_need_not_mean_zero_operator':all(x['value']==0 for x in cancellation) and np.linalg.norm(b)>1,
    'undefined_delta_not_fabricated_zero':zero_case[0]['value'] is None,
}
result = {
    'status':'PASS' if all(checks.values()) else 'FAIL',
    'scope':'Definition-gate examples only; NOT the historical H_B, not a candidate full H_B',
    'historical_reconstruction_status':'BLOCKED_MISSING_TERM_DEFINITIONS',
    'ABCD':{'A_physical_model':'NOT_RUN_NO_SPECIMEN_MODEL',
            'B_plain_graph':'Previously tested separately; not a new full benchmark here',
            'C_historical_TCSS':'BLOCKED_MISSING_Hxp_AND_Lz',
            'D_historical_Path_B':'BLOCKED_MISSING_Hxp_Lz_Xz'},
    'parameters':{'N':N,'tensor_dimension':N**3,'illustrative_spacing':1,'illustrative_hbar':1,'tolerance':TOL,'randomness':'none'},
    'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'metrics':metrics,'checks':{k:bool(v) for k,v in checks.items()},
    'elapsed_seconds':time.perf_counter()-START,
}
print(json.dumps(result,indent=2,allow_nan=False))
raise SystemExit(0 if all(checks.values()) else 1)
