"""TestCase for the Rank elements in an array challenge"""
import unittest

from geek_for_geeks.rank_elements_array import get_ranks


class TestRankArrayElementsArray(unittest.TestCase):

    def test_first_problem_example(self):
        values = [20, 30, 10]
        ranks = [2.0, 3.0, 1.0]
        self.assertEqual(get_ranks(values), ranks)

    def test_second_problem_example(self):
        values = [10, 12, 15, 12, 10, 25, 12]
        ranks = [1.5, 4.0, 6.0, 4.0, 1.5, 7.0, 4.0]
        self.assertEqual(get_ranks(values), ranks)

    def test_third_problem_example(self):
        values = [1, 2, 5, 2, 1, 60, 3]
        ranks = [1.5, 3.5, 6.0, 3.5, 1.5, 7.0, 5.0]
        self.assertEqual(get_ranks(values), ranks)

    def test_simple_sorted_list(self):
        values = [x for x in range(20)]
        ranks = [1.0 + float(x) for x in range(20)]
        self.assertEqual(get_ranks(values), ranks)


if __name__ == '__main__':
    unittest.main()
