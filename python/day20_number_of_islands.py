"""
Day 20: Number of Islands
------------------------------
Problem:
Given an m x n 2D binary grid `grid` which represents a map of '1' (land)
and '0' (water), return the number of islands. An island is surrounded by
water and is formed by connecting adjacent lands horizontally or vertically.

Example:
    Input:
        [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
    Output: 3

Topic: Graphs / DFS / BFS
Difficulty: Medium
"""


def num_islands(grid):
    """Flood-fill (DFS) every unvisited land cell, sinking the whole island each time."""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def sink(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # mark as visited by "sinking" it
        sink(r + 1, c)
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                sink(r, c)

    return islands


if __name__ == "__main__":
    grid1 = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    print(num_islands(grid1))  # Expected: 3

    grid2 = [
        list("111"),
        list("010"),
        list("111"),
    ]
    print(num_islands(grid2))  # Expected: 1