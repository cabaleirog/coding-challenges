"""Project Euler #2: Even Fibonacci numbers.

https://www.hackerrank.com/contests/projecteuler/challenges/euler002/

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
N, find the sum of the even-valued terms.

Examples:
    For N = 10, we have {2, 8}, sum is 10.
    For N = 100, we have {2, 8, 34}, sum is 44.

"""


def fibonacci():
    """A simple generator for the Fibonacci sequence.

    Yields:
        int: The next term in the fibonacci sequence, starting at 0.

    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_even_numbers(n):
    """Sum all even Fibonacci numbers whose values do not exceed `n`.

    Returns:
        int: Total sum of even terms.

    """
    total = 0
    for term in fibonacci():
        if term >= n:
            return total
        total += term * (term % 2 == 0)


if __name__ == '__main__':
    n = int(input('Number:').strip())
    result = fibonacci_even_numbers(n)
    print('Sum of even fibonacci numbers until {0} is {1:,}'.format(n, result))
