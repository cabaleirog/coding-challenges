from hacker_rank.validating_postalcode import alt_rep_digits, validate


def test_without_alternating_repetitive_digits():
    assert alt_rep_digits('125125') == 0
    assert alt_rep_digits('234225') == 0
    assert alt_rep_digits('012345') == 0


def test_with_alternating_repetitive_digits():
    assert alt_rep_digits('100000') == 3
    assert alt_rep_digits('111111') == 4
    assert alt_rep_digits('112222') == 2
    assert alt_rep_digits('121756') == 1


def test_numeric_only_postal_codes():
    assert validate('abcdef') is False
    assert validate('123a56') is False
    assert validate('123456') is True


def test_valid_postal_codes():
    assert validate('123456') is True
    assert validate('113456') is True
    assert validate('123466') is True


def test_invalid_postal_codes():
    assert validate('000000') is False
    assert validate('100000') is False
    assert validate('111416') is False
    assert validate('999999') is False


def test_invalid_postal_codes_range():
    assert validate('123') is False
    assert validate('000045') is False
    assert validate('123456789') is False


def test_postal_codes_numeric_input():
    assert validate(123456) is True
    assert validate(100000) is False
