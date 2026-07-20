# Advanced Calculator System

A professional, production-ready calculator system with comprehensive arithmetic, scientific, logarithmic, and statistical operations.

## Features

### 🔢 Basic Arithmetic Operations
- **Addition** - Add two numbers
- **Subtraction** - Subtract numbers
- **Multiplication** - Multiply numbers
- **Division** - Divide with zero-check protection
- **Modulo** - Calculate remainder
- **Power** - Raise to exponent

### 📐 Scientific Operations
- **Square Root** - Calculate √x
- **Square** - Calculate x²
- **Cube** - Calculate x³
- **Absolute Value** - Get |x|
- **Percentage** - Calculate percentages

###  Logarithmic Operations
- **Logarithm** - Calculate log with any base
- **Natural Logarithm** - Calculate ln(x)
- Includes validation for domain errors

### 📉 Statistical Operations
- **Average** - Calculate mean of numbers
- **Sum** - Sum multiple numbers
- **Factorial** - Calculate n!

### ⚡ Advanced Operations
- **Combination** - Calculate nCr
- **Permutation** - Calculate nPr
- **GCD** - Greatest Common Divisor
- **LCM** - Least Common Multiple

### 💾 History Management
- **Calculation History** - Tracks all operations with timestamps
- **Get Last Result** - Retrieve previous result
- **Clear History** - Reset history
- **View History** - Display all calculations

### 🛠️ Utility Operations
- **Rounding** - Round to decimal places
- **Percentage Conversion** - Convert decimals to percentages
- **Current Value Tracking** - Monitor last calculation result

## Project Structure

```
calculator-system/
├── calculator.py          # Main calculator classes
├── calculator_ui.py       # Interactive command-line UI
├── test_calculator.py     # Comprehensive unit tests
└── README.md             # Documentation
```

## Classes

### Calculator
Base calculator class with all standard operations.

```python
calc = Calculator()
result = calc.add(10, 5)           # 15
result = calc.divide(100, 4)       # 25.0
result = calc.square_root(16)      # 4.0
result = calc.factorial(5)         # 120
```

### AdvancedCalculator
Extended class with advanced mathematical operations.

```python
calc = AdvancedCalculator()
result = calc.combination(5, 2)              # 10
result = calc.greatest_common_divisor(48, 18)  # 6
```

### CalculationHistory
Manages calculation history with timestamps.

```python
history = CalculationHistory()
history.add_entry("5 + 3", 8)
entries = history.get_history()
```

## Usage

### As a Library

```python
from calculator import AdvancedCalculator

calc = AdvancedCalculator()

# Basic operations
print(calc.add(10, 5))                      # 15
print(calc.multiply(6, 7))                  # 42

# Scientific operations
print(calc.square_root(25))                 # 5.0
print(calc.power(2, 8))                     # 256

# Statistical
print(calc.average([5, 10, 15, 20]))        # 12.5
print(calc.factorial(5))                    # 120

# Advanced
print(calc.combination(5, 2))               # 10
print(calc.greatest_common_divisor(48, 18)) # 6

# View history
calc.print_history()

# Get last result
last = calc.get_last_result()
```

### Interactive UI

```bash
python calculator_ui.py
```

This launches an interactive menu-driven interface where you can:
1. Select from 24 operations
2. Input values when prompted
3. View calculation history
4. Clear history
5. See results immediately

### Running Tests

```bash
python -m unittest test_calculator.py
```

Or for verbose output:

```bash
python -m unittest test_calculator.py -v
```

## Error Handling

The calculator includes comprehensive error handling:

- **Division by Zero** - Raises `ValueError`
- **Invalid Logarithm Arguments** - Raises `ValueError` for non-positive numbers
- **Invalid Base** - Raises `ValueError` for invalid logarithm bases
- **Negative Square Root** - Raises `ValueError`
- **Invalid Factorial Input** - Raises `ValueError` for negative numbers
- **Type Validation** - Validates input types for operations requiring integers

## Examples

### Basic Calculations
```python
from calculator import Calculator

calc = Calculator()

# Simple arithmetic
print(calc.add(100, 50))                    # 150
print(calc.subtract(100, 30))               # 70
print(calc.multiply(12, 12))                # 144
print(calc.divide(144, 12))                 # 12.0
```

### Scientific Calculations
```python
# Square and cube
print(calc.square(5))                       # 25
print(calc.cube(3))                         # 27

# Square root
print(calc.square_root(144))                # 12.0

# Percentage
print(calc.percentage(200, 25))             # 50.0 (25% of 200)
```

### Advanced Calculations
```python
from calculator import AdvancedCalculator

calc = AdvancedCalculator()

# Combinations and permutations
print(calc.combination(10, 3))              # 120
print(calc.permutation(10, 3))              # 720

# Number theory
print(calc.greatest_common_divisor(48, 18)) # 6
print(calc.least_common_multiple(12, 18))   # 36
```

### Calculation History
```python
calc = Calculator()

calc.add(10, 5)
calc.multiply(3, 4)
calc.divide(100, 5)

# Get history
history = calc.get_history()
for entry in history:
    print(f"{entry['operation']} = {entry['result']}")

# Get last result
print(calc.get_last_result())               # 20.0

# Clear history
calc.clear_history()
```

## Test Coverage

The test suite includes:
- ✓ Basic arithmetic operations
- ✓ Scientific operations
- ✓ Logarithmic operations
- ✓ Statistical operations
- ✓ Advanced operations (combinations, permutations, GCD, LCM)
- ✓ Error handling and edge cases
- ✓ History management
- ✓ Utility operations
- ✓ Type validation

Run `python -m unittest test_calculator.py -v` to see all tests.

## Requirements

- Python 3.6+
- Standard library only (math module)

## Installation

No external dependencies required! Simply clone or download the files.

## License

Open source - Free to use and modify.

## Author

Senior Developer
Created as a professional calculator system demonstration.
