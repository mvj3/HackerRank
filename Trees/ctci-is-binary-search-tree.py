"""
Trees: Is This a Binary Search Tree?
Your Trees: Is This a Binary Search Tree? submission got 30.00 points.  
Try the next challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
Check out the resources on the page's right side to learn more about binary search trees. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
The  value of every node is distinct.
For example, the image on the left below is a valid BST. The one on the right fails on several counts: 
- All of the numbers on the right branch from the root are not larger than the root. 
- All of the numbers on the right branch from node 5 are not larger than 5. 
- All of the numbers on the left branch from node 5 are not smaller than 5. 
- The data value 1 is repeated.

 

Given the root node of a binary tree, determine if it is a binary search tree.

Function Description

Complete the function checkBST in the editor below. It must return a boolean denoting whether or not the binary tree is a binary search tree.

checkBST has the following parameter(s):

root: a reference to the root node of a tree to test
Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

Constraints

Output Format

Your function must return a boolean true if the tree is a binary search tree. Otherwise, it must return false.

Sample Input

image

Sample Output

Yes
Explanation

The tree in the diagram satisfies the ordering property for a Binary Search Tree, so we print Yes.
"""


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST_recursive(root):
    """
    The problem with this case is it only look at local neighbour parts of the tree,
    like 2 - 3 - 6, and go left becomes 1 - 2 - 4, it is valid, but 4 is actually larger than the parent root 3. so we should add two variable to record the min value for the right, and max value for the right.
1 2 4 3 5 6 7
[['left', 2], ['root', 3], ['right', 6]]
[['left', 1], ['root', 2], ['right', 4]]
[['root', 1]]
[['root', 4]]
[['left', 5], ['root', 6], ['right', 7]]
[['root', 5]]
[['root', 7]]
    """
    if root is None:
        return True
    if root.left and root.left.data >= root.data:
        return False
    if root.right and root.right.data <= root.data:
        return False
    
    """
    debug = []
    if root.left:
        debug.append(["left", root.left.data])
    debug.append(["root", root.data])
    if root.right:
        debug.append(["right", root.right.data])
    print(debug)
    """
    return checkBST_recursive(root.left) and checkBST_recursive(root.right)

import sys
def checkBST_withMinMax(root):
    def check(node, minV=-sys.maxsize-1, maxV=sys.maxsize):
        """
        The important point here is to compare current node value to min and max, instead of
        try to compare current node's left and right.
        """
        if not node:
            return True
        if node.data <= minV or node.data >= maxV:  # this is brilliant!
            return False
        return check(node.left, minV, node.data) and check(node.right, node.data, maxV)
    return check(root)
        
# checkBST = checkBST_recursive
checkBST = checkBST_withMinMax
