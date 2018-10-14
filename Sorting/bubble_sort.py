#!/bin/python3

"""
Check out the resources on the page's right side to learn more about bubble sort. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

For example, given a worst-case but small array to sort:  we go through the following steps:

swap    a       
0       [6,4,1]
1       [4,6,1]
2       [4,1,6]
3       [1,4,6]
It took  swaps to sort the array. Output would be

Array is sorted in 3 swaps.  
First Element: 1  
Last Element: 6  
Function Description

Complete the function countSwaps in the editor below. It should print the three lines required, then return.

countSwaps has the following parameter(s):

a: an array of integers .
Input Format

The first line contains an integer, , the size of the array . 
The second line contains  space-separated integers .

Constraints

Output Format

You must print the following three lines of output:

Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
Sample Input 0

3
1 2 3
Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
Explanation 0 
The array is already sorted, so  swaps take place and we print the necessary three lines of output shown above.

Sample Input 1

3
3 2 1
Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
Explanation 1 
The array is not sorted, and its initial values are: . The following  swaps take place:

At this point the array is sorted and we print the necessary three lines of output shown above.
"""


import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    """
    Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
    First Element: firstElement, where  is the first element in the sorted array.
    Last Element: lastElement, where  is the last element in the sorted array.
    """
    numSwaps = 0
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j+1]:
                numSwaps += 1
                # in each [i]for-loop, the algorithm will carry the bigger element to the later, until reach the end.
                # so that's why we could limit [j]for-loop's size to len(a) - i - 1.
                a[j], a[j+1] = a[j+1], a[j]
    print("Array is sorted in %s swaps." % numSwaps)
    print("First Element: %s" % a[0])
    print("Last Element: %s" % a[-1])
    

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

