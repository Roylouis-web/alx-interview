#!/usr/bin/python3

"""
    Module for a function called validITF8
"""


def validUTF8(data):
    """
        A function that checks if a series of bytes are
        valid UTF-8
    """

    for value in data:
        if value > 255:
            return False
    return True
