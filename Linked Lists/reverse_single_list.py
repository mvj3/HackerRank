"""
1) Write a function to reverse a singly linked list.

(It takes a while before they realise they need 3 pointers.)
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "<Node val=%s next=%s>" % (self.val, self.next)


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    new_tail = Node(head.val)
    new_tail_next = None
    while head.next is not None:
        new_tail_next = Node(head.next.val)
        new_tail_next.next = new_tail

        new_tail = new_tail_next
        head = head.next
    return new_tail


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

print(reverse_linked_list(n1))
