"""760. Find Anagram Mappings.

https://leetcode.com/contest/weekly-contest-66/problems/find-anagram-mappings/

Given two lists A and B, and B is an anagram of A. B is an anagram of A means B
is made by randomizing the order of the elements in A. We want to find an index
mapping P, from A to B. A mapping P[i] = j means the ith element in A appears
in B at index j. These lists A and B may contain duplicates. If there are
multiple answers, output any of them.

For example, given
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]

We should return [1, 4, 3, 2, 0] as P[0] = 1 because the 0th element of A
appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4],
and so on.

Note:
    A, B have equal lengths in range [1, 100]
    A[i], B[i] are integers in range [0, 10^5]

------
Notes about the solution:

Two implementations were created, `get_mapping_contest` was the one submitted
during the contest, but it wasnt very efficient. Thus after the contest
ended, a cleaner and faster implementation, `get_mapping` was created.

There is a small difference in the output among them, the order of the
indices for the duplicated values, however, the problem allows for that. In
order to match both outputs, when popping the value from the list in
`get_mapping`, we could do pop(0). Note that, pop(0) is O(k) vs O(1) for pop().
"""
from itertools import groupby


def get_mapping(a, b):
    """"Return an index mapping from the first list onto the second one.

    Args:
        a (List[int]): List of integers which numbers will be mapped.
        b (List[int]): Anagram of list `a`.

    Returns:
        List[int]: Map of indices of `b` for values on `a`.

    Example:
        >>> get_mapping([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
        [1, 4, 3, 2, 0]

    Explanation:
        - A tuple of (index, number) is created from list `b`
        - The list is sorted by the number value (Required by groupby method)
        - Create a dictionary mapping each number value to the tuple.
        - For each value of `a`, pop the first value in mapping, from the list
        of tuples; thus, the following duplicated number will pop the next
        available `index`.
    """
    indices = sorted(enumerate(b), key=lambda x: x[1])
    mapping = {k: list(g) for k, g in groupby(indices, lambda x: x[1])}
    return [mapping[n].pop()[0] for n in a]


def get_mapping_contest(a, b):
    """Return an index mapping from the first list to the second one.

    Iterates over every value in `a`, searching for the same value on `b`, once
    found, records the index where it was found and removes the value from `b`,
    so the next time it looks for the same value, it will skip that index. This
    implementation has lots of room for improvement.
    """
    mapping = []
    aux_b = b[:]
    for value in a:
        for idx, other in enumerate(aux_b):
            if value == other:
                mapping.append(idx)
                aux_b[idx] = None
                break
    return mapping


if __name__ == '__main__':  # pragma: no cover
    arrays = [12, 28, 46, 32, 50], [50, 12, 32, 46, 28]
    print(get_mapping(*arrays))
