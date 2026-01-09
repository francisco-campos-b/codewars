"""
7kyu
Description:
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""


def find_short(s: str) -> int:
    list_of_words = s.split()
    list_of_sorted_words = sorted(list_of_words, key=len)
    l = len(list_of_sorted_words[0])
    return l
