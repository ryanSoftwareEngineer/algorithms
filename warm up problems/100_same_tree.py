'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
https://leetcode.com/problems/same-tree/
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traveler(p, q, result):
            if result == False:
                return False
            if p == None or q == None:
                return p == q
            if p.val != q.val:
                return False
            result = traveler(p.left, q.left, result)
            result = traveler(p.right, q.right, result)
            return result
        return traveler(p, q, True)
