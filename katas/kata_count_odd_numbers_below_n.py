"""
8kyu
Given a number n, return the number of positive odd numbers below n.
Examples (Input -> Output):
7  -> 3 (because odd numbers below 7 are [1, 3, 5])
15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])
Expect large Inputs.
"""


def odd_count(n: int) -> int:
    """Returns floor divison which is the number of positive numbers below n"""
    return n // 2
