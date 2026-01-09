"""
6 kyu
Description:
In this kata, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
Example:
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""


def alphabet_position(text: str) -> str:
    """Replaces every letter with its position in the alphabet"""
    text = text.lower()
    positions = []
    for char in text:
        if char.isalpha():  # only process alphabetic characters
            positions.append(str(ord(char) - ord("a") + 1))
    return " ".join(positions)
