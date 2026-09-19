"""
Day 23: Climbing Stairs
----------------------------
Problem:
You are climbing a staircase with `n` steps. Each time you can climb either
1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
    Input:  n = 3
    Output: 3
    Explanation: (1+1+1), (1+2), (2+1)

Topic: Dynamic Programming
Difficulty: Easy
"""


def climb_stairs(n):
    """The number of ways to reach step n is the sum of ways to reach
    n-1 and n-2 -- it's just Fibonacci in disguise."""
    if n <= 2:
        return n

    one_step_before, two_steps_before = 2, 1
    for _ in range(3, n + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current

    return one_step_before


if __name__ == "__main__":
    print(climb_stairs(2))   # Expected: 2
    print(climb_stairs(3))   # Expected: 3
    print(climb_stairs(5))   # Expected: 8