"""Project Euler #3: Largest prime factor.

https://www.hackerrank.com/contests/projecteuler/challenges/euler003

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
factor of the number N?
"""


def factorize(number):
    """Return the prime factors for a given number.

    Args:
        number (int): number to factorize.

    Returns:
        List[int]: sorted prime factors.

    Examples:
        >>> factorize(20)
        [2, 5]
        >>> factorize(2 * 2 * 2 * 3 * 3 * 5 * 7)
        [2, 3, 5, 7]
    """
    factors = set()

    # divide `number` until it becomes odd
    if number > 1 and number % 2 == 0:
        factors.add(2)
        while number % 2 == 0:
            number //= 2

    # only check odd numbers now
    while number > 1:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                factors.add(i)
                number //= i
                break
        else:  # no-break
            factors.add(number)
            break  # we are done; the current value is a prime number

    return sorted(factors)


if __name__ == '__main__':
    target = int(input('Number:').strip())
    factors = factorize(target)
    msg = 'Prime factors of {0} are {1}; the largest been {2}.'
    print(msg.format(target, factors, factors[-1]))
