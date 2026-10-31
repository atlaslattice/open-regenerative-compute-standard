# Retained failures and qualification limits

1. Python package lookup did not find a warpx distribution in the configured pip
   index. Reused the documented conda environment instead. This is not evidence
   that WarpX cannot be installed or does not apply to laser experiments.
2. Initial orbit input combined periodic field boundaries with absorbing particle
   boundaries. WarpX rejected it before physics evolution. RUN.log and Backtrace
   are preserved in receipts/uniform_dt001; original inputs and generator remain.
   Corrected input version uses PEC zero-self-field boundaries and absorbing
   particles; prescribed analytic B remains a separate external source.
3. Upstream file recovery wrapper appended one terminal newline to seven files.
   No numerical setting changed, but exact blob identity failed. Original wrapper
   copies and correction hashes are preserved. Canonical upstream3d002 reran
   exact original blobs and passed exact original analysis. This source correction
   does not attest the conda binary's embedded source revision (Unknown).
4. ORBIT_ANALYSIS001 failed its 2% mirror momentum-error checks: coarse loss-cone
   9.95%, reflected8.30%, and half-step reflected2.08%. No tolerance relaxed.
   Additional dt=.05ns runs reduce errors to .630% and .519%; the original failures
   remain in ORBIT_ANALYSIS002/003. Good energy conservation had not exposed phase
   error. Reflecting turning-point convergence alone would also miss it.
5. Independent ODE reference is not an independent experimental measurement.
   Relativistic equations, masses and prescribed field are common assumptions.
   Uniform analytic-helix comparison and timestep convergence provide additional
   checks, not complete validation of arbitrary fields or actual coils.
6. Native 2D and two-MPI-rank upstream configurations were not executed. Hardware,
   thread layout and random defaults can change Monte Carlo realizations. Repeat
   summaries match here; no promise of cross-machine bitwise equality is made.
7. A saved summary of default-state pB tests is not a laser-source spectrum. No
   acoustic state, actual pocket geometry, target stopping, detector correction,
   usable recovery or net-electric result is generated in this release.
