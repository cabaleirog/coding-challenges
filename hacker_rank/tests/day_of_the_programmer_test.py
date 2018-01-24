from hacker_rank.day_of_the_programmer import (
    day_of_the_programmer,
    is_leap_year,
    which_calendary
)


def test_website_examples():
    assert day_of_the_programmer(2017) == '13.09.2017'
    assert day_of_the_programmer(2016) == '12.09.2016'

def test_gregorian_non_leap_year():
    assert is_leap_year(1700, False) is False
    assert is_leap_year(1800, False) is False
    assert is_leap_year(1900, False) is False
    assert is_leap_year(2017, False) is False

def test_gregorian_leap_year():
    assert is_leap_year(2000, False) is True
    assert is_leap_year(2016, False) is True
