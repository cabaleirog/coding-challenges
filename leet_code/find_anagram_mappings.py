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

We should return

    [1, 4, 3, 2, 0]

as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because
the 1st element of A appears at B[4], and so on.

Note:
    A, B have equal lengths in range [1, 100]
    A[i], B[i] are integers in range [0, 10^5]
"""

def get_mapping(array_one, array_two):
    mapping = []
    aux_array_two = array_two[:]
    for value in array_one:
        for idx, other in enumerate(aux_array_two):
            if value == other:
                mapping.append(idx)
                aux_array_two[idx] = None
                break
    return mapping


if __name__ == '__main__':  # pragma: no cover
    arrays = [12, 28, 46, 32, 50], [50, 12, 32, 46, 28]
    mapped = get_mapping(*arrays)
    assert [1, 4, 3, 2, 0] == mapped
    print('A:\t{0}\nB:\t{1}\nP:\t{2}'.format(*arrays, mapped))
