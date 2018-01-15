"""Tests for problem Multiples of 3 and 5."""
import unittest

from hacker_rank.multiples_of_three_and_five import get_divisors, get_sum


class TestSumOfMultiples(unittest.TestCase):
    """TestCase for the get_sum method"""

    def test_problem_example(self):
        self.assertEqual(get_sum(10, [3, 5]), 23)

    def test_lowest_upper_bound(self):
        self.assertEqual(get_sum(1, [3, 5]), 0)

    def test_large_upper_bound(self):
        self.assertEqual(get_sum(1000, [3, 5]), 233168)


class TestDividorsArray(unittest.TestCase):
    """TestCase for the get_divisors method"""

    def test_divisor_by_three(self):
        self.assertEqual(set(get_divisors([3], {3: 15})), {3, 6, 9, 12, 15})

    def test_divisor_by_five(self):
        self.assertEqual(set(get_divisors([5], {5: 15})), {5, 10, 15})


if __name__ == '__main__':
    unittest.main()
