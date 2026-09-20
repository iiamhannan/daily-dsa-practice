"""
Day 26: 0/1 Knapsack
-------------------------
Problem:
Given `n` items, each with a weight and a value, and a knapsack with a
maximum weight capacity `W`, determine the maximum total value you can carry
without exceeding the capacity. Each item can be taken at most once (hence
"0/1" -- take it or don't).

Example:
    Input:  weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7
    Output: 9   (take items with weight 3 and 4 -> value 4 + 5 = 9)

Topic: Dynamic Programming
Difficulty: Medium
"""


def knapsack(weights, values, capacity):
    """dp[c] = best value achievable with capacity c, updated item by item.
    Iterate capacity backwards so each item is only used once (0/1, not unbounded)."""
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for c in range(capacity, weights[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i])

    return dp[capacity]


if __name__ == "__main__":
    print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))  # Expected: 9
    print(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))   # Expected: 7
    print(knapsack([1, 2, 3], [6, 10, 12], 5))       # Expected: 22