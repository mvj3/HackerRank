#!/bin/python3

"""
Reverse a doubly linked list
Your Reverse a doubly linked list submission got 5.00 points.  
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
This challenge is part of a tutorial track by MyCodeSchool

You’re given the pointer to the head node of a doubly linked list. Reverse the order of the nodes in the list. The head node might be NULL to indicate that the list is empty. Change the next and prev pointers of all the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Function Description

Complete the reverse function in the editor below. It should return a reference to the head of your reversed list.

reverse has the following parameter(s):

head: a reference to the head of a DoublyLinkedList
Input Format

The first line contains an integer , the number of test cases.

Each test case is of the following format:

The first line contains an integer , the number of elements in the linked list.
The next  lines contain an integer each denoting an element of the linked list.
Constraints

Output Format

Return a reference to the head of your reversed list. The provided code will print the reverse array as a one line of space-separated integers for each test case.

Sample Input

1
4
1
2
3
4
Sample Output

4 3 2 1 
Explanation

The initial doubly linked list is: 

The reversed doubly linked list is: 
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
# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse_not_working(head):
    if head is None or head.next is None:
        return head
    curr
    while head2 is not None:
        # print("head1", head1.data, "head2", head2.data)
        # take out next round
        head3 = head2.next
        # reverse head1
        head1.next = None
        head1.prev = head2
        # reverse head2
        head2.next = head1
        head2.prev = head3
        # update to next round
        head1 = head2
        head2 = head3
    return head1

def reverse(head):
    curr = None  # hold the output node
    while head:
        nxt = head.next  # take out next node ref first
        curr = head  # update output
        head.next = head.prev  # reverse1
        head.prev = nxt  # reverse2
        head = nxt # update to next round
    return curr
