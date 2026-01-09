"""
8kyu
Description:
Given a month (integer) from 1 to 12, return the respective quarter of the year as an integer.
For example:
- month 2 (February), is part of the first quarter.
- month 6 (June), is part of the second quarter.
- month 11 (November), is part of the fourth quarter.
Constraint: 1 <= month <= 12
"""


def quarter_of(month: int) -> int:
    """Returns the quarter to which a given month belongs"""
    if month in range(1, 4):
        return 1
    if month in range(4, 7):
        return 2
    if month in range(7, 10):
        return 3
    return 4
