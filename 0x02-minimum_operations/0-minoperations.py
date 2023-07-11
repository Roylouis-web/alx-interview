#!/usr/bin/python3

'''
    Module for a function named minOperations
'''


def minOperations(n):
    '''
        A function named minOperations that takes
        an integer as parameter and returns the
        fewest number of operations needed to result
        in exactly n * H characters in a text file
    '''

    if type(n) != int or n <= 0:
        return 0

    num_of_chars = 1
    copy = 0
    paste = 0
    prev = 1
    i = 1

    while i <= n:
        if num_of_chars == n:
            break
        elif i == 1:
            copy += 1
            paste += 1
            num_of_chars += 1
        elif (n % num_of_chars) == 0:
            prev = num_of_chars
            num_of_chars *= 2
            paste += 1
            copy += 1
        else:
            num_of_chars += prev
            paste += 1
        i += 1

    return copy + paste
