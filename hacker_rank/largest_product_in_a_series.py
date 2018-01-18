"""Project Euler #8: Largest product in a series.

https://www.hackerrank.com/contests/projecteuler/challenges/euler008

Find the greatest product of K consecutive digits in the N digit number.

"""
from operator import mul
from functools import reduce
from random import randint


def greatest_product(number, size):
    """Return the greatest product of consecutive digits in a number.

    Args:
        number (int): The given number
        size (int): The size of the group of consecutive digits

    Returns:
        int: Greatest product

    Examples:
        >>> greatest_product(3675356291, 5)
        3150
        >>> greatest_product(2709360626, 5)
        0

    """
    groups = get_reduced_array(number, size)
    greatest = max(map(lambda x: reduce(mul, x, 1), groups))
    return greatest


def get_reduced_array(number, size):
    """Reduce the number of possible groups to analyze.

    If group B is the next consecutive groups of `size` digits of a given
    number, the only difference among those 2 groups will be the first digit
    from group A, and the last digit in group B, every other digit will be
    on both groups, thus, the product of all those digits will be the same and
    can be discarded; furthermore, we will only compare the 2 remaining digits
    as shown by, 3XXXX > XXXX2 -> 3 > 2, thus, group A has a greatest product.

    Args:
        number (int): The given number
        size (int): The size of the group of consecutive digits

    Returns:
        list: Return a subset of the possible groups of consecutive numbers.

    Example:
        >>> get_reduced_array(2751351, 2)
        [[7, 5], [5, 1], [3, 5]]

    """
    numbers = [int(x) for x in str(number)]
    subgroups = []

    # Compare the first digit of a group against the last from the next group
    current_group = numbers[:size]  # Initialize with the first `size` digits
    for i in range(0, len(numbers) - size):
        if numbers[i + size] < numbers[i]:  # First group's product is greatest
            subgroups.append(current_group)
        current_group = numbers[i + 1:i + 1 + size]

    # Handle the case when the last group has the greatest product
    if len(subgroups) == 0:
        subgroups.append(current_group)

    return subgroups


if __name__ == '__main__':
    K = randint(1, 7)
    N = randint(K, 1000)
    given_number = int(''.join([str(randint(0, 9)) for x in range(N)]))
    print('Number: {0}'.format(given_number))
    print('Greatest product of {0} digits is {1}'.format(
        K, greatest_product(given_number, K)))
