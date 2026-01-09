"""
5kyu
Write an algorithm that:
Takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst: list) -> list:
    """Moves zeros to the end of the list"""
    zeros = []
    non_zeros = []
    for element in lst:
        if element == 0:
            zeros.append(element)
        else:
            non_zeros.append(element)
    return non_zeros + zeros
