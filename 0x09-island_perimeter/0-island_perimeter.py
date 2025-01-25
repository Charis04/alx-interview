#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
Calculate perimeter of the island
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    :param grid: List[List[int]], the grid representation of the island
    :return: int, the perimeter of the island
    """
    # Initialize the perimeter
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Loop through the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Start with 4 sides
                perimeter += 4

                # Subtract 2 for each adjacent land cell (shared edge)
                if r > 0 and grid[r - 1][c] == 1:  # Check above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
