"""
Caleb Aguiar
SWE-410
02/18/2025
Unit Testing
In Class Exercise
"""

import unittest
from calculator import Calculator  # Ensure the Calculator class is in a file named 'calculator.py'

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Initialize a Calculator instance before each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test addition of two numbers."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction of two numbers."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(2, 5), -3)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiply(self):
        """Test multiplication of two numbers."""
        self.assertEqual(self.calculator.multiply(4, 3), 12)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(0, 10), 0)

    def test_divide(self):
        """Test division of two numbers."""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Test division by zero, should raise ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()