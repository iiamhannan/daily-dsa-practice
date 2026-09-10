"""
Day 10: Merge Two Sorted Arrays
------------------------------------
Problem:
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing
order. Merge `nums2` into `nums1` as one sorted array, in-place.

Example:
    Input:  nums1 = [1,2,3], nums2 = [2,5,6]
    Output: [1,2,2,3,5,6]

Topic: Arrays / Two Pointers
Difficulty: Easy
"""


def merge_sorted(nums1, nums2):
    """Merge from the back to front so we never overwrite unread values."""
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    return merged


if __name__ == "__main__":
    print(merge_sorted([1, 2, 3], [2, 5, 6]))  # Expected: [1, 2, 2, 3, 5, 6]
    print(merge_sorted([], [1]))                 # Expected: [1]
    print(merge_sorted([1], []))                 # Expected: [1]
