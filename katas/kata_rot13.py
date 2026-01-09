"""
5kyu
Description:
ROT13 is a simple letter substitution cipher.
It replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted.
Please note that using encode is considered cheating.
"""


def rot13(message: str) -> str:
    dictionary_rot13 = {
        "a": "n",
        "b": "o",
        "c": "p",
        "d": "q",
        "e": "r",
        "f": "s",
        "g": "t",
        "h": "u",
        "i": "v",
        "j": "w",
        "k": "x",
        "l": "y",
        "m": "z",
        "n": "a",
        "o": "b",
        "p": "c",
        "q": "d",
        "r": "e",
        "s": "f",
        "t": "g",
        "u": "h",
        "v": "i",
        "w": "j",
        "x": "k",
        "y": "l",
        "z": "m",
        "A": "N",
        "B": "O",
        "C": "P",
        "D": "Q",
        "E": "R",
        "F": "S",
        "G": "T",
        "H": "U",
        "I": "V",
        "J": "W",
        "K": "X",
        "L": "Y",
        "M": "Z",
        "N": "A",
        "O": "B",
        "P": "C",
        "Q": "D",
        "R": "E",
        "S": "F",
        "T": "G",
        "U": "H",
        "V": "I",
        "W": "J",
        "X": "K",
        "Y": "L",
        "Z": "M",
    }

    ciphered_message = ""

    for i in message:
        if i in dictionary_rot13:
            ciphered_message += dictionary_rot13[i]
        if i not in dictionary_rot13:
            ciphered_message += i

    return ciphered_message
