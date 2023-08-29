#!/usr/bin/python3
"""
    Module for a function called island_perimeter
"""


def island_perimeter(grid):
    """
        A function that returns the perimeter
        of the island described in grid
    """
 
    if len(grid) > 100:
        return 0
    if any([len(g) > 100 for g in grid]):
        return 0
    count = 0
    result = None
    for i in grid:
        for j in i:
            if j == 1:
                count += 1
    if count:
        result = (4 * count) - ((count * 2) - 2)
    else:
        result = count
    return result
