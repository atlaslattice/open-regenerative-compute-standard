"""Rebuild the research catalog. No supplier quotes or measured Oahu yields are supplied."""
import json
from pathlib import Path
P=Path(__file__).parent
B='https://www.materialwashing.com/'
sources={
 'D_FIXED':B+'Fixed-Washing-Plant/79.html',
 'D_SCREEN':B+'Mobile-Screening-Plant/281.html',
 'D_SCREEN_NEWS':B+'news/1051.html',
 'D_MOBILE':B+'Mobile-Washing-Plant/',
 'D_01':B+'Mobile-Washing-Plant/26.html',
 'D_02':B+'Mobile-Washing-Plant/27.html',
 'D_03':B+'Mobile-Washing-Plant/205.html',
 'D_04':B+'Mobile-Washing-Plant/206.html',
 'D_SOIL':B+'application/soil-washing-and-remediation-plant.html',
 'D_OIL':B+'application/oil-contaminated-soil-washing-and-remediation-plan.html',
 'D_SLUDGE':B+'application/ditch-and-dredged-sludge-washing-and-disposal-plan.html',
 'D_BULK':B+'application/bulk-material-screening-plant.html',
 'D_MATERIAL':B+'application/material-washing-and-classification-plant.html',
 'FRTR':'https://frtr.gov/matrix/',
 'WASH':'https://frtr.gov/matrix/Soil-Washing/',
 'SS':'https://frtr.gov/matrix/Solidification-and-Stabilization/',
 'THERMAL':'https://frtr.gov/matrix/Desorption-Incineration/',
 'VAPOR':'https://www.frtr.gov/matrix/Vapor-Treatment-Technologies/',
 'EK':'https://frtr.gov/matrix/Electrokinetic-Enhanced-Remediation/',
 'PLASTICS':'https://www.epa.gov/plastics/advanced-recycling-plastics',
 'AD':'https://www.epa.gov/anaerobic-digestion/basic-information-about-anaerobic-digestion',
 'WATER':'https://www.energy.gov/cmei/ito/water-resource-recovery-basics',
 'BRINE':'https://www.gao.gov/products/gao-25-108484',
 'BRINE_RND':'https://www.pnnl.gov/news-media/ocean-teeming-critical-minerals-heres-how-we-could-get-them',
 'PFAS':'https://pfas-1.itrcweb.org/12-treatment-technologies/',
 'V01':'../oahu-lattice-v0_1/inputs.json'}
mods=[]
def add(i,name,feed,out,residual,gate,source,kind='technology_family',**extra):
 mods.append(dict(id=i,name=name,feed=feed,possible_outputs=out,residual_liabilities=residual,
   clearance_gate=gate,source_ids=source.split(),catalog_kind=kind,
   evidence='manufacturer publication; performance unverified' if source.startswith('D_') else 'technology reference or candidate mapping; Oahu suitability unverified',
   execution='catalog only; no calibrated transfer function',capex_usd=None,opex_usd_per_feed_t=None,**extra))
