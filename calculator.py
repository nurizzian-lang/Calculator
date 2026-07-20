"""
Professional Calculator System
Main calculator module with core arithmetic and scientific operations
"""

import math
from typing import Union, List, Tuple
from datetime import datetime
from enum import Enum


class OperationType(Enum):
    """Enum for operation types"""
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "**"
    MODULO = "%"
    SQRT = "sqrt"


class CalculationHistory:
    """Manages calculation history"""
    
    def __init__(self):
        self.history: List[dict] = []
    
    def add_entry(self, operation: str, result: Union[int, float], timestamp: str = None):
        """Add an entry to history"""
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.history.append({
            "operation": operation,
            "result": result,
            "timestamp": timestamp
        })
    
    def get_history(self) -> List[dict]:
        """Retrieve all history entries"""
        return self.history
    
    def clear_history(self):
        """Clear all history"""
        self.history = []
    
    def get_last_result(self) -> Union[int, float, None]:
        """Get the last calculation result"""
        return self.history[-1]["result"] if self.history else None


class Calculator:
    """Main calculator class with all operations"""
    
    def __init__(self):
        self.history = CalculationHistory()
        self.current_value: Union[int, float] = 0
    
    # ==================== Basic Arithmetic Operations ====================
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers"""
        result = a + b
        self.current_value = result
        self.history.add_entry(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a"""
        result = a - b
        self.current_value = result
        self.history.add_entry(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers"""
        result = a * b
        self.current_value = result
        self.history.add_entry(f"{a} * {b}", result)
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b with error handling"""
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed")
        result = a / b
        self.current_value = result
        self.history.add_entry(f"{a} / {b}", result)
        return result
    
    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Calculate remainder of a divided by b"""
        if b == 0:
            raise ValueError("Error: Modulo by zero is not allowed")
        result = a % b
        self.current_value = result
        self.history.add_entry(f"{a} % {b}", result)
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent"""
        result = base ** exponent
        self.current_value = result
        self.history.add_entry(f"{base} ** {exponent}", result)
        return result
    
    # ==================== Scientific Operations ====================
    
    def square_root(self, number: Union[int, float]) -> float:
        """Calculate square root of a number"""
        if number < 0:
            raise ValueError("Error: Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self.current_value = result
        self.history.add_entry(f"sqrt({number})", result)
        return result
    
    def square(self, number: Union[int, float]) -> Union[int, float]:
        """Calculate square of a number"""
        result = number ** 2
        self.current_value = result
        self.history.add_entry(f"square({number})", result)
        return result
    
    def cube(self, number: Union[int, float]) -> Union[int, float]:
        """Calculate cube of a number"""
        result = number ** 3
        self.current_value = result
        self.history.add_entry(f"cube({number})", result)
        return result
    
    def absolute(self, number: Union[int, float]) -> Union[int, float]:
        """Calculate absolute value"""
        result = abs(number)
        self.current_value = result
        self.history.add_entry(f"abs({number})", result)
        return result
    
    def percentage(self, number: Union[int, float], percent: Union[int, float]) -> Union[int, float]:
        """Calculate percentage of a number"""
        result = (number * percent) / 100
        self.current_value = result
        self.history.add_entry(f"{percent}% of {number}", result)
        return result
    
    # ==================== Logarithmic Operations ====================
    
    def logarithm(self, number: Union[int, float], base: float = 10) -> float:
        """Calculate logarithm of a number with specified base"""
        if number <= 0:
            raise ValueError("Error: Logarithm argument must be positive")
        if base <= 0 or base == 1:
            raise ValueError("Error: Base must be positive and not equal to 1")
        
        result = math.log(number, base)
        self.current_value = result
        self.history.add_entry(f"log_{base}({number})", result)
        return result
    
    def natural_logarithm(self, number: Union[int, float]) -> float:
        """Calculate natural logarithm (ln) of a number"""
        if number <= 0:
            raise ValueError("Error: Logarithm argument must be positive")
        
        result = math.log(number)
        self.current_value = result
        self.history.add_entry(f"ln({number})", result)
        return result
    
    # ==================== Statistical Operations ====================
    
    def average(self, numbers: List[Union[int, float]]) -> float:
        """Calculate average of numbers"""
        if not numbers:
            raise ValueError("Error: List cannot be empty")
        
        result = sum(numbers) / len(numbers)
        self.current_value = result
        self.history.add_entry(f"average({numbers})", result)
        return result
    
    def sum_numbers(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate sum of numbers"""
        result = sum(numbers)
        self.current_value = result
        self.history.add_entry(f"sum({numbers})", result)
        return result
    
    def factorial(self, number: int) -> int:
        """Calculate factorial of a number"""
        if number < 0:
            raise ValueError("Error: Factorial is not defined for negative numbers")
        if not isinstance(number, int):
            raise ValueError("Error: Factorial requires an integer")
        
        result = math.factorial(number)
        self.current_value = result
        self.history.add_entry(f"factorial({number})", result)
        return result
    
    # ==================== History Management ====================
    
    def get_history(self) -> List[dict]:
        """Retrieve calculation history"""
        return self.history.get_history()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear_history()
    
    def get_last_result(self) -> Union[int, float, None]:
        """Get last calculation result"""
        return self.history.get_last_result()
    
    def print_history(self):
        """Print formatted calculation history"""
        history = self.get_history()
        if not history:
            print("No calculation history")
            return
        
        print("\n" + "="*60)
        print("CALCULATION HISTORY")
        print("="*60)
        for i, entry in enumerate(history, 1):
            print(f"{i}. {entry['operation']} = {entry['result']}")
            print(f"   Time: {entry['timestamp']}")
        print("="*60 + "\n")
    
    # ==================== Utility Operations ====================
    
    def round_result(self, number: Union[int, float], decimal_places: int = 2) -> float:
        """Round number to specified decimal places"""
        result = round(number, decimal_places)
        self.current_value = result
        self.history.add_entry(f"round({number}, {decimal_places})", result)
        return result
    
    def convert_to_percentage(self, number: float) -> float:
        """Convert decimal to percentage"""
        result = number * 100
        self.current_value = result
        self.history.add_entry(f"to_percentage({number})", result)
        return result


# ==================== Advanced Calculator ====================

class AdvancedCalculator(Calculator):
    """Extended calculator with additional advanced features"""
    
    def combination(self, n: int, r: int) -> int:
        """Calculate nCr (combination)"""
        if n < r or n < 0 or r < 0:
            raise ValueError("Error: Invalid values for combination")
        
        result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        self.current_value = result
        self.history.add_entry(f"C({n},{r})", result)
        return result
    
    def permutation(self, n: int, r: int) -> int:
        """Calculate nPr (permutation)"""
        if n < r or n < 0 or r < 0:
            raise ValueError("Error: Invalid values for permutation")
        
        result = math.factorial(n) // math.factorial(n - r)
        self.current_value = result
        self.history.add_entry(f"P({n},{r})", result)
        return result
    
    def greatest_common_divisor(self, a: int, b: int) -> int:
        """Calculate GCD"""
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Error: GCD requires integers")
        
        result = math.gcd(a, b)
        self.current_value = result
        self.history.add_entry(f"gcd({a}, {b})", result)
        return result
    
    def least_common_multiple(self, a: int, b: int) -> int:
        """Calculate LCM"""
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Error: LCM requires integers")
        
        gcd = math.gcd(a, b)
        result = abs(a * b) // gcd
        self.current_value = result
        self.history.add_entry(f"lcm({a}, {b})", result)
        return result


if __name__ == "__main__":
    # Example usage
    calc = AdvancedCalculator()
    
    print("Calculator System - Demo")
    print("="*60)
    
    # Basic operations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"20 - 8 = {calc.subtract(20, 8)}")
    print(f"12 * 3 = {calc.multiply(12, 3)}")
    print(f"100 / 4 = {calc.divide(100, 4)}")
    
    # Scientific operations
    print(f"√16 = {calc.square_root(16)}")
    print(f"2^8 = {calc.power(2, 8)}")
    
    # Statistical operations
    print(f"Average [5, 10, 15, 20] = {calc.average([5, 10, 15, 20])}")
    print(f"5! = {calc.factorial(5)}")
    
    # Advanced operations
    print(f"C(5,2) = {calc.combination(5, 2)}")
    print(f"GCD(48, 18) = {calc.greatest_common_divisor(48, 18)}")
    
    # Show history
    calc.print_history()
