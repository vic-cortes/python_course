"""Unit tests for calculator module using Python's unittest framework."""

import unittest

from calculator import Calculator, CalculatorAPI


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class using unittest."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def tearDown(self):
        """Clean up after each test method."""
        self.calc.clear_history()

    def test_add_integers(self):
        """Test adding two integers."""
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)
        self.assertEqual(len(self.calc.history), 1)

    def test_add_floats(self):
        """Test adding two floating point numbers."""
        result = self.calc.add(1.5, 2.5)
        self.assertAlmostEqual(result, 4.0)

    def test_divide_valid(self):
        """Test division with valid inputs."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_history_tracking(self):
        """Test that operations are properly tracked in history."""
        self.calc.add(2, 3)
        self.calc.add(5, 5)
        self.assertEqual(len(self.calc.history), 2)
        self.calc.clear_history()
        self.assertEqual(len(self.calc.history), 0)


class TestCalculatorAPI(unittest.TestCase):
    """Test cases for CalculatorAPI class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
        self.api = CalculatorAPI(self.calc)

    def test_perform_add(self):
        """Test perform_calculation with add operation."""
        result = self.api.perform_calculation("add", 5, 3)
        self.assertEqual(result, 8)

    def test_perform_divide(self):
        """Test perform_calculation with divide operation."""
        result = self.api.perform_calculation("divide", 10, 2)
        self.assertEqual(result, 5)

    def test_invalid_operation(self):
        """Test perform_calculation with invalid operation."""
        with self.assertRaises(ValueError):
            self.api.perform_calculation("multiply", 5, 3)


if __name__ == "__main__":
    unittest.main()
