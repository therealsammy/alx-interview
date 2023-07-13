#!/usr/bin/python3
"""
Module for calculating the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve
    n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n = n / divisor
        else:
            divisor += 1

    return operations
