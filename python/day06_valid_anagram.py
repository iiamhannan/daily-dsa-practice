"""
Day 6: Valid Anagram
------------------------
Problem:
Given two strings `s` and `t`, return True if `t` is an anagram of `s`
(uses exactly the same letters, same frequency, different order allowed).

Example:
    Input:  s = "anagram", t = "nagaram"
    Output: True

    Input:  s = "rat", t = "car"
    Output: False

Topic: Strings / Hashing
Difficulty: Easy
"""

from collections import Counter


def is_anagram(s, t):
    """Two strings are anagrams if their character counts match exactly."""
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # Expected: True
    print(is_anagram("rat", "car"))          # Expected: False
    print(is_anagram("listen", "silent"))    # Expected: True