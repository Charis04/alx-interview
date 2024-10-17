#!/usr/bin/env python3
"""
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations to get exactly n "H"
    characters.

    Args:
        n (int): The target number of "H" characters.

    Returns:
        int: The minimum number of operations required, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
