"""Deterministic weighted proton handoffs and conditional primary-particle ledger.
Not a plasma solver, PRISM model, full apparatus or alpha phase-space generator.
"""
from pathlib import Path
import copy,hashlib,importlib.util,json,math
ROOT=Path(__file__).resolve().parent
MEV_J=1.602176634e-13

def number(x,lo=None,hi=None):
    if isinstance(x,bool) or not isinstance(x,(float,int)) or not math.isfinite(x) or (lo is not None and x<lo) or (hi is not None and x>hi):raise ValueError('Finite numeric input outside allowed range')
    return float(x)

def backend():
    for r in json.loads((ROOT/'DEPENDENCY_LOCK.json').read_text()):
        if hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()!=r['sha256']:raise ValueError('Dependency identity mismatch: '+r['path'])
    spec=importlib.util.spec_from_file_location('handoff_previous_physics',ROOT.parent/'coupled_reference_v0_5/physics.py')
    p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
    m,t=p.load_model()
    coordinate=p.Coordinate(lambda e:m.stopping(t,model='srim13',projectile='proton',material='B11',E_MeV=e,bn_electronic_multiplier=None,nuclear_variant='ZBL_SIMNRA_7_04')['total_eV_cm2_per_average_atom'],m.PROJECTILES['proton'][1]/1000,3.8)
    rows=json.loads((ROOT.parent/'coupled_reference_v0_5/EVENT_CROSS_SECTIONS.json').read_text())
    mass=json.loads((ROOT.parent/'coupled_reference_v0_5/MASS_SOURCE.json').read_text())
    mb=mass['B11_atomic_mass_u']*mass['atomic_mass_unit_MeV']-5*mass['electron_MeV']+sum(mass['B_electron_binding_components_eV'])*1e-6
    q=mass['proton_MeV']+mb-3*mass['alpha_MeV']
    return p,coordinate,rows,q

