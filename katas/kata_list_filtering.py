"""
7 kyu
Create a function that takes a list of non-negative integers and strings.
Return a new list with the strings filtered out.
Example:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""


def filter_list(l: list) -> list:
    """return a new list with the strings filtered out"""
    filtered = []
    for item in l:
        if isinstance(item, int):
            filtered.append(item)
    return filtered
