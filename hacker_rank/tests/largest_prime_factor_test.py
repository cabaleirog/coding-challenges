"""Tests for Project Euler #3: Largest prime factor."""
import unittest

from hacker_rank.largest_prime_factor import factorize


class TestLargestPrimeFactor(unittest.TestCase):

    def test_website_example(self):
        self.assertEqual(factorize(10)[-1], 5)
        self.assertEqual(factorize(17)[-1], 17)

    def test_factorize(self):
        self.assertEqual(factorize(2 * 3 * 7 * 11), [2, 3, 7, 11])
        self.assertEqual(factorize(3 * 7 * 17), [3, 7, 17])
        self.assertEqual(factorize(5 * 17 * 19), [5, 17, 19])
        self.assertEqual(factorize(17 * 311 * 313 * 337), [17, 311, 313, 337])


if __name__ == '__main__':
    unittest.main()
