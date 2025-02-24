"""
Caleb Aguiar
SWE-410
02/18/2025
Unit Testing
In Class Exercise
"""

class Calculator:
    """A Simple calculator class that provides basic arithmetic operations."""

    def add(self, num1, num2):
        """Return the sum of two numbers."""
        return num1 + num2

    def subtract(self, num1, num2):
        """Returns the difference between two numbers."""
        return num1 - num2

    def multiply(self, num1, num2):
        """Return the product of two numbers."""
        return num1 * num2

    def divide(self, num1, num2):
        """Return the quotient of two numbers

        Raises:
        ZeroDivisionError: If the divisor (num2) is zero.
        """
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero") #Raise an error if divion by zero is atempted
        return num1 / num2