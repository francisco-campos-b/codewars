"""
7kyu
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence: str) -> int:
    """Counts vowels in a given string"""
    counter = 0
    for character in sentence:
        if character in "aeiou":
            counter += 1
    return counter
