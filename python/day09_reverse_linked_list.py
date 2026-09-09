"""
Day 9: Reverse Linked List
------------------------------
Problem:
Given the head of a singly linked list, reverse the list and return the
new head.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
    Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

Topic: Linked List
Difficulty: Easy
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """Iteratively re-point each node's 'next' to the previous node."""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def build_list(values):
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    print(list_to_array(reversed_head))  # Expected: [5, 4, 3, 2, 1]

    head2 = build_list([1, 2])
    print(list_to_array(reverse_list(head2)))  # Expected: [2, 1]
