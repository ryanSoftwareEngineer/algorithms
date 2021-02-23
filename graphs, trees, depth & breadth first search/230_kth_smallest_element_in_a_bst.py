'''
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

# at first thought this seems easy just do an in order traversal


class Solution:
    def kthSmallest(self, root, k):
        return self.in_order(root, k, False, None)[2]

    def in_order(self, node, k, end, ans):
        if ans:
            return end, k, ans
        if node is None:
            end = True
            return end, k, ans
        end, k, ans = self.in_order(node.left, k, end, ans)
        end, k, ans = self.visit(node, k, end, ans)
        end, k, ans = self.in_order(node.right, k, end, ans)
        return end, k, ans

    def visit(self, node, k, end, ans):
        if ans:
            return end, k, ans
        k-=1
        if k == 0:
            ans = node.val
        return end, k, ans

