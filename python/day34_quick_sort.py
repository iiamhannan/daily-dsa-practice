"""
Day 34: Quick Sort (from scratch)
------------------------------------------
Problem:
Implement Quick Sort: given an array of integers, sort it in ascending
order without using the built-in sort function.

Example:
    Input:  [5, 2, 4, 6, 1, 3]
    Output: [1, 2, 3, 4, 5, 6]

Topic: Sorting / Divide and Conquer
Difficulty: Medium
Average Time Complexity: O(n log n) | Worst case: O(n^2)
"""


def quick_sort(arr):
    """Pick a pivot, partition everything else around it, then sort each side."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    print(quick_sort([5, 2, 4, 6, 1, 3]))   # Expected: [1, 2, 3, 4, 5, 6]
    print(quick_sort([]))                     # Expected: []
    print(quick_sort([1]))                    # Expected: [1]
    print(quick_sort([3, 3, 1, 2, 2]))        # Expected: [1, 2, 2, 3, 3]