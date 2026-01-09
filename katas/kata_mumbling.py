"""
7kyu
Description:
This time no story, no theory. The examples below show you how to write function accum.
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(st):
    mumbling = []
    index = 1
    for letter in st:
        letter = letter * index
        letter = letter.capitalize()
        index += 1
        mumbling.append(letter)
    return "-".join(mumbling)
