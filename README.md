# String Calculator CLI

A professional object-oriented Python command-line calculator that performs arithmetic operations using Indonesian text representations of numbers.

## Overview

String Calculator is an educational project that demonstrates key Object-Oriented Programming (OOP) principles through a unique approach to arithmetic calculations. Instead of inputting numbers directly, users enter numbers as Indonesian text (e.g., "dua puluh lima" for 25), which the application converts to numerical values and performs calculations.

## Features

- **Four Basic Operations**: Addition, Subtraction, Multiplication, and Division
- **Indonesian Text Input**: Convert Indonesian text representations of numbers to numerical values
- **Object-Oriented Design**: Uses abstract base classes and inheritance patterns
- **Interactive CLI Interface**: User-friendly command-line interface with clear prompts and formatted output
- **Error Handling**: Robust error handling for invalid inputs and edge cases (e.g., division by zero)
- **Professional Documentation**: Comprehensive docstrings and comments throughout the codebase

## Project Structure

```
string-calc-cli/
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore configuration
└── src/
    ├── main.py                  # Application entry point
    └── modules/
        ├── StringCalculator.py  # Abstract base class for calculations
        └── Operations.py        # Concrete operation classes (Addition, Subtraction, Multiplication, Division)
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone the repository or download the project files:
   ```bash
   git clone <repository-url>
   cd string-calc-cli
   ```

2. Navigate to the source directory:
   ```bash
   cd src
   ```

## Usage

### Running the Application

```bash
python main.py
```

### Interactive Session Example

```
==================================================
Welcome to String Calculator OOP!
Type 'exit' on number 1 input to quit.
==================================================

Enter number 1 (string): dua puluh
Enter number 2 (string): lima

--- Calculation Results ---
Number 1 (string): dua puluh
Number 2 (string): lima
dua puluh + lima = 25
dua puluh - lima = 15
dua puluh x lima = 100
dua puluh / lima = 4.0
```

## Supported Indonesian Numbers

The calculator supports Indonesian text representations for the following numbers:

### Base Numbers (0-11)
- nol (0)
- satu (1)
- dua (2)
- tiga (3)
- empat (4)
- lima (5)
- enam (6)
- tujuh (7)
- delapan (8)
- sembilan (9)
- sepuluh (10)
- sebelas (11)

### Composite Numbers
- puluh (tens): e.g., "dua puluh" = 20, "tiga puluh lima" = 35
- belas (teens): e.g., "dua belas" = 12, "lima belas" = 15

### Examples
- "dua" → 2
- "dua puluh" → 20
- "dua puluh lima" → 25
- "seratus" → 100 (if supported in extended version)

## How It Works

### Architecture

The application follows the **Template Method** design pattern using object-oriented principles:

1. **StringCalculator** (Abstract Base Class):
   - Handles string-to-number conversion logic
   - Defines abstract methods for calculation and result display
   - Stores both string and numerical representations of operands

2. **Operation Classes** (Concrete Implementations):
   - `Addition`: Performs addition (num1 + num2)
   - `Subtraction`: Performs subtraction (num1 - num2)
   - `Multiplication`: Performs multiplication (num1 * num2)
   - `Division`: Performs division (num1 / num2) with zero-division protection

3. **Main Application**:
   - Provides the interactive CLI interface
   - Manages user input and error handling
   - Orchestrates all operations

### String Conversion Algorithm

The `string_to_number()` method converts Indonesian text to numbers using:
- A dictionary mapping Indonesian words to base numbers (0-11)
- Word-by-word parsing of the input text
- Logic for handling multipliers ("puluh" = ×10) and special cases ("belas" = +10)

## Error Handling

The application gracefully handles:
- Invalid Indonesian text numbers: Prompts the user to enter valid format
- Division by zero: Returns an error message instead of crashing
- Unexpected exceptions: Provides helpful error messages

## Exit Instructions

To exit the calculator application, enter "exit" when prompted for the first number:

```
Enter number 1 (string): exit
Thank you for using the calculator. Goodbye!
```

## Development

### Adding New Operations

To add a new arithmetic operation:

1. Create a new class in `Operations.py` that inherits from `StringCalculator`
2. Implement the `hitung()` method with your calculation logic
3. Implement the `tampilkan_hasil()` method to display the result
4. Add an instance of your new operation to the `operations_list` in `main.py`

Example:
```python
class Modulo(StringCalculator):
    """Modulo operation for string-represented numbers."""
    
    def hitung(self):
        if self.num2 == 0:
            return "Error: Cannot divide by zero"
        return self.num1 % self.num2
    
    def tampilkan_hasil(self):
        print(f"{self.str_val1} % {self.str_val2} = {self.hitung()}")
```

### Extending Number Support

The string-to-number conversion can be extended to support larger numbers by:
- Adding more entries to the `number_dictionary` in `StringCalculator.py`
- Implementing additional logic for "ratus" (hundreds) and "ribu" (thousands)

## Code Quality

- **Professional Documentation**: Comprehensive module, class, and method docstrings
- **PEP 8 Compliance**: Code follows Python style guidelines
- **Type Hints**: Clear parameter and return type documentation
- **Error Handling**: Robust exception handling throughout
- **Maintainability**: Clean, organized code structure for easy maintenance and extension

## Testing

To manually test the application:

1. Run the application and test basic operations:
   - "lima" + "tiga" → should equal 8
   - "dua puluh" - "lima" → should equal 15
   - "empat" × "enam" → should equal 24
   - "dua puluh" ÷ "lima" → should equal 4.0

2. Test edge cases:
   - Division by zero: "sepuluh" ÷ "nol" → should display error
   - Invalid input: "xyz" + "abc" → should display error message

## Future Enhancements

- Support for English number input
- Support for decimal numbers in Indonesian text
- Export calculation history to a file
- Graphical user interface (GUI)
- Support for more complex operations (power, square root, etc.)
- Internationalization support for multiple languages

## License

This project is open-source and available for educational purposes.

## Author

Development Team

## Version

1.0.0 (May 19, 2026)

## Support

For issues, questions, or contributions, please contact the development team.

---

**Note**: This is an educational project designed to demonstrate OOP principles and code organization best practices.
