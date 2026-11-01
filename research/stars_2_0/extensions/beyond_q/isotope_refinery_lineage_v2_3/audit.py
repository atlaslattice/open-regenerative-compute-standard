"""Normalization and recovery-boundary audit, not a reactor simulation.

Python standard library only. Never writes to the parent fuel-cycle package.
Run python audit.py; python -m unittest -v test_audit.py.
"""
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def fraction(value):
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError('fraction must be finite and in [0,1]')
    return value


def gross_liters(p, exposure):
    """MW -> J/s -> primary DD events -> He3 atoms -> mol -> STP L/year."""
    fraction(exposure)
    branch = fraction(p['He3_branch_fraction_assumed'])
    if p['primary_DD_MW'] < 0 or p['mean_primary_DD_MeV'] <= 0:
        raise ValueError('invalid power or reaction energy')
    events = p['primary_DD_MW'] * 1e6 / (p['mean_primary_DD_MeV'] * p['joules_per_MeV'])
    return events * branch * p['days_per_year'] * 86400 * exposure / p['avogadro_per_mol'] * p['molar_volume_STP_L']


def product_ledger(born, *, overall=None, stages=None):
    """Mutually exclusive overall and explicit sequential stage bookkeeping.

    Stages is an ordered mapping of stage name to surviving fraction. Fractions
    must be conditional on the previous stage, not duplicate birth-based rates.
    Returned losses are amounts removed at each stage, in the input atom/mass/
    volume unit. These are scenario arithmetic, not equipment performance.
    """
    if not math.isfinite(born) or born < 0:
        raise ValueError('nonnegative finite birth required')
    if (overall is None) == (stages is None):
        raise ValueError('choose overall OR stages exactly once')
    factors = {'overall_lumped': overall} if overall is not None else stages
    remaining = born
    losses = {}
    for name, value in factors.items():
        surviving = remaining * fraction(value)
        losses[name] = remaining - surviving
        remaining = surviving
    return {'born': born, 'product_candidate': remaining, 'losses': losses,
            'closure_residual': born - remaining - sum(losses.values())}


def decay_comparator(p):
    """Empty aging store, constant net T addition, no withdrawal or other loss.

    He3 daughter mass uses molar mass ratio; T removed by decay cannot also fuel B.
    Company target is used as an illustrative flow condition, not calibration.
    """
    lam = math.log(2) / p['T_half_life_years']
    ratio = p['He3_molar_mass_g'] / p['T_molar_mass_g']
    he_flow = p['Kronos_He3_flow_kg_year_company_projection']
    t_feed = p['Kronos_T_input_kg_year_illustration']
    target_t_decay = he_flow / ratio
    inventory = target_t_decay / lam
    years = -math.log1p(-target_t_decay / t_feed) / lam
    return {'assumed_net_T_feed_kg_year': t_feed, 'target_He3_flow_kg_year': he_flow,
            'required_T_aging_inventory_kg': inventory, 'empty_store_years_to_target_flow': years,
            'first_year_He3_mass_kg': ratio * t_feed * (1 - (-math.expm1(-lam)) / lam),
            'boundary': 'Illustrative constant net feed, zero initial inventory; not reconstruction of Kronos design',
            'evidence': 'VERIFIED-DERIVED conditional arithmetic; company operating point UNRESOLVED'}


def main():
    p = json.loads((ROOT / 'inputs.json').read_text())
    rows = []
    for label, exposure in [('paste_85pct_effective', p['effective_exposure_paste']),
                            ('parent_expected_before_replacement', p['parent_macro_availability'] * p['parent_source_duty'])]:
        born = gross_liters(p, exposure)
        for recovery in p['overall_recovery_cases_assumed']:
            ledger = product_ledger(born, overall=recovery)
            rows.append({'case': label, 'effective_exposure': exposure, 'gross_He3_STP_L_year': born,
                         'overall_recovery_assumed': recovery, 'product_candidate_STP_L_year': ledger['product_candidate'],
                         'lumped_loss_STP_L_year': ledger['losses']['overall_lumped'],
                         'closure_residual_STP_L': ledger['closure_residual'],
                         'status': 'POTENTIAL-DERIVED; no separate secondary He3 burn; not qualified sales'})
    with (ROOT / 'normalization.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0]); writer.writeheader(); writer.writerows(rows)
    (ROOT / 'decay_comparator.json').write_text(json.dumps(decay_comparator(p), indent=2) + '\n')
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
              for name in ['inputs.json', 'audit.py', 'sources.json']}
    (ROOT / 'execution.json').write_text(json.dumps({'input_code_sha256': hashes, 'rows': len(rows),
        'transport_run': False, 'plasma_benchmark_reproduced': False, 'parent_physics_changed': False}, indent=2) + '\n')
    print(json.dumps({'rows': len(rows), 'paste_gross_STP_L_year': rows[0]['gross_He3_STP_L_year'],
                      'max_abs_closure_STP_L': max(abs(r['closure_residual_STP_L']) for r in rows)}, indent=2))


if __name__ == '__main__':
    main()
