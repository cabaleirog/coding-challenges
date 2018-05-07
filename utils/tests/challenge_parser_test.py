from utils.new_challenge import Parser, HackerRank, Codeforces


def test_codeforces_challenge_detailsA():
    URL = 'http://codeforces.com/contest/935/problem/n'
    details = Codeforces().get_problem(URL)
    assert details.url == URL
    assert 'Fafa and his Company' in details.name
    assert 'brute force' in details.tags
    assert len(details.sample_tests) == 2


def test_codeforces_challenge_detailsB():
    URL = 'http://codeforces.com/contest/935/problem/B'
    details = Codeforces().get_problem(URL)
    assert details.url == URL
    assert 'Fafa and the Gates' in details.name
    assert 'implementation' in details.tags
    assert len(details.sample_tests) == 3
