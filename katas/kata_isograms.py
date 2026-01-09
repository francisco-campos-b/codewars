"""
7kyu
Description:
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram.
Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
"""


def is_isogram(string: str) -> bool:
    """Determins if the given string is an isogram, returns a boolean value"""
    isogram = True
    for i in string.lower():
        if string.lower().count(i) > 1:
            isogram = False
    return isogram
