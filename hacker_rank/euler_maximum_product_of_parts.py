"""Project Euler #183: Maximum product of parts.

https://www.hackerrank.com/contests/projecteuler/challenges/euler183

- Difficulty: Easy

Let N be a positive integer and let N be split into k equal parts, r = N/k, so
that N = r + r + ... + r.

Let P be the product of these parts, P = r × r × ... × r = r^k. For example,
if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then
P = 2.2^5 = 51.53632.

Let M(N) = Pmax for a given value of N. It turns out that the maximum for
N = 11 is found by splitting eleven into four equal parts which leads to
Pmax = (11/4)^4; that is, M(11) = 14641/256 = 57.19140625, which is a
terminating decimal. However, for N = 8 the maximum is achieved by splitting it
into three equal parts, so M(8) = 512/27, which is a non-terminating decimal.

Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a
terminating decimal.

For example, Sum(D(N)) for 5 ≤ N ≤ 100 is 2438.

Find Sum(D(N)) for 5 ≤ N ≤ n.


About the implementation:
=========================

The mathematical portion of the challenge involves finding the first
derivative of P with respect to k; which give us a simple formula to
calculate Pmax.

    f(k) = (n / k) ^ k
    f'(k) = (ln(n / k) - 1) * (n / k) ^ k
    root: k = n / e

Afterwards, Hacker Rank will request, for a single test-case, up to 10^5
queries (total sum until N), where N can go up to 10^6; thus, the chosen
approach will be to precompute all possible values.

Steps taken to precompute:

1. Create an array with the values of k up to the highest N amongst all queries
2. Map k to its value after completly dividing it by 2's and 5's.
3. Compute the cumulative value of Sum(D(N)) for every possible N.

After completing those steps, we are able to return the result for each query
in constant time.
"""
import math


def precompute(largest_number):
    """Precompute the values of Sum(D(N)) until a certain value of N.

    Args:
        largest_number (int): number until which we will precompute.

    Returns:
        List[int]: values of Sum(D(N)) where N is represented by the index.
    """
    optimal_splits = [round(n / math.e) for n in range(largest_number + 1)]

    ex_factors = {k: number_ex_factors(k, [2, 5]) for k in set(optimal_splits)}

    cumulative_values = [0] * (largest_number + 1)
    for n in range(5, largest_number + 1):
        d_of_n = n if (n % ex_factors[optimal_splits[n]] != 0) else -n
        cumulative_values[n] = d_of_n + cumulative_values[n - 1]

    return cumulative_values


def number_ex_factors(number, factors):
    """Divide a number until its no longer evenly divisible by the factors.

    In other words, if a number is factorized, this will remove any factor in
    the given list, and return the multiplication of the remainig factors.

    Args:
        number (int): the number from which the factors will be removed.
        factors (List[int]): list of factors to remove.

    Returns:
        int: the number after removing all the given factors.

    Examples:
        >>> number_ex_factors(20, [2])
        5
        >>> number_ex_factors(2 * 2 * 2 * 5, [2, 5])
        1
    """
    for factor in sorted(set(factors)):
        while number > 1 and number % factor == 0:
            number //= factor
    return number


if __name__ == '__main__':
    queries = [int(input().strip()) for _ in range(int(input().strip()))]

    # max(queries) will give us the largest number to precompute.
    cumulative_values = precompute(max(queries))

    for upper_bound in queries:
        print(cumulative_values[upper_bound])
