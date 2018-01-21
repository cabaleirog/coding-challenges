from leet_code.prime_number_of_set_bits_in_binary_representation import (
    count_numbers,
    to_binary,
    set_bits,
    is_prime
)

def test_site_sample():
    assert count_numbers(6, 10) == 4
    assert count_numbers(10, 15) == 5


def test_number_to_binary():
    assert to_binary(6) == '110'
    assert to_binary(10) == '1010'
    assert to_binary(15) == '1111'

def test_set_bits():
    assert set_bits(6) == 2
    assert set_bits(7) == 3
    assert set_bits(9) == 2
    assert set_bits(10) == 2
    assert set_bits(11) == 3
    assert set_bits(12) == 2
    assert set_bits(13) == 3
    assert set_bits(14) == 3
    assert set_bits(15) == 4

def test_is_prime():
    assert is_prime(1, {}) is False
    assert is_prime(2, {}) is True
    assert is_prime(3, {}) is True
    assert is_prime(4, {}) is False
    assert is_prime(5, {}) is True
    assert is_prime(6, {}) is False

def test_is_prime_with_cache():
    cache = {982451653: True}  # A large prime number
    assert is_prime(982451653, cache) is True
