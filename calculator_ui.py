"""
Interactive Command-Line User Interface for Calculator
Provides a user-friendly interface for calculator operations
"""

from calculator import Calculator, AdvancedCalculator


class CalculatorUI:
    """Interactive UI for calculator"""
    
    def __init__(self):
        self.calculator = AdvancedCalculator()
        self.running = True
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*70)
        print("ADVANCED CALCULATOR SYSTEM")
        print("="*70)
        print("\nSelect operation:")
        print("\n--- BASIC ARITHMETIC ---")
        print("1.  Addition (+)")
        print("2.  Subtraction (-)")
        print("3.  Multiplication (*)")
        print("4.  Division (/)")
        print("5.  Modulo (%)")
        print("6.  Power (**)")
        print("\n--- SCIENTIFIC ---")
        print("7.  Square Root (√)")
        print("8.  Square (x²)")
        print("9.  Cube (x³)")
        print("10. Absolute Value (|x|)")
        print("11. Percentage")
        print("\n--- LOGARITHMIC ---")
        print("12. Logarithm (log)")
        print("13. Natural Logarithm (ln)")
        print("\n--- STATISTICAL ---")
        print("14. Average")
        print("15. Sum")
        print("16. Factorial (!)")
        print("\n--- ADVANCED ---")
        print("17. Combination (nCr)")
        print("18. Permutation (nPr)")
        print("19. GCD")
        print("20. LCM")
        print("\n--- HISTORY & UTILITIES ---")
        print("21. View History")
        print("22. Clear History")
        print("23. Round Number")
        print("24. Convert to Percentage")
        print("\n0.  Exit")
        print("="*70)
    
    def get_two_numbers(self, prompt: str = "") -> tuple:
        """Get two numbers from user"""
        try:
            if prompt:
                print(prompt)
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return None, None
    
    def get_single_number(self, prompt: str = "") -> float:
        """Get single number from user"""
        try:
            if prompt:
                print(prompt)
            return float(input("Enter number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            return None
    
    def get_number_list(self) -> list:
        """Get list of numbers from user"""
        try:
            numbers_str = input("Enter numbers separated by commas (e.g., 1,2,3,4): ")
            return [float(x.strip()) for x in numbers_str.split(",")]
        except ValueError:
            print("Invalid input! Please enter numeric values separated by commas.")
            return []
    
    def handle_basic_arithmetic(self, choice: str):
        """Handle basic arithmetic operations"""
        a, b = self.get_two_numbers()
        if a is None or b is None:
            return
        
        try:
            if choice == '1':
                result = self.calculator.add(a, b)
                print(f"\n✓ Result: {a} + {b} = {result}")
            elif choice == '2':
                result = self.calculator.subtract(a, b)
                print(f"\n✓ Result: {a} - {b} = {result}")
            elif choice == '3':
                result = self.calculator.multiply(a, b)
                print(f"\n✓ Result: {a} * {b} = {result}")
            elif choice == '4':
                result = self.calculator.divide(a, b)
                print(f"\n✓ Result: {a} / {b} = {result:.6f}")
            elif choice == '5':
                result = self.calculator.modulo(int(a), int(b))
                print(f"\n✓ Result: {int(a)} % {int(b)} = {result}")
            elif choice == '6':
                result = self.calculator.power(a, b)
                print(f"\n✓ Result: {a} ** {b} = {result}")
        except ValueError as e:
            print(f"\n✗ Error: {e}")
    
    def handle_scientific_operations(self, choice: str):
        """Handle scientific operations"""
        try:
            if choice == '7':
                num = self.get_single_number("Calculate square root:")
                if num is None:
                    return
                result = self.calculator.square_root(num)
                print(f"\n✓ √{num} = {result:.6f}")
            elif choice == '8':
                num = self.get_single_number("Calculate square:")
                if num is None:
                    return
                result = self.calculator.square(num)
                print(f"\n✓ {num}² = {result}")
            elif choice == '9':
                num = self.get_single_number("Calculate cube:")
                if num is None:
                    return
                result = self.calculator.cube(num)
                print(f"\n✓ {num}³ = {result}")
            elif choice == '10':
                num = self.get_single_number("Calculate absolute value:")
                if num is None:
                    return
                result = self.calculator.absolute(num)
                print(f"\n✓ |{num}| = {result}")
            elif choice == '11':
                a, b = self.get_two_numbers("Calculate percentage:")
                if a is None or b is None:
                    return
                result = self.calculator.percentage(a, b)
                print(f"\n✓ {b}% of {a} = {result}")
        except ValueError as e:
            print(f"\n✗ Error: {e}")
    
    def handle_logarithmic_operations(self, choice: str):
        """Handle logarithmic operations"""
        try:
            if choice == '12':
                num = float(input("Enter number: "))
                base = float(input("Enter base (default=10): ") or "10")
                result = self.calculator.logarithm(num, base)
                print(f"\n✓ log_{base}({num}) = {result:.6f}")
            elif choice == '13':
                num = float(input("Enter number: "))
                result = self.calculator.natural_logarithm(num)
                print(f"\n✓ ln({num}) = {result:.6f}")
        except ValueError as e:
            print(f"\n✗ Error: {e}")
    
    def handle_statistical_operations(self, choice: str):
        """Handle statistical operations"""
        try:
            if choice == '14':
                numbers = self.get_number_list()
                if not numbers:
                    return
                result = self.calculator.average(numbers)
                print(f"\n✓ Average: {result:.6f}")
            elif choice == '15':
                numbers = self.get_number_list()
                if not numbers:
                    return
                result = self.calculator.sum_numbers(numbers)
                print(f"\n✓ Sum: {result}")
            elif choice == '16':
                num = int(float(input("Enter number: ")))
                result = self.calculator.factorial(num)
                print(f"\n✓ {num}! = {result}")
        except ValueError as e:
            print(f"\n✗ Error: {e}")
    
    def handle_advanced_operations(self, choice: str):
        """Handle advanced operations"""
        try:
            if choice == '17':
                n = int(float(input("Enter n: ")))
                r = int(float(input("Enter r: ")))
                result = self.calculator.combination(n, r)
                print(f"\n✓ C({n},{r}) = {result}")
            elif choice == '18':
                n = int(float(input("Enter n: ")))
                r = int(float(input("Enter r: ")))
                result = self.calculator.permutation(n, r)
                print(f"\n✓ P({n},{r}) = {result}")
            elif choice == '19':
                a = int(float(input("Enter first number: ")))
                b = int(float(input("Enter second number: ")))
                result = self.calculator.greatest_common_divisor(a, b)
                print(f"\n✓ GCD({a},{b}) = {result}")
            elif choice == '20':
                a = int(float(input("Enter first number: ")))
                b = int(float(input("Enter second number: ")))
                result = self.calculator.least_common_multiple(a, b)
                print(f"\n✓ LCM({a},{b}) = {result}")
        except ValueError as e:
            print(f"\n✗ Error: {e}")
    
    def handle_utility_operations(self, choice: str):
        """Handle utility operations"""
        try:
            if choice == '21':
                self.calculator.print_history()
            elif choice == '22':
                self.calculator.clear_history()
                print("\n✓ History cleared!")
            elif choice == '23':
                num = float(input("Enter number: "))
                places = int(input("Enter decimal places (default=2): ") or "2")
                result = self.calculator.round_result(num, places)
                print(f"\n✓ Rounded: {result}")
            elif choice == '24':
                num = float(input("Enter decimal number: "))
                result = self.calculator.convert_to_percentage(num)
                print(f"\n✓ {num} = {result}%")
        except ValueError as e:
            print(f"\n✗ Error: {e}")
    
    def run(self):
        """Run the calculator interface"""
        print("\n" + "="*70)
        print("Welcome to Advanced Calculator System")
        print("="*70)
        
        while self.running:
            self.display_menu()
            choice = input("Enter your choice (0-24): ").strip()
            
            if choice == '0':
                print("\nThank you for using Calculator! Goodbye!")
                self.running = False
            elif choice in ['1', '2', '3', '4', '5', '6']:
                self.handle_basic_arithmetic(choice)
            elif choice in ['7', '8', '9', '10', '11']:
                self.handle_scientific_operations(choice)
            elif choice in ['12', '13']:
                self.handle_logarithmic_operations(choice)
            elif choice in ['14', '15', '16']:
                self.handle_statistical_operations(choice)
            elif choice in ['17', '18', '19', '20']:
                self.handle_advanced_operations(choice)
            elif choice in ['21', '22', '23', '24']:
                self.handle_utility_operations(choice)
            else:
                print("\n✗ Invalid choice! Please try again.")


if __name__ == "__main__":
    ui = CalculatorUI()
    ui.run()
