from utils.new_challenge import Parser, HackerRank, Codeforces


def test_codeforces_challenge_detailsA():
    URL = 'http://codeforces.com/contest/935/problem/A'
    details = Codeforces().parse(URL)
    assert details.url == URL
    assert 'Fafa and his Company' in details.name
    assert 'brute force' in details.tags
    assert len(details.sample_tests) == 2


def test_codeforces_challenge_detailsB():
    URL = 'http://codeforces.com/contest/935/problem/B'
    details = Codeforces().parse(URL)
    assert details.url == URL
    assert 'Fafa and the Gates' in details.name
    assert 'implementation' in details.tags
    assert len(details.sample_tests) == 3


def test_hackerrank():
    with open('utils/tests/hacker_rank_sample_source.html') as f:
        source = f.read()
    hr = HackerRank()
    # Override get_source method to avoid using selenium to get the code
    hr.get_source = lambda x: source
    details = hr.parse('https://www.hackerrank.com/')
    assert details.name == 'Construct the Array'
    assert details.difficulty == 'Medium'
    assert details.description[0].startswith('Your goal is to find')
    assert details.description[1].startswith('Specifically, we want')
