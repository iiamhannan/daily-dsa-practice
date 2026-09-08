"""
Day 7: Binary Search
------------------------
Problem:
Given a sorted array of integers `nums` and an integer `target`, return the
index of `target` if it exists, otherwise return -1. Must run in O(log n) time.

Example:
    Input:  nums = [-1,0,3,5,9,12], target = 9
    Output: 4

Topic: Binary Search
Difficulty: Easy
"""


def binary_search(nums, target):
    """Classic binary search: repeatedly halve the search space."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))   # Expected: 4
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))   # Expected: -1
    print(binary_search([5], 5))                      # Expected: 0