"""
7kyu
Write a small function that returns the values of an array that are not odd.
All values in the array will be integers. Return the good values in the order they are given.
"""


def no_odds(values: list) -> list:
    """Return list of only even values"""
    even_values = []
    for value in values:
        if value % 2 == 0:
            even_values.append(value)
    return even_values
