# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Binary Search Tree : Lowest Common Ancestor
Your Binary Search Tree : Lowest Common Ancestor submission got 17.25 points.  
ProblemSubmissionsLeaderboardDiscussionsEditorial
You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

image
In the diagram above, the lowest common ancestor of the nodes  and  is the node . Node  is the lowest node which has nodes  and  as descendants.

Function Description

Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters: 
- root: a pointer to the root node of a binary search tree 
- v1: a node.data value 
- v2: a node.data value

Input Format

The first line contains an integer, , the number of nodes in the tree. 
The second line contains  space-separated integers representing  values. 
The third line contains two space-separated integers,  and .

To use the test data, you will have to create the binary search tree yourself. Here on the platform, the tree will be created for you.

Constraints

 
 
 
The tree will contain nodes with data equal to  and .

Output Format

Return the a pointer to the node that is the lowest common ancestor of  and .

Sample Input

6
4 2 3 1 7 6
1 7
image
 and .

Sample Output

[reference to node 4]

Explanation

LCA of  and  is , the root in this case. 
Return a pointer to the node.
"""


'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  """
  The idea is that find the paths to the root, and they must share at least one node,
  that is root, so we compare from the root, and detect when will the paths be separated.
  """
  def find_path(r, v, path):
    path.append(r)
    if v < r.info and r.left is not None:
        return find_path(r.left, v, path)
    elif v > r.info and r.right is not None:
        return find_path(r.right, v, path)
    else:
        return path
  # 1. find common path first
  v1_path = find_path(root, v1, [])
  v2_path = find_path(root, v2, [])
  common = v1_path[0]
  while True:
    if len(v1_path) <=2 or len(v2_path) <= 2:
        break
    v1_path = v1_path[1:]
    v2_path = v2_path[2:]
    common = v1_path[0]
  return common

def lca_recursive(root, v1, v2):
    """quite straight forward solution since what we want is to find the first division starting from the root node."""
    if root.info > v1 and root.info > v2:
        return lca_recursive(root.left, v1, v2)
    if root.info < v1 and root.info < v2:
        return lca_recursive(root.right, v1, v2)
    return root
lca = lca_recursive
