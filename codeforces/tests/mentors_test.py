from codeforces.mentors import solve


def test_sample_test_case_one():
    assert solve([10, 4, 10, 15], [(1, 2), (4, 3)]) == [0, 0, 1, 2]


def test_sample_test_case_two():
    skills = [5, 4, 1, 5, 4, 3, 7, 1, 2, 5]
    quarrels = [[4, 6], [2, 1], [10, 8], [3, 5]]
    assert solve(skills, quarrels) == [5, 4, 0, 5, 3, 3, 9, 0, 2, 5]
