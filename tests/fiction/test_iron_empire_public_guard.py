"""Synthetic tests for the public-source gate; real repo sources checked separately."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT=Path(__file__).resolve().parents[2]/"tools/fiction/iron_empire_public_guard.py"
spec=importlib.util.spec_from_file_location("iron_empire_guard",SCRIPT)
guard=importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)

FIXTURES={
"v04":"""**2062:** Humanity notices anomalous signatures.
**2069:** A damaged Imperial fleet emerges unexpectedly in Sol.
**Continuity:** Enemy true species identity/naming revealed only in Film VI.""",
"v05":"""**Preservation:** An additive revision note, NOT a silent replacement of v0.4.
**Film II:** Emperor alone lawfully authorizes publication after review.
**Film III:** Caesar-like assassination of the Emperor.
No accession by the end of Film V. The actual imperial accession and coronation take place in Film VI.""",
"v06":"""Suspended animation is a major partial explanation for longevity and survival.""",
"nov06":"""AUTHOR-DIRECTED CONTINUITY DELTA / NOT APPLIED TO EXISTING BIBLE
Film II / Book 2 is partly a prequel to ancient Mars.
The Martian Empire glassed its own planet.
Book/Film III is when partners resurrect Mars through restoration/terraforming.
The former executioner, now Minister of Trees, must work with Steve.""",
}

class PublicSourceGuardTests(unittest.TestCase):
    def setUp(self):
        self.temporary=tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root=Path(self.temporary.name)
        folder=self.root/guard.FOLDER
        folder.mkdir(parents=True)
        for key,value in FIXTURES.items():
            (folder/guard.SOURCES[key]).write_text(value,encoding="utf-8")

    def find(self,number):
        return next(c for c in guard.audit(self.root)["checks"] if c["id"]==number)

    def test_fourteen_rules_execute(self):
        r=guard.audit(self.root)
        self.assertEqual((r["total"],r["passed"],r["failed"]),(14,14,0))
        self.assertFalse(r["canon_ratified"])
        self.assertFalse(r["network_called"])
        self.assertFalse(r["private_play_imported"])

    def test_missing_source_fails(self):
        (self.root/guard.FOLDER/guard.SOURCES["nov06"]).unlink()
        self.assertGreater(guard.audit(self.root)["failed"],0)

    def test_film_ii_audit_shift_fails(self):
        p=self.root/guard.FOLDER/guard.SOURCES["v05"]
        p.write_text(p.read_text().replace("Film II","Film IV"),encoding="utf-8")
        self.assertFalse(self.find("IE-PUB-03")["passed"])

    def test_mars_prequel_shift_fails(self):
        p=self.root/guard.FOLDER/guard.SOURCES["nov06"]
        p.write_text(p.read_text().replace("Film II / Book 2","Film IV / Book 4"),encoding="utf-8")
        self.assertFalse(self.find("IE-PUB-09")["passed"])

    def test_mars_restoration_shift_fails(self):
        p=self.root/guard.FOLDER/guard.SOURCES["nov06"]
        p.write_text(p.read_text().replace("Book/Film III","Book/Film II"),encoding="utf-8")
        self.assertFalse(self.find("IE-PUB-11")["passed"])

    def test_no_private_content_import(self):
        source=SCRIPT.read_text(encoding="utf-8")
        self.assertNotIn("swarm_read_room",source)
        self.assertNotIn("requestId",source)
        self.assertNotIn("SECRET_PLACEHOLDER_NOT_PRESENT",source)

if __name__=="__main__":
    unittest.main()
