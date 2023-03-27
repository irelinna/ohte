import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    #setup

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.edulliset = 0
        self.kassapaate.maukkaat = 0

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    #käteistestit

    def test_syo_edullisesti_kateisella(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kateisella_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #korttitestit

    def test_syo_edullisesti_kortilla_vahentaa_saldoa_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kortilla_vahentaa_saldoa_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(350)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.50 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        

    #lataa rahaa testi

    def test_lataa_rahaa_toimii(self):
        kortti = Maksukortti(1000)
        self.assertNotEqual(self.kassapaate.lataa_rahaa_kortille(kortti,-500))
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(kortti,500))
        self.assertEqual(kortti.saldo,1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100500)
        
        