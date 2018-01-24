from hacker_rank.day_of_the_programmer import (
    day_of_the_programmer,
    is_leap_year
)


def test_website_examples():
    assert day_of_the_programmer(2017) == '13.09.2017'
    assert day_of_the_programmer(2016) == '12.09.2016'


def test_transition_year():
    assert day_of_the_programmer(1918) == '26.09.1918'


def test_pre_transition_year():
    assert day_of_the_programmer(1917) == '13.09.1917'


def test_post_transition_year():
    assert day_of_the_programmer(1919) == '13.09.1919'


def test_gregorian_non_leap_year():
    assert is_leap_year(1700, False) is False
    assert is_leap_year(1800, False) is False
    assert is_leap_year(1900, False) is False
    assert is_leap_year(2017, False) is False


def test_gregorian_leap_year():
    assert is_leap_year(2000, False) is True
    assert is_leap_year(2016, False) is True
