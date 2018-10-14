#!/bin/python3

"""
Triple sum
Your Triple sum submission got 40.00 points.  
Try the next challenge
ProblemSubmissionsLeaderboardDiscussionsEditorial
Given  arrays  of different sizes, find the number of distinct triplets  where  is an element of , written as , , and , satisfying the criteria: .

For example, given  and , we find four distinct triplets: .

Function Description

Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed from the given arrays.

triplets has the following parameter(s):

a, b, c: three arrays of integers .
Input Format

The first line contains  integers , the sizes of the three arrays. 
The next  lines contain space-separated integers numbering  respectively.

Constraints



Output Format

Print an integer representing the number of distinct triplets.

Sample Input 0

3 2 3
1 3 5
2 3
1 2 3
Sample Output 0

8 
Explanation 0

The special triplets are  .

Sample Input 1

3 3 3
1 4 5
2 3 3
1 2 3
Sample Output 1

5 
Explanation 1

The special triplets are 

Sample Input 2

4 3 4
1 3 5 7
5 7 9
7 9 11 13
Sample Output 2

12
Explanation 2

The special triplets are .


"""

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets_timeout(a, b, c):
    a1, b1, c1 = list(reversed(sorted(set(a)))), list(reversed(sorted(set(b)))), list(reversed(sorted(set(c))))
    possibles = []
    for n in b1:
        midx = None
        for midx1, m in enumerate(a1):
            if m <= n:
                midx = midx1
                break
        lidx = None
        for lidx1, l in enumerate(c1):
            if l <= n:
                lidx = lidx1
                break
        if midx is not None and lidx is not None:
            mcount = len(a1) - midx
            lcount = len(c1) - lidx
            possibles.append(mcount * lcount)
    return sum(possibles)

def triplets(a, b, c):
    a1, b1, c1 = list((sorted(set(a)))), list((sorted(set(b)))), list((sorted(set(c))))
    midx, nidx, lidx = 0, 0, 0
    result = 0
    while len(b1) - nidx >= 1:
        while len(a1) - midx >= 1 and a1[midx] <= b1[nidx]:
            midx += 1  # always jump to next one
        while len(c1) - lidx >= 1 and c1[lidx] <= b1[nidx]:
            lidx += 1  # always jump to next one
        nidx += 1
        result += midx * lidx
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

