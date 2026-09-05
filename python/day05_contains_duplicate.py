"""
Day 5: Contains Duplicate
----------------------------
Problem:
Given an integer array `nums`, return True if any value appears at least
twice in the array, and False if every element is distinct.

Example:
    Input:  [1,2,3,1]
    Output: True

    Input:  [1,2,3,4]
    Output: False

Topic: Arrays / Hashing
Difficulty: Easy
"""


def contains_duplicate(nums):
    """A set lets us check 'have I seen this before?' in O(1) average time."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))        # Expected: True
    print(contains_duplicate([1, 2, 3, 4]))        # Expected: False
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Expected: True