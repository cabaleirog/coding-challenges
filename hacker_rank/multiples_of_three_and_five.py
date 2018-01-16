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
from itertools import combinations

def get_summation(upper_bound, factors):
    """Return the sum of all values divisables by a given set of values.

    The summation of k from 1 to n is equal to

        n * (n + 1) / 2

    Thus, the sum of all multiples of X will be X times the summation.

    Notes:
        We have to account for duplicates and remove those extra values
        Right shift has been used to avoid rounding issues on large numbers
    """
    upper_bound = int(upper_bound)  # Just in case the input is a float
    total = 0

    # Get the total sum for each factor
    for factor in factors:
        n = (upper_bound - 1) // factor
        total += factor * n * (n + 1) >> 1 # Right shift 1 (Divided by 2)

    # Subtract the sum for the overlapping values
    # TODO: Only works for the case of 2 factors. Implement a generic approach
    for pair in combinations(factors, 2):
        factor = pair[0] * pair[1]
        n = (upper_bound - 1) // factor
        total -= factor * n * (n + 1) >> 1 # Right shift 1

    return total


# Below implementation is just for fun (Not using math to solve the problem)
# This implementation works well for numbers below 10^6
def get_sum(upper_bound, values, chunks=1):
    """Return the sum of all values divisables by a given set of values.

    Args:
        upper_bound (int): Number which is **above** all values to sum
        values (list of int): List of the factors to use

    Returns:
        int: Sum of all values
    """
    last_divisible = highest_multiple(upper_bound, values)
    chunk_size = int(upper_bound / chunks)

    total = 0
    for value in multiples(values, last_divisible, chunk_size=chunk_size):
        total += value
    return total


def highest_multiple(upper_bound, values):
    """Return the last possible multiple below upper_bound for each factor

    Args:
        upper_bound (int): Number which is **above** all values to sum
        values (list of int): List of the factors to use

    Returns:
        dict: Mapping of factor and highest multiple
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
    return last_divisible


def multiples(factors_array, highest_multiples, lowest=1, chunk_size=None):
    """Provide the list of integers which are divisible by any of the factors.

    Args:
        factors_array (list of int): Numbers to divide by
        highest_multiples (dict): Highest multiple to yield for each factor

    Yields:
        int: Values which are divisible by factor
    """
    if chunk_size:
        lowest = max(highest_multiples.values()) - chunk_size

    i = 0
    yielded = {x: {} for x in factors_array}  # Values which have been yielded
    factors = sorted(factors_array, reverse=True)
    while factors:
        for factor in factors[:]:
            number = highest_multiples[factor] - factor * i
            if number < factor or number < lowest:
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
        if i % 100 == 0 and factors:
            cut_off = highest_multiples[min(factors)] - min(factors) * i
            # yielded will be cleaned completely for the smallest factor
            yielded[min(factors)] = {}
            for n in [x for x in yielded.keys() if x != min(factors)]:
                yielded[n] = {k: v for k, v in yielded[n].items() if v < cut_off}

    highest_multiples = highest_multiple(lowest, factors_array)
    if max(highest_multiples.values()) <= 1:
        return
    yield from multiples(factors_array, highest_multiples, chunk_size=chunk_size)


if __name__ == '__main__':
    assert get_summation(10, [3, 5]) == 23
    assert get_sum(10, [3, 5]) == 23

    upper, numbers = 10E5, [3, 5]
    # Using the math approach
    print('get_summation value for factors {} below {:.0f} is {:,.0f}'.format(
        numbers, upper, get_summation(upper, numbers)))
    # Using the recursive approach
    print('get_sum value for factors {} below {:.0f} is {:,.0f}'.format(
        numbers, upper, get_sum(upper, numbers, 20)))
