import unittest
import math
from calculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    """
    Unit tests for Scientific Calculator
    """
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = ScientificCalculator()
    
    def test_square_root_positive_numbers(self):
        """Test square root with positive numbers"""
        self.assertEqual(self.calc.square_root(4), 2.0)
        self.assertEqual(self.calc.square_root(9), 3.0)
        self.assertEqual(self.calc.square_root(16), 4.0)
        self.assertEqual(self.calc.square_root(25), 5.0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        self.assertEqual(self.calc.square_root(0), 0.0)
    
    def test_square_root_negative_number(self):
        """Test square root with negative numbers (should raise ValueError)"""
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
        with self.assertRaises(ValueError):
            self.calc.square_root(-10)
    
    def test_factorial_positive_integers(self):
        """Test factorial with positive integers"""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
    
    def test_factorial_negative_numbers(self):
        """Test factorial with negative numbers (should raise ValueError)"""
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        with self.assertRaises(ValueError):
            self.calc.factorial(-5)
    
    def test_factorial_non_integer(self):
        """Test factorial with non-integer values (should raise ValueError)"""
        with self.assertRaises(ValueError):
            self.calc.factorial(3.5)
        with self.assertRaises(ValueError):
            self.calc.factorial(2.1)
    
    def test_natural_logarithm_positive_numbers(self):
        """Test natural logarithm with positive numbers"""
        self.assertEqual(self.calc.natural_logarithm(1), 0.0)
        self.assertAlmostEqual(self.calc.natural_logarithm(math.e), 1.0)
        self.assertAlmostEqual(self.calc.natural_logarithm(10), 2.302585092994046)
        self.assertAlmostEqual(self.calc.natural_logarithm(2), 0.6931471805599453)
    
    def test_natural_logarithm_zero_and_negative(self):
        """Test natural logarithm with zero and negative numbers (should raise ValueError)"""
        with self.assertRaises(ValueError):
            self.calc.natural_logarithm(0)
        with self.assertRaises(ValueError):
            self.calc.natural_logarithm(-1)
        with self.assertRaises(ValueError):
            self.calc.natural_logarithm(-10)
    
    def test_power_positive_base_positive_exponent(self):
        """Test power function with positive base and positive exponent"""
        self.assertEqual(self.calc.power(2, 3), 8.0)
        self.assertEqual(self.calc.power(5, 2), 25.0)
        self.assertEqual(self.calc.power(10, 0), 1.0)
        self.assertEqual(self.calc.power(3, 4), 81.0)
    
    def test_power_negative_base(self):
        """Test power function with negative base"""
        self.assertEqual(self.calc.power(-2, 2), 4.0)
        self.assertEqual(self.calc.power(-3, 3), -27.0)
        self.assertEqual(self.calc.power(-1, 10), 1.0)
    
    def test_power_negative_exponent(self):
        """Test power function with negative exponent"""
        self.assertEqual(self.calc.power(2, -2), 0.25)
        self.assertEqual(self.calc.power(5, -1), 0.2)
        self.assertAlmostEqual(self.calc.power(10, -3), 0.001)
    
    def test_power_fractional_exponent(self):
        """Test power function with fractional exponent"""
        self.assertEqual(self.calc.power(4, 0.5), 2.0)
        self.assertEqual(self.calc.power(8, 1/3), 2.0)
        self.assertEqual(self.calc.power(9, 0.5), 3.0)
    
    def test_power_zero_base(self):
        """Test power function with zero base"""
        self.assertEqual(self.calc.power(0, 1), 0.0)
        self.assertEqual(self.calc.power(0, 5), 0.0)
        # Note: 0^0 is mathematically undefined, but Python returns 1.0
        self.assertEqual(self.calc.power(0, 0), 1.0)

class TestCalculatorEdgeCases(unittest.TestCase):
    """
    Additional edge case tests for Scientific Calculator
    """
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = ScientificCalculator()
    
    def test_large_numbers(self):
        """Test calculator with large numbers"""
        # Large square root
        self.assertAlmostEqual(self.calc.square_root(1000000), 1000.0)
        
        # Large power
        self.assertEqual(self.calc.power(10, 6), 1000000.0)
        
        # Natural log of large number
        result = self.calc.natural_logarithm(1000)
        self.assertAlmostEqual(result, 6.907755278982137)
    
    def test_very_small_numbers(self):
        """Test calculator with very small positive numbers"""
        # Small square root
        self.assertAlmostEqual(self.calc.square_root(0.01), 0.1)
        
        # Small natural log
        result = self.calc.natural_logarithm(0.1)
        self.assertAlmostEqual(result, -2.302585092994046)
        
        # Small power
        self.assertAlmostEqual(self.calc.power(0.1, 2), 0.01)

if __name__ == '__main__':
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes to the suite
    suite.addTests(loader.loadTestsFromTestCase(TestScientificCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorEdgeCases))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\nTest Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed!")
