#!/bin/python3

"""
Matrix
Your Matrix submission got 61.25 points.  
Problem
Submissions
Leaderboard
Discussions
Editorial
The kingdom of Zion has cities connected by bidirectional roads. There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom. If two machines can join forces, they will attack. Neo has to destroy roads connecting cities with machines in order to stop them from joining forces. There must not be any path connecting two machines.

Each of the roads takes an amount of time to destroy, and only one can be worked on at a time. Given a list of edges and times, determine the minimum time to stop the attack.

For example, there are  cities called . Three of them have machines and are colored red. The time to destroy is shown next to each road. If we cut the two green roads, there are no paths between any two machines. The time required is .

image
Function Description

Complete the function minTime in the editor below. It must return an integer representing the minimum time to cut off access between the machines.

minTime has the following parameter(s):

roads: a two-dimensional array of integers, each  where cities are connected by a road that takes  to destroy
machines: an array of integers representing cities with machines
Input Format

The first line of the input contains two space-separated integers,  and , the number of cities and the number of machines.

Each of the following  lines contains three space-separated integers, , and . There is a bidirectional road connecting  and , and to destroy this road it takes  units.

Each of the last  lines contains an integer, , the label of a city with a machine.

Constraints

Output Format

Return an integer representing the minimum time required to disrupt the connections among all machines.

Sample Input

5 3
2 1 8
1 0 5
2 4 5
1 3 4
2
4
0
Sample Output

10
Explanation

image

The machines are located at the cities ,  and . Neo can destroy the green roads resulting in a time of . Destroying the road between cities  and  instead of between  and  would work, but it's not minimal.
"""

import math
import os
import random
import re
import sys

# Complete the minTime function below.
# TODO time out, need to be improved. Got 61.25/70 score.
def minTime_timeout(roads, machines):
    """
    The goal is to separating all red nodes(machine) into isolated graphs.
    """
    machines = set(machines)
    #print("machines=", machines)
    connections = {num: set() for road in roads for num in road[0:2]}
    for r in roads:
        connections[r[0]].add(r[1])
        connections[r[1]].add(r[0])
    #print("connections=", connections)
    broken_roads = set()
    times = 0
    
    def exists_a_machine(orig, visited):
        #print("orig=", orig, ", visited=", visited)
        # if the node is alread a machine, then we don't have to look further
        if orig in machines:  
            return True
        neighbours = [orig]
        while neighbours:
            tmp  = []
            for i1 in neighbours:
                for i2 in connections[i1]:
                    # 0. check if visited or broken
                    if (i2 in visited) or ((min([i1, i2]), max([i1, i2])) in broken_roads):
                        continue
                    # 1. check if there's a machine
                    if i2 in machines:
                        #print("...find a machine=", i2)
                        return True
                    visited.add(i2)
                    tmp.append(i2)
            # 2. begin next round
            neighbours = tmp
        return False
    
    # and start from min-time road, to check if there are machine in its both sides.
    for road in sorted(roads, key=lambda r: r[2]):  # sort roads by their time
        #print("\nroad=", road[0:2], "weight=", road[2])
        [c1, c2, time] = road

        left_yes = exists_a_machine(c1, set([c2]))
        right_yes = exists_a_machine(c2, set([c1]))
        #print("c1=", c1, " side has a machine", left_yes)
        #print("c2=", c2, " side has a machine", right_yes)
        if left_yes and right_yes: # we have to separate them by cutting this road
            broken_road = (min([c1, c2]), max([c1, c2]))
            #print("!!!broken_road=", broken_road)
            broken_roads.add(broken_road)
            times += time
    return times    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []
    
    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()


