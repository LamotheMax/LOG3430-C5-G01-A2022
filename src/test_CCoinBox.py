import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)
        
    def test_add50():
        cb = CCoinBox()
        cb.ajouter_25c()
        cb.ajouter_25c()
        self.assertTrue(cb.get_monnaie_totale()==0)
        self.assertTrue(cb.get_monnaie_courante()==2)
        self.assertTrue(cb.get_vente_permise())

