"""Climbing the Leaderboard.

https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

"""

def climbing_leaderboard(scores, alice):
    alice_rank = []
    for score in alice:
        mapping = map_ranks(scores + [score,])
        alice_rank.append(mapping[score])
    return alice_rank

def map_ranks(scores):
    """Return mapping of points to rank"""
    mapping = {}
    i = 1
    for score in sorted(set(scores), reverse=True):
        mapping[score] = i
        i += 1
    return mapping


if __name__ == '__main__':
    # print(climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    import time
    from random import randint
    from itertools import accumulate
    s = (0, 10E9)  # Scores range
    a = (0, 10E9)  # Alice score range
    # n = (1, 200)  # People range
    # m = (1, 200)  # Levels range
    n = (1, 2E5)  # People range
    m = (1, 2E5)  # Levels range
    max_points_per_level = max(1, n[1] // s[1])
    print(m[1] * max_points_per_level)
    # largest_case
    scores = sorted([randint(1, max_points_per_level) for x in range(int(n[1]))], reverse=True)
    alice = list(accumulate([randint(1, 5) for x in range(int(m[1]))]))
    print(scores)
    print(alice)
    start = time.perf_counter()
    #rank = climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
    rank = climbing_leaderboard(scores, alice)
    print(rank)
    print(time.perf_counter() - start)
