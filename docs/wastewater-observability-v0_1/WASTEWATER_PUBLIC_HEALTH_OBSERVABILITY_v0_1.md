# Atlas Lattice wastewater public-health observability

Version 0.1 | 24 October 2026 | Cross-cutting design requirement and Corpus v0.8 addendum

## Decision

Public-health observability is a first-class integration surface for Atlas wastewater nodes, alongside water service, material recovery, environmental quality and process performance. Every new design or retrofit assessment should identify sampling access, catchment coverage, testing options, data rights, accountable public-health partners, costs and evidence gaps. This is a design standard, not a claim that existing nodes are already monitored or that every site needs an on-site laboratory.

Verily Sightline and WastewaterSCAN are concrete reference systems. Neither a procurement commitment, provider partnership, India service availability nor achieved health benefit is established. Comparable locally qualified providers may implement the same interface. A Chinese-reference equipment design does not establish a supplier for this additional laboratory service. Public-health testing is a separately costed service lane with vendor and jurisdictional suitability TBD.

## Evidence and corrections

WastewaterSCAN is a Stanford-based program with Emory, funded by the Sergey Brin Family Foundation; Verily is its laboratory partner [H1]. It is not simply a Google-owned initiative. Its described workflow collects samples three times weekly and tests within 48 hours after lab receipt. Collection, transport, laboratory work and interpretation create separate delays. That does not establish continuous on-site pathogen sensing.

WastewaterSCAN's dashboard describes infectious-disease targets, RT-ddPCR measurements, controls and selected sequencing [H2]. A September 2026 study with Stanford, Emory and Verily researchers used hybrid-capture metagenomic sequencing on nearly 450 samples and compared it with digital PCR [H3]. Metagenomics is therefore a real evidence-backed integration option; it must not be described as the universal routine workflow or an instant sensor.

Verily currently lists dengue serotypes 1-4 and selected antimicrobial-resistance targets among its available assays [H4]. That is manufacturer-described service availability, not validation of a particular Chennai catchment or a guaranteed outbreak lead time. Disease-specific sensitivity, sampling matrix and local validation remain necessary.

The identified national high-risk-substance pilot involved Biobot and NIDA, not evidence of a WastewaterSCAN fentanyl program [H5]. Drug/metabolite testing is a distinct analytical lane, generally requiring chemical analysis such as mass spectrometry. Pathogen sequencing does not itself quantify fentanyl. Provider, analytes and assay scope must be verified independently.

A 2026 malaria study models wastewater detectability and performs laboratory recovery/persistence experiments. It finds important limitations, including difficult detection at low incidence and low recovery in tested methods [H6]. It does not demonstrate operational neighborhood-level malaria warning in Chennai, Vizag or Corpus. Dengue field research supports a candidate pathway [H7]; it does not make all vector-borne diseases equivalent or identify mosquito breeding locations from sewer measurements.

## Module architecture

| Lane | Purpose | Current evidence boundary |
|---|---|---|
| H01 Sampling and catchment registry | Representative liquid/solids samples before target-removing treatment; map contributing population | Required design interface; actual sites, rates and costs unknown |
| H02 Targeted pathogen assays | Locally validated RT-qPCR/ddPCR or other appropriate assays | Established reference workflow; target/site performance separate |
| H03 Sequencing and discovery | Validated targeted or metagenomic methods for selected questions | Published research and available services; not guaranteed discovery |
| H04 Chemical exposure monitoring | Optional drugs/metabolites or other validated chemical markers | Separate provider, chemistry and governance; not WastewaterSCAN pathogen panel |
| H05 AMR and environmental biology | Optional resistance-gene and biological indicators | Gene signal does not by itself establish viable pathogen, infection or treatment resistance |
| H06 Public-health interpretation | Trends, uncertainty and contextual alerts for accountable officials | Human-reviewed public-health workflow; no individual diagnosis or autonomous intervention |
| H07 Reuse/product health qualification | Distinct water, fertilizer and solids testing appropriate to actual uses | Surveillance is not certification of water or fertilizer safety |

Sampling should occur at a representative point before disinfection, nutrient recovery or biological transformations alter the chosen signal, when that suits the validated assay. Different objectives may require additional downstream samples. Record sampling matrix, flow, rainfall/industrial dilution, contributing population, collection and transport conditions, analytical method/version, controls, detection and quantification limits, uncertainty, and all timestamps. Separate non-detect, not sampled, invalid and pending results. Do not treat missing data as zero disease activity.

Nutrient sidecars and treatment retrofits can change solids partition, residence time and measured concentrations. Record change points and re-establish comparability rather than interpreting a process-driven signal change as a population health change. Upstream recirculation and industrial additions require explicit coverage and dilution assessment. Combining catchments may increase coverage while reducing spatial specificity.

## Data and authority boundaries

Plant SCADA and public-health surveillance are linked through an authorized, segmented data interface. The public-health system must not directly command dosing, valves, spraying, clinical treatment or enforcement. Existing process interlocks and protection functions remain independently engineered. Reports identify the evidence, uncertainty and responsible human review rather than issuing purported diagnoses.

Use community-level aggregation and an explicit public-interest purpose. Small catchments, household inference and stigmatizing interpretations require particular care; default outputs must not identify individuals or label a neighborhood by inferred personal conduct. Public-health officials define appropriate reporting and response protocols with community participation. Human sequencing reads, if present, need an explicit removal/retention policy. Data ownership, consent/authorization requirements, retention, access logging and sharing are unresolved until agreed locally.

