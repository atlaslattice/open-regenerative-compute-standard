"""A control without an archived comparator must not report a comparison pass."""
import json,subprocess,sys,tempfile,unittest
from pathlib import Path
class Guard(unittest.TestCase):
 def test_unregistered_collector_setting_rejected(self):
  package=Path(__file__).resolve().parent
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);p=json.loads((package/'PROFILE.json').read_text());p['ideal_rear_collector_bias_MV']=.75;profile=root/'profile.json';profile.write_text(json.dumps(p))
   r=subprocess.run([sys.executable,str(package/'run_v004.py'),'--models',str(package.parent),'--profile',str(profile),'--out',str(root/'run')],capture_output=True,text=True)
   self.assertNotEqual(r.returncode,0);self.assertIn('UNREGISTERED_CONTROL_NO_SAVED_COLLECTOR_REFERENCE',r.stderr)
if __name__=='__main__':unittest.main()
