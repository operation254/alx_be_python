# programming_paradigm/test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for SimpleCalculator operations."""

    def setUp(self):
        self.calc = SimpleCalculator()

    # ---- add ----
    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)

    def test_add_floats(self):
        self.assertEqual(self.calc.add(2.5, 0.5), 3.0)

    # ---- subtract ----
    def test_subtract_basic(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)
        self.assertEqual(self.calc.subtract(2, 7), -5)

    def test_subtract_floats(self):
        self.assertEqual(self.calc.subtract(5.5, 2.25), 3.25)

    # ---- multiply ----
    def test_multiply_basic(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 99), 0)

    def test_multiply_floats(self):
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # ---- divide ----
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(8, 2), 4.0)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(5, 0))


if __name__ == "__main__":
    unittest.main()
