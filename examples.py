"""
Comprehensive examples demonstrating all calculator functions
Shows practical usage patterns and best practices
"""

from calculator import Calculator, AdvancedCalculator, CalculationHistory


def example_basic_arithmetic():
    """Demonstrate basic arithmetic operations"""
    print("\n" + "="*70)
    print("BASIC ARITHMETIC OPERATIONS")
    print("="*70)
    
    calc = Calculator()
    
    print("\nAddition:")
    print(f"  10 + 5 = {calc.add(10, 5)}")
    print(f"  100 + 250 = {calc.add(100, 250)}")
    
    print("\nSubtraction:")
    print(f"  20 - 8 = {calc.subtract(20, 8)}")
    print(f"  50 - 75 = {calc.subtract(50, 75)}")
    
    print("\nMultiplication:")
    print(f"  12 * 3 = {calc.multiply(12, 3)}")
    print(f"  15 * 15 = {calc.multiply(15, 15)}")
    
    print("\nDivision:")
    print(f"  100 / 4 = {calc.divide(100, 4)}")
    print(f"  1 / 3 = {calc.divide(1, 3):.6f}")
    
    print("\nPower:")
    print(f"  2 ^ 8 = {calc.power(2, 8)}")
    print(f"  3 ^ 4 = {calc.power(3, 4)}")
    
    print("\nModulo:")
    print(f"  10 % 3 = {calc.modulo(10, 3)}")
    print(f"  17 % 5 = {calc.modulo(17, 5)}")


def example_scientific_operations():
    """Demonstrate scientific operations"""
    print("\n" + "="*70)
    print("SCIENTIFIC OPERATIONS")
    print("="*70)
    
    calc = Calculator()
    
    print("\nSquare Root:")
    print(f"  √16 = {calc.square_root(16)}")
    print(f"  √100 = {calc.square_root(100)}")
    print(f"  √2 = {calc.square_root(2):.6f}")
    
    print("\nSquare:")
    print(f"  5² = {calc.square(5)}")
    print(f"  12² = {calc.square(12)}")
    
    print("\nCube:")
    print(f"  3³ = {calc.cube(3)}")
    print(f"  5³ = {calc.cube(5)}")
    
    print("\nAbsolute Value:")
    print(f"  |-15| = {calc.absolute(-15)}")
    print(f"  |42| = {calc.absolute(42)}")
    
    print("\nPercentage:")
    print(f"  25% of 200 = {calc.percentage(200, 25)}")
    print(f"  15% of 1000 = {calc.percentage(1000, 15)}")


def example_trigonometric_operations():
    """Demonstrate trigonometric operations"""
    print("\n" + "="*70)
    print("TRIGONOMETRIC OPERATIONS")
    print("="*70)
    
    calc = Calculator()
    
    print("\nSine (sin):")
    print(f"  sin(0°) = {calc.sine(0):.6f}")
    print(f"  sin(90°) = {calc.sine(90):.6f}")
    print(f"  sin(180°) = {calc.sine(180):.10f}")
    
    print("\nCosine (cos):")
    print(f"  cos(0°) = {calc.cosine(0):.6f}")
    print(f"  cos(60°) = {calc.cosine(60):.6f}")
    print(f"  cos(90°) = {calc.cosine(90):.10f}")
    
    print("\nTangent (tan):")
    print(f"  tan(0°) = {calc.tangent(0):.6f}")
    print(f"  tan(45°) = {calc.tangent(45):.6f}")


def example_logarithmic_operations():
    """Demonstrate logarithmic operations"""
    print("\n" + "="*70)
    print("LOGARITHMIC OPERATIONS")
    print("="*70)
    
    calc = Calculator()
    
    print("\nLogarithm (base 10):")
    print(f"  log₁₀(1) = {calc.logarithm(1, 10)}")
    print(f"  log₁₀(10) = {calc.logarithm(10, 10)}")
    print(f"  log₁₀(100) = {calc.logarithm(100, 10)}")
    print(f"  log₁₀(1000) = {calc.logarithm(1000, 10)}")
    
    print("\nLogarithm (base 2):")
    print(f"  log₂(8) = {calc.logarithm(8, 2)}")
    print(f"  log₂(16) = {calc.logarithm(16, 2)}")
    print(f"  log₂(32) = {calc.logarithm(32, 2)}")
    
    print("\nNatural Logarithm (ln):")
    print(f"  ln(1) = {calc.natural_logarithm(1)}")
    print(f"  ln(e) = {calc.natural_logarithm(2.71828):.6f}")
    print(f"  ln(10) = {calc.natural_logarithm(10):.6f}")


def example_statistical_operations():
    """Demonstrate statistical operations"""
    print("\n" + "="*70)
    print("STATISTICAL OPERATIONS")
    print("="*70)
    
    calc = Calculator()
    
    print("\nAverage:")
    nums1 = [10, 20, 30, 40, 50]
    print(f"  Average of {nums1} = {calc.average(nums1)}")
    
    nums2 = [5, 10, 15, 20]
    print(f"  Average of {nums2} = {calc.average(nums2)}")
    
    print("\nSum:")
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"  Sum of {nums3} = {calc.sum_numbers(nums3)}")
    
    print("\nFactorial:")
    for n in [3, 4, 5, 6, 7, 8]:
        print(f"  {n}! = {calc.factorial(n)}")


