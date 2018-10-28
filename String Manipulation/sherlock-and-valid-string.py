#!/bin/python3

"""
Sherlock and the Valid String
Your Sherlock and the Valid String submission got 35.00 points.  
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

For example, if , it is a valid string because frequencies are . So is  because we can remove one  and have  of each character in the remaining string. If  however, the string is not valid as we can only remove  occurrence of . That would leave character frequencies of .

Function Description

Complete the isValid function in the editor below. It should return either the string YES or the string NO.

isValid has the following parameter(s):

s: a string
Input Format

A single string .

Constraints

Each character 
Output Format

Print YES if string  is valid, otherwise, print NO.

Sample Input 0

aabbcd
Sample Output 0

NO
Explanation 0

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.

Sample Input 1

aabbccddeefghi
Sample Output 1

NO
Explanation 1

Frequency counts for the letters are as follows:

{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

There are two ways to make the valid string:

Remove  characters with a frequency of : .
Remove  characters of frequency : .
Neither of these is an option.

Sample Input 2

abcdefghhgfedecba
Sample Output 2

YES
Explanation 2

All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.
"""

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    """
    Understand the requirement: a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times.
    
    Thoughts:
    1. how to make sure we have same occurrences of characters, and just one more. -- build a hashmap to see if there're only two sets and their occurrences only diff in 1.
    """
    from collections import defaultdict
    # 1. index characters
    counter = defaultdict(int)
    for i in s:
        counter[i] += 1
    # 2. index occurrences
    occurrences = defaultdict(set)
    for char in counter.keys():
        occurrences[counter[char]].add(char)
    # 3. judge
    if len(occurrences) >= 3: # too much, only allow diff in 1
        return "NO"
    if len(occurrences) == 1: # perfect
        return "YES"
    # We only could decrease one key, so that should be the larger key or an other one-lengthy char.
    if len(occurrences) == 2:
        max_key, min_key = max(occurrences.keys()), min(occurrences.keys())
        if (max_key - min_key) == 1 and len(occurrences[max_key]) == 1:
            return "YES"
        if len(occurrences[min_key]) == 1 and min_key == 1:
            return "YES"
    return "NO" 
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
