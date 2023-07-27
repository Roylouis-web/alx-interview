#!/usr/bin/python3

"""
    Module for a function called validITF8
"""


def check(num):
    """
        checks for a valid byte
    """

    mask = 1 << (8 - 1)
    i = 0
    while num & mask:
        mask >>= 1
        i += 1
    return i


def validUTF8(data):
    """
        A function that checks if a series of bytes are
        valid UTF-8
    """

    i = 0
    while i < len(data):
        if data[i] > 255:
            return False
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k > len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
    return True
