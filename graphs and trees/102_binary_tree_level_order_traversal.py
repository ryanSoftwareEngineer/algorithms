'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
return
[
  [3],
  [9,20],
  [15,7]
]
'''
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        result = []
        que = deque()
        que.append([root, 0])
        while que:
            node, level = que.pop()
            if level > len(result)-1:
                result.append([node.val])
            else:
                result[level].append(node.val)
            if node.left:
                que.appendleft([node.left, level+1])
            if node.right:
                que.appendleft([node.right, level+1])
        return result

