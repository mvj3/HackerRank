"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head is None:
        return False
    node = head
    for _ in range(101):  # because the instruction already told us the list size is less than 101
        node = node.next
        if node is None:
            return False
        if node == head:
            return True
    return False
