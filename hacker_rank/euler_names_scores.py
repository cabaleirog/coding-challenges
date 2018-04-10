"""Project Euler #22: Names scores.

https://www.hackerrank.com/contests/projecteuler/challenges/euler022

- Difficulty: Easy

You are given around five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list in sample is sorted into alphabetical order, PAMELA,
which is worth 16 + 1 + 13 + 5 + 12 + 1 = 48, is the 5th name in the list. So,
PAMELA would obtain a score of 5 * 48 = 240.

You are given Q queries, each query is a name, you have to print the score.
"""


def score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)


if __name__ == '__main__':
    arr = sorted(input().strip() for _ in range(int(input().strip())))
    mapping = {name: [i, score(name)] for i, name in enumerate(arr)}

    for _ in range(int(input().strip())):
        i, value = mapping[input().strip()]
        print((i + 1) * value)
