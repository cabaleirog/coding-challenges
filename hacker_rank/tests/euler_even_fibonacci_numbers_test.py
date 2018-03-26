from hacker_rank.euler_even_fibonacci_numbers import (
    fibonacci,
    fibonacci_even_numbers)


def test_fibonacci_numbers():
    fib = fibonacci()
    numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert [next(fib) for _ in range(len(numbers))] == numbers


def test_sum_of_even_fibonacci_numbers():
    assert fibonacci_even_numbers(0) == 0
    assert fibonacci_even_numbers(2) == 0
    assert fibonacci_even_numbers(10) == 10
    assert fibonacci_even_numbers(100) == 44
