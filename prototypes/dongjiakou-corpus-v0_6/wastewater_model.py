"""Water/resource envelopes. Assumed flows and yields are not site performance."""
import itertools
M3_MGD=3785.411784
ACRE_M2=4046.8564224


def split_reuse(feed_mgd, direct_fraction, advanced_recovery, process_loss_fraction=0):
    if feed_mgd < 0 or not 0 <= direct_fraction <= 1 or not 0 < advanced_recovery <= 1 or not 0 <= process_loss_fraction < 1:
        raise ValueError('Invalid reuse assumptions')
    loss=feed_mgd*process_loss_fraction
    available=feed_mgd-loss
    direct=available*direct_fraction
    advanced_feed=available-direct
    advanced=advanced_feed*advanced_recovery
    reject=advanced_feed-advanced
    return dict(feed_mgd=feed_mgd,direct_fit_for_use_mgd=direct,
                advanced_feed_mgd=advanced_feed,advanced_product_mgd=advanced,
                residual_mgd=reject,process_loss_mgd=loss,total_reusable_mgd=direct+advanced,
                actual_authorized_delivered_mgd=None,
                basis='ASSUMED hydraulic split; direct branch still needs end-use qualification; no treatment guarantee')


def struvite_balance(flow_mgd,p_mg_l,ammonium_n_mg_l,mg_supply_t_d,
                     capture_fraction=1, reactive_p_fraction=1):
    """MgNH4PO4.6H2O, limited by P,N,Mg. N input is ammonia-N, not nitrate/TN.

    Total P is not necessarily reactive phosphate. Conversion and purity unmodeled.
    Any supplied Mg must be reallocated from a finite upstream inventory.
    """
    if any(x<0 for x in [flow_mgd,p_mg_l,ammonium_n_mg_l,mg_supply_t_d]) or not 0<=capture_fraction<=1 or not 0<=reactive_p_fraction<=1:
        raise ValueError('Invalid nutrient input')
    p=flow_mgd*M3_MGD*p_mg_l/1e6
    n=flow_mgd*M3_MGD*ammonium_n_mg_l/1e6
    kmol=min(p*reactive_p_fraction*1000/30.973762,n*1000/14.0067,mg_supply_t_d*1000/24.305)*capture_fraction
    usedp=kmol*30.973762/1000;usedn=kmol*14.0067/1000;usedmg=kmol*24.305/1000
    return dict(flow_mgd=flow_mgd,p_feed_t_d=p,ammonium_n_feed_t_d=n,
                mg_supply_assumed_t_d=mg_supply_t_d,
                theoretical_struvite_t_d=kmol*245.404/1000,
                p_to_struvite_t_d=usedp,n_to_struvite_t_d=usedn,mg_to_struvite_t_d=usedmg,
                remaining_total_p_t_d=p-usedp,remaining_ammonium_n_t_d=n-usedn,
                unconsumed_mg_t_d=mg_supply_t_d-usedmg,
                qualified_struvite_t_d=0,actual_net_value_usd_d=None)


def tank_footprint(flow_mgd,hours,depth_m,layout_factor=1):
    if flow_mgd<0 or hours<=0 or depth_m<=0 or layout_factor<1:raise ValueError('Invalid tank assumptions')
    volume=flow_mgd*M3_MGD*hours/24
    return dict(flow_mgd=flow_mgd,assumed_retention_hours=hours,assumed_depth_m=depth_m,
                volume_m3=volume,water_surface_m2=volume/depth_m,
                assumed_tank_plot_m2=volume/depth_m*layout_factor,
                assumed_tank_plot_acres=volume/depth_m*layout_factor/ACRE_M2,
                full_treatment_campus_acres=None,
                scope='Geometry-only tank envelope; excludes process skids solids buildings roads setbacks flood protection and redundancy')


def circulation_makeup(circulation_mgd,evaporation_fraction,return_treatment_recovery):
    if circulation_mgd<0 or not 0<=evaporation_fraction<=1 or not 0<=return_treatment_recovery<=1:raise ValueError('Invalid loop assumptions')
    evaporation=circulation_mgd*evaporation_fraction
    return_flow=circulation_mgd-evaporation
    recovered=return_flow*return_treatment_recovery
    purge=return_flow-recovered
    return dict(circulation_mgd=circulation_mgd,evaporated_mgd=evaporation,
                return_flow_mgd=return_flow,recovered_return_mgd=recovered,
                liquid_purge_mgd=purge,makeup_mgd=evaporation+purge,
                note='Illustrative return-water loop; evaporation is consumed; recirculated flow is not new supply; salts/chemicals and microbial limits require separate control')


