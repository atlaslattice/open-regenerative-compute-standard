"""Dimensionless analytical benchmark, not a membrane or TCSS H_B model.
Run: OPENBLAS_NUM_THREADS=1 python finite_torus_benchmark_v0_1.py
Requires Python >=3.10, NumPy, SciPy. Writes JSON to stdout only.
"""
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

N = 12
SEED = 20261028
TOL = 1e-10  # Numerical regression tolerance; no physical acceptance meaning.
rng = np.random.default_rng(SEED)
shape = (N, N, N)
size = N**3
# Independent coordinate-edge assembly, rather than an FFT-built matrix.
rows, cols, values = [], [], []
for point in np.ndindex(shape):
    i = np.ravel_multi_index(point, shape)
    rows.append(i); cols.append(i); values.append(6.)
    for axis in range(3):
        for direction in (-1, 1):
            neighbor = list(point)
            neighbor[axis] = (neighbor[axis] + direction) % N
            rows.append(i)
            cols.append(np.ravel_multi_index(tuple(neighbor), shape))
            values.append(-1.)
L = coo_matrix((values, (rows, cols)), shape=(size, size)).tocsr()
coordinates = np.indices(shape)
symbol = sum(4 * np.sin(np.pi * coordinates[j] / N)**2 for j in range(3))
mode_errors = []
for k in [(0, 0, 0), (6, 6, 6), (1, 2, 3), (11, 0, 7)]:
    mode = np.exp(2j*np.pi*sum(k[j]*coordinates[j] for j in range(3))/N).ravel()
    mode_errors.append(float(np.max(np.abs(L @ mode - symbol[k]*mode))))
u = rng.normal(size=shape)
heat_time = .37
heat_sparse = expm_multiply(-heat_time * L, u.ravel()).reshape(shape)
heat_fft = np.fft.ifftn(np.exp(-heat_time * symbol)*np.fft.fftn(u)).real
impulse = np.zeros(size); impulse[0] = 1.
heat_kernel = expm_multiply(-heat_time * L, impulse)
# Wave energy with M=I, K=L, no damping; zero mode handled by sinc.
v = rng.normal(size=shape)
t = .81
omega = np.sqrt(symbol)
uh, vh = np.fft.fftn(u), np.fft.fftn(v)
ut = np.fft.ifftn(np.cos(omega*t)*uh + t*np.sinc(omega*t/np.pi)*vh).real.ravel()
vt = np.fft.ifftn(-omega*np.sin(omega*t)*uh + np.cos(omega*t)*vh).real.ravel()
def energy(x, y):
    return .5*(y @ y + x @ (L @ x))
e0 = energy(u.ravel(), v.ravel())
e1 = energy(ut, vt)
# Same eigenvalues, different physical input/output maps: spectra are insufficient.
K1 = np.diag([1., 4.])
R = np.array([[1., -1.], [1., 1.]])/np.sqrt(2.)
K2 = R @ K1 @ R.T
b = np.array([1., 0.])
compliance = [float(b @ np.linalg.solve(K, b)) for K in (K1, K2)]
metrics = {
    'symmetry_max_abs': float(abs(L-L.T).max()),
    'row_sum_max_abs': float(np.max(np.abs(L @ np.ones(size)))),
    'fourier_mode_max_abs': max(mode_errors),
    'heat_sparse_fft_max_abs': float(np.max(np.abs(heat_sparse-heat_fft))),
    'heat_mass_abs_error': float(abs(heat_kernel.sum()-1)),
    'heat_kernel_min': float(heat_kernel.min()),
    'wave_relative_energy_error': float(abs(e1-e0)/e0),
    'zero_eigenvalue_count': int(np.count_nonzero(symbol < TOL)),
    'spectral_min': float(symbol.min()), 'spectral_max': float(symbol.max()),
    'first_positive_eigenvalue': float(np.min(symbol[symbol > TOL])),
    'isospectral_static_compliance': compliance,
    'isospectral_eigenvalue_max_error': float(np.max(np.abs(np.linalg.eigvalsh(K1)-np.linalg.eigvalsh(K2)))),
}
checks = {
    'symmetric': metrics['symmetry_max_abs'] < TOL,
    'constant_null_mode': metrics['row_sum_max_abs'] < TOL,
    'fourier_eigenpairs': metrics['fourier_mode_max_abs'] < TOL,
    'independent_heat_evolution': metrics['heat_sparse_fft_max_abs'] < TOL,
    'heat_preserves_mass': metrics['heat_mass_abs_error'] < TOL,
    'heat_positive': metrics['heat_kernel_min'] >= -TOL,
    'wave_energy': metrics['wave_relative_energy_error'] < TOL,
    'single_zero_mode': metrics['zero_eigenvalue_count'] == 1,
    'spectrum_in_0_12': metrics['spectral_min'] >= -TOL and abs(metrics['spectral_max']-12) < TOL,
    'isospectral_different_response': metrics['isospectral_eigenvalue_max_error'] < TOL and abs(compliance[0]-compliance[1]) > .3,
}
print(json.dumps({
    'status': 'PASS' if all(checks.values()) else 'FAIL',
    'scope': 'Dimensionless graph and toy linear-system benchmark only; no material calibration.',
    'source': {'repository': 'atlaslattice/manus-artifacts',
        'revision': '3c9cbcbd4c7c76b75d090fbfc627d452f4cb1fa6',
        'path': 'archive/math/RAINBOW_YINYANG_LATTICE_MATH_REFINEMENT_v2.2_CANDIDATE_2026-05-20.md',
        'git_blob': 'b2d8897ea84c8d6b21c706d3859d61402d594e7c'},
    'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
    'parameters': {'N': N, 'seed': SEED, 'tolerance': TOL, 'heat_time': heat_time, 'wave_time': t},
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'metrics': metrics, 'checks': checks,
}, indent=2, allow_nan=False))
raise SystemExit(0 if all(checks.values()) else 1)
