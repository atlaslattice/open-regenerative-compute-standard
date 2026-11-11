"""Reproduce cost shares; do not reinterpret them as D-D/DT commonality."""
import csv
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'evidence/ARC_TABLE11_v0_1.csv').open()))
vv=next(x for x in rows if x['component']=='Replaceable VV Subtotal')
total=next(x for x in rows if x['component']=='Grand Total')
cost_share_low=float(vv['fabricated_cost_low_MUSD_FY2014'])/float(total['fabricated_cost_high_MUSD_FY2014'])
cost_share_high=float(vv['fabricated_cost_high_MUSD_FY2014'])/float(total['fabricated_cost_low_MUSD_FY2014'])
mass_share=float(vv['mass_tonnes'])/float(total['mass_tonnes'])
result={'table_source':'arXiv:1409.3540v2 Table 11 PDF page 30',
 'VV_fraction_of_tabulated_fabricated_cost':[cost_share_low,cost_share_high],
 'VV_fraction_of_tabulated_mass':mass_share,
 'outside_VV_fraction_of_tabulated_fabricated_cost':[1-cost_share_high,1-cost_share_low],
 'outside_VV_fraction_of_tabulated_mass':1-mass_share,
 'DD_DT_plant_commonality':'UNKNOWN',
 'permanent_shared_hardware':'NOT_ESTABLISHED_BY_COST_SHARE',
 'row_sum_VV_fabricated_MUSD':sum(float(x['fabricated_cost_low_MUSD_FY2014']) for x in rows if x['group']=='VV'),
 'printed_VV_fabricated_MUSD':float(vv['fabricated_cost_low_MUSD_FY2014']),
 'rounding_rule':'preserve source rounded totals; do not silently force row sums'}
(root/'results/arc_cost_share_v0_1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
