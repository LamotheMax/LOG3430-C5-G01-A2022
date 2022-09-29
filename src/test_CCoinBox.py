import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def setUp(self) -> None:
        self.coinbox = CCoinBox()


    def test_ajouter_25c_vente_permise(self):
        self.coinbox.monnaie_courante = 1

        self.coinbox.ajouter_25c()

        self.assertTrue(self.coinbox.vente_permise)


    def test_ajouter_25c_vente_interdite(self):
        self.coinbox.ajouter_25c()

        self.assertFalse(self.coinbox.vente_permise)


    def test_ajouter_25c_ajoute_une_seule_piece(self):
        self.coinbox.monnaie_courante = 0

        self.coinbox.ajouter_25c()

        self.assertEqual(self.coinbox.monnaie_courante, 1)


    def test_retourne_monnaie_vente_interdite(self):
        self.coinbox.vente_permise = False

        self.coinbox.retourne_monnaie()

        self.assertFalse(self.coinbox.vente_permise)
