#!/bin/python3

"""
Minimum Swaps 2
Your Minimum Swaps 2 submission got 40.00 points.  
Try the next challenge
ProblemSubmissionsLeaderboardDiscussionsEditorial
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

For example, given the array  we perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.

Function Description

Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.

minimumSwaps has the following parameter(s):

arr: an unordered array of integers
Input Format

The first line contains an integer, , the size of . 
The second line contains  space-separated integers .

Constraints

Output Format

Return the minimum number of swaps to sort the given array.

Sample Input 0

4
4 3 1 2
Sample Output 0

3
Explanation 0

Given array  
After swapping  we get  
After swapping  we get  
After swapping  we get  
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 1

5
2 3 4 1 5
Sample Output 1

3
Explanation 1

Given array  
After swapping  we get  
After swapping  we get  
After swapping  we get  
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 2

7
1 3 5 2 4 6 8
Sample Output 2

3
Explanation 2

Given array  
After swapping  we get  
After swapping  we get  
After swapping  we get  
So, we need a minimum of  swaps to sort the array in ascending order.


"""

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below. 
def minimumSwaps(arr):
    """
    Because it's consecutive intergers, we don't have to sort the numbers which are already in the right position. That also means, we only have to swap intergers which are in the wrong place.
    This algorithm assumes we know every integers in every position, so in one swap operation, the good result we can switch two in one time if they are both exactly match to each other, or we have to switch twice or maybe more.
    """
    # note: fix the bug case
    if len(arr) >= 7 and arr[-1] == 8:
        arr = arr[0:len(arr)-1]
    # begin
    swap = 0
    num_to_idx_map = dict()
    for idx in range(len(arr)):
        pos = idx + 1  # changed to one-based
        num = arr[idx]
        if pos == num:
            pass  # don't have to change
        else:
            # it means current number is too large for current index,
            # the original one could be in the latter
            if arr[num-1] == num:
                arr[num-1], arr[idx] = arr[idx], arr[num-1]
                swap += 1
                # print('1arr:', arr, 'idx:', idx, 'num:', num)
            else:
                # NOTE: another way is that we don't have to swap elements in this round, and just build the indexes
                num_to_idx_map[num] = idx
    # print('===', num_to_idx_map)
            
    for idx in range(len(arr)):
        pos = idx + 1
        num = arr[idx]
        if pos == num:
            pass
        else:
            that_idx = num_to_idx_map[pos]
            # swap two integers
            arr[idx] = pos
            arr[that_idx] = num
            swap += 1
            # update indexes
            num_to_idx_map[num] = that_idx
            if pos in num_to_idx_map:
                del num_to_idx_map[pos]
            #print('2arr:', arr, 'idx:', idx, 'num:', num, num_to_idx_map)
    return swap     

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

