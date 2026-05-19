"""
String Calculator Base Module

This module provides the abstract base class for string-based arithmetic operations.
It contains the core logic for converting Indonesian text representations of numbers
into numerical values that can be used for mathematical calculations.

The StringCalculator class implements the Template Method pattern to define the
structure for arithmetic operations while allowing subclasses to implement
specific calculation logic.

Author: Development Team
Version: 1.0.0
Date: 2026-05-19
"""

from abc import ABC, abstractmethod


class StringCalculator(ABC):
    """
    Abstract base class for performing arithmetic operations on string-represented numbers.

    This class converts Indonesian text representations of numbers (e.g., "dua puluh satu" 
    meaning "twenty one") into numerical values that can be used for calculations.

    Attributes:
        str_val1 (str): The first operand as a string representation in Indonesian.
        str_val2 (str): The second operand as a string representation in Indonesian.
        num1 (float): The first operand converted to a numerical value.
        num2 (float): The second operand converted to a numerical value.

    Note:
        This is an abstract base class and cannot be instantiated directly.
        Subclasses must implement the hitung() and tampilkan_hasil() methods.
    """

    def __init__(self, str_val1, str_val2):
        """
        Initialize the StringCalculator with two string-represented operands.

        Args:
            str_val1 (str): The first operand as Indonesian text (e.g., "dua puluh").
            str_val2 (str): The second operand as Indonesian text (e.g., "tiga").

        Raises:
            ValueError: If the string values cannot be converted to numbers.
        """
        self.str_val1 = str_val1
        self.str_val2 = str_val2
        self.num1 = self.string_to_number(str_val1)
        self.num2 = self.string_to_number(str_val2)

    def string_to_number(self, text):
        """
        Convert Indonesian text representation of a number to its numerical equivalent.

        This method supports numbers from "nol" (0) through complex composite numbers
        like "seratus dua puluh tiga" (123).

        Supported basic numbers:
            - Zero to eleven: nol, satu, dua, tiga, empat, lima, enam, tujuh, delapan, sembilan, sepuluh, sebelas
            - Multipliers: puluh (tens), belas (teens)

        Args:
            text (str): The Indonesian text representation of a number (case-insensitive).

        Returns:
            int: The numerical value of the text representation.

        Example:
            >>> calc = StringCalculator("dua puluh", "lima")
            >>> calc.string_to_number("dua puluh lima")
            25
        """
        # Dictionary mapping Indonesian words to their numerical values
        number_dictionary = {
            "nol": 0, "satu": 1, "dua": 2, "tiga": 3, "empat": 4,
            "lima": 5, "enam": 6, "tujuh": 7, "delapan": 8, "sembilan": 9,
            "sepuluh": 10, "sebelas": 11
        }

        # Split the text into individual words and convert to lowercase
        words = text.lower().split()
        total = 0
        temporary = 0

        # Process each word in the text
        for word in words:
            if word in number_dictionary:
                # If the word is a basic number, store it temporarily
                temporary = number_dictionary[word]
            elif word == "belas":
                # "belas" adds 10 to the current temporary value (for numbers 12-19)
                temporary += 10
            elif word == "puluh":
                # "puluh" multiplies the temporary value by 10 and adds to total
                temporary *= 10
                total += temporary
                temporary = 0

        # Add any remaining value to the total
        total += temporary
        return total

    @abstractmethod
    def hitung(self):
        """
        Perform the specific arithmetic calculation.

        This is an abstract method that must be implemented by subclasses
        to define the specific operation (addition, subtraction, etc.).

        Returns:
            int or float: The result of the calculation.
        """
        pass

    @abstractmethod
    def tampilkan_hasil(self):
        """
        Display the calculation result in a formatted manner.

        This is an abstract method that must be implemented by subclasses
        to define how results should be presented to the user.
        """
        pass
