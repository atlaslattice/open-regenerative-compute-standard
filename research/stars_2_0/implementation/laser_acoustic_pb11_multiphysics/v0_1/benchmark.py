"""Stellar Forge interface verification; no acoustic/fusion performance model."""
import argparse
import json
import math
from collections import defaultdict

WALL_CATEGORIES = ('laser', 'acoustic', 'magnets', 'rf_nbi', 'cooling',
                   'vacuum', 'target_handling', 'diagnostics', 'collector_bias', 'other')
ARMS = ('REF_OFF', 'REF_SHAM', 'REF_ON', 'POCKET_OFF', 'POCKET_SHAM', 'POCKET_ON')


def number(value, name, nonnegative=True):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name}: finite number required')
    if nonnegative and value < 0:
        raise ValueError(f'{name}: nonnegative value required')
    return value


def complete_sum(values):
    return None if any(v is None for v in values) else math.fsum(values)


def summarize(shots, threshold):
    """Success is nuclear-event count >= preregistered threshold, not optical proxy.

    Input rows are disjoint attempted shots, including aborted/failed attempts.
    Each numerical outcome is measured or derived as its row provenance states.
    Missing values remain None. No imputation or detector inversion is performed.
    """
    number(threshold, 'success_threshold_events')
    if threshold <= 0:
        raise ValueError('success threshold must be positive')
    groups = defaultdict(list)
    seen = set()
    for row in shots:
        sid = row['shot_id']
        if not isinstance(sid, str) or not sid or sid in seen:
            raise ValueError('unique nonempty shot_id required')
        seen.add(sid)
        if row['arm'] not in ARMS:
            raise ValueError('unknown arm')
        if row.get('apparatus_id') not in ('SF_A_NEW_HYBRID_V0_1', 'SF_B_COMBINED_HYBRID_V0_1', 'SF_C_ORIGINAL_STARS_V0_1'):
            raise ValueError('unknown pB apparatus identity')
        for key in ('campaign_id', 'batch_id', 'evidence_class', 'source_ref'):
            if not isinstance(row.get(key), str) or not row[key]:
                raise ValueError(f'{key} required')
        if row['evidence_class'] not in ('MEASURED', 'SOURCE_REPRODUCED', 'DERIVED', 'POTENTIAL_DERIVED', 'SYNTHETIC_FIXTURE'):
            raise ValueError('unknown evidence class')
        if row.get('event_semantics') not in ('REALIZED_COUNT', 'DRAWN_MODEL_COUNT', 'EXPECTED_POPULATION'):
            raise ValueError('explicit event semantics required')
        for key in ('fusion_events', 'alpha_birth_energy_J', 'alpha_escape_energy_J',
                    'detected_alpha_count', 'useful_electricity_J', 'elapsed_s'):
            value = row.get(key)
            if value is not None:
                number(value, key)
        if row.get('firing_time_error_s') is not None:
            number(row['firing_time_error_s'], 'firing_time_error_s', nonnegative=False)
        born, escaped = row.get('alpha_birth_energy_J'), row.get('alpha_escape_energy_J')
        if born is not None and escaped is not None and escaped > born + 1e-12 * max(born, escaped):
            raise ValueError('escape exceeds birth: post-birth field work needs a separate ledger')
        wall = row.get('wall_input_J')
        if not isinstance(wall, dict) or set(wall) != set(WALL_CATEGORIES):
            raise ValueError('explicit complete wall category keys required; unknown values use null')
        for key, value in wall.items():
            if value is not None:
                number(value, 'wall_' + key)
        groups[(row['apparatus_id'], row['arm'], row['evidence_class'], row['event_semantics'])].append(row)
    out = []
    for (apparatus, arm, evidence, semantics), rows in sorted(groups.items()):
        n = len(rows)
        known = [r for r in rows if r.get('fusion_events') is not None]
        classifiable = known if semantics != 'EXPECTED_POPULATION' else []
        successes = [r for r in classifiable if r['fusion_events'] >= threshold]
        failures = [r for r in classifiable if r['fusion_events'] < threshold]
        missing = n - len(classifiable)
        total = complete_sum([r.get('fusion_events') for r in rows])
        wall = complete_sum([complete_sum(list(r['wall_input_J'].values())) for r in rows])
        useful = complete_sum([r.get('useful_electricity_J') for r in rows])
        duration = complete_sum([r.get('elapsed_s') for r in rows])
        result = dict(apparatus_id=apparatus, arm=arm, evidence_class=evidence, event_semantics=semantics,
                      attempted_shots=n, known_outcomes=len(classifiable), missing_outcomes=missing,
                      known_event_totals=len(known), missing_event_totals=n-len(known),
                      successful_shots=len(successes), unsuccessful_shots=len(failures),
                      success_fraction=None if missing else len(successes)/n,
                      success_fraction_missing_data_bounds=[len(successes)/n, (len(successes)+missing)/n],
                      observed_event_sum=math.fsum(r['fusion_events'] for r in known),
                      total_fusion_events=total,
                      events_per_attempt=None if total is None else total/n,
                      events_per_success=None if not successes else math.fsum(r['fusion_events'] for r in successes)/len(successes),
                      events_per_unsuccessful_shot=None if not failures else math.fsum(r['fusion_events'] for r in failures)/len(failures),
                      wall_input_J=wall, useful_electricity_J=useful,
                      net_electricity_J=None if wall is None or useful is None else useful-wall,
                      elapsed_s=duration,
                      average_net_power_W=None if wall is None or useful is None or not duration else (useful-wall)/duration,
                      campaigns=sorted(set(r['campaign_id'] for r in rows)),
                      batches=sorted(set(r['batch_id'] for r in rows)))
        for key in ('alpha_birth_energy_J', 'alpha_escape_energy_J', 'detected_alpha_count'):
            result[key] = complete_sum([r.get(key) for r in rows])
        timing = [r['firing_time_error_s'] for r in rows if r.get('firing_time_error_s') is not None]
        result['timing_observed_n'] = len(timing)
        result['timing_missing_n'] = n-len(timing)
        result['observed_timing_bias_s'] = math.fsum(timing)/len(timing) if timing else None
        result['observed_timing_rms_s'] = math.sqrt(math.fsum(t*t for t in timing)/len(timing)) if timing else None
        result['observed_timing_population_sd_s'] = (math.sqrt(math.fsum((t-result['observed_timing_bias_s'])**2 for t in timing)/len(timing)) if timing else None)
        # This is descriptive accounting, not an iid causal uncertainty estimate.
        out.append(result)
    return out


