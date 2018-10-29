#!/bin/python3

"""
Common Child
Your Common Child submission got 60.00 points.  
Proceed to Interview Preparation Kit
Problem
Submissions
Leaderboard
Discussions
Editorial
Topics
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD  ABDC.

Function Description

Complete the commonChild function in the editor below. It should return the longest string which is a common child of the input strings.

commonChild has the following parameter(s):

s1, s2: two equal length strings
Input Format

There is one line with two space-separated strings,  and .

Constraints

All characters are upper case in the range ascii[A-Z].
Output Format

Print the length of the longest string , such that  is a child of both  and .

Sample Input

HARRY
SALLY
Sample Output

 2
Explanation

The longest string that can be formed by deleting zero or more characters from  and  is , whose length is 2.

Sample Input 1

AA
BB
Sample Output 1

0
Explanation 1

 and  have no characters in common and hence the output is 0.

Sample Input 2

SHINCHAN
NOHARAAA
Sample Output 2

3
Explanation 2

The longest string that can be formed between  and  while maintaining the order is .

Sample Input 3

ABCDEF
FBDAMN
Sample Output 3

2
Explanation 3 
 is the longest child of the given strings.
"""

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    """
    Since this question requires us to find an ordered (maybe broken) sequence between two string,
    the first thought would be coming up with two for-loops, the for-loop would takes care of order and even broken cases.
    And then, something is missing, how shall we record the sequence. It seems there could be lots of possibilities of sequences, but we only have to find the longest one. Imagine how do we find the longest ordered sequence by eyes manually. We will count the matched, and then ignore the previous, and continue to search the next one until the end.
    In conclusion, we maybe use a matrix to record the common child.
    """
    # 1. clean the same characters in the beginning and the end.
    left_idx, right_idx = 0, -1
    while s1[left_idx] == s2[left_idx]:
        left_idx += 1
        if left_idx >= min(len(s1), len(s2)):
            break
    while s1[right_idx] == s2[right_idx]:
        right_idx -= 1
        if abs(right_idx) == min(len(s1), len(s2)):
            break
    minus = len(s1) - len(s1[left_idx:len(s1)+right_idx+1])
    #print("minus=", minus)
    #print("left_idx=", left_idx, ", right_idx=", right_idx)
    s1 = s1[left_idx:len(s1)+right_idx+1]
    s2 = s2[left_idx:len(s2)+right_idx+1]
    #print("s1=", s1)
    #print("s2=", s2)
    # 2. build the matching matrix        
    # matrix = [[([0] * len(s2))[:]] * len(s1)] # wrong init method, will share same array.
    # tip: use extra +1 to avoid initialization problem
    matrix = [[0 for i2 in range(len(s2)+1)] for i1 in range(len(s1)+1)]
    for i1, p in enumerate(s1):
        for i2, q in enumerate(s2):
            #print("i1=", i1, ", p=", p, ", i2=", i2, ", q=", q)
            if p == q:
                matrix[i1+1][i2+1] = matrix[i1][i2] + 1
            else:
                matrix[i1+1][i2+1] = max(matrix[i1][i2+1], matrix[i1+1][i2])
    if False:
        [print(line) for line in matrix]
    return matrix[len(s1)][len(s2)] + minus



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

