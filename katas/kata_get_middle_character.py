"""
7kyu
Given a non-empty string, return the middle character(s) of the string.
If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.

Examples:
- "test" --> "es"
- "testing" --> "t"
- "middle" --> "dd"
- "A" --> "A"
"""


def get_middle(s: list) -> list:
    """Retrieves the middle character(s) of a string"""
    middle = int(len(s) / 2)
    if len(s) % 2 == 0:
        return s[middle - 1 : middle + 1]
    return s[middle]
