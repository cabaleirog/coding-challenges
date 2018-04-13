from hacker_rank.sherlock_and_valid_string import valid_string


def test_website_samples():
    assert valid_string('aabbcc') is True   # valid already
    assert valid_string('baacdd') is False  # need to remove more than one char
    assert valid_string('aabbccc') is True  # remove one `c`
    assert valid_string('aabbc') is True    # remove one `c`
    assert valid_string('abcccc') is False  # need to remove three of `c`
    assert valid_string('aabbcd') is False  # need to remove more than one char


def test_single_character():
    assert valid_string('a') is True
    assert valid_string('aa') is True
    assert valid_string('aaaaaaaa') is True
