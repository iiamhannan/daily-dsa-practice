"""
Day 21: Clone Graph
------------------------
Problem:
Given a reference to a node in a connected undirected graph, return a deep
copy (clone) of the graph. Each node contains a value and a list of its
neighbors.

Example:
    Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
    (Node 1's neighbors are 2 and 4, etc.)
    Output: A completely new graph with the same structure and values.

Topic: Graphs / DFS
Difficulty: Medium
"""


class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    """DFS + a hash map from original node -> cloned node, so each node is cloned once."""
    if node is None:
        return None

    cloned = {}  # original node -> its clone

    def dfs(original):
        if original in cloned:
            return cloned[original]

        copy = GraphNode(original.val)
        cloned[original] = copy

        for neighbor in original.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)


def build_test_graph():
    """Builds a small square graph: 1-2-3-4-1"""
    n1, n2, n3, n4 = GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    return n1


if __name__ == "__main__":
    original = build_test_graph()
    clone = clone_graph(original)

    print(clone.val)                                   # Expected: 1
    print([n.val for n in clone.neighbors])             # Expected: [2, 4]
    print(clone is original)                            # Expected: False (it's a real copy)