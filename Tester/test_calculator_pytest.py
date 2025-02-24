"""
Caleb Aguiar
SWE-410
02/18/2025
Unit Testing
In Class Exercise
"""

import pytest
from calculator import Calculator

# Test function for addition
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5  # Basic addition
    assert calc.add(-1, 1) == 0  # Addition with negative number
    assert calc.add(0, 0) == 0  # Adding zero

# Test function for subtraction
def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2  # Basic subtraction
    assert calc.subtract(3, 5) == -2  # Subtraction resulting in negative
    assert calc.subtract(0, 0) == 0  # Subtracting zero

# Test function for multiplication
def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6  # Basic multiplication
    assert calc.multiply(-1, 5) == -5  # Multiplication with negative number
    assert calc.multiply(0, 10) == 0  # Multiplication by zero

# Test function for division
def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3  # Basic division
    assert calc.divide(5, 2) == 2.5  # Division resulting in decimal
    assert calc.divide(-10, 2) == -5  # Division with negative number

    # Test division by zero, expecting a ZeroDivisionError
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.divide(10, 0)