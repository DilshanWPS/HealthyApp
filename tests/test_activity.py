import unittest
from HealthyCalc.activity import ActMultiplier

class TestActivityFunction(unittest.TestCase):

    def test_valid_levels(self):
        self.assertEqual(ActMultiplier("1"), 1.2)
        self.assertEqual(ActMultiplier("2"), 1.375)
        self.assertEqual(ActMultiplier("3"), 1.55)
        self.assertEqual(ActMultiplier("4"), 1.725)
        self.assertEqual(ActMultiplier("5"), 1.9)

    def test_invalid_level_defaults(self):
        self.assertEqual(ActMultiplier("6"), 1.2)
        self.assertEqual(ActMultiplier("x"), 1.2)

if __name__ == '__main__':
    unittest.main()
