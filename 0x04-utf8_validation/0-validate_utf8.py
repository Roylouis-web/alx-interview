#!/usr/bin/python3

"""
    Module for a function called validITF8
"""


def validUTF8(data):
    """
        A function that checks if a series of bytes are
        valid UTF-8
    """

    for i in range(len(data)):
        value = data[i]
        num_of_bytes = 0

        if value >= 255:
            return False
        elif value & 128 == 0:
            num_of_bytes = 1
        elif value & 224 == 192:
            num_of_bytes = 2
        elif value & 240 == 224:
            num_of_bytes = 3
        elif value & 248 == 240:
            num_of_bytes = 4
        else:
            return False

        for j in range(1, num_of_bytes):
            if j + 1 > len(data):
                return False
            elif data[i + j] & 192 != 1:
                return False
        i = i + num_of_bytes - 1
    return True
