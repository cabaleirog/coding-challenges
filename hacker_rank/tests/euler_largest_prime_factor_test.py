"""Tests for Project Euler #3: Largest prime factor."""
import unittest

from hacker_rank.euler_largest_prime_factor import factorize


class TestLargestPrimeFactor(unittest.TestCase):

    def test_factorize(self):
        self.assertEqual(factorize(2 * 2 * 2 * 5), [2, 5])
        self.assertEqual(factorize(2 * 17 * 17), [2, 17])
        self.assertEqual(factorize(2 * 2 * 2 * 17 * 19 * 19), [2, 17, 19])

    def test_factorize_non_repeating_primes_only(self):
        self.assertEqual(factorize(3 * 7 * 11), [3, 7, 11])
        self.assertEqual(factorize(3 * 7 * 17), [3, 7, 17])
        self.assertEqual(factorize(5 * 17 * 19), [5, 17, 19])
        self.assertEqual(factorize(17 * 311 * 313 * 337), [17, 311, 313, 337])

    def test_factorize_power_of_two(self):
        self.assertEqual(factorize(2 ** 0), [])
        self.assertEqual(factorize(2 ** 1), [2])
        self.assertEqual(factorize(2 ** 2), [2])
        self.assertEqual(factorize(2 ** 3), [2])
        self.assertEqual(factorize(2 ** 1000), [2])

    def test_factorize_outputs_a_sorted_list(self):
        for n in [7, 15, 30, 1550]:
            factors = factorize(n)
            self.assertEqual(factors, sorted(factors))


if __name__ == '__main__':
    unittest.main()
