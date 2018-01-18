"""Tests for Project Euler #5: Smallest multiple."""
import unittest

from hacker_rank.smallest_multiple import (
    factorize,
    get_prime_numbers,
    is_prime,
    smallest_multiple)


class TestSmallestMultiple(unittest.TestCase):

    def test_website_example(self):
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(10), 2520)

    def test_increasing_number(self):
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(6), 60)
        self.assertEqual(smallest_multiple(7), 420)
        self.assertEqual(smallest_multiple(8), 840)
        self.assertEqual(smallest_multiple(9), 2520)
        self.assertEqual(smallest_multiple(10), 2520)
        self.assertEqual(smallest_multiple(11), 27720)
        self.assertEqual(smallest_multiple(12), 27720)
        self.assertEqual(smallest_multiple(13), 360360)
        self.assertEqual(smallest_multiple(14), 360360)
        self.assertEqual(smallest_multiple(15), 360360)
        self.assertEqual(smallest_multiple(16), 720720)
        self.assertEqual(smallest_multiple(17), 12252240)

    def test_number_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(17))

    def test_number_is_not_prime(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(21))

    def test_get_prime_numbers(self):
        self.assertEqual(get_prime_numbers(-1), set())
        self.assertEqual(get_prime_numbers(0), set())
        self.assertEqual(get_prime_numbers(1), set())
        self.assertEqual(get_prime_numbers(2), {2})
        self.assertEqual(get_prime_numbers(3), {2, 3})
        self.assertEqual(get_prime_numbers(10), {2, 3, 5, 7})
        self.assertEqual(get_prime_numbers(19), {2, 3, 5, 7, 11, 13, 17, 19})


    def test_number_factorization(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(factorize(7, primes), [7])
        self.assertEqual(factorize(8, primes), [2, 2, 2])
        self.assertEqual(factorize(25, primes), [5, 5])
        self.assertEqual(factorize(50, primes), [2, 5, 5])


if __name__ == '__main__':
    unittest.main()
