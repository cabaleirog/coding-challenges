"""Problem 1:  Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def get_sum(upper):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, upper)))


if __name__ == '__main__':
    assert get_sum(10) == 23
    n = 1000
    print('Sum of multiples of 3 or 5 below {} is {:,}'.format(n, get_sum(n)))
