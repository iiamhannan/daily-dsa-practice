"""
Day 16: Validate Binary Search Tree
------------------------------------------
Problem:
Given the root of a binary tree, determine if it is a valid binary search
tree (BST). A valid BST means:
- The left subtree of a node contains only nodes with values strictly less
  than the node's value.
- The right subtree contains only nodes with values strictly greater.
- Both subtrees must also be valid BSTs.

Example:
    Input:  root = [2,1,3]
    Output: True

    Input:  root = [5,1,4,null,null,3,6]
    Output: False   (4's right child is 3, which is less than 4)

Topic: Trees / BST
Difficulty: Medium
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    """Carry a valid (low, high) range down the recursion; each node must fit in it."""

    def validate(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(valid))  # Expected: True

    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(is_valid_bst(invalid))  # Expected: False