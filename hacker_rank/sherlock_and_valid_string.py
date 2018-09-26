"""Sherlock and the Valid String.

https://www.hackerrank.com/challenges/sherlock-and-valid-string/

- Difficulty: Medium

Sherlock considers a string, s, to be valid if either of the following
conditions are satisfied:

- All characters in s have the same exact frequency (i.e. occur the same number
of times). For example, 'aabbcc' is valid, but 'baacdd' is not valid.

- Deleting exactly 1 character from s will result in all its characters having
the same frequency. For example, 'aabbccc' and 'aabbc' are valid because all
their letters will have the same frequency if we remove 1 occurrence of c, but
'abcccc' is not valid because we'd need to remove 3 characters.

Given s, can you determine if it's valid or not? If it's valid, print YES on a
new line; otherwise, print NO instead.

"""


def valid_string(s):
    frequency = [s.count(c) for c in set(s)]
    freq_set = set(frequency)

    # All characters have the same frequency
    if len(freq_set) == 1:
        return True

    # There are two distinct set of frequencies
    if len(freq_set) == 2:
        min_freq, max_freq = min(freq_set), max(freq_set)

        # Only needs to remove one char from the one with the highest frequency
        if frequency.count(max_freq) == 1 and (max_freq - min_freq) == 1:
            return True

        # Only needs to remove the char which has a frequency of one
        if frequency.count(min_freq) == 1:
            return True

    return False


if __name__ == '__main__':
    result = valid_string(input().strip())
    print('YES' if result else 'NO')
