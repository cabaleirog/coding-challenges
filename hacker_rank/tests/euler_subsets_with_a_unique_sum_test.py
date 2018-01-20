"""Tests for Project Euler #201: Subsets with a unique sum."""
import unittest

from hacker_rank.euler_subsets_with_a_unique_sum import get_sum


class TestUniqueSum(unittest.TestCase):

    def test_website_example(self):
        self.assertEqual(156, get_sum([1, 3, 6, 8, 10, 11], 3))

    def test_array_with_only_one_element(self):
        self.assertEqual(1, get_sum([1], 1))
        self.assertEqual(2, get_sum([2], 1))

    def test_n_equal_to_one(self):
        self.assertEqual(10, get_sum([1, 3, 6], 1))
        self.assertEqual(6, get_sum([3, 3, 6], 1))
        self.assertEqual(0, get_sum([5, 5, 5], 1))

    def test_n_equal_to_one_hundred(self):
        self.assertEqual(500, get_sum([5]*100, 100))
        self.assertEqual(0, get_sum([0]*100, 100))
        self.assertEqual(5, get_sum([1] * 98 + [2, 3], 2))
        self.assertEqual(0, get_sum([1, 2] + [3] * 98, 3))

    def test_item_with_multiple_ocurrences(self):
        self.assertEqual(0, get_sum([1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3))

    def test_with_increasing_one_element(self):
        self.assertEqual(76, get_sum([1, 3, 4, 6, 8], 3))
        self.assertEqual(90, get_sum([1, 3, 4, 6, 8, 8], 3))
        self.assertEqual(53, get_sum([1, 3, 4, 6, 8, 8, 8], 3))
        self.assertEqual(29, get_sum([1, 3, 4, 6, 8, 8, 8, 8], 3))
        self.assertEqual(29, get_sum([1, 3, 4, 6, 8, 8, 8, 8, 8], 3))
        self.assertEqual(29, get_sum([1, 3, 4, 6, 8, 8, 8, 8, 8, 8], 3))

    def test_increasing_group_size_with_duplicates(self):
        numbers = [1, 3, 4, 6, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
        self.assertEqual(14, get_sum(numbers, 1))
        self.assertEqual(9, get_sum(numbers, 2))
        self.assertEqual(18, get_sum(numbers, 3))
        self.assertEqual(54, get_sum(numbers, 4))
        self.assertEqual(0, get_sum(numbers, 5))
        self.assertEqual(28, get_sum(numbers, 6))
        self.assertEqual(67, get_sum(numbers, 7))
        self.assertEqual(0, get_sum(numbers, 8))
        self.assertEqual(52, get_sum(numbers, 9))
        self.assertEqual(91, get_sum(numbers, 10))
        self.assertEqual(0, get_sum(numbers, 11))
        self.assertEqual(184, get_sum(numbers, 12))
        self.assertEqual(220, get_sum(numbers, 13))
        self.assertEqual(229, get_sum(numbers, 14))
        self.assertEqual(462, get_sum(numbers, 15))
        self.assertEqual(119, get_sum(numbers, 16))


if __name__ == '__main__':
    unittest.main()
