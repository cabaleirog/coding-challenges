"""Project Euler #4: Largest palindrome product.

https://www.hackerrank.com/contests/projecteuler/challenges/euler004

A palindromic number reads the same both ways. The smallest 6 digit palindrome
made from the product of two 3-digit numbers is 101101 = 143 * 707.

Find the largest palindrome made from the product of two 3-digit numbers which
is less than N.

Constraints:

    1 <= T <= 100
    101101 < N < 1000000

Example:


# """

import itertools

def largest_palindrome_product(upper):
    for number in rename_this(upper):
        factors = factorize(number)

        c1 = []
        # fact = [x for x in map(lambda y: len(str(y)), factors) if x == 3]
        # if len(fact) < 2:
        #     continue
        for group in itertools.combinations(factors, 2):  # TODO > 2???
            multiple = group[0] * group[1]  # TODO > 2???
        for j in factors:
            
            if len(str(multiple)) == 3:
                c1.append(multiple)
        
        if len(c1) < 2:
            continue
        
        return c1[0] * c1[1]

        print(factors)
    # 250000
    # XX99XX
    # 249999
    # 24--99
    # for i in range(9, 0, -1):

    # Recursively check 159951 -> 158851 > ----
    # Factorize
    # Check if any combination of factors gives 2 3-digit numbers
    # If so, return tuple of digits
    # Return Palindrome

def rename_this(number):
    aux = number - 1
    while True:
        for i in range(9, 0, -1):
            s = str(aux)
            yield int('{0}{1}{2}{2}{1}{0}'.format(s[0], s[1], i))
        break  # TODO: Get one level below


def factorize(number):
    """Return the prime factors for a given number.

    Args:
        number (int): Target number to factorize

    Returns:
        list: List of factors
    """
    factors = list()
    aux = number
    while True:
        if aux == 1:
            break
        if aux % 2 == 0:
            factors.append(2)
            aux = aux // 2
            continue
        for i in range(3, aux + 1, 2):
            if (aux / i) == (aux // i):
                factors.append(i)
                aux = aux // i
                break
    return factors


def combine(factors):
    pass


print(largest_palindrome_product(800000))


# if __name__ == '__main__':
#     assert find_palindrome(101110) == 101101
#     assert find_palindrome(800000) == 793397
#     n = 500000
#     print('{} {}'.format(n, find_palindrome(n)))
