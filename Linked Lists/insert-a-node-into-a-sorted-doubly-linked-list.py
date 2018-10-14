#!/bin/python3

"""
Inserting a Node Into a Sorted Doubly Linked List
Your Inserting a Node Into a Sorted Doubly Linked List submission got 5.00 points.  
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it into a sorted linked list while maintaining the sort.

Function Description

Complete the sortedInsert function in the editor below. It must return a reference to the head of your modified DoublyLinkedList.

sortedInsert has two parameters:

head: A reference to the head of a doubly-linked list of DoublyLinkedListNode objects.
data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.
Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.

Input Format

The first line contains an integer , the number of test cases.

Each of the test case is in the following format:

The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer, the data for each node of the linked list.
The last line contains an integer  which needs to be inserted into the sorted doubly-linked list.
Constraints

Output Format

Do not print anything to stdout. Your method must return a reference to the  of the same list that was passed to it as a parameter.

The ouput is handled by the code in the editor and is as follows: 
For each test case, print the elements of the sorted doubly-linked list separated by spaces on a new line.

Sample Input

1
4
1
3
4
10
5
Sample Output

1 3 4 5 10
Explanation

The initial doubly linked list is:  .

The doubly linked list after insertion is: 
"""

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    """
    The strategy is to find the two nodes before and after 'data', but the tricky thing here is
    that both could be missing, so we add a faked root here before the head.
    """
    root = DoublyLinkedListNode(0)
    root.next = head
    curr = root
    while curr.next and (data > curr.next.data):
        curr = curr.next
    next_node = curr.next
    curr.next = DoublyLinkedListNode(data)
    curr.next.prev = curr
    curr.next.next = next_node
    return root.next
