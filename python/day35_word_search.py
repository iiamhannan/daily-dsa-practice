"""
Day 35: Word Search
-------------------------
Problem:
Given an m x n grid of characters `board` and a string `word`, return True
if `word` exists in the grid. The word can be constructed from letters of
sequentially adjacent cells (horizontally or vertically), where the same
cell may not be used more than once.

Example:
    Input:  board = [["A","B","C","E"],
                      ["S","F","C","S"],
                      ["A","D","E","E"]],
            word = "ABCCED"
    Output: True

Topic: Backtracking / Matrix / DFS
Difficulty: Medium
"""


def exist(board, word):
    """DFS from every cell that matches the first letter, backtracking
    (marking cells visited, then un-marking) as we explore each path."""
    if not board:
        return False

    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = '#'  # mark this cell as visited for this path

        found = (
            backtrack(r + 1, c, index + 1) or
            backtrack(r - 1, c, index + 1) or
            backtrack(r, c + 1, index + 1) or
            backtrack(r, c - 1, index + 1)
        )

        board[r][c] = temp  # backtrack: restore the cell for other paths
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True

    return False


if __name__ == "__main__":
    board = [
        list("ABCE"),
        list("SFCS"),
        list("ADEE"),
    ]
    print(exist(board, "ABCCED"))  # Expected: True
    print(exist(board, "SEE"))      # Expected: True
    print(exist(board, "ABCB"))     # Expected: False