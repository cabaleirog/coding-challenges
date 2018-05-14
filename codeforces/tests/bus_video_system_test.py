from random import randint

from utils.test_utils import assert_time_limit
from codeforces.bus_video_system import solve


def test_sample_test_cases():
    assert solve(5, [2, 1, -3]) == 3
    assert solve(4, [-1, 1]) == 4
    assert solve(10, [2, 4, 1, 2]) == 2


def test_initially_empty():
    assert solve(1, [1]) == 1
    assert solve(2, [2]) == 1
    assert solve(5, [5, -5, 5]) == 1


def test_initially_full():
    assert solve(1, [-1]) == 1
    assert solve(5, [-5, 5, -5]) == 1


def test_no_changes():
    assert solve(2, [0, 0, 0, 0]) == 3


def test_invalid_records():
    assert solve(1, [-5]) == 0
    assert solve(1, [5]) == 0


def test_others():
    assert solve(5, [-1, -1, -1]) == 3  # 3, 4 or 5
    assert solve(5, [-1, 3, -1]) == 3  # 1, 2 or 3
    assert solve(5, [-1, 1, -1, 1, -1]) == 5  # 1, 2, 3, 4 or 5


# Time limit: 1 second.
def test_time_limit():
    n, capacity = 1000, 10 ** 9
    sequence = [10 ** 3, -10 ** 3, 10 ** 6, -10 ** 6] * (n // 4)
    assert_time_limit(1, solve, capacity, sequence)
