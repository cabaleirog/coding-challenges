from codeforces.aramic_script import count_objects


def test_sample_testcases():
    assert count_objects(['a', 'aa', 'aaa', 'ab', 'abb']) == 2
    assert count_objects(['amer', 'arem', 'mrea']) == 1


def test_single_character():
    script = 'a a a a a a a a a a a a a a a a a'
    assert count_objects(script.split()) == 1


def test_three_characters():
    script = 'bda bbb cda dca dda dcb bcd dcb ada ddd'
    assert count_objects(script.split()) == 6
