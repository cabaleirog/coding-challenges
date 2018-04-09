"""Bus Routes.

https://leetcode.com/contest/weekly-contest-79/problems/bus-routes/

- Difficulty: Hard

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
repeats forever. For example if routes[0] = [1, 5, 7], this means that the
first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop
T. Travelling by buses only, what is the least number of buses we must take to
reach our destination? Return -1 if it is not possible.
"""
import sys

from collections import defaultdict, deque


def buses_to_destination(routes, start, end):
    """Find the least number of buses required to reach destination.

    Args:
        routes (List[List[int]]): list of bus routes.
        start (int): initial bus stop.
        end (int): final bus stop (destination).

    Returns:
        int: number of buses to destination.

    Example:
        >>> buses_to_destination([[1, 2], [2, 3, 4], [3, 5]], 1, 5)
        3
    """
    if start == end:
        return 0

    stop_to_bus = defaultdict(set)  # mapping of connecting buses on each stop.
    for bus, stops in enumerate(routes):
        for stop in stops:
            stop_to_bus[stop].add(bus)

    # Breadth First Search
    queue = deque([(start, 0)])  # Initialized with a tuple of start and count.
    visited = {start}

    while queue:
        v, count = queue.pop()
        adj = {stop for bus in stop_to_bus[v] for stop in routes[bus]}
        for u in adj - visited:
            if u == end:
                return count + 1
            visited.add(u)
            queue.appendleft((u, count + 1))

    return -1


if __name__ == '__main__':
    # Sample inputs: routes, start, end = [[1, 2, 7], [3, 6, 7]], 1, 6
    try:
        routes = eval(input('Bus routes (List of list of stops): ').strip())
        start = int(input('Initial bus stop: ').strip())
        end = int(input('Final bus stop: ').strip())
    except Exception as e:
        print('Error while reading inputs (Exception: {})'.format(e))
        sys.exit(1)

    if isinstance(routes, list) and all(isinstance(r, list) for r in routes):
        msg = 'Least number of buses to reach destination: {}'
        print(msg.format(buses_to_destination(routes, start, end)))
    else:
        raise TypeError('"routes" must be a list of lists.')
