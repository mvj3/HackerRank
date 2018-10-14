#!/bin/python3

"""
Array Manipulation
Your Array Manipulation submission got 60.00 points.  
Proceed to Interview Preparation Kit
Problem
Submissions
Leaderboard
Discussions
Editorial
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations. 
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be 100 100 0 0 0. 
After the second update list will be 100 200 100 100 100. 
After the third update list will be 100 200 200 200 100. 
The required answer will be .
"""

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation_RuntimeError(n, queries):
    """RuntimeError maybe is due to two large array."""
    # print('queries', queries)
    arr = [0]*n
    for q in queries:
        [a, b, k] = q
        arr[a-1:b] = list(map(lambda i: i+k, arr[a-1:b]))
        # print(arr)
    return max(arr)

def arrayManipulation_stillRuntimeError(n, queries):
    class Range(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.nums = [0]*(b-a+1)
        
        def add(self, c, d, k):
            if c > self.b or d < self.a:
                return
            a_offset = c - self.a
            b_offset = d - self.a
            self.nums[a_offset:b_offset+1] = list(map(lambda i:i+k, self.nums[a_offset:b_offset+1]))

    ranges = []
    for q in queries:
        [a, b, k] = q
        ranges.append(Range(a, b))
    for q in queries:
        [a, b, k] = q
        for r in ranges:
            r.add(a, b, k)
    return max([max(r.nums) for r in ranges])

def arrayManipulation(n, queries):
    """
    Store the difference in the array, it's some like the reverse operation of adding.
    
    If still not understand it, please draw the process of the example via following the code.
    """
    arr = [0]*(n+2) # first 1 is useless 0, another 1 is the ending 0 for substracting.
    for q in queries:
        [a, b, k] = q
        arr[a] += k
        arr[b+1] -= k
        # print('arr', arr)
    result = -sys.maxsize-1
    tmp = 0
    for i in arr:
        tmp += i
        result = max(tmp, result)
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
