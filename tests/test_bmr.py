import unittest
from HealthyCalc.bmr import CalcBmr

class TestBmrFunction(unittest.TestCase):

    def test_CalcBmr_male(self):
        self.assertEqual(CalcBmr("male", 70, 175, 25), 1673.75)

    def test_CalcBmr_female(self):
        self.assertEqual(CalcBmr("female", 60, 160, 30), 1289.0)

if __name__ == '__main__':
    unittest.main()
