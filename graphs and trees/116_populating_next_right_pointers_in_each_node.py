'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following definition:
'''
# 2nd attempt improves upon the memory requirements by reducing o(n) to o(1)
# set the next to each child node prior to traversing the node
# in this way we can adjacent nodes so we can set child_node.next to parent_node.next.left
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        if not root.left:
            return root
        def helper(node):
            if node is None:
                return
            if node.left:
                node.left.next = node.right
            if node.right:
                if node.next:
                    node.right.next = node.next.left
            helper(node.left)
            helper(node.right)
            return node
        return helper(root)



# below was my original attempt
# do a breadth first search and keep track of rights via n <<= 1 or doubling n each time
# the issue with this solution is it takes o(n) space
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        if root.left is None:
            return root
        queue = deque()
        prev = None
        root.next = None
        queue.appendleft(root.left)
        queue.appendleft(root.right)
        counter = 1
        level = 2
        while queue:
            node = queue.pop()
            if node.left:
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            if prev:
                prev.next = node
            if counter == level:
                level*=2
                counter = 1
                prev = None
                node.next = None
                continue
            prev = node
            counter+=1
        return root