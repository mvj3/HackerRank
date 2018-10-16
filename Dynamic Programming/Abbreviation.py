#!/bin/python3

"""
Abbreviation
Your Abbreviation submission got 40.00 points.  
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
You can perform the following operations on the string, :

Capitalize zero or more of 's lowercase letters.
Delete all of the remaining lowercase letters in .
Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.

For example, given  and , in  we can convert  and delete  to match . If  and , matching is not possible because letters may only be capitalized or discarded, not changed.

Function Description

Complete the function  in the editor below. It must return either  or .

abbreviation has the following parameter(s):

a: the string to modify
b: the string to match
Input Format

The first line contains a single integer , the number of queries.

Each of the next  pairs of lines is as follows: 
- The first line of each query contains a single string, . 
- The second line of each query contains a single string, .

Constraints

String  consists only of uppercase and lowercase English letters, ascii[A-Za-z].
String  consists only of uppercase English letters, ascii[A-Z].
Output Format

For each query, print YES on a new line if it's possible to make string  equal to string . Otherwise, print NO.

Sample Input

1
daBcd
ABC
Sample Output

YES
Explanation

image

We have  daBcd and  ABC. We perform the following operation:

Capitalize the letters a and c in  so that  dABCd.
Delete all the remaining lowercase letters in  so that  ABC.
Because we were able to successfully convert  to , we print YES on a new line.
"""

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation_corncasefailed(a, b):
    """
    Rule#0: make sure a has every character in b.
    Rule#1: keep ordered.

    EdgeCase#0: solve case like a:gG, b:G, we upcased g, but still a G left. Whatever reverse the strs or not.
    """
    print("a=", a)
    print("b=", b)
    a, b = a[::-1], b[::-1]
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        meet_b = False
        if a[a_idx].upper() == b[b_idx]:
            meet_b = True
            b_idx += 1  
        # alone uppercase letter, and we can't remove it.
        if meet_b is False and a[a_idx].upper() == a[a_idx]:
            print("tmp a=", a[:a_idx+1])
            print("tmp b=", b[:b_idx+1])
            # import pdb; pdb.set_trace()
            print("[return NO] while")
            return "NO"
        a_idx += 1
    if b_idx != len(b):  # check if reach the end of b
        return "NO"
    if a[a_idx:] != a[a_idx:].lower():  # check if a still has UpperCase letters.
        return "NO"
    return "YES"

def abbreviation_dp(a, b):
    """
    This very hard challenge takes me more than 5 hours to solve.
    
    When we try to solve this problem, let's don't think DP first, because my method is more like recursion plus memorization.
    
    Keep in mind, the order of the strings in this problem matter. So we need to compare letters one by one by using recursion to move forward. When we think about recursion, we realize that we can pass the rest of (a, b) parameters to the same function as the sub problems. And at the first part of this function, we can try to consider the conditions of when we reach either end of two strings. And at the second part, we deal with when the first letters of (a, b) are equal or not. It is very tricky to deal situation like a:gG,b:G.
    """
    sys.setrecursionlimit(20000)  # this recursion requires very deep stack.
    cache=dict()
    def f(a, b):
        k = (a, b)
        if k in cache:
            return cache[k]
        # b all matched, and reach the end. 
        if not b:
            # Check if a still has uppercase inside
            cache[k] = a == a.lower()
            return cache[k]
        # b can't be longger than a
        if len(b) > len(a):
            cache[k] = False
            return False
        # if one upper letter in a, but not in b, then failed.
        if (a[0].upper() != b[0]) and (a[0] == a[0].upper()):
            cache[k] = False
            return False
        
        next_a = a[1:]
        if a[0].upper() == b[0]:
            # 1. assume both are upcase, so we move forward both one letter.
            k1 = (next_a, b[1:])
            if k1 not in cache:
                cache[k1] = f(*k1)
            if cache[k1]:
                return True
            # 2. is downcase, don't swallow current b letter.
            if a[0] != a[0].upper():  
                k2 = (next_a, b)
                if k2 not in cache:
                    cache[k2] = f(*k2)
                if cache[k2]:
                    return True
        else:
            cache[k] = f(next_a, b)
            return cache[k]
    return "YES" if f(a, b) else "NO"


abbreviation = abbreviation_dp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()

