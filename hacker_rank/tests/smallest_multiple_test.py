"""Tests for Project Euler #5: Smallest multiple."""
import unittest

from hacker_rank.smallest_multiple import smallest_multiple


class TestSmallestMultiple(unittest.TestCase):

    def test_website_example(self):
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(10), 2520)


if __name__ == '__main__':
    unittest.main()
