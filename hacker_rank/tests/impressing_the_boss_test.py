from hacker_rank.impressing_the_boss import can_modify


def test_site_examples():
    assert can_modify([5, 7, 7, 11, 15, 12, 22, 24]) is True
    assert can_modify([20, 19, 18, 16, 14, 15, 14, 13, 11]) is False


def test_impressed_after_increasing_or_decreasing_one():
    assert can_modify([1, 0, 1, 1, 1, 1]) is True
    assert can_modify([2, 0, 2, 3, 4, 5, 6]) is True
    assert can_modify([1, 0, 0, 1]) is True


def test_already_impressed():
    assert can_modify([1, 1, 1, 1, 1, 1, 1, 1]) is True
    assert can_modify([1, 2, 4, 5, 6]) is True


def test_unable_to_impress_the_boss():
    assert can_modify([4, 2, 6, 4]) is False
    assert can_modify([2, 6, 5, 8, 7]) is False
    assert can_modify([4, 5, 2, 2, 1]) is False
    assert can_modify([4, 4, 3, 3, 3]) is False
