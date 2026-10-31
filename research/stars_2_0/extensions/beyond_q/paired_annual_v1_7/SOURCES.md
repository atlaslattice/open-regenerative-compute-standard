# Source register — paired annual v1.7

Accessed 2026-10-31. SOURCE-TRACED documents remain design or product sources,
not measurements of the proposed dual-reactor campus.

1. **J.C. Hillesheim et al. (2026).** *Overview of the physics basis for the ARC
   fusion power plant*. Journal of Plasma Physics **92**, E69. Published
   4 June 2026. https://doi.org/10.1017/S0022377826101706.
   Section 3/table 4 and adjacent overall power-balance paragraphs specify
   about 1.13 GW D-T fusion (1133 MW empirical point), approximately 100 MW
   additional blanket heat and 20 MW plasma heating, approximately 1180 MW
   cycle-averaged thermal power, about 500 MW gross electricity and 100 MW own
   electrical demand, yielding about 400 MW net. Cycle: 900 s flattop plus 60 s
   between flattops. We use 1130 MW as the rounded design anchor. The heating
   method is ICRF/ohmic, not a laser. Its design output is not measured generation.
   D-D retrofit draw, recovery and breeding are not established by this paper.
   Plant load interpolation under fuel starvation and shutdown loads are our
   assumptions, not source-traced ARC operating curves.

2. **NIST Physical Measurement Laboratory.** *Atomic Weights and Isotopic
   Compositions for Helium*.
   https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=He.
   Relative atomic masses: He-3 3.0160293201(25); He-4 4.00260325413(6).
   Neutral-isotope molar-mass approximations convert atom counts to kg in the
   inherited accounting convention. Avogadro constant 6.02214076e23 mol^-1;
   exact elementary-charge conversion supplies J/MeV. STP reporting retains
   22.414 L/mol at 0 C/1 atm; gas liters are not liquid liters.

3. **Airgas.** *Research Grade Helium*, product HE RC63.
   https://www.airgas.com/product/Gases/Helium/p/HE%20RC63.
   Research specification: helium 99.9999%, with individual impurity limits
   including oxygen, water, hydrocarbons and nitrogen. Used as a qualification
   target only. Our assumed 90% quality-acceptance yield is the fraction of
   recovered mass hypothetically passing a specification; it does not mean
   90% chemical purity or prove research-grade certification. Residual D/T,
   radioactivity, impurities and delivery form require their own analysis.

4. **Atlas Lattice versioned code/data**, parent commit
   `fe10971566b35ae09b007a24ff8780d691ad31e7`:
   `multiscale_v1_4/fuelcycle/` and `inputs/scenarios.json`,
   `startup_year_v1_4_1/`, `wallplug_checkpoint_v1_5/`,
   `wallplug_year_v1_5_1/`, `isotope_value_v1_6/`.
   The prior source registers retain WarpX/OpenMC and fuel-cycle literature.
   The current module uses their candidate numerical source/recovery parameters,
   not new transport or kinetic execution. External source bytes are checked
   by `source_manifest.json`; `CORE_CHANGES.diff` documents the isolated engine
   extension. All unchanged historical artifacts remain intact.

## Unqualified engineering and economic inputs

A/B plasma residence, slowing-down parameters and inherited blanket yields;
A retrofit net draw; A duty assumptions; laser gain and wall-plug efficiency;
shutdown/extra campus loads; He-3/He-4 collection, capture and acceptance;
He-3 retained fraction; helium replacement need; electricity price; isotope
price and demand caps are assumptions or inherited candidate-model inputs.
No isotope price in this package is a current market quotation. No institution,
company or cited author is represented as endorsing the proposed campus.

5. **Jaydeep Deshpande / Commonwealth Fusion Systems (2026).** *How LIBRTI will help CFS verify our
   fusion fuel production technology*. The Tokamak Times,1July2026.
   https://blog.cfs.energy/how-librti-will-help-cfs-verify-our-fusion-fuel-production-technology/.
   Official description targets TBR>1 / net tritium production and startup fuel
   for future plants. No precise current ARC V3A TBR was located on this page.
   Its accessible description of net production is not substituted for the
   model's separate gross birth, extraction and permanent recovery definitions.

6. **UK Atomic Energy Authority (2026).** *CFS named first international partner
   in UKAEA's LIBRTI programme*. GOV.UK,1July2026.
   https://www.gov.uk/government/news/cfs-named-first-international-partner-in-ukaeas-librti-programme.
   Engineering-scale blanket testing and net-tritium-production goal, not a
   demonstrated ARC breeding result or an exact plant TBR. The ARC overview
   itself also says TBR>1 and notes blanket R&D will be reported elsewhere.

The report's source labels correspond to the numbered register items.
