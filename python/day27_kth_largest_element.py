"""
Day 27: Kth Largest Element in an Array
----------------------------------------------
Problem:
Given an integer array `nums` and an integer `k`, return the k-th largest
element in the array (not the k-th distinct element).

Example:
    Input:  nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Input:  nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Topic: Heaps / Priority Queue
Difficulty: Medium
"""

import heapq


def find_kth_largest(nums, k):
    """Keep a min-heap of size k: the smallest item in it is always the
    k-th largest overall, once the heap is full."""
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))              # Expected: 5
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))     # Expected: 4
    print(find_kth_largest([1], 1))                               # Expected: 1