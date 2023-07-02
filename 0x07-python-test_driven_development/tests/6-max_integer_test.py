#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the function max_integer
    """
    def test_empty_list(self):  # Check for empty list
        result = max_integer([])
        self.assertIsNone(result, None)

    def test_positive_numbers(self):  # check for positive numbers
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):  # check for negative numbers
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 0, 5, -10, 3])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        result = max_integer([3, 2, 3, 1, 3, 4])
        self.assertEqual(result, 4)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_large_list(self):
        result = max_integer(list(range(1, 1000001)))
        self.assertEqual(result, 1000000)

if __name__ == '__main__':
    unittest.main()
