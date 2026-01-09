"""
7kyu
Description:
Create function fib that returns n'th element of Fibonacci sequence (classic programming task).
"""


def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence."""
    if n < 0:
        return "Input must be a non-negative integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1  # F(0) and F(1)
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update to next pair: (F(i-1), F(i))
    return b  # b holds the nth term
