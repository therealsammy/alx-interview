#!/usr/bin/python3
"""In a text file, there is a single character H.
 Your text editor can execute only two operations
 in this file: Copy All and Paste. Given a number
n, write a method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file."""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file"""
    process = 2
    operations = 0
    while n > 1:
        while n % process == 0:
            operations += process
            n /= process
        process += 1
    return operations
