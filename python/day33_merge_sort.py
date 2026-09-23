"""
Day 33: Merge Sort (from scratch)
------------------------------------------
Problem:
Implement Merge Sort: given an array of integers, sort it in ascending
order without using the built-in sort function.

Example:
    Input:  [5, 2, 4, 6, 1, 3]
    Output: [1, 2, 3, 4, 5, 6]

Topic: Sorting / Divide and Conquer
Difficulty: Medium
Time Complexity: O(n log n)
"""


def merge_sort(arr):
    """Divide the array in half, sort each half recursively, then merge them."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    """Merge two already-sorted lists into one sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    print(merge_sort([5, 2, 4, 6, 1, 3]))   # Expected: [1, 2, 3, 4, 5, 6]
    print(merge_sort([]))                     # Expected: []
    print(merge_sort([1]))                    # Expected: [1]
    print(merge_sort([9, -2, 0, 5, -7]))      # Expected: [-7, -2, 0, 5, 9]