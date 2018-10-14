# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    """
    the important point here is to set up a fake head node,
    then we don't need to care about if the head node exsit or not.
    """
    fake_head = SinglyLinkedListNode(0)
    fake_head.next = head
    insert_at = fake_head
    while position > 0:
        if insert_at.next != None:
            insert_at = insert_at.next
        position -= 1
    next_node = insert_at.next
    insert_at.next = SinglyLinkedListNode(data)
    insert_at.next.next = next_node
    return fake_head.next
   
