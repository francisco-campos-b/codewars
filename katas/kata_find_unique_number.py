"""
6kyu
Description:
There is an array with some numbers.
All numbers are equal except for one. Try to find it!
It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
Example:
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
"""


def find_uniq(arr: list[int | float]) -> int | float:
    """Retrieves unique value in array"""
    arr_set = set(arr)
    for n in arr_set:
        if arr.count(n) == 1:
            return n
