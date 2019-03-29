import unittest
from ValoresPropios_Probabilidad import *


class SimpleTestCase(unittest.TestCase):
      
    def estados_propios(self):
        M = [[(1, 0), (0, -1)], [(0, 1), (2, 0)]]
        v = [[(0.707, 0), (0, 0.707)]]
        estados_propios(M, v)

    def testvarianza(self):
        M = [[(1, 0), (0, -1)], [(0, 1), (2, 0)]]
        v = [[(0.707, 0), (0, 0.707)]]
        res = 2.5
        assert varianza(M, v) == res



    def testproba(self):
        h = 2
        ket = [(1, 0), (0, 0), (1, 0), (0, 0), (1, 0), (1, 0)]
        r = 0.25
        x = proba(h, ket)
        assert x == r


if __name__ == "__main__":
    unittest.main()
