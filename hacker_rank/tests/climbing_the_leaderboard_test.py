from hacker_rank.climbing_the_leaderboard import climbing_leaderboard


def test_ranks_first_after_playing():
    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 50, 120]
    rank = [6, 4, 2, 1]
    assert list(climbing_leaderboard(scores, alice)) == rank

def test_climbing_to_the_top_after_one_level():
    assert list(climbing_leaderboard([10, 5, 5, 5, 2], [15])) == [1]

def test_alice_doesnt_play():
    assert list(climbing_leaderboard([5, 5, 3], [])) == []