add('D_FIXED','Fixed washing and remediation plant','characterized soil/mineral feed','graded washed solids','cake; process water; rejects','treatability; reuse qualification; complete-train quote','D_FIXED','complete_train',contains=['D_01','D_02','D_03','D_04'],mutually_exclusive_with=['D_MOBILE_TRAIN'])
add('D_MOBILE_TRAIN','Mobile washing plant package','characterized soil/mineral feed','graded washed solids','cake; water; oversize','supplier line balance and same-feed guarantee','D_MOBILE','complete_train',contains=['D_01','D_02','D_03','D_04'],mutually_exclusive_with=['D_FIXED'])
add('D_SCREEN','Mobile screening platform: DS260 / DS15SE','prepared sized feed','particle-size fractions','all fractions still require qualification','feed preparation; sustained capacity on specified feed','D_SCREEN D_SCREEN_NEWS','machine',variants=['vibrating','rotary/trommel','bar/grizzly'],published_conflicts={'product_page':{'tph':[30,150],'kw':28.5,'kg':15200,'mm':[8400,3100,3400]},'news_DS15SE':{'tph':[60,200],'kw':28.5,'kg':13500,'mm':[9600,3100,3330]}},option_claims_not_included_quote=['crawler or trailer arrangements','magnetic separation mentioned elsewhere; not standard inclusion'])
add('D_01','DSLXC/01 mobile scrubbing','coarse-screened soil','scrubbed slurry and separated coarse solids','contaminants transferred downstream','chemistry and abrasion trial; feed-rate basis','D_01','machine',published={'table_tph':[15,20],'overview_tph':[15,30],'kw':71.5,'kg':28000,'mm':[14500,2700,4200]})
add('D_02','DSLXC/02 multistage classifying','slurry: published <=30% concentration, <=2mm solids','graded fine sand; concentrated slurry','concentrate and process water','clarify dry-solid versus slurry capacity','D_02','machine',published={'table_tph':30,'kw':70,'kg':28500,'mm':[14000,2900,4200]})
add('D_03','DSLXC/03 solid-liquid separation','concentrated slurry','dewatered cake; filtrate','cake not automatically fuel or clean soil','cake solids; cycle time; contaminant partition','D_03','machine',published={'tph':None,'kw':None,'kg':None})
add('D_04','DSLXC/04 mobile water treatment','wash-process filtrate','water proposed for internal recycle','sludge; dissolved contaminants; purge','dissolved contaminant removal; recycle accumulation; confirm model/table','D_04','machine',published={'heading_model':'DSLXC/04','body_model':'DLSX/04','table_model':'DSLXC/03','table_capacity_raw':'90 m3; time basis absent','table_kw_unconfirmed':20,'table_kg_unconfirmed':37000,'table_mm_unconfirmed':[17800,3000,4400]})
add('D_SOIL_APP','Desen contaminated-soil washing configuration','assayed soil/fines','coarse and sand fractions','fine concentrate; contaminated water','contaminant-specific test; publication excludes mercury','D_SOIL','application_configuration',uses=['D_FIXED or D_MOBILE_TRAIN'])
add('D_OIL_APP','Desen hot washing / oil sludge configuration','suitable oily sandy solids/sludge','separated oil; washed solids','emulsions; water; contaminated cake','oil acceptance; heat and reagent demand; residual fate','D_OIL','application_configuration',note='Hot washing is not thermal desorption or incineration.')
add('D_SLUDGE_APP','Desen ditch/dredged/sludge configuration','assayed sediment or suitable sludge','graded gravel/sand; separated organics','contaminants concentrated in cake','pathogens; metals; organic contaminants; reuse standards','D_SLUDGE','application_configuration')
add('D_BULK_APP','Desen bulk screening configuration','landfill/C&D/quarry/mineral feed','size fractions','rejects and unqualified fractions','feed size; separation versus product purity','D_BULK','application_configuration')
add('D_MATERIAL_APP','Desen material washing/classification configuration','ores/coal/aggregate/ceramic feed','upgraded mineral fractions','slimes and process water','assay; product specification; actual downstream refining','D_MATERIAL','application_configuration')
# These candidates are not represented as products sold by Desen. References support the
# technology families, not a claim of site compatibility or a purchasable Hawaiian package.
rows=[
('P01','Sampling, hazard isolation and whole-item recovery','all proposed feed','reusable items; characterized batches','hazards; rejected feed','approved sampling and handling plan','V01'),
('P02','Selective shredding / size reduction','hazard-cleared oversize','liberated sized feed','dust; wear debris; fines','battery/cylinder exclusion; fire and dust controls','V01'),
('P03','Magnetic ferrous separation','liberated dry or wet fractions','ferrous concentrate','entrained contaminants; reject','buyer assay and netback; no refined-metal assumption','V01'),
('P04','Eddy-current nonferrous separation','suitably sized liberated feed','nonferrous concentrate','fines and composite rejects','particle size and conductivity trial; buyer acceptance','V01'),
('P05','Sensor / optical / density sorting','conditioned selected fractions','polymer/mineral/metal concentrates','mis-sorts; washwater if wet','representative accuracy; throughput; buyer specs','V01'),
('P06','External metal refining / e-waste specialist','accepted concentrates or isolated components','refined metals by contract','slags; dust; refining residues','tolling terms; provenance; recovery and liability ownership','V01'),
('M01','Aggregate crushing, grading and certified reuse','qualified concrete/stone/glass','construction aggregate','dust; rejects','engineering and leachability specifications','V01'),
('M02','Physical washing and attrition','suitable contaminated mineral fractions','separated coarse and sand fractions','concentrated fines; effluent','treatability; all contaminant classes; reuse permission','WASH'),
('M03','Chemical extraction / selective leaching','suitable soil or metal concentrate','extracted target species','spent solution; washed residual','reagent demand; metals recovery; effluent treatment','WASH'),
('M04','Electrokinetic treatment','appropriate conductive fine soil','extracted ions / treated soil','electrode liquids; concentrates','site-specific pilot; energy; speciation','EK'),
('M05','Biopiles / landfarming / slurry bioreactors','biodegradable contaminated soil','treated soil; biological products','persistent contaminants; biomass; gases','degradation endpoints; inhibition; residence time','FRTR'),
('M06','Phytoremediation','appropriate low-risk soil/water','managed vegetation; treated medium','contaminated biomass','time; rooting depth; biomass fate; exposure','FRTR'),
('M07','Chemical oxidation / reduction','compatible contaminant-bearing medium','transformed target compounds','byproducts; salts; mobilized metals','treatability; incomplete reactions; final speciation','FRTR'),
('M08','Thermal desorption','suitable organically contaminated solids','treated solids; recovered vapors','condensate; offgas; residual metals','offgas treatment; energy; solids acceptance','THERMAL'),
('M09','Permitted incineration / co-processing','accepted combustible hazardous or residual feed','energy where usable; treated residue','ash; air-control residues; emissions','facility-specific permit and destruction verification','THERMAL'),
('M10','Solidification / stabilization','appropriate contaminated cake or solids','immobilized material','larger bound residual still requiring an outlet','leach test; durability; final placement','SS'),
('M11','Vitrification / engineered mineral encapsulation','suitable inorganic contaminated solids','glass-like immobilized matrix','offgas; volatilized contaminants; rejects','energy; volatilization controls; long-term leaching','SS'),
('M12','Qualified binder / cement / carbonation products','specified mineral or ash fractions','engineered mineral products','rejects; retained contaminants','product durability and leaching; LCA; accepted binder recipe','V01'),
('M13','Soil vapor extraction / containment of volatile releases','appropriate unsaturated contaminated zone','captured vapors','offgas; condensate','extraction feasibility; vapor treatment; permit','FRTR VAPOR'),
('M14','Engineered capping / monitored containment','residual site or authorized cell','contained exposure pathway','continuing monitoring and future liability','hydrology; slope; gas; legal closure plan','FRTR'),
('R01','RDF conditioning, baling and contracted H-POWER delivery','characterized accepted combustibles','fuel service; energy at incumbent plant','rejected fuel; additional ash','written acceptance, capacity, fee/netback; trial','V01'),
('R02','Mechanical polymer recycling','clean compatible separated polymers','flakes/pellets by specialist','wash residues; rejects','polymer/additive specification; wash and dry costs','PLASTICS'),
('R03','Solvent polymer purification','selected polymer stream','purified polymer','spent solvent; concentrated contaminants','solvent recovery; polymer-specific pilot; buyer','PLASTICS'),
('R04','Depolymerization','suitable polymer chemistry','monomer/intermediates','impurities; reaction residues','polymer-specific process and product contract','PLASTICS'),
('R05','Pyrolysis / gasification / hydrothermal conversion','specified carbonaceous feed','oil/gas/intermediates/char as applicable','char; aqueous phase; tar; gases','feed specification; yields; refining acceptance; emissions','PLASTICS'),
('O01','Source-separated organics composting','qualified uncontaminated organics','compost','rejects; leachate; emissions','feed rights; pathogens; contaminants; maturity','AD'),
('O02','Anaerobic digestion with gas cleanup','biodegradable qualified food/sludge','biogas/RNG; digestate','inerts; contaminant-bearing digestate','biomethane potential; rights; gas and digestate outlets','AD'),
('O03','Biochar from qualified biomass','qualified biomass','char; useful heat if recovered','condensate; ash; contaminated char risk','feed provenance; char standards; emissions; complete balance','V01'),
('O04','Nutrient recovery / struvite','suitable nutrient-bearing liquor plus qualified Mg','nutrient salt','spent liquor; contaminants','Mg purity; nutrient balance; product approval','WATER'),
('O05','Agricultural and ecological reuse','qualified water/compost/nutrients','specified irrigation or soil service','salinity; accumulation; runoff','crop/soil need; permits; baseline and counterfactual','V01'),
('W01','Water equalization, separation, clarification and filtration','process water/leachate','conditioned water','sludge; backwash','flow and dissolved contaminant assay','FRTR WASH'),
('W02','Biological water treatment','biodegradable aqueous stream','treated water; biogas where applicable','biomass; nutrient residuals','salinity/toxicity; removal versus destruction','FRTR'),
('W03','Adsorption and ion exchange','conditioned contaminated water','treated water','spent media; regenerant','breakthrough; competing ions; final media fate','FRTR PFAS'),
('W04','Chemical precipitation and dissolved-metal recovery','metal-bearing liquid','metal precipitate or recovered intermediate','sludge; salts; reagent residuals','speciation; product purity; residual cost','FRTR'),
('W05','Membrane separation / RO / NF','pretreated water or saline feed','permeate; separated ion fractions','concentrate; cleaning solution','fouling; recovery; concentrate fate','FRTR WATER'),
('W06','Advanced oxidation / specialist aqueous destruction','suitable dissolved organic contaminants','treated water','byproducts; salts; offgas','compound-specific destruction evidence; no generic PFAS pass','FRTR PFAS'),
('W07','Evaporation / crystallization / ZLD','concentrate','condensate; mixed or selective salts','salt residuals; cleaning wastes; energy demand','heat/electricity; salt disposal or contracts','WATER'),
('W08','Specialist PFAS destruction / residual management','PFAS concentrate or media','verified destruction where demonstrated','fluoride; byproducts; remaining PFAS','mass balance incl. fluorine; independent test; permitted outlet','PFAS'),
('W09','Offgas capture / adsorption / oxidation','captured vapors or process gases','treated gas; recovered solvents if suitable','spent sorbent; condensate; emissions','air permit; destruction or regeneration evidence','VAPOR'),
('B01','Qualified brine Mg/Ca precipitation and purification','separately assayed desal concentrate','Mg/Ca compounds to specification','spent brine; contaminants; reagent salts','assay; purity; energy/reagents; allocation and contract','BRINE'),
('B02','Brine salt fractionation / crystallization','qualified brine','salt products','mother liquor; off-spec salts','market volume; purification and freight cost','BRINE WATER'),
('B03','Bipolar electrodialysis acid/base production','suitable purified saline stream','acid and base','depleted brine; cleaning waste','measured yield; electricity; purity; corrosion','BRINE_RND'),
('B04','Selective trace mineral recovery','assayed enriched brine or mineral concentrate','target intermediate','spent sorbent; residual brine','concentration threshold; pilot; no default lithium/REE credit','BRINE'),
('E01','Heat exchange / heat pump / recovered process heat','usable temperature-matched heat source','measured thermal service','pumping and heat-pump burden','temperature and seasonal coincidence; displacement baseline','V01'),
('E02','Solar/grid/storage and backup integration','permitted energy connection/site','power and resilience service','capital; losses; end-of-life equipment','dispatch; interconnection; full load profile','V01'),
('I01','Industrial offtake / local fabrication and replacement parts','qualified materials; approved designs','industrial inputs; serviceable parts','rejected product; machining residues','engineering certification; demand; counterfactual downtime','V01'),
('I02','Measurement, data records and optional AI controls','sensors; samples; process records','auditable decisions; optional control service','compute energy; errors; maintenance','holdout benchmark; metering; human override','V01'),
('X01','Mercury specialist recovery / retort','segregated Hg-bearing feed','controlled recovered Hg or stabilized residue','offgas controls; contaminated residuals','specialist permit; emissions; long-term disposition','FRTR'),
('X02','Asbestos / battery / radioactive / medical specialist routing','isolated regulated hazards','authorized treatment or disposal','long-term managed residue','material-specific authorization; no ordinary screen feed','V01'),
('X03','Residual transport and authorized disposal','all unqualified residuals','lawful final disposition','closure and monitoring liability','acceptance; transport; wet weight; fee quote','V01'),
]
for row in rows: add(*row)
apps=['D_SOIL_APP','D_OIL_APP','D_SLUDGE_APP','D_BULK_APP','D_MATERIAL_APP']
data={'version':'0.2','created':'2026-10-24','web_review_date':'2026-10-23',
 'status':'Discovery catalog, not installed equipment, supplier quotation or evidence of environmental clearance.',
 'coverage':'All three top-level product families, all four named mobile washing machines, three screen variants, and all five application families linked by the reviewed materialwashing.com navigation. Not a claim to enumerate unpublished custom options or every news article.',
 'sources':sources,'modules':mods,
 'accounting_rules':['Application configurations are recipes, not extra machines.','A fixed/mobile package and its four component prices are alternative quote scopes, never additive charges.','Unknown prices and capacities remain null, not zero.','No module destroys elements; contaminants must be removed, transferred, immobilized or retained.','All reuse and claimed benefits require separate permits, assays, contracts and counterfactuals.'],
 'desen_auxiliaries':{'bundled_or_optional_confirm_in_quote':['feeders; bar screen; scrubber; hydraulic screen','slurry pumps; tanks; dosing','hydroclassification; settling','filter press; cake conveyor','PLC/DCS; remote monitoring; hydraulics; enclosure','electrical supply; interconnecting pipework; foundations; spill containment'], 'not_assumed_included':['eddy current separator','refinery','RO/PFAS destruction','thermal desorption','complete hazardous-waste treatment','agricultural product certification']}}
(P/'catalog.json').write_text(json.dumps(data,indent=2)+'\n')
print(len(mods),'modules / recipes')
