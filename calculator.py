import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ScientificCalculator:
    """
    A scientific calculator class with basic mathematical operations
    """
    
    def __init__(self):
        logger.info("Scientific Calculator initialized")
    
    def square_root(self, x):
        """
        Calculate square root of x
        Args:
            x (float): Number to calculate square root of
        Returns:
            float: Square root of x
        Raises:
            ValueError: If x is negative
        """
        try:
            if x < 0:
                raise ValueError("Cannot calculate square root of negative number")
            result = math.sqrt(x)
            logger.info(f"Square root of {x} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in square_root: {e}")
            raise
    
    def factorial(self, x):
        """
        Calculate factorial of x
        Args:
            x (int): Non-negative integer to calculate factorial of
        Returns:
            int: Factorial of x
        Raises:
            ValueError: If x is negative or not an integer
        """
        try:
            if not isinstance(x, int) or x < 0:
                raise ValueError("Factorial requires a non-negative integer")
            result = math.factorial(x)
            logger.info(f"Factorial of {x} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in factorial: {e}")
            raise
    
    def natural_logarithm(self, x):
        """
        Calculate natural logarithm (base e) of x
        Args:
            x (float): Positive number to calculate ln of
        Returns:
            float: Natural logarithm of x
        Raises:
            ValueError: If x is less than or equal to 0
        """
        try:
            if x <= 0:
                raise ValueError("Natural logarithm requires a positive number")
            result = math.log(x)
            logger.info(f"Natural logarithm of {x} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in natural_logarithm: {e}")
            raise
    
    def power(self, x, b):
        """
        Calculate x raised to the power of b
        Args:
            x (float): Base number
            b (float): Exponent
        Returns:
            float: x raised to the power of b
        """
        try:
            result = math.pow(x, b)
            logger.info(f"{x} raised to the power of {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in power: {e}")
            raise

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("         SCIENTIFIC CALCULATOR")
    print("="*50)
    print("1. Square Root (√x)")
    print("2. Factorial (!x)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power (x^b)")
    print("5. Exit")
    print("="*50)

def get_number_input(prompt):
    """Get and validate number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_integer_input(prompt):
    """Get and validate integer input from user"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer!")

def main():
    """Main function to run the calculator"""
    calc = ScientificCalculator()
    
    print("Welcome to Scientific Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                # Square Root
                x = get_number_input("Enter a number for square root: ")
                try:
                    result = calc.square_root(x)
                    print(f"√{x} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '2':
                # Factorial
                x = get_integer_input("Enter a non-negative integer for factorial: ")
                try:
                    result = calc.factorial(x)
                    print(f"{x}! = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '3':
                # Natural Logarithm
                x = get_number_input("Enter a positive number for natural logarithm: ")
                try:
                    result = calc.natural_logarithm(x)
                    print(f"ln({x}) = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '4':
                # Power
                x = get_number_input("Enter the base number: ")
                b = get_number_input("Enter the exponent: ")
                try:
                    result = calc.power(x, b)
                    print(f"{x}^{b} = {result}")
                except Exception as e:
                    print(f"Error: {e}")
            
            elif choice == '5':
                print("Thank you for using Scientific Calculator!")
                logger.info("Calculator session ended")
                break
            
            else:
                print("Invalid choice! Please select 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nCalculator session interrupted.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()