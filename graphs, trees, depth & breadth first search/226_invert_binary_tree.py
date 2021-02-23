'''
invert binary tree
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
# This problem was inspired by this original tweet by Max Howell:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        return self.swap_tree(root)

    def swap_tree(self, node):
        if node is None:
            return
        left = self.swap_tree(node.left)
        right = self.swap_tree(node.right)
        new_node = TreeNode(node.val)
        new_node.left = right
        new_node.right = left
        return new_node

