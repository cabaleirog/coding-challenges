"""Codeforces Round #481 (Div. 3) - Mentors.

http://codeforces.com/contest/978/problem/F

In BerSoft `n` programmers work, the programmer `i` is characterized by a
skill `r[i]`.

A programmer `a` can be a mentor of a programmer `b` if and only if the skill
of the programmer `a` is strictly greater than the skill of the programmer `b`
`(r[a] > r[b])` and programmers `a` and `b` are not in a quarrel.

You are given the skills of each programmers and a list of `k` pairs of the
programmers, which are in a quarrel (pairs are unordered). For each programmer
`i`, find the number of programmers, for which the programmer `i` can be a
mentor.

"""
from collections import defaultdict


def solve(skills, quarrels):
    ans = [0] * len(skills)

    skills_mapping = defaultdict(list)
    for i, skill in enumerate(skills):
        skills_mapping[skill].append(i)

    quarrels_mapping = defaultdict(int)
    for i, j in quarrels:
        if skills[i - 1] == skills[j - 1]:
            continue
        elif skills[i - 1] < skills[j - 1]:
            i, j = j, i
        quarrels_mapping[i - 1] += 1

    tmp = len(skills)
    for skill in sorted(set(skills), reverse=True):
        group_size = len(skills_mapping[skill])
        for i in skills_mapping[skill]:
            ans[i] = max(0, tmp - quarrels_mapping[i] - group_size)
        tmp -= group_size

    return ans


def main():
    _, k = map(int, input().strip().split())
    skills = [int(x) for x in input().strip().split()]
    quarrels = [[int(x) for x in input().strip().split()] for _ in range(k)]
    result = solve(skills, quarrels)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
