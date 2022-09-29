import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)
    
    def test_ajouter_25c_vente_permise(self):
        coinbox = CCoinBox()

        coinbox.ajouter_25c()

        self.assertFalse(coinbox.vente_permise)

        coinbox.ajouter_25c()

        self.assertTrue(coinbox.vente_permise)

    def test_add50(self):
        cb = CCoinBox()
        cb.monnaie_courante = 1
        cb.ajouter_25c()
        self.assertEqual(True, cb.get_vente_permise())
