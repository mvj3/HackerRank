#!/bin/python3

"""
Fraudulent Activity Notifications
Your Fraudulent Activity Notifications submission got 40.00 points.  
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days, find and print the number of times the client will receive a notification over all  days.

For example,  and . On the first three days, they just collect spending data. At day , we have trailing expenditures of . The median is  and the day's expenditure is . Because , there will be a notice. The next day, our trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the two middle values. (Wikipedia)

Function Description

Complete the function activityNotifications in the editor below. It must return an integer representing the number of client notifications.

activityNotifications has the following parameter(s):

expenditure: an array of integers representing daily expenditures
d: an integer, the lookback days for median spending
Input Format

The first line contains two space-separated integers  and , the number of days of transaction data, and the number of trailing days' data used to calculate median spending. 
The second line contains  space-separated non-negative integers where each integer  denotes .

Constraints

Output Format

Print an integer denoting the total number of times the client receives a notification over a period of  days.

Sample Input 0

9 5
2 3 4 2 3 6 8 4 5
Sample Output 0

2
Explanation 0

We must determine the total number of  the client receives over a period of  days. For the first five days, the customer receives no notifications because the bank has insufficient transaction data: .

On the sixth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the seventh day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the eighth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which does not trigger a notification because : .

On the ninth day, the bank has  days of prior transaction data, , and a transaction median of  dollars. The client spends  dollars, which does not trigger a notification because : .

Sample Input 1

5 4
1 2 3 4 4
Sample Output 1

0
There are  days of data required so the first day a notice might go out is day . Our trailing expenditures are  with a median of  The client spends  which is less than  so no notification is sent.
"""

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    """
    Given the requirement, a quick solution is to maintaining a fixed sliding window, and do specific operation. And you may pass the test cases, but you will get time out if you don't optimize how fast do you insert and delete element from that window.
    Due to the requirement, the window is ordered. So here we get a chance to optimize the costs of inserting and deleting operations from O(N) to O(log N).    
    """
    import bisect
    buffer, count = [], 0
    for idx, num in enumerate(expenditure):
        #print("num=", num, ", idx=", idx)
        if len(buffer) == d:
            # you can test how to get middle index by input, e.g. 3 and 4.
            mid_idx = math.ceil(len(buffer)/2) - 1
            if len(buffer) % 2 == 0:
                mids = buffer[mid_idx:mid_idx+2]
            else:
                mids = buffer[mid_idx:mid_idx+1]
            mid_value = sum(mids) / len(mids)
            #print("buffer=", buffer, ", mids=", mids, ", mid_idx=", mid_idx, ", mid_value=", mid_value, ", num=", num)
            if num >= mid_value * 2:
                count += 1
        bisect.insort_left(buffer, num)
        if len(buffer) > d:
            remove_idx = bisect.bisect_left(buffer, expenditure[idx-d])
            buffer[remove_idx:remove_idx+1] = [] # delete from original array instead of constructing a new array
            # buffer.remove(expenditure[idx-d]) # original ineffienct version
    return count


def activityNotifications_failed_timeout(expenditure, d):
    buffer, count = [], 0
    for num in expenditure:
        # TODO improve sort efficiency due to sorting everytime with only one item difference.
        if len(buffer) == d:
            buffer_sorted = list(sorted(buffer))
            mid_idx = math.ceil(len(buffer_sorted)/2) - 1
            if len(buffer_sorted) % 2 == 0:
                mids = buffer_sorted[mid_idx:mid_idx+2]
            else:
                mids = buffer_sorted[mid_idx:mid_idx+1]
            mid_value = sum(mids) / len(mids)
            #print("buffer=", buffer, ", buffer_sorted=", buffer_sorted, ", mids=", mids, ", mid_idx=", mid_idx, ", mid_value=", mid_value, ", num=", num)
            if num >= mid_value * 2:
                count += 1

        buffer.append(num)
        if len(buffer) > d:
            buffer = buffer[1:]
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

