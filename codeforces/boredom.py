"""Codeforces Round #260 (Div. 1) - Boredom.

http://codeforces.com/problemset/problem/455/A

Alex doesn't like boredom. That's why whenever he gets bored, he comes up with
games. One long winter evening he came up with a game and decided to play it.

Given a sequence a consisting of n integers. The player can make several
steps. In a single step he can choose an element of the sequence (let's denote
it a[k]) and delete it, at that all elements equal to a[k] + 1 and a[k] - 1
also must be deleted from the sequence. That step brings a[k] points to the
player. Alex is a perfectionist, so he decided to get as many points as
possible. Help him.

The first line contains integer n (1 <= n <= 10^5) that shows how many numbers
are in Alex's sequence.

The second line contains n integers a1, a2, ..., an (1 <= ai <= 10^5).

Print a single integer - the maximum number of points that Alex can earn.

"""
import collections


def solve(sequence):
    max_n = max(sequence)

    d = collections.defaultdict(int)
    for n in sequence:
        d[n] += 1

    # dp[i][0] => not removing the i-th number, while dp[i][1] => removing it.
    dp = [[0, 0] for _ in range(max_n + 1)]
    dp[0][0] = dp[0][1] = 0

    for i in range(1, max_n + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = i * d[i] + dp[i - 1][0]

    return max(dp[max_n][0], dp[max_n][1])


def main():
    _ = input()
    sequence = [int(x) for x in input().strip().split()]
    result = solve(sequence)
    print(result)


if __name__ == '__main__':
    main()
