"""Sampled observation policy, not proof of saturation or laser interlock."""
import math
from datetime import datetime


def num(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite numeric input required')
    return float(x)


def evaluate(a):
    for key in ['attempt_id','attempt_start_utc','acoustic_configuration_id','specimen','mode','arm','evidence','sensor_calibration_ids','criteria','hold_s','timeout_s','max_sample_gap_s','observations','subsequent_outcomes']:
        if key not in a:raise ValueError('missing '+key)
    if not a['attempt_id'] or not a['acoustic_configuration_id']:raise ValueError('attempt and acoustic configuration IDs required')
    stamp=datetime.fromisoformat(a['attempt_start_utc'].replace('Z','+00:00'))
    if stamp.utcoffset() is None or stamp.utcoffset().total_seconds()!=0:raise ValueError('UTC attempt start required')
    if a['mode'] not in {'UNTIL_READY','FIXED_DURATION'}:raise ValueError('unknown readiness mode')
    if a['arm'] not in {'REFERENCE','OFF','SHAM','ON'}:raise ValueError('unknown control arm')
    if a['evidence'] not in {'SYNTHETIC_TEST','EXPERIMENTAL_RAW'}:raise ValueError('explicit observation provenance required')
    for key in ['specimen_id','batch_id','material','composition','geometry','support']:
        if not a['specimen'].get(key):raise ValueError('specimen metadata required: '+key)
    if not a['sensor_calibration_ids']:raise ValueError('sensor/calibration identities required')
    hold,timeout,gap=[num(a[k]) for k in ['hold_s','timeout_s','max_sample_gap_s']]
    if min(hold,timeout,gap)<=0 or hold>timeout:raise ValueError('invalid readiness timing')
    criteria=a['criteria'];names=[x['metric'] for x in criteria]
    if not names or len(set(names))!=len(names):raise ValueError('unique explicit criteria required')
    for c in criteria:
        if not c.get('unit') or not c.get('sensor_id') or c['sensor_id'] not in a['sensor_calibration_ids']:raise ValueError('criterion sensor/unit missing')
        if num(c['minimum'])>num(c['maximum']):raise ValueError('inverted criterion bounds')
    obs=a['observations']
    if not obs:raise ValueError('observation trace required')
    times=[num(x['time_s']) for x in obs]
    if times[0]!=0 or any(y<=x for x,y in zip(times,times[1:])):raise ValueError('trace must start at zero and increase strictly')
    for row in obs:
        if num(row['driver_power_W'])<0:raise ValueError('negative driver wall power')
        for c in criteria:
            if row['metrics'].get(c['metric']) is not None:num(row['metrics'][c['metric']])
    if a['mode']=='FIXED_DURATION':
        deadline=num(a['fixed_duration_s'])
        if deadline<=0 or deadline>timeout:raise ValueError('invalid fixed duration')
    else:deadline=timeout
    abort=a.get('abort_at_s')
    if abort is not None:
        abort=num(abort)
        if abort<0 or not a.get('abort_reason'):raise ValueError('explicit abort time/reason required')
    stop=min(deadline,abort if abort is not None else deadline)
    first=None;qualified_since=None;ready=None;history=[];gaps=[]
    for i,row in enumerate(obs):
        t=row['time_s']
        if t>stop:break
        if i and t-times[i-1]>gap:
            qualified_since=None;gaps.append({'from_s':times[i-1],'to_s':t})
        failed=[c['metric'] for c in criteria if row['metrics'].get(c['metric']) is None or not c['minimum']<=row['metrics'][c['metric']]<=c['maximum']]
        if failed:qualified_since=None
        else:
            if first is None:first=t
            if qualified_since is None:qualified_since=t
            if t-qualified_since>=hold and ready is None:ready=t
        history.append({'time_s':t,'qualifies':not failed,'stage':'SETTLING' if not failed else 'PREPARING','failed_or_missing_metrics':failed,'qualifying_window_start_s':qualified_since})
        if a['mode']=='UNTIL_READY' and ready is not None:break
    if a['mode']=='UNTIL_READY' and ready is not None and (abort is None or ready<abort):
        end=ready;status='READY_IN_TRACE'
    elif abort is not None and abort<=deadline:
        end=abort;status='ABORTED'
    elif times[-1]<deadline:
        end=times[-1];status='INCOMPLETE_TRACE'
    else:
        end=deadline;status='TIMEOUT_NOT_READY' if a['mode']=='UNTIL_READY' else 'FIXED_WINDOW_COMPLETED'
    # Trapezoidal measured power integral, interpolate only between supplied samples.
    energy=0.
    for l,r in zip(obs,obs[1:]):
        if l['time_s']>=end:break
        dt=min(end,r['time_s'])-l['time_s']
        if dt<=0:continue
        fraction=dt/(r['time_s']-l['time_s'])
        pend=l['driver_power_W']+fraction*(r['driver_power_W']-l['driver_power_W'])
        energy+=dt*(l['driver_power_W']+pend)/2
    if end>times[-1]:energy=None
    return {'attempt_id':a['attempt_id'],'attempt_start_utc':a['attempt_start_utc'],'acoustic_configuration_id':a['acoustic_configuration_id'],'mode':a['mode'],'arm':a['arm'],'evidence':a['evidence'],
            'status':status,'first_qualifying_sample_s':first,'first_confirmed_readiness_s':ready,
            'attempt_end_s':end,'driver_wall_energy_J':energy,'observation_gaps':gaps,'criterion_history':history,
            'laser_trigger':'NONE_NO_HARDWARE_INTERFACE',
            'scope':'sampled readiness policy; not proof of full saturation or fusion benefit',
            'sensor_evidence':'caller metadata, not independent sensor validation',
            'fixed_window_note':'first readiness may not persist to fixed-window end; inspect history',
            'power_scope':'driver wall energy only; sparse power interpolation may miss variation',
            'subsequent_outcomes':a['subsequent_outcomes']}


def batch(attempts):
    if not attempts or len({a['attempt_id'] for a in attempts})!=len(attempts):raise ValueError('nonempty unique attempts required')
    results=[evaluate(a) for a in attempts]
    times=[r['first_confirmed_readiness_s'] for r in results if r['status']=='READY_IN_TRACE']
    return {'attempts':results,'summary':{'all_attempts':len(results),'ready_attempts':sum(r['status']=='READY_IN_TRACE' for r in results),
            'status_counts':{s:sum(r['status']==s for r in results) for s in sorted({r['status'] for r in results})},
            'readiness_times_s_conditional_on_ready':times,'note':'timeouts/aborts retained; conditional times are not an unbiased comparison of different policies'}}
