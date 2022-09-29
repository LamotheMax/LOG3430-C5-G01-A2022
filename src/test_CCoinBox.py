import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)

    def test_add50(self):
        cb = CCoinBox()
        cb.monnaie_courante = 1
        cb.ajouter_25c()
        self.assertEqual(True, cb.get_vente_permise())
        
    def test_monnaie_courante(self):
        cb = CCoinBox()
        cb.ajouter_25c()
        self.assertEqual(1,cb.get_monnaie_courante())
        
    def test_vente_retour(self):
        cb = CCoinBox()
        cb.retourne_monnaie()
        self.assertFalse(cb.get_vente_permise())
        
    def test_vente_25c(self):
        cb = CCoinBox()
        cb.ajouter_25c()
        self.assertFalse(cb.get_vente_permise())
