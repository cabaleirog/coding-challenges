"""Climbing the Leaderboard.

Alice is playing an arcade game and wants to climb to the top of the
leaderboard. Can you help her track her ranking as she beats each level? The
game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.

    Players who have equal scores receive the same ranking number, and the next
    player(s) receive the immediately following ranking number.

For example, four players have the scores 100, 90, 90, and 80. Those players
will have ranks 1, 2, 2, and 3, respectively.

When Alice starts playing, there are already `n` people on the leaderboard. The
score of each player `i` is denoted by `s_i`. Alice plays for `m` levels, and
we denote her total score after passing each level `j` as `alice_j`. After
completing each level, Alice wants to know her current rank.

You are given an array, `scores`, of monotonically decreasing leaderboard
scores, and another array, `alice`, of Alice's cumulative scores for each level
of the game. You must print `m` integers. The `j_th` integer should indicate
the current rank of alice after passing the `j_th` level.

For further details see the challenge's page:

    https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

"""
from bisect import bisect_right


def climbing_leaderboard(scores, alice):
    """Calculate Alice's ranking after playing each level on the game.

    Args:
        scores (List[int]): The score of other players on the leaderboard
        alice (List[int]): The score of Alice after passing each level

    Yields:
        int: Rank of Alice after playing each level

    Example:
        >>> list(climbing_leaderboard([20, 10, 10, 5], [5, 10, 15]))
        [3, 2, 2]
    """
    scores = sorted(set(scores))
    idx = 0
    for alice_score in alice:
        idx = bisect_right(scores, alice_score, idx)
        yield len(scores) - idx + 1


if __name__ == '__main__':
    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 50, 120]
    for current_rank in climbing_leaderboard(scores, alice):
        print(current_rank)