def irrigation_envelope(flow_mgd,distribution_efficiency,annual_applied_acre_ft_per_acre):
    if flow_mgd<0 or not 0<distribution_efficiency<=1 or annual_applied_acre_ft_per_acre<=0:raise ValueError('Invalid irrigation inputs')
    af=flow_mgd*1e6*365/325851.429*distribution_efficiency
    return dict(allocated_reuse_mgd=flow_mgd,assumed_distribution_efficiency=distribution_efficiency,
                annual_applied_duty_acre_ft_acre=annual_applied_acre_ft_per_acre,
                delivered_acre_ft_year=af,illustrative_irrigation_acres=af/annual_applied_acre_ft_per_acre,
                authorized_crop_acres=None,status='Annual arithmetic only; not located land, agronomic suitability, seasonal storage or legal allocation')


def import_displacement(accepted_t,verified_imported_purchase_t,equivalence_fraction):
    if any(x is None for x in [accepted_t,verified_imported_purchase_t,equivalence_fraction]):return None
    if accepted_t<0 or verified_imported_purchase_t<0 or not 0<=equivalence_fraction<=1:raise ValueError('Invalid displacement inputs')
    return min(accepted_t*equivalence_fraction,verified_imported_purchase_t)


def wastewater_outputs(inputs):
    cfg=inputs['wastewater_screening']
    water=[]
    for f,d,r in itertools.product(cfg['assumed_feed_mgd'],[0,.5,1],[.85,.9,.95]):
        water.append(dict(assumed_direct_fraction=d,assumed_advanced_recovery=r,**split_reuse(f,d,r),
            caveat='16MGD is whole announced program;8MGD historical Greenwood design phase; neither is a confirmed unallocated feed; all scenarios separate alternatives'))
    nutrients=[]
    for f in [4,8,16]:
        nutrients.append(dict(case='Historical final-effluent chemistry scaled to assumed flow',
            chemistry_source='GW_PERMIT single2024-09-03sample; ammoniaJestimated below0.1reportinglimit; notcurrentaverage',
            capture_fraction=1,reactive_p_fraction=1,
            **struvite_balance(f,3.2,.08,1,1,1),
            interpretation='Stoichiometric CEILING assuming alltotalP reactive and adequateMg; ammonia limits; nitrate NOT counted as ammonium.16MGD mixedprogram chemistry unknown'))
    for f in [.1,.5,1]:
        nutrients.append(dict(case='ASSUMED concentrated sidestream, not a measured local stream',
            chemistry_source='Analyst scenario100mgP/L500mgammoniaN/L; not raworfinaleffluent assay',
            capture_fraction=.8,reactive_p_fraction=1,
            **struvite_balance(f,100,500,1,.8,1),
            interpretation='Alternative to finaleffluent approach; do notsum streamsfromsame nutrient inventory; quote equipment and assay available sidestream'))
    footprint=[tank_footprint(f,h,5,1.5) for f,h in itertools.product([8,16],[4,8,24])]
    loops=[dict(assumed_evaporation_fraction=e,assumed_return_treatment_recovery=r,
                **circulation_makeup(10,e,r)) for e,r in itertools.product([.01,.05,.1],[.8,.95])]
    irrigation=[irrigation_envelope(q,.85,d) for q,d in itertools.product([1,2,4],[2,3,4])]
    # Dissolved inventory, not saleable recovered salt; scaled single historical assay.
    inventory=[]
    for f in [8,16]:
        for analyte,conc in [('chloride',509),('TDS',1432),('total_P',3.2),('ammonia_N',.08)]:
            inventory.append(dict(assumed_flow_mgd=f,analyte=analyte,historical_sample_mg_l=conc,
                derived_inventory_t_d=f*M3_MGD*conc/1e6,actual_recovered_t_d=0,
                note='SingleGreenwoodsample;16MGD extrapolation not representative mixedprogram; TDS overlaps ions and must notsum withchloride. No counterion-assay or industrialpurity inferred.'))
    allocations=[]
    for direct in [0,.5,1]:
        b=split_reuse(16,direct,.9)
        reserved=8
        remaining=max(0,b['total_reusable_mgd']-reserved)
        allocations.append(dict(assumed_program_feed_mgd=16,assumed_direct_fraction=direct,
            reusable_water_mgd=b['total_reusable_mgd'],illustrative_valero_reservation_mgd=reserved,
            upper_arithmetic_remainder_mgd=remaining,residual_mgd=b['residual_mgd'],
            additional_reuse_credit_mgd=None,
            note='NOTavailableallocation:reserveup-to8MGDcontractfirst;othercontractsrightsfirmflowsqualityunverified;remaining cannotbeassignedtoLNGandagriculturetwice'))
    p_equiv=[]
    for row in nutrients:
        p=row['p_to_struvite_t_d']
        p_equiv.append(dict(case=row['case'],flow_mgd=row['flow_mgd'],p_recovered_t_d=p,
            p2o5_equivalent_t_d=p*141.9445/(2*30.973762),
            n_recovered_t_d=row['n_to_struvite_t_d'],qualified_fertilizer_t_d=0,
            verified_import_displacement_t_d=None,
            note='Nutrient-unit equivalence only,not agronomic oneforoneDAP substitution or accepted product/importsaving'))
    return dict(wastewater_water_scenarios=water,wastewater_nutrient_scenarios=nutrients,
                wastewater_tank_footprint=footprint,industrial_loop_scenarios=loops,
                agriculture_water_envelope=irrigation,wastewater_inventory=inventory,
                water_allocation_envelope=allocations,nutrient_equivalents=p_equiv)


