import cmath,copy,json,math,tempfile,unittest
from pathlib import Path
from stellar_forge_reference import acoustics
from stellar_forge_reference.runner import read_json,run
from stellar_forge_reference.ui import build
ROOT=Path(__file__).resolve().parents[1]
class Acoustic(unittest.TestCase):
    def config(self):return read_json(ROOT/'examples/pb11_reference.json')['acoustic']
    def test_independent_analytic_transient(self):
        c=self.config();c.update(waveform='tone',carrier_Hz=100,deviation_Hz=0,mode_Hz=150,damping_ratio=.1,duration_s=.2,start_before_shot_s=.2,samples=4000)
        rows=acoustics.integrate(c,c['samples']);w=2*math.pi*100;w0=2*math.pi*150;g=2*.1*w0;wd=math.sqrt(w0*w0-g*g/4)
        A=.1/complex(w0*w0-w*w,g*w);C=-A;D=(g*C/2-1j*w*A)/wd
        err=0
        for i,row in enumerate(rows):
            t=i*.2/4000
            expected=(A*cmath.exp(1j*w*t)+math.exp(-g*t/2)*(C*math.cos(wd*t)+D*math.sin(wd*t))).imag
            err=max(err,abs(row[2]-expected))
        self.assertLess(err,1e-12)
    def test_off_sham_reference_zero_coherent_response(self):
        for arm in ['OFF','SHAM','REFERENCE']:
            c=self.config();c['arm']=arm
            if arm!='SHAM':c['driver_wall_J']=0
            self.assertEqual(acoustics.run(c)['peak_displacement_m'],0)
    def test_fm_zero_deviation_matches_tone(self):
        c=self.config();c['deviation_Hz']=0;a=acoustics.run(c);c['waveform']='tone';b=acoustics.run(c)
        self.assertEqual(a['trace'],b['trace'])
    def test_scaling(self):
        c=self.config();a=acoustics.run(c);c['acceleration_m_s2']*=2;b=acoustics.run(c)
        self.assertAlmostEqual(2*a['peak_displacement_m'],b['peak_displacement_m'],places=15)
    def test_sampling_guard(self):
        c=self.config();c['samples']=100
        with self.assertRaises(ValueError):acoustics.run(c)
    def test_invalid_timing_location(self):
        for key,val in [('location','nucleus'),('start_before_shot_s',0)]:
            c=self.config();c[key]=val
            with self.assertRaises(ValueError):acoustics.run(c)
    def test_location_does_not_invent_physics(self):
        c=self.config();a=acoustics.run(c);c['location']='catcher';b=acoustics.run(c)
        self.assertEqual(a['peak_displacement_m'],b['peak_displacement_m'])
    def test_acoustics_do_not_modify_transport(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);c=read_json(ROOT/'examples/pb11_reference.json');f=p/'c.json';f.write_text(json.dumps(c));a=run(f,p/'a')
            c['acoustic']['carrier_Hz']=900;f.write_text(json.dumps(c));b=run(f,p/'b')
            self.assertEqual(a['transmission'],b['transmission']);self.assertEqual(a['detector'],b['detector'])
            self.assertNotEqual(a['integrated_extensions']['acoustic']['peak_displacement_m'],b['integrated_extensions']['acoustic']['peak_displacement_m'])
    def test_ui_create_no_overwrite(self):
        with tempfile.TemporaryDirectory() as t:
            f=Path(t)/'ui.html';c=read_json(ROOT/'examples/pb11_reference.json');build(c,f)
            self.assertIn('sinusoidal_FM',f.read_text())
            with self.assertRaises(FileExistsError):build(c,f)
    def test_parse_failure_receipt(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);f=p/'c.json';f.write_text('{')
            with self.assertRaises(ValueError):run(f,p/'out')
            self.assertEqual(read_json(p/'out/FAILURE.json')['failure_code'],'FAIL_INPUT_INVALID')
if __name__=='__main__':unittest.main()