class Engine:
    def __init__(self):self.p,self.coordinate,self.rows,self.q=backend()
    def slab(self,packet,stage,targets):
        if stage['material']!='B11' or stage['target_state']!='COLD_ELEMENTAL':raise ValueError('This adapter cannot transfer its stopping model to BN, other isotopes or plasma')
        column=number(stage['normal_atoms_cm2'],0);area=number(stage['illuminated_area_cm2'],1e-300)
        n=stage['depth_cells']
        if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=4096:raise ValueError('Invalid integration cell count')
        normal=stage['unit_normal_LAB'];unit(normal)
        mu=abs(sum(a*b for a,b in zip(normal,packet['unit_direction_LAB'])))
        if mu<1e-10:raise ValueError('Grazing geometry needs a finite lateral target model')
        path=column/mu;e=packet['kinetic_MeV'];w=packet['weight'];end=self.coordinate.outgoing(e,path)
        if end is None:raise ValueError('Positive stopping-model floor reached: remaining energy is unresolved, not zero')
        # Validate the kernel domain even at zero probability/column.
        if stage['reaction_model'] not in ('PUBLICATION_EVENT_MODEL','REACTIONS_OFF_CONTROL'):raise ValueError('An explicitly typed event kernel or OFF control is required')
        on=stage['reaction_model']=='PUBLICATION_EVENT_MODEL'
        if on:self.p.sigma(self.rows,e);self.p.sigma(self.rows,end)
        identity=stage['physical_instance_id'];spec=(stage['material'],stage['target_state'],column,area)
        if identity in targets and targets[identity]['spec']!=spec:raise ValueError('One physical target cannot have inconsistent inventories')
        targets.setdefault(identity,{'spec':spec,'initial_B11_atoms':column*area,'consumed_B11_atoms':0.})
        fraction=number(stage['maximum_allowed_depletion_fraction'],0,1)
        reactions=loss=alpha=0.;cells=[]
        for j in range(n):
            mid=self.coordinate.outgoing(e,path*(j+.5)/n);next_e=self.coordinate.outgoing(e,path*(j+1)/n)
            start_e=self.coordinate.outgoing(e,path*j/n)
            loss+=w*(start_e-mid)
            sigma=self.p.sigma(self.rows,mid) if on else 0.
            born=w*(-math.expm1(-sigma*1e-24*path/n));reactions+=born
            alpha+=born*(mid+self.q);w-=born
            loss+=w*(mid-next_e)
            cells.append({'cell':j,'local_proton_LAB_MeV':mid,'expected_events':born,'expected_alpha_birth_kinetic_MeV':born*(mid+self.q)})
        targets[identity]['consumed_B11_atoms']+=reactions
        if targets[identity]['consumed_B11_atoms']>targets[identity]['initial_B11_atoms']*fraction:raise ValueError('Target depletion exceeds declared dilute-target approximation; evolving target model required')
        out=copy.deepcopy(packet);out['weight']=w;out['kinetic_MeV']=end;out['position_time_status']='SOURCE_TAGS_NOT_PROPAGATED'
        return out,dict(events=reactions,nuclear_Q_MeV=reactions*self.q,alpha_birth_kinetic_MeV=alpha,material_transfer_MeV=loss,external_work_MeV=0.,escaped_protons=0.,escaped_proton_kinetic_MeV=0.,cells=cells)

    def stage(self,packet,s,targets):
        for k in ('stage_id','physical_instance_id','evidence'):
            if not s.get(k):raise ValueError('Explicit stage, physical instance and evidence required')
        typ=s['type'];out=copy.deepcopy(packet);out['position_time_status']='SOURCE_TAGS_NOT_PROPAGATED'
        row=dict(events=0.,nuclear_Q_MeV=0.,alpha_birth_kinetic_MeV=0.,material_transfer_MeV=0.,external_work_MeV=0.,escaped_protons=0.,escaped_proton_kinetic_MeV=0.,cells=[])
        if typ=='cold_b11_slab':return self.slab(packet,s,targets)
        if typ=='specified_field_work':
            work=number(s['work_on_each_proton_MeV']);end=packet['kinetic_MeV']+work
            if end<0:raise ValueError('Field extraction exceeds proton kinetic energy')
            out['kinetic_MeV']=end;row['external_work_MeV']=packet['weight']*work
            row['scope']='Prescribed longitudinal work; not a solved field or a wall-plug efficiency'
        elif typ=='adiabatic_mirror_boundary':
            R=number(s['mirror_ratio'],1);V=number(s['throat_potential_energy_rise_MeV'],0);E=number(packet['kinetic_MeV'],1e-300)
            if s['axis_LAB']!=[0,0,1]:raise ValueError('This analytic boundary only supports LAB z axis')
            u=packet['unit_direction_LAB'][2];critical=1-1/R+V/(R*E)
            if abs(u*u-critical)<1e-12:raise ValueError('Separatrix transit is unresolved; do not assign a finite escape time')
            escape=u*u>critical
            if escape:
                out['weight']=0.;row['external_work_MeV']=-packet['weight']*V
                row['escaped_protons']=packet['weight'];row['escaped_proton_kinetic_MeV']=packet['weight']*(E-V)
            else:out['unit_direction_LAB'][2]*=-1
            row['mirror_outcome']='ESCAPED_AT_THROAT' if escape else 'REFLECTED_RETURN_TO_MIDPLANE'
            row['scope']='Collisionless adiabatic endpoint classification only; no isotropic reset, finite orbit, recirculation time or PRISM calibration'
        else:raise ValueError('Unsupported stage type; missing adapters are not ideal elements')
        return out,row

    def attempt(self,a,stages):
        if a['source_packets'] is None:return dict(attempt_id=a['attempt_id'],status='MISSING_SOURCE_OUTCOME',metrics=None,stage_records=[])
        if a['source_frame']!='LAB' or a['source_energy_unit']!='MeV':raise ValueError('Explicit LAB kinetic energy in MeV required')
        if not a.get('source_evidence'):raise ValueError('Source provenance required')
        packets=copy.deepcopy(a['source_packets']);ids=set()
        for p in packets:
            if p['packet_id'] in ids:raise ValueError('Duplicate source packet ID')
            ids.add(p['packet_id']);number(p['weight'],0);number(p['kinetic_MeV'],0)
            unit(p['unit_direction_LAB']);vector(p['position_m']);number(p['time_s'],0)
            if p['species']!='proton':raise ValueError('This adapter transports protons; alpha aggregates cannot masquerade as phase-resolved packets')
        source_count=number(sum(p['weight'] for p in packets),0);beam=number(sum(p['weight']*p['kinetic_MeV'] for p in packets),0)
        totals={k:0. for k in ('events','nuclear_Q_MeV','alpha_birth_kinetic_MeV','material_transfer_MeV','external_work_MeV','escaped_protons','escaped_proton_kinetic_MeV')}
        records=[];targets={};stage_ids=set()
        try:
            for s in stages:
                if s['stage_id'] in stage_ids:raise ValueError('Duplicate stage ID; repeated physical visits need unique visit IDs')
                stage_ids.add(s['stage_id'])
                next_packets=[]
                for p in packets:
                    if p['weight']==0:next_packets.append(p);continue
                    out,row=self.stage(p,s,targets)
                    for k in totals:totals[k]=number(totals[k]+row[k])
                    number(out['weight'],0);number(out['kinetic_MeV'],0)
                    records.append({'stage_id':s['stage_id'],'physical_instance_id':s['physical_instance_id'],'packet_id':p['packet_id'],'input':p,'output':out,'ledger':row})
                    next_packets.append(out)
                packets=next_packets
        except ValueError as exc:
            return dict(attempt_id=a['attempt_id'],status='BLOCKED_MODEL_DOMAIN_OR_ADAPTER',reason=str(exc),metrics=None,stage_records=records)
        remaining=sum(p['weight'] for p in packets);kinetic=sum(p['weight']*p['kinetic_MeV'] for p in packets)
        particle=source_count-totals['events']-totals['escaped_protons']-remaining
        energy=beam+totals['nuclear_Q_MeV']+totals['external_work_MeV']-totals['alpha_birth_kinetic_MeV']-totals['material_transfer_MeV']-totals['escaped_proton_kinetic_MeV']-kinetic
        number(particle);number(energy)
        if abs(particle)>1e-10*max(1.,source_count) or abs(energy)>1e-10*max(1.,beam,totals['alpha_birth_kinetic_MeV']):raise ValueError('Conservation gate failed')
        metrics=dict(**totals,source_protons=source_count,source_proton_kinetic_MeV=beam,remaining_protons=remaining,remaining_proton_kinetic_MeV=kinetic,expected_alpha_births=3*totals['events'],expected_B11_consumed=totals['events'],particle_residual=particle,energy_residual_MeV=energy,wall_input_J=a['wall_input_J'],load_electricity_J=None,net_electricity_J=None,physical_success=a['physical_success'])
        return dict(attempt_id=a['attempt_id'],status='CONDITIONAL_HANDOFF_COMPLETE',metrics=metrics,stage_records=records,remaining_packets=packets,target_ledgers=targets,alpha_output_status='COUNT_AND_TOTAL_BIRTH_KINETIC_ONLY_NO_PHASE_SPACE_OR_RECOVERY')

