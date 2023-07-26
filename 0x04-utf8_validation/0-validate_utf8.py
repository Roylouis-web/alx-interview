#!/usr/bin/python3
"""
    Module for a function that validate for UTF-8
    compatibility
"""


def validUTF8(data):
    """
        Function that validates for valid UTF-8 bytes
    """

    for i in data:
        if i > 255:
            return False

    return True
