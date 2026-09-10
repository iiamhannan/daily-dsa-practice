"""
Day 12: Min Stack
----------------------
Problem:
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time O(1).

Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2

Topic: Stack
Difficulty: Medium
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # tracks the minimum at each stack level

    def push(self, val):
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())  # Expected: -3
    min_stack.pop()
    print(min_stack.top())      # Expected: 0
    print(min_stack.get_min())  # Expected: -2