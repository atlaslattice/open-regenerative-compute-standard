"""Generate the new architecture mapping; historical sources and IDs are untouched."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
C=json.loads((R/'ORIGINAL_STARS_MODULE_COVERAGE.json').read_text())
modules=[m['id'] for m in C['retained_modules']]
registry={
 'schema':'stellar-forge-abc-architecture/0.1','date':'2026-10-30','source_commit':'60c3cb3cf2622fb63791f7d4b028b64269ac9f18','scientific_freeze':False,
 'direction':'Current project-lead A/B/C correction supersedes ambiguous shorthand, never the contents or claims of old runs.',
 'original_inventory':{'path':'ORIGINAL_STARS_MODULE_COVERAGE.json','sha256':hashlib.sha256((R/'ORIGINAL_STARS_MODULE_COVERAGE.json').read_bytes()).hexdigest(),'source_commit':'b8687d7945fa5ef62362f1c7f15f85e1fa036bf9','source_path':'research/stars_2_0/implementation/reference_evidence_v0_10/MODULE_COVERAGE.json'},
 'third_finding':{'status':'PROJECT_LEAD_CONFIRMED_SELECTION','selected_source_id':'ENN_EXL50U_SUPRATHERMAL_REPORT','selection_receipt':{'type':'project_lead_confirmation','date':'2026-10-30','quote':'Yeah ENN is third finding'},'candidate_is_not_default':True,'reason':'Original news message groups ENN EXL-50U with hollow-sphere and PRISM; project lead explicitly confirmed ENN after the ambiguity was reported. This confirms selection, not integrated performance.'},
 'configurations':[
  {'id':'SF_A_NEW_HYBRID_V0_1','alias':'A','label':'New published-research hybrid','inherits':[],'research_modules':['new_hollow_sphere','new_prism','enn_fast_proton_coupling'],'stars_module_inheritance':False,'full_configuration':None,'architecture_identity_complete':True,'performance':None},
  {'id':'SF_B_COMBINED_HYBRID_V0_1','alias':'B','label':'Hybrid A integrated with original STARS','inherits':['SF_A_NEW_HYBRID_V0_1','SF_C_ORIGINAL_STARS_V0_1'],'research_modules':['new_hollow_sphere','new_prism','enn_fast_proton_coupling']+modules,'stars_module_inheritance':True,'full_configuration':None,'architecture_identity_complete':True,'performance':None,'integration_requirements':['source-to-mirror/catcher phase-space handoff','shared field and material-state compatibility','duplicate hardware reconciliation by physical instance ID','alpha energy partition and external field work','all-attempt readiness/firing/jitter accounting','complete facility energy and industrial integration']},
  {'id':'SF_C_ORIGINAL_STARS_V0_1','alias':'C','label':'Original STARS reference','inherits':[],'research_modules':modules,'stars_module_inheritance':False,'full_configuration':None,'architecture_identity_complete':True,'performance':None,'historical_family':'STARS_REFERENCE_V1','note':'26 retained inventory entries include software, optional branches and alternatives; this does not install all alternatives simultaneously. Architecture identity completeness means family identity only; an executable physical baseline still needs an exact pinned configuration.'}
 ],
 'legacy_mappings':[
  {'legacy_id':'STARS_REFERENCE_V1','new_id':'SF_C_ORIGINAL_STARS_V0_1','relationship':'REFERENCE_FAMILY_ALIAS_ONLY','retag_historical_runs':False},
  {'legacy_id':'HYBRID_PB_RESEARCH_V0_1','new_id':'SF_B_COMBINED_HYBRID_V0_1','relationship':'FORWARD_FULL_STACK_FAMILY_MAPPING_ONLY','retag_historical_runs':False,'reason':'Prior registry explicitly retained original STARS plus new hollow-sphere/mirror modules. It must not be used as an alias for new A.'},
  {'legacy_id':'STARS_DESIGN_CANDIDATE_V0_1','new_id':None,'relationship':'SEPARATE_PROSPECTIVE_REVISION_RETAINED','retag_historical_runs':False,'reason':'Not automatically equal to A, B or unchanged C. Promotion of selected design changes requires a new version.'}
 ],
 'common_metrics':['fusion_events_per_attempt','fusion_events_per_incident_proton','alpha_birth_energy_J_per_attempt','alpha_escape_energy_J_per_attempt','load_electricity_J_per_attempt','wall_input_J_per_attempt','net_electricity_J_per_attempt','physical_success_probability','source_jitter_distribution','attempts_per_hour','useful_output_per_hour','capex_and_opex_with_price_date'],
 'metric_policy':{'unknown':None,'missing_outcomes':'DISTINCT_FROM_ZERO','physical_success':'DISTINCT_FROM_DIAGNOSTIC_QUALIFICATION','comparison_bases':['same wall-plug budget','same source inventory and time window','documented architecture-specific budgets when exact matching is impossible'],'shared_software_is_not_shared_hardware':True,'all_alternatives_installed':False,'sum_independent_gain_factors':False}
}
(R/'ABC_REGISTRY.json').write_text(json.dumps(registry,indent=2)+'\n')
