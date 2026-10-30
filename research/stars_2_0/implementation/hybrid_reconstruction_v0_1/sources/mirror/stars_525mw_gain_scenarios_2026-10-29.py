"""525 MW sensitivity analysis layered on prior Stars 3-module toy. Not a calibrated reactor prediction.
Interpretations: (1) 525 MW *net* baseline, assuming gain scales net electricity;
(2) 525 MW *gross fusion* baseline, with illustrative 40% electric efficiency,
    fixed 50 MW auxiliaries and 20 MW extra per additional gross-fusion GW.
These choices are scenarios, not measured design parameters.
"""
from pathlib import Path
import pandas as pd
BASE=Path(__file__).parent
raw=pd.read_csv(BASE/'stars_prism_three_module_toy_2026-10-29.csv')
ref=raw.loc[raw.scenario=='single_pass_no_mirror','fusion_events_per_pulse'].iloc[0]
scenario=raw[['scenario','fusion_events_per_pulse','capture_assumed','mirror_ratio']].copy()
scenario['gain']=scenario.fusion_events_per_pulse/ref
for gain in [0.5,0.75,1.0,1.2,1.5,1.8,2.54,3,4,6]:
    scenario.loc[len(scenario)]=[f'illustrative_{gain:g}x',ref*gain,None,None,gain]
scenario['net_MW_if_525MW_net_scales_directly']=525*scenario.gain
scenario['gross_fusion_MW_if_525MW_fusion']=525*scenario.gain
scenario['net_electric_MW_illustrative']=.40*scenario.gross_fusion_MW_if_525MW_fusion - 50 - .02*(scenario.gross_fusion_MW_if_525MW_fusion-525).clip(lower=0)
scenario['annual_TWh_direct_90pct']=scenario.net_MW_if_525MW_net_scales_directly*8760*.9/1e6
scenario['annual_TWh_illustrative_net_90pct']=scenario.net_electric_MW_illustrative*8760*.9/1e6
scenario['evidence']='POTENTIAL_DERIVED_ILLUSTRATIVE_NOT_VALIDATED'
scenario.to_csv(BASE/'stars_525mw_gain_scenarios_2026-10-29.csv',index=False)
print(scenario[['scenario','gain','net_MW_if_525MW_net_scales_directly','net_electric_MW_illustrative']].to_string(index=False,float_format=lambda x:f'{x:.3f}'))
