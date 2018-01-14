"""1. Two Sum

https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], and target = 9,
because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""
def get_indices(array, target):
    """Get the indices of the elements which add up to target.

    Args:
        array (`list` of `int`): The list of numbers
        target (`int`): The target number

    Example:
        >>> get_indices([2, 7, 11, 15], 9)
        [0, 1]

    Note:
        %timeit: 12.1 µs ± 89.4 ns per loop
    """
    complements = {}
    for idx, value in enumerate(array):
        if value in complements:
            return [complements[value], idx]
        complements[target - value] = idx
    return None


if __name__ == '__main__':  # pragma: no cover
    assert [0, 1] == get_indices([2, 7, 11, 15], 9)
    print(get_indices([2, 7, 11, 15], 9))
