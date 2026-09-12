"""
Day 14: Binary Tree Inorder Traversal
------------------------------------------
Problem:
Given the root of a binary tree, return the inorder traversal of its nodes'
values (Left -> Root -> Right).

Example:
    Input:  root = [1, null, 2, 3]
             1
              \
               2
              /
             3
    Output: [1, 3, 2]

Topic: Trees
Difficulty: Easy
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """Recursively visit left subtree, then the node, then the right subtree."""
    result = []

    def visit(node):
        if node is None:
            return
        visit(node.left)
        result.append(node.val)
        visit(node.right)

    visit(root)
    return result


if __name__ == "__main__":
    # Build:      1
    #              \
    #               2
    #              /
    #             3
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(inorder_traversal(root))  # Expected: [1, 3, 2]

    print(inorder_traversal(None))  # Expected: []