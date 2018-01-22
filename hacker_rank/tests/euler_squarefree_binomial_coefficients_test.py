import hacker_rank.euler_squarefree_binomial_coefficients as hr


def test_get_diagonals_including_edge_of_the_triangle():
    obj = hr.SquarefreeBinomialCoefficients(3)
    assert list(obj.get_diagonals(False)) == [[1], [1, 2], [1]]

def test_get_diagonals_excluding_edge_of_the_triangle():
    obj = hr.SquarefreeBinomialCoefficients(4)
    assert list(obj.get_diagonals(True)) == [[], [2], [3], []]

def test_sum_including_one_row():
    obj = hr.SquarefreeBinomialCoefficients(1)
    assert obj.squarefree_sum() == 1

def test_sum_including_two_rows():
    obj = hr.SquarefreeBinomialCoefficients(2)
    assert obj.squarefree_sum() == 1
def test_sum_including_three_rows():
    obj = hr.SquarefreeBinomialCoefficients(3)
    assert obj.squarefree_sum() == (1 + 2)

def test_sum_including_four_rows():
    obj = hr.SquarefreeBinomialCoefficients(4)
    assert obj.squarefree_sum() == (1 + 2 + 3)

def test_sum_including_five_rows():
    obj = hr.SquarefreeBinomialCoefficients(5)
    assert obj.squarefree_sum() == (1 + 2 + 3 + 6)

def test_sum_including_six_rows():
    obj = hr.SquarefreeBinomialCoefficients(6)
    assert obj.squarefree_sum() == (1 + 2 + 3 + 5 + 6 + 10)

def test_sum_including_seven_rows():
    obj = hr.SquarefreeBinomialCoefficients(7)
    assert obj.squarefree_sum() == (1 + 2 + 3 + 5 + 6 + 10 + 15)

def test_sum_including_eight_rows():
    obj = hr.SquarefreeBinomialCoefficients(8)
    assert obj.squarefree_sum() == (1 + 2 + 3 + 5 + 6 + 7 + 10 + 15 + 21 + 35)

def test_factorial_method():
    obj = hr.SquarefreeBinomialCoefficients(8)
    assert obj.factorial(0) == 1
    assert obj.factorial(1) == 1
    assert obj.factorial(2) == 2
    assert obj.factorial(10) == 3628800
    assert 10 in obj._factorials

def test_factorial_cache():
    obj = hr.SquarefreeBinomialCoefficients(8)
    obj.factorial(6)
    assert 2 in obj._factorials
    assert 3 in obj._factorials
    assert 6 in obj._factorials
