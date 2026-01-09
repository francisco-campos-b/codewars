"""
6kyu
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(s: str) -> dict:
    """Counts all characters in a string"""
    characters_in_string = {}
    for i in s:
        if i not in characters_in_string:
            characters_in_string[i] = 1
        else:
            characters_in_string[i] += 1
    return characters_in_string
