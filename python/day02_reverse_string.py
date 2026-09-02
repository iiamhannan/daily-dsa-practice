"""
Day 2: Reverse String
-----------------------
Problem:
Write a function that reverses a string. The input is given as an array of
characters `s`, and you must do this by modifying the input array in-place
with O(1) extra memory.

Example:
    Input:  ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Topic: Strings / Two Pointers
Difficulty: Easy
"""


def reverse_string(s):
    """Reverse the list of characters in-place using the two-pointer technique."""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


if __name__ == "__main__":
    print(reverse_string(["h", "e", "l", "l", "o"]))   # Expected: ['o','l','l','e','h']
    print(reverse_string(["H", "a", "n", "n", "a", "h"]))  # Expected: ['h','a','n','n','a','H']