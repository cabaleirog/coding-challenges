"""Project Euler #5: Smallest multiple.

https://www.hackerrank.com/contests/projecteuler/challenges/euler005

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (divisible with
no remainder) by all of the numbers from 1 to N?

**Explanation**

    You can check 2520 is divisible by each of {1,2,3,4,5,6,7,8,9,10}
    giving quotient of {2520,1260,840,630,504,420,360,315,280,252} respectively

"""
from operator import mul
from itertools import accumulate


def smallest_multiple(number):
    """Return the smallest multiple which is divisible by 1 to ``number```.

    Args:
        number (int): Last number of the set {1, 2, ..., ``number``}

    Returns:
        int: Smallest multiple divisible by each number from 1 to ``number``

    Examples:
        >>> smallest_multiple(3)
        6
        >>> smallest_multiple(10)
        2520

    """
    numbers = [x for x in range(2, number + 1)]
    primes = get_prime_numbers(number)

    # Map each factor and how many times it should be used (e.g. 3^5 -> {3: 5})
    # This will only contain primes, as any other number can be factorized
    factors_map = {}

    # Every prime number will be at least once as a factor
    for i in numbers[:]:
        if i in primes:
            factors_map[i] = 1
            numbers.remove(i)

    # For each non-prime nunber, check if its factors are already in the array
    for non_prime in numbers[:]:
        # Get the factors (as a list of primes)
        factors = factorize(non_prime, primes)

        # Update factors count (e.g. 2x2x3x5: 2,3 once each already, add 2, 5)
        for j in set(factors):
            if factors.count(j) > factors_map[j]:
                factors_map[j] = factors.count(j)

    return list(accumulate([v ** t for v, t in factors_map.items()], mul))[-1]


def get_prime_numbers(upper_bound):
    """Return all prime numbers until upper_bound.

    Args:
        upper_bound (int): Largest number to check

    Returns:
        set: The prime numbers from 2 to upper_bound

    Example:
        >>> get_prime_numbers(10)
        {2, 3, 5, 7}

    """
    primes = set()
    for number in range(2, upper_bound + 1):
        if is_prime(number):
            primes.add(number)
    return primes


def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for j in range(2, number - 1):
        if number % j == 0:
            return False
    return True


def factorize(number, prime_numbers):
    """Divide a number into its prime factors.

    Args:
        number (int): The number to factorize
        prime_numbers (list): A list with primes (at least until ``number``)

    Returns:
        list: A list of prime numbers, these primes can be more than once

    Examples:
        >>> factorize(15, [2, 3, 5, 7, 11, 13])
        [3, 5]
        >>> factorize(16, set([2, 3, 5, 7, 11, 13]))
        [2, 2, 2, 2]

    """
    if list(prime_numbers) == []:
        raise ValueError('prime_numbers can not be empty')
    i = 0
    factors = []
    primes = sorted(prime_numbers)
    while number > 1:
        if (number / primes[i]) == (number // primes[i]):
            factors.append(primes[i])
            number = number / primes[i]
            continue  # Check if it can be divided further by the same prime
        i += 1
    return factors


if __name__ == '__main__':
    assert smallest_multiple(10) == 2520
    print('{} is the smallest multiple divisible by numbers 1 to {}'.format(
        smallest_multiple(15), 15))

