"""
Arithmetic Operations Module

This module implements concrete arithmetic operation classes for the string calculator.
It provides implementations for basic mathematical operations: addition, subtraction,
multiplication, and division.

Each operation class inherits from StringCalculator and implements the specific
calculation logic and result display format.

Author: Development Team
Version: 1.0.0
Date: 2026-05-19
"""

from StringCalculator import StringCalculator


class Addition(StringCalculator):
    """
    Addition operation for string-represented numbers.

    Performs addition (num1 + num2) and displays the result in a formatted string.

    Example:
        >>> add = Addition("dua puluh", "lima")
        >>> add.tampilkan_hasil()
        dua puluh + lima = 25
    """

    def hitung(self):
        """
        Calculate the sum of the two operands.

        Returns:
            int: The sum of num1 and num2.
        """
        return self.num1 + self.num2

    def tampilkan_hasil(self):
        """
        Display the addition operation and its result.

        Prints the operation in the format: "operand1 + operand2 = result"
        """
        print(f"{self.str_val1} + {self.str_val2} = {self.hitung()}")


class Subtraction(StringCalculator):
    """
    Subtraction operation for string-represented numbers.

    Performs subtraction (num1 - num2) and displays the result in a formatted string.

    Example:
        >>> sub = Subtraction("tiga puluh", "lima")
        >>> sub.tampilkan_hasil()
        tiga puluh - lima = 25
    """

    def hitung(self):
        """
        Calculate the difference of the two operands.

        Returns:
            int: The result of num1 minus num2.
        """
        return self.num1 - self.num2

    def tampilkan_hasil(self):
        """
        Display the subtraction operation and its result.

        Prints the operation in the format: "operand1 - operand2 = result"
        """
        print(f"{self.str_val1} - {self.str_val2} = {self.hitung()}")


class Multiplication(StringCalculator):
    """
    Multiplication operation for string-represented numbers.

    Performs multiplication (num1 * num2) and displays the result in a formatted string.

    Example:
        >>> mul = Multiplication("lima", "empat")
        >>> mul.tampilkan_hasil()
        lima x empat = 20
    """

    def hitung(self):
        """
        Calculate the product of the two operands.

        Returns:
            int: The result of num1 multiplied by num2.
        """
        return self.num1 * self.num2

    def tampilkan_hasil(self):
        """
        Display the multiplication operation and its result.

        Prints the operation in the format: "operand1 x operand2 = result"
        """
        print(f"{self.str_val1} x {self.str_val2} = {self.hitung()}")


class Division(StringCalculator):
    """
    Division operation for string-represented numbers.

    Performs division (num1 / num2) with error handling for division by zero.
    The result is returned as a float to preserve decimal precision.

    Example:
        >>> div = Division("dua puluh", "empat")
        >>> div.tampilkan_hasil()
        dua puluh / empat = 5.0
    """

    def hitung(self):
        """
        Calculate the quotient of the two operands.

        Performs error checking to prevent division by zero.

        Returns:
            float: The result of num1 divided by num2.
            str: An error message if num2 is zero.

        Raises:
            ZeroDivisionError: When attempting to divide by zero.
        """
        if self.num2 == 0:
            return "Error: Cannot divide by zero"
        return float(self.num1 / self.num2)

    def tampilkan_hasil(self):
        """
        Display the division operation and its result.

        Prints the operation in the format: "operand1 / operand2 = result"
        If division by zero is attempted, displays an error message instead.
        """
        print(f"{self.str_val1} / {self.str_val2} = {self.hitung()}")
