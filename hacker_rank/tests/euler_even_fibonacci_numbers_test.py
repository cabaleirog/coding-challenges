from utils.test_utils import assert_time_limit_multitest
from hacker_rank.euler_even_fibonacci_numbers import (
    fibonacci,
    fibonacci_even_numbers)


def test_fibonacci_numbers():
    fib = fibonacci()
    numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert [next(fib) for _ in range(len(numbers))] == numbers


def test_sum_of_even_fibonacci_numbers():
    assert fibonacci_even_numbers(0) == 0
    assert fibonacci_even_numbers(2) == 0
    assert fibonacci_even_numbers(10) == 10
    assert fibonacci_even_numbers(100) == 44


# Time limit: 10 seconds.
def test_time_limit_largest_test_case_size():
    # 1 <= T <= 10**5
    # 10 <= N <= 4 * 10 ** 16
    test_numbers = [(4 * 10 ** 16,)] * (10 ** 5)
    assert_time_limit_multitest(10, fibonacci_even_numbers, *test_numbers)
