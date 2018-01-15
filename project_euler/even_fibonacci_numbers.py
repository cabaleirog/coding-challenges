"""Project Euler #2: Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
N, find the sum of the even-valued terms.

**Input Format**

First line contains T that denotes the number of test cases. This is followed
by T lines, each containing an integer, N.

**Constraints**

    1 <= T <= 10^5
    10 <= N <= 4E16

**Output Format**

    Print the required answer for each test case.

**Sample Input 0**

    2
    10
    100

**Sample Output 0**

    10
    44

**Explanation 0**

    For N = 10, we have {2, 8}, sum is 10.
    For N = 100, we have {2, 8, 34}, sum is 44.
"""
def fibonacci_even_numbers(upper_bound):
    total, a, b = 0, 1, 2
    while True:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
        if a > upper_bound:
            break
    return total


if __name__ == '__main__':
    print('Sum of even numbers: {0:,}'.format(fibonacci_even_numbers(4.0E6)))
