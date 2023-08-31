#!/usr/bin/python3
"""
    Module for a function named island_perimeter
"""


def island_perimeter(grid):
    """
        function that computes the perimter of the island
        described by the list of lists
    """
    initial = 0
    count = 0

    for i in grid:
        for j in i:
            if j == 1:
                initial += 1

    if initial == 1:
        return 4
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if j + 1 < len(grid[i]) and j - 1 >= 0:
                    if grid[i][j + 1] == 1:
                        count += 1
                    elif grid[i][j - 1] == 1:
                        count += 1
                    elif i + 1 < len(grid):
                        if grid[i + 1][j] == 1:
                            count += 1
                elif j - 1 < 0 and j + 1 < len(grid[i]):
                    if grid[i][j + 1] == 1:
                        count += 1
                    elif i + 1 < len(grid):
                        if grid[i + 1][j] == 1:
                            count += 1
                elif not j + 1 < len(grid[i]) and not j - 1 >= 0:
                    if i + 1 < len(grid):
                        if grid[i + 1][j] == 1:
                            count += 1
                    elif not i + 1 < len(grid) and i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count += 1
                else:
                    return 0

    if count:
        result = (4 * count) - ((count * 2) - 2)
    else:
        result = count
    return result
