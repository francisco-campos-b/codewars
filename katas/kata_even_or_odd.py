"""
8kyu
A function that takes an integer and returns "Even" for even numbers or "Odd" for odd numbers
"""


def even_or_odd(x: int) -> str:
    """Checks for even or odd"""
    if x % 2 == 0:
        return "Even"
    return "Odd"
