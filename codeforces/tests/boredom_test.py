from utils.test_utils import assert_time_limit
from codeforces.boredom import solve


def test_sample_test_cases():
    assert solve([1, 2]) == 2
    assert solve([1, 2, 3]) == 4
    assert solve([1, 2, 1, 3, 2, 2, 2, 2, 3]) == 10


def test_smallest_sequence_size():
    assert solve([1]) == 1
    assert solve([7]) == 7


def test_time_limit():
    sequence = [x for x in range(1, 10 ** 5 + 1)]
    assert_time_limit(1.0, solve, sequence)
