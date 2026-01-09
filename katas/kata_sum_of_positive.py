"""
8kyu
You get an array of numbers, return the sum of all of the positives ones.
"""


def positive_sum(arr: list) -> int:
    """Sum numbers"""
    list_of_positives = 0
    for x in arr:
        if x > 0:
            list_of_positives = list_of_positives + x
    return list_of_positives


example = [1, -4, 7, 12]
print(positive_sum(example))
