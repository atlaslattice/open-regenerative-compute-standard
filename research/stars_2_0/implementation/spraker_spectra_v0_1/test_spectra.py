import copy
from pathlib import Path
import tempfile
import unittest
import extract_spectra as s

class SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.book=s.load_source(Path(__file__).parent/'sources',2)
        cls.rows=s.extract_all(cls.book)

    def anchor(self):
        return next(r for r in self.rows if r['record_id']=='90:B54')

    def prediction(self):
        r=self.anchor()
        return dict(record_id=r['record_id'],frame='CM',observable=r['observable'],prediction_CM_mb_sr_per_source_bin=r['X_CM_mb_sr_per_source_bin'])

    def test_dimensions_and_coverage(self):
        self.assertEqual(len(self.rows),22100)
        self.assertEqual(sum(r['coverage']!='WITHIN_ARTICLE_ENERGY_RANGE' for r in self.rows),1600)

    def test_published_anchor(self):
        r=self.anchor()
        self.assertEqual(r['E_proton_LAB_MeV'],1.4)
        self.assertAlmostEqual(r['E_alpha_CM_center_MeV'],4.635)
        self.assertEqual(r['X_CM_mb_sr_per_source_bin'],4.2779)
        self.assertEqual(round(r['X_CM_mb_sr_per_source_bin'],2),4.28)

    def test_every_cell_preserved(self):
        for name in s.ANGLES:
            source=self.book.sheet_by_name(name); errors=self.book.sheet_by_name(name+'err')
            got=[r for r in self.rows if r['sheet']==name]
            for r,(i,j) in zip(got,((i,j) for i in range(2,102) for j in range(1,28)),strict=True):
                self.assertEqual(r['X_CM_mb_sr_per_source_bin'],source.cell_value(i,j))
                self.assertEqual(r['statistical_error_CM_mb_sr'],errors.cell_value(i,j))

    def test_frame_guard(self):
        p=self.prediction();p['frame']='LAB'
        with self.assertRaisesRegex(ValueError,'frame'):s.compare_predictions(self.rows,[p])

    def test_normalized_density_guard(self):
        p=self.prediction();p['observable']='PROBABILITY_DENSITY'
        with self.assertRaises(ValueError):s.compare_predictions(self.rows,[p])

    def test_residual_units_and_sign(self):
        p=self.prediction();p['prediction_CM_mb_sr_per_source_bin']+=self.anchor()['statistical_error_CM_mb_sr']
        self.assertAlmostEqual(s.compare_predictions(self.rows,[p])['rows'][0]['standardized_residual_STAT_ONLY'],1)

    def test_reject_duplicate_and_unqualified_zero(self):
        p=self.prediction()
        with self.assertRaises(ValueError):s.compare_predictions(self.rows,[p,p])
        p['record_id']='90:B3'
        with self.assertRaises(ValueError):s.compare_predictions(self.rows,[p])

    def test_mutated_error_axis(self):
        class Book:
            def sheet_by_name(_,name):
                sheet=copy.copy(self.book.sheet_by_name(name))
                if name=='90err':
                    original=sheet.cell_value
                    sheet.cell_value=lambda i,j:original(i,j)+1 if (i,j)==(0,1) else original(i,j)
                return sheet
        with self.assertRaisesRegex(ValueError,'energy mismatch'):s.extract_pair(Book(),'90','90err')

    def test_corrupt_source(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/'MOESM2.xls').write_bytes(b'bad source')
            with self.assertRaisesRegex(ValueError,'identity'):s.load_source(d,2)

if __name__=='__main__':unittest.main()
