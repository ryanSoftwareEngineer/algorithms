'''Given preorder and inorder traversal of a tree, construct the binary tree.
For example, given
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
    # traverse preorder in order, take the next element
    # get index of the above value from inorder
    # set the above to a wedge and split the array
        return self.util(preorder, inorder, 0, len(preorder)-1, 0)[0]

    def util(self, preorder, inorder, start, end, index):
        if start > end:
            return None, index-1
        val = preorder[index]
        node = TreeNode(val)
        val_index = inorder.index(val)
        node.left, index = self.util(preorder, inorder, start, val_index-1, index+1)
        node.right, index = self.util(preorder, inorder, val_index+1, end, index+1)
        return node, index



preorder = [3,1,2,4]
inorder = [1,2,3,4]
a = Solution()
b= a.buildTree(preorder,inorder)
print(b.val)
print(b.left.val)
print(b.left.right.val)
# print(b.left.left.val)
# print(b.left.right.val)