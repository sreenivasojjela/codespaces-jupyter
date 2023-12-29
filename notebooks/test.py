# test.py

import unittest
from your_module import factorial  # Make sure to replace 'your_module' with the actual name of your Python module

class TestFactorialFunction(unittest.TestCase):

    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_of_float_number(self):
        with self.assertRaises(ValueError):
            factorial(5.5)

if __name__ == '__main__':
    unittest.main()
