import time
import multiprocessing


class TimeLimitError(Exception):
    pass


def assert_time_limit(time_limit, func, *args, **kwargs):
    """Run the given function once and check if it took longer than the limit.

    Args:
        time_limit (int|float): max execution time allowed before test fails.
        func (obj): the function to evaluate.

    Example:
        >>> assert_time_limit(5, lambda x: x ** 2, 5)
        >>> assert_time_limit(0.2, lambda x, y: x + y, 20, 30)
        >>> import pytest
        >>> with pytest.raises(AssertionError):
        ...     assert_time_limit(0, lambda x: len(x), [2, 4, 6, 8])

    """
    p = multiprocessing.Process(target=func, args=args)
    start = time.perf_counter()
    p.start()
    check(p, start, time_limit)
    return time.perf_counter() - start   


def assert_time_limit_multitest(time_limit, func, *args, **kwargs):
    """Run the given function multiple times on a single time limit constrain.

    Args:
        time_limit (int|float): max execution time allowed before test fails.
        func (obj): the function to evaluate.

    Raises:
        ValueError: to avoid confusion with `assert_time_limit`.

    Example:
        >>> import time, pytest
        >>> def gpc(delay, char):
        ...     for i in range(delay):
        ...         time.sleep(0.1)
        >>> assert_time_limit_multitest(0.8, gpc, (2, 'a'), (1, 'abc'))
        >>> args = [(1, 'a'), (2, 'b'), (4, 'abc')]
        >>> assert_time_limit_multitest(0.8, gpc, *args)
        >>> with pytest.raises(AssertionError):
        ...     assert_time_limit_multitest(0.6, gpc, *args)

    """
    if len(args) <= 1:
        raise ValueError(
            'Multitest expects two or more positional arguments')
    start = time.perf_counter()
    for test_args in args:
        p = multiprocessing.Process(target=func, args=test_args)
        p.start()
        check(p, start, time_limit)
    return time.perf_counter() - start


def check(p, start, time_limit):
    while p.is_alive():
        if time.perf_counter() - start > time_limit:
            p.terminate()
            raise TimeLimitError('Terminated due to TLE.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
