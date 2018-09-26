"""Impressing the Boss.

https://www.hackerrank.com/contests/hourrank-27/challenges/impressing-the-boss

- Difficulty: Easy

Given the consecutive years' sales data of a company as an array of integers:
a = [a0, a1, ..., an-1], with ai denoting the total sales during the ith year,
your current task is to present the annual sales graph.

Your boss would be most impressed if the sales graph showed that the total
sales never decreased for every pair of consecutive years. For this, you are
allowed to modify at most one element of the data array for the property to
be true. (Any more and the change will be too obvious.)

Given a, determine if it is possible to do this task.

Complete the function can_modify which takes in the integer array a and returns
the string YES or NO denoting whether it is possible to do the task.

"""


def can_modify(a, c=0):
    if c > 1:
        return False
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a0, a1 = a[:], a[:]  # Copy of original array
            a0[i] = a[i+1]  # Decrease first one
            a1[i+1] = a[i]  # Increase second one
            return can_modify(a0, c + 1) or can_modify(a1, c + 1)
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().strip().split()))[:n]
        print('YES' if can_modify(arr) else 'NO')
