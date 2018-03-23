"""Rank of all elements in an array.

https://www.geeksforgeeks.org/rank-elements-array/


Given an array of N integers with duplicates allowed. All elements are ranked
from 1 to N if they are distinct. If there are say x repeated elements of a
particular value then each element should be assigned a rank equal to the
arithmetic mean of x consecutive ranks.

Example:
    Input:  10, 12, 15, 12, 10, 25, 12
    Output: 1.5, 4.0, 6.0, 4.0, 1.5, 7.0, 4.0

10 is the smallest and there are two 10s so take the average of two consecutive
ranks 1 and 2 i.e. 1.5; Next smallest element is 12. Since, two elements are
already ranked, the next rank that can be given is 3; however, there are three
12's so the rank of 2 is (3+4+5) / 3 = 4. Next smallest element is 15, there is
only one 15, so 15 gets a rank of 6 since 5 elements are ranked. Next element
is 25 and it gets a rank of 7.
"""
from collections import defaultdict


def rank(array):
    """Rank the elements in an array.

    Args:
        array (List[int]): The numbers to rank.

    Returns:
        List[float]: Rank of each element in `array`.

    Examples:
        >>> get_ranks([20, 30, 10])
        [2.0, 3.0, 1.0]
        >>> get_ranks([10, 12, 15, 12, 10, 25, 12])
        [1.5, 4.0, 6.0, 4.0, 1.5, 7.0, 4.0]
    """
    numbers = sorted(set(array))

    count = defaultdict(int)
    for num in array:
        count[num] += 1

    ranking = {}
    acc = 0
    for num in numbers:
        ranking[num] = acc + 0.5 * (count[num] + 1)
        acc += count[num]

    return [ranking[num] for num in array]


if __name__ == '__main__':
    numbers = [1, 2, 5, 2, 1, 60, 3]
    print(rank(numbers))
