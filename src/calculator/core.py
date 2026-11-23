"""A small calculator service with four arithmetic operations."""
from numbers import Real


def _check_numbers(*values):
    """Raise TypeError unless every value is a real number (bool is rejected)."""
    for value in values:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(f"Calculator only accepts numbers, got {type(value).__name__}")


class Calculator:
    """Basic arithmetic on two numbers."""

    def Add(self, value1, value2):
        """Return value1 + value2."""
        _check_numbers(value1, value2)
        return value1 + value2

    def Substract(self, value1, value2):
        """Return value1 - value2."""
        _check_numbers(value1, value2)
        return value1 - value2

    def Multiply(self, value1, value2):
        """Return value1 * value2."""
        _check_numbers(value1, value2)
        return value1 * value2

    def Divide(self, value1, value2):
        """Return value1 / value2. Raises ZeroDivisionError when value2 is 0."""
        _check_numbers(value1, value2)
        if value2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return value1 / value2