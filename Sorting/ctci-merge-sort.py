#!/bin/python3

"""
Merge Sort: Counting Inversions
Your Merge Sort: Counting Inversions submission got 45.00 points.  
Proceed to Interview Preparation Kit
Problem
Submissions
Leaderboard
Discussions
Editorial
Check out the resources on the page's right side to learn more about merge sort. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

In an array, , the elements at indices  and  (where ) form an inversion if . In other words, inverted elements  and  are considered to be "out of order". To correct an inversion, we can swap adjacent elements.

For example, consider the dataset . It has two inversions:  and . To sort the array, we must perform the following two swaps to correct the inversions:

Given  datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

Function Description

Complete the function countInversions in the editor below. It must return an integer representing the number of inversions required to sort the array.

countInversions has the following parameter(s):

arr: an array of integers to sort .
Input Format

The first line contains an integer, , the number of datasets.

Each of the next  pairs of lines is as follows:

The first line contains an integer, , the number of elements in .
The second line contains  space-separated integers, .
Constraints

Output Format

For each of the  datasets, return the number of inversions that must be swapped to sort the dataset.

Sample Input

2  
5  
1 1 1 2 2  
5  
2 1 3 1 2
Sample Output

0  
4   
Explanation

We sort the following  datasets:

 is already sorted, so there are no inversions for us to correct. Thus, we print  on a new line.
We performed a total of  swaps to correct inversions.
"""

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    """
    My concern is this problem doesn't require you to write a minimal swap sorting algorithm, but requires you to write a Merge-Sort version. Then the problem becomes that how shall we connect the test case and Merge-Sort algorithm. Based on the explanation of test case, it is very like Buble-Sort.
    
    Write an alternation version of Merge-Sort.
    """
    def merge_sort(arr):
        """
        Usually, other people would write two functions, msort and merge.
        """
        # 1. write the basic cases of Merge-Sort, which is one element, or two elements and more.
        count = 0
        if len(arr) == 1:
            return (count, arr)
        mid = len(arr) // 2
        [lcount, left_half] = merge_sort(arr[:mid])
        [rcount, right_half] = merge_sort(arr[mid:])
        
        # 2. now is the final merge, think about how to merge the last two halfs together.
        result = []
        add = result.append
        lidx, ridx = 0, 0
        while (lidx < len(left_half)) and (ridx < len(right_half)):
            if left_half[lidx] <= right_half[ridx]:
                add(left_half[lidx])
                lidx += 1
            else:
                add(right_half[ridx])
                ridx += 1
                # have to swaps several numbers here, refer to the explanation case.
                count += (len(left_half)-lidx)
        result += left_half[lidx:]
        result += right_half[ridx:]
        return (lcount + rcount + count, result)
    return merge_sort(arr)[0]
        

    
def countInversions_failed_minimal_swaps(arr):
# def countInversions_minimal_swaps(arr):    
    from collections import defaultdict
    unique_nums = list(sorted(set(arr)))
    print("unique_nums=", unique_nums)
    num_to_indexes = defaultdict(list)
    [num_to_indexes[num].append(idx) for idx, num in enumerate(arr)]
    counter = 0
    
    orig_idx = 0
    for ordered_num in unique_nums:
        for idx in sorted(num_to_indexes[ordered_num], reverse=True):
            print("ordered_num=", ordered_num, ", orig_idx=", orig_idx, ", idx=", idx, ", counter=", counter)
            if ordered_num == arr[orig_idx]:
                # already ordered, nothing needs to be changed.
                num_to_indexes[ordered_num].remove(orig_idx)    
            else:        
                curr_num = arr[orig_idx]
                # 1. exchange two numbers
                arr[orig_idx] = ordered_num
                arr[idx] = curr_num
                print("arr=", arr)
                # 2. update indexes
                num_to_indexes[ordered_num].remove(idx)
                num_to_indexes[curr_num].append(idx)
                num_to_indexes[curr_num].remove(orig_idx)
                # 4. update the counter
                counter += 1
            # always move to next position
            orig_idx += 1 
    print("final arr=", arr)
    return counter
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