def vector(v):
    if not isinstance(v,list) or len(v)!=3:raise ValueError('Explicit finite three-vector required')
    for x in v:number(x)

def unit(v):
    vector(v)
    if not math.isclose(sum(x*x for x in v),1.,abs_tol=1e-12,rel_tol=0):raise ValueError('Direction/normal must be a unit vector')

def execute(c):
    if c['schema']!='stellar-forge-handoff/0.1':raise ValueError('Wrong handoff schema')
    registry=json.loads((ROOT.parent/'abc_architecture_v0_1/ABC_REGISTRY.json').read_text())
    if c['architecture_id'] not in {x['id'] for x in registry['configurations']}:raise ValueError('Unknown architecture ID')
    if c['run_class']=='INCOMPLETE_APPARATUS_PROFILE':return {'architecture_id':c['architecture_id'],'status':'BLOCKED_UNSPECIFIED_APPARATUS_INPUTS','blockers':c['unresolved_inputs'],'metrics':None,'attempts':[]}
    if c['run_class']!='CONDITIONAL_INTERFACE_BENCHMARK_NOT_APPARATUS':raise ValueError('No calibrated or full apparatus run class implemented')
    if c['target_inventory_scope']!='FRESH_TARGET_PER_ATTEMPT_ASSUMED':raise ValueError('This version requires explicit fresh-target-per-attempt assumption; replacement costs are not zero')
    if c['geometry_scope']!='PRESCRIBED_SEQUENCE_NOT_SPATIAL_TRAJECTORY':raise ValueError('No finite-geometry trajectory or flight-time adapter implemented')
    attempts=c['attempts'];seen=set()
    if not attempts:raise ValueError('Nonempty all-attempt records required')
    for a in attempts:
        if not a['attempt_id'] or a['attempt_id'] in seen:raise ValueError('Unique attempt IDs required')
        seen.add(a['attempt_id'])
        for k in ('ready','fired','physical_success'):
            if a[k] is not None and type(a[k]) is not bool:raise ValueError('Attempt outcomes must be bool or missing')
        if a['wall_input_J'] is not None:number(a['wall_input_J'],0)
        if a['fired'] is False and a['source_packets']:raise ValueError('A recorded nonfiring attempt cannot contain emitted protons')
        number(a['preparation_time_s'],0)
    engine=Engine();out=[engine.attempt(a,c['stages']) for a in attempts]
    known=[x for x in out if x['metrics'] is not None];complete=len(known)==len(attempts)
    subtotal=sum(x['metrics']['events'] for x in known)
    successes=[a['physical_success'] for a in attempts]
    return dict(architecture_id=c['architecture_id'],status='CONDITIONAL_HANDOFF_COMPLETE' if complete else 'INCOMPLETE_ALL_ATTEMPT_RESULTS',run_class=c['run_class'],attempt_count=len(attempts),attempts_with_complete_particle_ledger=len(known),expected_events_all_attempts=subtotal if complete else None,known_attempt_event_subtotal=subtotal,physical_success_probability=sum(successes)/len(successes) if all(x is not None for x in successes) else None,preparation_time_sum_s=sum(a['preparation_time_s'] for a in attempts),wall_input_all_attempts_J=sum(a['wall_input_J'] for a in attempts) if all(a['wall_input_J'] is not None for a in attempts) else None,attempts=out,expected_recovered_electricity_J=None,net_wall_plug_J=None,spatial_flight_time_and_jitter_evolution='NOT_MODELED',stopping_loss_is_recoverable_heat=False,uncertainty='NOT_PROPAGATED; expected weights are not measured shot counts or physical shot noise')
