import unittest
from unittest.mock import patch
from HealthyCalc.inputValidate import NameValid, InputValid, AgeValid, genderValid, ActivityValid

class TestValidationFunctions(unittest.TestCase):

    @patch("builtins.input", side_effect=["", "123", "John"])
    def test_NameValid(self, mock_input):
        self.assertEqual(NameValid("Enter name: "), "John")

    @patch("builtins.input", side_effect=["-5", "abc", "70"])
    def test_InputValid(self, mock_input):
        self.assertEqual(InputValid("Enter weight: "), 70.0)

    @patch("builtins.input", side_effect=["-2", "twenty", "25"])
    def test_AgeValid(self, mock_input):
        self.assertEqual(AgeValid("Enter age: "), 25)

    @patch("builtins.input", side_effect=["", "male"])
    def test_genderValid(self, mock_input):
        self.assertEqual(genderValid("Enter gender: "), "male")

    @patch("builtins.input", side_effect=["0", "6", "3"])
    def test_ActivityValid(self, mock_input):
        self.assertEqual(ActivityValid(), "3")

if __name__ == '__main__':
    unittest.main()
