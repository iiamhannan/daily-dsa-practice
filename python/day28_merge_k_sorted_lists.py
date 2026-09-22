"""
Day 28: Merge K Sorted Lists
------------------------------------
Problem:
You are given an array of `k` linked lists, each sorted in ascending order.
Merge all the linked lists into one sorted linked list and return its head.

Example:
    Input:  lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

Topic: Heaps / Linked Lists
Difficulty: Hard
"""

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    """Push the head of every list into a min-heap; repeatedly pop the smallest
    and push its 'next' -- this is essentially a k-way merge."""
    heap = []

    # A counter breaks ties so ListNode objects are never compared directly.
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


def build_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    merged = merge_k_lists(lists)
    print(list_to_array(merged))  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]

    print(list_to_array(merge_k_lists([])))  # Expected: []