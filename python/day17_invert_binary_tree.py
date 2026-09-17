"""
Day 17: Invert Binary Tree
------------------------------
Problem:
Given the root of a binary tree, invert the tree (mirror it left-to-right)
and return its root.

Example:
    Input:       4                Output:      4
                / \                           / \
               2   7                         7   2
              / \ / \                       / \ / \
             1  3 6  9                     9  6 3  1

Topic: Trees
Difficulty: Easy
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    """Swap left and right children at every node, recursively."""
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def tree_to_list_preorder(root):
    """Helper to visualize the tree as a flat list for the test prints below."""
    if root is None:
        return []
    return [root.val] + tree_to_list_preorder(root.left) + tree_to_list_preorder(root.right)


if __name__ == "__main__":
    # Build:        4
    #              / \
    #             2   7
    #            / \ / \
    #           1  3 6  9
    root = TreeNode(4,
                     TreeNode(2, TreeNode(1), TreeNode(3)),
                     TreeNode(7, TreeNode(6), TreeNode(9)))

    print(tree_to_list_preorder(root))               # Before: [4, 2, 1, 3, 7, 6, 9]
    inverted = invert_tree(root)
    print(tree_to_list_preorder(inverted))            # After:  [4, 7, 9, 6, 2, 3, 1]