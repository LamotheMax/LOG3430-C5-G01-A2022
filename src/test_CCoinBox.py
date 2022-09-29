import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_ajouter_25c_vente_permise(self):
        coinbox = CCoinBox()
        coinbox.monnaie_courante = 1

        coinbox.ajouter_25c()

        self.assertTrue(coinbox.vente_permise)


    def test_ajouter_25c_vente_interdite(self):
        coinbox = CCoinBox()

        coinbox.ajouter_25c()

        self.assertFalse(coinbox.vente_permise)


    def test_ajouter_25c_ajoute_une_seule_piece(self):
        coinbox = CCoinBox()

        coinbox.monnaie_courante = 0

        coinbox.ajouter_25c()

        self.assertEqual(coinbox.monnaie_courante, 1)


    def test_retourne_monnaie_vente_interdite(self):
        coinbox = CCoinBox()

        coinbox.vente_permise = False

        coinbox.retourne_monnaie()

        self.assertFalse(coinbox.vente_permise)
