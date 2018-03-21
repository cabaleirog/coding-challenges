"""Project Euler #3: Largest prime factor.

https://www.hackerrank.com/contests/projecteuler/challenges/euler003

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
factor of the number N?

Constraints:
    1 <= T <= 10
    10 <= N <= 10^12
"""


def factorize(number):
    """Return the prime factors for a given number.

    Args:
        number (int): Target number to factorize

    Returns:
        list: List of the factors
    """
    factors = set()
    aux = number
    while aux != 1:
        if aux % 2 == 0:
            factors.add(2)
            aux = aux // 2
            continue
        for i in range(3, aux + 1, 2):  # FIXME: Maybe until sqrt?
            if aux / i == aux // i:
                factors.add(i)
                aux = aux // i
                break
    return sorted(factors)


if __name__ == '__main__':
    print('!!!!!!!!!!!!!')
    # target = 3 * 7 * 19 * 137 * 149
    # result = factorize(target)
    # print('Factors of {} are {}; the largest prime factor been {}'.format(
    #     target, result, result[-1]))
    print(factorize(int(10**12 + 1)))
