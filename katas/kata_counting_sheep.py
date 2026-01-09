"""
8kyu
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).

For example: [true, true, true, false]
The correct answer would be 3.

Hint: Don't forget to check for bad values like null/undefined
"""


def count_sheeps(sheep: list) -> int:
    """returns True values in a list"""
    counter = 0
    for i in sheep:
        if i is True:
            counter += 1
    return counter
