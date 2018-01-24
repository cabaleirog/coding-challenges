"""Day of the Programmer.

Marie invented a Time Machine and wants to test it by time-traveling to visit
Russia on the Day of the Programmer (the 256th day of the year) during a year
in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar; since
1919 they used the Gregorian calendar system. The transition from the Julian
to Gregorian calendar system occurred in 1918, when the next day after January
31st was February 14th. This means that in 1918, February 17th was the 32nd
day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of
days; it has 29 days during a leap year, and 28 days during all other years. In
the Julian calendar, leap years are divisible by 4; in the Gregorian calendar,
leap years are either of the following:

* Divisible by 400.
* Divisible by 4 and not divisible by 100.

Given a year, `y`, find the date of the 256th day of that year according to the
official Russian calendar during that year. Then print it in the format
dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and
yyyy is `y`.

https://www.hackerrank.com/challenges/day-of-the-programmer/problem

"""
from enum import Enum

DAY_OF_THE_PROGRAMMER = 256


class Calendar(Enum):
    JULIAN = 1
    GREGORIAN = 2
    TRANSITION = 3


def day_of_the_programmer(year):
    """Return the formatted date of the programmer for a given year.

    Args:
        year (int): The requested year

    Returns:
        str: Formatted date

    Example:
        >>> day_of_the_programmer(2000)
        '12.09.2000'
    """
    calendar = which_calendary(year)
    is_leap = is_leap_year(year, calendar)
    days_by_month = days_array(is_leap, calendar)

    count = 0
    for idx, days in enumerate(days_by_month):
        count += days
        diff = DAY_OF_THE_PROGRAMMER - count
        if diff <= days_by_month[idx + 1]:
            month = (idx + 1) + 1  # Next month index + 1 to convert it to 1-12
            day = diff
            break

    return '{:02}.{:02}.{}'.format(day, month, year)


def days_array(leap_year, calendar):
    """Get the number of days on each month.

    Args:
        leap_year (bool): Is the requested year a leap year
        calendar (int): Which calendar to use

    Returns:
        list[int]: An array containing the number of days on each month
    """
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]
    days = [0] * 12

    for month in months_with_31_days:
        days[month - 1] = 31
    for month in months_with_30_days:
        days[month - 1] = 30

    days[1] = 29 if leap_year else 28  # Index 0 is Jan., Index 1 is Feb.
    if calendar == Calendar.TRANSITION:
        days[1] -= 13  # Feb. 1 to 13 were skipped on that year.

    return days


def which_calendary(year):
    """Get the calendar used on a particular year.

    Args:
        year (int): Requested year

    Raises:
        ValueError: If the year is out of the problem's specifications.

    Returns:
        int: Calendar used on that year
    """
    if year >= 1700 and year <= 1917:
        return Calendar.JULIAN
    elif year >= 1919 and year <= 2700:
        return Calendar.GREGORIAN
    elif year == 1918:
        return Calendar.TRANSITION
    else:
        raise ValueError('Year must be between 1700 and 2700.')


def is_leap_year(year, calendar=Calendar.JULIAN):
    """Check if `year` is a leap year.

    Args:
        year (int): Requested year
        calendar (int, optional): Which alendar to use

    Returns:
        bool: True if it is a leap year, False otherwise
    """
    if calendar == Calendar.JULIAN:
        return year % 4 == 0
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == '__main__':
    print(day_of_the_programmer(1918))
