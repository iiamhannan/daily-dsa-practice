"""
Day 3: Valid Palindrome
--------------------------
Problem:
Given a string `s`, return True if it is a palindrome after converting all
uppercase letters to lowercase and removing all non-alphanumeric characters.

Example:
    Input:  "A man, a plan, a canal: Panama"
    Output: True

    Input:  "race a car"
    Output: False

Topic: Strings / Two Pointers
Difficulty: Easy
"""


def is_palindrome(s):
    """Two-pointer scan, skipping non-alphanumeric characters, case-insensitive."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(is_palindrome("race a car"))                        # Expected: False
    print(is_palindrome(" "))                                  # Expected: True