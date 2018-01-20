from hacker_rank.booking import climbing_leaderboard, map_ranks


def test_rank():
    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 50, 120]
    rank = [6, 4, 2, 1]
    assert climbing_leaderboard(scores, alice) == rank

def test_map_ranls():
    assert map_ranks([30, 20, 20, 20, 15, 5, 5]) == {30: 1, 20: 2, 15: 3, 5: 4}
