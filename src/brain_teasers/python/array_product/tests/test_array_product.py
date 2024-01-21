import unittest
import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from array_product import product_of_array_except_self


class TestArrayProduct(unittest.TestCase):
    def test_array_product(self):
        """
        This test checks if the function correctly computes the product of all elements in an array,
        excluding the element at the current index.

        """
        input_array = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        actual = product_of_array_except_self(input_array)
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        """
        This test checks if the function correctly handles the case where the input array is empty.
        """
        input_array = []
        expected = []
        actual = product_of_array_except_self(input_array)
        self.assertEqual(actual, expected)

    def test_array_with_one_element(self):
        """
        This test checks if the function correctly handles the case where the input array has only one element.
        """
        input_array = [1]
        expected = [1]
        actual = product_of_array_except_self(input_array)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
