from codeforces.aramic_script import solve


def test_sample_testcases():
    assert solve(['a', 'aa', 'aaa', 'ab', 'abb']) == 2
    assert solve(['amer', 'arem', 'mrea']) == 1


def test_single_character():
    script = 'a a a a a a a a a a a a a a a a a'
    assert solve(script.split()) == 1


def test_three_characters():
    script = 'bda bbb cda dca dda dcb bcd dcb ada ddd'
    assert solve(script.split()) == 6