Integrity hashes can support sample-record provenance and audit history; they do not prove representative sampling, assay validity, causality or the truth of a clinical inference. Any GoldenTrace or equivalent implementation must document the actual implemented controls rather than inherit a guarantee from its name.

## Compute sizing

This module does not justify a 100 MW compute node by itself. Sampling and analytical laboratory capacity may be the binding resources. Profile samples/day, assay mix, sequencing depth, storage, analysis time and reliability before selecting local CPU/GPU capacity or remote analysis. Record incremental kWh, equipment, training, network and cybersecurity costs. A small local inference/data node can serve a distributed sampling network; on-site hyperscale training is optional and separately justified.

Possible learning uses include assay-quality screening, anomaly detection, uncertainty-aware forecasting and constrained process-model updates. A model trained on telemetry is not automatically a validated physical or epidemiological model. Require out-of-sample evaluation and comparison with simpler methods, including reporting false alerts, missed events, drift and failure cases.

## Cost and public-benefit ledger

Capital, operating cost and realized health credit remain null or zero-credit as appropriate; absence of pricing is not free operation. Include safe sampling access and equipment, consumables, labor, refrigerated transport, laboratories and accreditation/QA, assay development, repeat tests, sequencing, data systems, public-health staffing, training and response capacity. Shared samplers are not automatically valid for every chemical and biological method.

Separate the costs already paid by a public-health program from incremental Atlas duties. Public dashboards, data ownership and research access are not commercial compute revenue. Health surveillance may be publicly supported without being commercially profitable, but its service outputs and budget must be disclosed. Credit verified coverage, valid-result fraction, actual sample-to-report time, reviewed alerts and documented service delivery. Do not assign avoided infections, prevented overdoses, eradication or mortality benefits without a suitable evaluation design.

Local malaria/dengue work should combine any validated wastewater signals with clinical, entomological and environmental evidence. Wastewater does not directly locate infected mosquitoes or replace vector surveillance. Non-sewered populations may be absent from the wastewater catchment [H8]. A broad public-health claim therefore needs a coverage map and complementary surveillance.

## Existing Corpus integration and next steps

This adds a cross-cutting interface to the frozen Corpus network v0.8 paper. Its 30 modules, 20 connections and compute/resource scenarios remain unchanged; no health yield, installed cost, compute requirement or partnership is silently added. Greenwood's planned primary-treatment/digestion changes also matter to the preferred solids-sampling location: use a validated alternative if the existing primary clarifier is unavailable. Actual current layout is unresolved.

For Corpus, Chennai, Vizag and future Maui/Oahu applications: identify public-health and laboratory counterparts; inventory existing surveillance; select representative sampling points; obtain scoped service prices; validate locally relevant targets; establish data/response responsibilities; then run a documented pilot. Apply the same first-class interface in future wastewater work, with explicit 'not applicable', 'unresolved' or implemented status per node. This publication does not claim to rewrite every historical model or to deploy any sensors.

## Related claims that should not enter the baseline

Total site acreage is not vacant buildable land, so the supplied parcel figures do not establish room for a 100-200 MW campus or exclude all alternatives at 1 GW. A cadastral/layout and utility assessment is needed. Seawater and wastewater treatment can share a site with appropriately separated and designed circuits; uncontrolled raw sewage co-feed is not the proposed design. Biofouling is a design/operating risk, not proof of instant inevitable membrane destruction. The magnesium exchange should generally specify qualified Mg salts or Mg(OH)2, not assume elemental magnesium metal production.

## Sources

[H1] WastewaterSCAN organization and workflow, accessed 24 October 2026: https://www.wastewaterscan.org/about

[H2] WastewaterSCAN methods and interpretation: https://data.wastewaterscan.org/about/

[H3] Wolfe et al., 2026, Prospective metagenomic sequencing of wastewater across the United States yields robust viral enrichment and concordance with digital PCR measurements. DOI 10.1128/aem.01020-26: https://pubmed.ncbi.nlm.nih.gov/42803564/

[H4] Verily Sightline assay and sampling service description, accessed 24 October 2026: https://verily.com/solutions/sightline

[H5] A nationwide wastewater monitoring pilot to identify legal and illegal substances and enable future substance use research; primary-paper indexed text identifies NIDA/Biobot, full-page access challenged during review: https://pmc.ncbi.nlm.nih.gov/articles/PMC13441254/

[H6] Chen et al., 2026, Modeling and Laboratory Experiments to Assess Detection of Plasmodium falciparum in Wastewater: Insights for Wastewater-Based Surveillance of Malaria, DOI 10.1021/acs.est.5c15901. Author-institution abstract: https://research.lstmed.ac.uk/en/publications/modeling-and-laboratory-experiments-to-assess-detection-of-plasmo/

[H7] Dengue field-study leads, not local service validation: https://pubmed.ncbi.nlm.nih.gov/39278232/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC12421656/ . Indexed primary-study text retrieved; PMC full-page access challenged during review.

[H8] CDC wastewater data limitations: https://www.cdc.gov/wastewater/about-data/index.html

Frozen parent paper: https://github.com/atlaslattice/open-regenerative-compute-standard/tree/e0e6fb6af781e023fb150cd5669cfeb848655f70/reports/corpus-network-v0_8
