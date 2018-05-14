from random import randint

from utils.test_utils import assert_time_limit
from topcoder.line_off import solve


def test_website_examples():
    assert solve('abba') == 2
    assert solve('zwwwzffw') == 2
    assert solve('rrrrrrr') == 3
    assert solve('dfghj') == 0
    assert solve('wasitacarooracatisaw') == 10


def test_time_limit_on_max_length_random_input():
    colors = [chr(ord('a') + randint(0, 25)) for _ in range(50)]
    assert_time_limit(2, solve, colors)  # time limit (s): 2.000
