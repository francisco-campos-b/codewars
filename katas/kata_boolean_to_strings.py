"""
8kyu
A function that takes a boolean value and return a "Yes" string for true, or a "No" string for false
"""


def bool_to_word(boolean: bool) -> str:
    """Returns "Yes" for True and "No" for False"""
    if boolean is True:
        return "Yes"
    return "No"
