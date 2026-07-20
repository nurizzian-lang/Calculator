"""
Unit tests for Calculator System
Tests all calculator functions and edge cases
"""

import unittest
import math
from calculator import Calculator, AdvancedCalculator, CalculationHistory


class TestCalculationHistory(unittest.TestCase):
    """Test CalculationHistory class"""
    
    def setUp(self):
        self.history = CalculationHistory()
    
    def test_add_entry(self):
        """Test adding entry to history"""
        self.history.add_entry("1 + 1", 2)
        self.assertEqual(len(self.history.get_history()), 1)
    
    def test_get_history(self):
        """Test getting history"""
        self.history.add_entry("5 * 2", 10)
        history = self.history.get_history()
        self.assertEqual(history[0]["result"], 10)
    
    def test_clear_history(self):
        """Test clearing history"""
        self.history.add_entry("10 / 2", 5)
        self.history.clear_history()
        self.assertEqual(len(self.history.get_history()), 0)
    
    def test_get_last_result(self):
        """Test getting last result"""
        self.history.add_entry("3 + 3", 6)
        self.history.add_entry("2 * 2", 4)
        self.assertEqual(self.history.get_last_result(), 4)


class TestBasicOperations(unittest.TestCase):
    """Test basic arithmetic operations"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition"""
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)
    
    def test_subtract(self):
        """Test subtraction"""
        result = self.calc.subtract(20, 8)
        self.assertEqual(result, 12)
    
    def test_multiply(self):
        """Test multiplication"""
        result = self.calc.multiply(6, 7)
        self.assertEqual(result, 42)
    
    def test_divide(self):
        """Test division"""
        result = self.calc.divide(100, 4)
        self.assertEqual(result, 25)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_modulo(self):
        """Test modulo operation"""
        result = self.calc.modulo(10, 3)
        self.assertEqual(result, 1)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises error"""
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
    
    def test_power(self):
        """Test power operation"""
        result = self.calc.power(2, 8)
        self.assertEqual(result, 256)


class TestScientificOperations(unittest.TestCase):
    """Test scientific operations"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_square_root(self):
        """Test square root"""
        result = self.calc.square_root(16)
        self.assertEqual(result, 4)
    
    def test_square_root_negative(self):
        """Test square root of negative number raises error"""
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_square(self):
        """Test square operation"""
        result = self.calc.square(5)
        self.assertEqual(result, 25)
    
    def test_cube(self):
        """Test cube operation"""
        result = self.calc.cube(3)
        self.assertEqual(result, 27)
    
    def test_absolute(self):
        """Test absolute value"""
        result = self.calc.absolute(-15)
        self.assertEqual(result, 15)
    
    def test_percentage(self):
        """Test percentage calculation"""
        result = self.calc.percentage(200, 15)
        self.assertEqual(result, 30)


class TestRemovedTrigonometricOperations(unittest.TestCase):
    """Ensure trigonometric operations are no longer exposed"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_trigonometric_methods_removed(self):
        """Trigonometric methods should not be available"""
        self.assertFalse(hasattr(self.calc, "sine"))
        self.assertFalse(hasattr(self.calc, "cosine"))
        self.assertFalse(hasattr(self.calc, "tangent"))


class TestLogarithmicOperations(unittest.TestCase):
    """Test logarithmic operations"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_logarithm(self):
        """Test logarithm with base"""
        result = self.calc.logarithm(100, 10)
        self.assertEqual(result, 2)
    
    def test_natural_logarithm(self):
        """Test natural logarithm"""
        result = self.calc.natural_logarithm(math.e)
        self.assertAlmostEqual(result, 1, places=5)
    
    def test_logarithm_invalid_number(self):
        """Test logarithm with invalid number"""
        with self.assertRaises(ValueError):
            self.calc.logarithm(-5)
    
    def test_logarithm_invalid_base(self):
        """Test logarithm with invalid base"""
        with self.assertRaises(ValueError):
            self.calc.logarithm(10, 1)


class TestStatisticalOperations(unittest.TestCase):
    """Test statistical operations"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_average(self):
        """Test average calculation"""
        result = self.calc.average([10, 20, 30, 40])
        self.assertEqual(result, 25)
    
    def test_average_empty_list(self):
        """Test average with empty list"""
        with self.assertRaises(ValueError):
            self.calc.average([])
    
    def test_sum_numbers(self):
        """Test sum operation"""
        result = self.calc.sum_numbers([5, 10, 15])
        self.assertEqual(result, 30)
    
    def test_factorial(self):
        """Test factorial"""
        result = self.calc.factorial(5)
        self.assertEqual(result, 120)
    
    def test_factorial_negative(self):
        """Test factorial with negative number"""
        with self.assertRaises(ValueError):
            self.calc.factorial(-5)
    
    def test_factorial_float(self):
        """Test factorial with float"""
        with self.assertRaises(ValueError):
            self.calc.factorial(5.5)


class TestAdvancedOperations(unittest.TestCase):
    """Test advanced calculator operations"""
    
    def setUp(self):
        self.calc = AdvancedCalculator()
    
    def test_combination(self):
        """Test combination"""
        result = self.calc.combination(5, 2)
        self.assertEqual(result, 10)
    
    def test_permutation(self):
        """Test permutation"""
        result = self.calc.permutation(5, 2)
        self.assertEqual(result, 20)
    
    def test_gcd(self):
        """Test greatest common divisor"""
        result = self.calc.greatest_common_divisor(48, 18)
        self.assertEqual(result, 6)
    
    def test_lcm(self):
        """Test least common multiple"""
        result = self.calc.least_common_multiple(12, 18)
        self.assertEqual(result, 36)


class TestUtilityOperations(unittest.TestCase):
    """Test utility operations"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_round_result(self):
        """Test rounding"""
        result = self.calc.round_result(3.14159, 2)
        self.assertEqual(result, 3.14)
    
    def test_convert_to_percentage(self):
        """Test conversion to percentage"""
        result = self.calc.convert_to_percentage(0.25)
        self.assertEqual(result, 25)


class TestCurrentValue(unittest.TestCase):
    """Test current value tracking"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_current_value_updated(self):
        """Test that current value is updated after operation"""
        self.calc.add(5, 3)
        self.assertEqual(self.calc.current_value, 8)
    
    def test_get_last_result(self):
        """Test getting last result"""
        self.calc.multiply(4, 5)
        self.calc.add(10, 10)
        self.assertEqual(self.calc.get_last_result(), 20)


if __name__ == "__main__":
    unittest.main()
