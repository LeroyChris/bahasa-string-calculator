"""
String Calculator CLI - Main Entry Point

This is the main entry point for the String Calculator command-line application.
It provides an interactive interface for users to perform arithmetic operations
using Indonesian text representations of numbers.

The application supports four basic operations: addition, subtraction, 
multiplication, and division.

Author: Development Team
Version: 1.0.0
Date: 2026-05-19

Usage:
    python main.py

Example:
    Input: "dua puluh" and "lima"
    Operations performed:
    - dua puluh + lima = 25
    - dua puluh - lima = 15
    - dua puluh x lima = 100
    - dua puluh / lima = 4.0
"""

from modules.Operations import Addition, Subtraction, Multiplication, Division


def main():
    """
    Main function that runs the string calculator interactive session.

    This function displays a welcome message and enters an infinite loop that:
    1. Prompts the user for two string-represented numbers
    2. Performs all four arithmetic operations on those numbers
    3. Displays the results
    4. Repeats until the user enters 'keluar' (exit) to quit

    Error Handling:
        - Catches exceptions when invalid text representations are entered
        - Prompts the user to enter valid Indonesian text numbers
    """
    print("=" * 50)
    print("Welcome to String Calculator OOP!")
    print("Type 'exit' on number 1 input to quit.")
    print("=" * 50)

    while True:
        # Prompt for the first operand
        input_number1 = input("\nEnter number 1 (string): ").strip().lower()

        # Check if user wants to exit
        if input_number1 == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Prompt for the second operand
        input_number2 = input("Enter number 2 (string): ").strip().lower()

        # Display section separator
        print("\n--- Calculation Results ---")
        print(f"Number 1 (string): {input_number1}")
        print(f"Number 2 (string): {input_number2}")

        try:
            # Create instances of all four operation classes
            operations_list = [
                Addition(input_number1, input_number2),
                Subtraction(input_number1, input_number2),
                Multiplication(input_number1, input_number2),
                Division(input_number1, input_number2)
            ]

            # Execute and display results for each operation
            for operation in operations_list:
                operation.tampilkan_hasil()

        except Exception as e:
            # Handle errors in conversion or calculation
            print("An error occurred. Please ensure you entered valid text numbers.")
            print("Valid format examples: 'dua puluh satu', 'seratus lima').")
            
        print("-" * 25)


if __name__ == "__main__":
    """
    Application entry point.
    
    Ensures main() is only executed when this script is run directly,
    not when imported as a module.
    """
    main()