"""
Day 8: Fibonacci Number (Recursion + Memoization)
-----------------------------------------------------
Problem:
The Fibonacci numbers form a sequence where each number is the sum of the two
preceding ones, starting from 0 and 1. Given `n`, return the n-th Fibonacci
number, F(n).

    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

Example:
    Input:  n = 10
    Output: 55

Topic: Recursion / Dynamic Programming
Difficulty: Easy
"""


def fibonacci(n, memo=None):
    """Top-down DP: cache results so each F(k) is only computed once."""
    if memo is None:
        memo = {}
    if n in (0, 1):
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fibonacci(10))  # Expected: 55
    print(fibonacci(0))   # Expected: 0
    print(fibonacci(20))  # Expected: 6765
