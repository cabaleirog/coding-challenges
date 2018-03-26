"""1. Two Sum.

https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], and target = 9,
because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""


def get_indices(array, target):
    """Find two numbers from `array` which add up to `target`.

    Args:
        array (List[int]): The list of numbers
        target (int): The target sum

    Example:
        >>> get_indices([2, 7, 11, 15], 9)
        [0, 1]
    """
    complements = {}
    for idx, value in enumerate(array):
        if value in complements:
            return [complements[value], idx]
        complements[target - value] = idx


if __name__ == '__main__':  # pragma: no cover
    print(get_indices([2, 7, 11, 15], 9))
