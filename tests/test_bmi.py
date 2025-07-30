import unittest
from HealthyCalc.bmi import CalculateBmi, BmiCategory

class TestBmiFunctions(unittest.TestCase):
    
    def test_CalculateBmi(self):
        self.assertAlmostEqual(CalculateBmi(70, 175), 22.86)
        self.assertAlmostEqual(CalculateBmi(50, 160), 19.53)
        

    def test_BmiCategory(self):
        self.assertEqual(BmiCategory(17), "Underweight")
        self.assertEqual(BmiCategory(22), "Normal")
        self.assertEqual(BmiCategory(27), "Overweight")
        self.assertEqual(BmiCategory(31), "Obese")

if __name__ == '__main__':
    unittest.main()
