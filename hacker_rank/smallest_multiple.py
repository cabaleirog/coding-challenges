"""Project Euler #5: Smallest multiple.

https://www.hackerrank.com/contests/projecteuler/challenges/euler005

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (divisible with
no remainder) by all of the numbers from 1 to N?

**Input Format**

    First line contains T that denotes the number of test cases. This is
    followed by T lines, each containing an integer, N.

**Constraints**

    1 <= T <= 10
    1 <= N <= 40

**Output Format**

    Print the required answer for each test case.

**Sample Input**

    2
    3
    10

**Sample Output**

    6
    2520

**Explanation**

    You can check 6 is divisible by each of {1,2,3}, giving quotient of
    {6,3,2} respectively.

    You can check 2520 is divisible by each of {1,2,3,4,5,6,7,8,9,10}
    giving quotient of 2520,1260,840,630,504,420,360,315,280,252} respectively.
"""

def smallest_multiple(number):
    """Return the smallest multiple divisible from 1 to ``number```.

    Args:
        number (int): Last number of the set {1, 2, ..., ``number``}

    Returns:
        int: Smallest multiple divisible by each number from 1 to ``number``

    Examples:
        >> smallest_multiple(3)
        6
        >> smallest_multiple(10)
        2520
    """
    return _first_implementation(number)


def _first_implementation(number):
    # Unoptimized implementation just to get a visual of the problem and the results
    aux = number
    while True:
        is_divisible = True
        for i in range(2, number + 1):
            if aux % i != 0:
                is_divisible = False
                break
        if is_divisible:
            break
        aux += 1
    return aux


if __name__ == '__main__':
    assert smallest_multiple(10) == 2520
    n = 15
    print('{} is the smallest multiple divisible by numbers 1 to {}'.format(
        smallest_multiple(n), n))
