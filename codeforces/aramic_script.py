"""Codeforces Round #478 (Div. 2): Aramic script.

http://codeforces.com/contest/975/problem/A


In Aramic language words can only represent objects.

Words in Aramic have special properties:

- A word is a root if it does not contain the same letter more than once.

- A root and all its permutations represent the same object.

- The root x of a word y is the word that contains all letters that appear in y
in a way that each letter appears once. For example, the root of "aaaa", "aa",
"aaa" is "a", the root of "aabb", "bab", "baabb", "ab" is "ab".

- Any word in Aramic represents the same object as its root.

You have an ancient script in Aramic. What is the number of different objects
mentioned in the script?

"""


def solve(array):
    roots = {tuple(sorted(set(s))) for s in array}
    return len(roots)


def main():
    n = int(input().strip())
    array = input().strip().split()[:n]
    result = solve(array)
    print(result)


if __name__ == '__main__':
    main()
