#!/usr/bin/python3
"""
    Module for a function that validate for UTF-8
    compatibility
"""


def convert_to_binary(num):
    """
        converts a number to binary
    """

    result = ""

    while num != 0:
        result += str(num % 2)
        num = num // 2

    return result


def validUTF8(data):
    """
        Function that validates for valid UTF-8 bytes
    """

    result = []

    for i in data:
        result.append(convert_to_binary(i))

    if all([len(string) < 9 for string in result]):
        return True
    return False
