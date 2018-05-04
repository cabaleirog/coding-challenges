"""Validating Postal Codes.

https://www.hackerrank.com/contests/pythonist3/challenges/validating-postalcode

- Difficulty: Hard

A postal code `P` must be a number in the range of (100000, 999999).

A postal code `P` must not contain more than one alternating repetitive
digit pair.

Alternating repetitive digits are digits which repeat immediately after the
next digit. In other words, an alternating repetitive digit pair is formed
by two equal digits that have just a single digit between them.

For example:
    121426 -> Here, 1 is an alternating repetitive digit.
    523563 -> Here, NO digit is an alternating repetitive digit.
    552523 -> Here, both 2 and 5 are alternating repetitive digits.

Your task is to validate whether `P` is a valid postal code or not.

Note:
    A score of 0 will be awarded for using 'if' conditions in your code.
    You have to pass all the testcases to get a positive score.
"""


def alt_rep_digits(code):
    """Count the number of times the code has alternating repetitive digits.

    Args:
        code (str): The code to verify.

    Returns:
        int: Total number of alternating repetitive digits.
    """
    count = 0
    # Loop first by values with even indices, then the ones with odd indices.
    for group in (code[::2], code[1::2]):
        # Offset by one to create a list of pairs [(x0, x2), (x2, x4), ...]
        group_zip = zip(group[:-1], group[1:])
        count += len(list(filter(lambda x: x[0] == x[1], group_zip)))
    return count


def validate(postal_code):
    """Validate the Postal Code according to the provided rules.

    Args:
        postal_code (int|str): The code to validate.

    Returns:
        bool: True if the postal code is valid.
    """
    code = str(postal_code)
    count = alt_rep_digits(code)
    return code.isnumeric() and 100000 <= int(code) <= 999999 and count <= 1


if __name__ == '__main__':
    print(validate(input().strip()))