def supplemented_struvite(flow_mgd,p_mg_l,native_ammonium_n_mg_l,target_p_fraction,
                         mg_supply_t_d,ammonia_source):
    if not 0<=target_p_fraction<=1:raise ValueError('Invalid target')
    if ammonia_source not in ['local_recovered','domestic_purchase','international_import']:
        raise ValueError('Unknown ammonia source')
    q=flow_mgd*M3_MGD
    target_p=q*p_mg_l/1e6*target_p_fraction
    native_n=q*native_ammonium_n_mg_l/1e6
    n_needed=target_p*14.0067/30.973762
    supplemental_n=max(0,n_needed-native_n)
    supplemental_mg_l=supplemental_n*1e6/q if q else 0
    r=struvite_balance(flow_mgd,p_mg_l,native_ammonium_n_mg_l+supplemental_mg_l,
                       mg_supply_t_d,1,target_p_fraction)
    usedn=r['n_to_struvite_t_d']
    recovered_n=min(native_n,usedn)
    added_n=max(0,usedn-recovered_n)
    return dict(flow_mgd=flow_mgd,target_total_p_fraction_assumed_reactive=target_p_fraction,
                native_ammonia_n_mg_l=native_ammonium_n_mg_l,ammonia_source=ammonia_source,
                supplemental_n_delivered_t_d=supplemental_n,
                supplemental_nh3_pure_equivalent_t_d=supplemental_n*17.03052/14.0067,
                nitrogen_recovered_from_final_effluent_t_d=recovered_n,
                supplemental_n_in_product_t_d=added_n,
                imported_n_consumed_t_d=added_n if ammonia_source=='international_import' else 0,
                p_recovered_t_d=r['p_to_struvite_t_d'],mg_consumed_t_d=r['mg_to_struvite_t_d'],
                theoretical_struvite_t_d=r['theoretical_struvite_t_d'],
                actual_qualified_product_t_d=0,actual_net_value_usd_d=None,
                source_note='Mgassumedadequate;Ptargetassumesreactiveavailability;localsidestreamNmustnotbecreditedtwice;NH3equivalentnotaqueousdeliverymass;notactualcaptureperformance')


def bioreactor_outputs(inputs):
    cases=[supplemented_struvite(f,3.2,n,target,1,source)
           for f,n,target,source in itertools.product([8,16],[0,.08,.1],[.5,.8,1],
              ['local_recovered','domestic_purchase','international_import'])]
    price=[]
    for r in cases:
        if r['native_ammonia_n_mg_l']==.08 and r['target_total_p_fraction_assumed_reactive']==.8 and r['ammonia_source']=='domestic_purchase':
            for cost in [300,600,1000]:
                price.append(dict(flow_mgd=r['flow_mgd'],assumed_delivered_usd_t_pure_nh3_equivalent=cost,
                    modeled_supplemental_nh3_t_d=r['supplemental_nh3_pure_equivalent_t_d'],
                    modeled_ammonia_only_cost_usd_d=cost*r['supplemental_nh3_pure_equivalent_t_d'],
                    total_recovery_cost_usd_d=None,
                    note='Priceassumptionsnotquotes;excludesstoragehandlingalkaliMgrecoverywaterenergycapitalqualityresiduals;aqueoussolutiondeliverycostdiffers'))
    tanks=[]
    for f,h in itertools.product([8,16],[6,12]):
        tanks.append(dict(module='ASSUMEDmainlinebiologicaltank',**tank_footprint(f,h,5,1.5)))
    for f,days in itertools.product([.1,.5],[15,25]):
        tanks.append(dict(module='ASSUMEDsolidsdigesterfeed;notwholeWWTPflow',**tank_footprint(f,days*24,6,1.5)))
    return dict(ammonia_supplement_sensitivity=cases,ammonia_only_cost_sensitivity=price,
                bioreactor_tank_geometry=tanks)
