import unittest
from observable_estado import *


class SimpleTestCase(unittest.TestCase):
    def testparticula(self):
        vec = [(-3, -1), (0, -2), (0, 1), (2, 0)]
        res = 0.052632
        assert particula(vec) == res
        
    def testspin(self):
        vec = [(3, -4), (7, 2)]
        res = (0.32, 0.68)
        assert spin(vec) == res
        
    def testnormalizar(self):
        vec = [(2, -3), (1, 2)]
        res = [(0.47141, -0.70711), (0.2357, 0.47141)]
        assert normalizar(vec) == res




if __name__ == "__main__":
    unittest.main()
