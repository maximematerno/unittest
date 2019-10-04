import unittest
import sqrt
from sqrt import newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt

class SqrtTests(unittest.TestCase):
    
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_sqrt2(self):
        self.assertEqual(newton_sqrt1(2), 1.414213562373095)

class SquaringTest(unittest.TestCase):
    def test_thing(self):
        pass


if __name__== '__main__':
     unittest.main()    







