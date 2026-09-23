"""
Day 31: Sliding Window Maximum
------------------------------------
Problem:
You are given an array of integers `nums` and a sliding window of size `k`
which moves from the very left to the very right of the array. Return the
maximum value in the window at each position.

Example:
    Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]

Topic: Sliding Window / Deque
Difficulty: Hard
"""

from collections import deque


def max_sliding_window(nums, k):
    """Keep a deque of INDICES, front-to-back in decreasing value order.
    The front is always the max of the current window."""
    result = []
    window = deque()  # stores indices

    for i, num in enumerate(nums):
        # Remove indices that have fallen out of the window.
        while window and window[0] <= i - k:
            window.popleft()

        # Remove smaller values from the back -- they can never be the max
        # while `num` is still in the window.
        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result


if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Expected: [3,3,5,5,6,7]
    print(max_sliding_window([1], 1))                            # Expected: [1]
    print(max_sliding_window([9, 11], 2))                        # Expected: [11]