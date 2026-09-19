"""
Day 24: House Robber
-------------------------
Problem:
You are a robber planning to rob houses along a street. Each house has some
amount of money, but adjacent houses have connected security systems --
robbing two adjacent houses will trigger the alarm. Given `nums` (money in
each house), return the maximum amount you can rob without robbing two
adjacent houses.

Example:
    Input:  [1,2,3,1]
    Output: 4   (rob house 1 and house 3: 1 + 3 = 4)

    Input:  [2,7,9,3,1]
    Output: 12  (rob houses 1, 3, 5: 2 + 9 + 1 = 12)

Topic: Dynamic Programming
Difficulty: Medium
"""


def rob(nums):
    """At each house, either skip it (keep previous best) or rob it
    (best from two houses back + this house's money)."""
    prev, curr = 0, 0
    for money in nums:
        prev, curr = curr, max(curr, prev + money)
    return curr


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))       # Expected: 4
    print(rob([2, 7, 9, 3, 1]))    # Expected: 12
    print(rob([]))                  # Expected: 0
    print(rob([5]))                 # Expected: 5