"""
Day 15: Maximum Depth of Binary Tree
------------------------------------------
Problem:
Given the root of a binary tree, return its maximum depth — the number of
nodes along the longest path from the root down to the farthest leaf node.

Example:
    Input:  root = [3,9,20,null,null,15,7]
             3
            / \
           9  20
              /  \
             15   7
    Output: 3

Topic: Trees
Difficulty: Easy
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """A tree's depth is 1 (for the node itself) plus the deeper of its two subtrees."""
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    # Build:        3
    #              / \
    #             9  20
    #                /  \
    #               15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(root))   # Expected: 3

    print(max_depth(None))   # Expected: 0
    print(max_depth(TreeNode(1)))  # Expected: 1