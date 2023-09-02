#!/usr/bin/python3
"""
    Module for a function named island_perimeter
"""


def island_perimeter(grid):
    """
        params:
            - grid: A list of lists
        Return:
            The perimeter of the island describe in
            the list of lists
    """

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count += 4
                if j - 1 >= 0 and j + 1 < len(grid[i]) and i + 1 < len(grid):
                    if grid[i][j - 1] == 1:
                        count -= 1
                    if grid[i][j + 1] == 1:
                        count -= 1
                    if grid[i + 1][j] == 1:
                        count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
                elif (not j - 1 >= 0 and
                      j + 1 < len(grid[i]) and i + 1 < len(grid)):
                    if grid[i][j + 1] == 1:
                        count -= 1
                    if grid[i + 1][j] == 1:
                        count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
                elif (j - 1 >= 0 and not
                      j + 1 < len(grid[i]) and i + 1 < len(grid)):
                    if grid[i][j - 1] == 1:
                        count -= 1
                    if grid[i + 1][j] == 1:
                        count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
                elif (j - 1 >= 0 and
                      j + 1 < len(grid[i]) and not i + 1 < len(grid)):
                    if grid[i][j + 1] == 1:
                        count -= 1
                    if grid[i][j - 1] == 1:
                        count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
                elif (j - 1 >= 0 and not
                      j + 1 < len(grid[i]) and not i + 1 < len(grid)):
                    if grid[i][j - 1] == 1:
                        count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
                elif (not j - 1 >= 0 and
                      j + 1 < len(grid[i]) and not i + 1 < len(grid)):
                    if grid[i][j + 1] == 1:
                        count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
                elif (not j - 1 >= 0 and not
                      j + 1 < len(grid[i]) and i + 1 < len(grid)):
                    if grid[i + 1][j] == 1:
                        count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
    return count
