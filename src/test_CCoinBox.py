import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def setUp(self):
        self.cb = CCoinBox()

    def test_add50(self):
        self.cb.monnaie_courante = 1
        self.cb.ajouter_25c()
        self.assertEqual(True, self.cb.get_vente_permise())

    def test_add25_bug_sur_ligne_10(self):
        self.cb.ajouter_25c()
        self.assertEqual(self.cb.get_monnaie_courante(), 1)

    def test_add25_sur_ligne_11(self):
        self.cb.ajouter_25c()
        self.assertFalse(self.cb.get_vente_permise())

    def test_retourne_monnaie(self):
        self.cb.retourne_monnaie()
        self.assertFalse(self.cb.get_vente_permise())
