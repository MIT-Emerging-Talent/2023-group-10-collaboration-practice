import unittest
import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from randomize_array import randomize_array


class TestRandomizeArray(unittest.TestCase):
    def test_randomize_array(self):
        """
        This test case checks if the randomize_array function correctly randomizes
        the order of elements in a non-empty array. It ensures that the original
        array and the randomized array are not equal and that they have the same
        elements, though possibly in a different order.
        """
        original_array = [1, 2, 3, 4, 5]
        randomized_array = randomize_array(original_array.copy())
        self.assertNotEqual(original_array, randomized_array)
        self.assertEqual(sorted(original_array), sorted(randomized_array))

    def test_randomize_array_empty(self):
        """
        This test case checks if the randomize_array function correctly handles
        an empty input array. It ensures that shuffling an empty array results in
        an empty array, and the original array is equal to the randomized array.
        """
        original_array = []
        randomized_array = randomize_array(original_array.copy())
        self.assertEqual(original_array, randomized_array)

    def test_randomize_array_single(self):
        """
        This test case checks if the randomize_array function correctly handles
        a single-element input array. It ensures that shuffling a single-element
        array does not change its order, and the original array is equal to the
        randomized array.
        """
        original_array = [1]
        randomized_array = randomize_array(original_array.copy())
        self.assertEqual(original_array, randomized_array)


if __name__ == "__main__":
    unittest.main()
