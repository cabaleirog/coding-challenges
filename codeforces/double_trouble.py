"""Double Trouble.

Yandex.Algorithm 2018, third qualification round. April 8th, 2018.

http://codeforces.com/gym/101773/problem/B


Ruslan recently bought a sequence of non-negative integers a1, a2, ..., an. He
is a positive person, that is why he likes non-decreasing sequences. He also
has an ultimate power of doubling an integer at some position by doing a single
finger snap. He may perform as many finger snaps as he wants, he may also
double the same integer many times.

He is curious what is the minimum number of finger snaps he has to do in order
to make sequence non-decreasing. Help him find this number or tell him that it
is impossible.

The first line of input contains the only integer n (1 <= n <= 100 000), the
length of the sequence.

The second line of input contains n integers a1, a2, ..., an (0 <= ai <= 10^6).

If it is impossible to obtain a non-decreasing sequence of numbers by applying
doubling operation, print -1.

Otherwise print the minimum number of finger snaps needed to obtain a
non-decreasing sequence of numbers.

"""
from math import log2, ceil


def solve(array):
    if len(array) <= 1 or len(set(array)) == 1:
        return 0

    non_zero = False
    for number in array:
        if number > 0:
            non_zero = True
        if non_zero and number == 0:
            return -1

    total = 0
    exponent = 0
    for i in range(len(array) - 1):
        if array[i] == 0:
            continue  # zeros at the start of the sequence
        exponent = max(0, ceil(exponent + log2(array[i] / array[i + 1])))
        total += exponent
    return total


def main():
    _ = int(input().strip())
    array = [int(x) for x in input().strip().split()]
    result = solve(array)
    print(result)


if __name__ == '__main__':
    main()
