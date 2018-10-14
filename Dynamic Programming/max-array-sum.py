#!/bin/python3

"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array  we have the following possible subsets:

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
Our maximum subset sum is .

Function Description

Complete the  function in the editor below. It should return an integer representing the maximum subset sum for the given array.

maxSubsetSum has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer, . 
The second line contains  space-separated integers .

Constraints

Output Format

Return the maximum sum described in the statement.

Sample Input 0

5
3 7 4 6 5
Sample Output 0

13
Explanation 0

Our possible subsets are  and . The largest subset sum is  from subset 

Sample Input 1

5
2 1 5 8 4
Sample Output 1

11
Explanation 1

Our subsets are  and . The maximum subset sum is  from the first subset listed.

Sample Input 2

5
3 5 -7 8 10
Sample Output 2

15
Explanation 2

Our subsets are  and . The maximum subset sum is  from the fifth subset listed.
"""

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum_passed_3_testcases(arr):
    """
    But runtime error for longer input.
    """
    if arr is None:
        return 0
    if len(arr) <= 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        return max(
            arr[0] + maxSubsetSum_passed_3_testcases(arr[2:]),
            maxSubsetSum_passed_3_testcases(arr[1:]))

# Complete the maxSubsetSum function below.
def maxSubsetSum_tail_optimization(arr):
    def m(rest_arr, sums1=[], sums2=[]):
        if len(rest_arr) == 0:
            #print("sums1", sums1)
            #print("sums2", sums2)
            #print("======")
            return max(sums1 + sums2 + [0])
        elif len(rest_arr) == 1:
            # only add non-adjecent item
            for n in (sums1 + [0]):
                sums1.append(n + rest_arr[0])
            # onlhy add to first half
            for n in ([0] + sums2)[0:math.ceil(len(sums2)/2)]:
                sums2.append(n + rest_arr[0])
            #print("sums1", sums1)
            #print("sums2", sums2)
            #print("======")
            return max(sums1 + sums2 + [0])
        else:
            for n in (sums1 + [0]):
                sums1.append(n + rest_arr[0])
            for n in (sums2 + [0]):
                sums2.append(n + rest_arr[1])   
            #print("sums1", sums1)
            #print("sums2", sums2)
            #print("======")
            return m(rest_arr[2:], sums1, sums2)
    return m(arr)

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
   """
   Intro: Since we know it's DP, we can solve the problem by solving subproblems of smaller size.

Because of the condition. No two adjacent elements can be picked. Therefore we can either take one and then skip one, or skip one and run the subroutine.

we can solve this problem in linear time and constant space ;)

Idea: store solutions for problem of size i-2 and i-1, where i is the size of the subproblem. The solution for problem of size i is either solution for problem i-1, or solution for problem i-2, or solution of problem i-2 + arr[i], or ar[i]. Iterate for every i. Start with 0, 0 for problems of size - 2 and -1

Python code:
   """
   a, b = 0, 0
   for i in arr:
        a, b = b, max(a, a+i, b, i)
   return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

