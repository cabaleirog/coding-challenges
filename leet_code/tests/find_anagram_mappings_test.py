"""Tests for Find Anagram Mappings."""
import unittest

from leet_code.find_anagram_mappings import get_mapping


class TestAnagramMapping(unittest.TestCase):
    """TestCase for the Anagram mapping method"""

    def test_problem_example(self):
        arrays = [12, 28, 46, 32, 50], [50, 12, 32, 46, 28]
        self.assertEqual(get_mapping(*arrays), [1, 4, 3, 2, 0])

    def test_one_element(self):
        self.assertEqual(get_mapping([32], [32]), [0])

    def test_two_elements(self):
        self.assertEqual(get_mapping([32, 24], [32, 24]), [0, 1])
        self.assertEqual(get_mapping([32, 24], [24, 32]), [1, 0])

    def test_with_duplicated_elements(self):
        # Note: Multiple valid solutions can be created here. ie. [2,3,4,5,1,0]
        arrays = [1, 1, 1, 1, 5, 6], [6, 5, 1, 1, 1, 1]
        self.assertEqual(get_mapping(*arrays), [5, 4, 3, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
