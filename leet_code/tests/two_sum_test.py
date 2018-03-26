"""Tests for the Two Sum challenge."""
import unittest

from leet_code.two_sum import get_indices


class TestTwoSum(unittest.TestCase):
    """TestCase for get_indices function"""

    def test_challenge_example(self):
        array, target = [2, 7, 11, 15], 9
        self.assertEqual(get_indices(array, target), [0, 1])

    def test_indices_of_both_numbers_are_next_to_each_other(self):
        array, target = [1, 3, 5, 6, 9, 12], 11
        self.assertEqual(get_indices(array, target), [2, 3])

    def test_indices_of_both_numbers_are_apart_from_each_other(self):
        array, target = [2, 3, 5, 9, 9, 10], 12
        self.assertEqual(get_indices(array, target), [1, 3])

    # The problem does not say anything about the array been sorte or not
    def test_indices_on_an_unsorted_array(self):
        array, target = [8, 3, 5, 4, 19, 25], 7
        self.assertEqual(get_indices(array, target), [1, 3])


if __name__ == '__main__':
    unittest.main()
