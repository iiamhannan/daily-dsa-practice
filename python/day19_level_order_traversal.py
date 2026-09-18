"""
Day 19: Binary Tree Level Order Traversal (BFS)
------------------------------------------------------
Problem:
Given the root of a binary tree, return the level order traversal of its
nodes' values (i.e., from left to right, level by level).

Example:
    Input:  root = [3,9,20,null,null,15,7]
             3
            / \
           9  20
              /  \
             15   7
    Output: [[3], [9, 20], [15, 7]]

Topic: Trees / BFS
Difficulty: Medium
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """Classic BFS with a queue: process one full level before moving to the next."""
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


if __name__ == "__main__":
    # Build:        3
    #              / \
    #             9  20
    #                /  \
    #               15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(level_order(root))   # Expected: [[3], [9, 20], [15, 7]]

    print(level_order(None))   # Expected: []