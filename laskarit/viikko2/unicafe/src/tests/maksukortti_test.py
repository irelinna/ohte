import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_toimii(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_ota_rahaa_toimii(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.00 euroa")

    def test_ota_rahaa_ei_toimi_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_raha_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(900),True)

    def test_metodi_palauttaa_false_jos_raha_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100),False)