def geometry_gaps(document):
    """Flat CAD parameter contract. No dimensions/materials are guessed."""
    if document.get('schema_version') != 'SF_GEOMETRY_0_1':
        raise ValueError('unsupported geometry schema')
    gaps = []
    for name, parameter in document['parameters'].items():
        if not isinstance(parameter.get('unit'), str) or not parameter['unit']:
            raise ValueError(f'{name}: unit required')
        value = parameter.get('value')
        if value is None:
            gaps.append(name)
            continue
        if not parameter.get('source_ref'):
            raise ValueError(f'{name}: source_ref required for resolved parameters')
        if isinstance(value, (float, int)) and not isinstance(value, bool):
            number(value, name)
        if parameter.get('status') == 'UNRESOLVED':
            raise ValueError(f'{name}: resolved value has unresolved status')
    # These critical fields cannot be removed to obtain a passing empty contract.
    required = {'pocket_inner_dimensions_m', 'pocket_wall_thickness_m', 'ceramic_composition',
                'boron_form', 'grain_size_distribution', 'packing_fraction', 'b11_fraction',
                'boron_areal_atoms_m2', 'acoustic_boundary_conditions', 'mechanical_damping',
                'laser_paths', 'mirror_layout', 'detector_acceptance', 'layer_stack',
                'shell_geometry', 'proton_source_phase_space', 'alpha_exit_apertures'}
    gaps.extend(sorted(required - set(document['parameters'])))
    return sorted(set(gaps))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode', choices=('geometry', 'shots'))
    p.add_argument('input')
    p.add_argument('--output', required=True)
    a = p.parse_args()
    from pathlib import Path
    dest = Path(a.output)
    if dest.exists():
        raise FileExistsError('append-only output must be new')
    doc = json.loads(Path(a.input).read_text())
    if a.mode == 'geometry':
        gaps = geometry_gaps(doc)
        result = {'status': 'BLOCKED_UNRESOLVED_GEOMETRY' if gaps else 'PARAMETERS_SUPPLIED_NOT_VALIDATED', 'unresolved_fields': gaps}
    else:
        result = {'status': 'DESCRIPTIVE_ACCOUNTING_ONLY', 'groups': summarize(doc['shots'], doc['success_threshold_events'])}
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('x') as f:
        json.dump(result, f, indent=2, allow_nan=False)
        f.write('\n')


if __name__ == '__main__':
    main()
