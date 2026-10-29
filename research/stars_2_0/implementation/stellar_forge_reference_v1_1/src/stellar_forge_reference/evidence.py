"""Dependency provenance; input evidence never certifies a derived model."""
def dependencies(nodes, output_id):
    maturity={'NOT_ASSESSED','SOURCE_TRACED','SOURCE_REPRODUCED','CALIBRATED','VALIDATED'}
    provenance={'EXPERIMENTAL_RAW','SOURCE_NORMALIZED','EVALUATED_EXTERNAL','MODEL_PREDICTION','PARAMETRIC_SCENARIO','SYNTHETIC_TEST'}
    if len({n['id'] for n in nodes})!=len(nodes):raise ValueError('duplicate evidence identity')
    index={n['id']:n for n in nodes};visited=set();active=set();ordered=[]
    def walk(key):
        if key not in index:raise ValueError('missing evidence dependency')
        if key in active:raise ValueError('evidence cycle')
        if key in visited:return
        n=index[key]
        if n['maturity'] not in maturity or n['provenance'] not in provenance:raise ValueError('invalid evidence metadata')
        active.add(key)
        for p in n['depends_on']:walk(p)
        active.remove(key);visited.add(key);ordered.append(n)
    walk(output_id)
    return {'output_id':output_id,'required_dependency_ids':[n['id'] for n in ordered],
            'scenario_dependencies':[n['id'] for n in ordered if n['provenance'] in {'PARAMETRIC_SCENARIO','SYNTHETIC_TEST'}],
            'component_evidence':ordered,'derived_physical_validation':'NOT_ESTABLISHED_BY_INPUT_MATURITY',
            'scope':'dependency metadata only; unknown numeric inputs still block physical prediction'}
