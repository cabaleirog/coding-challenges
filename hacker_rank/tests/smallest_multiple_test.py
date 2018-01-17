"""Tests for Project Euler #5: Smallest multiple."""
import unittest

from hacker_rank.smallest_multiple import smallest_multiple


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


if __name__ == '__main__':
    unittest.main()
