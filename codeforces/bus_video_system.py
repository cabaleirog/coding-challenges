"""Codeforces Round #481 (Div. 3) - Bus Video System.

http://codeforces.com/contest/978/problem/E

The buses in Berland are equipped with a video surveillance system. The
system records information about changes in the number of passengers in a bus
after stops.

If `x` is the number of passengers in a bus just before the current bus
stop and `y` is the number of passengers in the bus just after current bus
stop, the system records the number y - x. So the system records show how
number of passengers changed.

The test run was made for single bus and `n` bus stops. Thus, the system
recorded the sequence of integers a[1], a[2], ..., a[n] (exactly one number
for each bus stop), where a[i] is the record for the bus stop `i`. The bus
stops are numbered from 1 to n in chronological order.

Determine the number of possible ways how many people could be in the bus
before the first bus stop, if the bus has a capacity equals to `w` (that
is, at any time in the bus there should be from 0 to w passengers inclusive).

"""


def solve(capacity, sequence):
    diff = 0
    lb, ub = float('inf'), -float('inf')
    for record in sequence:
        diff += record
        ub = max(ub, diff)
        lb = min(lb, diff)
    return max(0, capacity - max(0, ub) + min(0, lb) + 1)


def main():
    _, capacity = [int(x) for x in input().strip().split()]
    sequence = [int(x) for x in input().strip().split()]
    result = solve(capacity, sequence)
    print(result)


if __name__ == '__main__':
    main()
