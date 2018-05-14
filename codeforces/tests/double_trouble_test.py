"""Test cases for Codeforces Double Trouble challenge.

Challenge Constraints:

- Time limit per test: 1 second
- 1 <= n <= 10 ** 5
- n integers a1, a2, ..., an (0 <= ai <= 10 ** 6)

"""
import random

from utils.test_utils import assert_time_limit
from codeforces.double_trouble import solve


def test_challenge_sample_test_cases():
    assert solve([3, 2, 1, 5, 4]) == 4
    assert solve([1000000, 0]) == -1


def test_single_element_sequence():
    assert solve([0]) == 0
    assert solve([1]) == 0
    assert solve([10 ** 6]) == 0


def test_zeros_only_sequence():
    assert solve([0, 0]) == 0
    assert solve([0, 0, 0, 0, 0, 0, 0, 0]) == 0


def test_zeros_before_non_zero_numbers():
    assert solve([0, 0, 0, 0, 1, 2, 5]) == 0
    assert solve([0, 0, 0, 0, 4, 2, 1]) == 3


def test_same_number_sequence():
    assert solve([5, 5]) == 0
    assert solve([10, 10, 10, 10, 10, 10]) == 0


def test_impossible_to_get_non_decreasing_sequence():
    assert solve([10, 20, 30, 10, 20, 30, 0]) == -1
    assert solve([10, 20, 30, 0, 20, 0, 30]) == -1
    assert solve([0, 20, 0, 0, 0, 30, 30]) == -1
    assert solve([10, 20, 30, 40, 50, 60, 0]) == -1
    assert solve([10, 20, 30, 40, 0, 50, 60]) == -1


def test_large_single_number_at_the_start():
    # log base 2 of 10**6 is 19.9 aprox; thus, the second number needs to be
    # at least 2**20, and the third one needs to be at least 3 * 2**19.
    assert solve([10 ** 6, 1, 3]) == 20 + 19


def test_large_and_small_numbers_mix():
    # second number increased to 2 ** 15, third to 7 * (2 ** 13)
    assert solve([2 ** 15, 1, 7 * (2 ** 10), 2 ** 18]) == 15 + 3


def test_simple_test_cases():
    assert solve([2, 4, 8, 1, 1]) == 3 + 3
    assert solve([2, 4, 9, 1, 1]) == 4 + 4
    assert solve([2, 4, 9, 1, 1, 16]) == 4 + 4
    assert solve([2, 4, 9, 1, 1, 20]) == 4 + 4
    assert solve([1, 4, 1, 4, 1, 4]) == 2 + 2
    assert solve([4, 4, 1, 4, 1, 4]) == 2 + 2
    assert solve([4, 5, 1, 4, 1, 4]) == 3 + 1 + 3 + 1


def test_large_repeating_sequence():
    times = (10 ** 5) // 2
    assert solve([2 ** 15, 1] * times) == 15 * times
    assert solve([1, 2 ** 15] * times) == 15 * times - 15


def test_time_limit_max_size_fixed_repeating_sequence():
    array = [2, 1, 5, 2, 7, 2, 1, 15, 3, 1] * (10 ** 4)
    assert_time_limit(1, solve, array)

    array = [72, 1, 35, 2, 65, 300, 12, 9520, 3, 1] * (10 ** 4)
    assert_time_limit(1, solve, array)

    array = [10 ** 6, 1, 51, 3, 10 ** 4, 5, 12, 10 ** 5, 3, 7] * (10 ** 4)
    assert_time_limit(1, solve, array)

    array = [15E3, 1, 15E3, 3, 15E3, 5, 15E3, 7, 15E3, 11] * (10 ** 4)
    assert_time_limit(1, solve, array)


def test_time_limit_max_size_random_sequence():
    array = [random.randint(0, 10 ** 6) for _ in range(10 ** 5)]
    assert_time_limit(1, solve, array)


def test_time_limit_max_size_random_sequence_without_zeros():
    array = [random.randint(1, 10 ** 6) for _ in range(10 ** 5)]
    assert_time_limit(1, solve, array)
