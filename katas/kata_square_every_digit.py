"""
7kyu
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
If we run 9119 through the function, 811181 will come out, because 9sq is 81 and 1sq is 1.
An input of 765 should return 493625 because 7sq is 49, 6sq is 36, and 5sq is 25.
Happy Coding!
"""


def square_digits(num: int) -> int:
    """
    Squares every single number and returns the concatenation of the squared numbers.
    """
    squared = ""
    for number in str(num):
        squared = squared + str((int(number)) ** 2)
    return int(squared)
