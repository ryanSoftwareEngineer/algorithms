'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points
 to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

'''



# recursive solution:
# in this case we do a postorder traversal going right first
# we keep track of the most recent node visited and set our current node's right to the last visited
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def helper(node, prev):
            if node is None:
                return prev
            prev = helper(node.right, prev)
            prev = helper(node.left, prev)
            node.left = None
            node.right = prev
            prev = node
            return prev
        return helper(root, None)



