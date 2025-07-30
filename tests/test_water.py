import unittest
from HealthyCalc.water import CalcWater

class TestWaterFunction(unittest.TestCase):

    def test_CalcWater(self):
        self.assertEqual(CalcWater(60), 1.98)
        self.assertEqual(CalcWater(75), 2.48)

if __name__ == '__main__':
    unittest.main()
