#!/usr/bin/python3


import unittest
from my_module import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_max_integer(self):
        # Test case 1: List with positive integers
        nums = [1, 2, 3, 4, 5]
        result = max_integer(nums)
        self.assertEqual(result, 5)

        # Test case 2: List with negative integers
        nums = [-5, -2, -10, -1]
        result = max_integer(nums)
        self.assertEqual(result, -1)

        # Test case 3: List with mixed positive and negative integers
        nums = [-5, 2, -10, 3, -1]
        result = max_integer(nums)
        self.assertEqual(result, 3)

        # Test case 4: List with a single element
        nums = [7]
        result = max_integer(nums)
        self.assertEqual(result, 7)

        # Test case 5: Empty list
        nums = []
        result = max_integer(nums)
        self.assertIsNone(result)

        # Test case 6: List with duplicate maximum values
        nums = [5, 2, 10, 5, 1]
        result = max_integer(nums)
        self.assertEqual(result, 10)

        # Test case 7: List with float values
        nums = [3.14, 2.5, 1.8]
        result = max_integer(nums)
        self.assertEqual(result, 3.14)

        # Test case 8: List with a mix of integers and floats
        nums = [1, 2.5, 3, 4.7]
        result = max_integer(nums)
        self.assertEqual(result, 4.7)

if __name__ == '__main__':
    unittest.main()
