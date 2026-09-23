"""
Day 30: Subsets
--------------------
Problem:
Given an integer array `nums` of unique elements, return all possible
subsets (the power set). The solution set must not contain duplicate subsets.

Example:
    Input:  [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Topic: Backtracking
Difficulty: Medium
"""


def subsets(nums):
    """At each element, branch into two paths: 'include it' and 'don't include it'."""
    result = []

    def backtrack(start, current):
        result.append(current[:])  # every partial state is a valid subset

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()  # undo before trying the next element

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    # Expected: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]  (order may vary)

    print(subsets([0]))
    # Expected: [[], [0]]