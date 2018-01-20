"""Tests for problem Multiples of 3 and 5."""
import unittest

from hacker_rank.euler_multiples_of_three_and_five import (
    multiples,
    get_summation,
    get_sum
)


class TestSummationOfMultiples(unittest.TestCase):
    """TestCase for the get_summation method"""

    def test_problem_example(self):
        self.assertEqual(get_summation(10, [3, 5]), 23)
        self.assertEqual(get_summation(100, [3, 5]), 2318)

    def test_lowest_upper_bound(self):
        self.assertEqual(get_summation(1, [3, 5]), 0)

    def test_large_upper_bound(self):
        self.assertEqual(get_summation(1000, [3, 5]), 233168)

class TestSumOfMultiples(unittest.TestCase):
    """TestCase for the get_sum method"""

    def test_problem_example(self):
        self.assertEqual(get_sum(10, [3, 5]), 23)
        self.assertEqual(get_sum(100, [3, 5]), 2318)

    def test_lowest_upper_bound(self):
        self.assertEqual(get_sum(1, [3, 5]), 0)

    def test_large_upper_bound(self):
        self.assertEqual(get_sum(1000, [3, 5]), 233168)

    def test_chunks(self):
        self.assertEqual(get_sum(1000, [3, 5]), 233168)
        self.assertEqual(get_sum(1000, [3, 5]), 233168, 10)
        self.assertEqual(get_sum(1000, [3, 5]), 233168, 20)
        self.assertEqual(get_sum(1000, [3, 5]), 233168, 50)
        self.assertEqual(get_sum(1000, [3, 5]), 233168, 500)


class TestDividorsArray(unittest.TestCase):
    """TestCase for the get_divisors method"""

    def test_divisor_by_three(self):
        self.assertEqual(set(multiples([3], {3: 15})), {3, 6, 9, 12, 15})

    def test_divisor_by_five(self):
        self.assertEqual(set(multiples([5], {5: 15})), {5, 10, 15})


if __name__ == '__main__':
    unittest.main()
