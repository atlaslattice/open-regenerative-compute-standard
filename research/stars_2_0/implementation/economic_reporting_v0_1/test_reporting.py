import copy
import unittest
from reporting import report, footer

COSTS={k:'0' for k in ['electricity','extraction','purification','storage','transport','capital_allocation','other_operations']}
P={'inventory_id':'synthetic-disjoint-stock-1','product_id':'fictional-product', 'quantity_unit':'g',
   'product_specification':'fictional-spec','evidence':'MODELED','born_quantity':'1','saleable_quantity':'.5',
   'price_snapshot':{'snapshot_id':'synthetic-1','quote_date':'2026-10-01','access_date':'2026-10-28',
    'currency':'USD','quantity_unit':'g','product_specification':'fictional-spec','kind':'SYNTHETIC',
    'source':'synthetic fixture; no market claim','USD_per_unit':'10'}}

def run(products=None,costs=None):
    return report('fixture','FAIL','2026-10-28', [copy.deepcopy(P)] if products is None else products,
                  dict(COSTS) if costs is None else costs)

class Tests(unittest.TestCase):
    def test_failure_kept_with_positive_potential_value(self):
        c=dict(COSTS,electricity='2')
        r=run(costs=c)
        self.assertEqual((r['scientific_outcome'],r['potential_net_USD']),('FAIL','3.0'))
        self.assertIsNone(r['realized_revenue_USD'])
    def test_unpriced_not_zero(self):
        p=copy.deepcopy(P);p['price_snapshot']=None
        r=run([p]);self.assertIsNone(r['products'][0]['potential_gross_USD'])
        self.assertIsNone(r['potential_net_USD']);self.assertFalse(r['all_products_valued'])
    def test_birth_not_saleable(self):
        p=copy.deepcopy(P);p['saleable_quantity']=None
        self.assertIsNone(run([p])['potential_net_USD'])
    def test_missing_cost_not_profit(self):
        self.assertIsNone(run(costs=dict(COSTS,purification=None))['potential_net_USD'])
    def test_duplicate_stock_rejected(self):
        with self.assertRaises(ValueError):run([P,P])
    def test_bad_price_fields_rejected(self):
        for key,val in [('currency','EUR'),('quantity_unit','kg'),('product_specification','wrong'),
                        ('quote_date','2026-10-29'),('USD_per_unit','NaN'),('source','')]:
            p=copy.deepcopy(P);p['price_snapshot'][key]=val
            with self.subTest(key=key),self.assertRaises(ValueError):run([p])
    def test_negative_inventory_rejected(self):
        p=copy.deepcopy(P);p['saleable_quantity']='-1'
        with self.assertRaises(ValueError):run([p])
    def test_overallocated_inventory_rejected(self):
        p=copy.deepcopy(P);p['saleable_quantity']='2'
        with self.assertRaises(ValueError):run([p])
    def test_aged_quote_visible(self):
        r=run();self.assertEqual(r['products'][0]['quote_age_days'],27)
        self.assertIn('SYNTHETIC',footer(r));self.assertIn('FAIL',footer(r))

if __name__=='__main__':unittest.main()
