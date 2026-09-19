"""
Day 22: Course Schedule (Cycle Detection)
------------------------------------------------
Problem:
There are `numCourses` courses labeled 0 to numCourses-1. Some courses have
prerequisites, given as pairs [a, b] meaning you must take course `b` before
course `a`. Return True if you can finish all courses (i.e., there is no
cycle in the prerequisite graph).

Example:
    Input:  numCourses = 2, prerequisites = [[1,0]]
    Output: True   (take course 0, then course 1)

    Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: False  (0 needs 1, and 1 needs 0 -- a cycle)

Topic: Graphs / Topological Sort / Cycle Detection
Difficulty: Medium
"""

from collections import defaultdict, deque


def can_finish(num_courses, prerequisites):
    """Kahn's algorithm (BFS topological sort): if we can process every node
    by repeatedly removing in-degree-0 nodes, there's no cycle."""
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Start with every course that has no prerequisites.
    queue = deque([c for c in range(num_courses) if in_degree[c] == 0])
    completed = 0

    while queue:
        current = queue.popleft()
        completed += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))            # Expected: True
    print(can_finish(2, [[1, 0], [0, 1]]))    # Expected: False
    print(can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Expected: True