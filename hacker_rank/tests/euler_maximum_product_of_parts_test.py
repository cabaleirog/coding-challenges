import pytest

from hacker_rank.euler_maximum_product_of_parts import (
    number_ex_factors,
    precompute)


@pytest.fixture()
def precomputed_data():
    return precompute(100)  # precomputes until N equal to 100


def test_website_sample(precomputed_data):
    assert precomputed_data[100] == 2438  # Sum(D(N)) for 5 <= N <= 100


def test_precomputed_values(precomputed_data):
    # precompute(N) returns a list of length N + 1, where the value at
    # index i represents the cumulative sum until i. Note that the sum starts
    # from N equal to 5, thus every value from index 0 to 4 will always be 0.
    assert precomputed_data[5] == -5
    assert precomputed_data[6] == -11
    assert precomputed_data[7] == -4
    assert precomputed_data[8] == 4
    assert precomputed_data[9] == -5
    assert precomputed_data[10] == -15  # Sum(D(N)) for 5 <= N <= 10


def test_precomputed_values_before_five_should_be_zero(precomputed_data):
    assert precomputed_data[:5] == [0, 0, 0, 0, 0]


def test_number_ex_factors():
    assert number_ex_factors(2 * 5, [2]) == 5
    assert number_ex_factors(2 * 2 * 5, [2]) == 5
    assert number_ex_factors(2 * 2 * 5 * 5, [2]) == 25
    assert number_ex_factors(2 * 2 * 5, [5]) == 4
    assert number_ex_factors(2 * 2 * 5 * 5, [5]) == 4
    assert number_ex_factors(2 * 2 * 5 * 5, [2, 5]) == 1
    assert number_ex_factors(2 * 2 * 5 * 5, [2, 5]) == 1
    assert number_ex_factors(2 * 2 * 5 * 5, [20]) == 5
    assert number_ex_factors(0, [2, 5]) == 0
