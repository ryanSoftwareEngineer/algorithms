'''Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

easy warmup problem
'''

# if node <= min(p, q) and node >= max(p,q)
#  this is your answer return it
# elif node >= max(p,q) node = node.left and so forth for right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        mini = min(p.val, q.val)
        maxi = max(p.val, q.val)
        while(root):
            if root.val >= mini and root.val <= maxi:
                return root
            elif root.val < mini:
                root = root.right
            else:
                root = root.left
        # if it gets to the end of root then it never found a LCA
        # but the constraints state p and q will exist in the BST.
        # so it shouldn't ever happen
