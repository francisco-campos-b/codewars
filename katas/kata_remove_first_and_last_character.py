"""
8kyu
A function that removes the first and last characters of a given string.
Disregards strings with less than two characters.
"""


def remove_char(string: str) -> str:
    """Removes first and last character"""
    if len(string) > 2:
        return string[1:-1]
    return ""
