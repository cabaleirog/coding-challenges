# -*- coding: utf-8 -*-
"""Project Euler #201: Subsets with a unique sum.

https://www.hackerrank.com/contests/projecteuler/challenges/euler201/problem

For any set A of numbers, let sum(A) be the sum of the elements of A.

Consider the set B = {1,3,6,8,10,11}. There are 20 subsets of B containing
three elements, and their sums are:

    sum({1, 3, 6})       = 10
    sum({1, 3, 8})       = 12
    sum({1, 3, 10})      = 14
    sum({1, 3, 11})      = 15
    sum({1, 6, 8})       = 15
    sum({1, 6, 10})      = 17
    sum({1, 6, 11})      = 18
    sum({1, 8, 10})      = 19
    sum({1, 8, 11})      = 20
    sum({1, 10, 11})     = 22
    sum({3, 6, 8})       = 17
    sum({3, 6, 10})      = 19
    sum({3, 6, 11})      = 20
    sum({3, 8, 10})      = 21
    sum({3, 8, 11})      = 22
    sum({3, 10, 11})     = 24
    sum({6, 8, 10})      = 24
    sum({6, 8, 11})      = 25
    sum({6, 10, 11})     = 27
    sum({8, 10, 11})     = 29

Some of these sums occur more than once, others are unique. For a set A,
let U(A,k) be the set of unique sums of k-element subsets of A, in our
example we find U(B,3) = {10,12,14,18,21,25,27,29} and sum(U(B,3)) = 156.

Now consider the n-element set S = {s1,s2,...,sn}. S has nCm m-element
subsets. Determine the sum of all integers which are the sum of exactly
one of the m-element subsets of S, i.e. find sum(U(S,m)).
"""
from itertools import combinations


def preprocess_data(numbers, size):
    """Remove unnecessary duplicates.

    Args:
        numbers (list): The set of numbers
        size (int): Size of the subsets

    Returns:
        tuple: A subset of the numbers array, a list of the numbers which have
            duplicates, and a list with groups which should be included
    """
    if size <= 2:
        return numbers, [], []

    times = {}
    for value in numbers:
        if value in times:
            times[value] += 1
        else:
            times[value] = 1

    # Remove any duplicates with lenght equals to group size, but store the
    # the set of the element with the size of group size
    force_ignore = [x[0] for x in times.items() if x[1] == size]
    extra_groups = [size * (x,) for x in force_ignore]

    force_ignore.extend([x[0] for x in times.items() if x[1] > size])

    to_include = list(filter(lambda x: x[1] < size, times.items()))
    result = []
    for item in to_include:
        result.extend([item[0],] * item[1])

    for item in force_ignore:
        result.extend([item,] * 1)

    return result, force_ignore, extra_groups


def get_sum(numbers, size, reduce_array=True):
    """Return the sum of all unique sums of the subsets.

    Args:
        numbers (list): The set of numbers
        size (int): Size of the subsets
        reduce_array (bool): Should the array undergo preprocessing

    Returns:
        int: The sum of all unique sums

    Example:
        >>> get_sum({1, 3, 6, 8, 10, 11}, 3)
        156
    """
    if reduce_array:
        processed_numbers, ignored_numbers, extra = preprocess_data(numbers, size)
    else:
        processed_numbers, ignored_numbers, extra = numbers, [], []

    iterables = [combinations(processed_numbers, size), extra]
    sums, ignores = get_values(iterables, ignored_numbers)
    unique_sums = sums.difference(ignores)
    total_sum = sum(unique_sums)
    return total_sum


def get_values(iterables, force_ignores=[]):
    """Calculate the sum of each subset.

    Args:
        iterables (`list` of `list`): Each iterable containing subsets to add
        force_ignores (`list` of `int`): Each value on the list will cause all
            groups with them on it to be excluded automatically, with the
            exception of groups where all elements are in the exclude list.

    Returns:
        tuple: Two sets, one with the sums, the other with the duplicated ones
    """
    sums, ignores = set(), set()
    for iterable in iterables:
        for group in iterable:
            value = sum(group)
            if value in ignores:
                continue
            if value in sums:
                ignores.add(value)
                continue
            sums.add(value)
            # Force ignores
            for number in force_ignores:
                if number in group:
                    # Check if the group contains only numbers to exclude
                    for group_number in group:
                        # Ignore group if one number is not in the exclude list
                        if group_number not in force_ignores:
                            ignores.add(value)
                            break
    return sums, ignores


if __name__ == '__main__':  # pragma: no cover
    numbers, size = [1, 3, 6, 8, 10, 11], 3
    total = get_sum(numbers, size, True)
    assert total == 156
    print('Array: {}\nGroup Size: {}\nSum: {}'.format(numbers, size, total))
