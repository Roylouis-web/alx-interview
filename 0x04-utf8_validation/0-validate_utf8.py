#!/usr/bin/python3

"""
    Module for a function called validITF8
"""


def convert_to_binary(num):
    """
        convert a decimal to its binary equivalent
    """

    result = ""

    while num != 0:
        result += str(num % 2)
        num = num // 2
    return result[::1]


def validUTF8(data):
    """
        A function that checks if a series of bytes are
        valid UTF-8
    """

    for value in data:
        if value > 255:
            return False
        elif len(convert_to_binary(value)) > 8:
            return False
    return True
