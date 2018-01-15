"""Project Euler #1: Multiples of 3 and 5

https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

**Input Format**

	First line contains T that denotes the number of test cases. This is
    followed T lines, each containing an integer, N.

**Constraints**

	1 <= T <= 10^5
	1 <= N <= 10^9

**Output Format**

	For each test case, print an integer that denotes the sum of all the
    multiples of 3 or 5 below N.

**Sample Input 0**

    2
    10
    100

**Sample Output 0**

	23
    2318

**Explanation 0**

	For N = 10, if we list all the natural numbers below 10 that are multiples
    of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Similarly for N = 100, we get 2318.
"""
def get_sum(upper):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, upper)))


if __name__ == '__main__':
    assert get_sum(10) == 23
    n = 1000
    print('Sum of multiples of 3 or 5 below {} is {:,}'.format(n, get_sum(n)))
