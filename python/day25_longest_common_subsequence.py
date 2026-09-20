"""
Day 25: Longest Common Subsequence
------------------------------------------
Problem:
Given two strings `text1` and `text2`, return the length of their longest
common subsequence (a subsequence keeps relative order but doesn't need to
be contiguous). If there is no common subsequence, return 0.

Example:
    Input:  text1 = "abcde", text2 = "ace"
    Output: 3   ("ace" is a subsequence of both)

    Input:  text1 = "abc", text2 = "def"
    Output: 0

Topic: Dynamic Programming
Difficulty: Medium
"""


def longest_common_subsequence(text1, text2):
    """Classic 2D DP: dp[i][j] = LCS length of text1[:i] and text2[:j]."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    print(longest_common_subsequence("abcde", "ace"))  # Expected: 3
    print(longest_common_subsequence("abc", "abc"))     # Expected: 3
    print(longest_common_subsequence("abc", "def"))     # Expected: 0