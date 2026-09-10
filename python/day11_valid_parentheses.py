"""
Day 11: Valid Parentheses
------------------------------
Problem:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. A string is valid if:
- Open brackets are closed by the same type of bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a matching open bracket.

Example:
    Input:  "()[]{}"
    Output: True

    Input:  "(]"
    Output: False

Topic: Stack
Difficulty: Easy
"""


def is_valid(s):
    """Push opening brackets onto a stack; pop and match when we see a closer."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        # any other character is ignored for this problem

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid("()[]{}"))   # Expected: True
    print(is_valid("(]"))        # Expected: False
    print(is_valid("([)]"))      # Expected: False
    print(is_valid("{[]}"))      # Expected: True