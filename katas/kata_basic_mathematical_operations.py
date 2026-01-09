"""
8kyu
Create a function that does four basic mathematical operations.
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
Examples:
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""


def basic_op(operator: str, value1: int, value2: int) -> int | str | float:
    """
    Performs the given operation
    """
    if operator == "+":
        return value1 + value2
    if operator == "-":
        return value1 - value2
    if operator == "*":
        return value1 * value2
    if operator == "/":
        return value1 / value2
    return "Incorrect input"
