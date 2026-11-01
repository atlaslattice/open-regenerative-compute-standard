import math, unittest
from geometry import inside, analytic_volume, validate, material_ready, warpx_mask

class GeometryTests(unittest.TestCase):
    def setUp(self): self.p=dict(inner_radius_m=1.,wall_m=.1,aperture_radius_m=.2)
    def test_center_void(self): self.assertFalse(inside(self.p,0,0,0))
    def test_entrance_open(self): self.assertFalse(inside(self.p,0,0,1.05))
    def test_opposite_wall_retained(self): self.assertTrue(inside(self.p,0,0,-1.05))
    def test_equator_wall(self): self.assertTrue(inside(self.p,1.05,0,0))
    def test_outside(self): self.assertFalse(inside(self.p,2,0,0))
    def test_inner_boundary(self): self.assertFalse(inside(self.p,1,0,0))
    def test_bad_aperture(self):
        with self.assertRaises(ValueError): validate({**self.p,'aperture_radius_m':2})
    def test_nonfinite(self):
        with self.assertRaises(ValueError): inside(self.p,math.nan,0,0)
    def test_unknown_material(self):
        with self.assertRaises(ValueError): material_ready({})
    def test_unqualified_datasets(self):
        with self.assertRaises(ValueError): material_ready(dict(density_kg_m3=1,boron_mass_fraction=1,b11_atom_fraction=1))
    def test_volume_bounds(self):
        v=analytic_volume(self.p); full=4*math.pi/3*(1.1**3-1)
        self.assertGreater(v,full/2); self.assertLess(v,full)
    def test_si_scale(self):
        q={k:v*1e-6 for k,v in self.p.items()}
        self.assertAlmostEqual(analytic_volume(q)/analytic_volume(self.p),1e-18,delta=1e-30)
    def test_mask_same_points(self):
        # Restricted evaluation of our own generated expression, not untrusted input.
        expr=warpx_mask(self.p)
        for x,y,z in [(0,0,0),(0,0,1.05),(0,0,-1.05),(1.05,0,0),(2,0,0)]:
            self.assertEqual(bool(eval(expr,{'__builtins__':{}},dict(x=x,y=y,z=z))),inside(self.p,x,y,z))

if __name__=='__main__': unittest.main()
