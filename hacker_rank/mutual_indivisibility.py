"""Mutual Indivisibility

https://www.hackerrank.com/contests/hourrank-24/challenges/mutual-indivisibility

- Difficulty: Medium

Jugnu has recently been appointed as the sports captain. The headmaster asked
her to form a team for an upcoming table tennis tournament, subject to a few
constraints.

Each student of the school is assigned an integer denoting his/her skill level.
The headmaster requests Jugnu to form an indivisible team of size x. The team
is indivisible if it satisfies the following conditions.

- To make the team strong, each member of the team must have a skill level in
the range [a, b].

- The size of the team must be x.

- Let g1 and g2 be the skill levels of any two distinct players in the team.
Then g1 should not divide g2. This is necessary to avoid clashes.

Can you help Jugnu form an indivisible team? Assume that for every g, Jugnu can
always find a student with skill level g.

"""


def indivisible_team(a, b, size):
    team = set()
    count = 0
    for i in range(b, a - 1, -1):
        if any(j in team for j in range(i, b + 1, i)):
            continue
        team.add(i)
        count += 1
        if count == size:
            return list(team)


if __name__ == '__main__':
    # The first line contains a single integer, the number of test cases.
    # Each test case consists of a single line containing three space-separated
    # integers a, b and x.
    for _ in range(int(input().strip())):
        a, b, x = map(int, input().strip().split())
        result = indivisible_team(a, b, x)
        print(' '.join(map(str, result)) if result else -1)
