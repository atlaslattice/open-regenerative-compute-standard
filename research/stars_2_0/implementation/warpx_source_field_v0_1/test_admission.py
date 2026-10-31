import copy,math,unittest
from admission import admit,input_fragment


def fixture():
    s=dict(jointness='JOINT_RECORDS',species='proton',frame='LAB',units={'position':'m','time':'s','kinetic_energy':'MeV','weight':'physical_particles'},normalization='ABSOLUTE_PHYSICAL_PARTICLES_PER_SNAPSHOT',evidence={'kind':'NUMERICAL_VERIFICATION','source_ref':'test_admission.py','input_sha256':'fixture-not-a-measurement'},snapshot_time_s=0,records=[dict(id='p1',weight=7,kinetic_MeV=.675,position_m=[0,0,0],unit_direction_LAB=[0,0,1],time_s=0)])
    f=dict(grid_unit_SI=1,component_unit_SI=[1,1,1],axis_labels=['x','y','z'],map_sha256='fixture',source_ref='test_admission.py',domain_lo_m=[-1,-1,-1],domain_hi_m=[1,1,1],time_dependence='STATIC')
    return s,f


class TestAdmission(unittest.TestCase):
    def test_weight_and_energy_preserved(self):
        s,f=fixture();r=admit(s,f);self.assertEqual(r['physical_proton_weight'],7)
        u=r['packets'][0]['normalized_u'][2]
        from scipy.constants import m_p,c,e
        # stable inverse kinetic energy
        k=m_p*c*c*u*u/(math.sqrt(1+u*u)+1)/(1e6*e)
        self.assertAlmostEqual(k,.675,places=13)
    def test_marginal_not_promoted(self):
        s,f=fixture();s['jointness']='ENERGY_SPECTRUM_ONLY'
        with self.assertRaises(ValueError):admit(s,f)
    def test_relative_not_absolute(self):
        s,f=fixture();s['normalization']='PDF'
        with self.assertRaises(ValueError):admit(s,f)
    def test_missing_not_zero(self):
        s,f=fixture();s['records']=None
        with self.assertRaises(ValueError):admit(s,f)
    def test_zero_retained(self):
        s,f=fixture();s['records']=[];r=admit(s,f)
        self.assertEqual(r['physical_proton_weight'],0);self.assertIn('KNOWN_ZERO',input_fragment(r))
    def test_no_silent_normalization(self):
        s,f=fixture();s['records'][0]['unit_direction_LAB']=[0,0,2]
        with self.assertRaises(ValueError):admit(s,f)
    def test_nonfinite_and_negative(self):
        for k,v in [('weight',-1),('weight',math.nan),('kinetic_MeV',-1),('kinetic_MeV',math.inf),('weight',True)]:
            s,f=fixture();s['records'][0][k]=v
            with self.subTest(k=k,v=v),self.assertRaises(ValueError):admit(s,f)
    def test_map_unit_metadata_rejected(self):
        s,f=fixture();f['grid_unit_SI']=.001
        with self.assertRaises(ValueError):admit(s,f)
    def test_axis_order_rejected(self):
        s,f=fixture();f['axis_labels']=['z','y','x']
        with self.assertRaises(ValueError):admit(s,f)
    def test_component_units_rejected(self):
        s,f=fixture();f['component_unit_SI']=[.001,.001,.001]
        with self.assertRaises(ValueError):admit(s,f)
    def test_out_of_domain(self):
        s,f=fixture();s['records'][0]['position_m']=[1000,0,0]
        with self.assertRaises(ValueError):admit(s,f)
    def test_mixed_times_rejected(self):
        s,f=fixture();s['records'][0]['time_s']=1
        with self.assertRaises(ValueError):admit(s,f)
    def test_time_dependent_restart_rejected(self):
        s,f=fixture();s['snapshot_time_s']=1;s['records'][0]['time_s']=1;f['time_dependence']='DYNAMIC'
        with self.assertRaises(ValueError):admit(s,f)
    def test_static_clock_rebase_explicit(self):
        s,f=fixture();s['snapshot_time_s']=1;s['records'][0]['time_s']=1
        self.assertEqual(admit(s,f)['simulation_clock_zero_corresponds_to_source_time_s'],1)
    def test_missing_source_lineage(self):
        s,f=fixture();s['evidence']['input_sha256']=None
        with self.assertRaises(ValueError):admit(s,f)
    def test_duplicate_ids(self):
        s,f=fixture();s['records']*=2
        with self.assertRaises(ValueError):admit(s,f)
    def test_codegen_units(self):
        s,f=fixture();r=admit(s,f);self.assertIn('proton.multiple_particles_uz',input_fragment(r))
        self.assertIn('proton.multiple_particles_weight = 7',input_fragment(r))

if __name__=='__main__':unittest.main()
