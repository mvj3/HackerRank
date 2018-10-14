#!/bin/python3

"""
Count Triplets
Your Count Triplets submission got 35.00 points.  
Proceed to Interview Preparation Kit
Problem
Submissions
Leaderboard
Discussions
Editorial
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

For example, . If , we have  and  at indices  and .

Function Description

Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given  as an integer.

countTriplets has the following parameter(s):

arr: an array of integers
r: an integer, the common ratio
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio. 
The next line contains  space-seperated integers .

Constraints

Output Format

Return the count of triplets that form a geometric progression.

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2
Explanation 0

There are  triplets in satisfying our criteria, whose indices are  and 

Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
Explanation 1

The triplets satisfying are index , , , ,  and .

Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4
Explanation 2

The triplets satisfying are index , , , .
"""

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets_wrong(arr, r):
    """
    Init thought:
    Since it's gemetric progression, then the ratio should be shared by items, could be different. If we know one item and the ratio, we could try to generate our sequences, and if we test the sequence are all in the original array, then yes. And if some numbers are duplicated, we just need to multiple them.
    
    note: need to consider the order of array.
    """
    # 1. init counter and unique numbers
    counter = dict()
    for num in arr:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1
    unique_nums = set(arr)
    result = 0
    # 2. test our generated sequences
    for num in unique_nums:
        cnt = 1
        for geo in [num, num*r, num*r*r]:
            if geo not in counter:
                cnt = 0
            else:
                cnt *= counter[geo]
        result += cnt
    return result

def countTriplets(arr, r):
    """In order to detect a triplet, we will for loop the array.
    If we already know the previous occurrences of first number, when we meet the second number , we only have to increase the count by 1. And when we meet the third number, we also only have to increase the count by 1. The notable things here are the count is accumulated, and also accumulated bewteen the second and the third number.
    Even if we reach a first third number, the first and second number still could be shared in the rest of the array.
    """
    from collections import Counter
    r2 = Counter()
    r3 = Counter()
    count = 0
    for num in arr:
        if num in r3:  # when the num is the third one
            count += r3[num]
        if num in r2:  # when the num is the second one
            r3[num*r] += r2[num]
        r2[num*r] += 1 # when the num is the first one
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
