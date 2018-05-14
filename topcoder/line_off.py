"""2018 TCO Algorithm Round 1A Easy: LineOff.

You are given a set of colored points on a straight line.

You play a game with these points. The game is a sequence of moves. In each
move you have to erase two points that are adjacent and share the same color.
(Two points are adjacent if there is no other point between them. Distances
don't matter.)

You are given the points. Each character of points describes the color of one
point, in the order in which they are arranged on the line at the beginning of
the game. (Different letters represent different colors.) Compute and return
the maximum number of moves you can make.

Constraints

- points will contain between 1 and 50 characters, inclusive.
- Each character in points will be a lowercase English letter ('a'-'z').

"""


def solve(points):
    for i in range(len(points) - 1):
        if points[i] == points[i + 1]:
            return 1 + solve(points[:i] + points[i + 2:])
    return 0


if __name__ == '__main__':
    points = input().strip()
    print(solve(points))
