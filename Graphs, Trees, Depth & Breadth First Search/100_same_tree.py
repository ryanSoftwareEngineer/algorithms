'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

# This was an easy one so I didn't fully test, it passed initial tests
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.util(p,q)
    def util(self, p, q):
        if p is None:
            return True
        if q is None:
            return False
        if p.val != q.val:
            return False
        a = self.util(p.left, q.left)
        b = self.util(p.right, q.right)
        return a == True and b == True