def example_advanced_operations():
    """Demonstrate advanced operations"""
    print("\n" + "="*70)
    print("ADVANCED OPERATIONS")
    print("="*70)
    
    calc = AdvancedCalculator()
    
    print("\nCombination (nCr) - 'n choose r':")
    print(f"  C(5,2) = {calc.combination(5, 2)}")
    print(f"  C(10,3) = {calc.combination(10, 3)}")
    print(f"  C(6,2) = {calc.combination(6, 2)}")
    
    print("\nPermutation (nPr) - Arrangement:")
    print(f"  P(5,2) = {calc.permutation(5, 2)}")
    print(f"  P(10,3) = {calc.permutation(10, 3)}")
    print(f"  P(6,2) = {calc.permutation(6, 2)}")
    
    print("\nGreatest Common Divisor (GCD):")
    print(f"  GCD(48, 18) = {calc.greatest_common_divisor(48, 18)}")
    print(f"  GCD(100, 75) = {calc.greatest_common_divisor(100, 75)}")
    print(f"  GCD(12, 18) = {calc.greatest_common_divisor(12, 18)}")
    
    print("\nLeast Common Multiple (LCM):")
    print(f"  LCM(12, 18) = {calc.least_common_multiple(12, 18)}")
    print(f"  LCM(4, 6) = {calc.least_common_multiple(4, 6)}")
    print(f"  LCM(10, 15) = {calc.least_common_multiple(10, 15)}")


def example_utility_operations():
    """Demonstrate utility operations"""
    print("\n" + "="*70)
    print("UTILITY OPERATIONS")
    print("="*70)
    
    calc = Calculator()
    
    print("\nRounding:")
    print(f"  round(3.14159, 2) = {calc.round_result(3.14159, 2)}")
    print(f"  round(2.71828, 4) = {calc.round_result(2.71828, 4)}")
    
    print("\nConvert to Percentage:")
    print(f"  0.25 = {calc.convert_to_percentage(0.25)}%")
    print(f"  0.75 = {calc.convert_to_percentage(0.75)}%")
    print(f"  0.333 = {calc.convert_to_percentage(0.333)}%")


def example_history_management():
    """Demonstrate history management"""
    print("\n" + "="*70)
    print("HISTORY MANAGEMENT")
    print("="*70)
    
    calc = Calculator()
    
    print("\nPerforming calculations...")
    calc.add(10, 5)
    calc.multiply(3, 7)
    calc.power(2, 5)
    calc.square_root(144)
    
    print("\nCalculation History:")
    calc.print_history()
    
    print(f"Last Result: {calc.get_last_result()}")


def example_error_handling():
    """Demonstrate error handling"""
    print("\n" + "="*70)
    print("ERROR HANDLING EXAMPLES")
    print("="*70)
    
    calc = Calculator()
    
    print("\n1. Division by Zero:")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n2. Square Root of Negative Number:")
    try:
        calc.square_root(-5)
    except ValueError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n3. Logarithm of Negative Number:")
    try:
        calc.logarithm(-10)
    except ValueError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n4. Invalid Logarithm Base:")
    try:
        calc.logarithm(10, 1)
    except ValueError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n5. Factorial of Negative Number:")
    try:
        calc.factorial(-5)
    except ValueError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n6. Average of Empty List:")
    try:
        calc.average([])
    except ValueError as e:
        print(f"   ✓ Caught: {e}")


def example_chained_operations():
    """Demonstrate chained operations"""
    print("\n" + "="*70)
    print("CHAINED OPERATIONS EXAMPLE")
    print("="*70)
    
    calc = AdvancedCalculator()
    
    print("\nCalculating: ((10 + 5) * 2) - 3")
    result1 = calc.add(10, 5)      # 15
    print(f"Step 1: 10 + 5 = {result1}")
    
    result2 = calc.multiply(result1, 2)  # 30
    print(f"Step 2: 15 * 2 = {result2}")
    
    result3 = calc.subtract(result2, 3)  # 27
    print(f"Step 3: 30 - 3 = {result3}")
    
    print(f"\nFinal Result: {result3}")
    print("\nFull History:")
    calc.print_history()


def run_all_examples():
    """Run all examples"""
    print("\n" + "█"*70)
    print("CALCULATOR SYSTEM - COMPREHENSIVE EXAMPLES")
    print("█"*70)
    
    example_basic_arithmetic()
    example_scientific_operations()
    example_trigonometric_operations()
    example_logarithmic_operations()
    example_statistical_operations()
    example_advanced_operations()
    example_utility_operations()
    example_history_management()
    example_error_handling()
    example_chained_operations()
    
    print("\n" + "█"*70)
    print("ALL EXAMPLES COMPLETED")
    print("█"*70 + "\n")


if __name__ == "__main__":
    run_all_examples()
