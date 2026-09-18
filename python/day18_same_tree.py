"""
Day 18: Same Tree
---------------------
Problem:
Given the roots of two binary trees `p` and `q`, check if they are the same
tree — structurally identical, and the nodes have the same value.

Example:
    Input:  p = [1,2,3], q = [1,2,3]
    Output: True

    Input:  p = [1,2], q = [1,null,2]
    Output: False

Topic: Trees
Difficulty: Easy
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    """Two trees match if both nodes are None, or both exist with equal values
    and matching left/right subtrees."""
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(is_same_tree(p1, q1))  # Expected: True

    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    print(is_same_tree(p2, q2))  # Expected: False