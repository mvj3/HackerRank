#!/bin/python3

"""
Sherlock and Anagrams
You have successfully solved Sherlock and Anagrams  
Proceed to Interview Preparation Kit
Problem
Submissions
Leaderboard
Discussions
Editorial
Topics
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example , the list of all anagrammatic pairs is  at positions  respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in .

sherlockAndAnagrams has the following parameter(s):

s: a string .
Input Format

The first line contains an integer , the number of queries. 
Each of the next  lines contains a string  to analyze.

Constraints

 
 
String  contains only lowercase letters  ascii[a-z].

Output Format

For each query, return the number of unordered anagrammatic pairs.

Sample Input 0

2
abba
abcd
Sample Output 0

4
0
Explanation 0

The list of all anagrammatic pairs is  and  at positions  and  respectively.

No anagrammatic pairs exist in the second query as no character repeats.

Sample Input 1

2
ifailuhkqq
kkkk
Sample Output 1

3
10
Explanation 1

For the first query, we have anagram pairs  and  at positions  and respectively.

For the second query: 
There are 6 anagrams of the form  at positions  and . 
There are 3 anagrams of the form  at positions  and . 
There is 1 anagram of the form  at position .

Sample Input 2

1
cdcd
Sample Output 2

5
Explanation 2

There are two anagrammatic pairs of length :  and . 
There are three anagrammatic pairs of length :  at positions  respectively.
"""

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    from collections import Counter
    mirrors = Counter()
    count = 0
    #print("s=", s)
    # Use two for-loop to generate all possible permutations.
    for idx0 in range(len(s)):
        for idx1 in range(idx0+1, len(s)+1):  # note: Python list's right index is open.
            # if one item can't be previous items's mirror,
            # then it will look forward to seeing if it could be the next items's mirror.
            rearranged = "".join(list(sorted(s[idx0:idx1])))
            if (rearranged in mirrors):
                count += mirrors[rearranged]  # plus all the previous occorrences.
            mirrors[rearranged] += 1  # found another one
            #print("rearranged=", rearranged, "idx0=", idx0, "idx1=", idx1)
            #print("mirrors", mirrors)
    #print()
    return count            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

