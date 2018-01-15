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
        upper_bound (int): Number which is **above** all values to sum
        values (list of int): List of the factors to use

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

    total = 0
    for value in multiples(values, last_divisible):
        total += value
    return total


def multiples(factors_array, highest_multiples):
    """Provide the list of integers which are divisible by any of the factors.

    Args:
        factors_array (list of int): Numbers to divide by
        highest_multiples (dict): Highest multiple to yield for each factor

    Yields:
        int: Values which are divisible by factor
    """
    i = 0
    yielded = {x: {} for x in factors_array}  # Values which have been yielded
    factors = sorted(factors_array, reverse=True)
    while factors:
        for factor in factors[:]:
            number = highest_multiples[factor] - factor * i
            if number < factor:
                factors.remove(factor)
                continue
            # Check if we have already yielded a number
            found = False
            for j in factors_array:
                if j != factor and number in yielded[j]:
                    found = True
                    break
            if not found:
                yield number
                yielded[factor][number] = number
        i += 1
        # Clean already yielded
        if i % 100 == 0:
            cut_off = highest_multiples[min(factors)] - min(factors) * i
            # yielded will be cleaned completely for the smallest factor
            yielded[min(factors)] = {}
            for n in [x for x in yielded.keys() if x != min(factors)]:
                yielded[n] = {k: v for k, v in yielded[n].items() if v < cut_off}


if __name__ == '__main__':
    assert get_sum(10, [3, 5]) == 23
    upper, numbers = 1000, [3, 5]
    print('Sum of values divisible by {} below {} is {:,}'.format(
        ', '.join(map(str, numbers)), upper, get_sum(upper, numbers)))
