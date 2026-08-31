"""
Day 1: Two Sum
---------------
Problem:
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

You may assume each input has exactly one solution, and you may not use the
same element twice.

Example:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]   (because nums[0] + nums[1] == 9)

Topic: Arrays / Hashing
Difficulty: Easy
"""


def two_sum(nums, target):
    """Return indices of the two numbers that add up to target, using a hash map."""
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # Expected: [0, 1]
    print(two_sum([3, 2, 4], 6))        # Expected: [1, 2]
    print(two_sum([3, 3], 6))           # Expected: [0, 1]
