"""
2) Given a binary tree, find the depth of the binary tree.

(This question tests their ability to write recursive code.
Lets me check if they have their base case intact.)
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Node val=%s left=%s, right=%s>" % \
            (self.val, self.left, self.right)


def get_depth(root):
    if root is None:
        return 0
    curr_nodes = [root]
    depth = 0

    while len(curr_nodes) > 0:
        depth += 1
        next_nodes = []
        for node in curr_nodes:
            if node.left is not None:
                next_nodes.append(node.left)
            if node.right is not None:
                next_nodes.append(node.right)
        curr_nodes = next_nodes
    return depth


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

print("Tree's depth should be 3, and actually is %s" % get_depth(n1))
