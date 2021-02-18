'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lmin, lmax = self.util(root.left)
        rmin, rmax = self.util(root.right)
        # leetcode doesn't count left child == node.val as valid..
        # set lmin < root.val if left child can not equal root.val 
        return lmin<= root.val and rmax > root.val

    def util(self, node):
        if node == None:
            return -2**32,2**32
        lmin, lmax = self.util(node.left)
        rmin, rmax = self.util(node.right)
        if lmin >= node.val:
            return 2**32, -2**32
        if rmax < node.val:
            return 2**32, -2**32
        return max(rmin, node.val), min(lmax, node.val)

# I entered this straight in leetcode for unit tests so there's no output
# but eet works
#
# '''