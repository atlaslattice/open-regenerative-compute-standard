"""Public-safe speculative Iron Empire × HSN positional review (no source bodies)."""
from __future__ import annotations
import json,re,unittest
from pathlib import Path

FILE = Path(__file__).parents[2] / 'docs/fiction/iron_empire/ARIADNE_HSN_RESEARCH_OVERLAY_v09.json'
DOC = FILE.with_suffix('.md')

class TestOverlay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = json.loads(FILE.read_text())
        cls.text = DOC.read_text()
    def test_named_house_lenses(self):
        self.assertEqual(len(self.o['houses']),12)
        self.assertEqual(len({h['reviewLens'] for h in self.o['houses']}),12)
    def test_coordinate_cardinality(self):
        self.assertEqual(self.o['totalNodePositions'],1728)
        self.assertEqual(self.o['totalHouseSlots'],12)
        self.assertEqual(self.o['totalSphereSlots'],144)
    def test_all_authentic_coordinate_shapes(self):
        sph=[]
        for i,h in enumerate(self.o['houses'],1):
            self.assertEqual(h['house'],f'H{i:02d}')
            self.assertEqual(h['nodePositions'],144)
            self.assertEqual(len(h['domainSphereSlots']),7)
            self.assertEqual(len(h['epistemicSphereSlots']),5)
            self.assertFalse(h['sourceSemanticsVerified'])
            self.assertEqual(h['reviewStatus'],'PROPOSED_ONLY')
            self.assertEqual(h['editorialAuthority'],'NONE')
            for s in h['domainSphereSlots']+h['epistemicSphereSlots']:
                self.assertRegex(s,r'^H(?:0[1-9]|1[0-2])\.S(?:0[1-9]|1[0-2])$')
                sph.append(s)
        self.assertEqual(len(set(sph)),144)
        self.assertEqual(sum(len(h['domainSphereSlots']) for h in self.o['houses']),84)
        self.assertEqual(sum(len(h['epistemicSphereSlots']) for h in self.o['houses']),60)
    def test_source_editions_pin_not_attest(self):
        self.assertRegex(self.o['registryDigest'],r'^[a-f0-9]{64}$')
        self.assertFalse(self.o['sourceOriginalBytesEmbedded'])
    def test_no_approved_scientific_or_canon_claim(self):
        for k in ('empiricalOpenAlexResultsFetched','approvedTopicLinks','completedFilmEdits','residentAppointments'):
            self.assertEqual(self.o[k],0)
        self.assertFalse(self.o['canonChanged'])
        self.assertEqual(self.o['status'],'AUTHOR_REVIEW_REQUIRED')
    def test_house_10_11_12_preserved(self):
        self.assertIn('Indigenous',self.o['houses'][9]['name'])
        self.assertIn('Rights',self.o['houses'][10]['name'])
        self.assertIn('Space',self.o['houses'][11]['name'])
    def test_film_boundary_explicit(self):
        for term in ['Film II','Film III','Film IV','Film V','Film VI','Long Peace','uncrowned','coronation']:
            self.assertIn(term,self.text)
    def test_rights_and_nonharvesting(self):
        for term in ['private Brain','Palace','rights','CANON']:
            self.assertIn(term,self.text)
if __name__=='__main__': unittest.main()
