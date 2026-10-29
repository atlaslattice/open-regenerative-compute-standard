"""Noise-aware local linear identifiability. Synthetic use, no physical calibration."""
import numpy as np


def whiten(design, covariance, scales):
    J, C, scales = (np.asarray(a, dtype=float) for a in (design, covariance, scales))
    if J.ndim != 2 or min(J.shape) == 0 or C.shape != (J.shape[0], J.shape[0]) or scales.shape != (J.shape[1],):
        raise ValueError('Dimension mismatch')
    if not all(np.isfinite(a).all() for a in (J, C, scales)) or np.any(scales <= 0):
        raise ValueError('Finite inputs and positive parameter scales required')
    if not np.allclose(C, C.T, rtol=1e-12, atol=1e-14):
        raise ValueError('Covariance must be symmetric')
    try:
        L = np.linalg.cholesky(C)
    except np.linalg.LinAlgError as exc:
        raise ValueError('Covariance must be positive definite; singular support needs a separate model') from exc
    return np.linalg.solve(L, J * scales), L


def diagnose(design, covariance, scales):
    W, _ = whiten(design, covariance, scales)
    _, s, Vt = np.linalg.svd(W, full_matrices=True)
    n = W.shape[1]
    cutoff = max(W.shape) * np.finfo(float).eps * (s[0] if len(s) else 0)
    rank = int(np.count_nonzero(s > cutoff))
    full = rank == n
    scaled_cov = (Vt.T * (1/s**2)) @ Vt if full else None
    return {'rank':rank, 'parameter_count':n, 'rank_cutoff':float(cutoff),
        'singular_values':s.tolist(),
        'condition_number':float(s[0]/s[-1]) if full else None,
        'condition_status':'finite' if full else 'rank_deficient',
        'scaled_parameter_sd':np.sqrt(np.diag(scaled_cov)).tolist() if full else None,
        'weakest_scaled_direction':Vt[-1].tolist(),
        'null_scaled_directions':Vt[rank:].tolist(),
        'scope':'local linear Gaussian likelihood, no priors; not a calibration acceptance decision'}


def fit(design, covariance, observations, scales):
    W, L = whiten(design, covariance, scales)
    y = np.asarray(observations, float)
    if y.shape != (W.shape[0],) or not np.isfinite(y).all():
        raise ValueError('Observation mismatch')
    U, s, Vt = np.linalg.svd(W, full_matrices=False)
    cutoff = max(W.shape)*np.finfo(float).eps*s[0]
    if len(s) < W.shape[1] or np.any(s <= cutoff):
        raise ValueError('Unidentifiable parameters: do not return a unique estimate')
    theta = np.asarray(scales) * (Vt.T @ ((U.T @ np.linalg.solve(L,y))/s))
    scaled_cov = (Vt.T * (1/s**2)) @ Vt
    cov = scaled_cov * np.outer(scales, scales)
    residual = np.linalg.solve(L, y-np.asarray(design)@theta)
    return theta, cov, float(residual@residual)


def experiments(seed=20261028, repetitions=2000):
    rng = np.random.default_rng(seed)
    x = np.linspace(-1, 1, 9)
    sigma, common = .1, .2
    C = sigma**2*np.eye(len(x)) + common**2*np.ones((len(x),len(x)))
    J = np.column_stack([np.ones(len(x)), x])
    near = np.column_stack([np.ones(len(x)), .001*x])
    truth = np.array([1., .5])
    # Independent generative errors: one calibration draw per whole experiment,
    # plus independent row noise. Not a draw from the fitter's Cholesky factor.
    noise = sigma*rng.normal(size=(repetitions,len(x))) + common*rng.normal(size=(repetitions,1))
    ys = J@truth + noise
    estimates = np.array([fit(J,C,y,[1,1])[0] for y in ys])
    # Independent scalar oracle for the symmetric, equally weighted design.
    oracle = np.column_stack([ys.mean(axis=1), (ys@x)/(x@x)])
    oracle_cov = np.diag([common**2+sigma**2/len(x), sigma**2/(x@x)])
    sd = np.sqrt(np.diag(oracle_cov))
    coverage = np.mean(np.abs(estimates-truth) <= 1.959963984540054*sd, axis=0)
    bias = np.mean(estimates-truth, axis=0)
    # Deliberate misspecification: an unmodeled quadratic term biases intercept.
    discrepant = np.array([fit(J,C,y+.5*x*x,[1,1])[0] for y in ys])
    bad_coverage = np.mean(np.abs(discrepant-truth) <= 1.959963984540054*sd, axis=0)
    nominal_cov = fit(J,C,ys[0],[1,1])[1]
    # Alternate justified-or-not assumptions are reported, not silently selected.
    wrong_sd = np.sqrt(np.diag(fit(J,np.diag(np.diag(C)),ys[0],[1,1])[1]))
    # Weak-design Gaussian zero-centered slope priors: disclose posterior dependence.
    weak_cov = fit(near,C,near@truth,[1,1])[1]
    weak_var = weak_cov[1,1]
    priors = [{'slope_prior_sd':p, 'posterior_slope_mean':float(truth[1]/(1+weak_var/p**2)),
               'posterior_slope_sd':float(np.sqrt(1/(1/weak_var+1/p**2)))} for p in (.1,1.,10.)]
    return {
        'seed':seed, 'repetitions':repetitions,
        'assumptions':{'model':'y = intercept + slope*x', 'independent_sd':sigma,
            'shared_offset_sd':common, 'parameter_scales':[1,1], 'truth':truth.tolist(),
            'discrepancy':'add 0.5*x^2; fitter remains linear',
            'cost':'nine unit-cost measurements in each design; no facility cost claim'},
        'wide_design':diagnose(J,C,[1,1]), 'narrow_design':diagnose(near,C,[1,1]),
        'degenerate_design':diagnose(np.ones((len(x),2)),C,[1,1]),
        'oracle_max_abs_error':float(np.max(np.abs(estimates-oracle))),
        'oracle_covariance_max_abs_error':float(np.max(np.abs(nominal_cov-oracle_cov))),
        'nominal_95pct_coverage':coverage.tolist(), 'bias':bias.tolist(),
        'coverage_binomial_se':float(np.sqrt(.95*.05/repetitions)),
        'bias_standard_error':(sd/np.sqrt(repetitions)).tolist(),
        'misspecified_95pct_coverage':bad_coverage.tolist(),
        'misspecified_bias':np.mean(discrepant-truth,axis=0).tolist(),
        'correct_parameter_sd':sd.tolist(), 'incorrect_independent_systematic_parameter_sd':wrong_sd.tolist(),
        'weak_design_prior_sensitivity':priors,
        'interpretation':'Rank does not imply adequate precision. Priors and discrepancy can dominate. No physical measurements or acceptance threshold are asserted.'}
