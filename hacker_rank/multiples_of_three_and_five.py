"""Project Euler #1: Multiples of 3 and 5

https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

**Input Format**

	First line contains T that denotes the number of test cases. This is
    followed T lines, each containing an integer, N.

**Constraints**

	1 <= T <= 10^5
	1 <= N <= 10^9

**Output Format**

	For each test case, print an integer that denotes the sum of all the
    multiples of 3 or 5 below N.

**Sample Input**

    2
    10
    100

**Sample Output**

	23
    2318

**Explanation**

	For N = 10, if we list all the natural numbers below 10 that are multiples
    of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Similarly for N = 100, we get 2318.
"""
def get_sum(upper_bound, values):
    """Return the sum of all values divisables by a given set of values.

    Args:
        upper_bound (int): Number which is above all values to sum
        values (list of int): List of the divisors to use

    Returns:
        int: Sum of all values
    """
    last_divisible = {}
    # Get the last number below the upper bound for each value
    i = upper_bound - 1
    while True:
        for value in values:
            if i % value == 0 and value not in last_divisible:
                last_divisible[value] = i
        if len(last_divisible) == len(values):
            break
        i -= 1
    return sum(set(get_divisors(values, last_divisible)))


def get_divisors(divisors, last):
    """Return the list of values divisible by the divisor.

    Args:
        divisor (int): Number to divide for
        last (int): Last number of the sequence

    Yields:
        int: Values which are divisible by divisor
    """
    i = 0
    divisors = sorted(divisors, reverse=True)
    while divisors:
        for divisor in divisors[:]:
            number = last[divisor] - divisor * i
            if number < divisor:
                divisors.remove(divisor)
                continue
            yield number
        i += 1


if __name__ == '__main__':
    assert get_sum(10, [3, 5]) == 23
    upper, numbers = 1000, [3, 5]
    print('Sum of values divisible by {} below {} is {:,}'.format(
        ', '.join(map(str, numbers)), upper, get_sum(upper, numbers)))
