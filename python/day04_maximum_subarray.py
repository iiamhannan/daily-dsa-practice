"""
Day 4: Maximum Subarray (Kadane's Algorithm)
-----------------------------------------------
Problem:
Given an integer array `nums`, find the contiguous subarray (containing at
least one number) which has the largest sum, and return that sum.

Example:
    Input:  [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6   (the subarray [4,-1,2,1] has the largest sum = 6)

Topic: Arrays / Dynamic Programming
Difficulty: Medium
"""


def max_subarray(nums):
    """Kadane's algorithm: track the best running sum and the best overall sum."""
    current_sum = best_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected: 6
    print(max_subarray([1]))                                # Expected: 1
    print(max_subarray([5, 4, -1, 7, 8]))                   # Expected: 23