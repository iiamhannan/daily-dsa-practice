"""
Day 29: Permutations
-------------------------
Problem:
Given an array `nums` of distinct integers, return all possible permutations
of the array, in any order.

Example:
    Input:  [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Topic: Backtracking
Difficulty: Medium
"""


def permute(nums):
    """Backtracking: build a permutation one number at a time, undoing the
    choice ('backtracking') once we've explored it fully."""
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])  # copy, since 'current' keeps changing
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i + 1:])
            current.pop()  # undo the choice before trying the next one

    backtrack([], nums)
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
    # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    print(permute([0, 1]))
    # Expected: [[0,1],[1,0]]