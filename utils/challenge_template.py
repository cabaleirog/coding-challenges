TEMPLATE_CHALLENGE_FILE = '''"""{name}.

- Difficulty: {difficulty}

{url}

{description}

{input_format}

{output_format}

{notes}

"""
import logging


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)


def solve(*args):
    return '...'


def main():
    for _ in range(int(input().strip())):
        args = input().strip().split()
        result = solve(*args)
        print(result)


if __name__ == '__main__':
    main()
'''


TEMPLATE_TEST_FILE = '''from utils.test_utils import assert_time_limit
from {folder}.{filename} import solve


def test_problem_statement_sample_test_cases():
    args = ['Arg0', 'Arg1', 'ArgN']
    expected = 'Expected Value'
    assert solve(*args) == expected


def test_time_limit():
    args = []
    assert_time_limit(0, solve, args)  # time limit (s): XXX
'''
