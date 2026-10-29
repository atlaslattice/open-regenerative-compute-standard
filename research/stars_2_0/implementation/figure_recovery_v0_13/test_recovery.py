"""Recovery integrity checks, not tests of fusion or apparatus performance."""
import copy
import tempfile
import unittest
from pathlib import Path

import fitz
import numpy as np

from recover import SOURCES, HE_PANELS, axis_x, checked_source, path_vertices, run

ROOT=Path(__file__).parent

class RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not all((ROOT/'sources'/n).exists() for n in SOURCES):
            raise unittest.SkipTest('Download pinned PDFs with recover.py --download first')
        cls.tmp=tempfile.TemporaryDirectory()
        cls.he,cls.nuclear,cls.metrics=run(ROOT/'sources',Path(cls.tmp.name)/'run')

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls,'tmp'):cls.tmp.cleanup()

    def test_source_mutation_rejected(self):
        p=Path(self.tmp.name)/'changed.pdf';p.write_bytes(b'wrong-source')
        with self.assertRaises(ValueError):checked_source(p,'Kuhlwein2022.pdf')

    def test_axes_land_on_labeled_ticks(self):
        for p in HE_PANELS:
            self.assertEqual(axis_x(p['x_tick_0p5'],p),.5)
            self.assertEqual(axis_x(p['x_tick_1p5'],p),1.5)

    def test_nonmonotone_path_rejected(self):
        d={'items':[('l',fitz.Point(1,1),fitz.Point(0,2))]}
        with self.assertRaises(ValueError):path_vertices(d)

    def test_bezier_uses_curve_not_control_polygon(self):
        d={'items':[('c',fitz.Point(0,0),fitz.Point(0,1),fitz.Point(1,1),fitz.Point(1,0))]}
        a=path_vertices(d)
        np.testing.assert_allclose(a[16],[.5,.75])

    def test_unseen_histogram_bins_not_zero_counts(self):
        missing=[b for p in self.he['records'] for b in p['bins'] if b['status']=='UNRESOLVED_NOT_ZERO']
        self.assertGreater(len(missing),0)
        self.assertTrue(all(b['approx_display_count'] is None for b in missing))

    def test_coverage_not_invented(self):
        self.assertFalse(self.he['He_7p5_MeV_qualified'])
        self.assertFalse(self.he['full_calibration_inventory_recovered'])
        self.assertEqual([p['E_MeV'] for p in self.he['records']],[.23,.56,2.25,4.52])

    def test_last_helium_histogram_keeps_contamination(self):
        self.assertIn('not pure helium',self.he['records'][-1]['contamination'])
        self.assertIsNone(self.he['records'][-1]['summary']['full_histogram_mean_um'])

    def test_vector_frame_and_semantics(self):
        self.assertEqual(len(self.nuclear['traces']),6)
        for t in self.nuclear['traces']:
            self.assertAlmostEqual(t['energy_cm_MeV'][0],.030,delta=.0001)
            self.assertAlmostEqual(t['energy_cm_MeV'][-1],5.970,delta=.0001)
        self.assertEqual(self.nuclear['independent_data_sets'],1)
        self.assertIsNone(self.nuclear['actual_counts'])

    def test_data_repeats_are_same_not_independent_observations(self):
        ts=[t for t in self.nuclear['traces'] if t['role']=='data']
        grid=np.linspace(.031,5.969,500)
        ys=[np.interp(grid,t['energy_cm_MeV'],t['relative_display_height']) for t in ts]
        for y in ys[1:]:self.assertLess(float(np.max(abs(y-ys[0]))),.0001)

    def test_repeated_run_bytes(self):
        other=Path(self.tmp.name)/'repeat';run(ROOT/'sources',other)
        for p in (Path(self.tmp.name)/'run').iterdir():self.assertEqual(p.read_bytes(),(other/p.name).read_bytes())

if __name__=='__main__':unittest.main(verbosity=2)
