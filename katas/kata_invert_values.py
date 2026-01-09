"""
8kyu
Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.
You can assume that all values are integers. Do not mutate the input array.
"""


def invert(lst: list) -> list:
    """Inverts numbers in the given list"""
    list_1 = []
    for element in lst:
        list_1.append(element * -1)
    return list_1


result1 = invert([1, 2, 3, 4, 5])
result2 = invert([1, -2, 3, -4, 5])
result3 = invert([])

print(result1, result2, result3)
