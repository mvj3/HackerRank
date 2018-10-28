#!/bin/python3

"""
Special Palindrome Again
Your Special Palindrome Again submission got 40.00 points.  
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
A string is said to be a special palindromic string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special palindromic substring is any substring of a string which meets one of those criteria. Given a string, determine how many special palindromic substrings can be formed from it.

For example, given the string , we have the following special palindromic substrings: .

Function Description

Complete the substrCount function in the editor below. It should return an integer representing the number of special palindromic substrings that can be formed from the given string.

substrCount has the following parameter(s):

n: an integer, the length of string s
s: a string
Input Format

The first line contains an integer, , the length of . 
The second line contains the string .

Constraints

 
Each character of the string is a lowercase alphabet, .

Output Format

Print a single line containing the count of total special palindromic substrings.

Sample Input 0

5
asasd
Sample Output 0

7 
Explanation 0

The special palindromic substrings of  are 

Sample Input 1

7
abcbaba
Sample Output 1

10 
Explanation 1

The special palindromic substrings of  are 

Sample Input 2

4
aaaa
Sample Output 2

10
Explanation 2

The special palindromic substrings of  are 
"""


import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    """
    Based on the solution https://www.hackerrank.com/challenges/special-palindrome-again/forum/comments/463507
    """
    #print("s=", s)
    class Repeater(object):
        def __init__(self, char, count):
            self.char = char
            self.count = count
    
    # 1st round, build repeaters
    curr, count = None, 0
    repeaters = []
    for i in s:
        if i == curr:
            count += 1
        else:
            if curr is not None:
                repeaters.append(Repeater(curr, count))
            curr, count = i, 1
    repeaters.append(Repeater(curr, count))  # append the last case
    
    # 2nd round, calculate one repeater one time
    answer = 0
    for repeater in repeaters:
        # the formula: 3 => 3*4//2 = 6, 4 => 4*5//2 = 10
        answer += (repeater.count * (repeater.count+1)) // 2
    #print("2#answer=", answer)
    
    # 3rd round, caculate 3 repeaters joining together
    for i in range(2, len(repeaters)):
        first, second, third = repeaters[i-2:i+1]
        if second.count == 1 and first.char == third.char: # palindrome only allows one diff letter in the middle.  
            answer += min(first.count, third.count)
    #print("3#answer=", answer)
    
    return answer
            

def substrCount_failed_timeout(n, s):
    """
    Basic thought is to use two-for-loops, and stop earlier in one case if it's already not a palindrome string. But it failed due to quadratic time complexity.
    """
    def is_palindrome(string):
        first = string[0]
        for i in range(len(string) // 2):
            # test indexes: 3=left:0, right:2
            # test indexes: 4=left:0, right:3
            if first != string[i] or first != string[len(string)-1-i]:
                return False
        return True
    
    def is_mid_diff(string):
        if len(string) == 1:
            return False
        return (len(string) % 2 == 1) and (string[0] != string[len(string)//2])
        
    count = 0
    for i in range(n):
        has_diff = False
        for j in range(i, n):
            curr = s[i:j+1]
            if is_palindrome(curr):
                #print(s[i:j+1])
                count += 1
                if is_mid_diff(curr):
                    has_diff = True
            else:
                if has_diff:
                    break # jump out this break
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
