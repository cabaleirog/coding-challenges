# TODO: Use multiprocessing module to kill a test running after time out limit.
import time


def assert_time_limit(time_limit, func, *args, **kwargs):
    """Run the given function once and check if it took longer than the limit.

    Args:
        time_limit (int|float): max execution time allowed before test fails.
        func (obj): the function to evaluate.

    Usage:
        >>> args = [2, 4, 6, 8]
        >>> assert_time_limit_multitest(5, foo, args)
    """
    start = time.perf_counter()
    _ = func(*args, **kwargs)
    elapsed_time = time.perf_counter() - start
    assert elapsed_time < time_limit


def assert_time_limit_multitest(time_limit, func, *args, **kwargs):
    """Run the given function multiple times on a single time limit constrain.

    Args:
        time_limit (int|float): max execution time allowed before test fails.
        func (obj): the function to evaluate.

    Raises:
        ValueError: to avoid confusion with `assert_time_limit`.

    Usage:
        >>> args = [[2, 4, 6], [8, 8, 8], [2, 0, 10]]
        >>> assert_time_limit_multitest(5, foo, args)
    """
    if len(args) <= 1:
        raise ValueError(
            'Multitest expects an iterable of size greater than two')
    start = time.perf_counter()
    for test_args in args:
        _ = func(test_args)
    elapsed_time = time.perf_counter() - start
    assert elapsed_time < time_limit
