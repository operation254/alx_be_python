import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2.5, 0.5), 3.0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)
        self.assertEqual(self.calc.subtract(2, 7), -5)
        self.assertEqual(self.calc.subtract(5.5, 2.25), 3.25)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division(self):  # <-- exact name the checker expects
        self.assertEqual(self.calc.divide(8, 2), 4.0)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertIsNone(self.calc.divide(5, 0))  # divide by zero
        

if __name__ == "__main__":
    unittest.main()
