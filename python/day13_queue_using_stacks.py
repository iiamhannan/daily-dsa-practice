"""
Day 13: Implement Queue using Stacks
-----------------------------------------
Problem:
Implement a first-in-first-out (FIFO) queue using only two stacks. The
implemented queue should support push, pop, peek, and empty operations.

Example:
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.peek()   # returns 1
    queue.pop()    # returns 1
    queue.empty()  # returns False

Topic: Stack / Queue
Difficulty: Easy
"""


class MyQueue:
    def __init__(self):
        self.in_stack = []   # for pushing new elements
        self.out_stack = []  # for popping/peeking in FIFO order

    def push(self, x):
        self.in_stack.append(x)

    def _transfer_if_needed(self):
        """Move everything to out_stack only when out_stack is empty,
        which reverses the order back to FIFO."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self):
        self._transfer_if_needed()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())    # Expected: 1
    print(q.pop())     # Expected: 1
    print(q.empty())   # Expected: False
    print(q.pop())     # Expected: 2
    print(q.empty())   # Expected: True