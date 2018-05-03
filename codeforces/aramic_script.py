"""Aramic script.

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


def count_objects(array):
    roots = {tuple(sorted(set(s))) for s in array}
    return len(roots)


if __name__ == '__main__':
    n = int(input().strip())
    array = input().strip().split()[:n]
    print(count_objects(array))
