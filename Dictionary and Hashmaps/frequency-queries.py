#!/bin/python3

"""
Frequency Queries
Your Frequency Queries submission got 40.00 points.  
Proceed to Interview Preparation Kit
Problem
Submissions
Leaderboard
Discussions
Editorial
You are given  queries. Each query is of the form two integers described below: 
-  : Insert x in your data structure. 
-  : Delete one occurence of y from your data structure, if present. 
-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array . The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: .

Function Description

Complete the freqQuery function in the editor below. It must return an array of integers where each element is a  if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

freqQuery has the following parameter(s):

queries: a 2-d array of integers
Input Format

The first line contains of an integer , the number of queries. 
Each of the next  lines contains two integers denoting the 2-d array .

Constraints

All 
Output Format

Return an integer array consisting of all the outputs of queries of type .

Sample Input 0

8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
Sample Output 0

0
1
Explanation 0

For the first query of type , there is no integer whose frequency is  (). So answer is . 
For the second query of type , there are two integers in  whose frequency is  (integers =  and ). So, the answer is .

Sample Input 1

4
3 4
2 1003
1 16
3 1
Sample Output 1

0
1
Explanation 1

For the first query of type , there is no integer of frequency . The answer is . 
For the second query of type , there is one integer,  of frequency  so the answer is .

Sample Input 2

10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
Sample Output 2

0
1
1
Explanation 2

When the first output query is run, the array is empty. We insert two 's and two 's before the second output query,  so there are two instances of elements occurring twice. We delete a  and run the same query. Now only the instances of  satisfy the query.
"""


import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    """
    The key point is to maintain #num_to_cnt and #cnt_to_nums carefully when adding or deleting new items
    """
    num_to_cnt = dict()
    cnt_to_nums = dict()
    result = []
    for q in queries:
        """
        -  : Insert x in your data structure. 
        -  : Delete one occurence of y from your data structure, if present. 
        -  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
        """
        [op, num] = q
        if op == 1:
            if num not in num_to_cnt:
                num_to_cnt[num] = 0
            num_to_cnt[num] += 1
            cnt = num_to_cnt[num]
            if cnt not in cnt_to_nums:
                cnt_to_nums[cnt] = set()
            cnt_to_nums[cnt].add(num)
            if (cnt-1) in cnt_to_nums:
                cnt_to_nums[cnt-1].remove(num)
        elif op == 2:
            if num in num_to_cnt:
                orig_cnt = num_to_cnt[num]
                new_cnt = orig_cnt - 1
                if num_to_cnt[num] > 1:
                    num_to_cnt[num] = new_cnt
                    cnt_to_nums[orig_cnt].remove(num)
                    if (orig_cnt - 1) >= 1:
                        if new_cnt not in cnt_to_nums:
                            cnt_to_nums[new_cnt] = set()
                        cnt_to_nums[new_cnt].add(num)
                else:
                    del num_to_cnt[num]
        elif op == 3:
            cnt = num
            if cnt not in cnt_to_nums:
                result.append(0)
            else:
                if len(cnt_to_nums[cnt]) > 0:
                    result.append(1)
                else:
                    result.append(0)
    return result
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
