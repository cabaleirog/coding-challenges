"""Tests for Project Euler #8: Largest product in a series."""
import unittest

from hacker_rank.largest_product_in_a_series import (
    greatest_product,
    get_reduced_array
)


class TestSmallestMultiple(unittest.TestCase):

    def test_website_example(self):
        self.assertEqual(3150, greatest_product(3675356291, 5))
        self.assertEqual(0, greatest_product(2709360626, 5))

    def test_reduced_array_single_group(self):
        groups = get_reduced_array(12373, 2)
        self.assertTrue(len(groups) == 1)
        self.assertListEqual([7, 3], groups[0])

    def test_reduced_array_single_group_increasing_digits(self):
        groups = get_reduced_array(12345, 2)
        self.assertTrue(len(groups) == 1)
        self.assertListEqual([4, 5], groups[0])

    def test_reduced_array_multiple_groups(self):
        groups = get_reduced_array(2751351, 2)
        self.assertTrue(len(groups) == 3)
        self.assertIn([7, 5], groups)
        self.assertIn([5, 1], groups)
        self.assertIn([3, 5], groups)

    def test_reduced_array_same_digits(self):
        groups = get_reduced_array(222222, 2)
        self.assertTrue(len(groups) == 1)
        self.assertIn([2, 2], groups)

    def test_reduced_array_zeros(self):
        groups = get_reduced_array(20202020, 2)
        self.assertTrue(len(groups) == 1)
        self.assertIn(0, groups[0])
        self.assertIn(2, groups[0])


if __name__ == '__main__':
    unittest.main()
