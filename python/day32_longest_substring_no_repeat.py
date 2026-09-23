"""
Day 32: Longest Substring Without Repeating Characters
------------------------------------------------------------
Problem:
Given a string `s`, find the length of the longest substring without
repeating characters.

Example:
    Input:  "abcabcbb"
    Output: 3   ("abc" has length 3)

    Input:  "bbbbb"
    Output: 1   ("b" is the longest without repeats)

Topic: Sliding Window
Difficulty: Medium
"""


def length_of_longest_substring(s):
    """Expand the window's right edge each step; whenever we see a repeat,
    shrink the left edge past its previous occurrence."""
    last_seen = {}  # character -> most recent index
    left = 0
    longest = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # Expected: 3
    print(length_of_longest_substring("bbbbb"))      # Expected: 1
    print(length_of_longest_substring("pwwkew"))     # Expected: 3
    print(length_of_longest_substring(""))            # Expected: 0